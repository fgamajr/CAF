from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from sqlalchemy import select

from caf_audit_knowledge.answering.classifier import QueryClassification, assess_query_risk, classify_query
from caf_audit_knowledge.config import settings
from caf_audit_knowledge.constants import LEGAL_TOKEN_RE, SourceType
from caf_audit_knowledge.embeddings.providers import get_embedding_provider
from caf_audit_knowledge.retrieval.elasticsearch_store import ElasticsearchStore
from caf_audit_knowledge.retrieval.reranker import RerankCandidate, get_reranker
from caf_audit_knowledge.retrieval.scoring import get_scoring_policy
from caf_audit_knowledge.retrieval.vector_store import VectorStore
from caf_audit_knowledge.storage.db import get_session
from caf_audit_knowledge.storage.models import ChunkRecord, DocumentRecord

logger = logging.getLogger(__name__)
STACK_TRACE_RE = re.compile(
    r"(traceback \(most recent call last\):|exception in thread|^\s*file \".*\", line \d+, in |\bat\s+\S+\([^)]*:\d+\))",
    re.IGNORECASE | re.MULTILINE,
)
HARD_FILTER_MARKERS: tuple[tuple[str, re.Pattern[str]], ...] = (
    ("debug_marker", re.compile(r"\b(?:bug:|debug:)\b", re.IGNORECASE)),
    ("review_artifact", re.compile(r"\b(?:bugs?\s+identificad[oa]s?|bug\s+adicional|tone check|swarm panel|review panel)\b", re.IGNORECASE)),
    ("adversarial_marker", re.compile(r"\b(?:persona:|chaos-agent|adversarial)\b", re.IGNORECASE)),
    ("stack_trace", STACK_TRACE_RE),
)
LEGAL_SIGNAL_RE = re.compile(LEGAL_TOKEN_RE, re.IGNORECASE)
EVIDENCE_PATTERNS: tuple[tuple[str, re.Pattern[str], float], ...] = (
    ("piece_reference", re.compile(r"\bconforme\s+peça\s*\d+|\bpeça\s*\d+\b", re.IGNORECASE), 0.25),
    ("verified_phrase", re.compile(r"\bfoi\s+verificad[oa]|\bverificou-se\b", re.IGNORECASE), 0.20),
    ("proof_phrase", re.compile(r"\bcomprovad[oa]|\bcomprova\b|\bcomprovam\b|\bcomprovação\b|\bcomprovacao\b", re.IGNORECASE), 0.20),
    ("document_phrase", re.compile(r"\bdocumento\s+analisado|\bdocumentos?\s+analisad[oa]s?\b", re.IGNORECASE), 0.15),
    ("annex_phrase", re.compile(r"\banexo\b|\banexos\b", re.IGNORECASE), 0.10),
    ("table_phrase", re.compile(r"\btabela\b|\bquadro\b", re.IGNORECASE), 0.10),
    ("record_phrase", re.compile(r"\bregistro\b|\bregistros\b|\bbase\s+de\s+dados\b", re.IGNORECASE), 0.10),
)


@dataclass(frozen=True)
class SearchHit:
    chunk: ChunkRecord
    score: float
    score_breakdown: dict[str, object]
    reasons: list[str]


@dataclass(frozen=True)
class QueryContext:
    query_type: str
    query_facets: tuple[str, ...]
    has_exact_match: bool
    exact_term: str | None
    preferred_section_types: tuple[str, ...]
    candidate_limit: int
    risk_flags: tuple[str, ...]
    risk_score: float
    safe_mode: bool


class RetrievalService:
    def __init__(self) -> None:
        self.es = ElasticsearchStore()
        self.vectors = VectorStore()
        try:
            self.embedding_provider = get_embedding_provider()
        except Exception as exc:
            logger.warning("Embedding provider unavailable for query-time vector search: %s", exc)
            self.embedding_provider = None
        try:
            self.reranker = get_reranker() if settings.reranker_enabled else None
        except Exception as exc:
            logger.warning("Reranker unavailable for query-time reranking: %s", exc)
            self.reranker = None

    def detect_scope(self, query: str, audit_object_id: str | None = None) -> str | None:
        if audit_object_id:
            return audit_object_id
        match = re.search(r"\bACH[-_ ]?0?([1-4])\b", query, re.IGNORECASE)
        if match:
            return f"ACH0{int(match.group(1))}"
        achado_numeric = re.search(r"\bachado\s+([1-4])(?:\.\d+)*\b", query, re.IGNORECASE)
        if achado_numeric:
            return f"ACH0{int(achado_numeric.group(1))}"
        achado_roman = re.search(r"\bachado\s+(i{1,3}|iv)\b", query, re.IGNORECASE)
        if achado_roman:
            roman = achado_roman.group(1).upper()
            roman_lookup = {"I": "ACH01", "II": "ACH02", "III": "ACH03", "IV": "ACH04"}
            return roman_lookup.get(roman)
        return None

    def classify_query(
        self,
        query: str,
        top_k: int,
        classification: QueryClassification | None = None,
    ) -> QueryContext:
        classification = classification or classify_query(query)
        lowered = query.casefold()
        exact_match = re.search(r'"([^"]+)"', query)
        ach_match = re.search(r"\bACH[-_ ]?0?([1-4])\b", query, re.IGNORECASE)
        achado_numeric = re.search(r"\bachado\s+([1-4])(?:\.\d+)*\b", query, re.IGNORECASE)
        law_match = re.search(r"\blei\s*n?[ºo]?\s*\d[\d\./-]*", query, re.IGNORECASE)
        exact_term = None
        if exact_match:
            exact_term = exact_match.group(1)
        elif ach_match:
            exact_term = f"ACH0{int(ach_match.group(1))}"
        elif achado_numeric:
            exact_term = f"ACH0{int(achado_numeric.group(1))}"
        elif law_match:
            exact_term = law_match.group(0)

        query_type = classification.query_type
        preferred_section_types: tuple[str, ...] = ()
        candidate_limit = max(top_k, settings.reranker_candidate_k)
        if query_type == "aggregation":
            preferred_section_types = ("sintese", "tabela", "efeito", "causa")
            candidate_limit = max(candidate_limit, 80)
        elif query_type == "summary":
            preferred_section_types = ("sintese", "causa", "efeito", "risco", "tabela")
            candidate_limit = max(candidate_limit, 60)
        elif query_type == "evidential":
            preferred_section_types = ("tabela", "sintese", "causa", "efeito")
            candidate_limit = max(candidate_limit, 70)
        elif query_type == "legal_reference":
            preferred_section_types = ("sintese", "tabela")
            candidate_limit = max(candidate_limit, 60)
        elif query_type == "accountability":
            preferred_section_types = ("efeito", "risco", "sintese")
            candidate_limit = max(candidate_limit, 55)
        elif query_type == "recommendation":
            preferred_section_types = ("sintese", "efeito", "risco")
            candidate_limit = max(candidate_limit, 70)
        elif any(token in lowered for token in ["causa", "causas"]):
            preferred_section_types = ("causa", "sintese")
            candidate_limit = max(candidate_limit, 60)
        elif any(token in lowered for token in ["efeito", "efeitos", "impacto", "impactos", "risco", "riscos"]):
            preferred_section_types = ("efeito", "risco", "sintese")
            candidate_limit = max(candidate_limit, 60)
        if "hierarchical" in classification.facets:
            candidate_limit = max(candidate_limit, 70)
        risk = assess_query_risk(query, classification)
        if risk.safe_mode:
            candidate_limit = max(candidate_limit, top_k + settings.safe_mode_top_k_bonus, 70)
        return QueryContext(
            query_type=query_type,
            query_facets=classification.facets,
            has_exact_match=exact_term is not None,
            exact_term=exact_term,
            preferred_section_types=preferred_section_types,
            candidate_limit=candidate_limit,
            risk_flags=risk.flags,
            risk_score=risk.score,
            safe_mode=risk.safe_mode,
        )

    def _hard_filter_reasons(self, chunk: ChunkRecord, document: DocumentRecord | None) -> list[str]:
        haystack = "\n".join(
            part
            for part in [
                chunk.text,
                chunk.section_type or "",
                document.title if document else "",
                document.source_path if document else "",
            ]
            if part
        )
        reasons = [label for label, pattern in HARD_FILTER_MARKERS if pattern.search(haystack)]
        if (chunk.section_type or "").lower() == "debug":
            reasons.append("debug_section")
        return sorted(set(reasons))

    def _policy_adjustments(
        self,
        chunk: ChunkRecord,
        document: DocumentRecord | None,
        query_context: QueryContext,
        *,
        entity_signal: float,
        evidence_signal: float,
    ) -> tuple[float, list[str]]:
        score = 1.0
        reasons: list[str] = []
        section_type = (chunk.section_type or "body").lower()
        text_casefold = chunk.text.casefold()
        title_casefold = (document.title or "").casefold() if document else ""
        metadata_types = {section_type, chunk.source_type.casefold()}

        if metadata_types.intersection({"debug", "analysis"}):
            score *= 0.6
            reasons.append("penalized: debug/analysis metadata")
        if section_type == "toc":
            score *= 0.7
            reasons.append("penalized: toc")
        if "persona:" in text_casefold or "chaos-agent" in text_casefold or "review panel" in title_casefold:
            score *= 0.7
            reasons.append("penalized: adversarial/debug context")
        if section_type in {"intro", "metodologia", "boilerplate"}:
            score *= 0.85
            reasons.append(f"penalized: {section_type}")
        if entity_signal < 0.2:
            score *= 0.9
            reasons.append("penalized: low entity density")
        if query_context.query_type == "evidential":
            if section_type in {"metodologia", "procedimento", "abordagem"}:
                score *= 0.6
                reasons.append("penalized: methodology_section")
            if evidence_signal <= 0:
                score *= 0.9
                reasons.append("penalized: low evidence density")
            else:
                score *= 1 + (0.2 * evidence_signal)
                reasons.append("boosted: evidential signal")
        if section_type == "sintese":
            score *= 1.15
            reasons.append("boosted: seção síntese")
        if section_type in {"causa", "efeito", "risco"}:
            score *= 1.10
            reasons.append(f"boosted: seção {section_type}")
        if section_type == "tabela" and query_context.query_type == "aggregation":
            score *= 1.10
            reasons.append("boosted: tabela para agregação")
        if query_context.preferred_section_types and section_type in query_context.preferred_section_types:
            score *= 1.15
            reasons.append(f"boosted: seção preferida para {query_context.query_type}")
        if query_context.query_type == "legal_reference":
            legal_haystack = "\n".join(part for part in [chunk.text, document.title if document else ""] if part)
            if LEGAL_SIGNAL_RE.search(legal_haystack):
                score *= 1.15
                reasons.append("boosted: legal reference signal")
            else:
                score *= 0.9
                reasons.append("penalized: no legal reference marker")
        if query_context.has_exact_match and query_context.exact_term:
            exact = query_context.exact_term.casefold()
            if exact in text_casefold or exact in title_casefold:
                score *= 1.20
                reasons.append("boosted: match exato")
        if "hierarchical" in query_context.query_facets and chunk.audit_object_id:
            score *= 1.05
            reasons.append("boosted: consulta hierárquica")
        return score, reasons

    def _evidence_signal(self, chunk: ChunkRecord, document: DocumentRecord | None) -> tuple[float, bool]:
        section_type = (chunk.section_type or "").lower()
        if section_type in {"evidencia", "evidence", "comprovacao", "comprovação"}:
            return 1.0, True
        haystack = "\n".join(
            part
            for part in [
                chunk.text,
                chunk.section_type or "",
                document.title if document else "",
            ]
            if part
        )
        score = 0.0
        for _label, pattern, weight in EVIDENCE_PATTERNS:
            if pattern.search(haystack):
                score += weight
        return min(round(score, 6), 1.0), False

    def _score_reasons(
        self,
        *,
        bm25: float,
        vector: float,
        reranker: float,
        authority: float,
        entity_density: float,
        evidence_score: float,
        policy_reasons: list[str],
        source_type: str,
        query_context: QueryContext,
    ) -> list[str]:
        reasons = list(policy_reasons)
        if bm25 >= 0.8:
            reasons.append("alta aderência lexical (BM25)")
        elif bm25 >= 0.4:
            reasons.append("aderência lexical moderada")
        if vector >= 0.8:
            reasons.append("alta relevância vetorial")
        elif vector >= 0.4:
            reasons.append("relevância vetorial moderada")
        if reranker >= 0.8:
            reasons.append("alta relevância semântica")
        elif reranker >= 0.4:
            reasons.append("relevância semântica moderada")
        if authority >= 0.95:
            reasons.append("fonte de alta autoridade")
        if entity_density >= 0.5:
            reasons.append("alta densidade de entidades")
        if evidence_score >= 0.7:
            reasons.append("alta densidade evidencial")
        elif evidence_score > 0:
            reasons.append("sinal evidencial presente")
        if source_type == SourceType.NORMATIVE.value:
            reasons.append("boosted: fonte normativa")
        if source_type == SourceType.GROUND_TRUTH.value:
            reasons.append("boosted: ground truth")
        if "hierarchical" in query_context.query_facets:
            reasons.append("consulta com hierarquia achado/subachado")
        if query_context.safe_mode:
            reasons.append("modo seguro ativado")
        return reasons

    def _search_impl(
        self,
        query: str,
        audit_object_id: str | None = None,
        source_types: list[str] | None = None,
        top_k: int = 5,
        query_context: QueryContext | None = None,
    ) -> tuple[list[SearchHit], dict, dict]:
        scope = self.detect_scope(query, audit_object_id)
        query_context = query_context or self.classify_query(query, top_k)
        candidate_limit = query_context.candidate_limit
        bm25_hits = self.es.search_chunks(query=query, audit_object_id=scope, source_types=source_types, size=candidate_limit)
        vector_hits = []
        if self.embedding_provider is not None:
            try:
                query_embedding = self.embedding_provider.embed([query])[0]
                vector_hits = self.vectors.query(query_embedding, audit_object_id=scope, source_types=source_types, limit=candidate_limit)
            except Exception as exc:
                logger.warning("Vector retrieval unavailable for query %r: %s", query, exc)
        vector_lookup = {hit.chunk_id: hit.score for hit in vector_hits}
        bm25_lookup = {hit["_id"]: float(hit["_score"]) for hit in bm25_hits}
        merged_ids = list(dict.fromkeys([hit["_id"] for hit in bm25_hits] + [hit.chunk_id for hit in vector_hits]))[:candidate_limit]
        if not merged_ids:
            empty_trace = {
                "query": query,
                "scope": scope,
                "query_context": {
                    "query_type": query_context.query_type,
                    "query_facets": list(query_context.query_facets),
                },
                "risk": {
                    "flags": list(query_context.risk_flags),
                    "score": query_context.risk_score,
                    "safe_mode": query_context.safe_mode,
                },
                "retrieval": [],
                "rerank": [],
                "scoring": [],
                "final": [],
            }
            return [], {"conflict": False, "source_types": []}, empty_trace

        def normalize(values: dict[str, float]) -> dict[str, float]:
            if not values:
                return {}
            minimum = min(values.values())
            maximum = max(values.values())
            if maximum == minimum:
                return {key: 1.0 for key in values}
            return {key: (value - minimum) / (maximum - minimum) for key, value in values.items()}

        norm_bm25 = normalize(bm25_lookup)
        norm_vector = normalize(vector_lookup)
        with get_session() as session:
            chunks = {
                record.id: record
                for record in session.execute(select(ChunkRecord).where(ChunkRecord.id.in_(merged_ids))).scalars().all()
            }
            documents = {
                record.id: record
                for record in session.execute(
                    select(DocumentRecord).where(DocumentRecord.id.in_({chunk.document_id for chunk in chunks.values()}))
                ).scalars().all()
            }
            reranker_lookup: dict[str, float] = {}
            if self.reranker is not None:
                try:
                    reranker_lookup = self.reranker.score(
                        query,
                        [
                            RerankCandidate(chunk=chunks[chunk_id], document=documents.get(chunks[chunk_id].document_id))
                            for chunk_id in merged_ids
                            if chunk_id in chunks
                        ],
                    )
                except Exception as exc:
                    logger.warning("Reranker unavailable for query %r: %s", query, exc)
                    reranker_lookup = {}
            norm_reranker = normalize(reranker_lookup)
            scoring_profile = get_scoring_policy().profile_for(query_context.query_type)
            results = []
            source_type_values = set()
            retrieval_trace = []
            rerank_trace = []
            scoring_trace = []
            filtered_trace = []
            for chunk_id in merged_ids:
                chunk = chunks.get(chunk_id)
                if chunk is None:
                    continue
                document = documents.get(chunk.document_id)
                hard_filter_reasons = self._hard_filter_reasons(chunk, document)
                if hard_filter_reasons:
                    filtered_trace.append(
                        {
                            "chunk_id": chunk.id,
                            "source_type": chunk.source_type,
                            "audit_object_id": chunk.audit_object_id,
                            "section_type": chunk.section_type,
                            "reasons": hard_filter_reasons,
                        }
                    )
                    continue
                source_type_values.add(chunk.source_type)
                bm25 = norm_bm25.get(chunk_id, 0.0)
                vector = norm_vector.get(chunk_id, 0.0)
                reranker = norm_reranker.get(chunk_id, 0.0)
                authority = chunk.authority_weight
                entity_density_raw = chunk.entity_density
                entity_density = min(entity_density_raw * 25, 1.0)
                evidence_score, evidence_structural = self._evidence_signal(chunk, document)
                policy_multiplier, policy_reasons = self._policy_adjustments(
                    chunk,
                    document,
                    query_context,
                    entity_signal=entity_density,
                    evidence_signal=evidence_score,
                )
                weights = scoring_profile.weights
                final = (
                    (reranker * weights.get("reranker", 0.0))
                    + (vector * weights.get("vector", 0.0))
                    + (bm25 * weights.get("bm25", 0.0))
                    + (authority * weights.get("authority", 0.0))
                    + (entity_density * weights.get("entity", 0.0))
                    + (evidence_score * weights.get("evidence", 0.0))
                )
                final *= policy_multiplier
                if chunk.source_type == SourceType.NORMATIVE.value:
                    final *= 1.25
                if chunk.source_type == SourceType.GROUND_TRUTH.value:
                    final *= 1.15
                penalties = [reason for reason in policy_reasons if reason.startswith("penalized")]
                boosts = [reason for reason in policy_reasons if reason.startswith("boosted")]
                evidence_boost_applied = "boosted: evidential signal" in boosts
                methodology_penalty_applied = "penalized: methodology_section" in penalties
                reasons = self._score_reasons(
                    bm25=bm25,
                    vector=vector,
                    reranker=reranker,
                    authority=authority,
                    entity_density=entity_density,
                    evidence_score=evidence_score,
                    policy_reasons=policy_reasons,
                    source_type=chunk.source_type,
                    query_context=query_context,
                )
                retrieval_trace.append(
                    {
                        "chunk_id": chunk.id,
                        "source_type": chunk.source_type,
                        "audit_object_id": chunk.audit_object_id,
                        "bm25_raw": round(bm25_lookup.get(chunk_id, 0.0), 6),
                        "bm25": round(bm25, 6),
                        "vector_raw": round(vector_lookup.get(chunk_id, 0.0), 6),
                        "vector": round(vector, 6),
                        "filtered": False,
                        "evidence_score": round(evidence_score, 6),
                    }
                )
                rerank_trace.append(
                    {
                        "chunk_id": chunk.id,
                        "rerank_raw": round(reranker_lookup.get(chunk_id, 0.0), 6),
                        "rerank": round(reranker, 6),
                    }
                )
                scoring_trace.append(
                    {
                        "chunk_id": chunk.id,
                        "source_type": chunk.source_type,
                        "section_type": chunk.section_type,
                        "bm25": round(bm25, 6),
                        "vector": round(vector, 6),
                        "reranker": round(reranker, 6),
                        "authority": round(authority, 6),
                        "entity_density_raw": round(entity_density_raw, 6),
                        "entity_density": round(entity_density, 6),
                        "evidence_score": round(evidence_score, 6),
                        "evidence_structural": evidence_structural,
                        "evidence_boost_applied": evidence_boost_applied,
                        "methodology_penalty_applied": methodology_penalty_applied,
                        "policy_multiplier": round(policy_multiplier, 6),
                        "penalties": penalties,
                        "boosts": boosts,
                        "scoring_profile": scoring_profile.weights,
                        "scoring_profile_source": scoring_profile.source,
                        "risk_flags": list(query_context.risk_flags),
                        "safe_mode": query_context.safe_mode,
                        "final_score": round(final, 6),
                        "reasons": reasons,
                    }
                )
                results.append(
                    SearchHit(
                        chunk=chunk,
                        score=round(final, 6),
                        score_breakdown={
                            "bm25Raw": round(bm25_lookup.get(chunk_id, 0.0), 6),
                            "bm25": round(bm25, 6),
                            "vectorRaw": round(vector_lookup.get(chunk_id, 0.0), 6),
                            "vector": round(vector, 6),
                            "rerankerRaw": round(reranker_lookup.get(chunk_id, 0.0), 6),
                            "reranker": round(reranker, 6),
                            "authority": round(authority, 6),
                            "entityDensityRaw": round(entity_density_raw, 6),
                            "policyMultiplier": round(policy_multiplier, 6),
                            "queryType": query_context.query_type,
                            "queryFacets": list(query_context.query_facets),
                            "entityDensity": round(entity_density, 6),
                            "evidenceScore": round(evidence_score, 6),
                            "evidenceStructural": evidence_structural,
                            "evidenceBoostApplied": evidence_boost_applied,
                            "methodologyPenaltyApplied": methodology_penalty_applied,
                            "penalties": penalties,
                            "boosts": boosts,
                            "riskFlags": list(query_context.risk_flags),
                            "riskScore": query_context.risk_score,
                            "safeMode": query_context.safe_mode,
                            "scoringProfile": scoring_profile.weights,
                            "scoringProfileSource": scoring_profile.source,
                            "finalScore": round(final, 6),
                        },
                        reasons=reasons,
                    )
                )
        ranked = sorted(results, key=lambda item: item.score, reverse=True)[:top_k]
        conflict = len({hit.chunk.source_type for hit in ranked}) > 1
        trace = {
            "query": query,
            "scope": scope,
            "query_context": {
                "query_type": query_context.query_type,
                "query_facets": list(query_context.query_facets),
                "candidate_limit": query_context.candidate_limit,
                "preferred_section_types": list(query_context.preferred_section_types),
            },
            "risk": {
                "flags": list(query_context.risk_flags),
                "score": query_context.risk_score,
                "safe_mode": query_context.safe_mode,
            },
            "retrieval": retrieval_trace,
            "filtered_out": filtered_trace,
            "rerank": rerank_trace,
            "scoring": scoring_trace,
            "final": [
                {
                    "rank": index,
                    "chunk_id": hit.chunk.id,
                    "source_type": hit.chunk.source_type,
                    "audit_object_id": hit.chunk.audit_object_id,
                    "section_type": hit.chunk.section_type,
                    "score": hit.score,
                    "reasons": hit.reasons,
                }
                for index, hit in enumerate(ranked, start=1)
            ],
        }
        return ranked, {"conflict": conflict, "source_types": sorted(source_type_values)}, trace

    def search(
        self,
        query: str,
        audit_object_id: str | None = None,
        source_types: list[str] | None = None,
        top_k: int = 5,
        query_context: QueryContext | None = None,
    ) -> tuple[list[SearchHit], dict]:
        hits, conflict, _trace = self._search_impl(
            query=query,
            audit_object_id=audit_object_id,
            source_types=source_types,
            top_k=top_k,
            query_context=query_context,
        )
        return hits, conflict

    def search_with_trace(
        self,
        query: str,
        audit_object_id: str | None = None,
        source_types: list[str] | None = None,
        top_k: int = 5,
        query_context: QueryContext | None = None,
    ) -> tuple[list[SearchHit], dict, dict]:
        return self._search_impl(
            query=query,
            audit_object_id=audit_object_id,
            source_types=source_types,
            top_k=top_k,
            query_context=query_context,
        )

    def document(self, document_id: str) -> DocumentRecord | None:
        with get_session() as session:
            return session.get(DocumentRecord, document_id)

    def chunk(self, chunk_id: str) -> ChunkRecord | None:
        with get_session() as session:
            return session.get(ChunkRecord, chunk_id)
