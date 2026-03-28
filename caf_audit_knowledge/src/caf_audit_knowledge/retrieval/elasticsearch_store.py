from __future__ import annotations

import json
from pathlib import Path

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

from caf_audit_knowledge.config import settings


class ElasticsearchStore:
    def __init__(self) -> None:
        kwargs = {}
        if settings.elasticsearch_user and settings.elasticsearch_password:
            kwargs["basic_auth"] = (settings.elasticsearch_user, settings.elasticsearch_password)
        self.client = Elasticsearch(settings.elasticsearch_url, **kwargs)
        config_root = settings.repository_root / "caf_audit_knowledge" / "config" / "elastic"
        self.document_mapping_path = config_root / "caf_documents.mapping.json"
        self.chunk_mapping_path = config_root / "caf_chunks.mapping.json"

    def ensure_indices(self, recreate: bool = False) -> None:
        for index_name, mapping_path in {
            "caf_documents": self.document_mapping_path,
            "caf_chunks": self.chunk_mapping_path,
        }.items():
            if recreate and self.client.indices.exists(index=index_name):
                self.client.indices.delete(index=index_name)
            if not self.client.indices.exists(index=index_name):
                mapping = json.loads(Path(mapping_path).read_text(encoding="utf-8"))
                self.client.indices.create(index=index_name, **mapping)

    def index_documents(self, documents: list[dict]) -> None:
        if not documents:
            return
        bulk(
            self.client,
            [{"_index": "caf_documents", "_id": item["doc_id"], "_source": item} for item in documents],
            refresh=True,
        )

    def index_chunks(self, chunks: list[dict]) -> None:
        if not chunks:
            return
        bulk(
            self.client,
            [{"_index": "caf_chunks", "_id": item["chunk_id"], "_source": item} for item in chunks],
            refresh=True,
        )

    def delete_document(self, doc_id: str) -> None:
        self.client.delete(index="caf_documents", id=doc_id, ignore=[404], refresh=True)
        self.client.delete_by_query(
            index="caf_chunks",
            query={"term": {"doc_id": doc_id}},
            ignore_unavailable=True,
            refresh=True,
        )

    def search_chunks(self, query: str, audit_object_id: str | None, source_types: list[str] | None, size: int = 20) -> list[dict]:
        filters = []
        if audit_object_id:
            filters.append({"term": {"audit_object_id": audit_object_id}})
        if source_types:
            filters.append({"terms": {"source_type": source_types}})
        body = {
            "size": size,
            "query": {
                "bool": {
                    "must": [{"multi_match": {"query": query, "fields": ["text^3", "audit_object_id", "source_type"]}}],
                    "filter": filters,
                }
            },
        }
        response = self.client.search(index="caf_chunks", **body)
        return response["hits"]["hits"]
