from __future__ import annotations

import json
from pathlib import Path

import typer
import uvicorn
from sqlalchemy import func, select
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from caf_audit_knowledge.answering import AnswerService, classify_query, get_query_classifier, get_scoring_policy, register_feedback, register_scoring_feedback
from caf_audit_knowledge.config import settings
from caf_audit_knowledge.embeddings.worker import EmbeddingWorker
from caf_audit_knowledge.graph.app import create_app
from caf_audit_knowledge.ingest.pipeline import RepositoryIndexer
from caf_audit_knowledge.repo_semantics import should_ignore_path
from caf_audit_knowledge.retrieval.service import RetrievalService
from caf_audit_knowledge.storage.db import get_session
from caf_audit_knowledge.storage.models import ChunkRecord, DocumentRecord, EmbeddingTaskRecord

app = typer.Typer(no_args_is_help=True)
debug_app = typer.Typer(no_args_is_help=True)


def _query_payload(text: str, audit_object_id: str | None = None, top_k: int = 5, explain: bool = False) -> dict:
    hits, conflict, trace = RetrievalService().search_with_trace(query=text, audit_object_id=audit_object_id, top_k=top_k)
    payload = {
        "conflict": conflict["conflict"],
        "source_types": conflict["source_types"],
        "results": [
            {
                "chunk_id": hit.chunk.id,
                "doc_id": hit.chunk.document_id,
                "source_type": hit.chunk.source_type,
                "authority_weight": hit.chunk.authority_weight,
                "audit_object_id": hit.chunk.audit_object_id,
                "page_start": hit.chunk.page_start,
                "page_end": hit.chunk.page_end,
                "section_type": hit.chunk.section_type,
                "citation": _format_page_citation(hit.chunk.page_start, hit.chunk.page_end),
                "score": hit.score,
                "score_breakdown": hit.score_breakdown if explain else {},
                "reasons": hit.reasons if explain else [],
                "text": hit.chunk.text,
            }
            for hit in hits
        ],
    }
    if explain:
        payload["query_context"] = trace["query_context"]
        payload["risk"] = trace["risk"]
        payload["filtered_out"] = trace.get("filtered_out", [])
    return payload


def _answer_payload(text: str, audit_object_id: str | None = None, explain: bool = False) -> dict:
    result = AnswerService().answer(query=text, audit_object_id=audit_object_id)
    payload = {
        "query": text,
        "classification": {
            "type": result.classification.query_type,
            "confidence": result.classification.confidence,
            "source": result.classification.source,
            "used_llm_fallback": result.classification.used_llm_fallback,
            "facets": list(result.classification.facets),
        },
        "risk": {
            "flags": list(result.risk.flags),
            "score": result.risk.score,
            "safe_mode": result.risk.safe_mode,
        },
        "conflict": result.conflict["conflict"],
        "source_types": result.conflict["source_types"],
        "answer": result.answer,
        "explain_log": result.explain_log if explain else {},
        "evidence": [
            {
                "chunk_id": hit.chunk.id,
                "doc_id": hit.chunk.document_id,
                "source_type": hit.chunk.source_type,
                "authority_weight": hit.chunk.authority_weight,
                "audit_object_id": hit.chunk.audit_object_id,
                "page_start": hit.chunk.page_start,
                "page_end": hit.chunk.page_end,
                "section_type": hit.chunk.section_type,
                "citation": _format_page_citation(hit.chunk.page_start, hit.chunk.page_end),
                "score": hit.score,
                "score_breakdown": hit.score_breakdown if explain else {},
                "reasons": hit.reasons if explain else [],
            }
            for hit in result.evidence
        ],
    }
    return payload


def _format_page_citation(page_start: int | None, page_end: int | None) -> str | None:
    if page_start is None and page_end is None:
        return None
    if page_start == page_end or page_end is None:
        return f"p. {page_start}"
    if page_start is None:
        return f"p. {page_end}"
    return f"pp. {page_start}-{page_end}"


@app.command("init-stores")
def init_stores(recreate_indices: bool = typer.Option(False, "--recreate-indices")) -> None:
    RepositoryIndexer().init_stores(recreate_indices=recreate_indices)
    typer.echo("Stores initialized.")


@app.command()
def build(full: bool = typer.Option(False, "--full")) -> None:
    result = RepositoryIndexer().build(full=full)
    typer.echo(json.dumps(result, indent=2))


@app.command()
def query(text: str, audit_object_id: str | None = None, explain: bool = False) -> None:
    typer.echo(json.dumps(_query_payload(text, audit_object_id=audit_object_id, explain=explain), indent=2, ensure_ascii=False))


@app.command()
def answer(text: str, audit_object_id: str | None = None, explain: bool = False) -> None:
    typer.echo(json.dumps(_answer_payload(text, audit_object_id=audit_object_id, explain=explain), indent=2, ensure_ascii=False))


@app.command("feedback-query")
def feedback_query(
    text: str,
    correct_type: str,
    predicted_type: str | None = None,
) -> None:
    predicted = classify_query(text)
    learned = register_feedback(
        query=text,
        predicted=predicted_type or predicted.query_type,
        correct=correct_type,
        confidence=predicted.confidence,
        source=predicted.source,
    )
    typer.echo(
        json.dumps(
            {
                "query": text,
                "predicted": predicted_type or predicted.query_type,
                "correct": correct_type,
                "patterns": learned,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


@app.command("feedback-answer")
def feedback_answer(
    text: str,
    success: bool = typer.Option(..., "--success/--failure"),
    query_type: str | None = None,
    note: str | None = None,
) -> None:
    classification = classify_query(text)
    profile = register_scoring_feedback(
        query_type=query_type or classification.query_type,
        success=success,
        query=text,
        note=note,
    )
    typer.echo(
        json.dumps(
            {
                "query": text,
                "query_type": profile.query_type,
                "success": success,
                "weights": profile.weights,
                "source": profile.source,
            },
            indent=2,
            ensure_ascii=False,
        )
    )


@app.command("debug-query")
def debug_query(text: str, audit_object_id: str | None = None, top_k: int = 5, explain: bool = True) -> None:
    typer.echo(json.dumps(_query_payload(text, audit_object_id=audit_object_id, top_k=top_k, explain=explain), indent=2, ensure_ascii=False))


@app.command()
def validate() -> None:
    with get_session() as session:
        discarded = session.execute(select(func.count()).select_from(DocumentRecord).where(DocumentRecord.source_path.contains("99_DISCARDED"))).scalar_one()
        duplicates_with_chunks = session.execute(
            select(func.count())
            .select_from(ChunkRecord)
            .join(DocumentRecord, DocumentRecord.id == ChunkRecord.document_id)
            .where(DocumentRecord.is_duplicate.is_(True))
        ).scalar_one()
        over_chunk_limit = session.execute(
            select(ChunkRecord.document_id, func.count(ChunkRecord.id).label("chunk_count"))
            .group_by(ChunkRecord.document_id)
            .having(func.count(ChunkRecord.id) > settings.max_chunks_per_doc)
        ).all()
    payload = {
        "discarded_indexed": discarded,
        "duplicate_chunks": duplicates_with_chunks,
        "documents_over_chunk_limit": len(over_chunk_limit),
        "valid": discarded == 0 and duplicates_with_chunks == 0 and len(over_chunk_limit) == 0,
    }
    typer.echo(json.dumps(payload, indent=2))


@app.command("embed-worker")
def embed_worker() -> None:
    EmbeddingWorker().run_forever()


@app.command()
def serve() -> None:
    uvicorn.run(create_app(), host=settings.graphql_host, port=settings.graphql_port)


@debug_app.command("list-docs")
def debug_list_docs(limit: int = 20, include_duplicates: bool = False) -> None:
    with get_session() as session:
        stmt = select(DocumentRecord)
        if not include_duplicates:
            stmt = stmt.where(DocumentRecord.is_duplicate.is_(False))
        rows = session.execute(stmt.order_by(DocumentRecord.source_path).limit(limit)).scalars().all()
    payload = [
        {
            "doc_id": row.id,
            "source_path": row.source_path,
            "source_type": row.source_type,
            "audit_object_id": row.audit_object_id,
            "authority_weight": row.authority_weight,
            "page_count": row.page_count,
            "is_duplicate": row.is_duplicate,
            "duplicate_of": row.duplicate_of,
        }
        for row in rows
    ]
    typer.echo(json.dumps(payload, indent=2, ensure_ascii=False))


@debug_app.command("stats")
def debug_stats() -> None:
    source_file_count = len(RepositoryIndexer().discover_paths())
    with get_session() as session:
        indexed_docs = session.execute(select(func.count()).select_from(DocumentRecord).where(DocumentRecord.is_duplicate.is_(False))).scalar_one()
        duplicate_docs = session.execute(select(func.count()).select_from(DocumentRecord).where(DocumentRecord.is_duplicate.is_(True))).scalar_one()
        chunk_count = session.execute(select(func.count()).select_from(ChunkRecord)).scalar_one()
        excluded_leaks = {
            "discarded": session.execute(
                select(func.count()).select_from(DocumentRecord).where(DocumentRecord.source_path.contains("99_DISCARDED"))
            ).scalar_one(),
            "bak": session.execute(
                select(func.count()).select_from(DocumentRecord).where(DocumentRecord.source_path.contains(".bak"))
            ).scalar_one(),
            "report_copy": session.execute(
                select(func.count()).select_from(DocumentRecord).where(DocumentRecord.source_path.contains("01_RELATORIO_V2 copy"))
            ).scalar_one(),
        }
        by_source = session.execute(
            select(DocumentRecord.source_type, func.count()).where(DocumentRecord.is_duplicate.is_(False)).group_by(DocumentRecord.source_type)
        ).all()
        by_audit = session.execute(
            select(DocumentRecord.audit_object_id, func.count())
            .where(DocumentRecord.is_duplicate.is_(False))
            .group_by(DocumentRecord.audit_object_id)
        ).all()
        embedding_status = session.execute(
            select(EmbeddingTaskRecord.status, func.count()).group_by(EmbeddingTaskRecord.status)
        ).all()
    payload = {
        "source_files_discovered": source_file_count,
        "indexed_documents": indexed_docs,
        "duplicates_skipped": duplicate_docs,
        "chunk_count": chunk_count,
        "excluded_path_leaks": excluded_leaks,
        "source_type_counts": {key or "unknown": value for key, value in by_source},
        "audit_object_counts": {key or "unscoped": value for key, value in by_audit},
        "embedding_status_counts": {key: value for key, value in embedding_status},
        "latest_manifest": str(settings.manifests_root / "latest.json"),
        "pruning_ledger": str(settings.ledger_root / "pruning.jsonl"),
    }
    typer.echo(json.dumps(payload, indent=2, ensure_ascii=False))


def _load_manifest(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


@debug_app.command("compare-chunks")
def debug_compare_chunks() -> None:
    manifest_paths = sorted(path for path in settings.manifests_root.glob("*.json") if path.name != "latest.json")
    if len(manifest_paths) < 2:
        raise typer.Exit(code=1)
    left = _load_manifest(manifest_paths[-2])
    right = _load_manifest(manifest_paths[-1])
    left_map = {row["source_path"]: row for row in left["documents"]}
    right_map = {row["source_path"]: row for row in right["documents"]}
    changed_paths = []
    for source_path in sorted(set(left_map) | set(right_map)):
        if left_map.get(source_path) != right_map.get(source_path):
            changed_paths.append(source_path)
    payload = {
        "left_manifest": str(manifest_paths[-2]),
        "right_manifest": str(manifest_paths[-1]),
        "identical": len(changed_paths) == 0,
        "left_chunk_count": left["summary"]["chunks"],
        "right_chunk_count": right["summary"]["chunks"],
        "left_document_count": left["summary"]["documents"],
        "right_document_count": right["summary"]["documents"],
        "changed_paths": changed_paths[:25],
        "changed_path_count": len(changed_paths),
    }
    typer.echo(json.dumps(payload, indent=2, ensure_ascii=False))


@debug_app.command("query")
def debug_subquery(text: str, audit_object_id: str | None = None, top_k: int = 5, explain: bool = True) -> None:
    typer.echo(json.dumps(_query_payload(text, audit_object_id=audit_object_id, top_k=top_k, explain=explain), indent=2, ensure_ascii=False))


@debug_app.command("classify-query")
def debug_classify_query(text: str) -> None:
    result = classify_query(text)
    typer.echo(
        json.dumps(
            {
                "query": text,
                "type": result.query_type,
                "confidence": result.confidence,
                "source": result.source,
                "used_llm_fallback": result.used_llm_fallback,
                "facets": list(result.facets),
            },
            indent=2,
            ensure_ascii=False,
        )
    )


@debug_app.command("query-patterns")
def debug_query_patterns() -> None:
    typer.echo(json.dumps(get_query_classifier().patterns(), indent=2, ensure_ascii=False))


@debug_app.command("query-feedback")
def debug_query_feedback(limit: int = 20) -> None:
    typer.echo(json.dumps(get_query_classifier().feedback_history(limit=limit), indent=2, ensure_ascii=False))


@debug_app.command("query-logs")
def debug_query_logs(limit: int = 5) -> None:
    if not settings.query_logs_path.exists():
        typer.echo("[]")
        return
    rows = [json.loads(line) for line in settings.query_logs_path.read_text(encoding="utf-8").splitlines() if line.strip()]
    typer.echo(json.dumps(rows[-limit:], indent=2, ensure_ascii=False))


@debug_app.command("scoring-profiles")
def debug_scoring_profiles() -> None:
    typer.echo(json.dumps(get_scoring_policy().profiles(), indent=2, ensure_ascii=False))


@debug_app.command("scoring-feedback")
def debug_scoring_feedback(limit: int = 20) -> None:
    typer.echo(json.dumps(get_scoring_policy().feedback_history(limit=limit), indent=2, ensure_ascii=False))


class _WatchHandler(FileSystemEventHandler):
    def __init__(self) -> None:
        self.indexer = RepositoryIndexer()

    def _handle(self, src_path: str, deleted: bool = False) -> None:
        path = Path(src_path)
        if should_ignore_path(path):
            return
        if deleted:
            self.indexer.delete_path(path)
            typer.echo(f"Deleted index state for {path}")
            return
        result = self.indexer.build(full=False, paths=[path])
        typer.echo(json.dumps({"path": str(path), **result}, ensure_ascii=False))

    def on_created(self, event) -> None:
        if not event.is_directory:
            self._handle(event.src_path)

    def on_modified(self, event) -> None:
        if not event.is_directory:
            self._handle(event.src_path)

    def on_deleted(self, event) -> None:
        if not event.is_directory:
            self._handle(event.src_path, deleted=True)


@app.command()
def watch() -> None:
    handler = _WatchHandler()
    observer = Observer()
    for dirname in [
        "00_CONTEXTO",
        "01_RELATORIO_V2",
        "02_FONTE_VERDADE",
        "03_RELATORIO_V1",
        "04_PECAS_EVIDENCIA",
        "05_PECAS_TRAMITACAO",
        "06_NORMAS_CRITERIOS",
        "07_MODELOS_TCU",
    ]:
        observer.schedule(handler, str(settings.repository_root / dirname), recursive=True)
    observer.start()
    typer.echo("Watching source directories...")
    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
        observer.join()


app.add_typer(debug_app, name="debug")
