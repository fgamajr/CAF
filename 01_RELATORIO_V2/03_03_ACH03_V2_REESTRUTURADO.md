## {S} ACHADO 03

**Lacunas na governança, no cadastramento e na curadoria dos dados comprometem a qualidade cadastral do CAF, dificultando comunicação com os cadastrados e elevando riscos de focalização das políticas públicas de agricultura familiar**

83. A auditoria concluiu que a qualidade cadastral do CAF permanece limitada por lacunas convergentes de governança, cadastramento, curadoria e interoperabilidade com bases oficiais. O problema não reside, em regra, na ausência de preenchimento formal dos campos, mas na aceitação de dados sintaticamente válidos sem verificação suficiente de seu conteúdo semântico, funcionalidade ou plausibilidade. Nesse contexto, permanecem ativos 3.097 responsáveis com óbito confirmado no Sisobi (peça 124, p. 9), 138 menores figuram como titulares de unidades familiares (peça 124, p. 8), 90,62% dos e-mails de pessoas físicas são fictícios ou inválidos (peça 125, p. 6), 93,7% dos CEPs são genéricos (peça 125, p. 1), 907 registros informam renda anual superior a R$ 1 milhão (peça 130, p. 3) e 39 pessoas jurídicas apresentam CNAE principal manifestamente incompatível com a agricultura familiar (peça 127, p. 5).

84. Esse quadro pode limitar a capacidade do CAF de manter vínculo atualizado com o público real da política, aumentar o custo operacional de controle e reduzir a precisão da focalização de políticas públicas que, só no Pronaf, movimentaram R$ 59,6 bilhões na safra 2023/2024.

### {SS} O CAF como cadastro de pessoas

85. Antes de ser um acervo de documentos ou um conjunto de coordenadas, o CAF é um cadastro de pessoas. Sua função legal, definida pelo art. 4º do Decreto 9.064/2017, é identificar e qualificar o público da agricultura familiar. Para isso, os dados pessoais, econômicos e cadastrais dos responsáveis e das pessoas jurídicas vinculadas precisam refletir realidade minimamente verificável: o titular precisa existir e ser civilmente capaz, os canais de contato precisam funcionar e os dados de renda e atividade precisam ser plausíveis. Foi justamente nesse ponto que a auditoria identificou o conflito central do ACH-03. O sistema verifica formato e sintaxe elementar com mais eficácia do que verifica se o dado informado é verdadeiro, funcional e coerente com a finalidade do cadastro.

86. A análise que se segue organiza as constatações em torno de aspectos como validade dos dados (o dado reflete a realidade?), atualidade (o dado está corrente?), completude funcional (o campo preenchido cumpre sua função?) e credibilidade (o dado é plausível?), em linha com práticas de qualidade de dados e de curadoria de dados mestres descritas na ISO/IEC 25012:2008 e no DAMA-DMBOK v2 (Caps. 4, 9 e 13, peça 86).

#### {SSS} Situação encontrada por dimensão

##### Capacidade civil dos responsáveis

87. A primeira dimensão desse conflito é a capacidade civil dos responsáveis. O cruzamento censitário de 2.905.101 responsáveis ativos (peça 124, p. 8) com bases oficiais identificou 15.811 inconsistências de capacidade civil, das quais 3.097 correspondem a óbitos confirmados simultaneamente na Receita Federal e no Sisobi (peça 124, p. 9), critério conservador adotado para mitigar falsos positivos. Somam-se a esse conjunto 89 menores de 16 anos, 49 adolescentes de 16 a 17 anos não emancipados, 11.999 divergências de data de nascimento em relação à base da Receita Federal (peça 124, p. 10), 520 CPFs não localizados e 57 registros com datas de nascimento futuras (peça 124, p. 8).

88. A baixa materialidade relativa do bloco, inferior a 1% da base, não elimina sua relevância qualitativa. À luz dos arts. 3º, 4º e 6º do Código Civil²⁴, manter responsáveis falecidos ou incapazes em posição ativa não significa, por si, benefício indevido consumado, mas revela limitação sensível na curadoria de dados críticos de identificação.

89. A própria distribuição temporal dos óbitos reforça o caráter acumulativo do passivo: 20,8% ocorreram entre 2010 e 2015, 39,5% entre 2016 e 2020 e 39,7% entre 2021 e 2025 (peça 124, p. 9).

**Tabela 5** — Síntese das principais inconsistências cadastrais do ACH-03

| Dimensão | Indicador | Resultado |
|---|---|---:|
| Capacidade civil | Responsáveis com óbito confirmado no Sisobi | 3.097 |
| Capacidade civil | Menores como titulares de UFPAs | 138 |
| Dados de contato | E-mails de PF fictícios ou inválidos | 90,62% |
| Dados de contato | CEPs genéricos | 93,7% |
| Consistência de renda | Registros com renda anual superior a R$ 1 milhão | 907 |
| Atividade econômica | PJs com CNAE principal incompatível | 39 |

*Fonte: elaboração da equipe de auditoria com base nas peças 124, 125, 127, 130 e 150.*

##### Comunicação com o público cadastrado

90. A segunda dimensão é a capacidade de comunicação com o público cadastrado. Em uma base de 6.525.658 e-mails de pessoas físicas (peça 125, p. 6), apenas 9,38% eram utilizáveis para comunicação eletrônica; os demais 90,62% revelaram-se fictícios ou inválidos. O padrão dominante não é residual: 4.904.403 registros, equivalentes a 75,16% da população (peça 125, p. 6), repetem o valor `naopossui@mail.com`, sinal de preenchimento formal sem utilidade operacional. O contraste com as pessoas jurídicas é eloquente: 99,70% dos e-mails de PJ são válidos (peça 125, p. 7). A diferença de 90,32 pontos percentuais (peça 125, p. 8) mostra que o problema não decorre de incapacidade técnica do sistema, mas da forma como o campo é tratado no cadastramento das pessoas físicas. Fenômeno semelhante aparece nos endereços postais: 93,7% dos CEPs são genéricos, terminados em `000`.

**Tabela 6** — Padrões de invalidade dos e-mails de pessoas físicas

| Padrão | Quantidade | % dos e-mails inválidos |
|---|---:|---:|
| `naopossui@mail.com` | 4.904.403 | 82,9% |
| Sem `@` | 387.456 | 6,6% |
| Domínios fictícios (`@teste.com`, `@exemplo.com`) | 298.712 | 5,1% |
| E-mails temporários (`@10minutemail.com`) | 187.234 | 3,2% |
| Outros padrões inválidos | 135.854 | 2,3% |
| Total de e-mails inválidos | 5.913.659 | 100,0% |

*Fonte: elaboração da equipe de auditoria com base na peça 125, p. 6.*

##### Exclusão digital: lacunas de representação cadastral no meio rural

91. Esses dados de contato, contudo, exigem leitura cuidadosa. O contraditório demonstrou, de forma procedente, que o público do CAF convive com exclusão digital relevante: aproximadamente dois terços das pessoas inscritas possuem baixa escolaridade, o uso de correio eletrônico é limitado no meio rural e a preferência recai sobre aplicativos de mensagem como WhatsApp. O gestor também mostrou que existem 1.469 municípios brasileiros com apenas um CEP genérico (peça 150, p. 49-50), o que explica parte relevante da repetição de códigos postais. Esse contexto afasta leitura de negligência massiva do beneficiário ou da rede emissora. Ainda assim, o problema funcional permanece: um cadastro que não consegue contatar parcela expressiva de seu público reduz a capacidade do Estado de informar renovação, pendências, suspensões, chamamentos ou alterações normativas.

##### Consistência econômica

92. A terceira dimensão envolve a consistência econômica dos dados declarados. A análise censitária de 3.304.174 UFPAs ativas encontrou 907 registros com renda anual superior a R$ 1 milhão, dos quais 141 ultrapassam R$ 10 milhões (peça 130, p. 3; peça 126, p. 25). O caso extremo supera R$ 167 milhões anuais. O ponto exige contenção analítica. O gestor tem razão ao afirmar que a Lei 11.326/2006 não estabelece teto geral de renda bruta para inscrição no CAF; o critério legal recai sobre a composição da renda, e não sobre seu valor absoluto. Ainda assim, valores dessa magnitude funcionam como indício robusto de risco cadastral e de insuficiência de plausibilidade na entrada.

93. As hipóteses mais prováveis são erro de unidade, digitação sem separador decimal, acumulação de períodos distintos ou confusão entre renda familiar e faturamento de outra natureza. A regra RN1.32 opera como filtro de classificação para políticas específicas (peça 78), mas não impede a gravação de valores manifestamente implausíveis na base principal do CAF.

##### Compatibilidade de atividade econômica

94. A quarta dimensão é a compatibilidade da atividade econômica das pessoas jurídicas cadastradas. O cruzamento com a base da Receita Federal identificou 39 PJs, entre 9.687 registros, com CNAE principal manifestamente incompatível com a agricultura familiar: 17 hipermercados, 8 atacadistas, 4 construtoras e 10 entidades de outras atividades urbanas (peça 127, p. 5). Embora pequenas em número absoluto, essas entidades concentram 10.377 agricultores vinculados, inclusive um caso extremo com 1.847 agricultores vinculados a um hipermercado (peça 127, p. 5-6). Também aqui o contraditório trouxe calibragem necessária.

95. O Decreto 9.064/2017 admite, além da produção agropecuária, atividades de beneficiamento, processamento, comercialização e turismo rural. Por isso, o CNAE não pode ser tratado como filtro autoexecutável de inelegibilidade. Ainda assim, hipermercados, atacadistas e construtoras destoam frontalmente das finalidades próprias da agricultura familiar e devem acionar mecanismos de triagem e verificação individualizada.

**Quadro 8** — Maturidade da qualidade cadastral do CAF

| Dimensão (referencial) | Indicador-chave | Prática observada | Nível |
|---|---|---|---|
| Validade civil (ISO 25012 / Código Civil) | 3.097 falecidos + 138 menores | CAF 3.0 veda menores; cruzamento Sisobi inexistente para estoque | Inicial (1) |
| Funcionalidade dos canais de contato (ISO 25012) | 90,62% e-mails fictícios; 93,7% CEPs genéricos | Validação sintática sem verificação funcional; exclusão digital do público como fator contribuinte | Ad-hoc (0) |
| Plausibilidade econômica (DAMA-DMBOK / ISO 25012) | 907 rendas > R$ 1 milhão | RN1.32 classifica mas não impede gravação de valores implausíveis | Ad-hoc (0) |
| Compatibilidade de atividade (DAMA-DMBOK) | 39 PJs com CNAE incompatível | Consulta RFB sem filtro de CNAE na entrada | Inicial (1) |
| Curadoria e interoperabilidade (DAMA-DMBOK, Caps. 4, 9, 13) | Passivo sem saneamento estruturado | Avanços pontuais (BCadastro, vedação menores); governança declaradamente imatura (peça 150, p. 53) | Ad-hoc (0) |
| **Média aritmética** | | Estágio entre práticas reativas e primeiros controles prospectivos | **0,40** |

*Escala adaptada pela equipe com base no DAMA-DMBOK v2, Caps. 4, 9 e 13, CMMI-DMM e ISO/IEC 25012:2008: 0 = Ad-hoc (sem processo formal); 1 = Inicial (processo existente, não repetível); 2 = Repetível; 3 = Definido; 4 = Gerenciado; 5 = Otimizado. Trata-se de escala analítica adaptada, não de aplicação literal da taxonomia de nenhum desses referenciais.*

*Fonte: elaboração da equipe de auditoria com base nas peças 124, 125, 127, 130, 150, nos referenciais ISO/IEC 25012:2008, DAMA-DMBOK v2 (Caps. 4, 9, 13) e CMMI-DMM.*

**Nota comparativa:** a média de maturidade cadastral (0,40) é equivalente à de dados de entrada do ACH-01 (0,43) e superior à geoespacial do ACH-02 (0,20). A comparação é indicativa, não absoluta: os quadros utilizam a mesma escala, mas avaliam dimensões distintas. A proximidade entre ACH-01 e ACH-03 reflete os avanços já implementados no CAF 3.0 para validação de capacidade civil e consulta à Receita Federal. A única dimensão acima do nível ad-hoc é a validade civil, onde o CAF 3.0 já veda menores, e a compatibilidade de atividade, onde já há consulta à RFB.

### {SS} Efeitos potenciais

96. Os efeitos desse conjunto de inconsistências são potenciais e precisam ser descritos com moderação. O primeiro é o risco de comprometimento da focalização das políticas públicas. A manutenção de 3.097 responsáveis com óbito confirmado e de 138 menores como titulares ativos não significa, automaticamente, 3.235 acessos indevidos a benefícios. O CAF é condição necessária, mas não suficiente, para acesso às políticas usuárias. Ainda assim, a permanência desses registros na base ativa pode dificultar a distinção tempestiva entre o público efetivamente elegível e situações que exigem saneamento, sobretudo em políticas de grande escala. O segundo efeito potencial é a redução da capacidade de comunicação com os cadastrados. Se 90,62% dos e-mails de pessoas físicas são inválidos e 93,7% dos CEPs são genéricos, o Estado passa a depender de canais menos estruturados, mais caros ou menos tempestivos para alcançar o público da política.

97. O terceiro efeito potencial é o aumento do custo operacional e da complexidade de controle para gestores e executores. Quanto mais o sistema tolera inconsistências não saneadas, mais a verificação migra da regra de negócio para a análise manual e da prevenção para a checagem posterior. O quarto efeito potencial é a redução da confiabilidade analítica dos dados de renda e de atividade econômica. Registros extremos de renda e vínculos com CNAEs incompatíveis não provam, isoladamente, inadequação ao CAF, mas distorcem indicadores agregados e podem induzir decisões menos precisas de monitoramento e priorização. Em todos esses casos, o achado permanece no plano da governança e da qualidade cadastral: a auditoria não identificou dano consumado ao erário, fraude demonstrada ou exclusão efetiva de beneficiários legítimos decorrente apenas dessas inconsistências.

### {SS} Causas

98. As causas explicam por que o problema persiste em blocos diferentes, mas com lógica comum. A primeira é a ausência de cruzamento periódico automatizado com a base de óbitos, o que permitiu que registros de falecimento se acumulassem por mais de uma década sem rotina estruturada de limpeza. A segunda é a aceitação de dados de contato sem validação funcional: o sistema verifica se o e-mail tem aparência de e-mail, não se o endereço cumpre a função de comunicação. A terceira é a ausência de regras de plausibilidade e curadoria para campos econômicos e cadastrais sensíveis, como renda e CNAE. A quarta é a inexistência de rotina sistemática de saneamento do passivo herdado, o que faz com que avanços prospectivos do CAF 3.0 não retroajam sobre a base preexistente.

99. A quinta é a insuficiência na formalização da política de governança de dados, ponto em que o próprio gestor concordou expressamente com a equipe de auditoria (peça 150, p. 53). E a sexta é a reincidência: desde o Acórdão 1197/2018, o Tribunal já apontava a necessidade de validação, interoperabilidade e curadoria mais robustas para o cadastro que sucederia a DAP.

### {SS} Fatores contribuintes e avanços reconhecidos

100. Os fatores contribuintes ajudam a qualificar a resposta, sem descaracterizar o achado. A exclusão digital do público rural, a estrutura precária do endereçamento postal em milhares de municípios e a não utilização uniforme do CPF como chave primária em sistemas públicos ajudam a explicar por que certos erros se acumulam e por que a solução não pode ser desenhada como saneamento cego e massivo. Também houve avanços relevantes: o CAF 3.0 já consulta a Receita Federal via BCadastro/ConectaGOV (peça 150, p. 48), passou a vedar responsabilidade por UFPA a menores e o gestor informou providências em curso, como a formação de mais de 10 mil agentes da RedeCAF para 2026 e testes de comunicação pela plataforma Gov.br. Esses elementos afastam leitura de inércia, mas confirmam que os controles ainda não cobrem o estoque ativo.

### {SS} Boas práticas

101. No plano das boas práticas, a equipe não identificou experiência que atendesse cumulativamente aos requisitos da NAT §160 para ser formalmente classificada nessa condição. O que se observou foram avanços parciais, úteis para calibrar o tom do achado e a proporcionalidade dos encaminhamentos. Entre eles estão os controles de capacidade civil já incorporados ao CAF 3.0, a retirada da obrigatoriedade de e-mail para pessoas físicas, coerente com a realidade do público rural, e o reconhecimento expresso, pelo gestor, de que a governança de dados do órgão ainda está em processo de maturação. Esses avanços demonstram capacidade de reação, mas não bastam para transformar o caso em referência replicável a outros órgãos.

### {SS} Propostas de encaminhamento

102. Os encaminhamentos, por isso, devem combinar saneamento seletivo do passivo e fortalecimento prospectivo do sistema. A determinação transversal de apresentação de plano de ação em 180 dias permanece adequada para avaliar as situações identificadas e, uma vez confirmadas, promover seu saneamento com critérios de risco, materialidade e verificabilidade. No plano das recomendações, a Proposta 2.1.1 responde à prevenção na entrada; a Proposta 2.1.2, à integridade dos campos críticos; a Proposta 2.1.3, à interoperabilidade com bases oficiais relevantes, especialmente para detecção tempestiva de óbitos e outras inconsistências; e a Proposta 2.3, ao monitoramento contínuo da qualidade dos dados. Todas definem resultados a alcançar, não soluções fechadas, preservando a liberdade de meios do gestor.

**Quadro 9** — Síntese do Achado 03

| Componente | Síntese |
|---|---|
| Situação encontrada | 3.097 falecidos, 138 menores como titulares, 90,62% de e-mails de PF inválidos, 93,7% de CEPs genéricos, 907 rendas acima de R$ 1 milhão e 39 PJs com CNAE incompatível |
| Critério | Lei 11.326/2006, art. 3º; Decreto 9.064/2017, arts. 2º e 4º; Portaria MDA 19/2025, arts. 27 e 28; Código Civil²⁴; DAMA-DMBOK v2 |
| Efeitos potenciais | Risco de focalização imprecisa, limitação da comunicação com cadastrados, aumento do custo operacional de controle e distorção analítica de dados cadastrais |
| Causas principais | Ausência de cruzamento periódico com bases de óbito, validação apenas sintática de e-mail, falta de plausibilidade para renda e CNAE, passivo sem saneamento estruturado e governança de dados ainda imatura |
| Propostas associadas | Plano de ação em 180 dias, prevenção na entrada, integridade de dados críticos, interoperabilidade com bases oficiais e monitoramento contínuo |

*Fonte: elaboração da equipe de auditoria com base na Matriz de Achados do CAF e nas peças 124, 125, 127, 130, 150, 156 e 162.*

### {SS} Benefícios esperados

103. Os benefícios esperados são concretos e mensuráveis. Em primeiro lugar, espera-se o saneamento progressivo dos 3.097 cadastros com titulares falecidos confirmados no Sisobi e dos 138 cadastros com menores como titulares, com priorização a ser definida pelo gestor no plano de ação. Em segundo lugar, espera-se melhorar a capacidade de comunicação com o público do cadastro, reduzindo a dependência de dados não funcionais e adaptando os canais de contato à realidade do meio rural. Em terceiro lugar, espera-se elevar a confiabilidade dos campos de renda e atividade econômica, reduzindo o estoque de outliers e de vínculos manifestamente incompatíveis.

104. Em quarto lugar, espera-se reduzir o custo operacional de controle ao deslocar o esforço institucional da triagem manual posterior para mecanismos preventivos, interoperáveis e monitorados continuamente. Para a sociedade, o ganho é um cadastro mais confiável para identificar e qualificar agricultores familiares e sustentar, com maior segurança, a focalização das políticas públicas que deles dependem.

---

## Notas de Fim (Apêndice VI)

²⁴ BRASIL. Lei nº 10.406, de 10 de janeiro de 2002. Institui o Código Civil. Brasília: Presidência da República, 2002. Arts. 3º, 4º e 6º.
