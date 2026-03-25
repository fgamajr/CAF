#!/usr/bin/env python3
"""
Executa as baterias de teste do indexador e gera relatório markdown/json.
"""

from __future__ import annotations

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Callable

import chromadb
import numpy as np
from chromadb.config import Settings
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from google import genai

from index_gemini import (
    DEFAULT_COLLECTION,
    DEFAULT_EMBEDDING_DIM,
    DEFAULT_EMBEDDING_MODEL,
    DEFAULT_ES_INDEX,
    CHROMA_DIR,
    prepare_embedding_text,
)
from search_review import (
    HIERARCHY_MAP,
    detect_piece_number,
    fuse_results,
    search_bm25,
    search_chroma,
    search_faiss,
)


ROOT = Path(__file__).resolve().parent
JSON_DEFAULT = ROOT / ".local" / "index_state" / "indexer_test_results_v2.json"
MD_DEFAULT = ROOT / "TESTES_INDEXADOR_V2.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Roda baterias de teste do indexador.")
    parser.add_argument("--battery", type=int, choices=range(1, 9), default=None)
    parser.add_argument("--output", default=str(MD_DEFAULT))
    parser.add_argument("--json-output", default=str(JSON_DEFAULT))
    parser.add_argument("--collection", default=DEFAULT_COLLECTION)
    parser.add_argument("--es-index", default=DEFAULT_ES_INDEX)
    return parser.parse_args()


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def contains_number(text: str, token: str) -> bool:
    variants = {token, token.replace(".", ","), token.replace(",", ".")}
    return any(variant in text for variant in variants)


def hierarchy_of(path: str) -> str:
    if path.startswith("02_FONTE_VERDADE/"):
        return "constituicao"
    if path.startswith("01_RELATORIO_V2/"):
        return "relatorio_v2"
    if path.startswith("04_PECAS_EVIDENCIA/"):
        return "pecas"
    if path.startswith("06_NORMAS_CRITERIOS/"):
        return "normas"
    if path.startswith("00_CONTEXTO/"):
        return "contexto"
    if path.startswith("03_RELATORIO_V1/"):
        return "v1"
    if path.startswith("05_PECAS_TRAMITACAO/"):
        return "tramitacao"
    if path.startswith("07_MODELOS_TCU/"):
        return "modelos"
    return "outros"


def is_matrix(path: str) -> bool:
    return path.startswith("02_FONTE_VERDADE/")


class TestRunner:
    def __init__(self, args: argparse.Namespace) -> None:
        load_dotenv(ROOT / ".env")
        api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise SystemExit("GEMINI_API_KEY/GOOGLE_API_KEY ausente")
        self.args = args
        self.gemini = genai.Client(api_key=api_key)
        self.es = Elasticsearch(os.getenv("ELASTICSEARCH_URL", "http://localhost:9200"), request_timeout=60)
        self.chroma = chromadb.PersistentClient(
            path=str(CHROMA_DIR),
            settings=Settings(anonymized_telemetry=False),
        )
        self.collection = self.chroma.get_collection(args.collection)
        self.query_cache: dict[tuple[str, int, str | None], dict[str, object]] = {}
        self.es_count = self.es.count(index=args.es_index)["count"]
        self.chroma_count = self.collection.count()
        sample = self.collection.get(limit=1, include=["embeddings"])
        self.chroma_dim = len(sample["embeddings"][0])

    def run_query(self, query: str, k: int = 5, hierarchy: str | None = None) -> dict[str, object]:
        key = (query, k, hierarchy)
        if key in self.query_cache:
            return self.query_cache[key]
        hierarchy_label = HIERARCHY_MAP.get(hierarchy) if hierarchy else None
        piece_number = detect_piece_number(query)
        fetch_k = max(k * 6, 30)
        query_vector = self.embed_query(query)
        bm25 = search_bm25(
            self.es,
            self.args.es_index,
            query,
            top_k=fetch_k,
            piece_number=piece_number,
            hierarchy_label=hierarchy_label,
        )
        chroma_hits = search_chroma(
            self.collection,
            query_vector,
            top_k=fetch_k,
            piece_number=piece_number,
            hierarchy_label=hierarchy_label,
        )
        faiss_hits = search_faiss(
            query_vector,
            top_k=fetch_k,
            piece_number=piece_number,
            hierarchy_label=hierarchy_label,
        )
        fused = fuse_results([bm25, chroma_hits, faiss_hits], k)
        payload = {
            "query": query,
            "hierarchy": hierarchy,
            "piece_number": piece_number,
            "results": fused,
        }
        self.query_cache[key] = payload
        return payload

    def embed_query(self, query: str) -> list[float]:
        result = self.gemini.models.embed_content(
            model=DEFAULT_EMBEDDING_MODEL,
            contents=[prepare_embedding_text(query, task_type="RETRIEVAL_QUERY")],
            config=genai.types.EmbedContentConfig(
                task_type="RETRIEVAL_QUERY",
                output_dimensionality=DEFAULT_EMBEDDING_DIM,
            ),
        )
        return list(result.embeddings[0].values)

    @staticmethod
    def result_path(res: dict[str, object] | None) -> str:
        if not res:
            return ""
        metadata = res.get("metadata", {})
        if isinstance(metadata, dict):
            return str(metadata.get("path", ""))
        return ""

    @staticmethod
    def result_text(res: dict[str, object] | None) -> str:
        if not res:
            return ""
        return str(res.get("text", ""))

    @staticmethod
    def result_prov(res: dict[str, object] | None) -> str:
        if not res:
            return ""
        return str(res.get("provenance", ""))

    @staticmethod
    def result_rrf(res: dict[str, object] | None) -> float:
        if not res:
            return 0.0
        return float(res.get("rrf_score", 0.0))

    def find_first(
        self,
        results: list[dict[str, object]],
        predicate: Callable[[str], bool],
        top_n: int | None = None,
    ) -> dict[str, object] | None:
        subset = results if top_n is None else results[:top_n]
        for result in subset:
            if predicate(self.result_path(result)):
                return result
        return None


def battery_1(runner: TestRunner) -> list[dict[str, object]]:
    tests: list[dict[str, object]] = []
    resp = runner.gemini.models.embed_content(
        model=DEFAULT_EMBEDDING_MODEL,
        contents=["teste de dimensão"],
        config=genai.types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=DEFAULT_EMBEDDING_DIM,
        ),
    )
    dim = len(resp.embeddings[0].values)
    tests.append({"name": "1.1 Dimensão do vetor Gemini", "pass": dim == 1024, "details": f"Dimensão: {dim}"})
    tests.append(
        {
            "name": "1.2 Dimensão do ChromaDB",
            "pass": runner.chroma_dim == 1024 and runner.chroma_count > 0,
            "details": f"Chroma dimensão: {runner.chroma_dim}; total: {runner.chroma_count}",
        }
    )
    tests.append(
        {
            "name": "1.3 Contagem do Elasticsearch",
            "pass": runner.es_count == runner.chroma_count,
            "details": f"ES count: {runner.es_count}",
        }
    )
    text = "qualidade de dados do cadastro da agricultura familiar"
    raw_doc = runner.gemini.models.embed_content(
        model=DEFAULT_EMBEDDING_MODEL,
        contents=[text],
        config=genai.types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=DEFAULT_EMBEDDING_DIM,
        ),
    )
    raw_query = runner.gemini.models.embed_content(
        model=DEFAULT_EMBEDDING_MODEL,
        contents=[text],
        config=genai.types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=DEFAULT_EMBEDDING_DIM,
        ),
    )
    raw_doc_vec = np.array(raw_doc.embeddings[0].values)
    raw_query_vec = np.array(raw_query.embeddings[0].values)
    raw_equal = bool(np.allclose(raw_doc_vec, raw_query_vec))

    eff_doc = runner.gemini.models.embed_content(
        model=DEFAULT_EMBEDDING_MODEL,
        contents=[prepare_embedding_text(text, task_type="RETRIEVAL_DOCUMENT")],
        config=genai.types.EmbedContentConfig(
            task_type="RETRIEVAL_DOCUMENT",
            output_dimensionality=DEFAULT_EMBEDDING_DIM,
        ),
    )
    eff_query = runner.gemini.models.embed_content(
        model=DEFAULT_EMBEDDING_MODEL,
        contents=[prepare_embedding_text(text, task_type="RETRIEVAL_QUERY")],
        config=genai.types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=DEFAULT_EMBEDDING_DIM,
        ),
    )
    eff_doc_vec = np.array(eff_doc.embeddings[0].values)
    eff_query_vec = np.array(eff_query.embeddings[0].values)
    eff_equal = bool(np.allclose(eff_doc_vec, eff_query_vec))
    tests.append(
        {
            "name": "1.4 Diferenciação query/documento na pipeline",
            "pass": not eff_equal,
            "details": f"raw_task_type_igual={raw_equal}; pipeline_com_prefixo_igual={eff_equal}",
        }
    )
    return tests


def battery_2(runner: TestRunner) -> list[dict[str, object]]:
    queries = [
        ("27,1% docs", "27,1% documentos semanticamente inadequados", "27,1%"),
        ("53,55% área", "53,55% divergência crítica de área", "53,55%"),
        ("33,33% tipo", "33,33% tipo documental inadequado", "33,33%"),
        ("68,7% DPI", "68,7% resolução inferior 300 DPI", "68,7%"),
        ("45,92% cartográfico", "45,92% erro cartográfico imóveis", "45,92%"),
        ("55,27% duplicações", "55,27% duplicações espaciais", "55,27%"),
        ("15,92% municipal", "15,92% inconsistência municipal", "15,92%"),
        ("632 municípios", "632 municípios inflação cadastral", "632"),
        ("3.097 falecidos", "3.097 titulares falecidos Sisobi", "3.097"),
        ("138 menores", "138 menores responsáveis unidades familiares", "138"),
        ("90,62% e-mails", "90,62% e-mails fictícios pessoa física", "90,62%"),
        ("93,7% CEPs", "93,7% CEPs genéricos", "93,7%"),
        ("907 renda", "907 registros renda superior milhão", "907"),
        ("39 PJs CNAE", "39 pessoas jurídicas CNAE incompatível", "39"),
        ("94,1% metadados", "94,1% descrições dicionário inadequadas", "94,1%"),
        ("84% numéricos", "84% campos numéricos sem unidade medida", "84%"),
        ("92% temporais", "92% campos temporais ambíguos", "92%"),
        ("59,6 bi Pronaf", "59,6 bilhões Pronaf safra", "59,6"),
        ("Leaflet 92,36%", "92,36% 16,59% Leaflet duplicações", "92,36%"),
        ("646 amostra", "646 amostra probabilística documentos", "646"),
        ("32% conformidade", "32% conformidade integral gestor", "32%"),
        ("742 mil renovação", "742 mil renovação registros", "742"),
    ]
    tests: list[dict[str, object]] = []
    for label, query, token in queries:
        payload = runner.run_query(query, 3)
        results = payload["results"]
        assert isinstance(results, list)
        top2_matrix = runner.find_first(results, is_matrix, top_n=2)
        number_in_snippet = contains_number(runner.result_text(top2_matrix), token) if top2_matrix else False
        provenance = runner.result_prov(top2_matrix) if top2_matrix else ""
        prov_ok = bool(provenance) and "bm25" in provenance and ("chroma" in provenance or "faiss" in provenance)
        ok = top2_matrix is not None and number_in_snippet and prov_ok
        tests.append(
            {
                "name": label,
                "query": query,
                "pass": ok,
                "matrix_top2": top2_matrix is not None,
                "number_in_snippet": number_in_snippet,
                "provenance": provenance or "n/a",
                "rrf_score": f"{runner.result_rrf(top2_matrix):.4f}" if top2_matrix else "n/a",
                "top_path": runner.result_path(results[0]) if results else "sem resultado",
            }
        )
    return tests


def battery_3(runner: TestRunner) -> list[dict[str, object]]:
    queries = [
        ("peça 103", "peça 103 adequação funcional documentos amostra", "103"),
        ("peça 106", "peça 106 resolução DPI qualidade digitalização", "106"),
        ("peça 109", "peça 109 divergência área imóvel hectares", "109"),
        ("peça 117", "peça 117 duplicações espaciais coordenadas idênticas", "117"),
        ("peça 121", "peça 121 áreas municipais impossíveis IBGE", "121"),
        ("peça 111", "peça 111 dimensionamento Leaflet georreferenciamento", "111"),
        ("peça 124", "peça 124 capacidade civil falecidos menores CPF", "124"),
        ("peça 125", "peça 125 e-mails fictícios naopossui padrões contato", "125"),
        ("peça 127", "peça 127 CNAE incompatível pessoa jurídica hipermercado", "127"),
        ("peça 130", "peça 130 outliers renda anual superior milhão", "130"),
        ("peça 135", "peça 135 qualidade semântica dicionário dados descrições", "135"),
        ("peça 136", "peça 136 unidades medida campos numéricos", "136"),
        ("peça 133", "peça 133 ambiguidade temporal campos data", "133"),
        ("peça 75", "peça 75 dicionário dados CAF tabelas campos", "75"),
        ("peça 78", "peça 78 regras negócio CAF validação", "78"),
        ("peça 137", "peça 137 Manual Crédito Rural BCB Pronaf", "137"),
        ("peça 150", "peça 150 comentários gestor contraditório resposta", "150"),
    ]
    tests: list[dict[str, object]] = []
    for label, query, piece in queries:
        payload = runner.run_query(query, 3)
        results = payload["results"]
        assert isinstance(results, list)
        top1 = results[0] if results else None
        top_path = runner.result_path(top1)
        expected = f"peca{int(piece):03d}"
        ok = expected in top_path.lower() and (
            top_path.startswith("04_PECAS_EVIDENCIA/txt_extraido/")
            or top_path.startswith("05_PECAS_TRAMITACAO/")
        )
        tests.append({"name": label, "query": query, "pass": ok, "top_path": top_path or "sem resultado"})
    return tests


def battery_4(runner: TestRunner) -> list[dict[str, object]]:
    queries = [
        ("método dedutivo", "método dedutivo parágrafo-síntese resultado completo", lambda paths: any(path.startswith("01_RELATORIO_V2/ACH0") for path in paths[:3])),
        ("storytelling propositivo", "storytelling auditoria operacional tom propositivo", lambda paths: any(path.startswith("01_RELATORIO_V2/") for path in paths[:3])),
        ("exclusão digital", "exclusão digital público rural conectividade", lambda paths: "01_RELATORIO_V2/ACH03_V2.md" in paths[:3]),
        ("conhecimento tácito", "dependência conhecimento tácito documentação sistema", lambda paths: "01_RELATORIO_V2/ACH04_V2.md" in paths[:3]),
        ("reincidência DAP", "reincidência DAP determinações pendentes monitoramento", lambda paths: any(path in {"01_RELATORIO_V2/VISAO_GERAL_V2.md", "01_RELATORIO_V2/ACH01_V2.md"} for path in paths[:3])),
        ("autodeclaratório", "autodeclaratório sem validação robusta ingestão", lambda paths: any(path in {"01_RELATORIO_V2/ACH01_V2.md", "01_RELATORIO_V2/VISAO_GERAL_V2.md"} for path in paths[:3])),
        ("transições tecnológicas", "transições tecnológicas passivo migração curadoria", lambda paths: "01_RELATORIO_V2/ACH02_V2.md" in paths[:3]),
        ("liberdade de meios", "liberdade de meios resultados a alcançar não prescrição", lambda paths: any(path.startswith("01_RELATORIO_V2/") for path in paths[:3])),
    ]
    tests: list[dict[str, object]] = []
    for label, query, checker in queries:
        payload = runner.run_query(query, 5)
        results = payload["results"]
        assert isinstance(results, list)
        paths = [runner.result_path(result) for result in results]
        tests.append({"name": label, "query": query, "pass": checker(paths), "top_paths": paths[:3]})
    return tests


def battery_5(runner: TestRunner) -> list[dict[str, object]]:
    cases = [
        ("5.1 sem filtro 27,1%", "27,1% documentos inadequados", None, lambda paths: len(paths) >= 3 and paths[0].startswith("02_FONTE_VERDADE/") and paths[2].startswith("01_RELATORIO_V2/")),
        ("5.2 constituicao 27,1%", "27,1% documentos inadequados", "constituicao", lambda paths: paths and all(hierarchy_of(path) == "constituicao" for path in paths)),
        ("5.3 relatorio_v2 27,1%", "27,1% documentos inadequados", "relatorio_v2", lambda paths: paths and all(hierarchy_of(path) == "relatorio_v2" for path in paths)),
        ("5.4 pecas 27,1%", "27,1% documentos inadequados", "pecas", lambda paths: paths and all(hierarchy_of(path) == "pecas" for path in paths)),
        ("5.5 sem filtro Acórdão 1197", "Acórdão 1197/2018 DAP fragilidades sistêmicas", None, lambda paths: bool(paths)),
        ("5.6 constituicao Acórdão 1197", "Acórdão 1197/2018 DAP fragilidades sistêmicas", "constituicao", lambda paths: paths and all(hierarchy_of(path) == "constituicao" for path in paths)),
        ("5.7 relatorio_v2 Acórdão 1197", "Acórdão 1197/2018 DAP fragilidades sistêmicas", "relatorio_v2", lambda paths: paths and all(hierarchy_of(path) == "relatorio_v2" for path in paths)),
        ("5.8 v1 Acórdão 1197", "Acórdão 1197/2018 DAP fragilidades sistêmicas", "v1", lambda paths: paths and all(hierarchy_of(path) == "v1" for path in paths)),
    ]
    tests: list[dict[str, object]] = []
    for label, query, hierarchy, checker in cases:
        payload = runner.run_query(query, 5 if hierarchy is None else 3, hierarchy)
        results = payload["results"]
        assert isinstance(results, list)
        paths = [runner.result_path(result) for result in results[:3]]
        tests.append({"name": label, "query": query, "pass": checker(paths), "top_paths": paths})
    return tests


def battery_6(runner: TestRunner) -> list[dict[str, object]]:
    cases = [
        ("ACH-01 vs Matriz", "27,1% documentos semanticamente inadequados 3,08 milhões", "constituicao", lambda results: results and is_matrix(runner.result_path(results[0])) and contains_number(runner.result_text(results[0]), "27,1%")),
        ("ACH-02 vs Matriz", "632 municípios área cadastrada superior oficial IBGE", "constituicao", lambda results: results and is_matrix(runner.result_path(results[0])) and contains_number(runner.result_text(results[0]), "632")),
        ("ACH-03 vs peça 125", "90,62% e-mails fictícios naopossui@mail.com 4.904.403", "pecas", lambda results: results and "peca125" in runner.result_path(results[0]).lower()),
        ("Proposta 2.1.3", "Proposta 2.1.3 interoperabilidade bases oficiais Sigef Sicar", "constituicao", lambda results: results and is_matrix(runner.result_path(results[0]))),
        ("ACH-04 vs peça 135", "94,1% descrições semanticamente inadequadas 496 527 campos", "pecas", lambda results: results and "peca135" in runner.result_path(results[0]).lower()),
        ("Resumo vs Visão Geral", "59,6 bilhões Pronaf safra 2023 2024", "relatorio_v2", lambda results: results and runner.result_path(results[0]).startswith("01_RELATORIO_V2/")),
    ]
    tests: list[dict[str, object]] = []
    for label, query, hierarchy, checker in cases:
        payload = runner.run_query(query, 3, hierarchy)
        results = payload["results"]
        assert isinstance(results, list)
        tests.append(
            {
                "name": label,
                "query": query,
                "pass": checker(results),
                "top_paths": [runner.result_path(result) for result in results[:3]],
            }
        )
    return tests


def battery_7(runner: TestRunner) -> list[dict[str, object]]:
    cases = [
        ("7.1 genérica", "dados informações sistema", lambda results: len(results) > 0),
        ("7.2 número isolado", "3.097", lambda results: len(results) > 0 and any(("peca124" in runner.result_path(r).lower()) or is_matrix(runner.result_path(r)) for r in results[:3])),
        ("7.3 acento", "módulos fiscais padrão técnico habilitação", lambda results: len(results) > 0),
        ("7.4 parágrafo longo", "Devido à insuficiência dos mecanismos de validação semântica e de consistência na ingestão documental do CAF decorrente de processo de cadastramento desenhado para aceitar documentos sem verificação de conteúdo", lambda results: len(results) > 0 and any(runner.result_path(r) == "01_RELATORIO_V2/ACH01_V2.md" for r in results[:3])),
        ("7.5 inglês", "data quality governance family agriculture cadastre", lambda results: len(results) > 0),
        ("7.6 norma específica", "ISO 11179 registro metadados gestão configuração", lambda results: len(results) > 0 and any(hierarchy_of(runner.result_path(r)) in {"normas", "relatorio_v2", "pecas"} for r in results[:3])),
        ("7.7 contraditório", "gestor concordou expressamente governança dados imatura", lambda results: len(results) > 0 and any(("peca150" in runner.result_path(r).lower()) or runner.result_path(r) == "01_RELATORIO_V2/ACH04_V2.md" or runner.result_path(r).startswith("02_FONTE_VERDADE/PECA169") for r in results[:3])),
        ("7.8 peça inexistente", "peça 999 inexistente", lambda results: True),
    ]
    tests: list[dict[str, object]] = []
    for label, query, checker in cases:
        payload = runner.run_query(query, 3)
        results = payload["results"]
        assert isinstance(results, list)
        tests.append(
            {
                "name": label,
                "query": query,
                "pass": checker(results),
                "top_paths": [runner.result_path(result) for result in results[:3]],
            }
        )
    return tests


def battery_8(runner: TestRunner) -> list[dict[str, object]]:
    before_notes = {
        "1": "Matriz aparecia, mas V1 ainda podia subir acima; sem ranking unificado",
        "2": "peça 124 já aparecia bem nas 3 listas separadas",
        "3": "PECA170 aparecia, mas não necessariamente em #1",
        "4": "NAT/manual_auditoria em #1 (irrelevante)",
    }
    checks = [
        ("1 — Número", "27,1% documentos semanticamente inadequados", lambda results: results and is_matrix(runner.result_path(results[0]))),
        ("2 — Peça", "peça 124 falecidos Sisobi 3.097", lambda results: results and "peca124" in runner.result_path(results[0]).lower()),
        ("3 — Proposta", "Proposta 2.1.3 interoperabilidade bases oficiais", lambda results: results and is_matrix(runner.result_path(results[0]))),
        ("4 — Conceitual", "parágrafo-síntese método dedutivo achado documentação", lambda results: results and any(runner.result_path(r).startswith("01_RELATORIO_V2/ACH0") for r in results[:3])),
    ]
    tests: list[dict[str, object]] = []
    for idx, (label, query, checker) in enumerate(checks, 1):
        payload = runner.run_query(query, 5)
        results = payload["results"]
        assert isinstance(results, list)
        tests.append(
            {
                "name": label,
                "query": query,
                "pass": checker(results),
                "before": before_notes[str(idx)],
                "after": " | ".join(runner.result_path(result) for result in results[:3]),
            }
        )
    return tests


BATTERY_FUNCS = {
    1: ("1 — Validação técnica", battery_1),
    2: ("2 — Integridade numérica", battery_2),
    3: ("3 — Peça específica", battery_3),
    4: ("4 — Conceitual", battery_4),
    5: ("5 — Filtro hierarquia", battery_5),
    6: ("6 — Busca cruzada", battery_6),
    7: ("7 — Stress test", battery_7),
    8: ("8 — Comparação antes/depois", battery_8),
}


def build_failure_entries(report: dict[str, object]) -> list[dict[str, object]]:
    failures: list[dict[str, object]] = []
    for battery in report["batteries"]:
        battery_name = str(battery["name"])
        for test in battery["tests"]:
            if test["pass"]:
                continue
            failures.append(
                {
                    "battery": battery_name,
                    "query": test.get("query", test["name"]),
                    "details": test,
                }
            )
    return failures


def render_markdown(report: dict[str, object], output_path: Path) -> None:
    lines: list[str] = []
    lines.append("# Testes do Indexador Corrigido — CAF-FINAL")
    lines.append("")
    lines.append(f"**Data:** {report['generated_at']}")
    lines.append(f"**Modelo:** {report['model']} ({report['embedding_dim']} dims MRL)")
    lines.append(f"**ES docs:** {report['es_count']}")
    lines.append(f"**ChromaDB vetores:** {report['chroma_count']}")
    lines.append(f"**ChromaDB dimensão:** {report['chroma_dim']}")
    lines.append("")
    lines.append("## Resumo")
    lines.append("")
    lines.append("| Bateria | Testes | Passou | Falhou | Taxa |")
    lines.append("|---|---:|---:|---:|---:|")
    for summary in report["summaries"]:
        lines.append(
            f"| {summary['name']} | {summary['total']} | {summary['passed']} | {summary['failed']} | {summary['rate']} |"
        )
    lines.append(
        f"| **TOTAL** | **{report['total_tests']}** | **{report['total_pass']}** | **{report['total_fail']}** | **{report['total_rate']}** |"
    )
    lines.append("")
    lines.append("## Veredicto")
    lines.append("")
    verdict = report["verdict"]
    lines.append(f"- {'[x]' if verdict == 'APROVADO' else '[ ]'} ✅ APROVADO — ≥ 60/77 testes passaram, incluindo ≥ 18/22 na bateria 2")
    lines.append(f"- {'[x]' if verdict == 'AJUSTES' else '[ ]'} ⚠️ AJUSTES — 45-59 testes passaram, corrigir e retestar")
    lines.append(f"- {'[x]' if verdict == 'REPROVADO' else '[ ]'} ❌ REPROVADO — < 45 testes passaram, problema estrutural")

    for battery in report["batteries"]:
        lines.append("")
        lines.append(f"## {battery['name']}")
        lines.append("")
        if battery["name"].startswith("2 —"):
            lines.append("| # | Query | Matriz top 2? | Número? | Proveniência | Score RRF | OK? |")
            lines.append("|---|---|---|---|---|---:|---|")
            for idx, test in enumerate(battery["tests"], 1):
                lines.append(
                    f"| {idx} | {md_escape(str(test['name']))} | {'Sim' if test['matrix_top2'] else 'Não'} | "
                    f"{'Sim' if test['number_in_snippet'] else 'Não'} | {md_escape(str(test['provenance']))} | "
                    f"{test['rrf_score']} | {'Sim' if test['pass'] else 'Não'} |"
                )
            continue
        if battery["name"].startswith("3 —"):
            lines.append("| Query | Top 1 | OK? |")
            lines.append("|---|---|---|")
            for test in battery["tests"]:
                lines.append(
                    f"| {md_escape(str(test['name']))} | {md_escape(str(test['top_path']))} | {'Sim' if test['pass'] else 'Não'} |"
                )
            continue
        if battery["name"].startswith(("4 —", "5 —", "6 —", "7 —")):
            lines.append("| Caso | Top resultados | OK? |")
            lines.append("|---|---|---|")
            for test in battery["tests"]:
                top_paths = test.get("top_paths", [])
                lines.append(
                    f"| {md_escape(str(test['name']))} | {md_escape(' ; '.join(top_paths))} | {'Sim' if test['pass'] else 'Não'} |"
                )
            continue
        if battery["name"].startswith("8 —"):
            lines.append("| Teste | Antes | Depois | Melhorou? |")
            lines.append("|---|---|---|---|")
            for test in battery["tests"]:
                lines.append(
                    f"| {md_escape(str(test['name']))} | {md_escape(str(test['before']))} | {md_escape(str(test['after']))} | {'Sim' if test['pass'] else 'Não'} |"
                )
            continue
        for test in battery["tests"]:
            lines.append(f"- {'PASSOU' if test['pass'] else 'FALHOU'}: **{test['name']}** — {test.get('details', '')}")

    lines.append("")
    lines.append("## Falhas detalhadas")
    lines.append("")
    if report["failures"]:
        for failure in report["failures"]:
            lines.append(f"- **{failure['battery']}** — Query/Teste: `{failure['query']}`")
            lines.append(f"  Detalhes: `{failure['details']}`")
    else:
        lines.append("- Nenhuma falha registrada.")
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    runner = TestRunner(args)
    selected = [args.battery] if args.battery else sorted(BATTERY_FUNCS)
    report: dict[str, object] = {
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model": DEFAULT_EMBEDDING_MODEL,
        "embedding_dim": DEFAULT_EMBEDDING_DIM,
        "es_count": runner.es_count,
        "chroma_count": runner.chroma_count,
        "chroma_dim": runner.chroma_dim,
        "batteries": [],
    }
    summaries: list[dict[str, object]] = []
    total_pass = 0
    total_tests = 0
    battery2_pass = None

    for battery_number in selected:
        name, func = BATTERY_FUNCS[battery_number]
        tests = func(runner)
        passed = sum(1 for test in tests if test["pass"])
        total = len(tests)
        total_pass += passed
        total_tests += total
        if battery_number == 2:
            battery2_pass = passed
        report["batteries"].append({"name": name, "tests": tests})
        summaries.append(
            {
                "name": name,
                "total": total,
                "passed": passed,
                "failed": total - passed,
                "rate": f"{passed / total:.1%}",
            }
        )

    verdict = "AJUSTES"
    if args.battery is None:
        if total_pass >= 60 and (battery2_pass or 0) >= 18:
            verdict = "APROVADO"
        elif total_pass < 45:
            verdict = "REPROVADO"
    report["summaries"] = summaries
    report["total_pass"] = total_pass
    report["total_tests"] = total_tests
    report["total_fail"] = total_tests - total_pass
    report["total_rate"] = f"{(total_pass / total_tests):.1%}" if total_tests else "0.0%"
    report["verdict"] = verdict
    report["failures"] = build_failure_entries(report)

    json_output = Path(args.json_output)
    json_output.parent.mkdir(parents=True, exist_ok=True)
    json_output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    output_path = Path(args.output)
    render_markdown(report, output_path)
    print(f"Relatório salvo em {output_path}")
    print(f"Resultado geral: {total_pass}/{total_tests} | veredicto={verdict}")
    if battery2_pass is not None:
        print(f"Bateria 2: {battery2_pass}/22")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
