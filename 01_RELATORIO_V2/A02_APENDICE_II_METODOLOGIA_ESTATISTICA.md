# APÊNDICE II — METODOLOGIA ESTATÍSTICA

## 1. Visão geral da abordagem estatística

Este apêndice documenta os desenhos amostrais, parâmetros de confiança, projeções populacionais e critérios de validação quantitativa empregados na auditoria do Sistema CAF. Em coerência com o Apêndice I, a estratégia estatística combinou duas abordagens: `i)` amostragem probabilística, quando a análise integral era desproporcional ao custo analítico; e `ii)` análise censitária, quando a população estava disponível integralmente em formato estruturado.

No eixo documental (ACH-01), a inferência foi feita sobre amostra probabilística estratificada de documentos comprobatórios. No eixo geoespacial (ACH-02), a auditoria partiu de amostra probabilística consolidada de 63.588 registros, depois depurada por filtros de validade algorítmica e precisão decimal. Já os achados cadastral (ACH-03) e de metadados (ACH-04) foram produzidos por análise censitária. Sempre que houve inferência para a população, o texto indica a proporção observada, o tamanho da amostra, o nível de confiança adotado e o intervalo correspondente.

## 2. Desenhos amostrais

### 2.1 Amostra documental (ACH-01)

O objetivo do desenho amostral documental foi estimar a taxa de inadequação funcional dos documentos comprobatórios anexados ao CAF. A população de referência corrigida era de 11.377.318 documentos, conforme atualização formalizada na peça 140. A peça 103 estruturou a amostra como amostragem probabilística estratificada por tipo documental, com alocação proporcional ao tamanho de cada estrato e seleção aleatória simples intrassestrato. A unidade amostral foi o documento individual.

| Parâmetro | Valor |
|---|---|
| População de referência | 11.377.318 documentos |
| Tamanho da amostra | 646 documentos |
| Nível de confiança | 99% |
| Margem de erro | ±4,5 p.p. |
| Estratos | 3 |
| Critério de estratificação | Tipo documental |
| Alocação | Proporcional ao tamanho do estrato |
| Seleção | Aleatória simples dentro de cada estrato |
| Unidade amostral | Documento individual |

| Estrato | População na peça 103 | Amostra | % da amostra |
|---|---:|---:|---:|
| Imóvel rural | 3.310.901 | 227 | 35,1% |
| Renda | 4.532.073 | 276 | 42,7% |
| Declarações de veracidade | 2.857.182 | 143 | 22,1% |
| **Total** | **10.700.156** | **646** | **100,0%** |

As contagens populacionais por estrato decorrem da peça 103 e refletem a base preliminar então disponível. A peça 140 atualizou apenas o denominador global da projeção, de 10.700.156 para 11.377.318 documentos, sem redistribuir formalmente os documentos adicionais entre os três estratos. Por isso, a projeção oficial atualizada foi refeita pela taxa amostral global `175/646 = 27,09%`, e não por nova ponderação estrato a estrato. A inferência incidiu sobre a proporção final consolidada de documentos `inadequados + parcialmente adequados`, tratada como taxa de não conformidade funcional.

### 2.2 Subamostra de divergência de área (ACH-01)

A análise de divergência de área não replicou o desenho da amostra geral de 646 documentos. Trata-se de recorte autônomo, derivado de amostra aleatória simples de 201 documentos de imóvel extraídos do universo de 3.392.881 documentos dessa categoria. Desse conjunto, apenas 155 permitiram comparação entre área documental e área cadastral, por apresentarem área legível e comparável nos dois lados. O objetivo foi estimar a taxa de divergência crítica de área, definida como diferença superior a 10% entre os dois valores.

| Parâmetro | Valor |
|---|---|
| Universo inicial do recorte | 3.392.881 documentos de imóvel |
| Subamostra comparável | 155 documentos |
| Critério de inclusão | Área legível e comparável no documento e no banco |
| População estimada com área válida | 2.615.891 documentos |
| Proporção com divergência crítica | 53,55% |
| Nível de confiança documentado | 95% |
| Margem de erro documentada | ±6,44 p.p. |

Os indicadores `27,1%` e `53,55%` medem fenômenos distintos e não são diretamente comparáveis. O primeiro estima inadequação funcional do conjunto documental; o segundo incide apenas sobre documentos de imóvel com área efetivamente comparável. A taxa de `53,55%` deve, portanto, ser lida como evidência complementar de baixa acurácia do campo área.

### 2.3 Amostra geoespacial (ACH-02)

O eixo geoespacial partiu da população analisável de 3.175.345 imóveis rurais ativos com coordenadas válidas para exame. Sobre essa base, os papéis de trabalho do funil geoespacial dimensionaram e extraíram amostra probabilística estratificada de 63.588 registros, organizada em quatro estratos temporais e tecnológicos. A cadeia metodológica foi a seguinte: PT-04 extraiu a amostra consolidada; PT-05 excluiu 12.231 registros por invalidez algorítmica, compreendendo coordenadas fora do envelope brasileiro, absurdos físicos, latitude igual à longitude e coordenadas zeradas; PT-06 reteve 43.812 registros com alta precisão decimal, definida como pelo menos cinco casas decimais em latitude e longitude. Esses 43.812 registros alimentaram, em paralelo, os testes de consistência municipal (PT-07) e de duplicação espacial (PT-08).

| Parâmetro | Valor |
|---|---|
| População de referência | 3.175.345 imóveis com coordenadas |
| Amostra consolidada inicial | 63.588 registros |
| Nível de confiança da amostra | 99% |
| Margem de erro de referência | ±1,0 p.p. no dimensionamento original |
| Margem de erro efetiva do filtro de alta precisão | ±0,40 p.p. |
| Estratos | 4 |
| Lógica de estratificação | Temporal/tecnológica |
| Seleção | Aleatória estratificada |

| Estrato | Tamanho amostral |
|---|---:|
| E1 — Leaflet antes | 16.501 |
| E2 — Leaflet depois | 14.359 |
| E3 — CAF 2.x | 16.456 |
| E4 — CAF 3.0 | 16.272 |
| **Total** | **63.588** |

Na documentação estatística, a margem de `±0,40 p.p.` está explicitamente associada, na peça 115, à estimativa da taxa de alta precisão decimal `43.812 / 51.357 = 85,31%`, com correção para população finita. Isso demonstra que o subconjunto usado nos testes geoespaciais avançados continua ancorado em base probabilística robusta. As taxas de erro cartográfico, duplicação espacial e inconsistência municipal devem, por isso, ser lidas como resultados do funil probabilístico sucessivamente qualificado.

## 3. Análises censitárias

### 3.1 Capacidade civil (ACH-03)

No ACH-03, a população de 2.905.101 responsáveis ativos foi submetida a cruzamento censitário com bases da Receita Federal e do Sisobi. Não houve amostragem. Cada CPF foi processado mediante ligação determinística e os resultados foram segregados por categoria de consistência cadastral. Como toda a população-alvo foi examinada, não se aplicam margem de erro, intervalo de confiança ou teste inferencial para os quantitativos produzidos.

| Indicador | Resultado | Critério |
|---|---:|---|
| Óbitos confirmados | 3.097 | Interseção RFB + Sisobi |
| Menores de 16 anos | 89 | Data de nascimento RFB |
| Adolescentes 16-17 não emancipados | 49 | Data de nascimento RFB |
| Divergências de data de nascimento | 11.999 | CAF diferente da RFB |
| CPFs não localizados | 520 | Sem retorno na base RFB |
| Datas futuras | 57 | Data posterior à data-base |

O aspecto estatisticamente relevante aqui não é a inferência, mas o critério de classificação. No caso dos óbitos, a auditoria adotou regra conservadora de dupla confirmação, exigindo presença simultânea em RFB e Sisobi.

### 3.2 Dados de contato, renda e CNAE (ACH-03)

Também por via censitária, a peça 125 avaliou 6.525.658 e-mails de pessoas físicas, 9.650 e-mails de pessoas jurídicas e 3.540.310 CEPs. A validação de e-mails combinou regra sintática tipo RFC 5322 com filtros semânticos para domínios fictícios. A validação de CEPs distinguiu CEPs genéricos e específicos e, entre os específicos, executou teste de consistência UF via API dos Correios. Complementarmente, os testes de renda e CNAE incidiram sobre 3.304.174 UFPAs ativas e 9.687 pessoas jurídicas.

| População/Indicador | Resultado |
|---|---:|
| E-mails PF analisados | 6.525.658 |
| E-mails PF inválidos/fictícios | 90,62% |
| Padrão `naopossui@mail.com` | 75,16% |
| E-mails PJ válidos | 99,70% |
| CEPs analisados | 3.540.310 |
| CEPs genéricos | 93,7% |
| UFPAs ativas para renda | 3.304.174 |
| Registros com renda > R$ 1 milhão | 907 |
| Registros com renda > R$ 10 milhões | 141 |
| Pessoas jurídicas com CNAE incompatível | 39 |

### 3.3 Metadados (ACH-04)

O ACH-04 foi inteiramente censitário. A auditoria processou a totalidade dos campos documentados no dicionário e os subconjuntos relevantes de campos numéricos, temporais e tabelas efetivamente em uso. A validade estatística decorre justamente da ausência de inferência: os percentuais divulgados correspondem à incidência direta do problema na população analisada.

| População/Indicador | Resultado | Critério |
|---|---:|---|
| Campos documentados | 527 | Universo do dicionário |
| Descrições inadequadas | 496 (94,1%) | Tautologia ou insuficiência semântica |
| Campos numéricos | 125 | Universo específico |
| Sem unidade de medida | 105 (84,0%) | Ausência de unidade explícita |
| Campos temporais | 87 | Universo específico |
| Temporais ambíguos | 80 (92,0%) | Evento temporal não especificado |
| Tabelas em uso documentadas | 95/95 (100%) | Cobertura do schema utilizado |

## 4. Projeções populacionais

As projeções populacionais foram calculadas pela aplicação da proporção observada na amostra à população-alvo correspondente. Quando a própria peça já continha cálculo formal do intervalo, prevaleceu o valor documentado. Quando o papel de trabalho apresentava apenas a projeção pontual, o intervalo foi reconstruído com base na fórmula clássica para proporções, com explicitação do nível de confiança utilizado.

```text
Estimativa pontual:
  P = p × N

Intervalo de confiança:
  IC = (p ± z × SE) × N

Com:
  p  = proporção observada na amostra
  N  = população de referência
  z  = valor crítico da distribuição normal
  SE = sqrt[p × (1-p) / n] × FPC
  FPC = sqrt[(N - n) / (N - 1)]
```

No ACH-01 geral, a peça 140 já traz o cálculo completo com correção para população finita. Na subamostra de divergência de área, a peça 109 documenta o desenho com 95% de confiança; o intervalo abaixo foi reconstruído a partir da proporção `83/155`. No eixo geoespacial, a peça 115 formaliza o uso de correção para população finita no filtro de alta precisão, o que sustenta a leitura probabilística do funil; para as projeções dos indicadores de erro cartográfico, duplicação espacial e inconsistência municipal, os valores abaixo devem ser lidos como aproximações conservadoras sob hipótese SRS aplicada ao subconjunto efetivamente analisado.

| Achado | Indicador | p | População (N) | Projeção central | Intervalo utilizado |
|---|---|---:|---:|---:|---|
| ACH-01 | Inadequação funcional documental | 27,1% | 11.377.318 | 3.083.253 | IC 99%: 2.571.274 a 3.595.272 |
| ACH-01 | Divergência crítica de área | 53,55% | 2.615.891 | 1.400.767 | IC 95% aprox.: 1.195.375 a 1.606.159 |
| ACH-02 | Erro cartográfico total | 45,92% | 3.175.345 | 1.458.118 | IC 99% aprox.: 1.440.278 a 1.475.959 |
| ACH-02 | Duplicações espaciais | 55,27% | 3.175.345 | 1.755.013 | IC 99% aprox.: 1.735.717 a 1.774.309 |
| ACH-02 | Inconsistência municipal | 15,92% | 3.175.345 | 505.515 | IC 99% aprox.: 491.316 a 519.713 |

Dois esclarecimentos são necessários. Primeiro, a projeção de `3,08 milhões` no ACH-01 deriva diretamente da peça 140 e é a referência oficial do relatório. Segundo, a projeção de divergência de área não substitui a projeção de inadequação funcional geral: trata-se de estimativa subordinada a universo comparável menor e a nível de confiança distinto. Terceiro, os indicadores projetados do ACH-02 não são mutuamente exclusivos e, portanto, não podem ser somados entre si para formar quantitativo único de registros afetados.

## 5. Validação e controle de qualidade

### 5.1 Validação da classificação documental

Na peça 103, a classificação automatizada dos 646 documentos foi submetida a estratificação prévia, tratamento de 23 casos inicialmente não classificados, reclassificação manual e validação cruzada independente. A taxa de inadequação projetada para a população não resulta de saída bruta do modelo, mas de consolidado final auditado. Não foi empregada métrica formal de concordância do tipo Kappa.

### 5.2 Validação dos cruzamentos censitários

Nos cruzamentos do ACH-03, a validação ocorreu por desenho conservador do critério decisório. O caso mais importante é o de falecidos, em que a equipe só contabilizou óbito quando houve confirmação simultânea em RFB e Sisobi. CPFs sem retorno foram segregados em categoria própria, evitando contaminação do indicador de óbitos confirmados. A mesma lógica de prudência foi utilizada nos testes de contato e CEP, mediante separação entre inválido, genérico, inexistente e inconsistente.

### 5.3 Reanálise ministerial no ACH-02

A análise de inflação cadastral municipal encontrou 632 municípios com área cadastrada superior à área oficial do IBGE. Desses, 608 apresentavam cobertura igual ou superior a 100% e foram objeto de reanálise específica pelo gestor na peça 161. O MDA afastou a materialidade em 558 casos e manteve universo residual de 50 municípios, dos quais 10 com indício de plausibilidade do achado e 40 dependentes de averiguação complementar. Sob perspectiva estatística, essa reanálise não invalida o teste censitário original; ela apenas recalibra a interpretação substantiva do subconjunto mais crítico e deve ser entendida como refino contraditório do alcance do indicador agregado.

## 6. Limitações estatísticas

As limitações quantitativas mais relevantes são as seguintes. A primeira diz respeito à heterogeneidade entre desenhos: o ACH-01 geral usa amostra estratificada específica de documentos; a subamostra de área usa recorte complementar com `n=155` e confiança de 95%; o ACH-02 opera sobre funil probabilístico em múltiplas camadas; e os ACH-03 e ACH-04 são censitários. Misturar esses desenhos como se fossem equivalentes levaria a conclusões indevidas. A segunda é que a validade inferencial das projeções geoespaciais depende da rastreabilidade entre PT-04, PT-05, PT-06 e os testes subsequentes; a documentação é suficiente, mas a replicação integral por terceiro exige acesso aos scripts e artefatos intermediários.

A terceira limitação concerne ao uso de classificação automatizada no ACH-01. Embora a estimativa final tenha sido validada manualmente em casos críticos, a ausência de métrica formal de concordância IA versus auditor impede afirmar precisão classificatória em sentido estritamente experimental. A quarta é que a análise de DPI da peça 106 foi complementar e não probabilística; por isso, ela não integra as tabelas inferenciais deste apêndice. A quinta é temporal: as estimativas refletem a base observada no período auditado e não capturam alterações posteriores. A sexta é interpretativa: o índice de conformidade integral de 32% produzido pelo gestor não compõe a base inferencial da auditoria e deve ser tratado apenas como contexto. Com essas ressalvas, a documentação estatística é suficiente para demonstrar que os achados amostrais foram produzidos com parâmetros explícitos de confiança e que os achados censitários dispensam extrapolação.
