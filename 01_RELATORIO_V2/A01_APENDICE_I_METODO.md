# APÊNDICE I — MÉTODO

## 1. Abordagem geral

Este trabalho foi conduzido como auditoria operacional, em conformidade com as NAT e em alinhamento com as ISSAI, com foco na obtenção de evidências suficientes e confiáveis e na documentação dos procedimentos executados (Introdução, §6; NAT, itens 107 a 111 e 134 a 135). O objeto auditado foi o Cadastro Nacional da Agricultura Familiar (CAF), considerando a versão 3 do sistema e a base observada entre março e agosto de 2025 (Introdução, §§2-5; peça 170). A estratégia analítica foi organizada em quatro dimensões de qualidade de dados: documental, geoespacial, cadastral e metadados. Essas dimensões responderam à `QST-01`, sobre a suficiência dos mecanismos de verificação de dados e regras de negócio do CAF, e à `QST-02`, sobre a suficiência da estrutura de governança e gestão de dados aplicada ao cadastro.

Para responder a essas questões, a equipe combinou revisão documental, cruzamento massivo de bases governamentais, análise geoespacial, classificação semântica automatizada de documentos e procedimentos estatísticos. O planejamento foi orientado pelos riscos `RIS-01`, `RIS-02` e `RIS-03`. Em todos os eixos, buscou-se manter rastreabilidade entre base utilizada, script executado, peça produzida e achado correspondente.

## 2. Fontes de dados

As análises utilizaram como fonte primária a extração integral da base do CAF fornecida à equipe de auditoria, complementada por bases externas, documentação técnica do sistema e manifestações do gestor. A base do CAF foi tratada como sistema de registro principal; as demais fontes foram usadas para validação, contraste e plausibilidade, conforme a natureza de cada teste.

| Fonte | Descrição | Período | Peça |
|---|---|---|---|
| Base de dados do CAF 3.0 | Extração integral da base ativa, incluindo UFPAs, imóveis, documentos, responsáveis e tabelas auxiliares | Mar-Ago/2025 | Peça 82 |
| Receita Federal (RFB) | Situação cadastral de CPFs, datas de nascimento e dados de identificação para cruzamentos de capacidade civil e plausibilidade cadastral | Bases consultadas no período de execução | Peça 124 |
| Sisobi | Registros de óbito utilizados para confirmação conservadora de falecimento de responsáveis | Cruzamento censitário | Peça 124 |
| CNIS | Base previdenciária utilizada como referência externa em cruzamentos cadastrais e de renda | Conforme disponibilidade institucional | Introdução, §3 |
| Sigef/Incra | Dados georreferenciados oficiais considerados em análises territoriais e de interoperabilidade | Conforme disponibilidade institucional | Introdução, §3 |
| Sicar (CAR) | Base subsidiária para comparações e discussão de interoperabilidade; excluída como eixo principal do escopo | Fonte auxiliar | Peça 39 |
| IBGE | Áreas oficiais municipais e malhas para testes de consistência territorial | 2022 | Peça 121 |
| Dicionário de dados do CAF | Artefato com 527 campos documentados e cobertura formal das tabelas em uso | Versão vigente à época da auditoria | Peça 75; peça 134 |
| Regras de negócio do CAF 3.0 | Documento funcional com RN de cadastro, validação e atualização | Vigente na execução | Peça 78 |
| Manifestação do gestor | Relatório Técnico DCAF e anexos de contraditório, usado para calibragem metodológica e reanálises pontuais | Mar/2026 | Peça 150 |

## 3. Técnicas empregadas

### 3.1 Revisão documental

A revisão documental foi a camada transversal do trabalho. Foram examinados normativos do CAF, documentação técnica do sistema e trabalhos anteriores do TCU sobre a DAP e o CAF. Essa revisão serviu para definir critérios de auditoria e interpretar corretamente os resultados dos testes automatizados.

### 3.2 Classificação semântica automatizada de documentos

No eixo documental, a equipe aplicou análise semântica automatizada sobre amostra probabilística estratificada de 646 documentos comprobatórios, distribuídos proporcionalmente entre declarações de veracidade, comprovantes de renda e documentos de imóvel (peça 103, p. 3-7). A amostra foi tratada com inferência estatística a 99% de confiança e margem de erro aproximada de ±4,5 pontos percentuais, com correção para população finita; as projeções populacionais foram atualizadas na peça 140 após consolidação da população correta de documentos do CAF em 11.377.318 registros (peça 140, p. 2-5). Os documentos foram classificados em três categorias operacionais: plenamente adequado, parcialmente adequado e inadequado.

A classificação foi executada por pipeline automatizado em Python com uso da API Claude Vision 3.5 Sonnet (outubro de 2025), da Anthropic, a partir de prompt estruturado desenvolvido pela equipe para avaliar adequação funcional documental segundo os critérios normativos do CAF (peça 103, p. 5). O prompt exigia classificação tripartite e justificativa textual. Considerou-se plenamente adequado o documento que comprovava integralmente o requisito declarado; parcialmente adequado aquele insuficiente para validação conclusiva; e inadequado aquele sem aptidão probatória para a categoria informada. O modelo foi utilizado como ferramenta auxiliar; os critérios de julgamento, a estratificação, os pesos populacionais e a validação final permaneceram sob responsabilidade dos auditores. Casos limítrofes ou sem classificação inicial passaram por reclassificação manual de 23 casos e validação cruzada independente ("prova dos 9"), com convergência superior a 95% e adoção de critério conservador nos casos duvidosos (peça 103, p. 7 e 16-24).

### 3.3 Cruzamento massivo de bases de dados governamentais

No eixo cadastral, a equipe empregou cruzamentos censitários sobre a população integral de registros relevantes, utilizando scripts SQL e consultas estruturadas sobre base PostgreSQL. Para capacidade civil, foram cruzados 2.905.101 responsáveis ativos do CAF com bases oficiais da Receita Federal e do Sisobi, por linkage determinístico de CPF e filtro posterior de confirmação em Sisobi, com critério conservador de dupla verificação de óbito (peça 124, p. 6-9 e Anexo C). Para dados de contato, aplicaram-se verificações sintáticas e funcionais sobre e-mails e CEPs (peça 125). Para renda, houve análise censitária de outliers e plausibilidade econômica, em complemento entre as peças 126 e 130. Para pessoas jurídicas, realizou-se cruzamento com a Receita Federal para identificação de CNAEs principais incompatíveis com a finalidade do cadastro (peça 127).

### 3.4 Análise geoespacial

No eixo geoespacial, a equipe estruturou uma cadeia de papéis de trabalho reproduzíveis para definir a população analisável, estratificar temporalmente a amostra e aplicar validações em camadas sucessivas. O ponto de partida foi a definição da população analítica de unidades familiares ativas, documentada no PT-01 reprodutível (peça 110). A partir dessa base, foi utilizada amostra estratificada temporal de 63.588 registros, com intervalo de confiança de 99% e margem de erro efetiva de ±0,40 ponto percentual, para comparar transições tecnológicas do CAF e identificar regressões ou melhorias em qualidade cartográfica (peças 110 e 119).

Os procedimentos combinaram validação algorítmica, validação territorial e análise agregada de integridade. Na primeira camada, a equipe detectou coordenadas fisicamente impossíveis, pontos fora do envelope brasileiro, casos de latitude igual à longitude e coordenadas zeradas (peça 114, p. 5-7). Na segunda, examinou consistência municipal, inflação cadastral, comparações com áreas oficiais do IBGE, duplicação espacial e efeitos das transições entre CAF 2.x, CAF 3.0 e Leaflet (peças 116, 117, 118, 119 e 121). A consistência municipal foi verificada por `spatial join`, com uso de `ST_Contains()` sobre a malha municipal oficial do IBGE em PostGIS, comparando o código IBGE do polígono de destino com o município declarado no cadastro (peça 116). O ferramental empregou SQL espacial, processamento em Python e visualizações cartográficas compatíveis com PostGIS, GeoPandas, Shapely e QGIS.

A reanálise ministerial sobre inflação municipal foi tratada como etapa de calibração. Dos 608 municípios com cobertura igual ou superior a 100% da área oficial, 558 foram reclassificados pelo gestor e 50 permaneceram como materialidade residual (peça 161). A etapa refinou o alcance probatório, mas não substituiu o teste original.

### 3.5 Análise estatística

A análise estatística foi aplicada em duas frentes. A primeira foi inferencial, com amostragem probabilística estratificada nos eixos documental e geoespacial. No ACH-01, a amostra de 646 documentos permitiu projeção populacional com intervalo de confiança de 99%, correção para população finita e estratificação por tipo documental; no subconjunto de documentos de imóvel com área válida identificável, foi utilizada subamostra específica de 155 casos para avaliação de divergência crítica de área, com 95% de confiança e margem de erro de ±6,44 pontos percentuais, conforme documentado na peça 109. No ACH-02, a amostra de 63.588 registros permitiu comparar estratos temporais e medir taxas de erro geoespacial com incerteza explicitada (peças 110 e 119).

A segunda frente foi censitária, aplicável aos achados cadastral e de metadados, nos quais a população integral estava disponível e pôde ser examinada diretamente. Sempre que houve generalização de resultados amostrais para a população, a equipe explicitou tamanho da amostra, método de seleção, parâmetros de confiança e incerteza embutida, em consonância com as NAT. O detalhamento completo de fórmulas e projeções consta do Apêndice II — Metodologia Estatística.

### 3.6 Análise de metadados

No ACH-04, a equipe empregou análise censitária sobre os metadados documentados do CAF. Foram confrontadas as tabelas base efetivamente existentes no schema `caf_mapa` com as tabelas e campos descritos no dicionário de dados oficial, mediante extração automatizada e comparação diferencial (peça 134). Em seguida, as descrições dos 527 campos documentados foram classificadas quanto à qualidade semântica com base em critérios inspirados na ISO/IEC 11179 e na ISO/IEC 25012, separando descrições tautológicas, técnicas, genéricas e funcionais (peça 135). Houve ainda análise de completude de unidade de medida em 125 campos numéricos (peça 136) e de ambiguidade semântica em 87 campos temporais (peça 133).

### 3.7 Avaliação de maturidade

Além dos testes substantivos, a equipe utilizou escala sintética de maturidade para organizar analiticamente as práticas observadas em cada achado. A escala foi adaptada do DAMA-DMBOK v2 e do CMMI-DMM, com seis níveis, de 0 a 5. Os níveis foram interpretados da seguinte forma: 0 = ad hoc, sem processo formal; 1 = inicial, com prática existente mas não repetível; 2 = repetível; 3 = definido; 4 = gerenciado; 5 = otimizado. As dimensões avaliadas foram ancoradas no referencial técnico mais aderente a cada achado.

## 4. Ferramentas computacionais

| Ferramenta | Uso | Achados |
|---|---|---|
| Python 3.x | Scripts de extração, classificação, cruzamento, consolidação e geração de memórias de cálculo | Todos |
| PostgreSQL / PostGIS | Consulta à base do CAF, filtros censitários, cruzamentos estruturados e operações espaciais | ACH-02, ACH-03, ACH-04 |
| Claude API (Anthropic) | Classificação semântica assistida de documentos comprobatórios | ACH-01 |
| GeoPandas / Shapely | Tratamento e validação de geometrias e coordenadas | ACH-02 |
| QGIS | Visualização cartográfica, inspeção de padrões espaciais e validação auxiliar | ACH-02 |
| Pandas / NumPy | Consolidação tabular, estatística descritiva e projeções | Todos |
| Jupyter Notebook e scripts versionados | Registro reprodutível de análises, tabelas e gráficos | Todos |

## 5. Limitações metodológicas

As limitações observadas não comprometem a suficiência das evidências, mas precisam ser explicitadas. A primeira é temporal: a auditoria incidiu sobre extrações e bases referentes principalmente ao período de março a agosto de 2025, embora alguns papéis de trabalho e reanálises tenham sido produzidos depois. A segunda decorre da natureza das técnicas empregadas. Na classificação semântica por IA, há risco inerente de variabilidade probabilística do modelo, mitigado por estratificação prévia, classificação supervisionada, reclassificação manual e validação cruzada independente. Nos testes de renda e plausibilidade econômica, a equipe avaliou coerência e sinais de anomalia, não veracidade material definitiva da renda autodeclarada. Na frente geoespacial, o uso do CAR foi subsidiário e fora do escopo principal, e a reanálise ministerial sobre municípios com inflação cadastral foi incorporada como refinamento do alcance probatório. O índice de 32% de conformidade integral produzido pelo gestor foi tratado apenas como dado contextual, sem auditoria independente.

## 6. Conformidade com as normas de auditoria

Os procedimentos descritos neste apêndice foram executados e documentados em conformidade com as NAT e em alinhamento com as ISSAI aplicáveis à auditoria operacional. A metodologia foi exposta resumidamente neste apêndice e detalhada em papéis de trabalho, memórias de cálculo e, quando pertinente, no Apêndice II, em observância ao dever de documentar planejamento, métodos, seleção de amostras, incerteza estatística e limitações do trabalho (NAT, itens 107 a 111, 134 e 135). Todas as evidências relevantes para sustentar os achados foram submetidas a avaliação de suficiência, relevância e confiabilidade, sem limitação metodológica identificada que comprometesse a confiabilidade global das conclusões do relatório (Introdução, §6).
