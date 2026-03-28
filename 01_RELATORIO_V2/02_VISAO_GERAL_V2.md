# 2. VISÃO GERAL DO OBJETO

9. A agricultura familiar responde por 77% dos estabelecimentos rurais do Brasil e emprega 67% da mão de obra no campo, aproximadamente 10,1 milhões de pessoas, segundo o Censo Agropecuário 2017¹¹. O setor é a base de sustentação de políticas públicas que, na safra 2023/2024, movimentaram R$ 59,6 bilhões apenas no Pronaf¹². Para acessar esse e outros programas (PAA, PNAE, Garantia-Safra, assistência técnica e habitação rural), o agricultor familiar precisa estar inscrito no Cadastro Nacional da Agricultura Familiar (CAF), instrumento de habilitação prévia instituído pelo Decreto 9.064/2017¹³ em substituição à Declaração de Aptidão ao Pronaf (DAP). A transição foi gradual: a DAP vigorou desde 1996; o CAF entrou em operação em 31 de dezembro de 2021 e o período de coexistência encerrou-se em outubro de 2022¹⁴.

10. Atualmente na versão 3.0, regulamentada pela Portaria MDA 19/2025¹⁵, o cadastro reúne cerca de 3,03 milhões de unidades familiares ativas (peça 152, p. 3), 3,2 milhões de imóveis georreferenciados (peça 110, p. 4) e 11,4 milhões de documentos comprobatórios digitalizados (peça 140, p. 5).

11. A qualidade desses dados condiciona diretamente a capacidade do CAF de atestar a elegibilidade dos cadastrados e, por consequência, a focalização de todas as políticas que dele dependem.

12. O cadastramento é descentralizado e opera por meio da Rede CAF, composta por emissores credenciados pelo MDA, como órgãos públicos federais, estaduais e municipais, entidades de assistência técnica (Emater), sindicatos rurais e entidades privadas sem fins lucrativos. Ao todo, 23.558 técnicos emissores em 6.690 entidades compõem essa rede (peça 152, p. 6). O modelo é autodeclaratório: o beneficiário apresenta documentação comprobatória de identidade, vínculo com a terra e renda, que deve demonstrar o atendimento aos requisitos cumulativos de elegibilidade do art. 3º da Lei 11.326/2006¹⁶, notadamente o limite de 4 módulos fiscais e a predominância de mão de obra e renda familiar.

13. O sistema CAF 3.0 opera sobre 109 tabelas (peça 134, p. 4) e integra-se a bases externas por meio do BCadastro/ConectaGOV, Receita Federal e Dataprev (peça 78, p. 7). O público cadastrado abrange agricultores familiares, extrativistas, pescadores artesanais, aquicultores, silvicultores, quilombolas, indígenas e assentados da reforma agrária.

**Quadro 1** — O CAF em números (março-agosto/2025)

| Dimensão | Quantidade |
|---|---:|
| Unidades familiares ativas | ~3,03 milhões |
| Imóveis  | ~3,2 milhões |
| Documentos comprobatórios digitalizados | ~11,4 milhões |
| Tabelas do banco de dados | 109 |
| Agentes da Rede CAF | 23.558 técnicos emissores em 6.690 entidades |
| Tipos de público cadastrado | 9 (agricultores, extrativistas, pescadores, aquicultores, silvicultores, quilombolas, indígenas, assentados e demais) |

*Fonte: base de dados do CAF 3.0 fornecida pelo MDA, apresentação institucional SAF/MDA (peça 152, p. 3, 4 e 6) e análise de cobertura do dicionário (peça 134, p. 4). Período: março a agosto de 2025.*

14. A tensão estrutural que motivou esta auditoria reside na coexistência de dois vetores opostos. De um lado, a modernização em curso: o CAF 3.0 incorporou validações que reduziram o cadastramento de novas propriedades inelegíveis (98,7% das que excedem 4 módulos fiscais foram cadastradas antes da versão atual; peça 107, p. 8) e a nova interface de mapeamento reduziu duplicações em novos cadastros de 92,36% para 16,59%, conforme informado pelo gestor (peça 117, p. 15).

15. De outro lado, o passivo acumulado nas versões anteriores (DAP, CAF 2.0) permanece ativo na base: 27,1% dos documentos comprobatórios são semanticamente inadequados (~3,08 milhões de documentos; peça 103, p. 9; peça 140, p. 5), 53,55% dos documentos de imóvel apresentam divergência crítica de área (peça 109, p. 7), a taxa de erro cartográfico alcança 45,92% da base georreferenciada (peça 119, p. 9), 3.097 titulares falecidos permanecem como responsáveis ativos (peça 124, p. 9) e 94,1% das descrições do dicionário de dados são inadequadas (peça 135, p. 4). Essa dualidade, entre avanço no fluxo corrente e persistência de fragilidades estruturais no estoque, é o eixo central dos achados.

16. A fiscalização originou-se da Proposta de Fiscalização 3019/2025, apresentada em 28/5/2025 pela AudTI, cujo escopo original abrangia o Cadastro Ambiental Rural (CAR) e o CAF. O Ministro Antonio Anastasia autorizou a realização em 9/6/2025 (peça 4, TC 009.045/2025-2), com início formalizado pela Portaria de Fiscalização 343/2025-AudTI (peça 3). Em 29/8/2025, por despacho do Relator (peça 39), o CAR foi excluído do escopo, passando a ser utilizado apenas como fonte subsidiária de informação, prosseguindo-se a auditoria com foco exclusivo no CAF.

17. O trabalho insere-se no Eixo 1 (Fiscalizações) da Estratégia de Atuação do TCU em Governança de Dados (GovDados 2023-2028), estruturada em quatro eixos (fiscalização, comunicação, capacitação e GovDados multinível), aprovada pelo Acórdão 390/2024-TCU-Plenário, que consigna governança e gestão de dados governamentais como tema de alto risco na Lista de Alto Risco do TCU. No âmbito específico da agricultura familiar, o Acórdão 1197/2018-TCU-Plenário já havia identificado fragilidades sistêmicas na emissão da DAP, com indícios de irregularidade em 1.335.852 declarações emitidas entre 2007 e 2017, cujas determinações permanecem pendentes de cumprimento integral após três monitoramentos.

18. São também processos conexos: o Acórdão 646/2017-TCU-Plenário (auditoria no PAA), o Acórdão 1708/2017-TCU-Plenário (levantamento no SNCR) e o Acórdão 2279/2021-TCU-Plenário (plataforma GovData/ConectaGOV). No plano jurisprudencial, registre-se que o Acórdão 457/2026-TCU-Plenário, embora proferido em processo do qual o MDA não era parte, adotou expressamente o DAMA-DMBOK v2 como referencial de maturidade de governança de dados em órgãos federais, ancorando a pertinência desse framework como critério de auditoria.

19. A relação completa dos trabalhos anteriores do TCU sobre o tema consta do Apêndice III.

20. A análise preliminar dos riscos identificou três vetores convergentes: (i) inexatidão e inconsistência dos dados, decorrentes de modelo autodeclaratório sem validação robusta e de integração deficiente com bases oficiais, manifestadas nas taxas de 27,1% de inadequação semântica documental, 53,55% de divergência de área e 45,92% de erro cartográfico, podendo resultar em concessão de benefícios a públicos não elegíveis ou em bloqueios injustos a beneficiários legítimos; (ii) obsolescência e incompletude, com 3.097 titulares falecidos (peça 124, p. 9) e 138 menores (peça 124, p. 8) mantidos como responsáveis ativos, comprometendo a análise de elegibilidade; e (iii) fragilidades de governança, com 94,1% das descrições do dicionário de dados inadequadas (peça 135, p. 4) e ausência de papéis e responsabilidades formalizados, impactando a transparência e a auditabilidade do cadastro.

21. Os riscos (i) e (ii) fundamentam a QST-1, que indaga em que medida os mecanismos de verificação de dados do CAF asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio, desdobrada nos achados ACH-01 (documentação comprobatória), ACH-02 (integridade geoespacial) e ACH-03 (qualidade dos dados cadastrais). O risco (iii) embasa a QST-2, que investiga se a estrutura de governança e gestão de dados assegura padrões claros, papéis definidos, rastreabilidade e integridade ao longo do ciclo de vida dos dados, desdobrada no achado ACH-04 (gestão de metadados).

22. A baixa maturidade em governança de dados autoavaliada pelo próprio MDA no iGovSisp 2024 (peça 139, p. 2) corrobora a pertinência da fiscalização. As duas questões foram desdobradas em treze subquestões, cujo detalhamento consta da Matriz de Planejamento (Anexo C).

**Quadro 2** — Mapeamento riscos → questões de auditoria → achados

| Questão de auditoria | Vetores de risco | Achados | Temas |
|---|---|---|---|
| QST-1 — Mecanismos de verificação de dados e regras de negócio | (i) Inexatidão e inconsistência; (ii) Obsolescência e incompletude | ACH-01; ACH-02; ACH-03 | Documentação comprobatória; Integridade geoespacial; Qualidade dos dados cadastrais |
| QST-2 — Governança e gestão de dados ao longo do ciclo de vida | (iii) Fragilidades de governança | ACH-04 | Gestão de metadados |

*Fonte: Matriz de Planejamento (Anexo C). As treze subquestões que desdobram QST-1 e QST-2 constam do mesmo anexo.*

---

## Notas de Fim (Apêndice VI)



¹¹ BRASIL. Instituto Brasileiro de Geografia e Estatística. Censo Agropecuário 2017. Rio de Janeiro: IBGE, 2019. Disponível em: https://www.ibge.gov.br/estatisticas/economicas/agricultura-e-pecuaria/21814-2017-censo-agropecuario.html. Acesso em: 24 mar. 2026.

¹² BRASIL. Agência Gov. Com Lula, Pronaf investe R$ 59,6 bilhões na agricultura familiar, aumento de 12,1% em relação à safra 2022/2023. Brasília: Governo Federal, 22 jul. 2024. Disponível em: https://agenciagov.ebc.com.br/noticias/202407/com-lula-pronaf-investe-r-59-6-bilhoes-na-agricultura-familiar-aumento-de-12-1-em-relacao-a-safra-2022-2023. Acesso em: 24 mar. 2026. [Mesma fonte da nota ¹ da Introdução; numeração mantida para remissão independente.]

¹³ BRASIL. Decreto nº 9.064, de 31 de maio de 2017. [Mesma referência da nota ³.]

¹⁴ MARIZ, Carlos. Prazo de transição da Declaração de Aptidão ao Pronaf para o Cadastro Nacional de Agricultura Familiar encerra dia 31 de outubro. Emdagro, Aracaju, 17 out. 2022. Disponível em: https://emdagro.se.gov.br/prazo-de-transicao-da-declaracao-de-aptidao-ao-pronaf-para-o-cadastro-nacional-de-agricultura-familiar-encerra-dia-31-de-outubro/. Acesso em: 24 mar. 2026.

¹⁵ BRASIL. Ministério do Desenvolvimento Agrário e Agricultura Familiar. Portaria MDA nº 19, de 21 de março de 2025. [Mesma referência da nota ⁴.]

¹⁶ BRASIL. Lei nº 11.326, de 24 de julho de 2006. [Mesma referência da nota ².]
