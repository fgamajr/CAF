# Testes do Indexador Corrigido — CAF-FINAL

**Data:** 2026-03-25 11:55:16
**Modelo:** gemini-embedding-2-preview (1024 dims MRL)
**ES docs:** 9251
**ChromaDB vetores:** 9251
**ChromaDB dimensão:** 1024

## Resumo

| Bateria | Testes | Passou | Falhou | Taxa |
|---|---:|---:|---:|---:|
| 1 — Validação técnica | 4 | 3 | 1 | 75.0% |
| 2 — Integridade numérica | 22 | 8 | 14 | 36.4% |
| 3 — Peça específica | 17 | 17 | 0 | 100.0% |
| 4 — Conceitual | 8 | 5 | 3 | 62.5% |
| 5 — Filtro hierarquia | 8 | 7 | 1 | 87.5% |
| 6 — Busca cruzada | 6 | 6 | 0 | 100.0% |
| 7 — Stress test | 8 | 7 | 1 | 87.5% |
| 8 — Comparação antes/depois | 4 | 3 | 1 | 75.0% |
| **TOTAL** | **77** | **56** | **21** | **72.7%** |

## Veredicto

- [ ] ✅ APROVADO — ≥ 60/77 testes passaram, incluindo ≥ 18/22 na bateria 2
- [x] ⚠️ AJUSTES — 45-59 testes passaram, corrigir e retestar
- [ ] ❌ REPROVADO — < 45 testes passaram, problema estrutural

## Bateria 1 — Validação técnica

- PASSOU: **1.1 Dimensão do vetor Gemini** — Dimensão: 1024
- PASSOU: **1.2 Dimensão do ChromaDB** — Chroma dimensão: 1024; total: 9251
- PASSOU: **1.3 Contagem do Elasticsearch** — ES count: 9251
- FALHOU: **1.4 Task type diferenciado** — Similaridade doc/query: 1.0000; vetores_diferentes=False

## Bateria 2 — Integridade numérica

| # | Query (resumida) | #1/#2 é Matriz? | Número no snippet? | Proveniência | Score RRF | OK? |
|---|---|---|---|---|---:|---|
| 1 | 27,1% docs | Sim | Sim | bm25+chroma+faiss | 0.0434 | Sim |
| 2 | 53,55% área | Sim | Sim | bm25+chroma+faiss | 0.0393 | Sim |
| 3 | 33,33% tipo | Sim | Sim | bm25+chroma+faiss | 0.0448 | Sim |
| 4 | 68,7% DPI | Não | Não | n/a | n/a | Não |
| 5 | 45,92% cartográfico | Não | Não | n/a | n/a | Não |
| 6 | 55,27% duplicações | Não | Não | n/a | n/a | Não |
| 7 | 15,92% municipal | Não | Não | n/a | n/a | Não |
| 8 | 632 municípios | Não | Não | n/a | n/a | Não |
| 9 | 3.097 falecidos | Sim | Sim | bm25+chroma+faiss | 0.0340 | Sim |
| 10 | 138 menores | Não | Não | n/a | n/a | Não |
| 11 | 90,62% e-mails | Não | Não | n/a | n/a | Não |
| 12 | 93,7% CEPs | Sim | Sim | bm25+chroma+faiss | 0.0418 | Sim |
| 13 | 907 renda | Sim | Sim | bm25+chroma+faiss | 0.0414 | Sim |
| 14 | 39 PJs CNAE | Não | Não | n/a | n/a | Não |
| 15 | 94,1% metadados | Não | Não | n/a | n/a | Não |
| 16 | 84% numéricos | Não | Não | n/a | n/a | Não |
| 17 | 92% temporais | Sim | Sim | bm25+chroma+faiss | 0.0388 | Sim |
| 18 | 59,6 bi Pronaf | Não | Não | n/a | n/a | Não |
| 19 | Leaflet 92,36% | Não | Não | n/a | n/a | Não |
| 20 | 646 amostra | Não | Não | n/a | n/a | Não |
| 21 | 32% conformidade | Sim | Sim | bm25+chroma+faiss | 0.0451 | Sim |
| 22 | 742 mil renovação | Não | Não | n/a | n/a | Não |

**Resultado:** 8/22 passaram. Meta do prompt: ≥ 18/22 com Matriz no top 2.

## Bateria 3 — Peça específica

| Query | Top 1 | OK? |
|---|---|---|
| peça 103 | 04_PECAS_EVIDENCIA/txt_extraido/peca103_adequacao_funcional_docs_texto.txt | Sim |
| peça 106 | 04_PECAS_EVIDENCIA/txt_extraido/peca106_pt_resolucao_dpi_texto.txt | Sim |
| peça 109 | 04_PECAS_EVIDENCIA/txt_extraido/peca109_texto_com_paginas.txt | Sim |
| peça 117 | 04_PECAS_EVIDENCIA/txt_extraido/peca117_PT08_duplicacoes_espaciais_texto.txt | Sim |
| peça 121 | 04_PECAS_EVIDENCIA/txt_extraido/peca121_PT12_areas_municipais_impossiveis_texto.txt | Sim |
| peça 111 | 04_PECAS_EVIDENCIA/txt_extraido/peca111_PT02_dimensionamento_leaflet_texto.txt | Sim |
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

**Resultado:** 17/17 passaram. Meta do prompt: ≥ 14/17.

## Bateria 4 — Conceitual

| Query | Top 3 | OK? |
|---|---|---|
| método dedutivo | 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf ; 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md ; 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md | Não |
| storytelling propositivo | 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf ; 04_PECAS_EVIDENCIA/txt_extraido/peca103_texto_com_paginas.txt ; 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf | Não |
| exclusão digital | 01_RELATORIO_V2/ACH03_V2.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 01_RELATORIO_V2/ACH03_V2.md | Sim |
| conhecimento tácito | 01_RELATORIO_V2/ACH04_V2.md ; 01_RELATORIO_V2/ACH04_V2.md ; 03_RELATORIO_V1/relatorio_v1.md | Sim |
| reincidência DAP | 01_RELATORIO_V2/ACH01_V2.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca151_oficio_aeci_acordao_885_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca151_oficio_aeci_acordao_885_texto.txt | Sim |
| autodeclaratório | 04_PECAS_EVIDENCIA/txt_extraido/peca103_texto_com_paginas.txt ; 01_RELATORIO_V2/ACH01_V2.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca121_texto_com_paginas.txt | Sim |
| transições tecnológicas | 01_RELATORIO_V2/ACH02_V2.md ; 04_PECAS_EVIDENCIA/txt_extraido/peca115_texto_com_paginas.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca160_oficio_spoa_incidentes_tic_texto.txt | Sim |
| liberdade de meios | 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md ; 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf ; 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf | Não |

**Resultado:** 5/8 passaram. Meta do prompt: ≥ 5/8.

## Bateria 5 — Filtro hierarquia

| Caso | Top resultados | OK? |
|---|---|---|
| 5.1 sem filtro 27,1% | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md ; 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md | Não |
| 5.2 constituicao 27,1% | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx | Sim |
| 5.3 relatorio_v2 27,1% | 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md ; 01_RELATORIO_V2/ACH01_V2.md ; 01_RELATORIO_V2/ACH01_V2.md | Sim |
| 5.4 pecas 27,1% | 04_PECAS_EVIDENCIA/txt_extraido/peca103_adequacao_funcional_docs_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca103_texto_com_paginas.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca103_adequacao_funcional_docs_texto.txt | Sim |
| 5.5 sem filtro Acórdão 1197 | 01_RELATORIO_V2/ACH01_V2.md ; 01_RELATORIO_V2/ACH01_V2.md ; 03_RELATORIO_V1/relatorio_v1.md | Sim |
| 5.6 constituicao Acórdão 1197 | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| 5.7 relatorio_v2 Acórdão 1197 | 01_RELATORIO_V2/ACH01_V2.md ; 01_RELATORIO_V2/VISAO_GERAL_V2.md ; 01_RELATORIO_V2/ACH01_V2.md | Sim |
| 5.8 v1 Acórdão 1197 | 03_RELATORIO_V1/relatorio_v1.md ; 03_RELATORIO_V1/relatorio_v1.md ; 03_RELATORIO_V1/relatorio_v1.md | Sim |

**Resultado:** 7/8 passaram.

## Bateria 6 — Busca cruzada

| Caso | Top resultados | OK? |
|---|---|---|
| ACH-01 vs Matriz | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx | Sim |
| ACH-02 vs Matriz | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md ; 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md | Sim |
| ACH-03 vs peça 125 | 04_PECAS_EVIDENCIA/txt_extraido/peca125_PT02_dados_contato_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca125_PT02_dados_contato_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca125_PT02_dados_contato_texto.txt | Sim |
| Proposta 2.1.3 | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx ; 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| ACH-04 vs peça 135 | 04_PECAS_EVIDENCIA/txt_extraido/peca135_pt_qualidade_semantica_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca135_pt_qualidade_semantica_texto.txt ; 04_PECAS_EVIDENCIA/txt_extraido/peca135_pt_qualidade_semantica_texto.txt | Sim |
| Resumo vs Visão Geral | 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md ; 01_RELATORIO_V2/INTRODUCAO_V2.md ; 01_RELATORIO_V2/ACH01_V2.md | Sim |

**Resultado:** 6/6 passaram. Meta do prompt: ≥ 5/6.

## Bateria 7 — Stress test

| Caso | Top resultados / comportamento | OK? |
|---|---|---|
| 7.1 genérica | 04_PECAS_EVIDENCIA/txt_extraido/peca72_texto_com_paginas.txt \| 03_RELATORIO_V1/relatorio_v1.md \| 04_PECAS_EVIDENCIA/txt_extraido/peca071_ata_reuniao_apresentacao_20250701_texto.txt | Sim |
| 7.2 número isolado | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md \| 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md \| 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| 7.3 acento | 04_PECAS_EVIDENCIA/txt_extraido/peca078_regras_negocio_caf_texto.txt \| 03_RELATORIO_V1/relatorio_v1.md \| 04_PECAS_EVIDENCIA/txt_extraido/peca107_texto_com_paginas.txt | Sim |
| 7.4 parágrafo longo | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md \| 01_RELATORIO_V2/ACH01_V2.md \| 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx | Sim |
| 7.5 inglês | 01_RELATORIO_V2/ACH03_V2.md \| 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md \| 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md | Sim |
| 7.6 norma específica | 04_PECAS_EVIDENCIA/txt_extraido/peca084_iso_11179_1_texto.txt \| 01_RELATORIO_V2/ACH04_V2.md \| 04_PECAS_EVIDENCIA/txt_extraido/peca084_iso_11179_1_texto.txt | Sim |
| 7.7 contraditório | 01_RELATORIO_V2/ACH04_V2.md \| 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md \| 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md | Não |
| 7.8 peça inexistente |  | Sim |

**Resultado:** 7/8 passaram.

## Bateria 8 — Comparação antes/depois

| Teste | Antes (embedding-001, sem RRF) | Depois (embedding-2, RRF+boost) | Melhorou? |
|---|---|---|---|
| 1 — Número | Matriz aparecia, mas V1 ainda podia subir acima; sem ranking unificado | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx \| 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md \| 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md | Sim |
| 2 — Peça | peça 124 já aparecia bem nas 3 listas separadas | 04_PECAS_EVIDENCIA/txt_extraido/peca124_PT01_capacidade_civil_texto.txt \| 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto.txt \| 04_PECAS_EVIDENCIA/txt_extraido/peca124_texto.txt | Sim |
| 3 — Proposta | PECA170 aparecia, mas não necessariamente em #1 | 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx \| 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md \| 02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md | Sim |
| 4 — Conceitual | NAT/manual_auditoria em #1 (irrelevante) | 06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf \| 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md \| 06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md | Não |

**Resultado:** 3/4 melhoraram materialmente.

## Falhas detalhadas

- **Bateria 2** — Query: `68,7% resolução inferior 300 DPI`
  Obtido: `['04_PECAS_EVIDENCIA/txt_extraido/peca106_pt_resolucao_dpi_texto.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca106_texto_com_paginas.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca106_pt_resolucao_dpi_texto.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `45,92% erro cartográfico imóveis`
  Obtido: `['01_RELATORIO_V2/ACH02_V2.md', '01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md', '03_RELATORIO_V1/relatorio_v1.md']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `55,27% duplicações espaciais`
  Obtido: `['04_PECAS_EVIDENCIA/txt_extraido/peca117_PT08_duplicacoes_espaciais_texto.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca117_PT08_duplicacoes_espaciais_texto.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca117_texto_com_paginas.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `15,92% inconsistência municipal`
  Obtido: `['04_PECAS_EVIDENCIA/txt_extraido/peca116_texto_com_paginas.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca116_PT07_consistencia_municipal_texto.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca116_texto_com_paginas.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `632 municípios inflação cadastral`
  Obtido: `['04_PECAS_EVIDENCIA/txt_extraido/peca121_texto_com_paginas.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca121_PT12_areas_municipais_impossiveis_texto.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca121_PT12_areas_municipais_impossiveis_texto.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `138 menores responsáveis unidades familiares`
  Obtido: `['03_RELATORIO_V1/relatorio_v1.md', '03_RELATORIO_V1/relatorio_v1.md', '04_PECAS_EVIDENCIA/txt_extraido/peca124_texto.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `90,62% e-mails fictícios pessoa física`
  Obtido: `['01_RELATORIO_V2/ACH03_V2.md', '03_RELATORIO_V1/relatorio_v1.docx', '03_RELATORIO_V1/relatorio_v1.md']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `39 pessoas jurídicas CNAE incompatível`
  Obtido: `['01_RELATORIO_V2/ACH03_V2.md', '04_PECAS_EVIDENCIA/txt_extraido/peca127_PT04_cnaes_pj_texto.txt', '02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `94,1% descrições dicionário inadequadas`
  Obtido: `['04_PECAS_EVIDENCIA/txt_extraido/peca135_pt_qualidade_semantica_texto.txt', '03_RELATORIO_V1/relatorio_v1.md', '03_RELATORIO_V1/relatorio_v1.md']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `84% campos numéricos sem unidade medida`
  Obtido: `['04_PECAS_EVIDENCIA/txt_extraido/peca136_pt_unidades_medida_texto.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca132_mc_index_achado04_texto.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca136_pt_unidades_medida_texto.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `59,6 bilhões Pronaf safra`
  Obtido: `['01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md', '00_CONTEXTO/RESUMO_EXECUTIVO_V2.md', '04_PECAS_EVIDENCIA/txt_extraido/peca137_mcr_bacen_texto.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `92,36% 16,59% Leaflet duplicações`
  Obtido: `['04_PECAS_EVIDENCIA/txt_extraido/peca117_PT08_duplicacoes_espaciais_texto.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca117_texto_com_paginas.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca117_texto_com_paginas.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `646 amostra probabilística documentos`
  Obtido: `['04_PECAS_EVIDENCIA/txt_extraido/peca103_texto_com_paginas.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca103_texto_com_paginas.txt', '04_PECAS_EVIDENCIA/txt_extraido/peca156_relatorio_monitoramento_caf_texto.txt']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 2** — Query: `742 mil renovação registros`
  Obtido: `['01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md', '04_PECAS_EVIDENCIA/txt_extraido/peca152_caf_em_numeros_32p_texto.txt', '00_CONTEXTO/RESUMO_EXECUTIVO_V2.md']`
  Esperado: Matriz no top 2 com número e proveniência forte
- **Bateria 4** — Query: `método dedutivo parágrafo-síntese resultado completo`
  Obtido: `['06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md', '06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md']`
  Esperado: resultado relevante do V2 no top 3
- **Bateria 4** — Query: `storytelling auditoria operacional tom propositivo`
  Obtido: `['06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '04_PECAS_EVIDENCIA/txt_extraido/peca103_texto_com_paginas.txt', '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf']`
  Esperado: resultado relevante do V2 no top 3
- **Bateria 4** — Query: `liberdade de meios resultados a alcançar não prescrição`
  Obtido: `['02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md', '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf']`
  Esperado: resultado relevante do V2 no top 3
- **Bateria 5** — Query: `27,1% documentos inadequados --hierarchy None`
  Obtido: `['02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.docx', '02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md', '01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md']`
  Esperado: Matriz #1 e V2 #2
- **Bateria 7** — Query: `gestor concordou expressamente governança dados imatura`
  Obtido: `01_RELATORIO_V2/ACH04_V2.md | 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md | 02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md`
  Esperado: não crashar e retornar algo coerente quando aplicável
- **Bateria 8** — Query: `parágrafo-síntese método dedutivo achado documentação`
  Obtido: `['06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf', '06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md', '06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md']`
  Esperado: melhora material em relação ao cenário anterior

## Consolidação — Revisão adversária do indexador

| Painel | Veredicto | Condições |
|---|---|---|
| jury_panel (kimi/qwen/zai × 3r) | Timeout da integração | Sem transcript; ver [TESTES_JURY_PANEL.md](/Users/fgamajr/Desktop/CAF-FINAL/TESTES_JURY_PANEL.md) |
| swarm eng./auditor/adversário | Timeout da integração | Sem transcript; ver [TESTES_SWARM_PANEL.md](/Users/fgamajr/Desktop/CAF-FINAL/TESTES_SWARM_PANEL.md) |
| minimax GO/NO-GO | NO-GO | Implementar pós-processamento/boost numérico e rerodar a bateria 2 |

### Decisão final

- [ ] ✅ GO — rodar revisão noturna
- [ ] ⚠️ GO com ressalvas — rodar, mas com condições
- [x] ❌ NO-GO — corrigir a recuperação dos números-chave antes de rodar
