from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass

from caf_audit_knowledge.constants import CHUNK_TARGET_CHARS, HARD_LIMIT, LEGAL_TOKEN_RE, MAX_CHUNKS_PER_DOC
from caf_audit_knowledge.text_extractors import PageSpan

ENTITY_RE = re.compile(r"\b(ACH0[1-4]|ACH-0[1-4]|peça\s*\d+|PEÇA\s*\d+|Lei\s*\d+|ISO\s*[\d\-]+)\b")
LEGAL_RE = re.compile(LEGAL_TOKEN_RE, re.IGNORECASE)


@dataclass(frozen=True)
class ChunkCandidate:
    text: str
    char_start: int
    char_end: int


def split_text(text: str, target_chars: int = CHUNK_TARGET_CHARS) -> list[ChunkCandidate]:
    paragraphs = [segment.strip() for segment in re.split(r"\n\s*\n", text) if segment.strip()]
    candidates: list[ChunkCandidate] = []
    cursor = 0
    buffer = ""
    start = 0
    for paragraph in paragraphs:
        candidate = f"{buffer}\n\n{paragraph}".strip() if buffer else paragraph
        if buffer and len(candidate) > target_chars:
            end = start + len(buffer)
            candidates.append(ChunkCandidate(text=buffer, char_start=start, char_end=end))
            cursor = end
            buffer = paragraph
            start = cursor + 2
            continue
        if not buffer:
            start = cursor
        buffer = candidate
    if buffer:
        candidates.append(ChunkCandidate(text=buffer, char_start=start, char_end=start + len(buffer)))
    return candidates or [ChunkCandidate(text=text, char_start=0, char_end=len(text))]


def _density(regex: re.Pattern[str], text: str) -> float:
    tokens = max(len(text.split()), 1)
    return round(len(regex.findall(text)) / tokens, 6)


def _importance(text: str) -> float:
    return round((_density(ENTITY_RE, text) * 0.6) + (_density(LEGAL_RE, text) * 0.4), 6)


def _coalesce(candidates: list[ChunkCandidate], max_chunks: int) -> list[ChunkCandidate]:
    merged = candidates[:]
    while len(merged) > max_chunks and len(merged) > 1:
        join_index = min(
            range(len(merged) - 1),
            key=lambda idx: len(merged[idx].text) + len(merged[idx + 1].text),
        )
        left, right = merged[join_index], merged[join_index + 1]
        combined = ChunkCandidate(
            text=f"{left.text}\n\n{right.text}".strip(),
            char_start=left.char_start,
            char_end=right.char_end,
        )
        merged = merged[:join_index] + [combined] + merged[join_index + 2 :]
    return merged


def _resolve_pages(page_spans: list[PageSpan], char_start: int, char_end: int) -> tuple[int | None, int | None]:
    pages = [
        span.page_number
        for span in page_spans
        if not (char_end <= span.char_start or char_start >= span.char_end)
    ]
    if not pages:
        return None, None
    return min(pages), max(pages)


def build_chunks(
    doc_id: str,
    text: str,
    source_type: str,
    authority_weight: float,
    audit_object_id: str | None,
    page_spans: list[PageSpan] | None = None,
) -> tuple[list[dict], dict | None]:
    candidates = split_text(text)
    page_spans = page_spans or []
    pruning_ledger = None
    if len(candidates) > HARD_LIMIT:
        scored = [(idx, _importance(candidate.text)) for idx, candidate in enumerate(candidates)]
        keep = {0, len(candidates) - 1}
        ranked_middle = sorted(scored[1:-1], key=lambda item: (-item[1], item[0]))
        for idx, _score in ranked_middle[: HARD_LIMIT - len(keep)]:
            keep.add(idx)
        kept_indices = sorted(keep)
        pruning_ledger = {
            "document_id": doc_id,
            "original_candidate_count": len(candidates),
            "kept_count": len(kept_indices),
            "dropped_sequences": [idx for idx in range(len(candidates)) if idx not in keep],
            "reason": f"candidate_count_exceeded_{HARD_LIMIT}",
        }
        candidates = [candidates[idx] for idx in kept_indices]

    candidates = _coalesce(candidates, MAX_CHUNKS_PER_DOC)
    chunks = []
    for seq, candidate in enumerate(candidates):
        entity_density = _density(ENTITY_RE, candidate.text)
        legal_density = _density(LEGAL_RE, candidate.text)
        importance = round((entity_density * 0.5) + (legal_density * 0.2) + (authority_weight * 0.3), 6)
        page_start, page_end = _resolve_pages(page_spans, candidate.char_start, candidate.char_end)
        manifest_payload = {
            "doc_id": doc_id,
            "seq": seq,
            "char_start": candidate.char_start,
            "char_end": candidate.char_end,
            "page_start": page_start,
            "page_end": page_end,
            "source_type": source_type,
            "audit_object_id": audit_object_id,
        }
        feature_payload = {
            "entity_density": entity_density,
            "legal_density": legal_density,
            "importance_score": importance,
        }
        chunk_manifest_hash = hashlib.sha256(json.dumps(manifest_payload, sort_keys=True).encode()).hexdigest()
        chunk_feature_hash = hashlib.sha256(json.dumps(feature_payload, sort_keys=True).encode()).hexdigest()
        chunk_id = hashlib.sha256(f"{doc_id}:{seq}:{chunk_manifest_hash}".encode()).hexdigest()
        chunks.append(
            {
                "id": chunk_id,
                "document_id": doc_id,
                "audit_object_id": audit_object_id,
                "text": candidate.text,
                "chunk_seq": seq,
                "char_start": candidate.char_start,
                "char_end": candidate.char_end,
                "page_start": page_start,
                "page_end": page_end,
                "source_type": source_type,
                "authority_weight": authority_weight,
                "chunk_manifest_hash": chunk_manifest_hash,
                "chunk_feature_hash": chunk_feature_hash,
                "entity_density": entity_density,
                "legal_density": legal_density,
                "importance_score": importance,
            }
        )
    return chunks, pruning_ledger
