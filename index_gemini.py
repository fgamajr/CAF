#!/usr/bin/env python3
"""
Indexa o acervo CAF-FINAL em Elasticsearch e ChromaDB usando embeddings Gemini.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

import chromadb
import faiss
import numpy as np
from chromadb.config import Settings
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from google import genai
from pypdf import PdfReader
from tqdm import tqdm


ROOT = Path(__file__).resolve().parent
CHROMA_DIR = ROOT / ".local" / "chroma"
STATE_DIR = ROOT / ".local" / "index_state"
PDF_CACHE_DIR = ROOT / ".local" / "pdf_text_cache"
DOC_CACHE_DIR = ROOT / ".local" / "doc_text_cache"
FAISS_DIR = ROOT / ".local" / "faiss"
FAISS_INDEX_PATH = FAISS_DIR / "caf-final.index"
FAISS_META_PATH = FAISS_DIR / "caf-final.metadata.jsonl"
DEFAULT_ES_INDEX = "caf-final"
DEFAULT_COLLECTION = "caf-final"
DEFAULT_EMBEDDING_MODEL = "gemini-embedding-001"
DEFAULT_EMBEDDING_DIM = 1024

PRIORITY_GLOBS: list[tuple[int, str]] = [
    (0, "MANIFEST.md"),
    (0, "README.md"),
    (1, "00_CONTEXTO/**/*.md"),
    (1, "02_FONTE_VERDADE/**/*.md"),
    (1, "02_FONTE_VERDADE/**/*.docx"),
    (2, "01_RELATORIO_V2/**/*.md"),
    (2, "03_2_POS_COMENTÁRIOS/**/*.pdf"),
    (2, "achado01/**/*.md"),
    (2, "achado01/**/*.txt"),
    (2, "achado01/**/*.docx"),
    (2, "OneDrive_2_23-06-2026/**/*.md"),
    (2, "OneDrive_2_23-06-2026/**/*.txt"),
    (2, "OneDrive_2_23-06-2026/**/*.docx"),
    (3, "04_PECAS_EVIDENCIA/txt_extraido/**/*.txt"),
    (4, "03_1_RELATORIO_V1/**/*.md"),
    (4, "03_1_RELATORIO_V1/**/*.docx"),
    (5, "06_NORMAS_CRITERIOS/**/*.md"),
    (5, "06_NORMAS_CRITERIOS/**/*.pdf"),
    (5, "06_NORMAS_CRITERIOS/**/*.doc"),
    (5, "06_NORMAS_CRITERIOS/**/*.docx"),
    (6, "05_PECAS_TRAMITACAO/**/*.pdf"),
    (7, "07_MODELOS_TCU/**/*.pdf"),
    (7, "07_MODELOS_TCU/**/*.docx"),
]

EXCLUDED_PARTS = {"_artefatos_latex", ".venv", ".git", ".local", "__pycache__"}
# Prefixos (relativos ao ROOT) pulados na descoberta: duplicatas e dumps gigantes.
EXCLUDED_PREFIXES = (
    "OneDrive_2_23-06-2026/achado01",            # dup exato de ./achado01 (já indexado)
    "OneDrive_2_23-06-2026/relatorio_auditoria/pecas",  # dup das peças em 04_.../txt_extraido
    "OneDrive_2_23-06-2026/CODEBASE_COMPLETE.txt",       # dump de 4MB do código-fonte
)
# Pula PDFs gigantes (scans/compilações de evidência redundante). 30MB preserva
# todo o corpus de peças (maior é ~19MB) e corta só os monstros de OCR do achado01.
MAX_PDF_BYTES = 30 * 1024 * 1024
# OCR de PDFs escaneados é lento (~30s/pág). Com CAF_PDF_OCR=0 usa só a camada de
# texto digital (rápido); PDFs sem texto retornam vazio em vez de disparar Tesseract.
PDF_OCR_ENABLED = os.getenv("CAF_PDF_OCR", "1") != "0"
TEXT_SUFFIXES = {".md", ".txt"}
PDF_SUFFIXES = {".pdf"}
WORD_SUFFIXES = {".doc", ".docx"}
PAGE_MARKER = re.compile(r"^--- Página (\d+) ---$", re.MULTILINE)
PARAGRAPH_MARKER = re.compile(r"^\s*(\d+)\.\s+", re.MULTILINE)

HIERARCHY_PREFIXES: list[tuple[str, str]] = [
    ("02_FONTE_VERDADE/", "constituicao"),
    ("01_RELATORIO_V2/", "relatorio_v2"),
    ("achado01/", "achado01"),
    ("OneDrive_2_23-06-2026/", "trabalho"),
    ("03_2_POS_COMENTÁRIOS/", "pos_comentarios"),
    ("04_PECAS_EVIDENCIA/", "pecas"),
    ("06_NORMAS_CRITERIOS/", "normas"),
    ("00_CONTEXTO/", "contexto"),
    ("03_1_RELATORIO_V1/", "v1"),
    ("05_PECAS_TRAMITACAO/", "tramitacao"),
    ("07_MODELOS_TCU/", "modelos"),
]

SECTION_SPLIT_H2 = re.compile(r"(?m)^##\s+")
SECTION_SPLIT_H3 = re.compile(r"(?m)^###\s+")
FONTE_VERDADE_MAX_CHARS = 12000
FONTE_VERDADE_OVERLAP = 4000

NUMEROS_CHAVE: list[dict[str, str]] = [
    {
        "valor": "27,1%",
        "achado": "ACH-01",
        "contexto": "27,1% dos documentos comprobatórios são semanticamente inadequados, equivalente a aproximadamente 3,08 milhões de documentos. Achado ACH-01.",
    },
    {
        "valor": "53,55%",
        "achado": "ACH-01",
        "contexto": "53,55% dos documentos de imóvel apresentam divergência crítica de área superior a 10%, projeção de aproximadamente 1,44 milhão de documentos. Achado ACH-01.",
    },
    {
        "valor": "33,33%",
        "achado": "ACH-01",
        "contexto": "33,33% dos documentos de imóvel são de tipo documental inadequado para comprovação de propriedade ou posse. Achado ACH-01.",
    },
    {
        "valor": "68,7%",
        "achado": "ACH-01",
        "contexto": "68,7% dos documentos examinados apresentaram resolução inferior a 300 DPI, parâmetro orientativo do Conarq. Achado ACH-01.",
    },
    {
        "valor": "45,92%",
        "achado": "ACH-02",
        "contexto": "45,92% de erro cartográfico na base geoespacial, equivalente a aproximadamente 1,46 milhão de imóveis. Achado ACH-02.",
    },
    {
        "valor": "55,27%",
        "achado": "ACH-02",
        "contexto": "55,27% de duplicações espaciais em registros de alta precisão, com coordenadas idênticas entre imóveis diferentes. Achado ACH-02.",
    },
    {
        "valor": "15,92%",
        "achado": "ACH-02",
        "contexto": "15,92% de inconsistência municipal, com imóveis localizados fora do município declarado. Achado ACH-02.",
    },
    {
        "valor": "632",
        "achado": "ACH-02",
        "contexto": "632 municípios apresentam inflação cadastral, com área total cadastrada no CAF superior à área oficial do IBGE. Achado ACH-02.",
    },
    {
        "valor": "3.097",
        "achado": "ACH-03",
        "contexto": "3.097 titulares falecidos permanecem como responsáveis ativos, confirmados por cruzamento com Sisobi e Receita Federal. Achado ACH-03.",
    },
    {
        "valor": "138",
        "achado": "ACH-03",
        "contexto": "138 menores figuram como titulares de unidades familiares, sendo 89 menores de 16 anos e 49 adolescentes entre 16 e 17 anos. Achado ACH-03.",
    },
    {
        "valor": "90,62%",
        "achado": "ACH-03",
        "contexto": "90,62% dos e-mails de pessoas físicas são fictícios ou inválidos, com 4.904.403 registros usando naopossui@mail.com. Achado ACH-03.",
    },
    {
        "valor": "93,7%",
        "achado": "ACH-03",
        "contexto": "93,7% dos CEPs são genéricos, terminados em 000, sem correspondência adequada com o endereço real. Achado ACH-03.",
    },
    {
        "valor": "907",
        "achado": "ACH-03",
        "contexto": "907 registros apresentam renda anual declarada superior a um milhão de reais, incompatível com o perfil de agricultura familiar. Achado ACH-03.",
    },
    {
        "valor": "39",
        "achado": "ACH-03",
        "contexto": "39 pessoas jurídicas apresentam CNAE principal incompatível com agricultura familiar, incluindo hipermercados, atacadistas e construtoras. Achado ACH-03.",
    },
    {
        "valor": "94,1%",
        "achado": "ACH-04",
        "contexto": "94,1% das descrições do dicionário de dados são semanticamente inadequadas, 496 de 527 campos. Achado ACH-04.",
    },
    {
        "valor": "84%",
        "achado": "ACH-04",
        "contexto": "84% dos campos numéricos não especificam unidade de medida. Achado ACH-04.",
    },
    {
        "valor": "92%",
        "achado": "ACH-04",
        "contexto": "92% dos campos temporais são ambíguos e não distinguem criação, atualização ou vigência. Achado ACH-04.",
    },
    {
        "valor": "59,6",
        "achado": "CONTEXTO",
        "contexto": "O Pronaf movimentou R$ 59,6 bilhões na safra 2023/2024 destinados à agricultura familiar.",
    },
    {
        "valor": "92,36%",
        "achado": "ACH-02",
        "contexto": "O Leaflet reduziu duplicações em novos cadastros de 92,36% para 16,59%, segundo o gestor. Achado ACH-02.",
    },
    {
        "valor": "646",
        "achado": "ACH-01",
        "contexto": "A amostra probabilística estratificada de 646 documentos foi calculada com intervalo de confiança de 99% e margem de erro de ±4,5 p.p. Achado ACH-01.",
    },
    {
        "valor": "32%",
        "achado": "ACH-01",
        "contexto": "O monitoramento próprio do gestor apurou conformidade integral de 32%. Achado ACH-01.",
    },
    {
        "valor": "742",
        "achado": "ACH-01",
        "contexto": "Está prevista a renovação de aproximadamente 742 mil registros em 2026. Achado ACH-01.",
    },
]


@dataclass
class SourceDocument:
    path: Path
    priority: int
    source_type: str


@dataclass
class Chunk:
    chunk_id: str
    path: str
    hierarchy_label: str
    priority: int
    source_type: str
    title: str
    section: str
    piece_number: int | None
    page_start: int | None
    page_end: int | None
    text: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Indexa o repositório CAF-FINAL.")
    parser.add_argument("--index-all", action="store_true", help="Recria o índice e reindexa tudo.")
    parser.add_argument("--reset", action="store_true", help="Alias para --index-all.")
    parser.add_argument("--force", action="store_true", help="Reindexa tudo e recria backends densos.")
    parser.add_argument("--status", action="store_true", help="Mostra o status dos backends sem reindexar.")
    parser.add_argument("--es-url", default=os.getenv("ELASTICSEARCH_URL", "http://localhost:9200"))
    parser.add_argument("--es-index", default=os.getenv("ELASTICSEARCH_INDEX", DEFAULT_ES_INDEX))
    parser.add_argument("--chroma-dir", default=str(CHROMA_DIR))
    parser.add_argument("--collection", default=os.getenv("CHROMA_COLLECTION", DEFAULT_COLLECTION))
    parser.add_argument("--batch-size", type=int, default=20)
    parser.add_argument("--embedding-dim", type=int, default=DEFAULT_EMBEDDING_DIM)
    parser.add_argument(
        "--embedding-model",
        default=os.getenv("GEMINI_EMBEDDING_MODEL", DEFAULT_EMBEDDING_MODEL),
    )
    return parser.parse_args()


def load_environment() -> None:
    load_dotenv(ROOT / ".env")
    STATE_DIR.mkdir(parents=True, exist_ok=True)
    CHROMA_DIR.mkdir(parents=True, exist_ok=True)
    PDF_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    DOC_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    FAISS_DIR.mkdir(parents=True, exist_ok=True)


def validate_env() -> str:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise SystemExit("GEMINI_API_KEY/GOOGLE_API_KEY não encontrado no ambiente/.env")
    return api_key


def discover_documents() -> list[SourceDocument]:
    found: dict[Path, SourceDocument] = {}
    for priority, pattern in PRIORITY_GLOBS:
        for path in ROOT.glob(pattern):
            if not path.is_file():
                continue
            if any(part in EXCLUDED_PARTS for part in path.parts):
                continue
            if str(path.relative_to(ROOT)).startswith(EXCLUDED_PREFIXES):
                continue
            if path.suffix.lower() in PDF_SUFFIXES and path.stat().st_size > MAX_PDF_BYTES:
                print(f"  [skip] PDF >{MAX_PDF_BYTES // (1024*1024)}MB: {path.relative_to(ROOT)}")
                continue
            found[path] = SourceDocument(
                path=path,
                priority=priority,
                source_type=path.suffix.lower().lstrip("."),
            )
    return sorted(found.values(), key=lambda doc: (doc.priority, str(doc.path)))


def read_document(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        return path.read_text(encoding="utf-8", errors="ignore")
    if suffix in PDF_SUFFIXES:
        return read_pdf(path)
    if suffix in WORD_SUFFIXES:
        return read_word_document(path)
    return ""


def read_word_document(path: Path) -> str:
    cached = read_doc_cache(path)
    if cached is not None:
        return cached

    text = extract_word_with_textutil(path)
    if not clean_text(text) and path.suffix.lower() == ".docx":
        text = extract_word_with_pandoc(path)

    text = clean_text(text)
    write_doc_cache(path, text)
    return text


def read_doc_cache(path: Path) -> str | None:
    DOC_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = doc_cache_path(path)
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8", errors="ignore")
    return None


def write_doc_cache(path: Path, content: str) -> None:
    DOC_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    doc_cache_path(path).write_text(content, encoding="utf-8")


def doc_cache_path(path: Path) -> Path:
    stat = path.stat()
    key = stable_id(str(path.resolve()), str(stat.st_mtime_ns), str(stat.st_size))
    return DOC_CACHE_DIR / f"{key}.txt"


def extract_word_with_textutil(path: Path) -> str:
    textutil = shutil.which("textutil")
    if not textutil:
        return ""
    result = subprocess.run(
        [textutil, "-convert", "txt", "-stdout", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def extract_word_with_pandoc(path: Path) -> str:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        return ""
    result = subprocess.run(
        [pandoc, str(path), "-t", "plain"],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def read_pdf(path: Path) -> str:
    cached = read_pdf_cache(path)
    if cached is not None:
        return cached

    reader = PdfReader(str(path))
    pages: list[str] = []
    for idx in range(1, len(reader.pages) + 1):
        digital_text = clean_text(extract_pdf_page_text(path, idx))
        if is_reliable_page_text(digital_text) or not PDF_OCR_ENABLED:
            final_text = digital_text
        else:
            ocr_text = clean_text(ocr_pdf_page(path, idx))
            final_text = merge_page_text(digital_text, ocr_text)
        pages.append(f"--- Página {idx} ---\n{final_text}".rstrip())

    content = "\n\n".join(pages).strip()
    write_pdf_cache(path, content)
    return content


def read_pdf_cache(path: Path) -> str | None:
    PDF_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = pdf_cache_path(path)
    if cache_path.exists():
        return cache_path.read_text(encoding="utf-8", errors="ignore")
    return None


def write_pdf_cache(path: Path, content: str) -> None:
    PDF_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    pdf_cache_path(path).write_text(content, encoding="utf-8")


def pdf_cache_path(path: Path) -> Path:
    stat = path.stat()
    key = stable_id(str(path.resolve()), str(stat.st_mtime_ns), str(stat.st_size))
    return PDF_CACHE_DIR / f"{key}.txt"


def extract_pdf_page_text(path: Path, page_number: int) -> str:
    pdftotext = shutil.which("pdftotext")
    if not pdftotext:
        return ""
    result = subprocess.run(
        [
            pdftotext,
            "-layout",
            "-enc",
            "UTF-8",
            "-f",
            str(page_number),
            "-l",
            str(page_number),
            str(path),
            "-",
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return ""
    return result.stdout


def ocr_pdf_page(path: Path, page_number: int) -> str:
    pdftoppm = shutil.which("pdftoppm")
    tesseract = shutil.which("tesseract")
    if not pdftoppm or not tesseract:
        return ""

    ocr_lang = os.getenv("TESSERACT_LANG", "por+eng")
    with tempfile.TemporaryDirectory(prefix="caf_pdf_ocr_") as tmpdir:
        prefix = Path(tmpdir) / "page"
        render = subprocess.run(
            [
                pdftoppm,
                "-r",
                "300",
                "-png",
                "-f",
                str(page_number),
                "-l",
                str(page_number),
                str(path),
                str(prefix),
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if render.returncode != 0:
            return ""

        images = sorted(Path(tmpdir).glob("page-*.png"))
        if not images:
            return ""

        ocr = subprocess.run(
            [
                tesseract,
                str(images[0]),
                "stdout",
                "-l",
                ocr_lang,
                "--psm",
                "3",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if ocr.returncode != 0:
            return ""
        return ocr.stdout


def is_reliable_page_text(text: str) -> bool:
    compact = re.sub(r"\s+", "", text)
    if len(compact) < 40:
        return False
    printable = sum(1 for ch in compact if ch.isprintable())
    letters = sum(1 for ch in compact if ch.isalpha())
    if printable and letters / printable < 0.2 and len(compact) < 200:
        return False
    if compact.count("�") > 3:
        return False
    return True


def merge_page_text(digital_text: str, ocr_text: str) -> str:
    digital_text = digital_text.strip()
    ocr_text = ocr_text.strip()
    if digital_text and ocr_text:
        if normalize_for_compare(digital_text) == normalize_for_compare(ocr_text):
            return digital_text
        return (
            "[Texto extraido]\n"
            f"{digital_text}\n\n"
            "[OCR fallback]\n"
            f"{ocr_text}"
        ).strip()
    return digital_text or ocr_text


def normalize_for_compare(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def clean_text(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\r\n?", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def chunk_document(doc: SourceDocument, text: str) -> list[Chunk]:
    text = clean_text(text)
    if not text:
        return []

    title = doc.path.name
    rel_path = str(doc.path.relative_to(ROOT))
    hierarchy_label = infer_hierarchy_label(rel_path)
    piece_number = extract_piece_number(rel_path)

    if doc.path.suffix.lower() == ".txt":
        return chunk_txt(rel_path, title, hierarchy_label, doc.priority, doc.source_type, piece_number, text)
    return chunk_markdown_like(rel_path, title, hierarchy_label, doc.priority, doc.source_type, piece_number, text)


def infer_hierarchy_label(path: str) -> str:
    normalized = path.replace("\\", "/")
    for prefix, label in HIERARCHY_PREFIXES:
        if normalized.startswith(prefix):
            return label
    return "outros"


def extract_piece_number(path: str) -> int | None:
    match = re.search(r"peca[_\s-]*0*(\d{1,3})", path, flags=re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def chunk_markdown_like(
    path: str,
    title: str,
    hierarchy_label: str,
    priority: int,
    source_type: str,
    piece_number: int | None,
    text: str,
) -> list[Chunk]:
    if hierarchy_label == "constituicao":
        return chunk_fonte_verdade(path, title, hierarchy_label, priority, source_type, piece_number, text)

    lines = text.splitlines()
    chunks: list[Chunk] = []
    current_section = title
    buffer: list[str] = []
    page_start: int | None = None
    page_end: int | None = None
    chunk_counter = 0

    def flush() -> None:
        nonlocal buffer, page_start, page_end, chunk_counter
        body = "\n".join(buffer).strip()
        if not body:
            buffer = []
            return
        chunk_id = stable_id(path, current_section, str(chunk_counter))
        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                path=path,
                hierarchy_label=hierarchy_label,
                priority=priority,
                source_type=source_type,
                title=title,
                section=current_section,
                piece_number=piece_number,
                page_start=page_start,
                page_end=page_end,
                text=body,
            )
        )
        chunk_counter += 1
        buffer = []
        page_start = None
        page_end = None

    for line in lines:
        page_match = PAGE_MARKER.match(line)
        if page_match:
            page = int(page_match.group(1))
            if page_start is None:
                page_start = page
            page_end = page
            continue

        if line.startswith("#"):
            flush()
            current_section = line.lstrip("#").strip() or title
            continue

        if PARAGRAPH_MARKER.match(line):
            flush()
            buffer = [line]
            continue

        buffer.append(line)
        if len("\n".join(buffer)) > 2200:
            flush()

    flush()
    return chunks


def chunk_fonte_verdade(
    path: str,
    title: str,
    hierarchy_label: str,
    priority: int,
    source_type: str,
    piece_number: int | None,
    text: str,
) -> list[Chunk]:
    chunks: list[Chunk] = []
    sections = split_fonte_verdade_sections(text)
    for chunk_counter, (section_title, section_text) in enumerate(sections):
        chunk_id = stable_id(path, section_title, str(chunk_counter))
        chunks.append(
            Chunk(
                chunk_id=chunk_id,
                path=path,
                hierarchy_label=hierarchy_label,
                priority=priority,
                source_type=source_type,
                title=title,
                section=section_title,
                piece_number=piece_number,
                page_start=None,
                page_end=None,
                text=section_text,
            )
        )
    return chunks


def split_fonte_verdade_sections(text: str) -> list[tuple[str, str]]:
    normalized = clean_text(text)
    if not normalized:
        return []

    parts = re.split(r"(?m)^##\s+", normalized)
    sections: list[tuple[str, str]] = []
    preamble = parts[0].strip()
    if preamble:
        sections.extend(split_large_fonte_verdade_chunk("Preambulo", preamble))

    for raw in parts[1:]:
        raw = raw.strip()
        if not raw:
            continue
        lines = raw.splitlines()
        heading = lines[0].strip()
        body = "\n".join(lines[1:]).strip()
        section_text = f"## {heading}\n\n{body}".strip()
        sections.extend(split_large_fonte_verdade_chunk(heading, section_text))

    return sections


def split_large_fonte_verdade_chunk(section_title: str, section_text: str) -> list[tuple[str, str]]:
    section_text = clean_text(section_text)
    if len(section_text) <= FONTE_VERDADE_MAX_CHARS:
        return [(section_title, section_text)]

    if "### " in section_text:
        parts = re.split(r"(?m)^###\s+", section_text)
        subchunks: list[tuple[str, str]] = []
        prefix = parts[0].strip()
        if prefix:
            subchunks.append((f"{section_title} — Parte 1", prefix))
        part_counter = 2
        for raw in parts[1:]:
            raw = raw.strip()
            if not raw:
                continue
            lines = raw.splitlines()
            heading = lines[0].strip()
            body = "\n".join(lines[1:]).strip()
            subtext = f"### {heading}\n\n{body}".strip()
            if len(subtext) <= FONTE_VERDADE_MAX_CHARS:
                subchunks.append((f"{section_title} — {heading}", subtext))
                continue
            for piece_idx, piece in enumerate(split_with_overlap(subtext), 1):
                contextualized = piece
                if not piece.startswith("### "):
                    contextualized = f"## {section_title}\n\n### {heading}\n\n{piece}".strip()
                subchunks.append((f"{section_title} — {heading} — Parte {piece_idx}", contextualized))
            part_counter += 1
        return subchunks

    chunks: list[tuple[str, str]] = []
    for piece_idx, piece in enumerate(split_with_overlap(section_text), 1):
        contextualized = piece
        if not piece.startswith("## "):
            contextualized = f"## {section_title}\n\n{piece}".strip()
        chunks.append((f"{section_title} — Parte {piece_idx}", contextualized))
    return chunks


def split_with_overlap(text: str) -> list[str]:
    pieces: list[str] = []
    start = 0
    while start < len(text):
        end = min(len(text), start + FONTE_VERDADE_MAX_CHARS)
        if end < len(text):
            paragraph_break = text.rfind("\n\n", start, end)
            if paragraph_break > start + FONTE_VERDADE_MAX_CHARS // 2:
                end = paragraph_break
        piece = text[start:end].strip()
        if piece:
            pieces.append(piece)
        if end >= len(text):
            break
        start = max(end - FONTE_VERDADE_OVERLAP, start + 1)
    return pieces


def chunk_txt(
    path: str,
    title: str,
    hierarchy_label: str,
    priority: int,
    source_type: str,
    piece_number: int | None,
    text: str,
) -> list[Chunk]:
    chunks: list[Chunk] = []
    chunk_counter = 0
    segments = PAGE_MARKER.split(text)
    if len(segments) == 1:
        return chunk_markdown_like(path, title, hierarchy_label, priority, source_type, piece_number, text)

    leading = clean_text(segments[0])
    if leading:
        chunks.extend(
            chunk_markdown_like(path, title, hierarchy_label, priority, source_type, piece_number, leading)
        )

    for idx in range(1, len(segments), 2):
        page = int(segments[idx])
        body = clean_text(segments[idx + 1])
        if not body:
            continue
        parts = re.split(r"\n\s*\n", body)
        current: list[str] = []
        for part in parts:
            part = part.strip()
            if not part:
                continue
            candidate = "\n\n".join(current + [part]).strip()
            if current and len(candidate) > 1800:
                chunk_body = "\n\n".join(current).strip()
                chunk_id = stable_id(path, f"Página {page}", str(chunk_counter))
                chunks.append(
                    Chunk(
                        chunk_id=chunk_id,
                        path=path,
                        hierarchy_label=hierarchy_label,
                        priority=priority,
                        source_type=source_type,
                        title=title,
                        section=f"Página {page}",
                        piece_number=piece_number,
                        page_start=page,
                        page_end=page,
                        text=chunk_body,
                    )
                )
                chunk_counter += 1
                current = [part]
            else:
                current.append(part)
        if current:
            chunk_body = "\n\n".join(current).strip()
            chunk_id = stable_id(path, f"Página {page}", str(chunk_counter))
            chunks.append(
                Chunk(
                    chunk_id=chunk_id,
                    path=path,
                    hierarchy_label=hierarchy_label,
                    priority=priority,
                    source_type=source_type,
                    title=title,
                    section=f"Página {page}",
                    piece_number=piece_number,
                    page_start=page,
                    page_end=page,
                    text=chunk_body,
                )
            )
            chunk_counter += 1
    return chunks


def stable_id(*parts: str) -> str:
    joined = "::".join(parts)
    return hashlib.sha1(joined.encode("utf-8")).hexdigest()


def build_chunks(documents: Sequence[SourceDocument]) -> list[Chunk]:
    chunks: list[Chunk] = []
    for doc in tqdm(documents, desc="Lendo documentos"):
        text = read_document(doc.path)
        doc_chunks = chunk_document(doc, text)
        chunks.extend(doc_chunks)
    chunks.extend(build_numeric_key_chunks())
    return chunks


def build_numeric_key_chunks() -> list[Chunk]:
    chunks: list[Chunk] = []
    for idx, item in enumerate(NUMEROS_CHAVE, 1):
        safe_value = (
            item["valor"]
            .replace("%", "pct")
            .replace(".", "_")
            .replace(",", "_")
            .replace("/", "_")
            .replace(" ", "_")
        )
        path = f'02_FONTE_VERDADE/NUMEROS_CHAVE/{item["achado"]}__{safe_value}.md'
        title = f'NÚMERO-CHAVE {item["valor"]}'
        text = (
            f'NÚMERO-CHAVE DA AUDITORIA: {item["valor"]}\n\n'
            f'Contexto: {item["contexto"]}\n'
            f'Achado relacionado: {item["achado"]}.'
        )
        chunks.append(
            Chunk(
                chunk_id=stable_id(path, item["valor"], str(idx)),
                path=path,
                hierarchy_label="constituicao",
                priority=1,
                source_type="synthetic",
                title=title,
                section=f'{item["achado"]} — Número-chave',
                piece_number=None,
                page_start=None,
                page_end=None,
                text=text,
            )
        )
    return chunks


def extract_embedding_values(item: Any) -> list[float]:
    values = getattr(item, "values", None)
    if values is None and isinstance(item, dict):
        values = item.get("values")
    if values is None:
        raise RuntimeError("Resposta de embedding sem vetor.")
    return list(values)


def prepare_embedding_text(text: str, *, task_type: str) -> str:
    normalized = clean_text(text)
    prefix = "search_document: "
    if task_type == "RETRIEVAL_QUERY":
        prefix = "search_query: "
    return f"{prefix}{normalized}"


def embed_texts(
    client: genai.Client,
    model: str,
    texts: Sequence[str],
    *,
    task_type: str,
    output_dimensionality: int,
) -> list[list[float]]:
    result = client.models.embed_content(
        model=model,
        contents=[prepare_embedding_text(text, task_type=task_type) for text in texts],
        config=genai.types.EmbedContentConfig(
            task_type=task_type,
            output_dimensionality=output_dimensionality,
        ),
    )
    embeddings: list[list[float]] = []
    for item in result.embeddings:
        embeddings.append(extract_embedding_values(item))
    return embeddings


def embed_query(client: genai.Client, model: str, query: str, output_dimensionality: int) -> list[float]:
    result = client.models.embed_content(
        model=model,
        contents=[prepare_embedding_text(query, task_type="RETRIEVAL_QUERY")],
        config=genai.types.EmbedContentConfig(
            task_type="RETRIEVAL_QUERY",
            output_dimensionality=output_dimensionality,
        ),
    )
    return extract_embedding_values(result.embeddings[0])


def write_faiss_index(
    embeddings: Sequence[Sequence[float]],
    chunks: Sequence[Chunk],
    dims: int,
) -> None:
    if len(embeddings) != len(chunks):
        raise RuntimeError("Quantidade de embeddings diferente da quantidade de chunks.")

    matrix = np.asarray(embeddings, dtype=np.float32)
    faiss.normalize_L2(matrix)
    index = faiss.IndexFlatIP(dims)
    index.add(matrix)

    FAISS_DIR.mkdir(parents=True, exist_ok=True)
    faiss.write_index(index, str(FAISS_INDEX_PATH))
    with FAISS_META_PATH.open("w", encoding="utf-8") as handle:
        for chunk in chunks:
            handle.write(
                json.dumps(
                    {
                        "chunk_id": chunk.chunk_id,
                        "path": chunk.path,
                        "hierarchy_label": chunk.hierarchy_label,
                        "title": chunk.title,
                        "section": chunk.section,
                        "priority": chunk.priority,
                        "source_type": chunk.source_type,
                        "piece_number": chunk.piece_number,
                        "page_start": chunk.page_start,
                        "page_end": chunk.page_end,
                        "text": chunk.text,
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )


def load_faiss_index() -> tuple[faiss.Index | None, list[dict[str, Any]]]:
    if not FAISS_INDEX_PATH.exists() or not FAISS_META_PATH.exists():
        return None, []

    index = faiss.read_index(str(FAISS_INDEX_PATH))
    metadata: list[dict[str, Any]] = []
    with FAISS_META_PATH.open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if line:
                metadata.append(json.loads(line))
    return index, metadata


def create_es_index(es: Elasticsearch, index_name: str, dims: int, recreate: bool) -> None:
    if recreate and es.indices.exists(index=index_name):
        es.indices.delete(index=index_name)

    if es.indices.exists(index=index_name):
        return

    mappings = {
        "settings": {
            # Single-node clusters (Docker/tunnel) cannot assign replica shards.
            "number_of_replicas": 0,
            "analysis": {
                "analyzer": {
                    "default": {
                        "type": "standard",
                    }
                }
            }
        },
        "mappings": {
            "properties": {
                "path": {"type": "keyword"},
                "hierarchy_label": {"type": "keyword"},
                "title": {"type": "text"},
                "section": {"type": "text"},
                "priority": {"type": "integer"},
                "source_type": {"type": "keyword"},
                "piece_number": {"type": "integer"},
                "page_start": {"type": "integer"},
                "page_end": {"type": "integer"},
                "text": {"type": "text"},
                "embedding": {
                    "type": "dense_vector",
                    "dims": dims,
                    "index": True,
                    "similarity": "cosine",
                },
            }
        },
    }
    es.indices.create(index=index_name, body=mappings)


def recreate_chroma_collection(client: chromadb.PersistentClient, name: str, recreate: bool):
    if recreate:
        try:
            client.delete_collection(name=name)
        except Exception:
            pass
    try:
        return client.get_collection(name=name)
    except Exception:
        return client.create_collection(name=name, metadata={"hnsw:space": "cosine"})


def index_chunks(
    *,
    chunks: Sequence[Chunk],
    embeddings: Sequence[Sequence[float]],
    es: Elasticsearch,
    es_index: str,
    chroma_collection,
    batch_size: int,
) -> None:
    from elasticsearch.helpers import bulk

    actions = []
    ids: list[str] = []
    docs: list[str] = []
    metadatas: list[dict[str, object]] = []
    vectors: list[list[float]] = []

    for chunk, vector in zip(chunks, embeddings, strict=True):
        metadata = {
            "chunk_id": chunk.chunk_id,
            "path": chunk.path,
            "hierarchy_label": chunk.hierarchy_label,
            "title": chunk.title,
            "section": chunk.section,
            "priority": chunk.priority,
            "source_type": chunk.source_type,
            "piece_number": chunk.piece_number,
            "page_start": chunk.page_start,
            "page_end": chunk.page_end,
        }
        actions.append(
            {
                "_op_type": "index",
                "_index": es_index,
                "_id": chunk.chunk_id,
                **metadata,
                "text": chunk.text,
                "embedding": list(vector),
            }
        )
        ids.append(chunk.chunk_id)
        docs.append(chunk.text)
        metadatas.append(metadata)
        vectors.append(list(vector))

        if len(actions) >= batch_size:
            bulk(es, actions, refresh=False)
            chroma_collection.upsert(ids=ids, documents=docs, metadatas=metadatas, embeddings=vectors)
            actions, ids, docs, metadatas, vectors = [], [], [], [], []

    if actions:
        bulk(es, actions, refresh=True)
        chroma_collection.upsert(ids=ids, documents=docs, metadatas=metadatas, embeddings=vectors)
    else:
        es.indices.refresh(index=es_index)


def write_manifest(
    chunks: Sequence[Chunk],
    es_index: str,
    collection: str,
    model: str,
    embedding_dim: int,
    faiss_total: int,
) -> None:
    payload = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S"),
        "chunk_count": len(chunks),
        "es_index": es_index,
        "chroma_collection": collection,
        "embedding_model": model,
        "embedding_dim": embedding_dim,
        "faiss_total": faiss_total,
        "sample_paths": sorted({chunk.path for chunk in chunks})[:25],
    }
    (STATE_DIR / "index_manifest.json").write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def show_status(args: argparse.Namespace) -> int:
    payload: dict[str, Any] = {}
    manifest_path = STATE_DIR / "index_manifest.json"
    if manifest_path.exists():
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))

    es = Elasticsearch(args.es_url, request_timeout=60)
    es_total = None
    if es.ping() and es.indices.exists(index=args.es_index):
        es_total = es.count(index=args.es_index)["count"]

    chroma_client = chromadb.PersistentClient(
        path=args.chroma_dir,
        settings=Settings(anonymized_telemetry=False),
    )
    chroma_total = None
    try:
        chroma_total = chroma_client.get_collection(name=args.collection).count()
    except Exception:
        chroma_total = None

    faiss_index, metadata = load_faiss_index()
    faiss_total = faiss_index.ntotal if faiss_index is not None else 0

    print(f"Embedding model: {payload.get('embedding_model', args.embedding_model)}")
    print(f"Embedding dim: {payload.get('embedding_dim', args.embedding_dim)}")
    print(f"Elasticsearch ({args.es_index}): {es_total if es_total is not None else 'ausente'}")
    print(f"ChromaDB ({args.collection}): {chroma_total if chroma_total is not None else 'ausente'}")
    print(f"FAISS ({FAISS_INDEX_PATH.name}): {faiss_total if faiss_total else 'ausente'}")
    print(f"Manifest chunk_count: {payload.get('chunk_count', 'ausente')}")
    print(f"FAISS metadata rows: {len(metadata) if metadata else 0}")
    return 0


def main() -> int:
    args = parse_args()
    load_environment()
    if args.status:
        return show_status(args)

    recreate = args.index_all or args.reset or args.force
    api_key = validate_env()

    es = Elasticsearch(args.es_url, request_timeout=120)
    if not es.ping():
        raise SystemExit(f"Elasticsearch indisponível em {args.es_url}")

    chroma_client = chromadb.PersistentClient(
        path=args.chroma_dir,
        settings=Settings(anonymized_telemetry=False),
    )
    collection = recreate_chroma_collection(chroma_client, args.collection, recreate)
    if recreate:
        for path in (FAISS_INDEX_PATH, FAISS_META_PATH):
            try:
                path.unlink()
            except FileNotFoundError:
                pass

    documents = discover_documents()
    if not documents:
        raise SystemExit("Nenhum documento elegível para indexação.")

    chunks = build_chunks(documents)
    if not chunks:
        raise SystemExit("Nenhum chunk gerado.")

    gemini_client = genai.Client(api_key=api_key)
    create_es_index(es, args.es_index, args.embedding_dim, recreate)

    all_embeddings: list[list[float]] = []
    for start in tqdm(range(0, len(chunks), args.batch_size), desc="Gerando embeddings"):
        batch = chunks[start:start + args.batch_size]
        texts = [chunk.text for chunk in batch]
        for attempt in range(8):
            try:
                result = embed_texts(
                    gemini_client,
                    args.embedding_model,
                    texts,
                    task_type="RETRIEVAL_DOCUMENT",
                    output_dimensionality=args.embedding_dim,
                )
                if len(result) == len(texts):
                    all_embeddings.extend(result)
                    break
                print(f"\nBatch {start}: got {len(result)}/{len(texts)} embeddings, retrying...")
                time.sleep(2 ** attempt)
            except Exception as e:
                # 429/RESOURCE_EXHAUSTED é limite por minuto: espera ~70s e segue.
                is_rate = "429" in str(e) or "RESOURCE_EXHAUSTED" in str(e)
                wait = 70 if is_rate else min(60, 2 ** attempt)
                print(f"\nBatch {start} attempt {attempt+1} failed ({'rate-limit' if is_rate else 'erro'}); aguardando {wait}s: {str(e)[:120]}")
                time.sleep(wait)
        else:
            raise SystemExit(f"Failed to embed batch starting at chunk {start} after 8 attempts")

    index_chunks(
        chunks=chunks,
        embeddings=all_embeddings,
        es=es,
        es_index=args.es_index,
        chroma_collection=collection,
        batch_size=args.batch_size,
    )
    write_faiss_index(all_embeddings, chunks, args.embedding_dim)
    faiss_index, _ = load_faiss_index()
    faiss_total = faiss_index.ntotal if faiss_index is not None else 0
    write_manifest(chunks, args.es_index, args.collection, args.embedding_model, args.embedding_dim, faiss_total)

    print(f"Indexação concluída: {len(chunks)} chunks")
    print(f"Elasticsearch: {args.es_index}")
    print(f"ChromaDB: {args.collection} @ {args.chroma_dir}")
    print(f"FAISS: {FAISS_INDEX_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
