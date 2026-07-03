# CAF-FINAL

Acervo de trabalho da auditoria do TCU sobre a qualidade dos dados do CAF (`TC 011.073/2025-0`).

## Ponto de partida
- Leia primeiro `MANIFEST.md`.
- Contexto inicial: `00_CONTEXTO/`.
- Fonte de verdade: `02_FONTE_VERDADE/`.
- Texto em revisão: `01_RELATORIO_V2/`.

## Índice de busca local
O repositório já está indexado em:
- Elasticsearch (`caf-final`)
- ChromaDB (`caf-final`)
- FAISS (`.local/faiss/caf-final.index`)
- embeddings Gemini (`gemini-embedding-001`, `1024` dims)

Status atual: rode `python3 index_gemini.py --status` para contagens atuais.

## Cobertura do índice
Corpus indexado via `index_gemini.py` (ver `PRIORITY_GLOBS`):
- `MANIFEST.md`, `README.md`
- `00_CONTEXTO/**/*.md`
- `01_RELATORIO_V2/**/*.md`
- `02_FONTE_VERDADE/**/*.md`, `*.docx`
- `03_1_RELATORIO_V1/**/*.md`, `*.docx`
- `03_2_POS_COMENTÁRIOS/**/*.pdf`
- `04_PECAS_EVIDENCIA/txt_extraido/**/*.txt`
- `05_PECAS_TRAMITACAO/**/*.pdf` (incl. `nota_tecnica_mda_15/`)
- `06_NORMAS_CRITERIOS/**`, `07_MODELOS_TCU/**`
- `achado01/**`, `OneDrive_2_23-06-2026/**` (com exclusões de duplicatas)

Ficam fora do índice por desenho:
- `_artefatos_latex/`
- `.venv/`, `.local/`, `.env`
- scripts e arquivos auxiliares do setup
- outros auxiliares fora do corpus de auditoria

## Extração de PDFs
PDFs são lidos com extração híbrida por página:
1. `pdftotext` quando há camada textual confiável
2. `tesseract` como fallback OCR quando a página vem vazia ou fraca

A auditoria de cobertura garante que o número de páginas extraídas bate com o número de páginas do PDF.

## Uso rápido
```bash
cd /Users/fgamajr/Desktop/CAF-FINAL
source .venv/bin/activate
python3 index_gemini.py --status
python3 search_review.py "peça 171"
python3 search_review.py "Nota Técnica 15 reclassificação 17%"
python3 search_review.py "27,1% documentos semanticamente inadequados" --hierarchy constituicao
python3 search_review.py "27,1% documentos" --hierarchy relatorio_v2
python3 search_review.py "632 municípios com área impossível"
```

Mais detalhes em `INDEXING.md`.
