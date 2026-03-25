# Testes do Indexador Corrigido — CAF-FINAL

**Data:** 2026-03-25 12:34:43
**Modelo:** gemini-embedding-2-preview (1024 dims MRL)
**ES docs:** 9141
**ChromaDB vetores:** 9141
**ChromaDB dimensão:** 1024

## Resumo

| Bateria | Testes | Passou | Falhou | Taxa |
|---|---:|---:|---:|---:|
| 1 — Validação técnica | 4 | 4 | 0 | 100.0% |
| 2 — Integridade numérica | 22 | 22 | 0 | 100.0% |
| 3 — Peça específica | 17 | 17 | 0 | 100.0% |
| 4 — Conceitual | 8 | 5 | 3 | 62.5% |
| 5 — Filtro hierarquia | 8 | 7 | 1 | 87.5% |
| 6 — Busca cruzada | 6 | 6 | 0 | 100.0% |
| 7 — Stress test | 8 | 8 | 0 | 100.0% |
| 8 — Comparação antes/depois | 4 | 2 | 2 | 50.0% |
| **TOTAL** | **77** | **71** | **6** | **92.2%** |

## Veredicto

- [x] ✅ APROVADO — ≥ 60/77 testes passaram, incluindo ≥ 18/22 na bateria 2
- [ ] ⚠️ AJUSTES — 45-59 testes passaram, corrigir e retestar
- [ ] ❌ REPROVADO — < 45 testes passaram, problema estrutural

## 1 — Validação técnica

- PASSOU: **1.1 Dimensão do vetor Gemini** — Dimensão: 1024
- PASSOU: **1.2 Dimensão do ChromaDB** — Chroma dimensão: 1024; total: 9141
- PASSOU: **1.3 Contagem do Elasticsearch** — ES count: 9141
- PASSOU: **1.4 Diferenciação query/documento na pipeline** — raw_task_type_igual=True; pipeline_com_prefixo_igual=False

## 2 — Integridade numérica

| # | Query | Matriz top 2? | Número? | Proveniência | Score RRF | OK? |
|---|---|---|---|---|---:|---|
| 1 | 27,1% docs | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 2 | 53,55% área | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 3 | 33,33% tipo | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 4 | 68,7% DPI | Sim | Sim | bm25+chroma+faiss | 0.0487 | Sim |
| 5 | 45,92% cartográfico | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 6 | 55,27% duplicações | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 7 | 15,92% municipal | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 8 | 632 municípios | Sim | Sim | bm25+chroma+faiss | 0.0487 | Sim |
| 9 | 3.097 falecidos | Sim | Sim | bm25+chroma+faiss | 0.0487 | Sim |
| 10 | 138 menores | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 11 | 90,62% e-mails | Sim | Sim | bm25+chroma+faiss | 0.0479 | Sim |
| 12 | 93,7% CEPs | Sim | Sim | bm25+chroma+faiss | 0.0481 | Sim |
| 13 | 907 renda | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 14 | 39 PJs CNAE | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 15 | 94,1% metadados | Sim | Sim | bm25+chroma+faiss | 0.0487 | Sim |
| 16 | 84% numéricos | Sim | Sim | bm25+chroma+faiss | 0.0489 | Sim |
| 17 | 92% temporais | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 18 | 59,6 bi Pronaf | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 19 | Leaflet 92,36% | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 20 | 646 amostra | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 21 | 32% conformidade | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |
| 22 | 742 mil renovação | Sim | Sim | bm25+chroma+faiss | 0.0492 | Sim |

## 3 — Peça específica

| Query | Top 1 | OK? |
|---|---|---|
| peça 103 | 04_PECAS_EVIDENCIA/txt_extraido/peca103_adequacao_funcional_docs_texto.txt | Sim |
| peça 106 | 04_PECAS_EVIDENCIA/txt_extraido/peca106_pt_resolucao_dpi_texto.txt | Sim |
| peça 109 | 04_PECAS_EVIDENCIA/txt_extraido/peca109_pt_dimensao_area_final_texto.txt | Sim |
| peça 117 | 04_PECAS_EVIDENCIA/txt_extraido/peca117_texto_com_paginas.txt | Sim |
| peça 121 | 04_PECAS_EVIDENCIA/txt_extraido/peca121_PT12_areas_municipais_impossiveis_texto.txt | Sim |
| peça 111 | 04_PECAS_EVIDENCIA/txt_extraido/peca111_texto_com_paginas.txt | Sim |
| peça 124 | 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto_com_paginas.txt | Sim |
| peça 125 | 04_PECAS_EVIDENCIA/txt_extraido/peca125_PT02_dados_contato_texto.txt | Sim |
| peça 127 | 04_PECAS_EVIDENCIA/txt_extraido/peca127_PT04_cnaes_pj_texto.txt | Sim |
| peça 130 | 04_PECAS_EVIDENCIA/txt_extraido/peca130_pt_outliers_renda_texto.txt | Sim |
| peça 135 | 04_PECAS_EVIDENCIA/txt_extraido/peca135_pt_qualidade_semantica_texto.txt | Sim |
| peça 136 | 04_PECAS_EVIDENCIA/txt_extraido/peca136_pt_unidades_medida_texto.txt | Sim |
| peça 133 | 04_PECAS_EVIDENCIA/txt_extraido/peca133_pt_ambiguidade_temporal_texto.txt | Sim |
| peça 75 | 04_PECAS_EVIDENCIA/txt_extraido/peca075_dicionario_dados_caf_texto.txt | Sim |
| peça 78 | 04_PECAS_EVIDENCIA/txt_extraido/peca078_regras_negocio_caf_texto.txt | Sim |
| peça 137 | 04_PECAS_EVIDENCIA/txt_extraido/peca137_mcr_bacen_texto.txt | Sim |
| peça 150 | 04_PECAS_EVIDENCIA/txt_extraido/peca150_relatorio_tecnico_dcaf_76p_texto.txt | Sim |

## 4 — Conceitual

| Caso | Top resultados | OK? |
|---|---|---|
| método dedutivo | 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf ; 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md ; 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf | Não |
| storytelling propositivo | 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf ; 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf ; 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf | Não |
| exclusão digital | 01_RELATORIO_V2/ACH03_V2.md ; 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md ; 01_RELATORIO_V2/ACH03_V2.md | Sim |
| conhecimento tácito | 01_RELATORIO_V2/ACH04_V2.md ; 01_RELATORIO_V2/ACH04_V2.md ; 03_RELATORIO_V1/relatorio_v1.md | Sim |
| reincidência DAP | 01_RELATORIO_V2/ACH01_V2.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca151_oficio_aeci_acordao_885_texto.txt ; 06_NORMAS_CRITERIOS/nat_tcu/normas_auditoria_nat_tcu.md | Sim |
| autodeclaratório | 01_RELATORIO_V2/ACH01_V2.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca121_texto_com_paginas.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca116_texto_com_paginas.txt | Sim |
| transições tecnológicas | 01_RELATORIO_V2/ACH02_V2.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca117_texto_com_paginas.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca114_texto_com_paginas.txt | Sim |
| liberdade de meios | 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf ; 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf ; 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf | Não |

## 5 — Filtro hierarquia

| Caso | Top resultados | OK? |
|---|---|---|
| 5.1 sem filtro 27,1% | 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-01__27_1pct.md ; 01_RELATORIO_V2/ACH01_V2.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca103_adequacao_funcional_docs_texto.txt | Não |
| 5.2 constituicao 27,1% | 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-01__27_1pct.md ; 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-01__33_33pct.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| 5.3 relatorio_v2 27,1% | 01_RELATORIO_V2/ACH01_V2.md ; 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md ; 01_RELATORIO_V2/ACH01_V2.md | Sim |
| 5.4 pecas 27,1% | 04_PECAS_EVIDENCIA/txt_extraido/peca103_adequacao_funcional_docs_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca103_adequacao_funcional_docs_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca105_texto_com_paginas.txt | Sim |
| 5.5 sem filtro Acórdão 1197 | 01_RELATORIO_V2/ACH01_V2.md ; 01_RELATORIO_V2/ACH03_V2.md ; 01_RELATORIO_V2/VISAO_GERAL_V2.md | Sim |
| 5.6 constituicao Acórdão 1197 | 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md | Sim |
| 5.7 relatorio_v2 Acórdão 1197 | 01_RELATORIO_V2/ACH01_V2.md ; 01_RELATORIO_V2/ACH03_V2.md ; 01_RELATORIO_V2/VISAO_GERAL_V2.md | Sim |
| 5.8 v1 Acórdão 1197 | 03_RELATORIO_V1/relatorio_v1.md ; 03_RELATORIO_V1/relatorio_v1.md ; 03_RELATORIO_V1/relatorio_v1.md | Sim |

## 6 — Busca cruzada

| Caso | Top resultados | OK? |
|---|---|---|
| ACH-01 vs Matriz | 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-01__27_1pct.md ; 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-04__94_1pct.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx | Sim |
| ACH-02 vs Matriz | 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-02__632.md ; 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| ACH-03 vs peça 125 | 04_PECAS_EVIDENCIA/txt_extraido/peca125_PT02_dados_contato_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca125_PT02_dados_contato_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca125_PT02_dados_contato_texto.txt | Sim |
| Proposta 2.1.3 | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| ACH-04 vs peça 135 | 04_PECAS_EVIDENCIA/txt_extraido/peca135_pt_qualidade_semantica_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca135_pt_qualidade_semantica_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca135_pt_qualidade_semantica_texto.txt | Sim |
| Resumo vs Visão Geral | 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md ; 01_RELATORIO_V2/INTRODUCAO_V2.md ; 01_RELATORIO_V2/VISAO_GERAL_V2.md | Sim |

## 7 — Stress test

| Caso | Top resultados | OK? |
|---|---|---|
| 7.1 genérica | 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md ; 03_RELATORIO_V1/relatorio_v1.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca121_texto_com_paginas.txt | Sim |
| 7.2 número isolado | 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-03__3_097.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca137_mcr_bacen_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca120_texto_com_paginas.txt | Sim |
| 7.3 acento | 04_PECAS_EVIDENCIA/txt_extraido/peca107_texto_com_paginas.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca107_texto_com_paginas.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca107_texto_com_paginas.txt | Sim |
| 7.4 parágrafo longo | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md ; 01_RELATORIO_V2/ACH01_V2.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx | Sim |
| 7.5 inglês | 01_RELATORIO_V2/ACH03_V2.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| 7.6 norma específica | 04_PECAS_EVIDENCIA/txt_extraido/peca084_iso_11179_1_texto.txt ; 01_RELATORIO_V2/ACH04_V2.md ; 01_RELATORIO_V2/VISAO_GERAL_V2.md | Sim |
| 7.7 contraditório | 01_RELATORIO_V2/ACH04_V2.md ; 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| 7.8 peça inexistente |  | Sim |

## 8 — Comparação antes/depois

| Teste | Antes | Depois | Melhorou? |
|---|---|---|---|
| 1 — Número | Matriz aparecia, mas V1 ainda podia subir acima; sem ranking unificado | 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-01__27_1pct.md \| 01_RELATORIO_V2/ACH01_V2.md \| 02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-04__94_1pct.md | Sim |
| 2 — Peça | peça 124 já aparecia bem nas 3 listas separadas | 04_PECAS_EVIDENCIA/txt_extraido/peca124_PT01_capacidade_civil_texto.txt \| 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto_com_paginas.txt \| 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto.txt | Sim |
| 3 — Proposta | PECA170 aparecia, mas não necessariamente em #1 | 03_RELATORIO_V1/relatorio_v1.md \| 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto.txt \| 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto_com_paginas.txt | Não |
| 4 — Conceitual | NAT/manual_auditoria em #1 (irrelevante) | 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf \| 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md \| 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md | Não |

## Falhas detalhadas

- **4 — Conceitual** — Query/Teste: `método dedutivo parágrafo-síntese resultado completo`
  Detalhes: `{'name': 'método dedutivo', 'query': 'método dedutivo parágrafo-síntese resultado completo', 'pass': False, 'top_paths': ['06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md', '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf']}`
- **4 — Conceitual** — Query/Teste: `storytelling auditoria operacional tom propositivo`
  Detalhes: `{'name': 'storytelling propositivo', 'query': 'storytelling auditoria operacional tom propositivo', 'pass': False, 'top_paths': ['06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf']}`
- **4 — Conceitual** — Query/Teste: `liberdade de meios resultados a alcançar não prescrição`
  Detalhes: `{'name': 'liberdade de meios', 'query': 'liberdade de meios resultados a alcançar não prescrição', 'pass': False, 'top_paths': ['06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf']}`
- **5 — Filtro hierarquia** — Query/Teste: `27,1% documentos inadequados`
  Detalhes: `{'name': '5.1 sem filtro 27,1%', 'query': '27,1% documentos inadequados', 'pass': False, 'top_paths': ['02_FONTE_VERDADE/NUMEROS_CHAVE/ACH-01__27_1pct.md', '01_RELATORIO_V2/ACH01_V2.md', '04_PECAS_EVIDENCIA/txt_extraido/peca103_adequacao_funcional_docs_texto.txt']}`
- **8 — Comparação antes/depois** — Query/Teste: `Proposta 2.1.3 interoperabilidade bases oficiais`
  Detalhes: `{'name': '3 — Proposta', 'query': 'Proposta 2.1.3 interoperabilidade bases oficiais', 'pass': False, 'before': 'PECA170 aparecia, mas não necessariamente em #1', 'after': '03_RELATORIO_V1/relatorio_v1.md | 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto.txt | 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto_com_paginas.txt'}`
- **8 — Comparação antes/depois** — Query/Teste: `parágrafo-síntese método dedutivo achado documentação`
  Detalhes: `{'name': '4 — Conceitual', 'query': 'parágrafo-síntese método dedutivo achado documentação', 'pass': False, 'before': 'NAT/manual_auditoria em #1 (irrelevante)', 'after': '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf | 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md | 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md'}`

## Consolidação — Reteste pós-patch

| Métrica | Antes do patch | Depois do patch |
|---|---:|---:|
| Bateria 2 | 8/22 (36,4%) | 22/22 (100,0%) |
| Bateria 3 | 17/17 (100,0%) | 17/17 (100,0%) |
| Bateria 4 | 5/8 (62,5%) | 5/8 (62,5%) |
| Bateria 6 | 6/6 (100,0%) | 6/6 (100,0%) |
| TOTAL | 56/77 (72,7%) | 71/77 (92,2%) |

| Painel | Veredicto pós-patch |
|---|---|
| run_panel | timeout |
| swarm_panel | timeout |
| minimax | GO COM RESSALVAS |

### Decisão

- [ ] ✅ GO — rodar revisão noturna
- [x] ⚠️ GO com ressalvas
- [ ] ❌ NO-GO — [o que falta]

### Ressalvas operacionais

- Para números-chave e conferência factual, o índice está pronto.
- Para queries do tipo `Proposta X.Y.Z`, usar `--hierarchy constituicao` até haver boost implícito por regex.
- Para buscas conceituais muito abstratas, validar o topo contra `01_RELATORIO_V2/` antes de aceitar um resultado de `06_NORMAS_CRITERIOS/`.
