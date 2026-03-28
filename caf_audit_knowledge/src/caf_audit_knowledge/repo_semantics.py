from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from caf_audit_knowledge.constants import AUTHORITY_WEIGHTS, CANONICAL_EXTENSION_RANK, INDEXED_EXTENSIONS, SOURCE_DIRECTORY_MAP, SourceType

ACH_DIRECT_RE = re.compile(r"\bACH[-_ ]?0?([1-4])\b", re.IGNORECASE)
ACH_TEXT_RE = re.compile(r"\bAchado\s+([IVX0-9]{1,4})\b", re.IGNORECASE)
PECA_RE = re.compile(r"peca[_ ]?0*([0-9]{1,3})", re.IGNORECASE)
COPYISH_RE = re.compile(r"( copy\b|\.bak$|__pycache__|\.venv|~\$)", re.IGNORECASE)
TABLE_RE = re.compile(r"^\|.+\|$", re.MULTILINE)
TOC_LINE_RE = re.compile(r"^\s*(?:\d+(?:\.\d+)*|[A-Z](?:\.\d+)?)\s+.*\s\d+\s*$", re.MULTILINE)

ROMAN_TO_ARABIC = {"I": 1, "II": 2, "III": 3, "IV": 4}

PIECE_TO_ACH = {
    range(103, 110): "ACH01",
    range(110, 123): "ACH02",
    range(123, 133): "ACH03",
    range(133, 137): "ACH04",
    range(140, 141): "ACH01",
}


@dataclass(frozen=True)
class SourceDescriptor:
    source_type: SourceType
    authority_weight: float


def should_ignore_path(path: Path) -> bool:
    path_str = str(path)
    if "99_DISCARDED" in path_str or "01_RELATORIO_V2 copy" in path_str:
        return True
    if COPYISH_RE.search(path_str):
        return True
    return path.suffix.lower() not in INDEXED_EXTENSIONS


def classify_source(path: Path) -> SourceDescriptor | None:
    parts = path.parts
    for part in parts:
        if part in SOURCE_DIRECTORY_MAP:
            source_type = SOURCE_DIRECTORY_MAP[part]
            return SourceDescriptor(source_type=source_type, authority_weight=AUTHORITY_WEIGHTS[source_type])
    return None


def canonical_rank(path: Path) -> tuple[int, int, str]:
    ext_rank = CANONICAL_EXTENSION_RANK.get(path.suffix.lower(), 99)
    penalty = 0
    path_str = str(path).lower()
    if "txt_extraido" in path_str:
        penalty += 1
    if "_texto_com_paginas" in path_str:
        penalty += 1
    return (ext_rank, penalty, path_str)


def extract_piece_number(text: str | None, path: Path) -> int | None:
    for candidate in (path.name, path.as_posix(), text or ""):
        match = PECA_RE.search(candidate)
        if match:
            return int(match.group(1))
    return None


def extract_audit_object_id(text: str | None, path: Path) -> str | None:
    for candidate in (path.name, path.as_posix(), text or ""):
        match = ACH_DIRECT_RE.search(candidate)
        if match:
            return f"ACH0{int(match.group(1))}"
        roman = ACH_TEXT_RE.search(candidate)
        if roman:
            token = roman.group(1).upper()
            if token.isdigit() and int(token) in {1, 2, 3, 4}:
                return f"ACH0{int(token)}"
            if token in ROMAN_TO_ARABIC:
                return f"ACH0{ROMAN_TO_ARABIC[token]}"

    piece = extract_piece_number(text, path)
    if piece is not None:
        for piece_range, audit_object_id in PIECE_TO_ACH.items():
            if piece in piece_range:
                return audit_object_id
    return None


def infer_section_type(text: str, title: str | None = None, source_path: str | None = None) -> str:
    title_text = (title or "").lower()
    source_text = (source_path or "").lower()
    head_text = text[:1500].lower()
    full_text = text.lower()
    head_haystack = "\n".join(part for part in [title_text, source_text, head_text] if part)
    full_haystack = "\n".join(part for part in [title_text, source_text, full_text] if part)
    toc_line_count = len(TOC_LINE_RE.findall("\n".join(text.splitlines()[:25])))

    if any(token in full_haystack for token in ["bug:", "persona:", "chaos-agent", "adversarial", "review panel", "swarm panel"]):
        return "debug"
    if toc_line_count >= 3 or any(token in head_haystack for token in ["sumário", "sumario", "lista de figuras", "lista de tabelas", "table of contents"]):
        return "toc"
    if any(token in head_haystack for token in ["frase-síntese", "frase-sintese", "síntese", "sintese", "resumo executivo"]):
        return "sintese"
    if any(token in head_haystack for token in ["causa raiz", "causas", "causa"]):
        return "causa"
    if any(token in head_haystack for token in ["efeitos", "efeito", "impactos", "impacto", "consequências", "consequencias"]):
        return "efeito"
    if any(token in head_haystack for token in ["riscos", "risco"]):
        return "risco"
    if any(token in head_haystack for token in ["metodologia", "amostra probabil", "intervalo de confiança", "intervalo de confianca", "procedimentos", "método", "metodo"]):
        return "metodologia"
    if TABLE_RE.search(text) or any(token in head_haystack for token in ["tabela", "quadro"]):
        return "tabela"
    if any(token in head_haystack for token in ["introdução", "introducao", "propósito", "proposito", "visão geral", "visao geral"]):
        return "intro"
    if any(token in head_haystack for token in ["análise", "analise", "diagnóstico", "diagnostico"]):
        return "analysis"
    return "body"
