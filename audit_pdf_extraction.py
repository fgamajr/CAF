#!/usr/bin/env python3
"""
Audita a extração híbrida de PDFs verificando se todas as páginas foram preservadas.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

from pypdf import PdfReader

import index_gemini


ROOT = Path(__file__).resolve().parent
TARGET_DIRS = [
    ROOT / "04_PECAS_EVIDENCIA",
    ROOT / "05_PECAS_TRAMITACAO",
    ROOT / "06_NORMAS_CRITERIOS",
    ROOT / "07_MODELOS_TCU",
]


def find_pdfs() -> list[Path]:
    files: list[Path] = []
    for base in TARGET_DIRS:
        files.extend(sorted(base.rglob("*.pdf")))
    return files


def main() -> int:
    index_gemini.load_environment()
    failures: list[str] = []
    total = 0
    total_ocr_pages = 0

    for pdf in find_pdfs():
        total += 1
        extracted = index_gemini.read_pdf(pdf)
        pdf_pages = len(PdfReader(str(pdf)).pages)
        text_markers = len(re.findall(r"^--- Página \d+ ---$", extracted, re.M))
        ocr_pages = extracted.count("[OCR fallback]")
        total_ocr_pages += ocr_pages
        if pdf_pages != text_markers:
            failures.append(
                f"{pdf.relative_to(ROOT)}: pdf_pages={pdf_pages}, text_markers={text_markers}, ocr_pages={ocr_pages}"
            )

    print(f"PDFs auditados: {total}")
    print(f"Páginas com OCR fallback: {total_ocr_pages}")
    print(f"Falhas de contagem: {len(failures)}")
    if failures:
        print("\n".join(failures[:50]))
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
