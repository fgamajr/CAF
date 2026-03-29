from __future__ import annotations

import json
import re
from dataclasses import dataclass
from difflib import SequenceMatcher

from caf_audit_knowledge.answering.classifier import QueryClassification
from caf_audit_knowledge.retrieval.service import SearchHit

SUBSCOPE_PATTERNS = (
    re.compile(r"\bsubachado\s+(\d+)\s+do\s+achado\s+([1-4])\b", re.IGNORECASE),
    re.compile(r"\bachado\s+([1-4]\.\d+)\b", re.IGNORECASE),
)
TOKEN_RE = re.compile(r"\b[\w-]+\b", re.UNICODE)
DEFAULT_AGGREGATION_SECTIONS = ("sintese", "tabela", "causa", "efeito", "risco")
LOW_SIGNAL_SECTIONS = {"body", "intro", "metodologia", "procedimento", "abordagem", "toc", "boilerplate"}


@dataclass(frozen=True)
class AggregatedBundle:
    payload: dict[str, object]
    ordered_hits: list[SearchHit]

    def to_json(self) -> str:
        return json.dumps(self.payload, indent=2, ensure_ascii=False)


def _normalize_text(text: str) -> str:
    lowered = text.casefold()
    tokens = TOKEN_RE.findall(lowered)
    return " ".join(tokens[:220])


def _similarity(left: str, right: str) -> float:
    if not left or not right:
        return 0.0
    ratio = SequenceMatcher(a=left, b=right).ratio()
    left_tokens = set(left.split())
    right_tokens = set(right.split())
    if not left_tokens or not right_tokens:
        return ratio
    jaccard = len(left_tokens & right_tokens) / len(left_tokens | right_tokens)
    return max(ratio, jaccard)


def _infer_subscope_id(hit: SearchHit) -> str | None:
    haystack = f"{hit.chunk.text}\n{hit.chunk.section_type or ''}"
    for pattern in SUBSCOPE_PATTERNS:
        match = pattern.search(haystack)
        if not match:
            continue
        if len(match.groups()) == 2:
            sub, ach = match.groups()
            return f"ACH0{ach}.{sub}"
        return f"ACH0{match.group(1).split('.')[0]}.{match.group(1).split('.', 1)[1]}"
    return None


def _compact_snippet(text: str, max_chars: int = 420) -> str:
    cleaned = " ".join(text.split())
    if len(cleaned) <= max_chars:
        return cleaned
    return f"{cleaned[:max_chars].rstrip()}..."


def _deduplicate_hits(hits: list[SearchHit], threshold: float = 0.9) -> list[SearchHit]:
    kept: list[SearchHit] = []
    seen_texts: list[str] = []
    for hit in hits:
        normalized = _normalize_text(hit.chunk.text)
        if any(_similarity(normalized, previous) >= threshold for previous in seen_texts):
            continue
        kept.append(hit)
        seen_texts.append(normalized)
    return kept


def _preferred_sections(query: str, classification: QueryClassification) -> tuple[str, ...]:
    lowered = query.casefold()
    if classification.query_type == "evidential":
        return ("tabela", "sintese", "causa", "efeito", "risco")
    if any(token in lowered for token in ["causa", "causas"]):
        return ("causa", "sintese", "tabela")
    if any(token in lowered for token in ["efeito", "efeitos", "impacto", "impactos"]):
        return ("efeito", "risco", "sintese", "tabela")
    if any(token in lowered for token in ["risco", "riscos"]):
        return ("risco", "efeito", "sintese", "tabela")
    if classification.query_type == "aggregation":
        return DEFAULT_AGGREGATION_SECTIONS
    if classification.query_type == "factual":
        return ("sintese", "causa", "efeito", "risco", "tabela")
    return ()


def _filter_relevant_hits(query: str, classification: QueryClassification, hits: list[SearchHit]) -> list[SearchHit]:
    preferred = _preferred_sections(query, classification)
    if not preferred:
        return hits

    preferred_set = set(preferred)
    preferred_hits = [hit for hit in hits if (hit.chunk.section_type or "body").lower() in preferred_set]
    if preferred_hits:
        return preferred_hits

    non_low_signal_hits = [hit for hit in hits if (hit.chunk.section_type or "body").lower() not in LOW_SIGNAL_SECTIONS]
    if non_low_signal_hits:
        return non_low_signal_hits
    return hits


def build_aggregation(
    *,
    query: str,
    classification: QueryClassification,
    hits: list[SearchHit],
) -> AggregatedBundle | None:
    if classification.query_type not in {"aggregation", "factual", "evidential"}:
        return None

    deduplicated = _deduplicate_hits(hits)
    filtered_hits = _filter_relevant_hits(query, classification, deduplicated)
    grouped: dict[tuple[str, str, str], list[SearchHit]] = {}
    for hit in filtered_hits:
        key = (
            hit.chunk.audit_object_id or "unscoped",
            _infer_subscope_id(hit) or "parent",
            hit.chunk.section_type or "body",
        )
        grouped.setdefault(key, []).append(hit)

    groups = []
    section_counts: dict[str, int] = {}
    audit_counts: dict[str, int] = {}
    for (audit_object_id, subscope_id, section_type), group_hits in sorted(grouped.items()):
        section_counts[section_type] = section_counts.get(section_type, 0) + len(group_hits)
        audit_counts[audit_object_id] = audit_counts.get(audit_object_id, 0) + len(group_hits)
        groups.append(
            {
                "audit_object_id": audit_object_id,
                "subscope_id": None if subscope_id == "parent" else subscope_id,
                "section_type": section_type,
                "item_count": len(group_hits),
                "items": [
                    {
                        "chunk_id": hit.chunk.id,
                        "doc_id": hit.chunk.document_id,
                        "source_type": hit.chunk.source_type,
                        "citation": (
                            f"pp. {hit.chunk.page_start}-{hit.chunk.page_end}"
                            if hit.chunk.page_start is not None and hit.chunk.page_end not in {None, hit.chunk.page_start}
                            else (f"p. {hit.chunk.page_start}" if hit.chunk.page_start is not None else None)
                        ),
                        "score": hit.score,
                        "summary": _compact_snippet(hit.chunk.text),
                    }
                    for hit in group_hits[:3]
                ],
            }
        )

    payload = {
        "query": query,
        "query_type": classification.query_type,
        "total_hits": len(hits),
        "deduplicated_hits": len(deduplicated),
        "filtered_hits": len(filtered_hits),
        "group_count": len(groups),
        "counts": {
            "by_audit_object_id": audit_counts,
            "by_section_type": section_counts,
        },
        "groups": groups,
    }
    return AggregatedBundle(payload=payload, ordered_hits=filtered_hits)
