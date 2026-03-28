from __future__ import annotations

import hashlib
import json
import os
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

from sqlalchemy import delete, select

from caf_audit_knowledge.config import settings
from caf_audit_knowledge.constants import EmbeddingStatus
from caf_audit_knowledge.ingest.chunking import build_chunks
from caf_audit_knowledge.ingest.relationships import build_relations
from caf_audit_knowledge.repo_semantics import canonical_rank, classify_source, extract_audit_object_id, extract_piece_number, infer_section_type, should_ignore_path
from caf_audit_knowledge.retrieval.elasticsearch_store import ElasticsearchStore
from caf_audit_knowledge.storage.db import engine, get_session
from caf_audit_knowledge.storage.models import AuditObjectRelationRecord, Base, ChunkRecord, DocumentRecord, DocumentRelationRecord, EmbeddingTaskRecord, PruningLedgerRecord
from caf_audit_knowledge.text_extractors import PageSpan, extract_document, read_bytes


@dataclass(frozen=True)
class CandidateDocument:
    path: Path
    doc_id: str
    content_hash: str
    source_type: str
    authority_weight: float
    audit_object_id: str | None
    piece_number: int | None
    title: str
    text: str
    structured_markdown: str
    page_count: int
    page_map: list[dict]


class RepositoryIndexer:
    def __init__(self) -> None:
        self.es = ElasticsearchStore()
        self._ensure_artifact_dirs()

    def _ensure_artifact_dirs(self) -> None:
        settings.effective_data_root.mkdir(parents=True, exist_ok=True)
        settings.ledger_root.mkdir(parents=True, exist_ok=True)
        settings.manifests_root.mkdir(parents=True, exist_ok=True)

    def discover_paths(self) -> list[Path]:
        paths = []
        for child in sorted(settings.repository_root.iterdir()):
            if not child.is_dir():
                continue
            if child.name not in {
                "00_CONTEXTO",
                "01_RELATORIO_V2",
                "02_FONTE_VERDADE",
                "03_RELATORIO_V1",
                "04_PECAS_EVIDENCIA",
                "05_PECAS_TRAMITACAO",
                "06_NORMAS_CRITERIOS",
                "07_MODELOS_TCU",
            }:
                continue
            for root, _dirs, files in os.walk(child):
                for filename in files:
                    path = Path(root) / filename
                    if not should_ignore_path(path):
                        paths.append(path)
        return sorted(paths)

    def _candidate(self, path: Path) -> CandidateDocument | None:
        descriptor = classify_source(path)
        if descriptor is None:
            return None
        raw_bytes = read_bytes(path)
        extraction = extract_document(path, raw_bytes=raw_bytes)
        if not extraction.text.strip():
            return None
        doc_id = hashlib.sha256(raw_bytes).hexdigest()
        content_hash = hashlib.sha256(extraction.text.encode("utf-8")).hexdigest()
        return CandidateDocument(
            path=path,
            doc_id=doc_id,
            content_hash=content_hash,
            source_type=descriptor.source_type.value,
            authority_weight=descriptor.authority_weight,
            audit_object_id=extract_audit_object_id(extraction.text, path),
            piece_number=extract_piece_number(extraction.text, path),
            title=path.stem,
            text=extraction.text,
            structured_markdown=extraction.structured_markdown,
            page_count=max((span.page_number for span in extraction.page_spans), default=1),
            page_map=[
                {
                    "page_number": span.page_number,
                    "char_start": span.char_start,
                    "char_end": span.char_end,
                }
                for span in extraction.page_spans
            ],
        )

    def _deduplicate(self, candidates: list[CandidateDocument]) -> tuple[list[CandidateDocument], dict[str, str]]:
        groups: dict[str, list[CandidateDocument]] = defaultdict(list)
        for candidate in candidates:
            groups[candidate.content_hash].append(candidate)
        canonical: list[CandidateDocument] = []
        duplicates: dict[str, str] = {}
        for group in groups.values():
            chosen = min(group, key=lambda item: canonical_rank(item.path))
            canonical.append(chosen)
            for item in group:
                if item.doc_id != chosen.doc_id:
                    duplicates[item.doc_id] = chosen.doc_id
        return canonical, duplicates

    def _document_payload(
        self,
        candidate: CandidateDocument,
        *,
        is_duplicate: bool,
        duplicate_of: str | None,
    ) -> dict:
        return {
            "doc_id": candidate.doc_id,
            "source_path": str(candidate.path),
            "source_type": candidate.source_type,
            "authority_weight": candidate.authority_weight,
            "audit_object_id": candidate.audit_object_id,
            "content_hash": candidate.content_hash,
            "pipeline_fingerprint": settings.pipeline_fingerprint,
            "title": candidate.title,
            "text": candidate.text,
            "structured_markdown": candidate.structured_markdown,
            "page_count": candidate.page_count,
            "page_map": candidate.page_map,
            "is_duplicate": is_duplicate,
            "duplicate_of": duplicate_of,
            "piece_number": candidate.piece_number,
        }

    def _document_index_payload(self, row: dict) -> dict:
        return {
            "doc_id": row["doc_id"],
            "content_hash": row["content_hash"],
            "source_path": row["source_path"],
            "source_type": row["source_type"],
            "authority_weight": row["authority_weight"],
            "audit_object_id": row["audit_object_id"],
            "pipeline_fingerprint": row["pipeline_fingerprint"],
            "title": row["title"],
            "text": row["text"],
            "structured_markdown": row["structured_markdown"],
            "page_count": row["page_count"],
            "is_duplicate": row["is_duplicate"],
            "duplicate_of": row["duplicate_of"],
        }

    def init_stores(self, recreate_indices: bool = False) -> None:
        Base.metadata.create_all(bind=engine)
        self.es.ensure_indices(recreate=recreate_indices)

    def recreate_stores(self) -> None:
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)
        self.es.ensure_indices(recreate=True)

    def reset_state(self) -> None:
        with get_session() as session:
            session.execute(delete(EmbeddingTaskRecord))
            session.execute(delete(DocumentRelationRecord))
            session.execute(delete(AuditObjectRelationRecord))
            session.execute(delete(PruningLedgerRecord))
            session.execute(delete(ChunkRecord))
            session.execute(delete(DocumentRecord))
            session.commit()
        self.es.ensure_indices(recreate=True)

    def delete_path(self, path: Path) -> None:
        with get_session() as session:
            record = session.execute(select(DocumentRecord).where(DocumentRecord.source_path == str(path))).scalar_one_or_none()
            if record is None:
                return
            doc_id = record.id
            session.execute(delete(EmbeddingTaskRecord).where(EmbeddingTaskRecord.chunk_id.in_(select(ChunkRecord.id).where(ChunkRecord.document_id == doc_id))))
            session.execute(delete(DocumentRelationRecord).where((DocumentRelationRecord.from_document_id == doc_id) | (DocumentRelationRecord.to_document_id == doc_id)))
            session.execute(delete(ChunkRecord).where(ChunkRecord.document_id == doc_id))
            session.execute(delete(DocumentRecord).where(DocumentRecord.id == doc_id))
            session.commit()
        self.es.delete_document(doc_id)

    def build(self, full: bool = False, paths: list[Path] | None = None) -> dict[str, int]:
        if full:
            self.recreate_stores()
        else:
            self.init_stores(recreate_indices=False)
        target_paths = paths or self.discover_paths()
        candidates = [item for item in (self._candidate(path) for path in target_paths) if item is not None]
        canonical, duplicates = self._deduplicate(candidates)
        canonical_docs = []
        document_rows = []
        chunk_rows = []
        pruning_rows = []
        for candidate in canonical:
            document_row = self._document_payload(candidate, is_duplicate=False, duplicate_of=None)
            document_rows.append(document_row)
            chunks, pruning_ledger = build_chunks(
                doc_id=candidate.doc_id,
                text=candidate.text,
                source_type=candidate.source_type,
                authority_weight=candidate.authority_weight,
                audit_object_id=candidate.audit_object_id,
                page_spans=[PageSpan(**item) for item in candidate.page_map],
            )
            canonical_docs.append(self._document_index_payload(document_row))
            if pruning_ledger:
                pruning_ledger["source_path"] = str(candidate.path)
                pruning_rows.append(pruning_ledger)
            chunk_rows.extend(
                {
                    "chunk_id": chunk["id"],
                    "doc_id": chunk["document_id"],
                    "audit_object_id": chunk["audit_object_id"],
                    "chunk_seq": chunk["chunk_seq"],
                    "char_start": chunk["char_start"],
                    "char_end": chunk["char_end"],
                    "page_start": chunk["page_start"],
                    "page_end": chunk["page_end"],
                    "section_type": infer_section_type(chunk["text"], title=candidate.title, source_path=str(candidate.path)),
                    "text": chunk["text"],
                    "source_type": chunk["source_type"],
                    "authority_weight": chunk["authority_weight"],
                    "chunk_manifest_hash": chunk["chunk_manifest_hash"],
                    "chunk_feature_hash": chunk["chunk_feature_hash"],
                    "entity_density": chunk["entity_density"],
                    "legal_density": chunk["legal_density"],
                    "importance_score": chunk["importance_score"],
                }
                for chunk in chunks
            )

        duplicate_rows = []
        for candidate in candidates:
            duplicate_of = duplicates.get(candidate.doc_id)
            if duplicate_of is None:
                continue
            duplicate_rows.append(self._document_payload(candidate, is_duplicate=True, duplicate_of=duplicate_of))

        relations, audit_relations = build_relations(document_rows)

        with get_session() as session:
            if not full:
                for path in target_paths:
                    existing = session.execute(select(DocumentRecord).where(DocumentRecord.source_path == str(path))).scalar_one_or_none()
                    if existing:
                        self.delete_path(path)
            for row in document_rows + duplicate_rows:
                session.add(
                    DocumentRecord(
                        id=row["doc_id"],
                        source_path=row["source_path"],
                        source_type=row["source_type"],
                        authority_weight=row["authority_weight"],
                        audit_object_id=row["audit_object_id"],
                        content_hash=row["content_hash"],
                        pipeline_fingerprint=row["pipeline_fingerprint"],
                        title=row["title"],
                        text=row["text"],
                        structured_markdown=row["structured_markdown"],
                        page_count=row["page_count"],
                        page_map=row["page_map"],
                        is_duplicate=row["is_duplicate"],
                        duplicate_of=row["duplicate_of"],
                    )
                )
            session.flush()
            for row in chunk_rows:
                session.add(
                    ChunkRecord(
                        id=row["chunk_id"],
                        document_id=row["doc_id"],
                        audit_object_id=row["audit_object_id"],
                        text=row["text"],
                        chunk_seq=row["chunk_seq"],
                        char_start=row["char_start"],
                        char_end=row["char_end"],
                        page_start=row["page_start"],
                        page_end=row["page_end"],
                        section_type=row["section_type"],
                        source_type=row["source_type"],
                        authority_weight=row["authority_weight"],
                        chunk_manifest_hash=row["chunk_manifest_hash"],
                        chunk_feature_hash=row["chunk_feature_hash"],
                        entity_density=row["entity_density"],
                        legal_density=row["legal_density"],
                        importance_score=row["importance_score"],
                        embedding_status=EmbeddingStatus.PENDING.value,
                        embedding_version=settings.embedding_version,
                    )
                )
                session.add(
                    EmbeddingTaskRecord(
                        chunk_id=row["chunk_id"],
                        provider=settings.embedding_provider,
                        model=settings.embedding_model,
                        version=settings.embedding_version,
                        status=EmbeddingStatus.PENDING.value,
                    )
                )
            for row in pruning_rows:
                session.add(PruningLedgerRecord(**row))
            for relation in relations:
                session.add(
                    DocumentRelationRecord(
                        from_document_id=relation.from_document_id,
                        to_document_id=relation.to_document_id,
                        relation_type=relation.relation_type,
                        confidence=relation.confidence,
                    )
                )
            for row in audit_relations:
                session.add(AuditObjectRelationRecord(**row))
            session.commit()

        self.es.index_documents(canonical_docs)
        self.es.index_chunks(chunk_rows)
        summary = {
            "documents": len(document_rows),
            "duplicates": len(duplicate_rows),
            "chunks": len(chunk_rows),
            "pruned_documents": len(pruning_rows),
        }
        self._write_build_artifacts(
            full=full,
            paths_scanned=target_paths,
            canonical_rows=document_rows,
            duplicate_rows=duplicate_rows,
            chunk_rows=chunk_rows,
            pruning_rows=pruning_rows,
            summary=summary,
        )
        return summary

    def _write_build_artifacts(
        self,
        *,
        full: bool,
        paths_scanned: list[Path],
        canonical_rows: list[dict],
        duplicate_rows: list[dict],
        chunk_rows: list[dict],
        pruning_rows: list[dict],
        summary: dict[str, int],
    ) -> None:
        created_at = datetime.now(timezone.utc)
        build_id = hashlib.sha256(
            json.dumps(
                {
                    "full": full,
                    "paths": [str(path) for path in paths_scanned],
                    "summary": summary,
                    "fingerprint": settings.pipeline_fingerprint,
                },
                sort_keys=True,
            ).encode("utf-8")
        ).hexdigest()[:16]
        chunks_by_doc: dict[str, list[dict]] = defaultdict(list)
        for chunk in chunk_rows:
            chunks_by_doc[chunk["doc_id"]].append(chunk)
        documents = []
        for row in sorted(canonical_rows, key=lambda item: item["source_path"]):
            doc_chunks = sorted(chunks_by_doc[row["doc_id"]], key=lambda item: item["chunk_seq"])
            documents.append(
                {
                    "source_path": row["source_path"],
                    "doc_id": row["doc_id"],
                    "content_hash": row["content_hash"],
                    "source_type": row["source_type"],
                    "authority_weight": row["authority_weight"],
                    "audit_object_id": row["audit_object_id"],
                    "page_count": row["page_count"],
                    "chunk_count": len(doc_chunks),
                    "chunk_manifest_hashes": [chunk["chunk_manifest_hash"] for chunk in doc_chunks],
                    "chunk_feature_hashes": [chunk["chunk_feature_hash"] for chunk in doc_chunks],
                    "chunk_pages": [
                        {
                            "chunk_id": chunk["chunk_id"],
                            "page_start": chunk["page_start"],
                            "page_end": chunk["page_end"],
                        }
                        for chunk in doc_chunks
                    ],
                }
            )
        manifest = {
            "build_id": build_id,
            "created_at": created_at.isoformat(),
            "full": full,
            "pipeline_fingerprint": settings.pipeline_fingerprint,
            "summary": {**summary, "paths_scanned": len(paths_scanned)},
            "documents": documents,
            "duplicates": [
                {
                    "source_path": row["source_path"],
                    "doc_id": row["doc_id"],
                    "duplicate_of": row["duplicate_of"],
                    "content_hash": row["content_hash"],
                }
                for row in sorted(duplicate_rows, key=lambda item: item["source_path"])
            ],
            "pruning": [
                {
                    "doc_id": row["document_id"],
                    "source_path": row["source_path"],
                    "original_candidate_count": row["original_candidate_count"],
                    "kept_count": row["kept_count"],
                    "pruned_chunk_count": row["original_candidate_count"] - row["kept_count"],
                    "dropped_sequences": row["dropped_sequences"],
                    "reason": row["reason"],
                }
                for row in pruning_rows
            ],
        }
        manifest_name = f"{created_at.strftime('%Y%m%dT%H%M%SZ')}_{build_id}.json"
        manifest_path = settings.manifests_root / manifest_name
        manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")
        (settings.manifests_root / "latest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")

        pruning_path = settings.ledger_root / "pruning.jsonl"
        with pruning_path.open("a", encoding="utf-8") as handle:
            for row in manifest["pruning"]:
                handle.write(
                    json.dumps(
                        {
                            "build_id": build_id,
                            "created_at": created_at.isoformat(),
                            **row,
                        },
                        ensure_ascii=False,
                    )
                    + "\n"
                )
