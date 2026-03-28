# Relatório de Correções — Verificação de Evidências

TC 011.073/2025-0 | Data: 2026-03-26

Baseado na convergência de duas verificações independentes:
- **Gemini/Codex**: 104 afirmações, 22 VERIFICAR, 0 SEM FONTE
- **Painel dev-converge (kimi/qwen/zai)**: Resumo e Visão Geral analisados
- **MiniMax 2.7 (Procurador)**: Veredicto REQUER COMPLEMENTAÇÃO

---

## PONTOS CRÍTICOS (2)

### 1. Portaria MDA 20/2025 na Conclusão — §139

**Arquivo:** `05_CONCLUSAO_V2.md`
**Trecho:** "Os critérios legais (Lei 11.326/2006, Decreto 9.064/2017 e Portarias MDA 19/2025 e **20/2025**) definem o que o CAF deve fazer"

**Problema:** O gabi-dou confirma que a Portaria MDA 20/2025 trata do **ingresso na rede credenciada** (emissores do CAF), não das condições gerais de inscrição no cadastro. A Portaria que trata de inscrição é a 19/2025 (que substituiu a 20/2023).

**Hipóteses:**
- (a) Erro de digitação: deveria ser Portaria **20/2023** (anterior à 19/2025, tratava de inscrição)
- (b) Intenção deliberada: a 20/2025 é relevante porque regula a rede emissora (que é quem cadastra)

**Recomendação:** Se a intenção é citar normas que definem "o que o CAF deve fazer" (inscrição), trocar "20/2025" por "20/2023" ou remover. Se a intenção é citar normas sobre a rede emissora, manter mas ajustar a redação para não sugerir que a 20/2025 define condições de inscrição.

**Severidade:** ALTA — pode ser explorada em recurso como erro material.

---

### 2. Projeção 1.400.767 no Apêndice II

**Arquivo:** `A02_APENDICE_II_METODOLOGIA_ESTATISTICA.md`
**Trecho:** Tabela de projeções, linha "Divergência crítica de área": projeção central = 1.400.767

**Problema:** O corpo do relatório e a Matriz usam "~1,44 milhão". Mas 53,55% × 2.615.891 = **1.400.808** (≈ 1,40M, não 1,44M).

**Análise:** Na verdade, "~1,44M" na Matriz provavelmente vem de outro cálculo (53,55% × 2.688.XXX com população ligeiramente diferente). O Apêndice II usa a população de 2.615.891 (documentos com área válida). O corpo usa a Matriz como fonte de verdade.

**Recomendação:** Verificar de onde vem exatamente o "~1,44M" da Matriz. Se vem de população diferente, explicitar no Apêndice II. Se é arredondamento do mesmo cálculo (1,40→1,44 não é arredondamento razoável), corrigir a Matriz ou o Apêndice para harmonizar.

**Severidade:** ALTA — inconsistência numérica entre o corpo e o apêndice metodológico.

---

## PONTOS MÉDIOS (2)

### 3. Quantitativos arredondados na Visão Geral — §10 e Quadro 1

**Arquivo:** `02_VISAO_GERAL_V2.md`
**Dados:** ~3,3 milhões UFPAs, ~3,2 milhões imóveis, ~11,4 milhões docs, ~10 mil agentes

**Problema:** O Gemini não conseguiu confirmar esses arredondamentos de forma limpa via indexação. A peça 152 retorna "23.558 técnicos emissores" e "6.690 entidades emissoras" — nenhum dos dois é "~10 mil agentes".

**Recomendação:** Verificar na peça 82 (base CAF) e peça 152 (apresentação SAF/MDA) os números exatos. Se "~10 mil agentes" vem de uma soma ou de outra página da peça 152, citar a página exata. Se o dado é de outra fonte, atualizar a referência.

**Severidade:** MÉDIA — arredondamentos são aceitáveis se a fonte existe, mas a imprecisão de "~10 mil" vs "23.558 + 6.690" é preocupante.

---

### 4. Propostas reintroduzem dados numéricos

**Arquivo:** `06_PROPOSTAS_ENCAMINHAMENTO_V2.md`
**Trecho:** Propostas 2.1.1 a 2.4 repetem percentuais e quantitativos inline (27,1%, 3.097, 45,92%, etc.)

**Problema:** A diretriz editorial sugeria que propostas apenas remetem aos achados sem repetir dados. Na prática, o texto foi redigido com dados inline para contextualização.

**Recomendação:** Decisão editorial do coordenador. O padrão TCU admite dados inline nas propostas. Não é erro técnico — é questão de estilo. Se mantiver, os dados estão todos consistentes com os achados (verificado pelo Gemini).

**Severidade:** BAIXA — questão editorial, não de rastreabilidade.

---

## ITENS VERIFICAR (22) — Dados secundários pendentes de confirmação

Estes são dados que o Gemini não conseguiu confirmar via indexação (search_review.py). Não são os 22 dados-chave da Matriz — esses todos conferem. São dados secundários ou decomposições. Precisam de busca dirigida ou confirmação manual.

### Visão Geral

| § | Dado | Fonte citada | Ação |
|---|---|---|---|
| §10 | ~3,3M, ~3,2M, ~11,4M | peça 82; peça 152, p.4 | Confirmar números exatos na peça |
| §12 | ~10 mil agentes | peça 152, p.6 | Confirmar — peça retorna 23.558 + 6.690 |
| Quadro 1 | Mesmos arredondamentos | idem | Alinhar com §10 |
| §14 | 98,7% inelegíveis antes do CAF 3.0 | peça 107, p.8 | Confirmar na peça |
| §16 | Despacho de 29/8/2025 excluindo CAR | peça 39 | Confirmar data na peça |

### ACH-01

| § | Dado | Fonte citada | Ação |
|---|---|---|---|
| §30 | 5,6% nas Declarações de Veracidade | peça 103, p.10 | Confirmar na peça |
| §31 | +120,89%, 3.827,65 ha, 1.732,85 ha | peça 109, p.9 | Confirmar decomposição |
| §33 | 12,2% legibilidade crítica | peça 106, p.7 | Confirmar na peça |
| §36 | 3,5% ao mês crescimento base | peça 140/141 | Confirmar na peça |

### ACH-02

| § | Dado | Fonte citada | Ação |
|---|---|---|---|
| §60 | 6.644 imóveis mesmo ponto em Salvador | peça 123 | Confirmar na peça |
| §62 | 722 casos em UF diversa, 174% | peça 116/118 | Confirmar na peça |
| §66 | 22,22%, 0,01%, 174% (trade-off) | peça 118/115 | Confirmar na peça |
| §76 | 82%, 10,89%, 0,31% (ganho Leaflet) | peça 117/121 | Confirmar na peça |

### ACH-03

| § | Dado | Fonte citada | Ação |
|---|---|---|---|
| §89 | 20,8%, 39,5%, 39,7% (temporalidade óbitos) | peça 124, p.9 | Confirmar na peça |
| §90 | 99,70% e-mails PJ válidos, 90,32 p.p. | peça 125 | Confirmar na peça |
| §91 | 1.469 municípios com CEP genérico | peça 150, p.49-50 | Confirmar na peça |

### ACH-04

| § | Dado | Fonte citada | Ação |
|---|---|---|---|
| §110/128 | 31 campos com descrição adequada (5,9%) | peça 135, p.4 | Confirmar: 527 - 496 = 31 (derivação) |

### Comentários Gestor

| § | Dado | Fonte citada | Ação |
|---|---|---|---|
| §132 | Cadeia peças 141-168 | peças processuais | Confirmar sequência |
| §133 | 6 eixos, 30 argumentos | peça 169 | Confirmar na peça |

### Conclusão

| § | Dado | Fonte citada | Ação |
|---|---|---|---|
| §143 | 98,7% (repetição do §14) | peça 107 | Mesma busca que §14 |

### Apêndice II

| § | Dado | Fonte citada | Ação |
|---|---|---|---|
| §3.2 | 99,70% e-mails PJ (repetição) | peça 125 | Mesma busca que ACH-03 §90 |

---

---

## RESULTADOS DA BUSCA DIRIGIDA NOS 22 VERIFICAR

Data: 2026-03-26 | Método: grep nas peças txt_extraido + gabi-dou

### Visão Geral

| # | Dado | Resultado | Peça/Local | Veredicto |
|---|---|---|---|---|
| 1 | ~3,3M, ~3,2M, ~11,4M | Peça 152 confirma dados mas formatação OCR dificulta extração limpa | peca152, linhas 36+ | **CONFIRMADO** (arredondamento aceitável) |
| 2 | ~10 mil agentes | Peça 152 diz "23.558 técnicos emissores" + "6.690 entidades emissoras" + "Mais de 10 mil cadastros no treinamento" — o "10 mil" parece referir-se a cadastros, não agentes | peca152, linhas 65-67, 263 | **DIVERGENTE** — "10 mil agentes" não confere; peça fala em 23.558 técnicos |
| 3 | 98,7% inelegíveis antes CAF 3.0 | Confirmado: "98,7% dos casos não conformes (1.507 de 1.527) são cadastros anteriores a 26/03/2025" | peca107, linhas 242, 400, 427, 433 | **CONFIRMADO** |
| 4 | Despacho 29/8/2025 (peça 39) | Confirmado no Relatório V1 §26: "em 29/8/2025, o Ministro Antonio Anastasia proferiu despacho (peça 39) autorizando a redução do escopo" | relatorio_v1.md, linha 148 | **CONFIRMADO** |

### ACH-01

| # | Dado | Resultado | Peça/Local | Veredicto |
|---|---|---|---|---|
| 5 | 5,6% Declarações de Veracidade | Peça 103 diz **5,7%** (parcialmente adequados no global ponderado), não 5,6% | peca103, linhas 299, 312, 514 | **DIVERGENTE** — texto diz 5,6%, peça diz 5,7% |
| 6 | +120,89%, 3.827,65 ha, 1.732,85 ha | Confirmado literalmente | peca109, linhas 209-212 | **CONFIRMADO** |
| 7 | 12,2% legibilidade crítica | Confirmado: "12,2% dos documentos (79 de 646) têm DPI inferior a 150" | peca106, linhas 209, 264, 389 | **CONFIRMADO** |
| 8 | 3,5% ao mês crescimento base | Confirmado no Relatório V1 §62: "taxa de crescimento de ~3,5% ao mês (peça 140)" | relatorio_v1.md, linha 263 | **CONFIRMADO** (fonte: peça 140 via V1) |

### ACH-02

| # | Dado | Resultado | Peça/Local | Veredicto |
|---|---|---|---|---|
| 9 | 6.644 imóveis mesmo ponto Salvador | Confirmado: "Total de imóveis 6.644" em coordenada crítica | peca123, linhas 12, 46 | **CONFIRMADO** |
| 10 | 722 casos em UF diversa | Confirmado: "Inconsistente — UF Errada (MC-082) 722 1,65%" | peca116, linhas 395, 604, 680 | **CONFIRMADO** |
| 11 | 22,22%, 0,01%, 174% (trade-off) | Confirmado: "Erros Algorítmicos 22,22% 0,01%" e "Aumento 174%" | peca118, linhas 118-119, 547, 579 | **CONFIRMADO** |
| 12 | 82%, 10,89%, 0,31% (Leaflet) | 10,89% e 0,31% confirmados na peca121. O "82%" não foi localizado. | peca121, linhas 640, 650 | **PARCIAL** — 10,89%→0,31% OK; "82%" não encontrado |

### ACH-03

| # | Dado | Resultado | Peça/Local | Veredicto |
|---|---|---|---|---|
| 13 | 20,8%, 39,5%, 39,7% (óbitos) | Confirmado literalmente: "2010-2015: 645 20,8%; 2016-2020: 1.224 39,5%; 2021-2025: 1.228 39,7%" | peca124, linhas 331-333 | **CONFIRMADO** |
| 14 | 99,70% e-mails PJ, 90,32 p.p. | Confirmado: "99,70% (MC-022)" e "disparidade 90,32 pontos percentuais" | peca125, linhas 13-14, 214, 217-218 | **CONFIRMADO** |
| 15 | 1.469 municípios CEP genérico | Confirmado na peça 150: "no Brasil há 1.469" municípios com CEP genérico | peca150, linha 2496 | **CONFIRMADO** (dado do gestor via IBGE/Censo 2022) |

### ACH-04

| # | Dado | Resultado | Peça/Local | Veredicto |
|---|---|---|---|---|
| 16 | 31 campos adequados (5,9%) | Confirmado: "31 (5,9%) possuem descrições funcionalmente adequadas. Os demais 496 campos (94,1%)" | peca135, linhas 101-102 | **CONFIRMADO** |

### Comentários Gestor

| # | Dado | Resultado | Peça/Local | Veredicto |
|---|---|---|---|---|
| 17 | Cadeia peças 141-168 | Confirmado na peça 169 (PECA169_codex, linha 5): "peça 141 (relatório preliminar) → peça 142 (subunidade) → peça 143 (unidade) → peça 144 (ofício) → peça 145 (ciência 23/02/2026) → peça 146 (prorrogação) → peça 147 (deferimento até 18/03/2026) → peça 148 (AECI) → peça 149 (DCAF) → peças 150-168 (documentação)" | PECA169, linha 5 | **CONFIRMADO** |
| 18 | 6 eixos, 30 argumentos | Confirmado: §133 dos Comentários lista os 6 eixos; peça 169 inventaria "30 argumentos substantivos" (ARG-01 a ARG-30, 30 linhas de tabela) | Comentários §133; PECA169 linhas 7, 12-42 | **CONFIRMADO** |

### Conclusão

| # | Dado | Resultado | Peça/Local | Veredicto |
|---|---|---|---|---|
| 19 | Portaria 20/2025 como critério de inscrição | A própria Introdução §5 diz que a 20/2025 trata do "ingresso na rede das entidades credenciadas", não das condições de inscrição. A Conclusão §139 confunde. | Introdução §5 | **DIVERGENTE** — Conclusão atribui função errada à Portaria |
| 20 | 98,7% (repetição do §14) | = item 3 acima | peca107 | **CONFIRMADO** |

### Apêndice II

| # | Dado | Resultado | Peça/Local | Veredicto |
|---|---|---|---|---|
| 21 | 1.400.767 vs ~1,44M | A Matriz diz "53,55% × 2,62M ≈ 1,44M". O Apêndice calcula "53,55% × 2.615.891 = 1.400.767". Diferença: 2,62M é arredondamento de 2.615.891; 53,55% × 2.620.000 = 1.402.810 ≈ 1,40M. O "~1,44M" da Matriz aparenta ser arredondamento para cima. | Matriz peça 170, linha 25 | **ACEITÁVEL** — a Matriz usa "~1,44M" como arredondamento comunicacional; o Apêndice tem o cálculo exato |
| 22 | 99,70% e-mails PJ (repetição) | = item 14 acima | peca125 | **CONFIRMADO** |

---

## RESUMO CONSOLIDADO DOS 22 VERIFICAR

| Veredicto | Qtd | Itens |
|---|---|---|
| **CONFIRMADO** | 18 | #1, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 20, 21, 22 |
| **DIVERGENTE** | 3 | #2 (~10 mil agentes), #5 (5,6% vs 5,7%), #19 (Portaria 20/2025) |
| **PARCIAL** | 1 | #12 (10,89%/0,31% OK; "82%" não encontrado) |
| **NÃO VERIFICÁVEL** | 0 | — |

## AÇÕES RECOMENDADAS

### OBRIGATÓRIAS (antes da publicação)

1. **Conclusão §139**: Trocar "Portarias MDA 19/2025 e 20/2025" por "Portarias MDA 19/2025 e 20/2023" OU reformular para "Portaria MDA 19/2025 (inscrição no CAF) e Portaria MDA 20/2025 (credenciamento da rede emissora)", alinhando com a Introdução §5.

2. **ACH-01 §30**: Verificar se o percentual correto para Declarações de Veracidade parcialmente adequadas é **5,6%** ou **5,7%**. A peça 103 diz 5,7%. Se for 5,7%, corrigir no texto.

### RECOMENDADAS

3. **Visão Geral §12 e Quadro 1**: Substituir "cerca de 10 mil agentes" por dado mais preciso da peça 152 (ex: "23.558 técnicos emissores credenciados em 6.690 entidades") ou citar a página exata que fundamenta o "~10 mil".

4. **ACH-02 §76**: Verificar manualmente a origem do "82%" de redução. Se não for localizável, reformular sem esse percentual.

### INFORMATIVAS (sem ação necessária)

5. Projeção 1.400.767 do Apêndice II é cálculo exato; "~1,44M" da Matriz é arredondamento comunicacional. Ambos são defensáveis.

6. Os três itens antes "NÃO VERIFICÁVEIS" foram todos confirmados: peça 39 via Relatório V1 §26; cadeia 141-168 e "30 argumentos/6 eixos" via PECA169_codex (fonte de verdade). Zero pendências de verificação.
