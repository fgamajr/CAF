## {S} ACHADO 04

**Insuficiência qualitativa dos metadados do CAF compromete a interpretação autônoma dos dados, a auditabilidade do cadastro e a sustentabilidade das melhorias recomendadas nos achados anteriores**

105. Devido à maturidade ainda incipiente da gestão de metadados do CAF, em que o conhecimento técnico existe, mas permanece fragmentado entre instrumentos não integrados e sem atualização incorporada ao ciclo de desenvolvimento, a única documentação estruturada do banco de dados apresenta insuficiência qualitativa relevante: 94,1% das descrições do dicionário são semanticamente inadequadas, 84% dos campos numéricos não informam unidade de medida e 92% dos campos temporais permanecem ambíguos, embora haja cobertura formal de 100% das 95 tabelas efetivamente em uso. Esse quadro não traduz ausência absoluta de documentação, mas compromete potencialmente a rastreabilidade, a auditabilidade, a interpretação independente dos dados e a manutenção evolutiva do sistema.

106. Além disso, o quadro reduz a sustentabilidade das melhorias recomendadas nos achados anteriores, já que validação, curadoria e monitoramento dependem de metadados claros para se manterem consistentes ao longo do tempo. Os referenciais adotados para esta avaliação são a ISO/IEC 11179:2015 ²⁵, o Decreto 10.046/2019 ²⁶ e o COBIT 2019 ²⁷.

### {SS} O dicionário de dados como manual de instruções do CAF

107. O tema é mais abstrato do que os dos achados anteriores, porque não trata diretamente de documentos, mapas ou pessoas cadastradas, mas da infraestrutura semântica que permite compreender tudo isso. Em termos simples, o dicionário de dados funciona como o manual de instruções do banco de dados do CAF. É ele que deveria explicar, para cada campo, o que a informação significa, em que unidade está expressa, qual evento temporal registra e como deve ser interpretada. Quando esse manual é insuficiente, o sistema não deixa de funcionar, mas passa a operar como caixa-preta: só compreende plenamente seus dados quem já conhece as regras implícitas. No caso do CAF, isso é especialmente sensível porque a base reúne 527 campos documentados e integra esquema maior com 109 tabelas, das quais 95 estavam efetivamente em uso no momento da análise e cobertas pelo dicionário (peça 70; peça 134, p. 4).

108. A ISO/IEC 11179:2015 estabelece que todo elemento de dados em um registro de metadados deve conter, no mínimo, nome, definição inequívoca, tipo, domínio de valores, unidade de medida (quando aplicável) e fonte autoritativa, ou seja, o conjunto de atributos necessário para que qualquer usuário autorizado possa interpretar o dado sem conhecimento prévio do sistema. O DAMA-DMBOK v2 complementa esse referencial ao tratar os metadados como pré-requisito para todas as demais funções de governança de dados: sem saber o que cada campo significa, não é possível definir regras de qualidade, implementar validações, planejar integrações nem monitorar a evolução da base (Cap. 12, peça 86, p. 13). A análise que se segue organiza as constatações em dimensões que refletem esses referenciais.

109. Para manter comparabilidade com os achados anteriores, a equipe adota a mesma escala sintética de maturidade: 0 = ad-hoc; 1 = inicial; 2 = repetível; 3 = definido; 4 = gerenciado; 5 = otimizado. Trata-se de escala analítica adaptada do DAMA-DMBOK e do CMMI-DMM, não de aplicação literal da taxonomia de nenhum desses referenciais.

#### Ponto forte: cobertura estrutural

110. Antes de detalhar as dimensões de fragilidade, é necessário reconhecer o ponto positivo mais relevante: o dicionário de dados do CAF cobre 100% das 95 tabelas efetivamente em uso (peça 134, p. 4). Além disso, 31 campos (5,9%) já apresentam descrições funcionais adequadas (peça 135, p. 4), constituindo benchmark interno que demonstra viabilidade técnica imediata, pois a equipe do sistema sabe produzir descrições de qualidade quando o faz. O diagnóstico que se segue, portanto, não é sobre ausência de documentação, mas sobre insuficiência qualitativa da documentação existente. Essa distinção é central para calibrar o tom do achado: o CAF dispõe de alicerce concreto para melhoria incremental, não necessita de reconstrução do zero.

#### {SSS} Diagnóstico por dimensão de qualidade de metadados

##### Dimensão 1 — Riqueza semântica das descrições

111. A auditoria constatou, assim, um conflito claro entre o que existe e o que deveria existir. De um lado, há infraestrutura básica de documentação, ponto positivo que precisa ser reconhecido: o dicionário cobre integralmente as tabelas em uso e o Documento de Regras de Negócio do CAF 3.0 contém definições funcionais relevantes (peça 78). De outro, a qualidade semântica dessa documentação permanece insuficiente para os padrões de gestão de metadados preconizados pela ISO/IEC 11179, pelo DAMA-DMBOK v2 e pela governança de dados da Administração Pública. A análise censitária dos 527 campos mostrou que 496 descrições, equivalentes a 94,1%, são inadequadas porque apenas repetem o nome técnico da coluna ou empregam fórmulas genéricas que não ajudam o leitor a compreender o dado em contexto de negócio (peça 135, p. 4). Em vez de explicar, o dicionário frequentemente apenas reescreve o nome da variável em português corrido.

**Tabela 7** — Síntese das insuficiências do dicionário de dados do CAF

| Dimensão | Universo analisado | Situação identificada | Resultado |
|---|---:|---|---:|
| Cobertura formal | 95 tabelas em uso | Tabelas documentadas no dicionário | 100% |
| Qualidade semântica | 527 campos | Descrições inadequadas | 94,1% |
| Unidade de medida | 125 campos numéricos | Campos sem unidade especificada | 84% |
| Clareza temporal | 87 campos temporais | Campos ambíguos quanto ao evento registrado | 92% |

*Fonte: elaboração da equipe de auditoria com base nas peças 132, 133, 134, 135 e 136.*

112. A deficiência torna-se mais visível quando se abandona a abstração e se olha para exemplos concretos. O campo `id_area_imovel`, por exemplo, aparece descrito como "ID de identificação de área imóvel", expressão tautológica que não informa sua função no modelo de dados; `nr_area` surge como "Tamanho da área imóvel", sem dizer se o valor está em hectares, metros quadrados ou outra unidade; `nr_latitude` e `nr_longitude` não informam datum ou formato; `dt_criacao` e `dt_atualizacao` não distinguem se se referem à criação técnica do registro ou ao evento de negócio subjacente (peça 75; peça 133, p. 6-8; peça 136, p. 5-6). Em outras palavras, o manual existe, mas grande parte de suas instruções é insuficiente para orientar quem precisa operar, integrar, auditar ou evoluir o sistema. Em termos de maturidade, a situação é **Ad-hoc (0)**: as descrições existem mas não cumprem a função de interpretação autônoma.

**Tabela 8** — Exemplos de descrições atuais e do conteúdo semântico que deveriam conter

| Campo | Descrição atual no dicionário | O que deveria conter |
|---|---|---|
| `id_area_imovel` | "ID de identificação de área imóvel" | Identificador único da área do imóvel vinculada à unidade familiar e usado para relacionamento entre tabelas |
| `nr_area` | "Tamanho da área imóvel" | Área do imóvel rural em hectares (ha), com precisão definida e uso associado à verificação do limite legal |
| `nr_latitude` | "Latitude da área imóvel" | Latitude em graus decimais, com indicação do datum geodésico adotado |
| `dt_criacao` | "Data criação" | Data e hora de criação técnica do registro no banco de dados, distinta de eventos de negócio |
| `dt_atualizacao` | "Data atualização" | Data e hora da última atualização técnica do registro, com distinção em relação a vigência cadastral |
| `vl_renda_auferida` | "Valor renda auferida" | Valor da renda familiar auferida no período de referência, em reais (R$), conforme regra de negócio aplicável |

*Fonte: elaboração da equipe de auditoria com base nas peças 75, 78, 133 e 136.*

##### Dimensão 2 — Vinculação ao marco regulatório

113. O dicionário de dados do CAF não mapeia campos para os dispositivos legais que os fundamentam. Na prática, isso significa que a rastreabilidade entre dado e norma é inexistente no artefato de metadados. O campo `nr_modulo_fiscal`, por exemplo, existe porque o art. 3º, I, da Lei 11.326/2006 define o limite de 4 módulos fiscais como requisito de elegibilidade, mas o dicionário não registra essa vinculação. Os campos de renda existem por força do art. 3º, V, da mesma Lei (predominância de renda familiar), mas o dicionário não documenta qual critério legal cada campo operacionaliza. A Portaria MDA 19/2025 define 14 tipos documentais aceitos para comprovação de posse ou propriedade (art. 8º, I, c), mas o dicionário não mapeia quais campos implementam essas categorias nem quais regras de negócio as operacionalizam.

114. A ISO/IEC 11179 trata a "fonte autoritativa" como atributo obrigatório de cada elemento de dados: para cada campo, deve ser possível identificar qual norma justifica sua existência. O DAMA-DMBOK complementa ao tratar a linhagem de dados como função que inclui a rastreabilidade até a regra de negócio originária.

115. O impacto dessa lacuna é prospectivo: quando a norma muda, como ocorreu na transição da Portaria 20/2023 para a 19/2025, não há mapa para saber quais campos, tabelas e regras de negócio precisam ser revisados. Em termos de maturidade, a situação é **Ad-hoc (0)**: não há mapeamento campo→norma no dicionário.

##### Dimensão 3 — Clareza do modelo conceitual

116. O modelo entidade-relacionamento (MER) técnico do CAF existe (peça 76) e documenta as 109 tabelas do banco de dados com suas chaves primárias e estrangeiras. Trata-se, porém, de diagrama técnico de banco de dados, não de modelo conceitual de negócio legível por gestores, auditores ou equipes novas. A camada de abstração que explicaria, em linguagem acessível, as relações entre os conceitos centrais do cadastro (como UFPA se relaciona com imóvel, como imóvel se relaciona com documento, como responsável se vincula a UFPA, como o ciclo de vida de uma inscrição ativa→suspensa→inativa se reflete nas tabelas) não está formalizada em artefato autônomo.

117. O DAMA-DMBOK trata o modelo conceitual como ponte entre regras de negócio e implementação técnica: sem ele, apenas quem conhece o código-fonte ou já trabalhou com o sistema compreende as relações entre entidades. A ISO/IEC 11179 complementa ao exigir que o registro de metadados documente relacionamentos entre elementos de dados, não apenas definições isoladas. A consequência prática é que um novo desenvolvedor, auditor ou gestor que receba o MER técnico e o dicionário atual não consegue reconstruir a lógica do CAF sem orientação presencial de quem já conhece o sistema, reforçando a dependência de conhecimento tácito identificada como efeito potencial central deste achado. Em termos de maturidade, a situação é **Inicial (1)**: o MER técnico existe e é funcional, mas a camada conceitual de negócio está ausente.

##### Dimensão 4 — Completude de unidades de medida

118. Dos 125 campos numéricos identificados no dicionário, 105 (84%) não especificam unidade de medida (peça 136, p. 4-5). A ausência é particularmente crítica em campos como `nr_area` (hectares? alqueires? m²?), coordenadas geográficas (sem datum), e campos monetários (reais? centavos? mensal? anual?). Sem essa especificação, a interpretação dos dados depende de quem já conhece o sistema. A ISO/IEC 11179 trata a unidade de medida como atributo obrigatório para elementos numéricos. Em termos de maturidade, a situação é **Ad-hoc (0)**: o template do dicionário sequer prevê campo para registrar unidade.

##### Dimensão 5 — Precisão temporal

119. Dos 87 campos temporais, 80 (92%) são ambíguos quanto ao evento que registram (peça 133, p. 5). Campos como `dt_criacao` e `dt_atualizacao` não distinguem se se referem à criação técnica do registro, ao evento de negócio subjacente ou à aprovação administrativa. A ISO/IEC 11179 exige que definições distinguam univocamente entre elementos similares. Em termos de maturidade, a situação é **Ad-hoc (0)**: sem distinção formal entre tipos de data.

##### Dimensão 6 — Integração ao ciclo de desenvolvimento

120. O dicionário foi produzido e mantido, em grande medida, como documentação posterior ao desenvolvimento, sem enriquecimento semântico sistemático (peça 150, p. 59-60). O resultado natural de documentação post mortem é a descrição tautológica: registra-se o nome do campo, mas não seu significado de negócio. Quando o esquema do banco muda (nova coluna, nova tabela, nova regra), o dicionário não é obrigatoriamente atualizado. Não há registro de quando uma definição mudou, quem mudou nem por quê. O COBIT 2019 (BAI10) trata a gestão de configuração como função que exige documentação sincronizada com mudanças no sistema. Em termos de maturidade, a situação é **Ad-hoc (0)**: sem processo formal de manutenção.

##### Dimensão 7 — Governança e data stewardship de metadados

121. A gestão de metadados ainda não está plenamente integrada ao ciclo de vida do sistema como artefato obrigatório de mudança, com responsáveis, padrões mínimos e revisão contínua. O dicionário permanece em formato estático, desvinculado de processo robusto de controle de versão semântica (peça 150, p. 57-60). Não há dono formal do dicionário (data steward de metadados), nem comitê ou processo para arbitrar definições conflitantes, nem métricas de qualidade do próprio dicionário. O gestor concordou expressamente que a governança de dados do órgão ainda está em processo de maturação (peça 150, p. 53). O DAMA-DMBOK trata a governança de dados como função que exige papéis formalizados para cada domínio, incluindo metadados (Cap. 4, peça 86). Em termos de maturidade, a situação é **Ad-hoc (0)**: sem papéis formalizados.

**Quadro 10** — Maturidade da gestão de metadados do CAF

| Dimensão (referencial) | Indicador-chave | Prática observada | Nível |
|---|---|---|---|
| Riqueza semântica (ISO 11179) | 94,1% tautológicas (496/527) | Descrições existem mas não permitem interpretação autônoma | Ad-hoc (0) |
| Vinculação ao marco regulatório (ISO 11179 / DAMA-DMBOK) | 0% de campos com mapeamento campo→norma | Dicionário não registra qual dispositivo legal fundamenta cada campo | Ad-hoc (0) |
| Clareza do modelo conceitual (DAMA-DMBOK / ISO 11179) | MER técnico existe; modelo conceitual de negócio ausente | Relações entre entidades legíveis apenas por quem conhece o código | Inicial (1) |
| Unidades de medida (ISO 11179) | 84% sem unidade (105/125) | Template do dicionário não prevê campo para unidade | Ad-hoc (0) |
| Precisão temporal (ISO 11179) | 92% ambíguos (80/87) | Sem distinção criação/atualização/vigência | Ad-hoc (0) |
| Integração ao desenvolvimento (COBIT BAI10) | Documentação post mortem | Sem versionamento nem sincronização com mudanças | Ad-hoc (0) |
| Governança/stewardship (DAMA-DMBOK Cap. 4) | Sem dono formal | Papéis não formalizados; gestor reconhece maturidade incipiente | Ad-hoc (0) |
| **Média aritmética** | | Estágio predominantemente reativo, com alicerce estrutural parcial | **0,14** |

*Escala de maturidade adaptada do DAMA-DMBOK v2 (Caps. 4, 12) e do CMMI-DMM: 0 = Ad-hoc (sem processo formal); 1 = Inicial (processo existente, não repetível); 2 = Repetível; 3 = Definido; 4 = Gerenciado; 5 = Otimizado. A ISO/IEC 11179 define o conteúdo que os metadados deveriam ter (nomes, definições, unidades, domínios, fontes autoritativas); a escala de maturidade avalia o grau de institucionalização desse conteúdo. As dimensões combinam requisitos de conteúdo (ISO 11179), de processo (COBIT BAI10) e de governança (DAMA-DMBOK), conforme indicado entre parênteses no quadro.*

*Fonte: elaboração da equipe de auditoria com base nas peças 75, 76, 78, 84, 86, 132-136 e 150.*

**Nota sobre cobertura vs. maturidade:** A cobertura de 100% das tabelas não se traduz em nível Inicial para a maioria das dimensões porque cobertura e maturidade medem coisas distintas. É como uma biblioteca que tem 100% dos livros catalogados, mas sem sistema de busca, classificação ou indexação: a presença dos livros (cobertura) não garante que se possa encontrá-los e usá-los (maturidade). No caso do CAF, os 527 campos estão listados no dicionário, mas 94,1% das descrições não explicam o significado do dado, ou seja, o "catálogo" existe mas não cumpre sua função. A cobertura é o alicerce sobre o qual a melhoria pode ser construída; a avaliação de maturidade mede o quanto o dicionário já funciona como instrumento de governança.

**Nota comparativa:** a maturidade de metadados (0,14) é a mais baixa entre os 4 achados (ACH-01: 0,43; ACH-02: 0,20; ACH-03: 0,40). A comparação é indicativa, não absoluta: os quadros avaliam dimensões distintas. A posição reflete o fato de que a camada mais fundamental, a que explica o que os dados significam, é a que recebeu menos atenção formal, apesar de o dicionário existir e cobrir 100% do esquema. A única dimensão acima do nível ad-hoc é a clareza do modelo conceitual, onde o MER técnico já existe como alicerce parcial.

### {SS} Conexão transversal: por que metadados são o alicerce dos 4 achados

122. Este achado é, em larga medida, um achado-plataforma. As melhorias propostas para documentos comprobatórios, georreferenciamento e dados cadastrais exigem saber, com precisão, o que cada campo representa. Sem isso, validações automáticas podem incidir sobre o atributo errado, integrações com bases oficiais podem ser mapeadas de forma equivocada e o monitoramento contínuo da qualidade fica dependente de engenharia reversa. A tabela abaixo explicita como as insuficiências de metadados afetam cada achado anterior.

**Tabela 9** — Conexão transversal: como metadados inadequados afetam os achados anteriores

| Achado | Fragilidade | Vínculo com metadados |
|---|---|---|
| **ACH-01** — 53,55% divergência de área | Campo `nr_area` sem unidade de medida | Parte das divergências pode decorrer de conversão implícita entre hectares, alqueires e m² |
| **ACH-01** — 33,33% tipo documental inadequado | Dicionário não mapeia quais tipos a Portaria 19/2025 aceita | Sem vinculação campo→norma, a validação tipo-documental não pode ser automatizada |
| **ACH-02** — 15,92% fora do município | Coordenadas sem datum geodésico no dicionário; modelo conceitual não explicita relação coordenada→município | A inconsistência municipal pode ser compreendida como falha de modelo, não apenas como dado errado |
| **ACH-02** — Transições sem regressão | Sem versionamento de metadados | Não há registro de como o esquema mudou entre DAP→CAF 2.0→3.0; sem modelo conceitual, as relações alteradas nas migrações ficam opacas |
| **ACH-03** — 3.097 falecidos ativos | Campos temporais ambíguos (92%) | A data de referência para detectar obsolescência não está documentada |
| **ACH-03** — 907 renda > R$1M | Campo `vl_renda` sem unidade | Impossível implementar regra de plausibilidade sem saber se o valor é mensal, anual, em reais ou centavos |

*Fonte: elaboração da equipe de auditoria com base na análise transversal dos achados e nos referenciais ISO/IEC 11179:2015 e DAMA-DMBOK v2.*

123. Se o dicionário de dados documentasse adequadamente o significado de cada campo, sua unidade de medida e suas relações com outros campos, as validações propostas nos ACH-01, ACH-02 e ACH-03 poderiam ser implementadas como regras de negócio automatizadas, e não como verificações manuais dependentes de quem já conhece o sistema. O ACH-04, portanto, não é apenas mais um achado: é o habilitador transversal cuja resolução potencializa todas as demais melhorias.

### {SS} Efeitos potenciais

124. Essa lacuna semântica projeta efeitos potenciais relevantes. O primeiro é a limitação da interpretação autônoma dos dados. Se o campo `nr_area` não informa sua unidade, a implementação de validações de área, como as discutidas nos achados anteriores, depende de conhecimento tácito sobre o que o sistema "quer dizer" com aquele valor. Se um campo temporal como `dt_cadastro` ou `dt_atualizacao` não distingue evento de sistema, vigência ou atualização de negócio, a curadoria de registros desatualizados, cancelados ou herdados de versões anteriores torna-se menos confiável. O segundo efeito potencial é a concentração de conhecimento crítico em poucos indivíduos. Quando o significado dos campos não está suficientemente formalizado, ele se preserva por meio da memória dos técnicos mais antigos, e não por documentação institucional durável.

125. O terceiro efeito potencial é o aumento do risco de erro silencioso em integrações, consultas analíticas e manutenção evolutiva. Sistemas externos e equipes novas podem consumir a mesma coluna com premissas diferentes sem perceber a divergência. O quarto efeito potencial é a limitação da auditabilidade futura do CAF. Um sistema relevante para políticas públicas não pode exigir, a cada nova fiscalização, consultas reiteradas aos seus "intérpretes autorizados" para explicar o que cada dado significa.

### {SS} Causas

126. As causas ajudam a entender por que o manual de instruções chegou a esse ponto. A primeira é que o dicionário foi produzido e mantido, em grande medida, como documentação posterior ao desenvolvimento, sem enriquecimento semântico sistemático. O resultado natural de documentação post mortem é a descrição tautológica: registra-se o nome do campo, mas não seu significado de negócio. A segunda é a fragmentação do conhecimento entre o dicionário de dados e o Documento de Regras de Negócio. A peça 78 contém definições úteis, inclusive exemplos de unidades de medida e regras materiais, mas essas informações não foram vinculadas campo a campo ao artefato consultado por quem tenta entender a estrutura do banco. Assim, o conhecimento existe, porém espalhado.

127. A terceira causa é que a gestão de metadados ainda não está plenamente integrada ao ciclo de vida do sistema como artefato obrigatório de mudança, com responsáveis, padrões mínimos e revisão contínua. O dicionário permanece em formato estático, desvinculado de processo robusto de controle de versão semântica. A quarta é a limitação do próprio template documental, que não favorece o registro estruturado de unidade de medida, datum geodésico, domínio de valores e natureza do evento temporal. Essas causas foram agravadas por fatores contribuintes adequadamente descritos no contraditório: pressão operacional, dívida técnica acumulada ao longo das transições do CAF, reconstrução institucional do MDA e priorização legítima de entregas funcionais em detrimento da documentação. O gestor reconheceu essa moldura como problema qualitativo de maturidade, não como vazio absoluto de governança, e acolheu expressamente a recomendação correspondente (peça 150, p. 57-60 e 71).

### {SS} Boas práticas

128. No plano das boas práticas, a equipe não identificou experiência que atendesse cumulativamente aos critérios da NAT §160. Houve, contudo, avanços parciais relevantes. O primeiro é a cobertura integral das 95 tabelas em uso pelo dicionário, o que fornece base concreta para melhoria incremental em vez de reconstrução do zero. O segundo é a existência de 31 campos com descrição funcional adequada, benchmark interno que demonstra viabilidade técnica imediata. O terceiro é o próprio acolhimento, pelo gestor, de implementação progressiva e integrada à gestão de mudanças. Esses pontos não convertem o caso em boa prática formal, mas mostram que o sistema já dispõe de alicerces institucionais para amadurecer a gestão de metadados.

### {SS} Propostas de encaminhamento

129. Os encaminhamentos, por isso, devem preservar liberdade de meios e concentrar-se no resultado a alcançar. A determinação transversal de apresentação de plano de ação em 180 dias é pertinente também para este achado, porque permite ao gestor organizar, por risco e criticidade, a revisão do passivo documental e a consolidação de critérios mínimos de metadados. Especificamente para o ACH-04, a Proposta 2.4 responde de forma direta ao problema identificado: aprimorar a gestão de metadados do CAF, assegurando definições semânticas documentadas, alinhadas às regras de negócio e ao marco legal, com responsabilidades atribuídas e atualização integrada ao ciclo de vida do sistema. Não se está impondo ferramenta única, modelo fechado ou saneamento massivo imediato; define-se, isto sim, a necessidade de que o manual do sistema passe a explicar, de modo verificável, o que seus dados significam.

**Quadro 11** — Síntese do Achado 04

| Componente | Síntese |
|---|---|
| Situação encontrada | Dicionário de dados com 94,1% de descrições inadequadas, 84% de campos numéricos sem unidade de medida e 92% de campos temporais ambíguos, apesar de cobertura formal de 100% das 95 tabelas em uso |
| Critério | ISO/IEC 11179 ²⁵, DAMA-DMBOK v2, Decreto 10.046/2019 ²⁶, COBIT 2019 ²⁷ e referenciais de governança de dados adotados pelo TCU |
| Efeitos potenciais | Limitação da interpretação autônoma, concentração de conhecimento tácito, risco de erro em integrações e perda de sustentabilidade das melhorias recomendadas nos achados anteriores |
| Causas principais | Documentação post mortem, fragmentação entre dicionário e regras de negócio, metadados fora do ciclo de desenvolvimento e template sem campos estruturais suficientes |
| Propostas associadas | Plano de ação em 180 dias e aprimoramento da gestão de metadados do CAF com atualização contínua e responsabilidades definidas |

*Fonte: elaboração da equipe de auditoria com base na Matriz de Achados do CAF e nas peças 75, 78, 132, 133, 134, 135, 136 e 150.*

### {SS} Benefícios esperados

130. Os benefícios esperados são concretos e estruturantes. Em primeiro lugar, espera-se reduzir progressivamente a taxa de 94,1% de descrições inadequadas, especificar unidade para os 105 campos numéricos sem essa informação e eliminar a ambiguidade dos 80 campos temporais cuja semântica ainda é incerta. Em segundo lugar, espera-se diminuir a dependência de conhecimento tácito, preservando institucionalmente informações hoje dispersas entre documentos e memória de equipes. Em terceiro lugar, espera-se ampliar a auditabilidade e a interoperabilidade do CAF.

131. Sobretudo, espera-se dar sustentação às melhorias dos demais achados: corrigir a porta documental do cadastro, a coerência territorial dos imóveis e a curadoria dos registros cadastrais exige saber com precisão o que cada campo representa. Se o ACH-01 tratou do que entra no sistema, o ACH-02 do lugar onde o cadastro se ancora e o ACH-03 da consistência das pessoas e vínculos registrados, o ACH-04 trata da linguagem comum que torna essas correções duráveis. Para a sociedade, o ganho final é um CAF menos opaco, mais auditável e preparado para sustentar, com continuidade, políticas públicas voltadas à agricultura familiar.

---

## Notas de Fim (Apêndice VI)

²⁵ INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. ISO/IEC 11179-1:2015 — Information technology — Metadata registries (MDR) — Part 1: Framework. Geneva: ISO, 2015.

²⁶ BRASIL. Decreto nº 10.046, de 9 de outubro de 2019. Dispõe sobre a governança no compartilhamento de dados no âmbito da administração pública federal. Brasília: Presidência da República, 2019.

²⁷ ISACA. COBIT 2019 Framework: Governance and Management Objectives. Schaumburg: ISACA, 2018. BAI10 — Managed Configuration.
