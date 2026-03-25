#!/usr/bin/env python3
"""
Extract text from PDFs in CAF-FINAL structure.
Skips PDFs that already have corresponding .txt files.
"""

import os
import sys
from pathlib import Path
from pypdf import PdfReader

# Configuration
SCAN_DIRS = [
    "/sessions/vigilant-relaxed-cannon/mnt/CAF-FINAL/04_PECAS_EVIDENCIA",
    "/sessions/vigilant-relaxed-cannon/mnt/CAF-FINAL/05_PECAS_TRAMITACAO",
]

OUTPUT_DIR = "/sessions/vigilant-relaxed-cannon/mnt/CAF-FINAL/04_PECAS_EVIDENCIA/txt_extraido"

def get_all_pdfs(directories):
    """Recursively find all PDF files in the given directories."""
    pdfs = []
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith('.pdf'):
                    pdfs.append(os.path.join(root, file))
    return sorted(pdfs)

def txt_exists(pdf_path):
    """Check if a .txt file already exists for this PDF."""
    basename = os.path.basename(pdf_path)
    name_without_ext = os.path.splitext(basename)[0]
    txt_path = os.path.join(OUTPUT_DIR, f"{name_without_ext}_texto.txt")
    return os.path.exists(txt_path)

def extract_pdf_text(pdf_path):
    """Extract text from a PDF file, returning (success, text_or_error)."""
    try:
        reader = PdfReader(pdf_path)
        text_parts = []

        for page_num, page in enumerate(reader.pages, 1):
            text_parts.append(f"--- Página {page_num} ---")
            text = page.extract_text()
            if text:
                text_parts.append(text)
            text_parts.append("")

        return True, "\n".join(text_parts)
    except Exception as e:
        return False, str(e)

def save_extracted_text(pdf_path, text):
    """Save extracted text to output directory."""
    basename = os.path.basename(pdf_path)
    name_without_ext = os.path.splitext(basename)[0]
    output_path = os.path.join(OUTPUT_DIR, f"{name_without_ext}_texto.txt")

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    return output_path

def main():
    print("=" * 70)
    print("PDF Text Extraction Script")
    print("=" * 70)
    print()

    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Get all PDFs
    all_pdfs = get_all_pdfs(SCAN_DIRS)
    print(f"Total PDFs found: {len(all_pdfs)}")
    print()

    # Statistics
    already_extracted = 0
    successfully_extracted = 0
    failed_extractions = 0
    failed_pdfs = []

    # Process each PDF
    for idx, pdf_path in enumerate(all_pdfs, 1):
        pdf_name = os.path.basename(pdf_path)

        # Check if already extracted
        if txt_exists(pdf_path):
            already_extracted += 1
            print(f"[{idx}/{len(all_pdfs)}] SKIP (exists): {pdf_name}")
            continue

        # Extract text
        print(f"[{idx}/{len(all_pdfs)}] EXTRACTING: {pdf_name}", end=" ... ")
        success, result = extract_pdf_text(pdf_path)

        if success:
            output_path = save_extracted_text(pdf_path, result)
            successfully_extracted += 1
            print("OK")
        else:
            failed_extractions += 1
            failed_pdfs.append((pdf_name, result))
            print(f"FAILED: {result}")

    # Print summary
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    print(f"Total PDFs processed: {len(all_pdfs)}")
    print(f"Already had text:     {already_extracted}")
    print(f"Newly extracted:      {successfully_extracted}")
    print(f"Failed:               {failed_extractions}")
    print()

    if failed_pdfs:
        print("Failed PDFs:")
        for pdf_name, error in failed_pdfs:
            print(f"  - {pdf_name}: {error[:100]}")

    print()
    print("=" * 70)

if __name__ == "__main__":
    main()
