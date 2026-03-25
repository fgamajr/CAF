# MANIFEST.md — Índice Mestre do Projeto CAF-FINAL

> **LEIA ESTE ARQUIVO PRIMEIRO.** Este é o mapa completo do projeto.
> Se você é um agente LLM começando do zero, siga a ordem de leitura indicada.

---

## 1. Contexto do Projeto

Auditoria operacional do TCU (TC 011.073/2025-0) sobre a qualidade dos dados do Cadastro Nacional da Agricultura Familiar (CAF 3.0). Avalia se os mecanismos de verificação de dados asseguram requisitos de qualidade e se a governança de dados assegura padrões, papéis, rastreabilidade e integridade. Quatro achados: documentação comprobatória (ACH-01), integridade geoespacial (ACH-02), qualidade cadastral (ACH-03) e gestão de metadados (ACH-04). Período: março-agosto/2025. Unidade fiscalizada: SAF/MDA.

---

## 2. Hierarquia de Documentos (INVIOLÁVEL)

| Nível | Documento | Pasta | Regra |
|---|---|---|---|
| 1 — Constituição | `PECA170_MATRIZ_DE_ACHADOS_CAF.md` | `02_FONTE_VERDADE/` | Lei maior: toda narrativa deve ser consistente com esta matriz |
| 2 — Lei complementar | `PECA169_codex_anexo_comentarios_gestor_v2.md` | `02_FONTE_VERDADE/` | Tom e calibragem: define como responder ao gestor |
| 3 — Relatório V2 (em revisão) | `ACH01_V2.md` a `ACH04_V2.md` + `INTRODUCAO_V2.md` | `01_RELATORIO_V2/` | O documento que está sendo revisado |
| 4 — Peças de evidência | PDFs e .txt em `04_PECAS_EVIDENCIA/` | Por achado | Sustentam os achados — dados, estatísticas, peças processuais |
| 5 — Normas e critérios | ISOs, DAMA-DMBOK, NAT, legislação | `06_NORMAS_CRITERIOS/` | Referenciais técnicos e legais |
| 6 — Relatório V1 | `relatorio_v1.md` | `03_RELATORIO_V1/` | Referência histórica — NÃO usar como fonte primária |

**Regra de ouro:** Se houver conflito entre níveis, prevalece o nível superior.

---

## 3. Ordem de Leitura para o Agente LLM

1. **Este MANIFEST.md** — entender o mapa
2. **00_CONTEXTO/RESUMO_EXECUTIVO_V2.md** — visão de 1 página
3. **00_CONTEXTO/VISAO_GERAL_V2.md** — contexto completo
4. **02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md** — a lei maior
5. **02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md** — tom e calibragem
6. **01_RELATORIO_V2/** — as seções a revisar (INTRODUCAO, ACH01-04)
7. **04_PECAS_EVIDENCIA/** — evidências conforme necessidade por achado
8. **06_NORMAS_CRITERIOS/** — consulta conforme necessidade

---

## 4. Mapa de Pastas

| Pasta | Conteúdo | Arquivos |
|---|---|---|
| `00_CONTEXTO/` | Resumo executivo e visão geral — ponto de partida | 2 .md |
| `01_RELATORIO_V2/` | Seções do relatório V2 em revisão | 5 .md |
| `02_FONTE_VERDADE/` | Matriz de Achados + Anexo Comentários Gestor | 3 arquivos |
| `03_RELATORIO_V1/` | Relatório V1 (peça 141) + codex de upgrades | 3 arquivos |
| `04_PECAS_EVIDENCIA/` | Peças processuais por achado + texto extraído | ~50 PDFs + .txt |
| `05_PECAS_TRAMITACAO/` | Ofícios, atas, despachos, termos | ~50 PDFs |
| `06_NORMAS_CRITERIOS/` | Legislação, ISOs, DAMA-DMBOK, NAT | ~15 arquivos |
| `07_MODELOS_TCU/` | Templates de relatório | 2 arquivos |
| `_artefatos_latex/` | .aux/.log/.out isolados (não indexar) | 9 arquivos |

---

## 5. Índice de Peças por Achado

### ACH-01 — Insuficiência da documentação comprobatória

| Peça | Arquivo | Conteúdo | Dados-chave |
|---|---|---|---|
| 103 | `peca103_adequacao_funcional_docs.pdf` | Análise de adequação funcional dos documentos | 27,1% inadequados (n=646, IC 99%) |
| 104 | `peca104_documentos_dimensao_area.pdf` | Documentos da dimensão área | Suporte ao ACH-01 |
| 105 | `peca105_analise_dimensao_area.pdf` | Análise de dimensão de área | 33,33% tipo inadequado |
| 106 | `peca106_pt_resolucao_dpi.pdf` | Papel de trabalho — resolução DPI | 68,7% abaixo de 300 DPI |
| 107 | `peca107_pt_analise_quatro_modulos.pdf` | Análise dos 4 módulos fiscais | 98,7% cadastradas antes do CAF 3.0 |
| 109 | `peca109_pt_dimensao_area_final.pdf` | Análise de área — versão final | 53,55% divergência crítica (n=155) |
| 140 | `peca140_nota_tecnica_populacao.pdf` | Nota técnica de atualização da população | Projeção: ~3,08M documentos |

### ACH-02 — Integridade geoespacial

| Peça | Arquivo | Conteúdo | Dados-chave |
|---|---|---|---|
| 110 | `peca110_PT01_filtro_uf_ativa.pdf` | PT-01: Filtro UF ativa | Base de análise |
| 111 | `peca111_PT02_dimensionamento_leaflet.pdf` | PT-02: Dimensionamento Leaflet | Regressão de precisão |
| 112 | `peca112_PT03_dimensionamento_caf3.pdf` | PT-03: Dimensionamento CAF 3.0 | Comparativo versões |
| 113 | `peca113_PT04_extracao_amostral.pdf` | PT-04: Extração amostral | Amostra geoespacial |
| 114 | `peca114_PT05_deteccao_algoritmica.pdf` | PT-05: Detecção algorítmica | Erros algorítmicos |
| 115 | `peca115_PT06_analise_precisao.pdf` | PT-06: Análise de precisão | Precisão decimal |
| 116 | `peca116_PT07_consistencia_municipal.pdf` | PT-07: Consistência municipal | 15,92% inconsistências |
| 117 | `peca117_PT08_duplicacoes_espaciais.pdf` | PT-08: Duplicações espaciais | 55,27% coordenadas idênticas |
| 118 | `peca118_PT09_analise_temporal_leaflet.pdf` | PT-09: Análise temporal Leaflet | Série temporal |
| 119 | `peca119_PT10_analise_temporal_caf30.pdf` | PT-10: Análise temporal CAF 3.0 | Taxa erro: 45,92% |
| 120 | `peca120_PT11_validacao_temporal.pdf` | PT-11: Validação temporal estratos | Equivalência |
| 121 | `peca121_PT12_areas_municipais_impossiveis.pdf` | PT-12: Áreas municipais impossíveis | 632 municípios |
| 122 | `peca122_MC_master_index_ach02.pdf` | Master Index — Achado 02 | Índice de variáveis |

### ACH-03 — Qualidade dos dados cadastrais

| Peça | Arquivo | Conteúdo | Dados-chave |
|---|---|---|---|
| 123 | `peca123_pt_salvador_populacao.pdf` | PT: Salvador — população total | Contexto populacional |
| 124 | `peca124_PT01_capacidade_civil.pdf` | PT-01: Capacidade civil | 3.097 óbitos + 138 menores |
| 125 | `peca125_PT02_dados_contato.pdf` | PT-02: Dados de contato | 90,62% e-mails fictícios |
| 126 | `peca126_PT03_renda_outliers.pdf` | PT-03: Outliers de renda | 907 registros > R$ 1M |
| 127 | `peca127_PT04_cnaes_pj.pdf` | PT-04: CNAEs de PJ | CNAEs incompatíveis |
| 128 | `peca128_mc_master_index.pdf` | Master Index — Achado 03 | Índice de variáveis |
| 129 | `peca129_scripts_labcontas.pdf` | Scripts PT-01 LabContas/SQLServer | Código das queries |
| 130 | `peca130_pt_outliers_renda.pdf` | PT: Outliers de renda (LaTeX) | Detalhamento renda |
| 131 | `peca131_pt_capacidade_civil.pdf` | PT: Capacidade civil (LaTeX) | Detalhamento óbitos |
| 132 | `peca132_mc_index_achado04.pdf` | MC Index Achado 04 | Índice complementar |

### ACH-04 — Gestão de metadados

| Peça | Arquivo | Conteúdo | Dados-chave |
|---|---|---|---|
| 133 | `peca133_pt_ambiguidade_temporal.pdf` | PT: Ambiguidade temporal | Campos temporais |
| 134 | `peca134_pt_cobertura_dicionario.pdf` | PT: Cobertura do dicionário | 109 tabelas |
| 135 | `peca135_pt_qualidade_semantica.pdf` | PT: Qualidade semântica | 94,1% descrições inadequadas |
| 136 | `peca136_pt_unidades_medida.pdf` | PT: Unidades de medida | 84% sem unidade |

### Peças transversais (múltiplos achados)

| Peça | Arquivo | Conteúdo |
|---|---|---|
| 75 | `peca075_dicionario_dados_caf.pdf` | Dicionário de dados do CAF |
| 76 | `peca076_modelo_entidade_relacionamento.pdf` | MER do CAF |
| 77 | `peca077_especificacoes_ambiente_caf.pdf` | Especificações do ambiente |
| 78 | `peca078_regras_negocio_caf.pdf` | Regras de negócio do CAF 3.0 |
| 108 | `peca108_portaria_mda_19_2025.pdf` | Portaria MDA 19/2025 |

### Peças de tramitação pós-relatório (contraditório)

| Peça | Arquivo | Conteúdo |
|---|---|---|
| 142 | `peca142_pronunciamento_subunidade_audti.pdf` | Anuência do supervisor |
| 143 | `peca143_pronunciamento_unidade_audti.pdf` | Encaminha relatório ao MDA |
| 144 | `peca144_oficio_4045_seproc_diligencia.pdf` | Ofício de diligência |
| 145 | `peca145_termo_ciencia_conecta_tcu.pdf` | Ciência pelo MDA |
| 146 | `peca146_oficio_28_aeci_prorrogacao.pdf` | Pedido de prorrogação |
| 147 | `peca147_despacho_prorrogacao_prazo.pdf` | Deferimento prorrogação |
| 148 | `peca148_oficio_aeci_encaminhamento.pdf` | Encaminhamento ao TCU |
| 149 | `peca149_oficio_dcaf_manifestacao.pdf` | Manifestação DCAF |
| 150 | `peca150_relatorio_tecnico_dcaf_76p.pdf` | Relatório técnico DCAF (76p) — PEÇA CENTRAL do contraditório |
| 151 | `peca151_oficio_aeci_acordao_885.pdf` | Ofício sobre Acórdão 885/2024 |
| 152 | `peca152_caf_em_numeros_32p.pdf` | CAF em números (indicadores) |
| 153 | `peca153_organograma_dcaf_20p.pdf` | Organograma DCAF |
| 154 | `peca154_nota_tecnica_cgti_tic.pdf` | NT CGTI — contratação TIC |
| 155 | `peca155_etp_contratacao_tic_81p.pdf` | ETP contratação TIC (81p) |
| 156 | `peca156_relatorio_monitoramento_caf.pdf` | Monitoramento CAF 2º sem/2024 |
| 157 | `peca157_nota_tecnica_ted_ufes.pdf` | NT — TED UFES formação |
| 158 | `peca158_plano_trabalho_ted_ufes.pdf` | Plano de trabalho TED UFES |
| 159 | `peca159_contrato_dataprev.pdf` | Contrato TIC Dataprev |
| 160 | `peca160_oficio_spoa_incidentes_tic.pdf` | Incidentes TIC/MAPA |
| 161 | `peca161_memoria_tecnica_doc121.pdf` | Reanálise municipal |
| 162 | `peca162_apresentacao_caf_governanca.pdf` | Apresentação CAF/governança |
| 163 | `peca163_anexo_tecnico_achado01.pdf` | Anexo técnico Achado I |
| 164 | — | **AUSENTE DO ACERVO** |
| 165 | `peca165_nota_tecnica_cafweb.pdf` | NT — intermitência CAFWeb |
| 166 | `peca166_memoria_tecnica_doc105.pdf` | Conferência Doc. 105 |
| 167 | `peca167_termo_recebimento_area_validation.pdf` | Recebimento planilha área |
| 168 | `peca168_termo_recebimento_inflacao_municipal.pdf` | Recebimento planilha inflação |

---

## 6. Índice de Normas e Critérios

| Norma | Arquivo | Para que serve |
|---|---|---|
| Lei 11.326/2006 | `06_NORMAS_CRITERIOS/legislacao/lei_11326_2006.pdf` + `peca080` | Agricultura Familiar — requisitos de elegibilidade |
| Decreto 9.064/2017 | `06_NORMAS_CRITERIOS/legislacao/decreto_9064_2017.pdf` + `peca081` | Institui o CAF |
| Portaria MDA 19/2025 | `06_NORMAS_CRITERIOS/legislacao/portaria_mda_19_2025.pdf` + `peca108` | Operacionaliza o CAF 3.0 |
| Resolução TCU 315/2020 | `06_NORMAS_CRITERIOS/nat_tcu/resolucao_tcu_315_2020.doc` | Procedimentos de auditoria |
| ISO/IEC 25012:2008 | `06_NORMAS_CRITERIOS/iso_referenciais/ISO_IEC_25012_2008.pdf` + `peca085` | Qualidade de dados |
| ISO 19157-1:2023 | `06_NORMAS_CRITERIOS/iso_referenciais/ISO_19157_1_2023.pdf` + `peca083` | Qualidade geoespacial |
| ISO/IEC 11179:2023 | `06_NORMAS_CRITERIOS/iso_referenciais/ISO_IEC_11179_1_2023.pdf` + `peca084` | Gestão de metadados |
| ISO 8000-2:2022 | `06_NORMAS_CRITERIOS/iso_referenciais/ISO_8000_2_2022.pdf` + `peca082` | Qualidade de dados master |
| DAMA-DMBOK v2 | `06_NORMAS_CRITERIOS/iso_referenciais/dama_dmbok_2ed.pdf` + `peca086` | Governança de dados |
| Manual Auditoria Operacional 4ª ed. | `06_NORMAS_CRITERIOS/nat_tcu/manual_auditoria_operacional_4ed.pdf` | NAT — fonte autoritativa |
| Manual de Redação TCU | `06_NORMAS_CRITERIOS/nat_tcu/manual_de_redacao.pdf` | Padrão redacional |
| MCR Bacen | `peca137_mcr_bacen.pdf` | Manual de Crédito Rural |
| Resolução Conarq | `peca079_resolucao_conarq.pdf` | Digitalização documental |

---

## 7. Dados-Chave da Auditoria (para verificação cruzada)

| # | Dado | Valor | Fonte |
|---|---|---|---|
| 1 | Unidades familiares ativas | ~3,3 milhões | peça 152, p. 4 |
| 2 | Imóveis cadastrados | ~3,2 milhões | peça 152, p. 4 |
| 3 | Documentos digitalizados | ~11,4 milhões | peça 103 |
| 4 | Tabelas do banco de dados | 109 | peça 134, p. 4 |
| 5 | Agentes da Rede CAF | ~10 mil | peça 152, p. 6 |
| 6 | Recursos Pronaf safra 2023/2024 | R$ 59,6 bilhões | dado público |
| 7 | Inadequação semântica documental | 27,1% (n=646, IC 99%) | peça 103, p. 9 |
| 8 | Projeção documentos inadequados | ~3,08 milhões | peça 140, p. 5 |
| 9 | Tipo documental inadequado (imóvel) | 33,33% | peça 105, p. 7 |
| 10 | Divergência crítica de área | 53,55% (n=155) | peça 109, p. 7 |
| 11 | Divergência agregada de área | +120,89% | peça 109, p. 9 |
| 12 | Resolução < 300 DPI | 68,7% | peça 106, p. 7 |
| 13 | Taxa erro cartográfico | 45,92% (~1,46M imóveis) | peça 119, p. 9 |
| 14 | Coordenadas idênticas | 55,27% | peça 117 |
| 15 | Municípios com área impossível | 632 | peça 121 |
| 16 | Titulares falecidos ativos | 3.097 | peça 124, p. 9 |
| 17 | Menores como responsáveis | 138 (89 + 49) | peça 124, p. 8 |
| 18 | E-mails PF fictícios | 90,62% | peça 125 |
| 19 | Renda > R$ 1 milhão | 907 registros | peça 126 |
| 20 | Descrições dicionário inadequadas | 94,1% | peça 135, p. 4 |
| 21 | Campos sem unidade de medida | 84% | peça 136 |
| 22 | Conformidade no monitoramento gestor | 32% | peça 150, p. 22 |

---

## 8. Instruções para o Agente LLM

### 8.1 Como indexar

1. **Texto:** Indexar todos os `.md` e `.txt` em `04_PECAS_EVIDENCIA/txt_extraido/`
2. **PDFs:** Usar pypdf para extrair texto dos PDFs que não têm .txt
3. **Prioridade:** Indexar primeiro `02_FONTE_VERDADE/` e `01_RELATORIO_V2/`
4. **Chunking:** Respeitar limites de parágrafo (§§ numerados) como unidade mínima

### 8.2 Como buscar

- **Por achado:** Ir direto à subpasta correspondente em `04_PECAS_EVIDENCIA/`
- **Por peça:** Usar `peca###_` como prefixo de busca (zero-padded a 3 dígitos)
- **Por norma:** Consultar `06_NORMAS_CRITERIOS/` + tabela acima
- **Por dado numérico:** Consultar tabela de dados-chave (seção 7) e localizar no .md

### 8.3 O que verificar nos 8 passes de revisão

1. **Consistência narrativa:** V2 × Matriz de Achados (nível 1 vs nível 3)
2. **Precisão numérica:** Todos os 22 dados-chave conferem entre V2 e peças?
3. **Referências cruzadas:** Toda citação "(peça X, p. Y)" é verificável?
4. **Completude:** Todos os argumentos do gestor (ARG-01 a ARG-30) têm resposta?
5. **Tom e calibragem:** Coerência com Anexo CG (nível 2)?
6. **Conformidade NAT:** Checklist NAT atendido?
7. **Coesão interna:** Seções V2 não se contradizem entre si?
8. **Encaminhamentos:** Determinações e recomendações alinhadas com achados?
