#!/usr/bin/env python3
"""
Consulta híbrida com RRF para revisão do relatório V2.
"""

from __future__ import annotations

import argparse
import os
import re
import sys
from pathlib import Path
from typing import Any

import chromadb
from chromadb.config import Settings
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from google import genai

from index_gemini import (
    DEFAULT_EMBEDDING_DIM,
    DEFAULT_EMBEDDING_MODEL,
    embed_query,
    load_faiss_index,
)


ROOT = Path(__file__).resolve().parent
HIERARCHY_MAP = {
    "constituicao": "constituicao",
    "relatorio_v2": "relatorio_v2",
    "pecas": "pecas",
    "normas": "normas",
    "contexto": "contexto",
    "v1": "v1",
    "tramitacao": "tramitacao",
    "modelos": "modelos",
}
HIERARCHY_BOOST = {
    "constituicao": 2.0,
    "relatorio_v2": 1.8,
    "contexto": 1.4,
    "pecas": 1.3,
    "normas": 1.2,
    "v1": 1.0,
    "tramitacao": 0.8,
    "modelos": 0.7,
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Busca híbrida em Elasticsearch + ChromaDB + FAISS")
    parser.add_argument("query", help="Pergunta ou termo de busca")
    parser.add_argument("--k", type=int, default=5, help="Número de resultados finais")
    parser.add_argument("--es-url", default=os.getenv("ELASTICSEARCH_URL", "http://localhost:9200"))
    parser.add_argument("--es-index", default=os.getenv("ELASTICSEARCH_INDEX", "caf-final"))
    parser.add_argument("--collection", default=os.getenv("CHROMA_COLLECTION", "caf-final"))
    parser.add_argument("--chroma-dir", default=str(ROOT / ".local" / "chroma"))
    parser.add_argument("--embedding-dim", type=int, default=DEFAULT_EMBEDDING_DIM)
    parser.add_argument(
        "--embedding-model",
        default=os.getenv("GEMINI_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL),
    )
    parser.add_argument(
        "--hierarchy",
        "-H",
        choices=sorted(HIERARCHY_MAP.keys()),
        default=None,
        help="Filtra por hierarquia documental",
    )
    return parser.parse_args()


def rrf_score(rank: int, k: int = 60) -> float:
    return 1.0 / (k + rank + 1)


def detect_piece_number(query: str) -> int | None:
    match = re.search(r"(?:peça|peca)\s*0*(\d{1,3})", query, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def build_es_query(query: str, piece_number: int | None, hierarchy_label: str | None) -> dict[str, Any]:
    must_clause = {
        "multi_match": {
            "query": query,
            "fields": ["title^4", "section^2", "path^2", "text"],
        }
    }
    filters: list[dict[str, Any]] = []
    if piece_number is not None:
        filters.append({"term": {"piece_number": piece_number}})
    if hierarchy_label is not None:
        filters.append({"term": {"hierarchy_label": hierarchy_label}})
    if not filters:
        return must_clause
    return {"bool": {"must": [must_clause], "filter": filters}}


def normalize_hit(
    *,
    hit_id: str,
    text: str,
    metadata: dict[str, Any],
    source_name: str,
    engine_score: float,
) -> dict[str, Any]:
    payload = {
        "id": hit_id,
        "text": text,
        "metadata": metadata,
        "source": metadata.get("path", ""),
        "engine_scores": {source_name: engine_score},
        "provenance_set": {source_name},
    }
    return payload


def search_bm25(
    es: Elasticsearch,
    index_name: str,
    query: str,
    *,
    top_k: int,
    piece_number: int | None,
    hierarchy_label: str | None,
) -> list[dict[str, Any]]:
    response = es.search(index=index_name, size=top_k, query=build_es_query(query, piece_number, hierarchy_label))
    results: list[dict[str, Any]] = []
    for hit in response["hits"]["hits"]:
        src = hit["_source"]
        metadata = {
            "path": src["path"],
            "hierarchy_label": src.get("hierarchy_label", "outros"),
            "title": src["title"],
            "section": src["section"],
            "priority": src["priority"],
            "source_type": src["source_type"],
            "piece_number": src.get("piece_number"),
            "page_start": src.get("page_start"),
            "page_end": src.get("page_end"),
        }
        results.append(
            normalize_hit(
                hit_id=hit["_id"],
                text=src["text"],
                metadata=metadata,
                source_name="bm25",
                engine_score=float(hit["_score"] or 0.0),
            )
        )
    return results


def search_chroma(
    collection,
    query_embedding: list[float],
    *,
    top_k: int,
    piece_number: int | None,
    hierarchy_label: str | None,
) -> list[dict[str, Any]]:
    response = collection.query(query_embeddings=[query_embedding], n_results=top_k)
    results: list[dict[str, Any]] = []
    for hit_id, text, meta, distance in zip(
        response.get("ids", [[]])[0],
        response.get("documents", [[]])[0],
        response.get("metadatas", [[]])[0],
        response.get("distances", [[]])[0],
        strict=True,
    ):
        metadata = dict(meta or {})
        if piece_number is not None and metadata.get("piece_number") != piece_number:
            continue
        if hierarchy_label is not None and metadata.get("hierarchy_label") != hierarchy_label:
            continue
        results.append(
            normalize_hit(
                hit_id=hit_id,
                text=text,
                metadata=metadata,
                source_name="chroma",
                engine_score=1.0 - float(distance),
            )
        )
    return results


def search_faiss(
    query_embedding: list[float],
    *,
    top_k: int,
    piece_number: int | None,
    hierarchy_label: str | None,
) -> list[dict[str, Any]]:
    import faiss
    import numpy as np

    index, metadata_rows = load_faiss_index()
    if index is None or not metadata_rows:
        return []

    query_matrix = np.asarray([query_embedding], dtype=np.float32)
    faiss.normalize_L2(query_matrix)
    search_k = min(max(top_k * 4, top_k), index.ntotal)
    scores, indices = index.search(query_matrix, search_k)

    results: list[dict[str, Any]] = []
    for score, idx in zip(scores[0], indices[0], strict=True):
        if idx < 0:
            continue
        metadata = metadata_rows[idx]
        if piece_number is not None and metadata.get("piece_number") != piece_number:
            continue
        if hierarchy_label is not None and metadata.get("hierarchy_label") != hierarchy_label:
            continue
        results.append(
            normalize_hit(
                hit_id=metadata["chunk_id"],
                text=metadata["text"],
                metadata=metadata,
                source_name="faiss",
                engine_score=float(score),
            )
        )
        if len(results) >= top_k:
            break
    return results


def get_hierarchy_boost(metadata: dict[str, Any]) -> float:
    return HIERARCHY_BOOST.get(metadata.get("hierarchy_label", "outros"), 1.0)


def fuse_results(result_sets: list[list[dict[str, Any]]], top_k: int) -> list[dict[str, Any]]:
    combined: dict[str, dict[str, Any]] = {}
    rrf_scores: dict[str, float] = {}

    for result_set in result_sets:
        for rank, hit in enumerate(result_set):
            hit_id = hit["id"]
            rrf_scores[hit_id] = rrf_scores.get(hit_id, 0.0) + rrf_score(rank)
            if hit_id not in combined:
                combined[hit_id] = hit
                continue
            combined_hit = combined[hit_id]
            combined_hit["provenance_set"].update(hit["provenance_set"])
            combined_hit["engine_scores"].update(hit["engine_scores"])

    ranked: list[dict[str, Any]] = []
    for hit_id, score in sorted(rrf_scores.items(), key=lambda item: item[1], reverse=True):
        hit = combined[hit_id]
        boost = get_hierarchy_boost(hit["metadata"])
        hit["rrf_score"] = score
        hit["hierarchy_boost"] = boost
        hit["final_score"] = score * boost
        hit["provenance"] = "+".join(sorted(hit["provenance_set"]))
        ranked.append(hit)

    ranked.sort(key=lambda item: item["final_score"], reverse=True)
    return ranked[:top_k]


def format_location(metadata: dict[str, Any]) -> str:
    page_start = metadata.get("page_start")
    page_end = metadata.get("page_end")
    section = metadata.get("section") or "sem seção"
    if page_start and page_end and page_start != page_end:
        return f"p. {page_start}-{page_end} | {section}"
    if page_start:
        return f"p. {page_start} | {section}"
    return section


def print_results(query: str, results: list[dict[str, Any]], *, piece_number: int | None, hierarchy_label: str | None) -> None:
    print(f'Query: "{query}"')
    if piece_number is not None:
        print(f"Filtro de peça: {piece_number}")
    if hierarchy_label is not None:
        print(f"Filtro de hierarquia: {hierarchy_label}")
    if not results:
        print("Nenhum resultado relevante.")
        return

    print("\nTop resultados (RRF fusionado):")
    for idx, result in enumerate(results, 1):
        metadata = result["metadata"]
        preview = " ".join(result["text"].split())[:320]
        print(
            f"\n[{idx}] final={result['final_score']:.4f} "
            f"(rrf={result['rrf_score']:.4f}, boost={result['hierarchy_boost']:.1f}, {result['provenance']})"
        )
        print(f"    {metadata.get('path', '')}")
        print(f"    {format_location(metadata)} | {metadata.get('hierarchy_label', 'outros')}")
        print(f"    {preview}")


def main() -> int:
    args = parse_args()
    load_dotenv(ROOT / ".env")
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY/GOOGLE_API_KEY ausente")

    es = Elasticsearch(args.es_url, request_timeout=60)
    if not es.ping():
        raise SystemExit(f"Elasticsearch indisponível em {args.es_url}")

    chroma_client = chromadb.PersistentClient(
        path=args.chroma_dir,
        settings=Settings(anonymized_telemetry=False),
    )
    collection = chroma_client.get_collection(name=args.collection)
    gemini = genai.Client(api_key=api_key)

    hierarchy_label = HIERARCHY_MAP.get(args.hierarchy) if args.hierarchy else None
    piece_number = detect_piece_number(args.query)
    fetch_k = max(args.k * 6, 30)
    query_embedding = embed_query(gemini, args.embedding_model, args.query, args.embedding_dim)

    bm25_results = search_bm25(
        es,
        args.es_index,
        args.query,
        top_k=fetch_k,
        piece_number=piece_number,
        hierarchy_label=hierarchy_label,
    )
    chroma_results = search_chroma(
        collection,
        query_embedding,
        top_k=fetch_k,
        piece_number=piece_number,
        hierarchy_label=hierarchy_label,
    )
    faiss_results = search_faiss(
        query_embedding,
        top_k=fetch_k,
        piece_number=piece_number,
        hierarchy_label=hierarchy_label,
    )

    fused = fuse_results([bm25_results, chroma_results, faiss_results], args.k)
    print_results(args.query, fused, piece_number=piece_number, hierarchy_label=hierarchy_label)
    return 0


if __name__ == "__main__":
    sys.exit(main())
