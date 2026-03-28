# CONCLUSÃO

60. A auditoria avaliou a qualidade dos dados do CAF 3.0 em quatro dimensões complementares — documental, geoespacial, cadastral e de metadados — e a estrutura de governança de dados aplicada ao cadastro, no período de março a agosto de 2025. Os achados foram analisados à luz dos critérios legais de elegibilidade e dos referenciais técnicos de governança e qualidade de dados. Esta seção sintetiza os resultados, responde às questões de auditoria e fundamenta as propostas de encaminhamento.

## 4.1 Critérios de auditoria aplicados

61. A avaliação utilizou conjunto integrado de critérios legais, regulamentares e técnicos. Os critérios legais — Lei 11.326/2006, Decreto 9.064/2017 e Portarias MDA 19/2025 e 20/2025 — definem o que o CAF deve fazer: identificar e qualificar o público da agricultura familiar com base em requisitos cumulativos de elegibilidade. Os referenciais técnicos — DAMA-DMBOK v2, ISO/IEC 25012:2008, ISO 19157-1:2023, ISO/IEC 11179:2015 e COBIT 2019 — definem como avaliar se o cadastro está fazendo adequadamente: qualidade de dados, qualidade geoespacial, registro de metadados e gestão de mudanças. O DAMA-DMBOK, expressamente adotado pelo Acórdão 457/2026-TCU-Plenário como referencial de maturidade de governança de dados, funcionou como critério transversal aplicável aos quatro achados. A avaliação de maturidade, adaptada do CMMI-DMM, foi adotada como instrumento analítico para permitir comparação entre dimensões e situar o estágio observado em cada uma delas. A cadeia de reincidência — Acórdãos 1197/2018, 1866/2021 e 885/2024-TCU-Plenário — fundamentou a natureza de determinação (e não mera recomendação) do encaminhamento principal.

**Quadro 6** — Rastreabilidade dos critérios de auditoria

| Critério | Natureza | Achados |
|---|---|---|
| Lei 11.326/2006 (elegibilidade, 4 módulos fiscais) | Legislação | ACH-01, ACH-02, ACH-03 |
| Decreto 9.064/2017 (finalidade do CAF) | Legislação | ACH-01, ACH-02, ACH-03 |
| Portaria MDA 19/2025 (inscrição no CAF) | Regulamentação | ACH-01, ACH-03 |
| Código Civil, arts. 3º, 4º e 6º | Legislação | ACH-03 |
| Decreto 10.046/2019 (governança de dados na APF) | Legislação | ACH-02, ACH-04 |
| DAMA-DMBOK v2 (governança de dados) | Técnico | ACH-01, ACH-02, ACH-03, ACH-04 |
| ISO/IEC 25012:2008 (qualidade de dados) | Técnico | ACH-01, ACH-03 |
| ISO 19157-1:2023 (qualidade geoespacial) | Técnico | ACH-02 |
| ISO/IEC 11179:2015 (metadados) | Técnico | ACH-04 |
| COBIT 2019 BAI10 (gestão de mudanças) | Técnico | ACH-02, ACH-04 |
| Ac. 1197/2018-TCU-Plenário (reincidência) | Jurisprudência | ACH-01, ACH-02, ACH-03 |
| Ac. 457/2026-TCU-Plenário (DAMA-DMBOK) | Jurisprudência | ACH-04 |

*Fonte: Matriz de Planejamento (Anexo C) e Matriz de Achados (Anexo B).*

## 4.2 Síntese dos achados como quadro integrado

62. Os quatro achados não descrevem problemas isolados, mas dimensões convergentes de um mesmo fenômeno: a insuficiência dos mecanismos de governança e qualidade de dados do CAF para assegurar, em escala compatível com o cadastro, a confiabilidade das informações que sustentam a identificação e qualificação da agricultura familiar. A avaliação de maturidade, aplicada de forma adaptada em cada achado, permite visualizar esse diagnóstico em perspectiva comparada.

**Quadro 7** — Maturidade consolidada da governança de dados do CAF

| Achado | Referencial principal | Dimensões avaliadas | Maturidade média | Dimensão mais frágil |
|---|---|---|---|---|
| ACH-01 — Dados de entrada | DAMA-DMBOK Cap. 13 | 7 | Inicial (0,43) | Consistência e acurácia de área = Ad-hoc (0) |
| ACH-02 — Geoespacial | ISO 19157-1:2023 | 5 | Ad-hoc (0,20) | 4 de 5 dimensões = Ad-hoc (0) |
| ACH-03 — Cadastral | ISO/IEC 25012:2008 | 5 | Ad-hoc (0,40) | Funcionalidade dos canais de contato = Ad-hoc (0) |
| ACH-04 — Metadados | ISO/IEC 11179:2015 | 7 | Ad-hoc (0,14) | 6 de 7 dimensões = Ad-hoc (0) |
| **Média geral** | | **24 dimensões** | **Ad-hoc (0,29)** | |

*Escala adaptada do DAMA-DMBOK v2 e CMMI-DMM: 0 = Ad-hoc; 1 = Inicial; 2 = Repetível; 3 = Definido; 4 = Gerenciado; 5 = Otimizado. A comparação entre achados é indicativa, não absoluta: os quadros utilizam a mesma escala mas avaliam dimensões distintas. Nota: o ACH-04 apresenta a menor maturidade entre os quatro achados (0,14), refletindo o fato de que a camada mais fundamental — a que explica o que os dados significam — é a que recebeu menos atenção formal, apesar de o dicionário existir e cobrir 100% do esquema. A única dimensão acima do nível ad-hoc é a clareza do modelo conceitual, onde o MER técnico já existe como alicerce parcial.*

*Fonte: elaboração da equipe de auditoria com base nos quadros de maturidade dos quatro achados.*

63. Três leituras emergem desse quadro. A primeira é o padrão transversal: a média geral de 0,29 situa a governança de dados do CAF entre o estágio Ad-hoc e o Inicial. Existem práticas pontuais — o dicionário de dados cobre 100% das tabelas, o Leaflet reduziu duplicações em novos cadastros de 92,36% para 16,59%, o BCadastro consulta a base da Receita Federal —, mas sem processos formais, repetíveis e monitorados. A segunda é a dualidade fluxo corrente vs. passivo: o CAF 3.0 elevou várias dimensões ao nível Inicial no fluxo de novos cadastros, mas o passivo herdado das versões anteriores permanece em nível Ad-hoc, sem programa estruturado de curadoria. A terceira é a hierarquia de fragilidade: a camada de metadados (ACH-04, média 0,14) é a mais frágil e também a mais fundamental — sem ela, as melhorias propostas para as três dimensões anteriores não se sustentam a longo prazo.

**Quadro 8** — Dados-chave consolidados

| Dimensão | Indicadores principais | Projeção de impacto |
|---|---|---|
| Documental (ACH-01) | 27,1% inadequados (~3,08M docs), 53,55% divergência área (~1,44M), 68,7% < 300 DPI | Habilitação prévia Pronaf (R$ 59,6 bi/safra) |
| Geoespacial (ACH-02) | 45,92% erro cartográfico (~1,46M imóveis), 55,27% duplicações, 632 municípios | Validação de 4 módulos fiscais |
| Cadastral (ACH-03) | 3.097 falecidos, 138 menores, 90,62% e-mails fictícios, 907 renda > R$1M | Focalização + comunicação com beneficiários |
| Metadados (ACH-04) | 94,1% descrições inadequadas, 84% sem unidade, 92% temporais ambíguos | Sustentabilidade de todas as melhorias |

*Fonte: Matriz de Achados (Anexo B) e peças processuais referenciadas em cada achado.*

## 4.3 Discussão das situações identificadas — Resposta às questões de auditoria

### Primeira questão: qualidade dos dados e tratamento do passivo

64. **QST-1 — Em que medida os mecanismos de verificação de dados do CAF asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio?**

Os mecanismos asseguram o atendimento de forma parcial e insuficiente. O CAF 3.0 implementou melhorias demonstráveis no fluxo corrente de cadastramento: validações que reduziram o cadastramento de propriedades inelegíveis (98,7% das que excedem 4 módulos fiscais são anteriores ao CAF 3.0), interface Leaflet que conteve duplicações geoespaciais (92,36% → 16,59% em novos cadastros), consultas automatizadas à base da Receita Federal via BCadastro/ConectaGOV e vedação de menores como responsáveis. Esses avanços são relevantes e afastam leitura de inércia administrativa.

65. Porém, o passivo acumulado nas versões anteriores permanece ativo na base sem rotina estruturada de saneamento. A coexistência de 27,1% de documentos semanticamente inadequados com 45,92% de erro cartográfico e 3.097 titulares falecidos configura fragilidade sistêmica que transcende qualquer dimensão individual. O problema não está apenas nos documentos, nas coordenadas ou nos dados cadastrais isoladamente, mas na ausência de governança integrada que trate essas dimensões como sistema. O tratamento do passivo requer resposta institucional planejada — o plano de ação em 180 dias proposto visa exatamente criar esse planejamento, com critérios de risco, materialidade e verificabilidade definidos pelo próprio gestor.

### Segunda questão: governança como pré-requisito e metadados como habilitador

66. **QST-2 — Em que medida a estrutura de governança e gestão de dados aplicada ao CAF assegura padrões claros, papéis definidos, rastreabilidade e integridade das informações ao longo de todo o ciclo de vida dos dados?**

A estrutura de governança apresenta maturidade incipiente. O iGovSisp 2024 confirma a autoavaliação do MDA nesse sentido (peça 139, p. 2), e o gestor concordou expressamente durante o contraditório que a governança de dados do órgão está em processo de maturação (peça 150, p. 53). O achado de metadados (ACH-04) revelou que a única documentação estruturada do banco de dados — o dicionário — apresenta insuficiência qualitativa relevante: 94,1% de descrições inadequadas, 84% de campos numéricos sem unidade e 92% de campos temporais ambíguos. O conhecimento sobre o significado dos dados existe, mas está fragmentado entre instrumentos não integrados e preservado, em grande medida, na memória dos técnicos mais antigos.

67. A conexão transversal demonstrou que metadados inadequados são a causa subjacente de parte das fragilidades identificadas nos demais achados: impossibilidade de automatizar validação tipo-documental quando o dicionário não mapeia os tipos aceitos pela Portaria 19/2025 (ACH-01); opacidade das relações coordenada→município quando o modelo de dados não explicita essas relações (ACH-02); e ambiguidade temporal que dificulta a curadoria de dados obsoletos quando os campos de data não distinguem criação técnica e evento de negócio (ACH-03). Governança, portanto, não é uma dimensão a mais — é o pré-requisito para que as correções nas três dimensões anteriores sejam sustentáveis. E metadados são o habilitador operacional dessa governança.

### Institucionalização: formalização de papéis como condição de sustentabilidade

68. Se a governança é incipiente e os metadados são a infraestrutura, a pergunta que se impõe é: quem é responsável por cada domínio de dados do CAF? A auditoria identificou que não há data steward formal para as dimensões de dados examinadas, que as responsabilidades de curadoria estão distribuídas informalmente, que o dicionário de dados não tem dono designado e que as regras de negócio (peça 78), embora relevantes, não estão vinculadas campo a campo aos metadados. A formalização de papéis não é proposta como burocracia adicional, mas como condição para que as melhorias se institucionalizem — para que não dependam de indivíduos e se tornem patrimônio institucional do MDA.

## 4.4 Riscos à missão institucional do CAF

69. A Visão Geral (§12) identificou três vetores de risco que motivaram a auditoria. Os achados confirmaram e detalharam cada um deles.

| Vetor de risco | Como os achados confirmaram |
|---|---|
| (i) Inexatidão e inconsistência | ACH-01: 27,1% inadequação semântica, 53,55% divergência de área. ACH-02: 45,92% erro cartográfico, 55,27% duplicações |
| (ii) Obsolescência e incompletude | ACH-03: 3.097 falecidos, 138 menores, 90,62% e-mails fictícios |
| (iii) Fragilidades de governança | ACH-04: 94,1% descrições inadequadas, governança declaradamente imatura |

70. A persistência conjunta desses vetores configura risco potencial de que o CAF, que serve de habilitação prévia para políticas que movimentaram R$ 59,6 bilhões na safra 2023/2024, opere com nível de incerteza informacional incompatível com a escala e a criticidade do cadastro. A auditoria não identificou dano consumado ao erário nem fraude demonstrada. Os riscos descritos são potenciais e decorrem da fragilidade sistêmica documentada nos quatro achados, não de ação ou omissão dolosa. Os avanços implementados pelo gestor — CAF 3.0, Leaflet, BCadastro/ConectaGOV, vedação de menores, TED DCAF/UFES 2025-2027, renovação prevista de ~742 mil registros em 2026 e formação de mais de 10 mil agentes da RedeCAF — demonstram capacidade de reação institucional e afastam leitura de inércia, mas confirmam que o enfrentamento ainda não alcança a totalidade do passivo ativo na base.

## 4.5 Formulação das propostas — Ponte para os encaminhamentos

71. Os encaminhamentos propostos combinam uma determinação e sete recomendações, organizadas pela lógica causa→proposta. A determinação de apresentação de plano de ação em 180 dias (Proposta 1) é medida de natureza obrigatória, fundamentada na reincidência documentada na cadeia de deliberações Acórdão 1197/2018-TCU-Plenário (TC 012.700/2017-7, item 9.2.6 — incorporar salvaguardas de qualidade de dados ao sistema que sucederia a DAP) → Acórdão 1866/2021-TCU-Plenário (monitoramento — cumprimento parcial) → Acórdão 885/2024-TCU-Plenário (monitoramento — itens pendentes de cumprimento integral). A natureza de determinação, e não de mera recomendação, decorre do fato de que as situações identificadas nesta auditoria reproduzem, em grande medida, fragilidades já apontadas naquela cadeia de deliberações. O prazo permite ao gestor planejar o saneamento com critérios de risco, materialidade e verificabilidade, conforme defendido no contraditório. As recomendações, por sua vez, definem resultados a alcançar, sem prescrever soluções técnicas.

**Quadro 9** — Rastreabilidade das propostas: causa → dimensão → resultado esperado

| Proposta | Causa que endereça | Achados/Dimensões | Resultado esperado |
|---|---|---|---|
| **1** — Plano de ação 180 dias (determinação) | Passivo sem saneamento + reincidência | Transversal (ACH-01 a ACH-04) | Planejamento estruturado por risco e materialidade |
| **2.1.1** — Prevenção na entrada | Ingestão sem validação semântica | ACH-01 (Dim. 1) | Reduzir taxa de 27,1% |
| **2.1.2** — Integridade campos críticos | Ausência de controles de área e localização | ACH-01 (Dim. 2), ACH-02, ACH-03 | Reduzir divergência de 53,55% e erro de 45,92% |
| **2.1.3** — Interoperabilidade | Sem cruzamento Sisobi/Sigef/Sicar | ACH-02, ACH-03 | Detecção tempestiva de inconsistências |
| **2.1.4** — Qualidade de digitalização | Sem requisitos técnicos formais | ACH-01 (Dim. 3) | Viabilizar OCR e auditabilidade |
| **2.2** — Gestão de mudanças | Transições sem regressão | ACH-02 (Dim. 5), ACH-04 | Preservar qualidade em evoluções |
| **2.3** — Monitoramento contínuo | Sem dashboards nem métricas | ACH-01 (Dim. 4), ACH-03 | Visibilidade da qualidade |
| **2.4** — Gestão de metadados | Dicionário inadequado | ACH-04 | Sustentabilidade de todas as melhorias |

*Fonte: Matriz de Achados (Anexo B) e análise transversal dos encaminhamentos.*

72. Todas as propostas foram formuladas como resultados a alcançar, preservando a liberdade de meios do gestor para definir as soluções técnicas e operacionais mais adequadas à sua realidade institucional. O gestor acolheu parte das propostas e apresentou enfrentamento em curso, o que foi registrado nos respectivos achados. O detalhamento dos encaminhamentos e a proposta de deliberação constam da seção seguinte.
