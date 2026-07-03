# AGENTS.md — CAF-FINAL

TCU operational audit workspace (TC 011.073/2025-0) on CAF 3.0 data quality. Primarily Markdown, PDF, DOCX — no app build pipeline. All prose in Portuguese.

## First read

1. `MANIFEST.md` — master index, document hierarchy, piece catalog, 22 key data points
2. `00_CONTEXTO/RESUMO_EXECUTIVO_V2.md` — 1-page summary
3. `02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md` — the "constitution": all numbers and formulations are definitive here
4. `02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md` — tone and calibration
5. `CLAUDE.md` — full project context, MCP server usage, known bugs, current status

## Document hierarchy (inviolable)

| Level | Source | Rule |
|---|---|---|
| 1 — Constitution | `02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md` | Always prevails over any other source |
| 2 — Calibration | `02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md` | Tone, anchors, concessions to gestor |
| 3 — Report V2 | `01_RELATORIO_V2/*.md` (INTRODUCAO, ACH01-04, RESUMO, VISAO_GERAL) | Document under revision |
| 4 — Evidence | PDFs + `.txt` in `04_PECAS_EVIDENCIA/` | Per-achado evidence |
| 5 — Norms | `06_NORMAS_CRITERIOS/` | ISOs, DAMA-DMBOK, legislation |
| 6 — V1 (historical) | `03_1_RELATORIO_V1/` | Never use as primary source |

If anything conflicts, higher level wins. Cross-check every number against the 22 key data points in `MANIFEST.md` §7.

## Folder map

| Folder | Purpose |
|---|---|
| `00_CONTEXTO/` | Executive summary + overview (start here after MANIFEST) |
| `01_RELATORIO_V2/` | Active drafting: 7 files under review |
| `02_FONTE_VERDADE/` | Frozen unless formally approved — the authoritative source |
| `03_1_RELATORIO_V1/` | Historical reference (peça 141) |
| `03_2_POS_COMENTÁRIOS/` | Final report PDFs post-comentários (peças 170–175) |
| `04_PECAS_EVIDENCIA/` | PDFs grouped by achado + `txt_extraido/` for searchable text |
| `05_PECAS_TRAMITACAO/` | Ofícios, atas, contraditório (peças 142–168), NT MDA 15 |
| `06_NORMAS_CRITERIOS/` | Laws, ISOs, NAT, DAMA-DMBOK |
| `07_MODELOS_TCU/` | TCU report templates |
| `_artefatos_latex/` | Ignore — generated .aux/.log/.out; never index or edit |

## Key commands

### Search the indexed corpus
```bash
source .venv/bin/activate
python3 search_review.py "query text"                    # hybrid RRF (BM25 + ChromaDB + FAISS)
python3 search_review.py "peça 171"                      # metadata filter by piece_number
python3 search_review.py "query" --hierarchy constituicao  # only Matriz (level 1)
python3 search_review.py "query" --hierarchy relatorio_v2  # only V2 sections
python3 search_review.py "query" --hierarchy pos_comentarios  # final report PDFs
python3 search_review.py "query" --hierarchy pecas         # only evidence
python3 search_review.py "query" --k 10                    # more results
```

### Check index status
```bash
python3 index_gemini.py --status
```

### Rebuild index (requires Elasticsearch reachable)
```bash
# Default: http://localhost:9200 (often via SSH tunnel; set ELASTICSEARCH_URL in .env)
python3 index_gemini.py --index-all --force  # full reindex
```

### Run indexer test batteries
```bash
python3 run_indexer_tests.py
```

### Trace citations
```bash
rg "peça 150|ACHADO 01" 01_RELATORIO_V2 04_PECAS_EVIDENCIA/txt_extraido
rg "27,1%" 04_PECAS_EVIDENCIA/txt_extraido/
```

### Script syntax check
```bash
python3 -m py_compile extract_pdf_text.py
python3 -m py_compile index_gemini.py
python3 -m py_compile search_review.py
```

## Paragraph and footnote numbering

Paragraphs are numbered sequentially across the entire V2 report, not per-file:
- §1-7: INTRODUCAO
- §8-12: VISAO_GERAL
- §13-23: ACH-01
- §24-34: ACH-02
- §35-48: ACH-03
- §49+: ACH-04

Footnotes follow the same pattern: ¹-¹⁰ (Intro), ¹¹-²⁰ (VG), ²¹-²² (ACH-01), ²³ (ACH-02), ²⁴ (ACH-03), ²⁵+ (ACH-04).

Tables and figures are also numbered sequentially across the full report.

## Audit rules (operational audit — not fraud/multas)

- Propositive tone, no blame attribution, no fines, no fraud allegations
- All effects are "potential" — never "consumed damage to treasury"
- Deductive method (Bertuol): synthesis paragraph first, then storytelling
- "Freedom of means": proposals define results, not solutions
- Acknowledge gestor advances (CAF 3.0, Leaflet, TED DCAF/UFES)
- The 32% conformity figure comes from peça 150 (gestor's own monitoring) — always caveat it as "gestor data, not audit-verified"

## Review workflow

`PROMPT_REVISAO_INTEGRAL_V2.md` contains the complete 8-pass review checklist + 3 adversarial panels. Read it before any revision work.

## Scripts with hardcoded paths

`extract_pdf_text.py` has absolute paths from a previous environment (`/sessions/vigilant-relaxed-cannon/`). Update `SCAN_DIRS` and `OUTPUT_DIR` before running. The indexer (`index_gemini.py`) uses `ROOT` relative paths and is safe.

## Environment

- `.env` exists locally (gitignored) with API keys for Gemini, Elasticsearch, ChromaDB — keep `chmod 600 .env`
- Python venv at `.venv/`
- Elasticsearch: default `http://localhost:9200` (`ELASTICSEARCH_URL` in `.env`; often SSH tunnel, not necessarily local Docker)
- Embeddings: `gemini-embedding-001` (1024 dims)
- ChromaDB persisted at `.local/chroma/`
- FAISS index at `.local/faiss/`
- PDF text cache at `.local/pdf_text_cache/`
- Word doc cache at `.local/doc_text_cache/`

## MCP servers (available for review)

- **adversarial-mcp** — code review and critique with multiple agents
- **gabi-mcp** — Brazilian legal corpus (DOU, TCU jurisprudence, IBGE, Querido Diário)
- **jurisprudencias-ai** — court decisions search (STF, STJ, TRFs, TJs)
- **car-mgi-audit-knowledge** — indexed audit corpus retrieval (query, answer, stats)

## Security

Do not commit `.env`. Treat `02_FONTE_VERDADE/` as frozen. Do not edit `_artefatos_latex/*.aux`, `.log`, `.out`.
