# Indexação CAF-FINAL

## Stack
- Elasticsearch em `http://localhost:9200` para busca lexical BM25.
- ChromaDB persistido em `.local/chroma`.
- FAISS persistido em `.local/faiss`.
- Embeddings Gemini via `GEMINI_API_KEY` do `.env`, usando `gemini-embedding-2-preview` com `1024` dimensões (`MRL`).
- PDFs lidos com extração híbrida: `pdftotext` por página + `tesseract` como fallback OCR.

## Setup
```bash
cd /Users/fgamajr/Desktop/CAF-FINAL
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-indexing.txt
bash scripts/start_elasticsearch.sh
python3 index_gemini.py --index-all --force
python3 index_gemini.py --status
python3 audit_pdf_extraction.py
```

## Cobertura do índice
O indexador lê `MANIFEST.md` primeiro e prioriza:
1. `02_FONTE_VERDADE/`
2. `01_RELATORIO_V2/`
3. `04_PECAS_EVIDENCIA/txt_extraido/`
4. `03_RELATORIO_V1/`
5. `06_NORMAS_CRITERIOS/`
6. `05_PECAS_TRAMITACAO/`

`_artefatos_latex/` é ignorada.

Cobertura atual:
- `9251` chunks indexados em Elasticsearch, ChromaDB e FAISS
- `107` PDFs auditados
- `24` páginas com OCR fallback
- `0` falhas de contagem de páginas

Escopo incluído:
- `MANIFEST.md`
- `README.md`
- `00_CONTEXTO/**/*.md`
- `01_RELATORIO_V2/**/*.md`
- `02_FONTE_VERDADE/**/*.md`
- `02_FONTE_VERDADE/**/*.docx`
- `03_RELATORIO_V1/**/*.md`
- `03_RELATORIO_V1/**/*.docx`
- `04_PECAS_EVIDENCIA/txt_extraido/**/*.txt`
- PDFs de `04_PECAS_EVIDENCIA/`, `05_PECAS_TRAMITACAO/`, `06_NORMAS_CRITERIOS/` e `07_MODELOS_TCU/`
- `06_NORMAS_CRITERIOS/**/*.doc`
- `06_NORMAS_CRITERIOS/**/*.docx`
- `07_MODELOS_TCU/**/*.docx`

Escopo excluído:
- `_artefatos_latex/`
- `.venv/`, `.local/`, `.env`
- scripts e auxiliares de infraestrutura
- outros auxiliares fora do corpus

## Teste rápido
```bash
python3 search_review.py "27,1% de inadequação semântica documental"
python3 search_review.py "qual peça sustenta os 632 municípios com área impossível?"
python3 search_review.py "peça 150 contraditório conformidade 32%"
python3 search_review.py "27,1% documentos" --hierarchy constituicao
```

## Observações
- `extract_pdf_text.py` e `reorganizar.sh` usam caminhos absolutos antigos e não participam deste fluxo novo.
- O arquivo `.local/index_state/index_manifest.json` registra a última indexação.
- Consultas com `peça XXX` aplicam filtro por número de peça em BM25, ChromaDB e FAISS.
- `search_review.py` faz fusão `RRF` entre `BM25 + ChromaDB + FAISS`, mostrando proveniência por backend.
- Resultados recebem boost por hierarquia documental: `02_FONTE_VERDADE/` > `01_RELATORIO_V2/` > evidências/apoio.
- `PROMPT_REVISAO_INTEGRAL_V2.md` já está pronto para orientar a revisão do V2 sobre esta base indexada.
- `audit_pdf_extraction.py` confere se o número de páginas do PDF bate com os marcadores `--- Página N ---` do texto extraído.
