# Relatório de Análise — Estrutura da Pasta CAF-FINAL

**Data:** 2026-03-24
**Objetivo:** Avaliar a estrutura atual para otimização do trabalho de um agente LLM

---

## 1. Inventário do Conteúdo

### 1.1 Números gerais

| Métrica | Valor |
|---|---:|
| Total de arquivos | 180 |
| PDFs | 108 |
| Arquivos .txt (texto extraído) | 31 |
| Arquivos .md (Markdown) | 19 |
| Arquivos .tex (LaTeX fonte) | 4 |
| Arquivos .docx | 4 |
| Artefatos LaTeX (.aux, .log, .out) | 9 |
| Arquivos .json | 2 |
| Arquivo .doc (formato legado) | 1 |
| Pastas de primeiro nível | 6 |

### 1.2 Estrutura atual de pastas

```
CAF-FINAL/
├── MODELOS_RELATORIO_TCU/     # 2 arquivos — template e exemplo de relatório TCU
├── NORMAS_CRITERIOS/          # 14 arquivos — ISOs, DAMA-DMBOK, NAT, normas
├── PECAS_A_INSERIR/           # 3 arquivos — Matriz de Achados e Anexo CG (V2)
├── PECAS_EXISTENTES/          # 131 arquivos — peças 4 a 168 + inventários + .txt
├── PHASE3_MOUNTING_REPORT/    # 7 arquivos — seções do Relatório V2
└── RELATORIO_ATUAL_PECA_141/  # 3 arquivos — Relatório V1 + codex de upgrades
```

---

## 2. Problemas Identificados

### 2.1 Nomenclatura de arquivos

| # | Problema | Exemplos | Impacto no LLM |
|---|---|---|---|
| N1 | **UUIDs no nome** — 27 PDFs têm UUIDs que não informam conteúdo | `PECA142_417ffa70-e6ca-4e95-87b8-ecbe44ef7598.pdf` | LLM não sabe o que é sem abrir |
| N2 | **Espaços e caracteres especiais** nos nomes | `peca61_ Encaminhamento de Dados de Acesso – Processo SEI n 55000012930_2025-64.pdf` | Dificulta referência em shell |
| N3 | **Acentos nos nomes** | `peca107_papel_trabalho_análise_quatro_modulos.pdf` | Pode causar problemas de encoding |
| N4 | **Inconsistência de case** — PECA vs peca | `PECA142_...pdf` vs `peca103_...pdf` | Dificulta glob/regex |
| N5 | **Sem zero-padding** na numeração | `peca4`, `peca33`, `peca103` | Ordenação lexicográfica errada |
| N6 | **Nomes genéricos** sem descrição funcional | `peca4-comunicacao-fiscalizacao.pdf` | Ambíguo — comunicação de quê? |
| N7 | **Nomes excessivamente longos** | `peca65_email de Encaminhamento de Dados de Acesso – Processo SEI n 55000012930_2025-64.pdf` | Truncamento em terminais |

### 2.2 Duplicatas e redundâncias

| # | Arquivo A | Arquivo B | Situação |
|---|---|---|---|
| D1 | `peca58_OFICIO...MDA_N_130...` | `peca62_OFICIO...MDA_N_130...` | Mesmo ofício, tamanhos quase idênticos (71826 vs 71824 bytes) |
| D2 | `peca59_DESPACHO...N_196...` | `peca63_DESPACHO...N_196...` | Mesmo despacho, tamanho idêntico (69785 bytes) |
| D3 | `peca60_OFICIO_N_59...MAPA` | `peca64_OFICIO_N_59...MAPA` | Mesmo ofício, tamanho idêntico (65896 bytes) |
| D4 | `peca61_Encaminhamento...` | `peca65_email_Encaminhamento...` | Mesmo conteúdo em formatos diferentes |
| D5 | `peca108_PortariaMDAn19.pdf` | `peca108_PortariaMDAn19_original.pdf` | Duas versões da mesma portaria (16.5 MB vs 6.7 MB) |
| D6 | `NORMAS_CRITERIOS/PortariaMDAn19.pdf` | `peca108_PortariaMDAn19.pdf` | Mesmo documento em pastas diferentes |
| D7 | `NORMAS_CRITERIOS/ISO_IEC_25012_2008.pdf` | `peca85_ISO_IEC_25012_2018.pdf` | Mesma norma em pastas diferentes |
| D8 | `NORMAS_CRITERIOS/README.md` | `NORMAS_CRITERIOS/README 2.md` | Dois READMEs (conteúdos completamente diferentes) |

### 2.3 Artefatos desnecessários (lixo de indexação)

| Tipo | Arquivos | Impacto |
|---|---|---|
| `.aux` (LaTeX) | `peca130_*.aux`, `peca131_*.aux`, `peca140_*.aux` | Poluem indexação com metadados LaTeX |
| `.log` (LaTeX) | `peca130_*.log`, `peca131_*.log`, `peca140_*.log` | Logs de compilação sem valor para auditoria |
| `.out` (LaTeX) | `peca130_*.out`, `peca131_*.out`, `peca140_*.out` | Bookmarks de PDF sem valor para auditoria |
| `.DS_Store` | 2 arquivos | Metadados macOS sem valor |
| `.doc` legado | `Resolução TCU n° 315_2020.doc` | Formato antigo, precisa conversão |

### 2.4 Cobertura de texto extraído

| Categoria | PDFs | Com .txt | Sem .txt | Taxa de cobertura |
|---|---:|---:|---:|---:|
| Peças 4-86 (pré-relatório) | 53 | 0 | 53 | **0%** |
| Peças 103-140 (papéis de trabalho) | 28 | 23 | 5 | 82% |
| Peças 142-168 (pós-relatório/CG) | 26 | 0 | 26 | **0%** |
| NORMAS_CRITERIOS/ | 6 | 0 | 6 | **0%** |
| MODELOS_RELATORIO_TCU/ | 1 | 0 | 1 | **0%** |
| **TOTAL** | **114** | **23** | **91** | **20%** |

**Problema crítico:** 80% dos PDFs não têm texto extraído. O agente LLM não conseguirá indexar esses documentos sem extrair o texto primeiro.

### 2.5 Problemas de organização

| # | Problema | Detalhe |
|---|---|---|
| O1 | **Sem hierarquia por função** | Peças de tramitação (ofícios), evidência (PTs) e normas convivem na mesma pasta |
| O2 | **Sem separação por achado** | As 86 peças de evidência não estão organizadas por achado |
| O3 | **Fonte de verdade não destacada** | Matriz de Achados e Anexo CG estão em PECAS_A_INSERIR (nome pouco intuitivo) |
| O4 | **Sem MANIFEST.md** | Não há índice mestre que mapeie tudo |
| O5 | **READMEs inconsistentes** | Só NORMAS_CRITERIOS tem README, mas são 2 com conteúdos distintos |
| O6 | **Nome "PECAS_A_INSERIR" confuso** | Mistura peças a inserir (futuras) com fonte de verdade do projeto |
| O7 | **Nome "PHASE3_MOUNTING_REPORT" técnico demais** | Um agente LLM não sabe o que é "Phase 3" |
| O8 | **Peça 164 ausente** | Documentada como ausente nos inventários, mas sem registro na pasta |

---

## 3. Proposta de Estrutura Otimizada

### 3.1 Nova árvore de pastas

```
CAF-FINAL/
├── MANIFEST.md                    # Índice mestre — o LLM lê isto PRIMEIRO
│
├── 00_CONTEXTO/                   # O que o LLM precisa ler antes de tudo
│   ├── README.md
│   ├── RESUMO_EXECUTIVO_V2.md
│   └── VISAO_GERAL_V2.md
│
├── 01_RELATORIO_V2/               # O documento sendo revisado (seções do V2)
│   ├── README.md
│   ├── INTRODUCAO_V2.md
│   ├── ACH01_V2.md
│   ├── ACH02_V2.md
│   ├── ACH03_V2.md
│   └── ACH04_V2.md
│
├── 02_FONTE_VERDADE/              # Hierarquia máxima — Matriz + Anexo CG
│   ├── README.md
│   ├── PECA170_MATRIZ_DE_ACHADOS_CAF.md
│   ├── PECA170_MATRIZ_DE_ACHADOS_CAF.docx
│   └── PECA169_codex_anexo_comentarios_gestor_v2.md
│
├── 03_RELATORIO_V1/               # Referência histórica
│   ├── README.md
│   ├── relatorio_v1.md
│   ├── relatorio_v1.docx
│   └── CODEX_UPGRADED_V1_FINDINGS.md
│
├── 04_PECAS_EVIDENCIA/            # Peças de evidência organizadas por achado
│   ├── README.md
│   ├── ACH01_documental/          # Peças do Achado 01
│   ├── ACH02_geoespacial/         # Peças do Achado 02
│   ├── ACH03_cadastral/           # Peças do Achado 03
│   ├── ACH04_metadados/           # Peças do Achado 04
│   ├── TRANSVERSAIS/              # Peças que servem a múltiplos achados
│   └── txt_extraido/              # Texto extraído dos PDFs
│
├── 05_PECAS_TRAMITACAO/           # Ofícios, atas, despachos, termos
│   ├── README.md
│   ├── pre_relatorio/             # Peças 4-86 (comunicações iniciais)
│   └── pos_relatorio/             # Peças 142-168 (contraditório)
│
├── 06_NORMAS_CRITERIOS/           # Legislação, ISOs, DAMA-DMBOK, NAT
│   ├── README.md
│   ├── legislacao/                # Leis, decretos, portarias
│   ├── iso_referenciais/          # ISOs e DAMA-DMBOK
│   └── nat_tcu/                   # NAT, checklist, termos oficiais
│
├── 07_MODELOS_TCU/                # Templates e exemplos
│   └── README.md
│
└── _artefatos_latex/              # .aux, .log, .out isolados
```

### 3.2 Justificativa dos princípios

1. **Prefixo numérico** (00_, 01_, ...) — força ordem de leitura natural para o LLM
2. **00_CONTEXTO primeiro** — o agente que "não sabe nada" começa pelo resumo executivo
3. **02_FONTE_VERDADE separada** — Matriz e Anexo CG têm hierarquia superior a tudo
4. **04_PECAS por achado** — busca por achado é a operação mais frequente na revisão
5. **05_PECAS_TRAMITACAO separada** — ofícios e atas raramente são consultados durante revisão de achados
6. **txt_extraido centralizado** — evita poluir pastas de PDFs com .txt
7. **_artefatos_latex** — prefixo `_` = último na listagem, sinaliza "não indexar"

---

## 4. Tabela de Renomeação (amostra representativa)

| Arquivo atual | Nome novo | Justificativa |
|---|---|---|
| `PECA142_417ffa70-...pdf` | `peca142_pronunciamento_subunidade_audti.pdf` | UUID → descrição funcional |
| `PECA143_f0db14d5-...pdf` | `peca143_pronunciamento_unidade_audti.pdf` | UUID → descrição funcional |
| `PECA144_2112260a-...pdf` | `peca144_oficio_4045_seproc_diligencia.pdf` | UUID → descrição funcional |
| `PECA145_a1e6d198-...pdf` | `peca145_termo_ciencia_conecta_tcu.pdf` | UUID → descrição funcional |
| `PECA146_a4725580-...pdf` | `peca146_oficio_28_aeci_prorrogacao.pdf` | UUID → descrição funcional |
| `PECA147_5ba9b46c-...pdf` | `peca147_despacho_prorrogacao_prazo.pdf` | UUID → descrição funcional |
| `PECA148_5222b52c-...pdf` | `peca148_oficio_aeci_encaminhamento.pdf` | UUID → descrição funcional |
| `PECA149_1577c261-...pdf` | `peca149_oficio_dcaf_manifestacao.pdf` | UUID → descrição funcional |
| `PECA150_5b1299d3-...pdf` | `peca150_relatorio_tecnico_dcaf_76p.pdf` | UUID → descrição funcional |
| `PECA151_467145c7-...pdf` | `peca151_oficio_aeci_acordao_885.pdf` | UUID → descrição funcional |
| `PECA152_e5bbcc39-...pdf` | `peca152_caf_em_numeros_32p.pdf` | UUID → descrição funcional |
| `PECA153_c8039635-...pdf` | `peca153_organograma_dcaf_20p.pdf` | UUID → descrição funcional |
| `PECA154_06fe444a-...pdf` | `peca154_nota_tecnica_cgti_tic.pdf` | UUID → descrição funcional |
| `PECA155_5206d838-...pdf` | `peca155_etp_contratacao_tic_81p.pdf` | UUID → descrição funcional |
| `PECA156_3e723048-...pdf` | `peca156_relatorio_monitoramento_caf.pdf` | UUID → descrição funcional |
| `PECA157_64b09371-...pdf` | `peca157_nota_tecnica_ted_ufes.pdf` | UUID → descrição funcional |
| `PECA158_5e826027-...pdf` | `peca158_plano_trabalho_ted_ufes.pdf` | UUID → descrição funcional |
| `PECA159_ef2d8c1d-...pdf` | `peca159_contrato_dataprev.pdf` | UUID → descrição funcional |
| `PECA160_b1ec4ff1-...pdf` | `peca160_oficio_spoa_incidentes_tic.pdf` | UUID → descrição funcional |
| `PECA161_dcb721d5-...pdf` | `peca161_memoria_tecnica_doc121.pdf` | UUID → descrição funcional |
| `PECA162_05f48235-...pdf` | `peca162_apresentacao_caf_governanca.pdf` | UUID → descrição funcional |
| `PECA163_c43e9fb1-...pdf` | `peca163_anexo_tecnico_achado01.pdf` | UUID → descrição funcional |
| `PECA165_8c85f34f-...pdf` | `peca165_nota_tecnica_cafweb_intermitencia.pdf` | UUID → descrição funcional |
| `PECA166_2d24187f-...pdf` | `peca166_memoria_tecnica_doc105.pdf` | UUID → descrição funcional |
| `PECA167_434aa822-...pdf` | `peca167_termo_recebimento_area_validation.pdf` | UUID → descrição funcional |
| `PECA168_241b881b-...pdf` | `peca168_termo_recebimento_inflacao_municipal.pdf` | UUID → descrição funcional |
| `peca004-comunicacao-fiscalizacao.pdf` | `peca004_oficio_0132_audti_comunicacao.pdf` | Zero-padding + descrição |
| `peca033_30ef9bec-...pdf` | `peca033_oficio_sei_98265_mgi.pdf` | UUID → descrição funcional |
| `peca046_Ofício 0001492025...` | `peca046_oficio_000149_audti.pdf` | Espaços removidos, padronizado |
| `peca061_ Encaminhamento...` | `peca061_encaminhamento_dados_acesso_sei.pdf` | Espaços e caracteres especiais removidos |
| `peca078_regras_negocio_caf_33ead8fe-...pdf` | `peca078_regras_negocio_caf.pdf` | UUID removido |
| `peca103_adequacao_funcional_b89deb70-...pdf` | `peca103_adequacao_funcional_docs.pdf` | UUID removido |
| `peca139_PFIS AudQualidadeDados...pdf` | `peca139_pfis_qualidade_dados_rurais.pdf` | Espaços e parênteses removidos |

---

## 5. Mapeamento Peça → Achado

### ACH-01 — Documentação comprobatória
Peças: 103, 104, 105, 106, 107, 109, 140

### ACH-02 — Integridade geoespacial
Peças: 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122

### ACH-03 — Qualidade dos dados cadastrais
Peças: 123, 124, 125, 126, 127, 128, 129, 130, 131, 132

### ACH-04 — Gestão de metadados
Peças: 133, 134, 135, 136

### Transversais (múltiplos achados)
Peças: 75 (dicionário dados), 76 (MER), 77 (especificações), 78 (regras negócio), 108 (Portaria 19)

### Normas e legislação (peças-norma)
Peças: 79, 80, 81, 82, 83, 84, 85, 86, 137, 138, 139

### Tramitação pré-relatório
Peças: 4, 33, 46, 49, 51, 56, 58, 59, 60, 61, 62, 63, 64, 65, 66, 68, 69, 70, 71, 72, 73, 74

### Tramitação pós-relatório (contraditório)
Peças: 142-168 (exceto 164 ausente)
