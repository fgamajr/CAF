# Repository Guidelines

## Project Structure & Module Organization
Start with `MANIFEST.md`, then read `00_CONTEXTO/` for the executive summary and full case context. Active drafting lives in `01_RELATORIO_V2/` (`INTRODUCAO_V2.md`, `ACH01_V2.md` to `ACH04_V2.md`). Authoritative source documents live in `02_FONTE_VERDADE/`; if anything conflicts with other folders, this directory wins. Historical reference material stays in `03_RELATORIO_V1/`. Evidence is grouped by finding in `04_PECAS_EVIDENCIA/`, procedural records are in `05_PECAS_TRAMITACAO/`, normative references in `06_NORMAS_CRITERIOS/`, and TCU templates in `07_MODELOS_TCU/`. Ignore generated LaTeX byproducts in `_artefatos_latex/`.

## Build, Test, and Development Commands
This repository is primarily Markdown, PDF, DOCX, and reference material, so there is no app build pipeline.

- `python3 extract_pdf_text.py`: extracts text from PDFs into `04_PECAS_EVIDENCIA/txt_extraido/` for search and review.
- `bash reorganizar.sh`: recreates the organized folder layout from the earlier raw archive. Review the hard-coded `BASE` path before running.
- `python3 -m py_compile extract_pdf_text.py`: quick syntax check after editing the Python helper.
- `rg "peça 150|ACHADO 01" 01_RELATORIO_V2 04_PECAS_EVIDENCIA/txt_extraido`: preferred way to trace citations and evidence.

## Coding Style & Naming Conventions
Keep prose and documentation in Portuguese unless a file already establishes a different language. Preserve the repository naming pattern: numbered top-level folders (`00_CONTEXTO`), report files in uppercase topic form (`ACH01_V2.md`), and evidence files as `pecaNNN_descricao_curta.ext`. Use concise Markdown headings, compact tables, and explicit citations such as `peça 103, p. 9`. For scripts, follow existing shell/Python style: 4-space indentation in Python, `set -euo pipefail` in Bash, and avoid introducing absolute paths unless required.

## Testing Guidelines
There is no automated test suite. Validate changes by checking source hierarchy, citation accuracy, and document placement. For script edits, run `python3 -m py_compile extract_pdf_text.py` and spot-check generated `.txt` output against the source PDF. For report edits, compare every factual change against `02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md` and the relevant evidence file.

## Commit & Pull Request Guidelines
Git history is not available in this exported workspace, so no local convention can be inferred from commits. Use short imperative subjects with scope, for example: `docs: refine ACH03 evidence citations` or `scripts: fix PDF extraction output path`. PRs should state which achado or peça was changed, cite the governing source in `02_FONTE_VERDADE/`, list any affected files, and include screenshots only when layout-sensitive templates or rendered outputs changed.

## Security & Contributor Notes
Do not commit secrets from `.env`. Treat `02_FONTE_VERDADE/` as frozen unless the change is formally approved. Do not edit `_artefatos_latex/*.aux`, `.log`, or `.out`; regenerate them instead.
