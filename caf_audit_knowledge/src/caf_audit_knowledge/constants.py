from __future__ import annotations

from enum import Enum


class SourceType(str, Enum):
    CONTEXT = "context"
    REPORT_FINAL = "report_final"
    REPORT_DRAFT = "report_draft"
    GROUND_TRUTH = "ground_truth"
    EVIDENCE = "evidence"
    PROCEDURAL = "procedural"
    NORMATIVE = "normative"
    TEMPLATE = "template"


class EmbeddingStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    DONE = "done"
    FAILED = "failed"
    SKIPPED = "skipped"


AUTHORITY_WEIGHTS = {
    SourceType.CONTEXT: 0.4,
    SourceType.REPORT_FINAL: 0.9,
    SourceType.REPORT_DRAFT: 0.6,
    SourceType.GROUND_TRUTH: 1.0,
    SourceType.EVIDENCE: 0.95,
    SourceType.PROCEDURAL: 0.7,
    SourceType.NORMATIVE: 1.0,
    SourceType.TEMPLATE: 0.3,
}

SOURCE_DIRECTORY_MAP = {
    "00_CONTEXTO": SourceType.CONTEXT,
    "01_RELATORIO_V2": SourceType.REPORT_FINAL,
    "02_FONTE_VERDADE": SourceType.GROUND_TRUTH,
    "03_RELATORIO_V1": SourceType.REPORT_DRAFT,
    "04_PECAS_EVIDENCIA": SourceType.EVIDENCE,
    "05_PECAS_TRAMITACAO": SourceType.PROCEDURAL,
    "06_NORMAS_CRITERIOS": SourceType.NORMATIVE,
    "07_MODELOS_TCU": SourceType.TEMPLATE,
}

CANONICAL_EXTENSION_RANK = {
    ".md": 0,
    ".txt": 1,
    ".pdf": 2,
    ".docx": 3,
    ".doc": 4,
}

INDEXED_EXTENSIONS = {".md", ".txt", ".pdf", ".docx", ".doc"}

MAX_CHUNKS_PER_DOC = 8
HARD_LIMIT = 12
CHUNK_TARGET_CHARS = 2200

LEGAL_TOKEN_RE = (
    r"\b(lei|decreto|portaria|resolucao|acordao|manual|iso|cobit|dama-dmbok|art\.?|inciso)\b"
)
