# Verificação Integral de Evidências — Relatório CAF (TC 011.073/2025-0)

## Escopo e método aplicado

Esta verificação foi executada com as restrições definidas no prompt de controle de qualidade:

- peças processuais e documentos-fonte grandes foram verificados apenas por indexação (`search_review.py`);
- acórdãos e portarias foram verificados no MCP `gabi-dou`;
- arquivos do relatório foram lidos diretamente por serem curtos e estruturados;
- a unidade de contagem adotada foi a **afirmação factual agrupada por parágrafo ou bloco inseparável**, para evitar duplicação artificial de números repetidos na mesma sentença.

Classes usadas:

- `RASTREADA`: a afirmação tem fonte explícita e o dado principal foi localizado no índice;
- `IMPLÍCITA`: a afirmação aparece sem citação local, mas está rastreada em outro trecho do relatório;
- `DERIVADA`: a afirmação resulta de cálculo ou consolidação a partir de dados rastreados;
- `SEM FONTE`: não localizada por indexação nem por remissão interna;
- `VERIFICAR`: a referência existe, mas o dado exato não foi confirmado no índice, ou houve indício de divergência.

## Bloco 1 — Corpo do relatório

## Arquivo: 00_RESUMO_EXECUTIVO_V2.md

Total de afirmações: 8
- RASTREADA: 0
- IMPLÍCITA: 8
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 0

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| capa | `R$ 59,6 bilhões` na safra 2023/2024 | sem citação local | IMPLÍCITA | Rastreada em [02_VISAO_GERAL_V2.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/02_VISAO_GERAL_V2.md) e notas 1/12 |
| 1 | escopo da auditoria, `TC 011.073/2025-0`, período `março a agosto de 2025` | sem citação local | IMPLÍCITA | Detalhado em [02_VISAO_GERAL_V2.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/02_VISAO_GERAL_V2.md) e [A01_APENDICE_I_METODO.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/A01_APENDICE_I_METODO.md) |
| 1 | pendência do `Acórdão 1197/2018` após três verificações | sem citação local | IMPLÍCITA | Rastreado em [02_VISAO_GERAL_V2.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/02_VISAO_GERAL_V2.md) e [A03_APENDICE_III_TRABALHOS_ANTERIORES.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/A03_APENDICE_III_TRABALHOS_ANTERIORES.md) |
| 2 | `27,1%` e `53,55%` no eixo documental | sem citação local | IMPLÍCITA | Subconjunto fiel do ACH-01 |
| 2 | `45,92%`, `55,27%` e `632 municípios` no eixo geoespacial | sem citação local | IMPLÍCITA | Subconjunto fiel do ACH-02 |
| 2 | `3.097`, `138`, `90,62%`, `93,7%`, `39`, `907` no eixo cadastral | sem citação local | IMPLÍCITA | Subconjunto fiel do ACH-03 |
| 2 | `94,1%`, `84%`, `92%` no eixo de metadados | sem citação local | IMPLÍCITA | Subconjunto fiel do ACH-04 |
| 3 | plano em `180 dias`, formação `2025-2027` e renovação de `~742 mil` registros em `2026` | sem citação local | IMPLÍCITA | Rastreado nos achados e nos comentários do gestor |

### Afirmações SEM FONTE

Nenhuma.

### Afirmações IMPLÍCITAS

As oito afirmações do resumo dependem do corpo do relatório e não introduzem dado autônomo novo.

## Arquivo: 02_VISAO_GERAL_V2.md

Total de afirmações: 11
- RASTREADA: 7
- IMPLÍCITA: 0
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 4

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 9 | `77%` dos estabelecimentos, `67%` da mão de obra, `10,1 milhões` de pessoas e `R$ 59,6 bilhões` no Pronaf 2023/2024 | notas 11 e 12 | RASTREADA | Conferência por notas de fim; compatível com o texto |
| 9 | transição DAP -> CAF; entrada em operação em `31/12/2021`; coexistência até `outubro/2022` | nota 14 | RASTREADA | Datas rastreadas pela própria nota |
| 10 | Portaria MDA `19/2025` e quantitativos de `~3,3 milhões`, `~3,2 milhões` e `~11,4 milhões` | peça 82; peça 152, p. 4 | VERIFICAR | Os quantitativos arredondados não foram confirmados de forma limpa no índice; surgiram números concorrentes em peças 152/153 |
| 12 | `cerca de 10 mil agentes` na Rede CAF | peça 152, p. 6 | VERIFICAR | O índice retornou `23.558 técnicos emissores` e `6.690 entidades emissoras`, não `~10 mil agentes` |
| 13 | `109 tabelas` e integração com RFB/Dataprev/ConectaGOV | peça 134, p. 4; peça 78, p. 7 | RASTREADA | `109 tabelas` confirmado; integração descrita nas regras de negócio |
| Quadro 1 | quadro “CAF em números” com `~3,3 milhões`, `~3,2 milhões`, `~11,4 milhões`, `109`, `~10 mil` e `9` tipos de público | peça 82; peça 152; peça 134 | VERIFICAR | O item replica os quantitativos arredondados já não confirmados no índice |
| 14 | `98,7%` das propriedades acima de 4 módulos fiscais anteriores ao CAF 3.0 e redução `92,36% -> 16,59%` nas duplicações em novos cadastros | peça 107, p. 8; peça 117, p. 15 | VERIFICAR | A redução `92,36% -> 16,59%` foi confirmada; o `98,7%` não foi localizado de forma limpa por indexação |
| 15 | `27,1%`, `53,55%`, `45,92%`, `3.097`, `94,1%` | peça 103; peça 109; peça 119; peça 124; peça 135 | RASTREADA | Todos os números-chave conferem com a matriz |
| 16 | origem da fiscalização em `28/5/2025`, autorização em `9/6/2025`, portaria `343/2025`, exclusão do CAR em `29/8/2025` | peça 4; peça 3; peça 39 | VERIFICAR | `3019/2025` e `343/2025-AudTI` foram localizados; o despacho de `29/8/2025` não foi confirmado no índice |
| 17 | Ac. `390/2024` e Ac. `1197/2018`, com `1.335.852` DAPs irregulares e três verificações subsequentes | notas 17 e 18 | RASTREADA | Conferido no `gabi-dou` e na nota 18 |
| 18 | Acs. `646/2017`, `1708/2017`, `2279/2021` e `457/2026` | nota 19 e nota 20 | RASTREADA | Todos conferidos no `gabi-dou` |

### Afirmações SEM FONTE

Nenhuma.

### Afirmações VERIFICAR

| § | Afirmação | Sugestão |
|---|---|---|
| 10 | `~3,3 milhões`, `~3,2 milhões`, `~11,4 milhões` | substituir por número exato e peça/página confirmada |
| 12 | `cerca de 10 mil agentes` | revisar contra a peça 152, que no índice aponta quantitativos diferentes |
| Quadro 1 | quadro replica quantitativos arredondados não confirmados | alinhar com número exato já adotado no corpo |
| 16 | exclusão do CAR em `29/8/2025` | confirmar por busca dirigida da peça 39 ou checagem manual |

## Arquivo: 03_01_ACH01_V2_REESTRUTURADO.md

Total de afirmações: 12
- RASTREADA: 7
- IMPLÍCITA: 1
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 4

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 23 | insuficiência dos mecanismos documentais frente ao art. 3º da Lei 11.326/2006 e à Portaria `19/2025` | Lei 11.326/2006; Portaria 19/2025 | RASTREADA | Critério normativo consistente |
| 24 | `27,1%`, `33,33%`, `53,55%`, `68,7%` | peça 103; peça 105; peça 109; peça 106 | RASTREADA | Todos conferem com os números-chave ou com peça específica |
| 28 | amostra de `646` documentos; `27,1%`; `37,0%` em imóvel rural; `30,5%` em renda | peça 103, p. 9-11 | RASTREADA | `646` e `27,1%` confirmados; percentuais setoriais aderem à peça 103 |
| 29 | população documental de `11.377.318` e projeção de `~3,08 milhões` | peça 140, p. 5 | RASTREADA | Compatível com a atualização da peça 140 |
| 30 | inadequação de apenas `5,6%` nas Declarações de Veracidade | peça 103, p. 10 | VERIFICAR | Não confirmado de forma limpa no índice |
| 30 | `33,33%` de tipo documental inadequado | peça 105, p. 7 | RASTREADA | Confirmado |
| 31 | `53,55%` e divergência agregada de `+120,89%` (`3.827,65 ha` x `1.732,85 ha`) | peça 109, p. 7 e 9 | VERIFICAR | O `53,55%` confere; a decomposição `120,89%`/hectares não foi confirmada por indexação |
| 33 | `68,7%` abaixo de `300 DPI` e `12,2%` em condição crítica | peça 106, p. 7 | VERIFICAR | `68,7%` confirmado; `12,2%` não localizado no índice |
| 36 | crescimento de `3,5% ao mês` da base documental | peça 140; peça 141, §62 | VERIFICAR | Não confirmado no índice |
| 37 | monitoramento do gestor com `32%` de conformidade integral | peça 150, p. 22 | RASTREADA | Dado explicitamente localizado |
| 45 | TED DCAF/UFES `2025-2027` e renovação de `~742 mil` registros em `2026` | peça 150, p. 27 e 29 | RASTREADA | `742 mil` confirmado; TED está coerente com a peça 150 |
| 46-47 | base com `~3,3 milhões`, `~3,2 milhões`, `~11,4 milhões`; avanço de `98,7%` antes do CAF 3.0 | peça 107; peça 152 | IMPLÍCITA | Os quantitativos reaproveitam a Visão Geral; `98,7%` segue pendente de confirmação exata |

### Afirmações SEM FONTE

Nenhuma.

### Afirmações VERIFICAR

| § | Afirmação | Sugestão |
|---|---|---|
| 30 | `5,6%` nas Declarações de Veracidade | confirmar na peça 103 e citar página exata já usada no índice de trabalho |
| 31 | `+120,89%`, `3.827,65 ha`, `1.732,85 ha` | confirmar diretamente por busca dirigida na peça 109 |
| 33 | `12,2%` de legibilidade crítica | confirmar ou retirar, mantendo o `68,7%` já rastreado |
| 36 | `3,5% ao mês` | confirmar na peça 141 ou reescrever sem o percentual |

## Arquivo: 03_02_ACH02_V2_REESTRUTURADO.md

Total de afirmações: 9
- RASTREADA: 5
- IMPLÍCITA: 0
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 4

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 53 | `45,92%`, `55,27%`, `15,92%`, `632 municípios` | peça 119; peça 117; peça 116; peça 121 | RASTREADA | Núcleo quantitativo do achado conferido |
| 57 | população de `3.175.345` imóveis, amostra de `63.588`, erro `45,92%` e `~1,46 milhão` | peça 110; peça 119 | RASTREADA | População e taxa confirmadas |
| 60 | `43.812` registros de alta precisão, `55,27%` de duplicações e `6.644` imóveis em um ponto em Salvador | peça 117; peça 123 | VERIFICAR | `55,27%` confirmado; `6.644` não foi checado por busca específica |
| 61 | redução `92,36% -> 16,59%` | peça 117, p. 15 | RASTREADA | Confirmado no índice |
| 62 | `15,92%` fora do município; `722` casos em UF diversa; aumento de `174%` | peça 116; peça 118 | VERIFICAR | `15,92%` confirmado; `722` e `174%` não foram confirmados no índice |
| 63-64 | `632` municípios; caso extremo `2.248 vezes`; reanálise de `608`, `558`, `50`, `10` e `40` | peça 121; peça 161 | RASTREADA | Confirmado no índice |
| 66 | trade-off Leaflet: `22,22% -> 0,01%`, `+174%`, `-14,33 p.p.` | peça 118; peça 115 | VERIFICAR | `14,33 p.p.` confirmado; demais percentuais exigem checagem adicional |
| 76 | redução de `82%`; inflação cadastral em novos registros de `10,89% -> 0,31%` | peça 117; peça 121 | VERIFICAR | Ganho qualitativo plausível, mas percentuais não confirmados integralmente por indexação |
| 81 | benefícios esperados retomam `45,92%`, `55,27%`, `15,92%` | sem citação local | RASTREADA | Recapitula dados já rastreados no próprio achado |

### Afirmações SEM FONTE

Nenhuma.

### Afirmações VERIFICAR

| § | Afirmação | Sugestão |
|---|---|---|
| 60 | `6.644` imóveis no mesmo ponto em Salvador | confirmar na peça 123 |
| 62 | `722` casos em UF diversa e `174%` | confirmar ou simplificar o texto para o dado já rastreado (`15,92%`) |
| 66 | `22,22%`, `0,01%`, `174%` | confirmar na peça 118 antes da publicação |
| 76 | `82%`, `10,89%`, `0,31%` | confirmar na peça 121 ou reescrever qualitativamente |

## Arquivo: 03_03_ACH03_V2_REESTRUTURADO.md

Total de afirmações: 9
- RASTREADA: 4
- IMPLÍCITA: 2
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 3

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 83 | `3.097`, `138`, `90,62%`, `93,7%`, `907`, `39` | peças 124, 125, 127, 130 | RASTREADA | Todos conferem com os números-chave |
| 84 | `R$ 59,6 bilhões` no Pronaf 2023/2024 | sem citação local | IMPLÍCITA | Já rastreado na Visão Geral |
| 87 | `2.905.101` responsáveis, `15.811` inconsistências, `3.097`, `89`, `49`, `11.999`, `520`, `57` | peça 124 | RASTREADA | Os principais quantitativos foram confirmados por indexação |
| 89 | distribuição temporal dos óbitos: `20,8%`, `39,5%`, `39,7%` | peça 124, p. 9 | VERIFICAR | Não confirmado no índice |
| 90 | `6.525.658` e-mails PF; `9,38%` utilizáveis; `4.904.403` (`75,16%`) no padrão `naopossui`; `99,70%` de e-mails PJ válidos; diferença de `90,32 p.p.`; `93,7%` de CEPs genéricos | peça 125 | VERIFICAR | `90,62%`, `4.904.403`, `75,16%` e `93,7%` foram confirmados; `99,70%` e `90,32 p.p.` não |
| 91 | `1.469` municípios com apenas um CEP genérico | peça 150, p. 49-50 | VERIFICAR | Não confirmado de forma limpa no índice |
| 92 | `3.304.174` UFPAs; `907` acima de R$ 1 milhão; `141` acima de R$ 10 milhões | peça 130; peça 126 | RASTREADA | Confirmado no índice |
| 94 | `39` PJs incompatíveis, `9.687` registros, `10.377` agricultores vinculados e caso extremo de `1.847` agricultores | peça 127, p. 5-6 | RASTREADA | Confirmado no índice |
| 100 | formação de `mais de 10 mil agentes` da RedeCAF para 2026 | peça 150, p. 48 | IMPLÍCITA | Compatível com a narrativa do gestor, mas o quantitativo “10 mil” segue sensível na peça 152 |

### Afirmações SEM FONTE

Nenhuma.

### Afirmações VERIFICAR

| § | Afirmação | Sugestão |
|---|---|---|
| 89 | `20,8%`, `39,5%`, `39,7%` | confirmar na peça 124 ou retirar a decomposição temporal |
| 90 | `99,70%` de e-mails PJ válidos e `90,32 p.p.` | confirmar na peça 125 |
| 91 | `1.469 municípios` com apenas um CEP genérico | confirmar na peça 150 |

## Arquivo: 03_04_ACH04_V2_REESTRUTURADO.md

Total de afirmações: 10
- RASTREADA: 7
- IMPLÍCITA: 1
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 2

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 105 | `94,1%`, `84%`, `92%` e cobertura formal de `100%` das `95` tabelas em uso | peças 133-136 | RASTREADA | Núcleo do achado confirmado |
| 107 | `527` campos documentados, esquema de `109` tabelas e `95` em uso | peça 70; peça 134 | RASTREADA | Confirmado |
| 110 | `100%` de cobertura das `95` tabelas e `31` campos adequados (`5,9%`) | peça 134; peça 135 | VERIFICAR | `100%` confirmado; `31` não foi confirmado de forma limpa no índice |
| 111 | `496` descrições inadequadas (`94,1%`) | peça 135, p. 4 | RASTREADA | Confirmado |
| 113-115 | ausência de mapeamento campo->norma; transição da Portaria `20/2023` para `19/2025` | Lei 11.326/2006; Portaria 20/2023; Portaria 19/2025 | RASTREADA | Conferido com `gabi-dou` |
| 116-117 | existência do MER técnico em `109` tabelas, mas ausência de modelo conceitual de negócio | peça 76 | RASTREADA | Consistência interna satisfatória |
| 118 | `105` de `125` campos numéricos sem unidade | peça 136, p. 4-5 | RASTREADA | Confirmado |
| 119 | `80` de `87` campos temporais ambíguos | peça 133, p. 5 | RASTREADA | Confirmado |
| 128 | referência a `31` campos com descrição funcional adequada | peça 135, p. 4 | VERIFICAR | Mesmo problema do §110 |
| 130 | benefícios esperados retomam `94,1%`, `105` e `80` | sem citação local | IMPLÍCITA | Recapitula números já rastreados |

### Afirmações SEM FONTE

Nenhuma.

### Afirmações VERIFICAR

| § | Afirmação | Sugestão |
|---|---|---|
| 110 | `31` campos adequados (`5,9%`) | confirmar por busca dirigida na peça 135 |
| 128 | `31` campos com descrição funcional adequada | alinhar com a confirmação do §110 |

## Arquivo: 04_COMENTARIOS_GESTOR_V2.md

Total de afirmações: 5
- RASTREADA: 2
- IMPLÍCITA: 1
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 2

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 132 | fluxo procedimental do contraditório: peças `141-168`, ciência em `23/2/2026`, prorrogação até `18/3/2026`, relatório técnico de `76 páginas` | peças 141-168 | VERIFICAR | A cadeia é plausível, mas não foi integralmente confirmada no índice |
| 133 | manifestação em `seis eixos` e análise de `trinta argumentos` na peça 169 | peça 169 | VERIFICAR | Não confirmado por indexação específica |
| 134 | acolhimento majoritário; reconhecimento do `TED 2025-2027`, da renovação de `~742 mil` em `2026` e do prazo de `180 dias` | peça 150 | IMPLÍCITA | `742 mil` foi confirmado; o restante é coerente com a redação dos achados |
| 135 | concordância do gestor nas págs. `53`, `69` e `71` da peça 150 | peça 150 | RASTREADA | Compatível com os trechos rastreados |
| 137 | dos `trinta argumentos`, nenhum afastou a substância dos quatro achados | peça 169 | RASTREADA | Consistência interna com a seção de comentários |

### Afirmações SEM FONTE

Nenhuma.

### Afirmações VERIFICAR

| § | Afirmação | Sugestão |
|---|---|---|
| 132 | cadeia procedimental detalhada das peças 141-168 | confirmar por busca dirigida ou revisão manual das peças de tramitação |
| 133 | `seis eixos` e `trinta argumentos` | confirmar na peça 169 |

## Arquivo: 05_CONCLUSAO_V2.md

Total de afirmações: 9
- RASTREADA: 3
- IMPLÍCITA: 3
- DERIVADA: 1
- SEM FONTE: 0
- VERIFICAR: 2

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 138 | escopo, quatro dimensões e período `março a agosto de 2025` | sem citação local | IMPLÍCITA | Recapitula a Visão Geral e o Apêndice I |
| 139 | critérios legais incluem `Lei 11.326/2006`, `Decreto 9.064/2017` e `Portarias MDA 19/2025 e 20/2025` como normas que “definem o que o CAF deve fazer” | sem citação local | VERIFICAR | **DIVERGÊNCIA CRÍTICA**: o `gabi-dou` confirma que a Portaria `20/2025` trata do ingresso na rede credenciada, não das condições gerais de inscrição no CAF |
| 140 | cadeia de reincidência com os Acórdãos `1197/2018`, `1866/2021` e `885/2024` | sem citação local | RASTREADA | Conferido no `gabi-dou` |
| Quadro 13 | médias `0,43`, `0,20`, `0,40`, `0,14` e média geral `0,29` | quadros dos achados | DERIVADA | Cálculo interno coerente com as médias por achado |
| 142 | `100%` de cobertura do dicionário, redução `92,36% -> 16,59%` e uso do BCadastro | sem citação local | IMPLÍCITA | Todos os dados reaparecem em trechos já rastreados |
| 143 | `98,7%` anteriores ao CAF 3.0; `92,36% -> 16,59%`; consultas ao BCadastro; vedação de menores | sem citação local | VERIFICAR | O bloco reaproveita um dado (`98,7%`) ainda não confirmado no índice |
| 145 | iGovSisp 2024 e peça 150 p. 53 como confirmação de governança incipiente; `94,1%`, `84%`, `92%` no dicionário | peça 139; peça 150 | IMPLÍCITA | Os três percentuais conferem; o detalhe do iGovSisp depende da peça 139 |
| 149 | risco potencial sobre política de `R$ 59,6 bilhões`; avanços com `CAF 3.0`, `Leaflet`, `BCadastro`, `TED 2025-2027`, `~742 mil` em `2026` e `mais de 10 mil agentes` | sem citação local | IMPLÍCITA | O bloco recompõe dados já vistos, mas o quantitativo “10 mil agentes” continua sensível |
| 150 | cadeia de deliberações com itens `9.2.6`, `1866/2021` e `885/2024` | sem citação local | RASTREADA | Compatível com o Apêndice III e com o `gabi-dou` |

### Afirmações SEM FONTE

Nenhuma.

### Divergência crítica

| § | Afirmação | Problema |
|---|---|---|
| 139 | `Portarias MDA 19/2025 e 20/2025` definem o que o CAF deve fazer | A Portaria `20/2025` confirmada no `gabi-dou` regula o ingresso na rede credenciada, não as condições gerais de inscrição no CAF |

## Arquivo: 06_PROPOSTAS_ENCAMINHAMENTO_V2.md

Total de afirmações: 7
- RASTREADA: 1
- IMPLÍCITA: 6
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 0

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 153 | determinação de plano de ação em `180 dias`, com base na Resolução-TCU 315/2020, Lei 11.326/2006 e Decreto 9.064/2017 | citação normativa local | RASTREADA | Critério formal suficiente |
| 2.1.1 | `27,1%`, `3.097` e `138` | remissão aos achados | IMPLÍCITA | Dados já rastreados, mas a seção de propostas reintroduz números |
| 2.1.2 | `53,55%`, `45,92%` e `907` | remissão aos achados | IMPLÍCITA | Dados já rastreados |
| 2.1.3 | `55,27%` e cruzamento censitário com Sisobi | remissão aos achados | IMPLÍCITA | Dados já rastreados |
| 2.1.4 | `68,7%` abaixo de 300 DPI | remissão ao ACH-01 | IMPLÍCITA | Dado já rastreado |
| 2.3 | `32%` de conformidade integral do gestor | remissão aos achados | IMPLÍCITA | Dado já rastreado |
| 2.4 e 2.2 | `94,1%`, `84%`, `92%` e degradação recente em transição tecnológica | remissão aos achados | IMPLÍCITA | Dado já rastreado |

### Observação editorial

A seção de propostas contraria a regra editorial adotada no prompt de revisão: ela **contém dados numéricos** em vez de apenas remeter aos achados correspondentes. Não é um problema de fonte, mas é um problema de consistência redacional.

## Bloco 2 — Apêndices

## Arquivo: A01_APENDICE_I_METODO.md

Total de afirmações: 7
- RASTREADA: 6
- IMPLÍCITA: 1
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 0

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 1 | auditoria operacional; período `março a agosto de 2025`; duas questões e quatro dimensões | Introdução; peça 170 | IMPLÍCITA | Compatível com o corpo do relatório |
| tabela fontes | peça 82; peça 124; IBGE `2022`; dicionário com `527` campos; manifestação do gestor em `mar/2026` | tabela local | RASTREADA | Coerente com os achados e apêndices |
| 3.2 | amostra de `646`, confiança `99%`, margem `±4,5 p.p.`, população `11.377.318` | peça 103; peça 140 | RASTREADA | Confirmado |
| 3.3 | `2.905.101` responsáveis; cruzamentos censitários; bases RFB/Sisobi | peça 124 | RASTREADA | Confirmado |
| 3.4 | amostra geoespacial de `63.588`; margem `±0,40 p.p.`; reanálise `558`/`50` | peças 110, 115, 161 | RASTREADA | Confirmado |
| 3.6 | `527` campos, `125` numéricos e `87` temporais | peças 133-136 | RASTREADA | Confirmado |
| 5 | índice de `32%` do gestor tratado como contextual e não auditado | peça 150 | RASTREADA | Confirmado |

### Afirmações SEM FONTE

Nenhuma.

## Arquivo: A02_APENDICE_II_METODOLOGIA_ESTATISTICA.md

Total de afirmações: 9
- RASTREADA: 6
- IMPLÍCITA: 0
- DERIVADA: 2
- SEM FONTE: 0
- VERIFICAR: 1

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 2.1 | população de `11.377.318`, amostra de `646`, `99%`, `±4,5 p.p.` | peça 103; peça 140 | RASTREADA | Confirmado |
| 2.2 | universo `3.392.881`, subamostra `155`, população comparável `2.615.891`, taxa `53,55%`, `95%`, `±6,44 p.p.` | peça 109 | RASTREADA | Confirmado |
| 2.3 | população `3.175.345`, amostra `63.588`, filtro `43.812`, margem `±0,40 p.p.` | peças 110 e 115 | RASTREADA | Confirmado |
| 3.1 | tabela censitária de capacidade civil: `3.097`, `89`, `49`, `11.999`, `520`, `57` | peça 124 | RASTREADA | Confirmado |
| 3.2 | tabela censitária de contato/renda/CNAE: `6.525.658`, `90,62%`, `75,16%`, `99,70%`, `3.540.310`, `93,7%`, `907`, `141`, `39` | peças 125, 126, 127, 130 | VERIFICAR | `99,70%` segue sem confirmação limpa; demais números principais conferem |
| 3.3 | tabela censitária de metadados: `527`, `496`, `125`, `105`, `87`, `80`, `95/95` | peças 133-136 | RASTREADA | Confirmado |
| 4 | projeção `27,1% -> 3.083.253` | peça 140 | DERIVADA | Derivação compatível com a população usada no apêndice |
| 4 | projeção `53,55% -> 1.400.767` | reconstrução do apêndice | DERIVADA | **DIVERGÊNCIA CRÍTICA**: conflita com a matriz e com o corpo, que usam `~1,44 milhão` |
| 5-6 | limitação: `32%` do gestor é apenas contexto; ACH-01 usa IA sem Kappa formal | peça 103; peça 150 | RASTREADA | Consistência metodológica satisfatória |

### Divergência crítica

| § | Afirmação | Problema |
|---|---|---|
| 4 | projeção `1.400.767` para divergência crítica de área | diverge do valor matriz/corpo (`~1,44 milhão`), que é a referência mandatória do relatório |

## Arquivo: A03_APENDICE_III_TRABALHOS_ANTERIORES.md

Total de afirmações: 8
- RASTREADA: 6
- IMPLÍCITA: 0
- DERIVADA: 2
- SEM FONTE: 0
- VERIFICAR: 0

| § | Afirmação | Fonte citada | Classificação | Observação |
|---|---|---|---|---|
| 1 | trajetória superior a duas décadas e organização em cinco blocos | construção do apêndice | DERIVADA | Coerente com a própria estrutura do apêndice |
| 2 | cadeia `1197/2018` -> `1866/2021` -> `885/2024` -> presente auditoria, com `1.335.852` DAPs e sete anos de pendência | Quadro A3.1 | RASTREADA | Conferido no `gabi-dou` |
| Quadro A3.1 | dados dos acórdãos `1197/2018`, `1866/2021`, `885/2024` | tabela local | RASTREADA | Todos conferidos no `gabi-dou` |
| 3 | processos conexos `646/2017`, `1708/2017`, `687/2019` e `R$ 59,6 bilhões` no Pronaf | Quadro A3.2 | RASTREADA | Conferido em `gabi-dou` e nota do Pronaf |
| 4 | GovDados `390/2024` e `457/2026` | Quadro A3.3 | RASTREADA | Conferido no `gabi-dou` |
| 5 | `2279/2021` para GovData/ConectaGOV | Quadro A3.4 | RASTREADA | Conferido no `gabi-dou` |
| 6 | histórico Pronaf: Decisões `498/2002`, `370/2002`, Acórdãos `2280/2008`, `2029/2011`, `2689/2012` | Quadro A3.5 | RASTREADA | Decisões e acórdãos conferidos no `gabi-dou` |
| 7 | síntese de `24 anos` e `14 trabalhos anteriores` | § final do apêndice | DERIVADA | Contagem interna confere: `3 + 3 + 2 + 1 + 5 = 14` |

### Afirmações SEM FONTE

Nenhuma.

## Bloco 3 — Referencial / consistência

## Arquivo: A04_APENDICE_IV_GLOSSARIO.md

Total de afirmações: 0
- RASTREADA: 0
- IMPLÍCITA: 0
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 0

Observação: o glossário contém predominantemente definições conceituais; não há afirmações factuais dependentes de rastreabilidade probatória.

## Arquivo: A05_APENDICE_V_LISTAS.md

Total de afirmações: 0
- RASTREADA: 0
- IMPLÍCITA: 0
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 0

Observação: verificação apenas de consistência interna. A enumeração de quadros e tabelas é compatível com a estrutura efetivamente encontrada no relatório.

## Arquivo: 00_SUMARIO_.md

Total de afirmações: 0
- RASTREADA: 0
- IMPLÍCITA: 0
- DERIVADA: 0
- SEM FONTE: 0
- VERIFICAR: 0

Observação: arquivo vazio.

## Consolidado final

| Arquivo | Total | Rastreada | Implícita | Derivada | Sem Fonte | Verificar |
|---|---:|---:|---:|---:|---:|---:|
| 00_RESUMO_EXECUTIVO_V2.md | 8 | 0 | 8 | 0 | 0 | 0 |
| 02_VISAO_GERAL_V2.md | 11 | 7 | 0 | 0 | 0 | 4 |
| 03_01_ACH01_V2_REESTRUTURADO.md | 12 | 7 | 1 | 0 | 0 | 4 |
| 03_02_ACH02_V2_REESTRUTURADO.md | 9 | 5 | 0 | 0 | 0 | 4 |
| 03_03_ACH03_V2_REESTRUTURADO.md | 9 | 4 | 2 | 0 | 0 | 3 |
| 03_04_ACH04_V2_REESTRUTURADO.md | 10 | 7 | 1 | 0 | 0 | 2 |
| 04_COMENTARIOS_GESTOR_V2.md | 5 | 2 | 1 | 0 | 0 | 2 |
| 05_CONCLUSAO_V2.md | 9 | 3 | 3 | 1 | 0 | 2 |
| 06_PROPOSTAS_ENCAMINHAMENTO_V2.md | 7 | 1 | 6 | 0 | 0 | 0 |
| A01_APENDICE_I_METODO.md | 7 | 6 | 1 | 0 | 0 | 0 |
| A02_APENDICE_II_METODOLOGIA_ESTATISTICA.md | 9 | 6 | 0 | 2 | 0 | 1 |
| A03_APENDICE_III_TRABALHOS_ANTERIORES.md | 8 | 6 | 0 | 2 | 0 | 0 |
| A04_APENDICE_IV_GLOSSARIO.md | 0 | 0 | 0 | 0 | 0 | 0 |
| A05_APENDICE_V_LISTAS.md | 0 | 0 | 0 | 0 | 0 | 0 |
| 00_SUMARIO_.md | 0 | 0 | 0 | 0 | 0 | 0 |
| **TOTAL** | **104** | **54** | **23** | **5** | **0** | **22** |

## BLOQUEANTES (SEM FONTE)

Nenhum caso puro de `SEM FONTE` foi identificado na amostragem agrupada adotada.

## Pontos críticos remanescentes

Mesmo sem casos puros de `SEM FONTE`, permanecem pontos bloqueantes para publicação porque envolvem divergência normativa ou quantitativa:

1. [05_CONCLUSAO_V2.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/05_CONCLUSAO_V2.md): §139 atribui à Portaria MDA `20/2025` função normativa que não confere com a base do `gabi-dou`.
2. [A02_APENDICE_II_METODOLOGIA_ESTATISTICA.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/A02_APENDICE_II_METODOLOGIA_ESTATISTICA.md): tabela de projeções usa `1.400.767` para o ACH-01, divergindo do valor matriz/corpo (`~1,44 milhão`).
3. [02_VISAO_GERAL_V2.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/02_VISAO_GERAL_V2.md): quantitativos arredondados `~3,3 milhões`, `~3,2 milhões`, `~11,4 milhões` e `~10 mil agentes` não ficaram firmemente confirmados no índice e colidem com números concorrentes das peças 152/153.
4. [06_PROPOSTAS_ENCAMINHAMENTO_V2.md](/Users/fgamajr/Desktop/CAF-FINAL/01_RELATORIO_V2/06_PROPOSTAS_ENCAMINHAMENTO_V2.md): a seção reintroduz dados quantitativos, contrariando a diretriz editorial de que propostas deveriam apenas remeter aos achados.

## DIVERGÊNCIAS GABI-DOU

1. `Portaria MDA 20/2025`: confirmada no `gabi-dou` como “ingresso na rede das entidades credenciadas para realizar inscrição no CAF”; o texto da Conclusão a trata como se definisse, ao lado da Portaria `19/2025`, as regras gerais do que o CAF deve fazer.

## Revisão adversarial — MiniMax 2.7

Prompt sugerido para submissão adversarial final:

```text
Você é revisor independente do MP junto ao TCU. Recebeu o relatório
de verificação de evidências abaixo. Sua tarefa:

1. O revisor foi RIGOROSO O SUFICIENTE? Ele deixou passar alguma afirmação
   sem fonte que deveria ter sido flagrada?
2. Há falsos positivos? Alguma afirmação classificada como VERIFICAR ou
   IMPLÍCITA que na verdade já está plenamente rastreada?
3. Os dados conferem com a tabela de 22 dados-chave da Matriz?
4. Algum acórdão ou norma foi verificado incorretamente?

VEREDICTO: APROVADO / REQUER COMPLEMENTAÇÃO / INSUFICIENTE.

RELATÓRIO DE VERIFICAÇÃO:
[colar este arquivo]
```
