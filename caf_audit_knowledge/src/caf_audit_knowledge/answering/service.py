from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone

from caf_audit_knowledge.answering.classifier import QueryClassification, RiskAssessment, assess_query_risk, classify_query
from caf_audit_knowledge.answering.prompts import SYSTEM_PROMPT, build_prompt
from caf_audit_knowledge.config import settings
from caf_audit_knowledge.llm import get_completion_provider
from caf_audit_knowledge.retrieval.service import RetrievalService, SearchHit


@dataclass(frozen=True)
class AnswerResult:
    answer: str
    classification: QueryClassification
    risk: RiskAssessment
    evidence: list[SearchHit]
    conflict: dict
    explain_log: dict


class AnswerService:
    def __init__(self) -> None:
        self.retrieval = RetrievalService()
        try:
            self.llm = get_completion_provider()
        except Exception:
            self.llm = None

    def _write_query_log(self, payload: dict) -> None:
        settings.ledger_root.mkdir(parents=True, exist_ok=True)
        with settings.query_logs_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(payload, ensure_ascii=False) + "\n")

    def _top_k_for(self, classification: QueryClassification, risk: RiskAssessment) -> int:
        top_k = settings.answer_top_k_default
        if classification.query_type in {"summary", "aggregation", "evidential", "recommendation", "legal_reference"}:
            top_k = settings.answer_top_k_expanded
        if "hierarchical" in classification.facets:
            top_k = max(top_k, settings.answer_top_k_default + 2)
        if risk.safe_mode:
            top_k += settings.safe_mode_top_k_bonus
        return top_k

    def _subscope_markers(self, query: str) -> list[str]:
        lowered = query.casefold()
        markers: list[str] = []
        for match in re.finditer(r"\bachado\s+([1-4]\.\d+)\b", lowered):
            markers.extend([match.group(1), f"achado {match.group(1)}"])
        subachado_match = re.search(r"\bsubachado\s+(\d+)\s+do\s+achado\s+([1-4])\b", lowered)
        if subachado_match:
            sub, ach = subachado_match.groups()
            markers.extend([f"subachado {sub}", f"achado {ach}.{sub}", f"{ach}.{sub}"])
        return list(dict.fromkeys(markers))

    def _supports_requested_subscope(self, query: str, hits: list[SearchHit]) -> bool:
        markers = self._subscope_markers(query)
        if not markers:
            return True
        for hit in hits:
            haystack = f"{hit.chunk.text}\n{hit.chunk.section_type or ''}".casefold()
            if any(marker in haystack for marker in markers):
                return True
        return False

    def answer(
        self,
        query: str,
        audit_object_id: str | None = None,
        source_types: list[str] | None = None,
    ) -> AnswerResult:
        classification = classify_query(query, llm=self.llm)
        pre_risk = assess_query_risk(query, classification)
        query_context = self.retrieval.classify_query(
            query,
            top_k=self._top_k_for(classification, pre_risk),
            classification=classification,
        )
        hits, conflict, trace = self.retrieval.search_with_trace(
            query=query,
            audit_object_id=audit_object_id,
            source_types=source_types,
            top_k=self._top_k_for(classification, pre_risk),
            query_context=query_context,
        )
        score_margin = 1.0
        if len(hits) >= 2:
            score_margin = max(hits[0].score - hits[1].score, 0.0)
        risk = assess_query_risk(
            query,
            classification,
            result_count=len(hits),
            conflict=conflict["conflict"],
            score_margin=score_margin,
        )
        explain_log = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "query": query,
            "classification": {
                "type": classification.query_type,
                "confidence": classification.confidence,
                "source": classification.source,
                "used_llm_fallback": classification.used_llm_fallback,
                "facets": list(classification.facets),
            },
            "risk": {
                "flags": list(risk.flags),
                "score": risk.score,
                "safe_mode": risk.safe_mode,
            },
            "conflict": conflict,
            "query_context": trace["query_context"],
            "retrieval": trace["retrieval"],
            "rerank": trace["rerank"],
            "scoring": trace["scoring"],
            "final": trace["final"],
        }
        if not hits:
            result = AnswerResult(
                answer="Nenhuma evidência relevante foi recuperada para responder com segurança.",
                classification=classification,
                risk=risk,
                evidence=[],
                conflict=conflict,
                explain_log=explain_log,
            )
            self._write_query_log({"event": "answer", **explain_log, "answer": result.answer, "conflict": conflict})
            return result
        if self.llm is None:
            result = AnswerResult(
                answer="A camada de resposta LLM não está disponível no momento. Use as evidências recuperadas abaixo.",
                classification=classification,
                risk=risk,
                evidence=hits,
                conflict=conflict,
                explain_log=explain_log,
            )
            self._write_query_log({"event": "answer", **explain_log, "answer": result.answer, "conflict": conflict})
            return result
        if "subscope" in classification.facets and not self._supports_requested_subscope(query, hits):
            answer = (
                "Não foi possível isolar com segurança o subachado solicitado a partir das evidências recuperadas. "
                "Os resultados sustentam o achado pai, mas não trazem marcação textual suficiente para confirmar o subnível pedido."
            )
            explain_log["guardrail"] = {
                "triggered": True,
                "reason": "subscope_not_explicit_in_evidence",
            }
            result = AnswerResult(
                answer=answer,
                classification=classification,
                risk=risk,
                evidence=hits,
                conflict=conflict,
                explain_log=explain_log,
            )
            self._write_query_log({"event": "answer", **explain_log, "answer": answer, "conflict": conflict})
            return result
        prompt = build_prompt(query=query, hits=hits, classification=classification, conflict=conflict, risk=risk)
        answer = self.llm.complete(system=SYSTEM_PROMPT, prompt=prompt)
        result = AnswerResult(
            answer=answer,
            classification=classification,
            risk=risk,
            evidence=hits,
            conflict=conflict,
            explain_log=explain_log,
        )
        self._write_query_log({"event": "answer", **explain_log, "answer": answer, "conflict": conflict})
        return result
