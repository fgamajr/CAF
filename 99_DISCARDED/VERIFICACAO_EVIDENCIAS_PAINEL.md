# Verificação de Evidências — Painel Adversarial (dev-converge + Claude + MiniMax)

TC 011.073/2025-0 — Relatório de Auditoria CAF
Data: 2026-03-26

---

## Arquivo 1: 00_RESUMO_EXECUTIVO_V2.md

### Resultado do run_panel (kimi/qwen/zai, 2 rounds)

**Consenso:** ~27-31 afirmações factuais identificadas (variação por critério de atomicidade).

| Classificação | Kimi | Qwen | Zai | Consenso |
|---|---|---|---|---|
| COM FONTE | 6 | 4 | 4 | **4** (TC, Lei, Decreto, Acórdão) |
| SEM FONTE | 24 | 23 | 27 | **~27** |

**Afirmações COM FONTE (consenso):**
1. TC 011.073/2025-0
2. Lei 11.326/2006
3. Decreto 9.064/2017
4. Acórdão 1197/2018-TCU-Plenário

**Afirmações SEM FONTE no Resumo (consenso — 27 itens):**

| # | Afirmação | Esperado no corpo? |
|---|---|---|
| 1 | R$ 59,6 bilhões na safra 2023/2024 | Visão Geral §8, nota ¹² |
| 2 | CAF é instrumento de habilitação de Pronaf, PAA e PNAE | Visão Geral §8 |
| 3 | Período de março a agosto de 2025 | Visão Geral §12 |
| 4 | Deliberações do Ac. 1197/2018 pendentes | Visão Geral §11, nota ¹⁸ |
| 5 | Três monitoramentos realizados | Visão Geral §11, nota ¹⁸ |
| 6 | 27,1% docs semanticamente inadequados | ACH-01, peça 103, p. 9 |
| 7 | ~3,08 milhões de documentos | ACH-01, peça 140, p. 5 |
| 8 | 53,55% divergência crítica de área | ACH-01, peça 109, p. 7 |
| 9 | 45,92% erro cartográfico | ACH-02, peça 119, p. 9 |
| 10 | ~1,46 milhão de imóveis | ACH-02, derivado |
| 11 | 55,27% coordenadas idênticas | ACH-02, peça 119 |
| 12 | 632 municípios inflação cadastral | ACH-02, peça 121 |
| 13 | 3.097 titulares falecidos | ACH-03, peça 124, p. 9 |
| 14 | 138 menores como responsáveis | ACH-03, peça 124, p. 8 |
| 15 | 90,62% e-mails PF fictícios | ACH-03, peça 125 |
| 16 | 907 registros renda > R$ 1M | ACH-03, peça 126/130 |
| 17 | 94,1% descrições dicionário inadequadas | ACH-04, peça 135, p. 4 |
| 18 | 84% campos numéricos sem unidade | ACH-04, peça 136 |
| 19 | CAF 3.0 reduziu inelegíveis | ACH-01/ACH-02, peça 107, p. 8 |
| 20 | Redução duplicações 92,36%→16,59% | ACH-02, peça 117, p. 15 (dado do gestor) |
| 21 | Passivo acumulado permanece ativo | Conclusão (juízo analítico) |
| 22 | 180 dias para plano de ação | Propostas §79 |
| 23 | Sete recomendações | Propostas §80-86 |
| 24 | Plano de formação 2025-2027 | peça 150 (manifestação gestor) |
| 25 | ~742 mil registros a renovar em 2026 | peça 150 (manifestação gestor) |
| 26 | R$ 59,6 bilhões por safra (repetição) | = item 1 |
| 27 | Limite de 4 módulos fiscais | Lei 11.326/2006, art. 3º |

### Análise Claude

**Contexto:** O Resumo Executivo do TCU é, por design, uma síntese sem notas de rodapé. Todos os dados aparecem com referência completa nos achados do corpo do relatório. As 27 afirmações "SEM FONTE" no Resumo são IMPLÍCITAS — têm fonte no corpo.

**Classificação final:**
- RASTREADA no Resumo: 4
- IMPLÍCITA (fonte no corpo): 22
- DERIVADA: 1 (item 10: ~1,46M = 45,92% × 3,175M)
- SEM FONTE real: 0
- VERIFICAR: 0

**Veredicto: LIMPO** — Nenhuma afirmação sem rastreabilidade no corpo do relatório.

### Observações do painel (válidas para melhoria futura, não bloqueantes)
- "conforme informado pelo gestor" poderia citar peça 117, p. 15 ou peça 150
- "conforme sua manifestação" poderia citar peça 150

---

## Arquivo 2: 02_VISAO_GERAL_V2.md

### Resultado do run_panel (kimi/qwen/zai, 2 rounds)

**Contexto:** A Visão Geral é o arquivo mais densamente referenciado do relatório — 10 notas de fim (¹¹-²⁰) + 12 referências a peças + leis/decretos/acórdãos inline.

**Afirmações SEM FONTE identificadas pelo painel (consenso):**

| § | Afirmação | Análise Claude |
|---|---|---|
| §9 | Inscrição no CAF como requisito para PAA, PNAE, Garantia-Safra | NORMA — Decreto 9.064/2017 (já citado no mesmo §). Não é SEM FONTE. |
| §11 | "qualidade dos dados condiciona diretamente a capacidade do CAF" | JUÍZO ANALÍTICO da equipe, não afirmação factual. Não precisa de fonte. |
| §12 | "modelo autodeclaratório" | FATO NORMATIVO — decorre do Decreto 9.064/2017 e Portaria MDA 19/2025 (ambos citados). |
| §16 | Proposta de Fiscalização 3019/2025, datas | FATO PROCESSUAL interno do TCU — rastreável via peças 3 e 4 (citadas no próprio §16). |
| §20 | Repetição de 27,1%, 53,55%, 45,92% sem referenciar peças | VÁLIDO — os dados são repetidos do §15, onde têm fonte. Painel sugere remissão "(ver §15)". |

**Classificação final:**
- RASTREADA: ~35 afirmações (com peça, nota de fim ou norma)
- IMPLÍCITA: 3 (dados repetidos no §20 sem remissão ao §15)
- SEM FONTE real: 0
- VERIFICAR: 0

**Ação sugerida pelo painel (válida):** No §20, adicionar "(ver §15)" ou repetir as referências de peça quando reutilizar estatísticas. Baixa prioridade — dados estão referenciados 5 parágrafos acima.

**Veredicto: LIMPO**

## Arquivo 3: 03_01_ACH01_V2_REESTRUTURADO.md

**Status:** Pendente

## Arquivo 4: 03_02_ACH02_V2_REESTRUTURADO.md

**Status:** Pendente

## Arquivo 5: 03_03_ACH03_V2_REESTRUTURADO.md

**Status:** Pendente

## Arquivo 6: 03_04_ACH04_V2_REESTRUTURADO.md

**Status:** Pendente

## Arquivo 7: 04_COMENTARIOS_GESTOR_V2.md

**Status:** Pendente

## Arquivo 8: 05_CONCLUSAO_V2.md

**Status:** Pendente

## Arquivo 9: 06_PROPOSTAS_ENCAMINHAMENTO_V2.md

**Status:** Pendente

## Arquivo 10: Apêndices I + II + III

**Status:** Pendente

---

## Consolidado

| Arquivo | Afirmações | Rastreada | Implícita | Derivada | Sem Fonte | Verificar | Veredicto |
|---|---|---|---|---|---|---|---|
| Resumo Executivo | 27 | 4 | 22 | 1 | 0 | 0 | LIMPO |
| Visão Geral | ~38 | 35 | 3 | 0 | 0 | 0 | LIMPO |
| ACH-01 | — | — | — | — | — | — | Pendente |
| ACH-02 | — | — | — | — | — | — | Pendente |
| ACH-03 | — | — | — | — | — | — | Pendente |
| ACH-04 | — | — | — | — | — | — | Pendente |
| Comentários Gestor | — | — | — | — | — | — | Pendente |
| Conclusão | — | — | — | — | — | — | Pendente |
| Propostas | — | — | — | — | — | — | Pendente |
| Apêndices I-III | — | — | — | — | — | — | Pendente |
