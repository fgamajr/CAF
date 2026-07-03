# Indexação CAF-FINAL

## Stack
- Elasticsearch em `http://localhost:9200` (ou `ELASTICSEARCH_URL` no `.env`; frequentemente túnel SSH).
- ChromaDB persistido em `.local/chroma`.
- FAISS persistido em `.local/faiss`.
- Embeddings Gemini via `GEMINI_API_KEY` do `.env`, usando `gemini-embedding-001` com `1024` dimensões.
- PDFs lidos com extração híbrida: `pdftotext` por página + `tesseract` como fallback OCR.

## Setup
```bash
cd /Users/fgamajr/Documents/GitHub/CAF
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-indexing.txt
python3 index_gemini.py --index-all --force
python3 index_gemini.py --status
python3 audit_pdf_extraction.py
```

## Cobertura do índice
O indexador lê `MANIFEST.md` primeiro e prioriza (ver `PRIORITY_GLOBS` em `index_gemini.py`):
1. `02_FONTE_VERDADE/`
2. `01_RELATORIO_V2/`, `03_2_POS_COMENTÁRIOS/`, `achado01/`, `OneDrive_2_23-06-2026/`
3. `04_PECAS_EVIDENCIA/txt_extraido/`
4. `03_1_RELATORIO_V1/`
5. `06_NORMAS_CRITERIOS/`
6. `05_PECAS_TRAMITACAO/` (incl. `nota_tecnica_mda_15/`)
7. `07_MODELOS_TCU/`

`_artefatos_latex/` é ignorada. Duplicatas em `OneDrive_2_23-06-2026/` são excluídas por prefixo.

Contagens atuais: `python3 index_gemini.py --status`.

## Teste rápido
```bash
python3 search_review.py "27,1% de inadequação semântica documental"
python3 search_review.py "peça 171"
python3 search_review.py "Nota Técnica 15 reclassificação 17%"
python3 search_review.py "27,1% documentos" --hierarchy constituicao
```

## Observações
- `extract_pdf_text.py` usa caminhos absolutos antigos e não participa deste fluxo.
- O arquivo `.local/index_state/index_manifest.json` registra a última indexação.
- Consultas só com `peça NNN` filtram por metadata (`piece_number`) de forma determinística.
- Consultas textuais com `peça NNN` no meio aplicam filtro + busca híbrida.
- `search_review.py` faz fusão `RRF` entre `BM25 + ChromaDB + FAISS`.
- Resultados recebem boost por hierarquia documental: `02_FONTE_VERDADE/` > `01_RELATORIO_V2/` > evidências/apoio.
