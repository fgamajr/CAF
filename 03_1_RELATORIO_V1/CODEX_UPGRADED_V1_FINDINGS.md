# Upgrade dos Achados do `relatorio_v1`

## Objetivo

Este documento registra os `upgrades` recomendados para os quatro achados do `relatorio_v1.md`, com base na comparacao entre:

- a reconstrucao independente dos achados a partir das pecas disponiveis ate a `140`;
- a matriz preliminar elaborada em `CODEX_MATRIZ_ACHADOS_PRELIMINAR.md`;
- a tabela de concordancia em `CODEX_TABELA_CONCORDANCIA_ACHADOS.md`.

O foco nao e reescrever todo o relatorio, mas `melhorar o que precisa ser melhorado`, preservando o que ja esta mais forte e corrigindo apenas o que aumenta fidelidade, robustez e reprodutibilidade.

## Visao geral

- `Achado I`: o relatorio ja esta melhor do que a minha versao inicial; o upgrade e de `clarificacao metodologica`.
- `Achado II`: o relatorio esta mais forte que a minha sintese inicial; o upgrade e de `nuanca analitica`.
- `Achado III`: ha `correcao numerica relevante` e um ajuste de ancoragem probatoria.
- `Achado IV`: o principal upgrade e `recalibrar o foco`, afastando a ideia de incompletude de cobertura e concentrando o achado na qualidade dos metadados.

## Achado I

### Diagnostico

O seu `Achado I` ja esta metodologicamente superior ao meu esboco inicial, porque usa a formulacao refinada da `peça 109` para a analise de area, com `53,55%` de divergencias criticas entre os `155` documentos com area valida identificavel, alem de divergencia agregada de `+120,89%` `(peça 109, p. 7 e p. 9)`.

O ponto que ainda pode ser melhorado e deixar `explicito` que:

- `27,1%` mede inadequacao semantica na amostra documental geral `(peça 103, p. 9-11)`;
- `53,55%` mede divergencia critica de area apenas no subconjunto comparavel de documentos de imovel com area valida identificavel `(peça 109, p. 7)`.

Sem essa explicacao, o leitor pode ler os dois numeros como se disputassem o mesmo fenomeno.

### Upgrade sugerido

Manter a tese central, mas explicitar que as duas metricas tratam de `universos distintos e complementares`.

### Redacao sugerida

`A auditoria identificou dois blocos complementares de fragilidade documental. No plano semantico, 27,1% dos documentos analisados mostraram-se inadequados para comprovar os requisitos que declaravam comprovar, com projecao de aproximadamente 3,08 milhoes de documentos problematicos na populacao documental do CAF (peça 103, p. 9-11; peça 140, p. 3-4). No plano especifico dos documentos de imovel com area comparavel, 53,55% apresentaram divergencia critica superior a 10% entre a area constante do documento e a area registrada na base, com viés agregado de +120,89%, projetando-se cerca de 1,44 milhao de documentos problematicos nesse subconjunto (peça 109, p. 7 e p. 9). As metricas nao se contradizem: a primeira mede inadequacao semantica da documentacao em geral; a segunda mede inconsistencia de area em documentos de imovel com area valida identificavel.`

## Achado II

### Diagnostico

O seu `Achado II` esta mais completo do que a minha reconstrucao inicial. Ele integra bem os PTs do bloco geoespacial e registra:

- aumento da taxa total de erro de `32,66%` para `45,92%` `(peça 119, p. 9)`;
- inconsistencias municipais em `15,92%` dos registros de alta precisao;
- regressao de precisao decimal na interface `Leaflet`;
- duplicacoes espaciais em patamar elevado;
- inflacao cadastral municipal.

O upgrade util aqui nao e reforcar materialidade, porque isso o texto ja faz. O ganho esta em adicionar uma `nuanca defensavel`: a deterioracao geoespacial nao significa que `tudo` piorou uniformemente, mas que o `efeito combinado das transicoes tecnologicas` produziu piora global material da confiabilidade espacial.

Isso deixa o achado mais equilibrado e menos vulneravel a critica de sobreafirmacao.

### Upgrade sugerido

Manter o achado, mas explicitar que houve `quadro combinado` de passivo herdado, regressao de validacoes e trade-offs de interface, e que a conclusao deriva da `piora global do resultado`, nao de uma tese de colapso uniforme em toda subdimensao.

### Redacao sugerida

`A evidencia indica deterioracao material da confiabilidade geoespacial do CAF, especialmente apos as transicoes tecnologicas recentes. Embora nem toda subdimensao tenha se comportado de forma identica, o efeito combinado do passivo historico, do relaxamento de validacoes e dos trade-offs introduzidos na migracao para o CAF 3.0 e na interface Leaflet elevou a taxa total de erro de 32,66% para 45,92%, ampliou os erros algoritmicos, preservou duplicacoes espaciais em patamar elevado e manteve inconsistencias territoriais relevantes, inclusive em nivel municipal (peça 114, p. 18-19; peça 117, p. 31-32; peça 119, p. 9; peça 121, p. 27-28).`

## Achado III

### Diagnostico

Aqui esta o principal ajuste objetivo.

O relatorio usa `139` UFs com renda superior a `R$ 10 milhoes`, mas a versao recalculada mais recente e o indice mestre apontam `141` UFs `(peça 126, p. 25; peça 128, changelog)`.

Ha tambem um ponto de ancoragem probatoria que merece ficar mais limpo:

- `12.820` registros relacionados a obito funcionam como `triagem bruta`;
- o numero conservador e conclusivo para o achado e `3.097` obitos confirmados no `Sisobi` `(peça 124, p. 9 e p. 15)`.

O nucleo do achado nao muda, mas a precisao melhora.

### Upgrade sugerido

- corrigir `139` para `141`;
- deixar claro, quando o tema for obito/capacidade civil, qual numero e de triagem e qual numero e de confirmacao robusta.

### Redacao sugerida

`A auditoria identificou fragilidades relevantes na qualidade cadastral do CAF, com 15.811 inconsistencias criticas de identidade e capacidade civil, entre as quais 3.097 obitos confirmados no Sisobi, alem de registros com menores sem capacidade civil, idades impossiveis e divergencias cadastrais relevantes (peça 124, p. 9 e p. 15). Nos dados de contato, 90,62% dos e-mails de pessoas fisicas mostraram-se invalidos ou ficticios e 93,7% dos CEPs eram genericos (peça 125, p. 5-9). Nos dados economicos, a analise identificou 141 Unidades Familiares com renda superior a R$ 10 milhoes, incluindo valor extremo de R$ 167,3 milhoes, sem evidencia de trava automatizada de plausibilidade compativel com a criticidade do campo (peça 126, p. 25; peça 128).`

## Achado IV

### Diagnostico

O principal ganho aqui e `recalibrar o objeto do achado`.

O seu texto ja absorveu corretamente a clarificacao de que as `95` tabelas em uso estao documentadas, ou seja, nao ha mais base para sustentar `incompletude de cobertura` como nucleo do achado `(relatorio_v1.md, §1088)`.

Com isso, o foco mais defensavel e:

- inadequacao semantica das descricoes;
- ausencia de unidades de medida;
- ambiguidade temporal;
- fragilidades de rastreabilidade e de manutencao.

Tambem foi uma boa decisao nao puxar o subbloco de `foreign keys` para o centro do achado sem PT primario claramente localizado.

### Upgrade sugerido

Reposicionar o achado como `deficiencia qualitativa e de maturidade dos metadados`, e nao como falha de cobertura do dicionario.

### Redacao sugerida

`O problema central do dicionario de dados do CAF nao e mais de cobertura formal das tabelas em uso, mas de qualidade, granularidade e utilidade auditavel dos metadados. Embora as 95 tabelas em uso estejam documentadas, persistem deficiencias semanticamente relevantes nas descricoes dos campos, ausencia de unidades de medida em parcela expressiva dos atributos numericos e ambiguidades temporais que comprometem interpretacao independente, manutencao tecnica e rastreabilidade analitica (peça 132, p. 3; peça 133, p. 3; peça 135, p. 3-4; peça 136, p. 3-4).`

## Prioridade de incorporacao

Se voce quiser aplicar upgrades minimos de alto impacto no `relatorio_v1`, a ordem recomendada e:

1. `Achado III`: corrigir `139 -> 141` e separar triagem bruta de confirmacao robusta.
2. `Achado IV`: recentrar o achado em `qualidade/maturidade dos metadados`, nao em cobertura.
3. `Achado I`: explicitar que `27,1%` e `53,55%` medem universos diferentes.
4. `Achado II`: adicionar a nuanca de que a conclusao decorre da `piora global combinada`, e nao de deterioracao uniforme em toda subdimensao.

## Conclusao

O saldo da comparacao e favoravel ao seu relatorio: em `Achado I`, `Achado II` e `Achado IV`, o `relatorio_v1` ja estava melhor calibrado do que a minha sintese inicial. Os upgrades acima servem para `blindar` a redacao, reduzir vulnerabilidade a contestacoes metodologicas e aumentar a reprodutibilidade por terceiro independente.
