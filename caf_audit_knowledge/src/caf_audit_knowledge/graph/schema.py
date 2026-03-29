from __future__ import annotations

from datetime import datetime

import strawberry
from strawberry.scalars import JSON
from sqlalchemy import select

from caf_audit_knowledge.answering import AnswerService, classify_query, register_feedback, register_scoring_feedback
from caf_audit_knowledge.constants import EmbeddingStatus, SourceType
from caf_audit_knowledge.ingest.pipeline import RepositoryIndexer
from caf_audit_knowledge.retrieval.service import RetrievalService
from caf_audit_knowledge.storage.db import get_session
from caf_audit_knowledge.storage.models import AuditObjectRelationRecord, ChunkRecord, DocumentRecord, DocumentRelationRecord

SourceTypeEnum = strawberry.enum(SourceType)
EmbeddingStatusEnum = strawberry.enum(EmbeddingStatus)


@strawberry.type
class ScoreBreakdown:
    bm25_raw: float | None = strawberry.field(name="bm25Raw", default=None)
    bm25: float | None = None
    vector_raw: float | None = strawberry.field(name="vectorRaw", default=None)
    vector: float | None = None
    reranker_raw: float | None = strawberry.field(name="rerankerRaw", default=None)
    reranker: float | None = None
    authority: float | None = None
    policy_multiplier: float | None = strawberry.field(name="policyMultiplier", default=None)
    query_type: str | None = strawberry.field(name="queryType", default=None)
    query_facets: JSON | None = strawberry.field(name="queryFacets", default=None)
    entity_density_raw: float | None = strawberry.field(name="entityDensityRaw", default=None)
    entity_density: float | None = strawberry.field(name="entityDensity", default=None)
    evidence_score: float | None = strawberry.field(name="evidenceScore", default=None)
    evidence_structural: bool | None = strawberry.field(name="evidenceStructural", default=None)
    evidence_boost_applied: bool | None = strawberry.field(name="evidenceBoostApplied", default=None)
    methodology_penalty_applied: bool | None = strawberry.field(name="methodologyPenaltyApplied", default=None)
    penalties: JSON | None = None
    boosts: JSON | None = None
    risk_flags: JSON | None = strawberry.field(name="riskFlags", default=None)
    risk_score: float | None = strawberry.field(name="riskScore", default=None)
    safe_mode: bool | None = strawberry.field(name="safeMode", default=None)
    scoring_profile: JSON | None = strawberry.field(name="scoringProfile", default=None)
    scoring_profile_source: str | None = strawberry.field(name="scoringProfileSource", default=None)
    final_score: float | None = strawberry.field(name="finalScore", default=None)


@strawberry.type
class Chunk:
    id: strawberry.ID
    document_id: strawberry.ID = strawberry.field(name="documentId")
    audit_object_id: str | None = strawberry.field(name="auditObjectId")
    text: str
    chunk_seq: int | None = strawberry.field(name="chunkSeq")
    char_start: int | None = strawberry.field(name="charStart")
    char_end: int | None = strawberry.field(name="charEnd")
    page_start: int | None = strawberry.field(name="pageStart")
    page_end: int | None = strawberry.field(name="pageEnd")
    section_type: str | None = strawberry.field(name="sectionType")
    source_type: SourceTypeEnum = strawberry.field(name="sourceType")
    authority_weight: float = strawberry.field(name="authorityWeight")
    chunk_manifest_hash: str = strawberry.field(name="chunkManifestHash")
    chunk_feature_hash: str = strawberry.field(name="chunkFeatureHash")
    entity_density: float | None = strawberry.field(name="entityDensity")
    legal_density: float | None = strawberry.field(name="legalDensity")
    importance_score: float | None = strawberry.field(name="importanceScore")
    embedding_status: EmbeddingStatusEnum | None = strawberry.field(name="embeddingStatus")
    embedding_version: str | None = strawberry.field(name="embeddingVersion")

    @staticmethod
    def from_record(record: ChunkRecord) -> "Chunk":
        return Chunk(
            id=record.id,
            document_id=record.document_id,
            audit_object_id=record.audit_object_id,
            text=record.text,
            chunk_seq=record.chunk_seq,
            char_start=record.char_start,
            char_end=record.char_end,
            page_start=record.page_start,
            page_end=record.page_end,
            section_type=record.section_type,
            source_type=SourceType(record.source_type),
            authority_weight=record.authority_weight,
            chunk_manifest_hash=record.chunk_manifest_hash,
            chunk_feature_hash=record.chunk_feature_hash,
            entity_density=record.entity_density,
            legal_density=record.legal_density,
            importance_score=record.importance_score,
            embedding_status=EmbeddingStatus(record.embedding_status) if record.embedding_status else None,
            embedding_version=record.embedding_version,
        )


@strawberry.type
class DocumentRelation:
    from_document_id: strawberry.ID = strawberry.field(name="fromDocumentId")
    to_document_id: strawberry.ID = strawberry.field(name="toDocumentId")
    relation_type: str = strawberry.field(name="relationType")
    confidence: float | None = None


@strawberry.type
class AuditObjectRelation:
    from_id: str = strawberry.field(name="from")
    to_id: str = strawberry.field(name="to")
    relation_type: str = strawberry.field(name="relationType")


@strawberry.type
class ConflictResult:
    conflict: bool
    source_types: list[SourceTypeEnum] = strawberry.field(name="sourceTypes")
    conflicting_chunks: list[Chunk] | None = strawberry.field(name="conflictingChunks", default=None)
    explanation: str | None = None


@strawberry.type
class Document:
    id: strawberry.ID
    source_path: str = strawberry.field(name="sourcePath")
    source_type: SourceTypeEnum = strawberry.field(name="sourceType")
    authority_weight: float = strawberry.field(name="authorityWeight")
    audit_object_id: str | None = strawberry.field(name="auditObjectId")
    content_hash: str = strawberry.field(name="contentHash")
    pipeline_fingerprint: str = strawberry.field(name="pipelineFingerprint")
    page_count: int = strawberry.field(name="pageCount")
    created_at: datetime | None = strawberry.field(name="createdAt")
    updated_at: datetime | None = strawberry.field(name="updatedAt")

    @strawberry.field
    def chunks(self) -> list[Chunk]:
        with get_session() as session:
            rows = session.execute(select(ChunkRecord).where(ChunkRecord.document_id == str(self.id)).order_by(ChunkRecord.chunk_seq)).scalars().all()
            return [Chunk.from_record(row) for row in rows]

    @strawberry.field(name="relatedDocuments")
    def related_documents(self) -> list[DocumentRelation]:
        with get_session() as session:
            rows = session.execute(
                select(DocumentRelationRecord).where(DocumentRelationRecord.from_document_id == str(self.id))
            ).scalars().all()
            return [DocumentRelation(from_document_id=row.from_document_id, to_document_id=row.to_document_id, relation_type=row.relation_type, confidence=row.confidence) for row in rows]

    @staticmethod
    def from_record(record: DocumentRecord) -> "Document":
        return Document(
            id=record.id,
            source_path=record.source_path,
            source_type=SourceType(record.source_type),
            authority_weight=record.authority_weight,
            audit_object_id=record.audit_object_id,
            content_hash=record.content_hash,
            pipeline_fingerprint=record.pipeline_fingerprint,
            page_count=record.page_count,
            created_at=record.created_at,
            updated_at=record.updated_at,
        )


@strawberry.type
class SearchResult:
    chunk: Chunk
    score: float
    score_breakdown: ScoreBreakdown = strawberry.field(name="scoreBreakdown")


@strawberry.type
class AnswerClassification:
    query_type: str = strawberry.field(name="queryType")
    confidence: float
    source: str
    used_llm_fallback: bool = strawberry.field(name="usedLlmFallback")
    facets: JSON = strawberry.field(default_factory=list)


@strawberry.type
class AnswerPayload:
    answer: str
    classification: AnswerClassification
    risk: JSON
    conflict: bool
    source_types: list[SourceTypeEnum] = strawberry.field(name="sourceTypes")
    aggregation: JSON | None = None
    evidence: list[SearchResult]
    explain_log: JSON = strawberry.field(name="explainLog")


@strawberry.type
class AuditObject:
    id: strawberry.ID

    @strawberry.field
    def documents(self) -> list[Document]:
        with get_session() as session:
            rows = session.execute(
                select(DocumentRecord).where(DocumentRecord.audit_object_id == str(self.id), DocumentRecord.is_duplicate.is_(False))
            ).scalars().all()
            return [Document.from_record(row) for row in rows]

    @strawberry.field
    def chunks(self) -> list[Chunk]:
        with get_session() as session:
            rows = session.execute(select(ChunkRecord).where(ChunkRecord.audit_object_id == str(self.id))).scalars().all()
            return [Chunk.from_record(row) for row in rows]

    @strawberry.field
    def evidence(self) -> list[Document]:
        return self._documents_by_source(SourceType.EVIDENCE)

    @strawberry.field
    def reports(self) -> list[Document]:
        return self._documents_by_source(SourceType.REPORT_FINAL, SourceType.REPORT_DRAFT)

    @strawberry.field
    def normative(self) -> list[Document]:
        return self._documents_by_source(SourceType.NORMATIVE)

    @strawberry.field
    def procedural(self) -> list[Document]:
        return self._documents_by_source(SourceType.PROCEDURAL)

    @strawberry.field(name="relatedObjects")
    def related_objects(self) -> list[AuditObjectRelation]:
        with get_session() as session:
            rows = session.execute(
                select(AuditObjectRelationRecord).where(AuditObjectRelationRecord.from_audit_object_id == str(self.id))
            ).scalars().all()
            return [AuditObjectRelation(from_id=row.from_audit_object_id, to_id=row.to_audit_object_id, relation_type=row.relation_type) for row in rows]

    @strawberry.field
    def conflicts(self) -> ConflictResult | None:
        results, conflict = RetrievalService().search(query=str(self.id), audit_object_id=str(self.id), top_k=5)
        return ConflictResult(
            conflict=conflict["conflict"],
            source_types=[SourceType(value) for value in conflict["source_types"]],
            conflicting_chunks=[Chunk.from_record(item.chunk) for item in results] if conflict["conflict"] else None,
            explanation="Multiple source domains appear in the top hybrid results." if conflict["conflict"] else None,
        )

    @strawberry.field
    def summary(self) -> str:
        with get_session() as session:
            count = session.execute(select(DocumentRecord).where(DocumentRecord.audit_object_id == str(self.id), DocumentRecord.is_duplicate.is_(False))).scalars().all()
        return f"{self.id} aggregates {len(count)} canonical documents linked through repository semantics."

    def _documents_by_source(self, *source_types: SourceType) -> list[Document]:
        with get_session() as session:
            rows = session.execute(
                select(DocumentRecord).where(
                    DocumentRecord.audit_object_id == str(self.id),
                    DocumentRecord.source_type.in_([item.value for item in source_types]),
                    DocumentRecord.is_duplicate.is_(False),
                )
            ).scalars().all()
            return [Document.from_record(row) for row in rows]


@strawberry.type
class Query:
    @strawberry.field
    def search(
        self,
        query: str,
        audit_object_id: str | None = strawberry.UNSET,
        source_types: list[SourceTypeEnum] | None = strawberry.UNSET,
        top_k: int = 5,
        explain: bool = False,
    ) -> list[SearchResult]:
        service = RetrievalService()
        hits, _conflict = service.search(
            query=query,
            audit_object_id=None if audit_object_id is strawberry.UNSET else audit_object_id,
            source_types=None if source_types is strawberry.UNSET else [item.value for item in source_types],
            top_k=top_k,
        )
        return [
            SearchResult(
                chunk=Chunk.from_record(hit.chunk),
                score=hit.score,
                score_breakdown=ScoreBreakdown(
                    bm25_raw=hit.score_breakdown["bm25Raw"] if explain else None,
                    bm25=hit.score_breakdown["bm25"] if explain else None,
                    vector_raw=hit.score_breakdown["vectorRaw"] if explain else None,
                    vector=hit.score_breakdown["vector"] if explain else None,
                    reranker_raw=hit.score_breakdown["rerankerRaw"] if explain else None,
                    reranker=hit.score_breakdown["reranker"] if explain else None,
                    authority=hit.score_breakdown["authority"] if explain else None,
                    policy_multiplier=hit.score_breakdown["policyMultiplier"] if explain else None,
                    query_type=hit.score_breakdown["queryType"] if explain else None,
                    query_facets=hit.score_breakdown["queryFacets"] if explain else None,
                    entity_density_raw=hit.score_breakdown["entityDensityRaw"] if explain else None,
                    entity_density=hit.score_breakdown["entityDensity"] if explain else None,
                    evidence_score=hit.score_breakdown["evidenceScore"] if explain else None,
                    evidence_structural=hit.score_breakdown["evidenceStructural"] if explain else None,
                    evidence_boost_applied=hit.score_breakdown["evidenceBoostApplied"] if explain else None,
                    methodology_penalty_applied=hit.score_breakdown["methodologyPenaltyApplied"] if explain else None,
                    penalties=hit.score_breakdown["penalties"] if explain else None,
                    boosts=hit.score_breakdown["boosts"] if explain else None,
                    risk_flags=hit.score_breakdown["riskFlags"] if explain else None,
                    risk_score=hit.score_breakdown["riskScore"] if explain else None,
                    safe_mode=hit.score_breakdown["safeMode"] if explain else None,
                    scoring_profile=hit.score_breakdown["scoringProfile"] if explain else None,
                    scoring_profile_source=hit.score_breakdown["scoringProfileSource"] if explain else None,
                    final_score=hit.score_breakdown["finalScore"] if explain else None,
                ),
            )
            for hit in hits
        ]

    @strawberry.field
    def answer(
        self,
        query: str,
        audit_object_id: str | None = strawberry.UNSET,
        source_types: list[SourceTypeEnum] | None = strawberry.UNSET,
        explain: bool = False,
    ) -> AnswerPayload:
        result = AnswerService().answer(
            query=query,
            audit_object_id=None if audit_object_id is strawberry.UNSET else audit_object_id,
            source_types=None if source_types is strawberry.UNSET else [item.value for item in source_types],
        )
        return AnswerPayload(
            answer=result.answer,
            classification=AnswerClassification(
                query_type=result.classification.query_type,
                confidence=result.classification.confidence,
                source=result.classification.source,
                used_llm_fallback=result.classification.used_llm_fallback,
                facets=list(result.classification.facets),
            ),
            risk={
                "flags": list(result.risk.flags),
                "score": result.risk.score,
                "safe_mode": result.risk.safe_mode,
            },
            conflict=result.conflict["conflict"],
            source_types=[SourceType(value) for value in result.conflict["source_types"]],
            aggregation=result.aggregation if explain else None,
            explain_log=result.explain_log,
            evidence=[
                SearchResult(
                    chunk=Chunk.from_record(hit.chunk),
                    score=hit.score,
                    score_breakdown=ScoreBreakdown(
                        bm25_raw=hit.score_breakdown["bm25Raw"] if explain else None,
                        bm25=hit.score_breakdown["bm25"] if explain else None,
                        vector_raw=hit.score_breakdown["vectorRaw"] if explain else None,
                        vector=hit.score_breakdown["vector"] if explain else None,
                        reranker_raw=hit.score_breakdown["rerankerRaw"] if explain else None,
                        reranker=hit.score_breakdown["reranker"] if explain else None,
                        authority=hit.score_breakdown["authority"] if explain else None,
                        policy_multiplier=hit.score_breakdown["policyMultiplier"] if explain else None,
                        query_type=hit.score_breakdown["queryType"] if explain else None,
                        query_facets=hit.score_breakdown["queryFacets"] if explain else None,
                        entity_density_raw=hit.score_breakdown["entityDensityRaw"] if explain else None,
                        entity_density=hit.score_breakdown["entityDensity"] if explain else None,
                        evidence_score=hit.score_breakdown["evidenceScore"] if explain else None,
                        evidence_structural=hit.score_breakdown["evidenceStructural"] if explain else None,
                        evidence_boost_applied=hit.score_breakdown["evidenceBoostApplied"] if explain else None,
                        methodology_penalty_applied=hit.score_breakdown["methodologyPenaltyApplied"] if explain else None,
                        penalties=hit.score_breakdown["penalties"] if explain else None,
                        boosts=hit.score_breakdown["boosts"] if explain else None,
                        risk_flags=hit.score_breakdown["riskFlags"] if explain else None,
                        risk_score=hit.score_breakdown["riskScore"] if explain else None,
                        safe_mode=hit.score_breakdown["safeMode"] if explain else None,
                        scoring_profile=hit.score_breakdown["scoringProfile"] if explain else None,
                        scoring_profile_source=hit.score_breakdown["scoringProfileSource"] if explain else None,
                        final_score=hit.score_breakdown["finalScore"] if explain else None,
                    ),
                )
                for hit in result.evidence
            ],
        )

    @strawberry.field(name="auditObject")
    def audit_object(self, id: strawberry.ID) -> AuditObject | None:
        return AuditObject(id=id)

    @strawberry.field
    def document(self, id: strawberry.ID) -> Document | None:
        record = RetrievalService().document(str(id))
        return Document.from_record(record) if record else None

    @strawberry.field
    def chunk(self, id: strawberry.ID) -> Chunk | None:
        record = RetrievalService().chunk(str(id))
        return Chunk.from_record(record) if record else None

    @strawberry.field(name="relatedDocuments")
    def related_documents(self, document_id: strawberry.ID, relation_type: str | None = None) -> list[DocumentRelation]:
        with get_session() as session:
            stmt = select(DocumentRelationRecord).where(DocumentRelationRecord.from_document_id == str(document_id))
            if relation_type:
                stmt = stmt.where(DocumentRelationRecord.relation_type == relation_type)
            rows = session.execute(stmt).scalars().all()
            return [DocumentRelation(from_document_id=row.from_document_id, to_document_id=row.to_document_id, relation_type=row.relation_type, confidence=row.confidence) for row in rows]

    @strawberry.field
    def evidence(self, audit_object_id: str) -> list[Document]:
        return AuditObject(id=audit_object_id).evidence()

    @strawberry.field
    def normative(self, audit_object_id: str) -> list[Document]:
        return AuditObject(id=audit_object_id).normative()

    @strawberry.field
    def conflicts(self, query: str | None = None, audit_object_id: str | None = None) -> ConflictResult:
        search_query = query or (audit_object_id or "")
        hits, conflict = RetrievalService().search(search_query, audit_object_id=audit_object_id, top_k=5)
        return ConflictResult(
            conflict=conflict["conflict"],
            source_types=[SourceType(value) for value in conflict["source_types"]],
            conflicting_chunks=[Chunk.from_record(hit.chunk) for hit in hits] if conflict["conflict"] else None,
            explanation="Top results span multiple source types." if conflict["conflict"] else None,
        )


@strawberry.type
class Mutation:
    @strawberry.field
    def reindex(self, full: bool = False) -> bool:
        RepositoryIndexer().build(full=full)
        return True

    @strawberry.field(name="recomputeEmbeddings")
    def recompute_embeddings(self, audit_object_id: str | None = None) -> bool:
        with get_session() as session:
            stmt = select(ChunkRecord)
            if audit_object_id:
                stmt = stmt.where(ChunkRecord.audit_object_id == audit_object_id)
            for chunk in session.execute(stmt).scalars().all():
                chunk.embedding_status = EmbeddingStatus.PENDING.value
            session.commit()
        return True

    @strawberry.field(name="registerQueryFeedback")
    def register_query_feedback(self, query: str, correct_type: str, predicted_type: str | None = None) -> bool:
        predicted = classify_query(query)
        register_feedback(
            query=query,
            predicted=predicted_type or predicted.query_type,
            correct=correct_type,
            confidence=predicted.confidence,
            source=predicted.source,
        )
        return True

    @strawberry.field(name="registerAnswerFeedback")
    def register_answer_feedback(self, query: str, success: bool, query_type: str | None = None, note: str | None = None) -> JSON:
        classification = classify_query(query)
        profile = register_scoring_feedback(
            query_type=query_type or classification.query_type,
            success=success,
            query=query,
            note=note,
        )
        return {
            "query_type": profile.query_type,
            "success": success,
            "weights": profile.weights,
            "source": profile.source,
        }


schema = strawberry.Schema(query=Query, mutation=Mutation)
