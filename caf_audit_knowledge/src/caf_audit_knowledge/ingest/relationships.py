from __future__ import annotations

import re
from collections import defaultdict
from dataclasses import dataclass

from caf_audit_knowledge.constants import SourceType

PIECE_MENTION_RE = re.compile(r"peça\s*0*([0-9]{1,3})", re.IGNORECASE)


@dataclass(frozen=True)
class RelationCandidate:
    from_document_id: str
    to_document_id: str
    relation_type: str
    confidence: float


def build_relations(documents: list[dict]) -> tuple[list[RelationCandidate], list[dict]]:
    piece_index: dict[int, list[dict]] = defaultdict(list)
    audit_lookup: dict[str, list[dict]] = defaultdict(list)
    for document in documents:
        piece = document.get("piece_number")
        if piece is not None:
            piece_index[piece].append(document)
        if document.get("audit_object_id"):
            audit_lookup[document["audit_object_id"]].append(document)

    relations: list[RelationCandidate] = []
    audit_relations: set[tuple[str, str, str]] = set()

    for document in documents:
        text = document["text"]
        doc_id = document["doc_id"]
        audit_object_id = document.get("audit_object_id")

        for match in PIECE_MENTION_RE.findall(text):
            for referenced in piece_index.get(int(match), []):
                if referenced["doc_id"] == doc_id:
                    continue
                relations.append(
                    RelationCandidate(
                        from_document_id=doc_id,
                        to_document_id=referenced["doc_id"],
                        relation_type="references",
                        confidence=0.85,
                    )
                )
                if audit_object_id and referenced.get("audit_object_id") and audit_object_id != referenced["audit_object_id"]:
                    audit_relations.add((audit_object_id, referenced["audit_object_id"], "overlaps"))

        if not audit_object_id:
            continue
        for related in audit_lookup[audit_object_id]:
            if related["doc_id"] == doc_id:
                continue
            pair = {document["source_type"], related["source_type"]}
            if SourceType.REPORT_FINAL.value in pair or SourceType.REPORT_DRAFT.value in pair:
                relation_type = "supports"
            elif SourceType.PROCEDURAL.value in pair:
                relation_type = "references"
            else:
                relation_type = "derived_from"
            relations.append(
                RelationCandidate(
                    from_document_id=doc_id,
                    to_document_id=related["doc_id"],
                    relation_type=relation_type,
                    confidence=0.7,
                )
            )

    audit_relation_rows = [
        {"from_audit_object_id": left, "to_audit_object_id": right, "relation_type": relation_type}
        for left, right, relation_type in sorted(audit_relations)
    ]
    unique_relations = {(item.from_document_id, item.to_document_id, item.relation_type): item for item in relations}
    return list(unique_relations.values()), audit_relation_rows
