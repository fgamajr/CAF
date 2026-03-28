from __future__ import annotations

from dataclasses import dataclass

from sqlalchemy import select

from caf_audit_knowledge.config import settings
from caf_audit_knowledge.storage.db import get_session
from caf_audit_knowledge.storage.models import ChunkRecord


@dataclass(frozen=True)
class VectorHit:
    chunk_id: str
    score: float


class VectorStore:
    def query(self, embedding: list[float], audit_object_id: str | None, source_types: list[str] | None, limit: int = 20) -> list[VectorHit]:
        if settings.vector_backend.lower() != "pgvector":
            return []
        with get_session() as session:
            distance = ChunkRecord.embedding.cosine_distance(embedding).label("distance")
            stmt = select(ChunkRecord.id, distance).where(ChunkRecord.embedding.is_not(None))
            if audit_object_id:
                stmt = stmt.where(ChunkRecord.audit_object_id == audit_object_id)
            if source_types:
                stmt = stmt.where(ChunkRecord.source_type.in_(source_types))
            rows = session.execute(stmt.order_by(distance).limit(limit)).all()
            if not rows:
                return []
            return [
                VectorHit(chunk_id=row.id, score=1.0 / (1.0 + float(row.distance)))
                for row in rows
            ]
