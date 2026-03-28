from __future__ import annotations

import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

from docx import Document as DocxDocument
from pypdf import PdfReader


@dataclass(frozen=True)
class PageSpan:
    page_number: int
    char_start: int
    char_end: int


@dataclass(frozen=True)
class ExtractionResult:
    text: str
    structured_markdown: str
    page_spans: list[PageSpan]


def read_bytes(path: Path) -> bytes:
    return path.read_bytes()


def normalize_text(text: str) -> str:
    normalized = text.replace("\x00", " ")
    normalized = normalized.replace("\r\n", "\n").replace("\r", "\n")
    normalized = re.sub(r"[ \t]+", " ", normalized)
    normalized = re.sub(r"\n{3,}", "\n\n", normalized)
    normalized = re.sub(r"[\x01-\x08\x0b\x0c\x0e-\x1f]", " ", normalized)
    normalized = re.sub(r"\bPágina\s+\d+\b", " ", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"\bPage\s+\d+\b", " ", normalized, flags=re.IGNORECASE)
    normalized = re.sub(r"^\s*\d+\s*$", "", normalized, flags=re.MULTILINE)
    return normalized.strip()


def _decode_text(raw_bytes: bytes) -> str:
    for encoding in ("utf-8", "latin-1"):
        try:
            return raw_bytes.decode(encoding)
        except UnicodeDecodeError:
            continue
    return raw_bytes.decode("utf-8", errors="ignore")


def _build_from_pages(page_texts: list[str]) -> ExtractionResult:
    text_parts: list[str] = []
    markdown_parts: list[str] = []
    page_spans: list[PageSpan] = []
    cursor = 0
    for page_number, page_text in enumerate(page_texts, start=1):
        normalized_page = normalize_text(page_text)
        if not normalized_page:
            continue
        if text_parts:
            text_parts.append("\n\n")
            cursor += 2
        char_start = cursor
        text_parts.append(normalized_page)
        cursor += len(normalized_page)
        page_spans.append(PageSpan(page_number=page_number, char_start=char_start, char_end=cursor))
        markdown_parts.append(f"## Page {page_number}\n\n{normalized_page}")
    text = "".join(text_parts).strip()
    structured_markdown = "\n\n".join(markdown_parts).strip()
    if text and not page_spans:
        page_spans = [PageSpan(page_number=1, char_start=0, char_end=len(text))]
    return ExtractionResult(text=text, structured_markdown=structured_markdown or text, page_spans=page_spans)


def extract_document(path: Path, raw_bytes: bytes | None = None) -> ExtractionResult:
    suffix = path.suffix.lower()
    if suffix in {".md", ".txt"}:
        text = _decode_text(raw_bytes or path.read_bytes())
        return _build_from_pages([text])
    if suffix == ".docx":
        document = DocxDocument(path)
        text = "\n".join(paragraph.text for paragraph in document.paragraphs if paragraph.text.strip())
        return _build_from_pages([text])
    if suffix == ".doc":
        try:
            result = subprocess.run(
                ["textutil", "-convert", "txt", "-stdout", str(path)],
                check=True,
                capture_output=True,
                text=True,
            )
            return _build_from_pages([result.stdout])
        except Exception:
            return ExtractionResult(text="", structured_markdown="", page_spans=[])
    if suffix == ".pdf":
        reader = PdfReader(path)
        return _build_from_pages([page.extract_text() or "" for page in reader.pages])
    return ExtractionResult(text="", structured_markdown="", page_spans=[])


def extract_text(path: Path, raw_bytes: bytes | None = None) -> str:
    return extract_document(path, raw_bytes=raw_bytes).text
