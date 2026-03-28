from __future__ import annotations

from datetime import datetime

from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, JSON, String, Text, UniqueConstraint
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from caf_audit_knowledge.constants import EmbeddingStatus

try:
    from pgvector.sqlalchemy import Vector
except Exception:  # pragma: no cover
    Vector = None


class Base(DeclarativeBase):
    pass


def vector_column(dimensions: int = 3072):
    if Vector is not None:
        return mapped_column(Vector(dimensions), nullable=True)
    return mapped_column(JSON, nullable=True)


class DocumentRecord(Base):
    __tablename__ = "documents"

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    source_path: Mapped[str] = mapped_column(Text, unique=True, index=True)
    source_type: Mapped[str] = mapped_column(String(32), index=True)
    authority_weight: Mapped[float] = mapped_column(Float)
    audit_object_id: Mapped[str | None] = mapped_column(String(8), index=True, nullable=True)
    content_hash: Mapped[str] = mapped_column(String(64), index=True)
    pipeline_fingerprint: Mapped[str] = mapped_column(Text)
    title: Mapped[str | None] = mapped_column(Text, nullable=True)
    text: Mapped[str] = mapped_column(Text)
    structured_markdown: Mapped[str] = mapped_column(Text, default="")
    page_count: Mapped[int] = mapped_column(Integer, default=1)
    page_map: Mapped[list[dict]] = mapped_column(JSON, default=list)
    is_duplicate: Mapped[bool] = mapped_column(Boolean, default=False, index=True)
    duplicate_of: Mapped[str | None] = mapped_column(String(64), ForeignKey("documents.id"), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    chunks: Mapped[list["ChunkRecord"]] = relationship(back_populates="document", cascade="all, delete-orphan")


class ChunkRecord(Base):
    __tablename__ = "chunks"
    __table_args__ = (UniqueConstraint("document_id", "chunk_seq", name="uq_document_chunk_seq"),)

    id: Mapped[str] = mapped_column(String(64), primary_key=True)
    document_id: Mapped[str] = mapped_column(String(64), ForeignKey("documents.id"), index=True)
    audit_object_id: Mapped[str | None] = mapped_column(String(8), index=True, nullable=True)
    text: Mapped[str] = mapped_column(Text)
    chunk_seq: Mapped[int] = mapped_column(Integer)
    char_start: Mapped[int] = mapped_column(Integer)
    char_end: Mapped[int] = mapped_column(Integer)
    page_start: Mapped[int | None] = mapped_column(Integer, nullable=True)
    page_end: Mapped[int | None] = mapped_column(Integer, nullable=True)
    section_type: Mapped[str | None] = mapped_column(String(32), nullable=True, index=True)
    source_type: Mapped[str] = mapped_column(String(32), index=True)
    authority_weight: Mapped[float] = mapped_column(Float)
    chunk_manifest_hash: Mapped[str] = mapped_column(String(64))
    chunk_feature_hash: Mapped[str] = mapped_column(String(64))
    entity_density: Mapped[float] = mapped_column(Float, default=0.0)
    legal_density: Mapped[float] = mapped_column(Float, default=0.0)
    importance_score: Mapped[float] = mapped_column(Float, default=0.0)
    embedding_status: Mapped[str] = mapped_column(String(16), default=EmbeddingStatus.PENDING.value, index=True)
    embedding_version: Mapped[str | None] = mapped_column(String(32), nullable=True, index=True)
    embedding = vector_column()

    document: Mapped[DocumentRecord] = relationship(back_populates="chunks")


class DocumentRelationRecord(Base):
    __tablename__ = "document_relations"
    __table_args__ = (
        UniqueConstraint("from_document_id", "to_document_id", "relation_type", name="uq_document_relation"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    from_document_id: Mapped[str] = mapped_column(String(64), ForeignKey("documents.id"), index=True)
    to_document_id: Mapped[str] = mapped_column(String(64), ForeignKey("documents.id"), index=True)
    relation_type: Mapped[str] = mapped_column(String(32), index=True)
    confidence: Mapped[float | None] = mapped_column(Float, nullable=True)


class AuditObjectRelationRecord(Base):
    __tablename__ = "audit_object_relations"
    __table_args__ = (UniqueConstraint("from_audit_object_id", "to_audit_object_id", "relation_type", name="uq_audit_relation"),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    from_audit_object_id: Mapped[str] = mapped_column(String(8), index=True)
    to_audit_object_id: Mapped[str] = mapped_column(String(8), index=True)
    relation_type: Mapped[str] = mapped_column(String(32), index=True)


class EmbeddingTaskRecord(Base):
    __tablename__ = "embedding_tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    chunk_id: Mapped[str] = mapped_column(String(64), ForeignKey("chunks.id"), unique=True)
    provider: Mapped[str] = mapped_column(String(32))
    model: Mapped[str] = mapped_column(String(64))
    version: Mapped[str] = mapped_column(String(32), index=True)
    status: Mapped[str] = mapped_column(String(16), default=EmbeddingStatus.PENDING.value, index=True)
    attempt_count: Mapped[int] = mapped_column(Integer, default=0)
    last_error: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class PruningLedgerRecord(Base):
    __tablename__ = "pruning_ledger"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    document_id: Mapped[str] = mapped_column(String(64), index=True)
    source_path: Mapped[str] = mapped_column(Text)
    original_candidate_count: Mapped[int] = mapped_column(Integer)
    kept_count: Mapped[int] = mapped_column(Integer)
    dropped_sequences: Mapped[list[int]] = mapped_column(JSON)
    reason: Mapped[str] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
