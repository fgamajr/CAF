from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from functools import lru_cache

from caf_audit_knowledge.config import settings
from caf_audit_knowledge.llm import CompletionProvider

QUERY_TYPES = (
    "exact_match",
    "aggregation",
    "summary",
    "factual",
    "exploratory",
    "evidential",
    "legal_reference",
    "accountability",
    "recommendation",
)
TOKEN_RE = re.compile(r"\b[\w-]+\b", re.UNICODE)
STOPWORDS = {
    "achado",
    "subachado",
    "quais",
    "quaissao",
    "qual",
    "para",
    "sobre",
    "foram",
    "identificados",
    "explicar",
    "explique",
    "todos",
    "todas",
}
RISK_WEIGHTS = {
    "hierarchical_query": 0.30,
    "subscope_resolution_risk": 0.25,
    "multi_evidence_required": 0.30,
    "entity_resolution_risk": 0.20,
    "aggregation_precision_risk": 0.20,
    "legal_precision_required": 0.15,
    "recommendation_synthesis_risk": 0.20,
    "low_context": 0.20,
    "cross_source_conflict": 0.15,
    "ranking_ambiguity": 0.15,
}


@dataclass(frozen=True)
class QueryClassification:
    query_type: str
    confidence: float
    source: str = "rule"
    used_llm_fallback: bool = False
    facets: tuple[str, ...] = ()


@dataclass(frozen=True)
class RiskAssessment:
    flags: tuple[str, ...]
    score: float
    safe_mode: bool


def _detect_facets(query: str) -> tuple[str, ...]:
    lowered = query.casefold()
    facets: list[str] = []
    if re.search(r"\bsubachado\b", lowered) or re.search(r"\bachado\s+(?:[1-4](?:\.\d+)*|i{1,3}|iv)\b", lowered):
        facets.append("hierarchical")
    if re.search(r"\bsubachado\s+\d+\b", lowered) or re.search(r"\bachado\s+[1-4]\.\d+\b", lowered):
        facets.append("subscope")
    if re.search(r'"[^"]+"', query) or re.search(r"\bach[-_ ]?0?\d+\b", lowered):
        facets.append("exact_reference")
    return tuple(facets)


def _regex_classification(query: str) -> QueryClassification:
    lowered = query.casefold()
    facets = _detect_facets(query)

    if any(token in lowered for token in ["quantos", "quantas", "quantidade", "total", "número de", "numero de", "lista de todos"]):
        return QueryClassification(query_type="aggregation", confidence=0.9, source="rule", facets=facets)

    if any(token in lowered for token in ["resuma", "resumo", "sintese", "síntese", "explique o achado", "explique a seção", "explique a secao"]):
        return QueryClassification(query_type="summary", confidence=0.9, source="rule", facets=facets)

    if any(
        token in lowered
        for token in [
            "evidência",
            "evidencias",
            "evidências",
            "prova",
            "provaram",
            "provar",
            "comprova",
            "comprovam",
            "comprovação",
            "comprovacao",
            "documento",
            "documentos",
            "base documental",
            "base probatória",
            "base probatoria",
            "foi verificado",
        ]
    ):
        return QueryClassification(query_type="evidential", confidence=0.9, source="rule", facets=facets)

    if any(token in lowered for token in ["legislação", "legislacao", "norma", "normas", "lei", "decreto", "portaria", "iso", "tcu nat"]):
        return QueryClassification(query_type="legal_reference", confidence=0.9, source="rule", facets=facets)

    if any(token in lowered for token in ["responsável", "responsavel", "responsabilidade", "quem ficou responsável", "quem ficou responsavel"]):
        return QueryClassification(query_type="accountability", confidence=0.88, source="rule", facets=facets)

    if any(token in lowered for token in ["proposta", "solução", "solucao", "recomendação", "recomendacao", "plano de ação", "plano de acao"]):
        return QueryClassification(query_type="recommendation", confidence=0.88, source="rule", facets=facets)

    if any(token in lowered for token in ["quais são", "quais sao", "qual é", "qual e", "causas", "causa", "efeitos", "efeito", "riscos", "risco"]):
        return QueryClassification(query_type="factual", confidence=0.85, source="rule", facets=facets)

    if re.search(r'"[^"]+"', query) or re.search(r"\bach[-_ ]?0?\d+\b", lowered):
        return QueryClassification(query_type="exact_match", confidence=0.95, source="rule", facets=facets)

    return QueryClassification(query_type="exploratory", confidence=0.6, source="rule", facets=facets)


def _classify_with_llm(query: str, llm: CompletionProvider) -> str:
    system = (
        "Classify audit-retrieval queries. "
        "Return only one label from: exact_match, aggregation, summary, factual, exploratory, evidential, legal_reference, accountability, recommendation."
    )
    prompt = (
        "Classify the query into one of:\n"
        "- exact_match\n"
        "- aggregation\n"
        "- summary\n"
        "- factual\n"
        "- evidential\n"
        "- legal_reference\n"
        "- accountability\n"
        "- recommendation\n"
        "- exploratory\n\n"
        f'Query: "{query}"\n\n'
        "Return only the label."
    )
    label = llm.complete(system=system, prompt=prompt).strip().lower()
    return label if label in QUERY_TYPES else "exploratory"


class AdaptiveQueryClassifier:
    def __init__(self) -> None:
        settings.ledger_root.mkdir(parents=True, exist_ok=True)
        self.pattern_overrides = self._load_patterns()

    def _load_patterns(self) -> dict[str, str]:
        if not settings.query_patterns_path.exists():
            return {}
        payload = json.loads(settings.query_patterns_path.read_text(encoding="utf-8"))
        patterns = payload.get("patterns", {})
        return {
            pattern.casefold(): label
            for pattern, label in patterns.items()
            if label in QUERY_TYPES
        }

    def _save_patterns(self) -> None:
        payload = {
            "version": 1,
            "updated_at": datetime.now(timezone.utc).isoformat(),
            "patterns": dict(sorted(self.pattern_overrides.items())),
        }
        settings.query_patterns_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    def _feedback_rows(self) -> list[dict]:
        if not settings.query_feedback_path.exists():
            return []
        rows = []
        for line in settings.query_feedback_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                rows.append(json.loads(line))
        return rows

    def _match_override(self, query: str) -> QueryClassification | None:
        lowered = query.casefold()
        for pattern, label in sorted(self.pattern_overrides.items(), key=lambda item: (-len(item[0]), item[0])):
            if pattern in lowered:
                return QueryClassification(
                    query_type=label,
                    confidence=0.95,
                    source="learned_pattern",
                    facets=_detect_facets(query),
                )
        return None

    def classify(self, query: str, llm: CompletionProvider | None = None) -> QueryClassification:
        if settings.adaptive_classifier_enabled:
            override = self._match_override(query)
            if override is not None:
                return override

        result = _regex_classification(query)
        if (
            llm is None
            or not settings.classification_llm_fallback_enabled
            or result.confidence >= settings.classification_llm_fallback_threshold
        ):
            return result
        return QueryClassification(
            query_type=_classify_with_llm(query, llm),
            confidence=max(result.confidence, settings.classification_llm_fallback_threshold),
            source="llm",
            used_llm_fallback=True,
            facets=result.facets,
        )

    def register_feedback(
        self,
        *,
        query: str,
        predicted: str,
        correct: str,
        confidence: float,
        source: str,
    ) -> dict[str, str]:
        if correct not in QUERY_TYPES:
            raise ValueError(f"Unsupported query type: {correct}")
        if predicted not in QUERY_TYPES:
            raise ValueError(f"Unsupported predicted query type: {predicted}")

        row = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "query": query,
            "predicted": predicted,
            "correct": correct,
            "confidence": confidence,
            "source": source,
        }
        with settings.query_feedback_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
        learned = self.learn()
        return learned

    def learn(self) -> dict[str, str]:
        rows = self._feedback_rows()
        support: dict[str, Counter] = defaultdict(Counter)
        for row in rows:
            predicted = row.get("predicted")
            correct = row.get("correct")
            query = row.get("query", "")
            if predicted == correct or correct not in QUERY_TYPES:
                continue
            tokens = {
                token.casefold()
                for token in TOKEN_RE.findall(query)
                if len(token) >= settings.adaptive_pattern_min_token_length
                and not token.isdigit()
                and token.casefold() not in STOPWORDS
            }
            for token in tokens:
                support[token][correct] += 1

        learned_patterns: dict[str, str] = {}
        for token, counts in support.items():
            label, count = counts.most_common(1)[0]
            if count >= settings.adaptive_pattern_min_support:
                learned_patterns[token] = label
        self.pattern_overrides = learned_patterns
        self._save_patterns()
        return learned_patterns

    def patterns(self) -> dict[str, str]:
        return dict(sorted(self.pattern_overrides.items()))

    def feedback_history(self, limit: int = 50) -> list[dict]:
        rows = self._feedback_rows()
        return rows[-limit:]


@lru_cache(maxsize=1)
def get_query_classifier() -> AdaptiveQueryClassifier:
    return AdaptiveQueryClassifier()


def classify_query(query: str, llm: CompletionProvider | None = None) -> QueryClassification:
    return get_query_classifier().classify(query, llm=llm)


def assess_query_risk(
    query: str,
    classification: QueryClassification,
    *,
    result_count: int | None = None,
    conflict: bool | None = None,
    score_margin: float | None = None,
) -> RiskAssessment:
    _ = query
    flags: list[str] = []
    if "hierarchical" in classification.facets:
        flags.append("hierarchical_query")
    if "subscope" in classification.facets:
        flags.append("subscope_resolution_risk")
    if classification.query_type in {"aggregation", "summary", "evidential", "recommendation"}:
        flags.append("multi_evidence_required")
    if classification.query_type == "aggregation":
        flags.append("aggregation_precision_risk")
    if classification.query_type == "legal_reference":
        flags.append("legal_precision_required")
    if classification.query_type == "accountability":
        flags.append("entity_resolution_risk")
    if classification.query_type == "recommendation":
        flags.append("recommendation_synthesis_risk")
    if result_count is not None and result_count < 3:
        flags.append("low_context")
    if conflict:
        flags.append("cross_source_conflict")
    if score_margin is not None and score_margin < 0.08:
        flags.append("ranking_ambiguity")
    unique_flags = tuple(dict.fromkeys(flags))
    score = min(sum(RISK_WEIGHTS.get(flag, 0.0) for flag in unique_flags), 1.0)
    return RiskAssessment(
        flags=unique_flags,
        score=round(score, 4),
        safe_mode=score >= settings.risk_safe_mode_threshold,
    )


def register_feedback(
    *,
    query: str,
    predicted: str,
    correct: str,
    confidence: float,
    source: str,
) -> dict[str, str]:
    return get_query_classifier().register_feedback(
        query=query,
        predicted=predicted,
        correct=correct,
        confidence=confidence,
        source=source,
    )
