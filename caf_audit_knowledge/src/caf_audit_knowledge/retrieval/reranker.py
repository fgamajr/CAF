from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache

from caf_audit_knowledge.config import settings
from caf_audit_knowledge.storage.models import ChunkRecord, DocumentRecord


@dataclass(frozen=True)
class RerankCandidate:
    chunk: ChunkRecord
    document: DocumentRecord | None


class CrossEncoderReranker:
    def __init__(self) -> None:
        from sentence_transformers import CrossEncoder

        device = self._resolve_device()
        self.model = CrossEncoder(
            settings.reranker_model,
            device=device,
            max_length=settings.reranker_max_length,
        )
        if settings.reranker_use_fp16 and device.startswith("cuda") and hasattr(self.model.model, "half"):
            self.model.model.half()

    def _resolve_device(self) -> str:
        configured = settings.reranker_device.lower()
        if configured != "auto":
            return settings.reranker_device
        try:
            import torch

            return "cuda" if torch.cuda.is_available() else "cpu"
        except Exception:
            return "cpu"

    def _build_document_text(self, candidate: RerankCandidate) -> str:
        parts = []
        if candidate.document and candidate.document.title:
            parts.append(f"Document title: {candidate.document.title}")
        parts.append(f"Source type: {candidate.chunk.source_type}")
        if candidate.chunk.section_type:
            parts.append(f"Section type: {candidate.chunk.section_type}")
        if candidate.chunk.audit_object_id:
            parts.append(f"Audit object: {candidate.chunk.audit_object_id}")
        if candidate.chunk.page_start is not None:
            page_ref = f"{candidate.chunk.page_start}"
            if candidate.chunk.page_end not in {None, candidate.chunk.page_start}:
                page_ref = f"{page_ref}-{candidate.chunk.page_end}"
            parts.append(f"Pages: {page_ref}")
        parts.append(candidate.chunk.text)
        return "\n".join(parts)

    def score(self, query: str, candidates: list[RerankCandidate]) -> dict[str, float]:
        if not candidates:
            return {}
        pairs = [(query, self._build_document_text(candidate)) for candidate in candidates]
        scores = self.model.predict(
            pairs,
            batch_size=settings.reranker_batch_size,
            show_progress_bar=False,
        )
        return {
            candidate.chunk.id: float(score)
            for candidate, score in zip(candidates, scores, strict=True)
        }


@lru_cache(maxsize=1)
def get_reranker() -> CrossEncoderReranker:
    return CrossEncoderReranker()
