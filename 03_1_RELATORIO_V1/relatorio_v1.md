
 
Relatório de Auditoria
Qualidade de Dados no CAF

TC 011.073/2025-0					Fiscalização: 128/2025
Relator: Antonio Anastasia

DA FISCALIZAÇÃO
Instrumento: auditoria operacional.
Ato originário: despacho de 9/6/2025 do Min. Antonio Anastasia (TC 009.045/2025-2, peça 4).
Objeto da fiscalização: bases de dados relacionadas ao Cadastro Nacional da Agricultura Familiar (CAF), com foco na identificação de inconsistências e fragilidades nos dados que possam comprometer a execução das políticas públicas da área ambiental e da agricultura familiar.
Atos de designação: 1) Planejamento: Portaria de Fiscalização - AudTI 343/2025, de 10/6/2025 (peça 3); 2) Alteração de planejamento: Portaria de Fiscalização - AudTI 366/2025, de 17/6/2025 (peça 25); 3) Alteração de planejamento: Portaria de Fiscalização - AudTI 490/2025, de 7/8/2025 (peça 32); 4) Execução e Relatório: Portaria de Fiscalização - AudTI 568/2025, de 1º/9/2025 (peça 40).
Período de realização da auditoria: 16/6/2025 a 21/11/2025.
Composição da equipe:
Auditor	Matrícula	Lotação
Harley Alves Ferreira (supervisor)	5666-9	AudTI
Fernando Lima Gama Júnior (coordenador)	6499-8	AudTI
Sylvio Xavier Júnior	2423-6	AudTI
Kalenus Pires da Nóbrega	10662-3	AudTI

DOS ÓRGÃOS/ENTIDADES FISCALIZADOS
Órgão/entidade fiscalizado	Ministério do Desenvolvimento Agrário e Agricultura Familiar (MDA)
Vinculação ministerial	Ministério do Desenvolvimento Agrário e Agricultura Familiar (MDA)
Vinculação no TCU	AudSustentabilidade
Responsável pelo órgão/entidade	Nome	Luiz Paulo Teixeira Ferreira
	Cargo	Ministro de Estado
	Período	A partir de 1º/1/2023 (Decreto 11.338/2023)
PROCESSOS CONEXOS
TC 016.167/2023-6: Relatório de Levantamento sobre Governança de Dados na APF (Acórdão 390/2024-TCU-Plenário; Relator: Min. Benjamin Zymler)
TC 012.700/2017-7: Auditoria de Conformidade na Declaração de Aptidão ao PRONAF (DAP) (Acórdão 1.197/2018-TCU-Plenário; Relator: Min. André Luís de Carvalho)
TC 013.179/2016-0: Levantamento no Sistema Nacional de Crédito Rural (SNCR) (Acórdão 1.708/2017-TCU-Plenário; Relator: Min. Augusto Nardes)
TC 024.338/2015-0: Auditoria Operacional no Programa de Aquisição de Alimentos (PAA) (Acórdão 646/2017-TCU-Plenário; Relator: Min. Augusto Nardes)
TC 031.158/2020-0: Acompanhamento sobre Plataformas de Compartilhamento de Dados (Acórdão 2.279/2021-TCU-Plenário; Relator: Min. Aroldo Cedraz)
 
Resumo
Por que a auditoria foi realizada
A agricultura familiar é responsável por 77% dos estabelecimentos rurais do país. O Cadastro Nacional da Agricultura Familiar (CAF), gerido pelo Ministério do Desenvolvimento Agrário (MDA), é o instrumento obrigatório para identificar esses beneficiários e habilitá-los ao acesso a políticas públicas críticas, como o Programa Nacional de Fortalecimento da Agricultura Familiar (Pronaf), o Programa de Aquisição de Alimentos (PAA) e o Programa Nacional de Alimentação Escolar (PNAE), que movimentam dezenas de bilhões de reais anualmente. A fiscalização foi motivada pela necessidade de avaliar se a transição da antiga Declaração de Aptidão ao Pronaf (DAP) para o CAF 3.0 corrigiu fragilidades históricas e se o sistema apresenta inconsistências de dados que comprometem a correta aplicação desses recursos públicos e a segurança jurídica das políticas agrárias.
Quais os benefícios esperados? 
Espera-se que a implementação das propostas promova a confiabilidade do cadastro, assegurando que os recursos do Pronaf, PAA e PNAE alcancem exclusivamente o público-alvo definido em lei. Almeja-se, ainda, a redução significativa de erros na base de dados, a detecção automatizada de inconsistências, o saneamento do passivo histórico e a modernização da governança de dados do MDA, garantindo maior eficiência, transparência e segurança jurídica às políticas de desenvolvimento agrário.	Auditoria na base do Cadastro da Agricultura Familiar
A auditoria operacional realizada no CAF revelou um cenário de fragilidade sistêmica na governança de dados do Cadastro, evidenciando deficiências críticas na validação documental, na integridade cartográfica, na qualidade dos registros cadastrais e no dicionário de dados do sistema, o que pode comprometer a confiabilidade do acesso às principais políticas públicas agrárias do país.
O que o TCU fiscalizou?
O TCU realizou auditoria operacional no CAF para avaliar a conformidade, integridade e confiabilidade dos dados armazenados. O trabalho focou na análise dos mecanismos de verificação de elegibilidade (regras de negócio), na qualidade dos dados cadastrais e cartográficos e na estrutura de governança de dados do CAF. Foram utilizadas técnicas de análise de dados massiva, inteligência artificial e cruzamento com bases oficiais (Receita Federal, Sisobi e Incra) para testar a robustez do cadastro que abrange 3,3 milhões de unidades familiares. 
O que o TCU encontrou?
Quanto à documentação, identificou-se que 27,1% dos documentos são semanticamente inadequados para comprovar elegibilidade, com dependência de validação manual, sem verificação automatizada robusta. No aspecto cartográfico, constatou-se deterioração da qualidade geoespacial: a migração para o CAF 3.0 elevou a taxa de erros cartográficos em 40,6%, com duplicações espaciais massivas e municípios cuja área cadastrada supera a extensão territorial oficial. Em relação à qualidade cadastral, foram detectados responsáveis falecidos, menores de idade, 90,62% de e-mails fictícios e valores de renda manifestamente implausíveis. Por fim, verificou-se incompletude do dicionário de dados, comprometendo a auditabilidade e a transparência do sistema.
O que o TCU propõe?
O TCU propõe determinação ao MDA para que elabore plano que contemple ações para que sejam avaliadas as falhas identificadas, e, uma vez confirmadas, adote as medidas de saneamento, abrangendo: documentos inadequados e com baixa resolução, divergências de área, passivo histórico de erros cartográficos, registros de responsáveis falecidos e menores, dados de contato fictícios, inconsistências de renda e de natureza jurídica de pessoas jurídicas, e deficiências no dicionário de dados. 
Recomenda, ainda, que o MDA padronize os procedimentos de cadastramento e validação pela rede de cadastradores; implemente controles automatizados em campos críticos (documentos, coordenadas, dados civis, renda e contato); promova a interoperabilidade do CAF com bases de dados oficiais para detecção tempestiva de anomalias; aprimore a gestão de mudanças do sistema para prevenir regressões de qualidade do sistema; crie painéis de monitoramento contínuo com indicadores de qualidade cadastral; e aperfeiçoe a gestão de metadados com definições semânticas claras e papéis formais de responsabilidade sobre os dados.


Sumário
1.	Introdução	7
1.1.	Decisão que originou a fiscalização e suas razões	7
1.2.	Processos conexos	8
1.3.	Mapeamento dos riscos	8
1.4.	Questões de auditoria	10
1.5.	Método	10
1.6.	Limitação de auditoria	12
2.	Visão geral do objeto	12
2.1.	Definição e Histórico	12
2.2.	Contexto e Materialidade	13
2.3.	Funcionamento e Atores	13
2.4.	Desafios e Governança	13
2.5.	Trabalhos anteriores do TCU sobre o tema	14
3.	Achados de auditoria	14
3.1.	Achado I: Fragilidades no processo de validação e inadequações na documentação comprobatória comprometem a comprovação da elegibilidade da agricultura familiar	14
3.2.	Achado II: Regressões em transições tecnológicas e passivo histórico deterioram a qualidade cartográfica e fragilizam a integridade geoespacial do CAF, comprometendo a rastreabilidade e validações baseadas em localização	23
3.3.	Achado III: Fragilidades de governança, cadastramento e curadoria dos dados comprometem a qualidade cadastral do CAF, dificultando comunicação com os cadastrados e elevando riscos de focalização das políticas públicas de agricultura familiar	35
3.4.	Achado IV: Falhas na gestão de metadados resultam em dicionário de dados inadequado, comprometendo rastreabilidade e auditabilidade do CAF	48
4.	Conclusão	57
5.	Comentários dos gestores	59
6.	Propostas de Encaminhamento	59
Apêndice I – Método	62
Apêndice II – Trabalhos Anteriores do TCU	65
Apêndice III – Matriz de Achados	68
Apêndice III.A – Matriz de Achados – Achado I	68
Apêndice III.B – Matriz de Achados – Achado II	72
Apêndice III.C – Matriz de Achados – Achado III	76
Apêndice III.D – Matriz de Achados – Achado IV	80
Apêndice IV – Matriz de Planejamento	85
Apêndice V – Metodologia Estatística da Análise Documental	89
Apêndice VI – Glossário	93
Apêndice VII – Listas de Siglas, de Figuras e de Tabelas	103
Apêndice VIII – Notas de fim	108

 
1.	Introdução
1.	 Trata-se de auditoria operacional na base de dados do Cadastro da Agricultura Familiar (CAF), versão 3.0, gerido pelo Ministério do Desenvolvimento Agrário e Agricultura Familiar (MDA). A fiscalização foi determinada pelo despacho de 9/6/2025 do Ministro Antonio Anastasia, no âmbito do processo TC 009.045/2025-2.
2.	A agricultura familiar desempenha papel central na economia e na segurança alimentar do Brasil . O CAF constitui o principal instrumento de identificação e qualificação de seus beneficiários, funcionando como porta de entrada para políticas públicas estruturantes, como o Programa Nacional de Fortalecimento da Agricultura Familiar (Pronaf) e o Programa de Aquisição de Alimentos (PAA)       .
3.	O objetivo principal da auditoria foi avaliar a qualidade dos dados da base do CAF e a estrutura de governança de dados implementada pelo MDA. Buscou-se verificar se os mecanismos de controle asseguram a confiabilidade das informações que fundamentam a concessão de benefícios e se a gestão dos dados observa os princípios da Administração Pública Federal.
4.	O escopo do trabalho delimitou-se à análise da base de dados do CAF (versão 3.0), abrangendo registros cadastrais, documentos digitalizados e dados geoespaciais. 
5.	A avaliação utilizou como principais critérios de auditoria a Lei 11.326/2006 (Lei da Agricultura Familiar), o Decreto 10.046/2019 (Governança de Dados), a Portaria MDA 19/2025 , além de referenciais técnicos como a norma ABNT NBR ISO/IEC 25012:2008 (Qualidade de Dados de Software) e o guia DAMA-DMBOK v2.
6.	 O método empregado baseou-se em técnicas de análise de dados massiva (data analytics), incluindo o uso de inteligência artificial para leitura automatizada de documentos e validação cartográfica, além de cruzamentos com bases de dados governamentais (Receita Federal, Sisobi e Instituto Nacional de Colonização e Reforma Agrária - Incra).
7.	A presente fiscalização foi realizada em conformidade com as Normas de Auditoria do Tribunal de Contas da União (NAT) e com os padrões internacionais de auditoria das Entidades Fiscalizadoras Superiores (ISSAI), não havendo restrições significativas à execução dos trabalhos.
8.	Este relatório está organizado em cinco capítulos que, além desta introdução, apresentam a visão geral do objeto, a análise detalhada dos quatro achados de auditoria, as conclusões e as propostas de encaminhamento.
1.1.	Decisão que originou a fiscalização e suas razões
9.	A presente fiscalização originou-se da Proposta de Fiscalização 3019 (peça 139), apresentada em 28/5/2025 pela Unidade de Auditoria Especializada em Tecnologia da Informação (AudTI), com o objetivo de avaliar a qualidade das informações constantes das bases de dados relacionadas ao Cadastro Ambiental Rural (CAR) e ao Cadastro Nacional da Agricultura Familiar (CAF), com foco na identificação de inconsistências e fragilidades nos dados que possam comprometer a execução das políticas públicas da área ambiental e da agricultura familiar. 
10.	Após sorteio do relator, o Ministro Antonio Anastasia proferiu despacho em 9/6/2025 (peça 4 do processo administrativo TC 009.045/2025-2), autorizando a realização da auditoria nos termos propostos. Em 16/6/2025, foi expedida a Portaria de Fiscalização 343/2025-AudTI (peça 3, processo principal TC 011.073/2025-0), iniciando formalmente a etapa de planejamento dos trabalhos. Conforme despacho do Relator, de 29/8/2025 (peça 39), o Cadastro Ambiental Rural (CAR) foi excluído do escopo inicialmente estabelecido, sendo utilizado apenas como fonte subsidiária de informação.
1.2.	Processos conexos
11.	São processos conexos a esta auditoria:
11.1.	Governança de Dados
11.1.1.	TC 016.167/2023-6 – Relatório de Levantamento sobre Governança de Dados na APF (Relator: Min. Benjamin Zymler; Acórdão 390/2024-TCU-Plenário).
11.1.1.1.	Por meio desse acórdão, o TCU aprovou relatório com proposta de Estratégia de Atuação do Tribunal em Governança de Dados (GovDados) para o período 2023-2028, estruturada em quatro eixos: (i) fiscalização, no qual o TCU busca aumentar o grau de maturidade da APF por meio de ações de controle que avaliam práticas, processos e papéis relacionados à governança e gestão de dados; (ii) comunicação, no qual o TCU promove eventos e publicações para disseminar conhecimento e aumentar a conscientização sobre governança de dados; (iii) capacitação, voltada ao desenvolvimento de competências em governança de dados entre servidores e gestores; e (iv) GovDados multinível, que visa promover a transformação em governança de dados em todo o setor público brasileiro, incluindo estados e municípios.
11.1.1.2.	Essa presente auditoria no CAF, portanto, insere-se no Eixo 1 – Fiscalizações da referida estratégia, especificamente no âmbito das "fiscalizações de propósito específico" (item 7.1.2), que visam a avaliar práticas de governança e gestão de dados em organizações da APF, com foco em temas considerados importantes para o bom uso de dados. A estratégia busca mitigar os riscos relacionados no item 26 da Lista de Alto Risco do TCU (LAR), que consigna "Governança e gestão de dados governamentais" como tema de alto risco para a APF, tendo em vista as consequências para a Administração Pública e para o cidadão relacionadas à má qualidade das informações.
11.1.2.	TC 031.158/2020-0 (Acórdão 2.279/2021- TCU-Plenário, Rel. Min. Aroldo Cedraz): Acompanhamento sobre Plataforma de Compartilhamento de Dados e o projeto GovData.
11.2.	Auditorias na DAP e Políticas Correlatas:
11.2.1.	TC 012.700/2017-7: (Acórdão 1.197/2018-TCU-Plenário, Rel. Min. Subst. André Luís de Carvalho): Auditoria na DAP que identificou fragilidades sistêmicas na autodeclaração e falhas nos controles de elegibilidade;
11.2.2.	TC 013.179/2016-0 (Acórdão 1.708/2017- TCU-Plenário, Rel. Min. Augusto Nardes): Levantamento no Sistema Nacional de Crédito Rural (SNCR);
11.2.3.	TC 024.338/2015-0 (Acórdão 646/2017- TCU-Plenário, Rel. Min. Augusto Nardes): Auditoria no PAA, política pública que utiliza a DAP/CAF como critério de acesso.
1.3.	Mapeamento dos riscos
12.	A gestão de dados em cadastros governamentais estratégicos, como o CAF, envolve um conjunto complexo de riscos inter-relacionados. A qualidade da informação, que sustenta políticas públicas de impacto financeiro relevante, é diretamente afetada por deficiências nas dimensões de exatidão, completude, consistência, atualidade e validade. Somam-se a isso os riscos legais, como a necessidade de conformidade com a Lei Geral de Proteção de Dados Pessoais (LGPD), e os desafios operacionais de segurança da informação e interoperabilidade entre sistemas. A governança inadequada sobre essas dimensões compromete a justiça no acesso a políticas públicas de fomento à agricultura familiar e a credibilidade do Estado perante beneficiários e parceiros.
13.	A análise deste cenário revela que a Administração Pública federal está exposta a riscos sistêmicos. Com base em boas práticas e nas dimensões de qualidade de dados reconhecidas internacionalmente, foram mapeados os seguintes riscos centrais para a execução das políticas públicas dependentes do CAF:
13.1.	Risco 1: Devido a fragilidades sistêmicas na gestão do ciclo de vida dos dados cadastrais de agricultores familiares, que incluem falhas na entrada de dados (autodeclaração de informações e integração deficiente com outras bases governamentais), poderá ocorrer a consolidação da base de dados do CAF com informações fraudulentas ou incorretas (inverídicas, imprecisas, incompletas, desatualizadas e conflitantes), o que poderá levar à concessão indevida de benefícios e à exclusão de agricultores familiares legítimos do acesso a benefícios, como programas de crédito, assistência técnica e comercialização, impactando a efetividade das políticas de incentivo à agricultura familiar;
13.2.	Risco 2: Devido a limitações sistêmicas na capacidade de verificação e fiscalização dos dados constantes no CAF, decorrente tanto de falhas nos mecanismos de cruzamento de dados quanto da dificuldade em obter e tratar dados de referência externos de qualidade , poderá ocorrer a permanência, sem detecção, de informações fraudulentas ou incorretas, o que poderá levar a perda de recursos públicos por fraudes e desvios de recursos públicos para beneficiários indevidos, impactando a efetividade das políticas de incentivo à agricultura familiar; e 
13.3.	Risco 3: Devido à inexistência de estrutura adequada de governança e gestão de dados, poderá ocorrer a indefinição de normas, padrões, papéis e responsabilidades, o que poderá levar à falta de documentação e orientação clara sobre dados, processos e critérios, impactando a transparência e a tomada de decisões baseadas em dados completos e confiáveis.
14.	Os riscos identificados no CAF incluem:
Risco	Descrição
Inexatidão e Inconsistência dos Dados	A exatidão dos dados é comprometida por um modelo autodeclaratório sem validação robusta. Coordenadas geográficas apresentam inconsistências. A falta de validação cruzada com outras bases oficiais, como as do Instituto Brasileiro de Geografia e Estatística (IBGE) e da Secretaria Especial da Receita Federal do Brasil (RFB), agrava o problema.
Obsolescência e Incompletude	A defasagem temporal das informações é crítica, com dados desatualizados (responsáveis falecidos, mudanças de situação econômica). A incompletude de atributos essenciais nos cadastros impede a correta análise de elegibilidade para políticas públicas e bloqueia o acesso de beneficiários legítimos a serviços como o crédito rural.
Fraudes e Comprometimento de Políticas Públicas	Dados de baixa qualidade facilitam inclusões indevidas. Inconsistências geram bloqueios automáticos e injustos no acesso ao crédito, afetando milhares de famílias, e comprometem a eficácia de programas como PRONAF, PAA e PNAE – Programa Nacional de Alimentação Escolar.
Riscos Legais e de Segurança	O tratamento de dados pessoais sensíveis (CPF, renda, patrimônio) sem as devidas medidas de segurança expõe os órgãos a sanções da LGPD, sendo já consolidada a responsabilidade objetiva do Estado por danos causados por dados incorretos.
Falta de Interoperabilidade	A fragmentação dos dados entre múltiplos órgãos (MDA, Incra, RFB) e a ausência de uma arquitetura de dados unificada resultam em retrabalho, inconsistências e dificultam a validação cruzada das informações, além da duplicação de gastos com equipamentos e serviços que poderiam ser compartilhados.
15.	Considerando que o CAF sustenta políticas que movimentam enormes montantes anualmente em crédito rural e incentivos (Pronaf, PAA, PNAE) e serve de instrumento de qualificação para milhões de unidades familiares, a atuação do TCU para avaliar a qualidade dos dados do Cadastro se faz oportuna. A baixa maturidade em governança de dados autoavaliada pelos próprios órgãos gestores do MDA, segundo dados do iGovSisp 2024, corrobora a urgência desta fiscalização.
1.4.	Questões de auditoria
16.	Em razão dos riscos mapeados, foram elaboradas as seguintes questões para a auditoria:
16.1.	QST-1: Em que medida os mecanismos de verificação de dados do CAF (versão 3, período: março de 2025 a agosto de 2025) asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio, considerando-se como critérios a Lei 11.326/2006, as Portarias - MDA 19/2025 e 20/2025, a norma ISO/IEC 25012:2008, o framework DAMA-DMBOK v2 e os princípios da Administração Pública?
16.2.	QST-2: Em que medida a estrutura de governança e gestão de dados aplicada ao CAF assegura padrões claros, papéis definidos, rastreabilidade e integridade das informações ao longo de todo o ciclo de vida dos dados, considerando-se os critérios do Decreto 10.046/2019, da norma ISO/IEC 11179:2015, do COBIT 2019 e do DAMA-DMBOK v2?
17.	Para responder às questões acima de forma sistemática e abrangente, a equipe de auditoria desdobrou-as em treze subquestões específicas, organizadas em quatro achados, cada um investigando dimensões distintas da qualidade de dados e da governança do CAF. O Achado I examinou a adequação dos documentos comprobatórios e a acurácia das áreas registradas, aspectos essenciais para a verificação das regras de negócio e da qualidade dos dados (QST-1). O Achado II avaliou a qualidade cartográfica, incluindo erros posicionais, duplicações espaciais e inflação cadastral, dimensões críticas da acurácia, unicidade e consistência lógica dos dados (QST-1). O Achado III investigou a qualidade dos dados cadastrais de pessoas físicas e jurídicas, abrangendo validade, atualidade, completude e plausibilidade (QST-1). O Achado IV analisou o dicionário de dados do sistema, instrumento fundamental para assegurar padrões claros, rastreabilidade e integridade ao longo do ciclo de vida dos dados (QST-2).
1.5.	Método
18.	O método empregado na presente auditoria foi baseado na Matriz de Planejamento aprovada (Apêndice IV), que estabeleceu seis grupos de procedimentos: (i) verificação de regras de negócio; (ii) data profiling de qualidade de dados; (iii) rastreabilidade e logs; (iv) cruzamentos de bases governamentais; (v) análise de governança de dados; e (vi) investigação de causas e efeitos. 
19.	O data profiling consiste na análise técnica detalhada dos dados disponíveis em uma fonte de informação, visando compreender sua estrutura, conteúdo e relacionamentos. Essa técnica permite identificar padrões, anomalias e inconsistências (como campos nulos, formatos inválidos ou valores fora do padrão esperado) antes mesmo de se iniciar a análise de negócio propriamente dita, funcionando como um diagnóstico prévio da saúde da base de dados.
20.	Durante a execução, a equipe identificou oportunidades de aprofundamento que levaram à realização de procedimentos adicionais. Todos os achados foram sustentados mediante requisições de informações, análise de documentos normativos e reuniões com gestores do MDA (Atas de reuniões de 07/10/2025 e 21/10/2025, peças 73 e 74), conforme informações contantes do Apêndice I – Método.
21.	Para essa avaliação, foram adotados como critérios técnicos:
21.1.	Governança de TI: Cobit 2019 (ISACA), domínios APO11 (Gestão da Qualidade), BAI08 (Gestão do Conhecimento) e BAI10 (Gestão de Configuração);
21.2.	Qualidade de Dados: ISO/IEC 25012:2008, que define características de Acurácia, Consistência e Completude;
21.3.	Dados Geoespaciais: ISO 19157-1:2023 (Qualidade de Dados Geográficos);
21.4.	Metadados: ISO/IEC 11179:2015 (Registro de Metadados);
21.5.	Gestão de Dados: DAMA-DMBOK v2.
22.	Foram aplicadas técnicas de Análise de Dados (Data Analytics), Inteligência Artificial para leitura de documentos e cruzamento massivo com bases oficiais (da RFB, do Sisobi e do Incra). A avaliação revelou um cenário de fragilidade sistêmica na governança e na qualidade dos dados do CAF, materializada em quatro eixos de deficiências:
22.1.	(i) Fragilidades no processo de validação e inadequações na documentação comprobatória comprometem a comprovação da elegibilidade da agricultura familiar (Achado I): insuficiência semântica e técnica dos documentos de terra e renda para habilitação de beneficiários;
22.2.	(ii) Regressões em transições tecnológicas e passivo histórico deterioram a qualidade cartográfica e fragilizam a integridade geoespacial do CAF, comprometendo a rastreabilidade e validações baseadas em localização (Achado II): sobreposições críticas, coordenadas implausíveis e "inflação cadastral" de áreas municipais;
22.3.	(iii) Fragilidades de governança, cadastramento e curadoria dos dados comprometem a qualidade cadastral do CAF, dificultando comunicação com os cadastrados e elevando riscos de focalização das políticas públicas de agricultura familiar (Achado III): responsáveis falecidos, menores de idade, dados fictícios e valores estatisticamente impossíveis;
22.4.	(iv) Falhas na gestão de metadados resultam em dicionário de dados inadequado, comprometendo rastreabilidade e auditabilidade do CAF (Achado IV): documentação deficiente que compromete auditabilidade e manutenção do sistema.
1.6.	Limitação de auditoria
23.	Durante a reunião de apresentação realizada em 1º/7/2025 com o Ministério da Gestão e da Inovação em Serviços Públicos (MGI), órgão gestor do CAR, o diretor da Diretoria de Cadastro Ambiental Rural solicitou à equipe de auditoria o adiamento da fiscalização para dezembro de 2025, pedido posteriormente formalizado por meio do Ofício SEI 98265/2025/MGI, de 16/7/2025 (peça 33). 
24.	Diante da solicitação do MGI, a equipe de auditoria avaliou a convergência de fatores relevantes à decisão. A AudTI considerou os argumentos razoáveis e convincentes, tendo em vista que ficou demonstrada a concentração de atividades paralelas trazendo sobrecarga real às equipes técnicas do MGI responsáveis pela gestão do CAR. Por outro lado, o Ministério do Desenvolvimento Agrário (MDA), gestor do CAF, manifestou grande interesse na realização dos trabalhos relativos a esse cadastro sob sua responsabilidade, inclusive com a pronta disponibilização das bases de dados à equipe, que se encontrava alocada e mobilizada para a realização dos procedimentos de auditoria, com a etapa de planejamento já concluída. 
25.	Nesse contexto, o coordenador da auditoria elaborou instrução propondo a redução do escopo da fiscalização (peça 34), manifestação que recebeu pareceres favoráveis do supervisor da auditoria e do Auditor-Chefe da AudTI (peças 34-37) e anuência da Secretaria de Controle Externo de Governança, Inovação e Transformação Digital do Estado – SecexEstado (peça 38). 
26.	Nessa esteira, em 29/8/2025, o Ministro Antonio Anastasia proferiu despacho (peça 39) autorizando a redução do escopo da auditoria nos termos propostos, no sentido de dar continuidade aos trabalhos de fiscalização com foco no CAF, sob a gestão do Ministério do Desenvolvimento Agrário, utilizando-se o CAR de forma subsidiária, mediante consulta a fontes públicas e a documentos já constantes dos autos, sem requisições e outras demandas ao MGI durante o presente trabalho.
2.	Visão geral do objeto
2.1.	Definição e Histórico
27.	A agricultura familiar, reconhecida como categoria econômico-social pelo art. 3º da Lei 11.326/2006, desempenha papel central na economia e na segurança alimentar do Brasil. Segundo o Censo Agropecuário 2017 do IBGE2, o setor é responsável por 77% dos estabelecimentos rurais e emprega 67% da mão de obra no campo, totalizando aproximadamente 10,1 milhões de pessoas.
28.	Historicamente, a identificação desse público para fins de políticas públicas era realizada pela Declaração de Aptidão ao Pronaf (DAP). Contudo, o Decreto 9.064/2017 instituiu o Cadastro Nacional da Agricultura Familiar (CAF) como o instrumento oficial de identificação e qualificação, substituindo progressivamente a DAP. 
29.	A necessidade de modernização surgiu após auditorias do TCU (notadamente a que deu origem ao Acórdão 1.197/2018-TCU-Plenário) identificarem fragilidades na emissão das antigas DAPs. O Sistema do CAF entrou em operação em 31 de dezembro de 2021, iniciando um período de transição que se estendeu até outubro de 2022   . Atualmente, a plataforma encontra-se na versão CAF 3.0, regulamentada pela Portaria - MDA 19/2025, gerenciando uma base de 3,3 milhões de unidades familiares ativas e 11,3 milhões de documentos.
2.2.	Contexto e Materialidade
30.	O CAF não é um benefício financeiro direto, mas a porta de entrada obrigatória (habilitação prévia) para acessar as principais políticas públicas de desenvolvimento agrário. A integridade de seus dados é crítica para a correta aplicação de recursos em programas como:
30.1.	Programa Nacional de Fortalecimento da Agricultura Familiar (Pronaf): Responsável pela concessão de crédito rural com taxas subsidiadas (R$ 59,6 bilhões na safra 2023/2024);
30.2.	Programa de Aquisição de Alimentos (PAA): Promove a compra direta de produtos da agricultura familiar;
30.3.	Programa Nacional de Alimentação Escolar (PNAE): Destina recursos para aquisição de alimentos para merenda escolar;
30.4.	Outros programas como Garantia-Safra, Assistência Técnica e Extensão Rural (Ater) e Programa Nacional de Reforma Agrária (PNRA).
2.3.	Funcionamento e Atores
31.	O processo de cadastramento no Sistema do CAF é descentralizado e opera mediante a Rede CAF, composta por emissores credenciados pelo MDA. O fluxo baseia-se em informações autodeclaradas pelos beneficiários, acompanhadas de documentos comprobatórios (identificação, terra e renda) que devem demonstrar o atendimento aos requisitos de elegibilidade da Lei 11.326/2006.
32.	Os principais atores envolvidos na governança do sistema são:
32.1.	MDA (Gestor): Responsável pela definição de normas, manutenção da plataforma do Sistema do CAF, credenciamento de emissores e fiscalização;
32.2.	Rede de Emissores: Órgãos públicos (federais, estaduais e municipais) e entidades privadas sem fins lucrativos que realizam o atendimento e a inserção de dados na plataforma;
32.3.	Beneficiários: Agricultores familiares e suas formas associativas (cooperativas, associações) que utilizam o CAF (documento/cadastro) para acesso a políticas;
32.4.	Conselhos Municipais de Desenvolvimento Rural Sustentável (CMDRSs): Responsáveis pelo controle social do cadastro em nível local.
2.4.	Desafios e Governança
33.	A gestão do cadastro busca equilibrar a inclusão social de um público vulnerável com o necessário rigor no controle de elegibilidade. Em consonância com as diretrizes de governo digital, o MDA busca a simplificação e racionalização dos processos de cadastro para facilitar o acesso do cidadão.
34.	Contudo, essa simplificação pressupõe a existência de mecanismos robustos de governança e validação automatizada de dados (como a interoperabilidade com outras bases governamentais). A ausência desses controles pode comprometer a integridade do sistema, permitindo que a facilidade de entrada resulte em inconsistências ou concessão de benefícios a públicos não elegíveis.
2.5.	Trabalhos anteriores do TCU sobre o tema
35.	A relação detalhada dos trabalhos anteriores do TCU sobre o tema, incluindo transcrições de achados relevantes, encontra-se consolidada no Apêndice II – Trabalhos Anteriores do TCU.
3.	Achados de auditoria
3.1.	Achado I: Fragilidades no processo de validação e inadequações na documentação comprobatória comprometem a comprovação da elegibilidade da agricultura familiar
Síntese: A auditoria identificou que 27,1% dos documentos apresentados no CAF são semanticamente inadequados para comprovar os requisitos de elegibilidade, projetando-se cerca de 3 milhões de documentos problemáticos. Adicionalmente, 53,55% dos documentos de imóveis apresentam divergências críticas de área superiores a 10% em relação à base de dados, com viés sistemático de +120,89%. A validação depende exclusivamente de análise documental manual, sem verificação automatizada de requisitos legais, e 68,7% das digitalizações têm resolução inferior ao padrão definido pelo Conselho Nacional de Arquivos (Conarq). As causas incluem processos permissivos, ausência de validação semântica e limitações técnicas na digitalização.
36.	Atualmente, a validação da elegibilidade dos cadastrados depende principalmente da análise de documentos comprobatórios apresentados pelos próprios beneficiários, uma vez que não há verificação automatizada de requisitos legais no momento do cadastramento. As Regras de Negócio do CAF exigem apenas que documentos sejam anexados (peça 78, p. 5, Regra de Negócio RN1.17), mas não especificam validação do conteúdo semântico desses documentos. As únicas validações automatizadas existentes (peça 78, p. 7, Regra de Negócio RN1.29-30) consultam bases de dados sob gestão da Dataprev, não o conteúdo dos documentos anexados.
37.	A Lei 11.326/2006, art. 3º, estabelece os requisitos cumulativos para caracterização de agricultor familiar (peça 80, p. 1), incluindo o limite de área de 4 módulos fiscais (inciso I): 
(...) considera-se agricultor familiar e empreendedor familiar rural aquele que pratica atividades no meio rural, atendendo, simultaneamente, aos seguintes requisitos: 
I - não detenha, a qualquer título, área maior que 4 (quatro) módulos fiscais; 
II - utilize predominantemente mão-de-obra da própria família nas atividades econômicas do seu estabelecimento ou empreendimento; 
III - tenha percentual mínimo da renda familiar originada de atividades econômicas do seu estabelecimento ou empreendimento; 
IV - dirija seu estabelecimento ou empreendimento com sua família.
38.	A Portaria - MDA 19/2025, art. 8º, por seu turno, operacionaliza a validação documental especificando quais documentos são obrigatórios para inscrição no CAF: documento de identificação, comprovante de residência, documentação comprobatória de propriedade ou posse da terra e documentação comprobatória de renda (peça 108, p. 5). Os subitens subsequentes detalham os tipos documentais específicos admitidos para cada categoria de comprovação.
39.	Nesse sentido, diante dos riscos identificados à focalização das políticas públicas e considerando os critérios legais e técnicos apresentados, a equipe de auditoria realizou avaliação com a finalidade de responder às seguintes subquestões de auditoria específicas:
 
(i)	Os documentos comprobatórios apresentados pelos beneficiários do CAF são adequados para comprovar os requisitos de elegibilidade da agricultura familiar estabelecidos na legislação?
(ii)	As áreas de imóveis rurais registradas na base de dados do CAF correspondem aos valores que constam nos documentos apresentados pelos beneficiários?
40.	Para avaliar a acurácia dos dados, a equipe utilizou tecnologia de inteligência artificial (Claude Vision AI da Anthropic) para extrair dados dos documentos digitalizados e compará-los com os registros da base de dados (peça 103, p. 5). Cabe ressaltar que a precisão da ferramenta foi calibrada mediante validação cruzada com auditoria humana em amostra piloto, resultando em taxa de concordância superior a 95%, o que mitiga riscos de erro de medição automatizada.
Situação Encontrada
41.	A equipe de auditoria identificou inadequações sistêmicas que comprometem a capacidade do sistema de validar os requisitos de elegibilidade da agricultura familiar. Em resposta à primeira subquestão, a análise de amostra estratificada de 646 documentos revelou que 27,1% dos documentos apresentados são semanticamente inadequados — ou seja, não comprovam efetivamente os requisitos legais que declaram comprovar (peça 103, p. 9). Aplicando-se essa proporção à população total de 11.377.318 documentos cadastrados no CAF, projeta-se aproximadamente 3,08 milhões de documentos problemáticos, com intervalo de confiança de 99% compreendendo de 2,57 a 3,60 milhões de documentos nessa situação (peça 140, p. 3-4).  
42.	Exemplos de inadequação funcional identificados na análise amostral incluem: documentos de identidade (RG, CPF) ou comprovantes de residência anexados na categoria "documentos de imóvel rural", sem qualquer relação com os requisitos de comprovação de posse ou propriedade de terra estabelecidos pelo art. 8° da Portaria - MDA 19/2025; notas fiscais de aquisição de insumos agrícolas adquiridas pelos cadastrados e apresentadas como comprovação de renda quando tais notas comprovam despesas, não receitas; selfies e fotografias pessoais sem valor probatório; e arquivos de texto genéricos ou documentos em branco salvos como PDF (peça 103, p. 12-14).
Tabela 1. Inadequação Semântica por Tipo de Documento
Tipo de Documento	Analisados	Plenamente Adequados	Parcialmente Adequados (P)	Inadequados (I)	% Inadequação (P + I)
Imóvel Rural	227	144	20	63	36,6%
Renda	276	192	13	71	30,4%
Declarações	143	135	5	3	5,6%
Total	646	471	38	137	27,1%
Fonte: Análise de Adequação Semântica por Tipo de Documento (peça 103, p. 9-10). Amostra probabilística estratificada (n=646, IC 99%, margem de erro ±4,5 p.p.). Elaboração: equipe de auditoria.
43.	A inadequação concentra-se em categorias de documentos que comprovam requisitos mais sensíveis para determinação de elegibilidade: 36,6% dos documentos de imóvel rural são inadequados, seguidos por 30,4% dos documentos de renda (peça 103, p. 10-11). As Declarações de Veracidade — documentos padronizados emitidos pelo próprio sistema do CAF — apresentam a menor taxa de inadequação: apenas 5,6%, demonstrando que documentos estruturados e padronizados têm taxa de conformidade significativamente superior a documentos de livre apresentação pelos beneficiários.
44.	Em resposta à segunda subquestão, a análise de 155 documentos de imóveis rurais com área válida identificável (de uma amostra aleatória de 201 documentos) revelou que 53,55% apresentam divergências críticas superiores a 10% entre a área extraída do documento digitalizado e a área registrada na base de dados (peça 109, p. 7). Adotou-se o limiar de 10% como margem de segurança conservadora para afastar falsos positivos decorrentes de arredondamentos ou pequenas imprecisões de conversão. Essa proporção foi projetada para a população estimada de 2,62 milhões de documentos de imóveis com área válida — correspondente a 77,1% dos 3.392.881 documentos de imóveis cadastrados (peça 109, p. 7) —, resultando em aproximadamente 1,44 milhão de documentos com divergências significativas de área (os casos em que a área não pôde ser identificada devido à baixa qualidade do documento são tratados nos parágrafos 48 a 49 deste relatório). A análise foi conduzida com nível de confiança de 95% e margem de erro de ±6,44% (peça 109, p. 4; detalhamento metodológico no Apêndice V).
Figura 1. Documento de imóvel com área divergente na base de dados.
 
Na base, o imóvel representado na figura tem área de 1,5 ha; no documento o valor é de 5.0 ha (peça 105, p. 276-277, Documento 188). 
Fonte: AWS S3 caf-prod-mapa.
45.	Isso ocorreu devido às divergências não se distribuírem simetricamente. A análise agregada revelou divergência sistemática de +120,89%. Enquanto os documentos digitalizados indicam área total de 3.827,65 hectares, a base de dados do CAF registra apenas 1.732,85 hectares para os mesmos imóveis (peça 109, p. 9).
 
Tabela 2. Divergências de Área por Faixa de Magnitude
Faixa de Divergência	Casos	% do Total	Projeção População	IC 95% Inferior	IC 95% Superior
0-5% (tolerável)	70	45,16%	1.181.370	974.715	1.388.026
5-10% (moderada)	2	1,29%	33.753	0	240.409
10-50% (crítica)	15	9,68%	253.151	46.495	459.806
>50% (muito crítica)	68	43,87%	1.147.617	940.961	1.354.272
Total analisado	155	100,0%	2.615.891	—	—
Fonte: Análise de Dimensão Área (peça 109, p. 9). Subamostra de documentos de imóveis com área válida identificável (n=155). Elaboração: equipe de auditoria
46.	Com efeito, a divergência agregada de +120,89% identificada não é compatível com erros aleatórios de digitação, que produziriam divergências positivas e negativas com tendência a compensação estatística (somatório próximo a zero). O padrão sistemático observado — áreas no banco consistentemente menores que nos documentos — sugere causas estruturais: erro sistemático de conversão de unidades de medida (alqueires/hectares), registro apenas de área útil quando o documento apresenta área total, documentos agregando várias propriedades ou desatualização entre documentos e valores cadastrados (peça 109, p. 9-10).
47.	Ademais, a auditoria identificou que 33,33% dos documentos de imóveis rurais analisados são de tipo inadequado para comprovação de propriedade ou posse de terra (peça 105, p.7), não correspondendo aos tipos documentais aceitos especificados no art. 8º, I, c, da Portaria - MDA 19/2025 (peça 108, p. 5). Projetando-se para a população de 3.392.881 documentos de imóveis cadastrados, estima-se 1,13 milhão de documentos em desconformidade com as regras definidas pela referida Portaria para comprovação da posse de imóveis.
48.	Durante a análise de adequação semântica dos documentos, a equipe identificou, incidentalmente, situação relacionada à qualidade técnica da digitalização: 68,7% dos documentos digitalizados (444 de 646 analisados) apresentam resolução inferior a 300 DPI (dots per inch) (peça 106, p. 7), violando o padrão técnico estabelecido pela Resolução - Conarq 31/2010 (peça 79, p. 20, Tabela 1), que recomenda resolução mínima de 300 DPI para documentos textuais, especialmente aqueles que utilizarão tecnologia OCR (Optical Character Recognition). O não atendimento a esse padrão técnico básico compromete tanto a validação manual atual (pela dificuldade de leitura de documentos de baixa qualidade) quanto a viabilidade de implementação futura de validação automatizada por OCR.
 
Tabela 3. Distribuição de Resolução de Documentos (DPI)
Faixa de Resolução	Documentos	% do Total	Status Conarq
< 150 DPI (crítico)	79	12,2%	❌ Muito inadequado
150-299 DPI (inadequado)	365	56,5%	❌ Inadequado
300-599 DPI (aceitável)	173	26,8%	✅ Aceitável
≥ 600 DPI (alta qualidade)	23	3,6%	✅ Excelente
Sem imagens detectadas	6	0,9%	⚠️ N/A
Total	646	100,0%	—
< 300 DPI (não conforme)	444	68,7%	❌ Violação Conarq
Fonte: Análise de Qualidade Técnica de Digitalização (peça 106, p. 7). Análise técnica via pdfimages (Poppler Utils) em amostra de 646 documentos. Elaboração: equipe de auditoria.
49.	A inadequação técnica de digitalização compromete simultaneamente as três dimensões de validação analisadas neste achado (peça 106, p. 9), isto é: dificulta ou inviabiliza validação automatizada (68,7% dos documentos com DPI abaixo de 300 violam o padrão Conarq para OCR, sendo 12,2% em nível crítico com texto borrado ou “pixelizado”); compromete validação de acurácia de área (a extração automatizada de valores numéricos mediante IA apresenta taxa de erro elevada em documentos com baixa resolução); e compromete auditabilidade futura.
50.	Em conformidade com o estabelecido no parágrafo 159.1 das Normas de Auditoria do Tribunal (NAT), as conclusões quantitativas apresentadas neste achado podem ser extrapoladas para as respectivas populações, uma vez que foram empregadas metodologias estatísticas com grau de incerteza quantificado.
51.	A conclusão sobre a taxa de 27,1% de documentos semanticamente inadequados pode ser extrapolada para a população total de 11.377.318 documentos. A seleção da amostra de 646 documentos utilizou amostragem aleatória estratificada — para permitir diagnóstico específico por tipologia documental — e parametrizou-se com intervalo de confiança de 99% e margem de erro de ±4,5 pontos percentuais. A adoção desse nível de rigor estatístico (superior ao padrão de 95%) fundamenta-se na alta materialidade dos programas suportados pelo cadastro (superiores a R$ 60 bilhões anuais) e na criticidade dos riscos de elegibilidade identificados. Similarmente, a conclusão sobre a taxa de 53,55% de divergências críticas de área é extrapolável para a população de documentos com área válida identificável, com intervalo de confiança de 95% e margem de erro de ±6,44 pontos percentuais (detalhamento no Apêndice V).
Causas
Causas raiz (processuais e de governança)
Causa raiz 1 – Inadequação do processo de validação e asseguramento da qualidade dos documentos e dados do CAF, incompatível com a escala e criticidade do cadastro.
52.	Embora o CAF exija a anexação de documentos comprobatórios, o arranjo operacional resulta em delegação da verificação da adequação semântica dos documentos e da acurácia dos dados a um processo manual executado pela rede de cadastradores, o qual se mostra intrinsecamente inviável, dada a escala de 11.377.318 documentos atualmente cadastrados. Essa inadequação do processo de validação (por desenho/capacidade) cria uma lacuna de controle na entrada e na manutenção do acervo documental, permitindo a aceitação e a permanência de documentos manifestamente inadequados e inconsistências relevantes sem detecção e correção tempestivas.
Causa raiz 2 – Ausência de um processo efetivo de garantia da qualidade técnica da digitalização, com requisitos e bloqueios mínimos para assegurar legibilidade e futura tratabilidade.
53.	A baixa qualidade das imagens decorre da ausência de controles de qualidade técnica no processo de digitalização, o que permite a permanência de documentos em padrões inferiores ao recomendado (ex.: 300 DPI), comprometendo a leitura/validação e a viabilidade de automação futura.
Causas contributivas (controles e meios insuficientes)
Causa contributiva 1 – Insuficiência de controles preventivos/detectivos na entrada documental (validação semântica do conteúdo e aderência do tipo documental), que reduz a efetividade e a escalabilidade do processo de validação.
54.	As regras de negócio contemplam a obrigatoriedade de anexação de documentos, porém não estabelecem validações automatizadas do conteúdo semântico; as validações previstas consultam bases externas, não o teor dos documentos, o que permite anexação de documentos incompatíveis com a categoria selecionada e dificulta a confirmação de requisitos por evidência documental. A Figura 3 apresenta exemplos de inadequação semântica de documentos comprobatórios no CAF.
Figura 2. Exemplos de inadequação semântica de documentos comprobatórios no CAF
  	 

À esquerda: Carteira de Identidade (RG) classificada como "documento de imóvel", sem qualquer relação com comprovação de propriedade ou posse de terra (peça 103, p. 12).
À direita: Planta topográfica georreferenciada que, embora técnica, não comprova direitos de propriedade ou posse conforme exigido pela Portaria - MDA 19/2025, art. 8º (peça 108, p. 5). Todos os casos evidenciam ausência de validação semântica no momento do upload, permitindo que documentos manifestamente inadequados sejam aceitos pelo sistema.
Fonte: Amostra probabilística de 646 documentos do AWS S3 caf-prod-mapa (peça 103, p. 12-13). Análise via Claude Vision AI. Elaboração: equipe de auditoria.
Causa contributiva 2 – Limitações de interoperabilidade/verificação cruzada com bases georreferenciadas oficiais, restringindo a capacidade de validação de área e requisitos legais correlatos.
55.	A ausência de integração do CAF com bases georreferenciadas oficiais (como Sigef e Sicar) impede a validação automática de dados de área no momento do cadastramento; embora o sistema permita a importação de dados de bases do Incra em etapas específicas, não há mecanismo de cruzamento automatizado para validar o dado declarado; em relação ao Sicar (CAR), a própria gestão do MDA informou em reunião técnica que os cruzamentos automáticos com essa base são planejados apenas "futuramente" (peça 72, p. 2), confirmando que a validação documental da área de imóveis rurais carece de automação com essa base cartográfica essencial.
Causa contributiva 3 – Fragilidades estruturais na captura/registro de área (potenciais erros sistemáticos), não mitigadas por validações de consistência.
56.	O padrão sistemático de divergência agregada (+120,89%) sugere causas estruturais (p. ex., conversão de unidades alqueires/hectares, registro de área útil vs. total, agregação de propriedades, desatualização entre documento e dado cadastrado), sem que haja mecanismos eficazes de detecção/correção no fluxo.
Efeitos (Impactos Reais e Concretos)
E1) Inviabilidade de confirmação documental da elegibilidade para parcela expressiva da base
57.	A situação identificada produz efeitos reais concretos que já comprometem a gestão do do CAF e a efetividade das políticas públicas de agricultura familiar. A presença de cerca de 3,08 milhões de documentos semanticamente inadequados resulta na impossibilidade prática de o Sistema do CAF atestar que os beneficiários correspondentes cumprem os requisitos cumulativos estabelecidos na Lei 11.326/2006 (peça 140, p. 3-4). Isso significa que, para aproximadamente um quarto da base de cadastros, não há como confirmar se os beneficiários atendem às condições legais, comprometendo a função primordial do CAF como instrumento de habilitação prévia.
E2) Comprometimento da base de dados para validação de requisitos legais de área
58.	A identificação de 1,44 milhão de documentos com divergências críticas superiores a 10% (agravada pela divergência sistemática de +121%) resulta em dados de área não confiáveis para fins de validação do requisito legal de 4 módulos fiscais (peça 109, p. 7). Dados com essa magnitude de divergência não podem ser utilizados com segurança para planejamento, dimensionamento de recursos ou monitoramento de programas, comprometendo a capacidade do sistema de cumprir sua função regulatória.
E3) Obstrução técnica à automação e à auditabilidade do acervo documental
59.	A identificação de que 68,7% dos documentos digitalizados (aproximadamente 2,33 milhões) apresentam resolução inferior a 300 DPI dificulta ou impossibilita a implementação de tecnologias de OCR e a validação semântica automatizada (peça 106, p. 15). Tal deficiência perpetua a dependência de validação manual (inviável pela escala) e compromete a auditabilidade futura do acervo.
Riscos (Impactos Potenciais)
R1) Risco de desvio de finalidade e aplicação indevida de recursos públicos (Pronaf, PAA e PNAE)
60.	Uma vez que a elegibilidade de 3,08 milhões de cadastros não pode ser comprovada documentalmente (peça 140, p. 3-4), existe o risco crítico de que recursos de programas que utilizam o CAF como habilitação prévia estejam sendo direcionados a beneficiários que não atendem aos critérios legais.
R2) Risco de insegurança jurídica e responsabilização de gestores e beneficiários
61.	A taxa de inadequação documental de 27,1% pode gerar insegurança jurídica tanto para gestores (risco de responsabilização por concessão indevida) quanto para beneficiários (risco de suspensão de direitos e questionamento posterior da elegibilidade, mesmo após anos de participação regular nos programas).
R3) Risco de agravamento sistêmico por inércia operacional e crescimento do passivo
62.	Caso não sejam implementadas correções sistêmicas, os problemas documentados tendem a se agravar. Considerando a taxa de crescimento de ~3,5% ao mês (peça 140), em nove meses a quantidade de documentos inadequados pode ultrapassar 4 milhões, tornando a correção progressivamente mais complexa e custosa. Este risco de agravamento por inércia é severo, pois as causas são corrigíveis mediante medidas técnicas viáveis, ao passo que a omissão resultará em custos crescentes.
Conclusão
63.	A auditoria evidenciou inadequações sistêmicas que comprometem a capacidade do CAF de validar requisitos de elegibilidade da agricultura familiar com base em documentação comprobatória e em dados confiáveis. Na amostra, 27,1% dos documentos apresentaram inadequação semântica, com projeção para aproximadamente 3,08 milhões de documentos problemáticos na população; adicionalmente, foram identificadas inconformidades relevantes em documentos de imóvel e divergências críticas de área em parcela expressiva dos casos com área identificável.
64.	As evidências indicam que a causa raiz reside na inadequação do processo de validação e asseguramento da qualidade (por desenho/capacidade) frente à escala do acervo, com dependência de validação manual intrinsecamente inviável; essa lacuna é agravada por controles tecnológicos insuficientes (ausência de validação do conteúdo semântico e limitações de verificação cruzada com bases georreferenciadas oficiais) e pela ausência de controles de qualidade técnica de digitalização, que prejudica tanto a validação atual quanto a viabilidade de automação futura.
65.	A equipe reconhece que o MDA, gestor do CAF, tem demonstrado esforços para aprimoramento contínuo do sistema. A implementação da versão CAF 3.0 representou evolução em relação às versões anteriores, como evidenciado pelo fato de que 98,7% das propriedades que excedem 4 módulos fiscais foram cadastradas antes dessa versão, indicando que os controles implementados no CAF 3.0 reduziram — embora não tenha eliminado — o cadastramento de propriedades inelegíveis.
66.	A equipe reconhece também que o gestor enfrenta desafios operacionais significativos que contribuem para os problemas identificados. A escala de 11,4 milhões de documentos e 3,5 milhões de Unidades Familiares cadastradas representa complexidade operacional que inviabiliza validação manual individualizada. A diversidade da agricultura familiar brasileira — abrangendo desde pequenos agricultores em assentamentos até extrativistas, pescadores artesanais, quilombolas e povos indígenas — implica variabilidade de tipos documentais e situações fáticas que desafiam a padronização de processos de validação.
67.	Essas dificuldades, contudo, não eliminam a necessidade de controles adequados, mas justificam e reforçam a urgência de implementação de oportunidades de melhoria que podem gerar benefícios significativos. Entre os benefícios destacam-se: maior confiabilidade da base cadastral de documentos comprobatórios (a correção dos 3,08 milhões de documentos semanticamente inadequados e dos 1,44 milhão com divergências de área permitirá validar com segurança a elegibilidade de milhões de agricultores familiares); economia de recursos públicos (a validação automatizada de requisitos legais e a integração com bases oficiais reduzirão o risco de direcionamento indevido de recursos de programas federais; ganhos de eficiência operacional; e redução de retrabalho).
68.	Entre os benefícios qualitativos destacam-se: fortalecimento da credibilidade do CAF como instrumento confiável de habilitação prévia, perante órgãos executores de políticas públicas e de órgãos de controle; segurança jurídica para gestores públicos e beneficiários, mitigando riscos de responsabilização por concessão ou recebimento de benefícios com base em documentação inadequada; transparência e rastreabilidade das decisões de elegibilidade, permitindo auditabilidade dos critérios aplicados; e efetividade das políticas públicas de agricultura familiar.
69.	Sem a implementação coordenada de melhorias, o CAF corre o risco de não cumprir sua finalidade legal de garantir que os benefícios da agricultura familiar alcancem exclusivamente quem comprova, documentalmente e faticamente, atender aos requisitos estabelecidos pela Lei 11.326/2006.
Propostas de Encaminhamento
70.	D1) Para reduzir os riscos de uso do CAF com baixa confiabilidade para implementação de políticas públicas, a Unidade Técnica propõe determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução - TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação, com responsáveis e prazos, para avaliar as falhas na qualidade de dados e de documentos do CAF apontadas no relatório de auditoria e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial: 
70.1.	documentos inadequados para comprovar os requisitos de elegibilidade;
70.2.	documentos de imóveis que apresentam divergências críticas de área em relação à base de dados;
70.3.	documentos com resolução inferior ao padrão definido pela Resolução - Conarq 31/2010.
71.	Espera-se que o saneamento conjunto dessas falhas aumente a confiabilidade da comprovação de elegibilidade no CAF, com redução de inconsistências documentais e territoriais, maior robustez das análises e menor risco de decisões baseadas em registros inadequados.
72.	E1) Para reduzir a recorrência de inconsistências documentais no CAF, aumentar a confiabilidade dos registros para fins de elegibilidade e diminuir o retrabalho de saneamento, a Unidade Técnica propõe recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução - TCU 315/2020, que:
72.1.	reavalie e aperfeiçoe os processos de cadastramento, atualização e controle de qualidade do CAF, de forma a torná-lo compatível com a escala e a criticidade do cadastro para implementação de políticas públicas da agricultura familiar, contemplando mecanismos de prevenção à inserção e permanência de dados inválidos, em especial:
72.1.1.	padronização de procedimentos para cadastramento e atualização do CAF pela rede de cadastradores, incluindo validação e garantia de qualidade de documentos, revisão periódica baseada em risco/amostragem e mecanismos de orientação e supervisão dos cadastradores;
72.1.2.	 aperfeiçoamento das regras de negócio e implementação de controles automatizados de validação em campos críticos, com ênfase na qualificação e validação dos documentos anexados;
72.1.3.	 interoperabilidade com bases oficiais pertinentes (ex.: bases geoespaciais oficiais), para detecção tempestiva de anomalias e redução de retrabalho de saneamento;
72.1.4.	 adoção de requisitos mínimos de qualidade técnica dos documentos digitalizados, inclusive padrão de resolução compatível que assegure validação automatizada e auditabilidade do acervo, a exemplo do padrão de resolução de 300 DPI definido pela Resolução - Conarq 31/2010.
73.	Espera-se que a implementação dessas medidas fortaleça a comprovação de elegibilidade, aumente a auditabilidade dos registros e diminua o custo operacional associado ao saneamento dos dados do Cadastro.
74.	Para fortalecer a governança da qualidade do CAF e tornar mais efetiva a priorização e o acompanhamento das ações de saneamento, a Unidade Técnica recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução - TCU 315/2020, que desenvolva e implemente mecanismos de acompanhamento gerencial (tais como relatórios periódicos, painéis de indicadores ou dashboards) para monitoramento contínuo da qualidade dos documentos e das informações constantes do CAF, de modo a subsidiar a priorização de ações corretivas e a avaliação da efetividade das medidas adotadas para aprimoramento da qualidade cadastral e documental do Cadastro.
75.	Espera-se que o monitoramento gerencial contínuo do CAF permita identificar com maior tempestividade tendências de deterioração, direcionar recursos para problemas de maior impacto E acompanhar a execução das correções com base em dados mais precisos e tempestivos.
3.2.	Achado II: Regressões em transições tecnológicas e passivo histórico deterioram a qualidade cartográfica e fragilizam a integridade geoespacial do CAF, comprometendo a rastreabilidade e validações baseadas em localização
Síntese: A avaliação da base de 3,17 milhões de imóveis rurais revelou deterioração da qualidade geoespacial: a migração para o CAF 3.0 causou aumento de 40,6% na taxa total de erros cartográficos (de 32,7% para 45,9%), por relaxamento das validações de bounding box. Foram identificadas 8.527 duplicações espaciais exatas em 4.016 localizações, 147 municípios com "inflação cadastral" (área cadastrada superior à oficial), totalizando 16,5 milhões de hectares excedentes, e passivo de 11,65 milhões de coordenadas com precisão insuficiente. As causas incluem regressão de controles nas transições tecnológicas, ausência de validação cruzada com malha IBGE e acúmulo histórico não saneado.
76.	O CAF constitui a maior base de dados georreferenciados da agricultura familiar brasileira, sendo utilizado também para planejamento territorial, fiscalização ambiental e gestão de políticas públicas agrárias. Assim, a qualidade dos dados geoespaciais é condição sine qua non para que o CAF cumpra sua função de instrumento de identificação e qualificação dos agricultores familiares.
77.	Desse modo, a equipe de auditoria realizou avaliação sistemática da qualidade cartográfica, cobrindo as dimensões de acurácia posicional (PT-05, peça 114), consistência lógica (PT-07, peça 116) e integridade territorial (PT-08, peça 117; PT-12, peça 121).
78.	A avaliação norteou-se pelas seguintes subquestões específicas (peça 121, p. 5): 
(i)	Qual o impacto das mudanças tecnológicas (Interface Leaflet e Sistema CAF 3.0) na taxa de erros cartográficos? 
(ii)	Qual a magnitude das duplicações espaciais e seu impacto na unicidade dos beneficiários? 
(iii)	Qual a extensão do fenômeno da "inflação cadastral" (área cadastrada superior à área oficial do município)?
79.	A população analisada compreende 3.175.345 imóveis rurais cadastrados (extração da base de dados de 2/9/2025; peça 110, p. 4), dos quais foram extraídas quatro amostras estratificadas temporais (n=63.588 registros, peca 113, p. 9) correspondentes às transições tecnológicas do sistema: (i) baseline (linha de base) CAF 2.x (anterior a março/2025); (ii) implementação CAF 3.0 (março/2025); (iii) período pré-Leaflet (anterior a agosto/2025); e (iv) implementação Leaflet (agosto/2025 em diante), conforme documentado no Papel de Trabalho PT-04 –Extração Amostral  Estratificada (peça 113, p. 4-9). A estratificação temporal permitiu análises comparativas do tipo "antes vs depois" para avaliar os impactos de cada transição de sistema na qualidade cartográfica e integridade geoespacial dos dados.
Situação Encontrada
80.	A análise de qualidade cartográfica classifica erros em duas categorias fundamentais com implicações distintas (peça 114, p. 6-7): erros algorítmicos (ou sintáticos) referem-se a coordenadas que violam as regras matemáticas básicas do sistema de coordenadas geográficas (latitude de 0° a 90° Norte/Sul, longitude de 0° a 180° Leste/Oeste, indicando a distância angular da Linha do Equador e do Meridiano de Greenwich, respectivamente, onde o sinal de negativo indica Sul/Oeste), que podem ser sintetizados como: 
80.1.	latitude fora do intervalo [-90º, 90º]; 
80.2.	longitude fora do intervalo [-180º, 180º]; ou 
80.3.	coordenadas fora dos limites físicos do território brasileiro: latitude não pertence (∉) ao intervalo [−34º, 6º] e longitude ∉ ao intervalo [−74º, −34º].
81.	Esse tipo de erro é facilmente detectável por validação de formato e, por esse motivo, essa questão foi analisada de modo censitário.
Figura 3. Comparação Visual entre Erros Algorítmicos (Detectáveis por Validação de Formato) e Erros Geoespaciais (Requerem Validação Cruzada com Bases Oficiais)
 
Fonte: Peça 114 (PT-05). Painel superior: representação esquemática dos padrões de erros geoespaciais — à esquerda, erros algorítmicos (pontos vermelhos fora do envelope brasileiro, detectáveis por validação de formato); à direita, erros geoespaciais (pontos laranja em município incorreto, requerem validação cruzada com base de dados do IBGE). Painel inferior: distribuição quantitativa (12.231 erros algorítmicos, 19,2%; 51.357 coordenadas válidas, 80,8%) e caracterização dos tipos de erro. A distinção é metodologicamente relevante: erros algorítmicos permitem análise censitária, enquanto erros geoespaciais demandam amostragem estatística.
82.	Já erros geoespaciais (ou semânticos) referem-se a coordenadas sintaticamente válidas, mas semanticamente incorretas, como coordenadas que localizam o imóvel em município diferente do declarado quando cruzadas com a malha oficial do IBGE (peça 116, p. 14). Esse tipo de erro exige validação cruzada com bases geoespaciais de referência, tornando a detecção mais complexa. 
83.	Enquanto erros algorítmicos indicam falha básica de validação de interface, erros geoespaciais podem decorrer de imprecisão na coleta, seleção incorreta no mapa ou desconhecimento do usuário sobre a localização exata do imóvel.
Advento do CAF 3.0: Regressão de Controles e Desalinhamento Normativo
84.	O advento do CAF 3.0 em 26/3/2025 (peça 119, p. 4), apesar de ter introduzido melhorias significativas no sistema em relação à versão 2.x anterior, falhou em relação à qualidade dos dados geoespaciais. A mudança de versão causou deterioração crítica, com aumento de 40,6% na taxa total de erro, que subiu de 32,66% para 45,92% (afetando ~1,46 milhão de imóveis; peça 119, p. 9), em desconformidade com o dever de promover a melhoria da qualidade e fidedignidade dos dados estabelecido no Decreto 10.046/2019, art. 1º, inciso IV. 
85.	Durante a migração para o CAF 3.0, as validações de bounding box (envelope geográfico) do Brasil que existiam na versão 2.x foram relaxadas ou removidas (peça 119, p. 34). Bounding box é um mecanismo de verificação que define os limites extremos norte, sul, leste e oeste de uma região; qualquer coordenada fora desse "retângulo" deve ser rejeitada pelo sistema. Enquanto o CAF 2.x rejeitava parte das coordenadas fora do território brasileiro, o CAF 3.0 passou a aceitar coordenadas desde que estejam no intervalo mundial válido (latitude ∈ [−90º, 90º], longitude ∈ [−180º, 180º]), sem verificar se pertencem ao envelope geográfico brasileiro (latitude ∈ [−34º, 6º], longitude ∈ [−74º, −34º]). Esse relaxamento de controle explica o aumento de +11,76 p.p. nos erros algorítmicos.
Figura 4. Evolução dos erros ao longo da introdução do CAF 3.0
 
Nota: Análise comparativa de amostra estratificada antes (n=16.456) e depois (n=16.272) da atualização do sistema CAF 3.0 (26/3/2025). Fonte: PT-03 e PT-10 (peças 112 e 119, p. 10 e p. 4, respectivamente).
86.	A deterioração observada no CAF 3.0 apresentou perfil distinto das transições típicas de sistemas: enquanto migrações tecnológicas geralmente operam trade-offs (resolvem um tipo de problema, mas podem introduzir outro), o CAF 3.0 piorou simultaneamente ambos os tipos de erro. Os erros algorítmicos (coordenadas sintaticamente inválidas) aumentaram de 20,31% para 32,07% (+11,76 p.p., +57,9%), e os erros geoespaciais (coordenadas válidas, mas em município errado) aumentaram de 12,35% para 13,85% (+1,50 p.p., +12,1%).
87.	Verifica-se, assim, que a mudança de versão possivelmente não foi conduzida com boas práticas de gestão de configuração (como as recomendadas no objetivo BAI10 do Cobit 9), capazes de assegurar baselines, controle de versões, rastreabilidade e verificações de impacto (como testes de regressão) sobre itens de configuração críticos que afetam a qualidade geoespacial.
Introdução do Leaflet: O Trade-off Algorítmico-Semântico e Benefício de Auditoria
88.	A implementação da interface Leaflet (em 15/8/2025) (peça 118, p. 6) substituiu a digitação manual de coordenadas pela seleção visual em mapa. Essa mudança operou um trade-off algorítmico-semântico estatisticamente significativo: eliminou erros de digitação, mas incentivou a imprecisão geográfica por falta de travas de consistência municipal.
89.	Cabe registrar que a implementação do Leaflet ocorreu durante a execução da presente auditoria, após a equipe ter constatado e comunicado erros preliminares ao gestor já na reunião de abertura (peça 72, p. 1). Visto que não havia previsão anterior no planejamento de TI do MDA para adoção desta interface específica (conforme verificado no PDTIC), a implementação é considerada um benefício indireto da ação de controle, motivada pela demonstração da gravidade dos erros de digitação manual pela equipe de auditoria.
Figura 5. Trade-off algorítmico-semântico na transição Leaflet
 
Fonte: PT-09 (Análise Estratificada Temporal Leaflet; peca 118, p. 16), Memórias de Cálculo MC-095 e MC-096 (peca 118, p. 36). Amostra: 16.501 registros (E1: pré-agosto/2025) + 14.359 registros (E2: pós-agosto/2025). Intervalo de Confiança: 99%. O slope graph evidencia a transformação radical do perfil de erros: erros algorítmicos caíram de 22,22% para 0,01% (-99,95%), enquanto erros geoespaciais aumentaram de 11,83% para 32,46% (+174%). A taxa total de erro teve redução modesta de apenas 1,58 p.p. (de 34,05% para 32,47%)
90.	Na transição Leaflet, os erros algorítmicos caíram de 22,22% para 0,01%. Em contrapartida, os erros geoespaciais aumentaram de 11,83% para 32,46%, resultando em uma taxa total de erro que caiu apenas 1,58 p.p. (de 34,05% para 32,47%; peça 118, p. 16).
Tabela 4. Trade-off algorítmico-semântico na transição Leaflet: eliminação de erros de formato às custas de erros de conteúdo
Período	Erros Algorítimicos	Erros Geospaciais	Taxa Total de Erro
Pré-Leaflet (E1)	22,22%	11,83%	34,05%
Pós-Leaflet (E2)	0,01%	32,46%	32,47%
Variação	-22,21 p.p	+20,63 p.p.	-1,58 p.p.
Fonte: PT-09 – Análise Estratificada Temporal Leaflet (peça 118, p. 16). Amostra: 16.501 registros (E1) + 14.359 registros (E2). Intervalo de Confiança: 99%.
91.	A interface Leaflet permite que o usuário clique livremente no mapa sem que o sistema verifique se o ponto está dentro do município declarado (peça 118, p. 36). Esse problema é agravado em municípios de pequena extensão ou áreas de fronteira, onde cliques imprecisos resultam em localização indevida em municípios vizinhos (peça 118, p. 24). 
92.	Assim, a causa raiz do trade-off observado na implementação do Leaflet foi a ausência de validação de consistência entre a coordenada selecionada e o município declarado no formulário. Assim, enquanto erros algorítmicos foram virtualmente eliminados (-99,95%), os erros geoespaciais aumentaram (+174%).
Precisão Decimal e Consistência Espacial
93.	As transições também causaram regressões na precisão decimal. A interface Leaflet causou perda de 14,33 p.p. em alta precisão (>= 5 casas decimais). A análise de consistência espacial identificou que 15,92% dos registros de alta precisão (6.976 de 43.812 registros) apresentam coordenadas localizadas fora do município declarado, projetando-se para aproximadamente 431.000 imóveis na população de alta precisão (peças 115, p. 6 e 116, p. 14).
94.	Dentre os 6.976 registros com inconsistência espacial, destaca-se um subconjunto de 722 registros (1,65% da amostra de alta precisão) cujas coordenadas apontam para Unidade da Federação (UF) completamente diferente da declarada. Trata-se de erro que pode indicar falha sistêmica na validação ou conduta deliberada de cadastramento em região diversa da real, requerendo investigação específica para identificação de padrões e eventuais responsabilizações (peça 116, p. 14 e 21).
Duplicações Espaciais e o Caso Salvador
95.	A análise de duplicações da amostra de 43.182 imóveis revelou que 55,27% dos registros de alta precisão compartilham coordenadas idênticas com outros imóveis (projeção de ~1,75 milhão de imóveis duplicados espacialmente). Isso inviabiliza cruzamentos com bases de dados de outros sistemas de informação, como o Sistema de Detecção de Desmatamento em Tempo Real (DETER) do Instituto Nacional de Pesquisas Espaciais (INPE). A identificação dessas duplicatas utilizou o cálculo da distância haversine, que permite medir a distância linear entre dois pontos sobre uma esfera (a Terra) a partir de suas latitudes e longitudes; registros com distância zero (duplicatas exatas) indicam que os pontos ocupam o exato mesmo lugar geográfico no sistema.
Tabela 5. Resumo quantitativo de duplicações espaciais em registros de alta precisão
Categoria	Total	% do Total
Únicos espacialmente	19.404	44,29%
Duplicatas exatas (h=0)	24.215	55,27%
Duplicatas próximas (0<h<10m)	158	0,36%
Clusters densos (>=3 pts/100m)	35	0,08%
Total	43.812	100%
Fonte: PT-08 – Análise de Duplicações Espaciais (peça 117, p. 14, Tabela 3). Amostra: 43.812 registros de alta precisão (≥5 casas decimais).
96.	A Tabela 5 classifica os registros de alta precisão em quatro categorias hierárquicas de qualidade espacial (peça 117, p. 10-13): (i) únicos espacialmente, imóveis sem nenhum outro cadastro a menos de dez metros, representando a situação ideal de rastreabilidade individual; (ii) duplicatas exatas, múltiplos imóveis cadastrados com coordenadas geográficas idênticas (distância haversine = 0), impossibilitando distinção espacial; (iii) duplicatas próximas, imóveis distintos com coordenadas separadas por menos de dez metros, possivelmente decorrentes de erro de GPS ou arredondamento; e (iv) clusters densos, aglomerações de três ou mais imóveis dentro de um raio de cem metros, que podem representar assentamentos rurais legítimos de alta densidade (comunidades tradicionais, assentamentos de reforma agrária) ou erros sistemáticos de cadastramento em lote, requerendo investigação adicional para distinção.
Nota Técnica: A distância haversine é uma fórmula matemática que permite o cálculo da distância entre dois pontos em uma esfera (como a Terra) a partir de suas latitudes e longitudes, sendo preferível ao cálculo euclidiano simples para grandes áreas ou em coordenadas geográficas.
97.	Estudo de Caso: Salvador/BA. O município de Salvador/BA apresentou o caso mais emblemático de duplicação espacial massiva identificado na auditoria: 6.644 imóveis rurais cadastrados compartilham exatamente a mesma coordenada (latitude -12,960000°, longitude -38,510000°), o que representa 1,46% de todas as duplicações do sistema, concentradas em um único ponto. Essa coordenada corresponde aproximadamente ao Centro Histórico de Salvador (região da Praça da Sé), área urbana consolidada, onde a existência de milhares de propriedades rurais distintas é fisicamente impossível, evidenciando o uso da sede municipal como referência geográfica genérica inadequada para a localização real dos imóveis rurais. O fenômeno ocorreu exclusivamente na Bahia e se desenvolveu progressivamente ao longo de 445 dias (junho/2024 a setembro/2025), sugerindo prática sistemática, e não evento isolado.
98.	O caso evidencia falha crítica de validação: o sistema aceita coordenadas sintaticamente válidas, porém semanticamente incompatíveis com o contexto (área urbana registrada como imóvel rural), sem mecanismos para rejeitar coordenadas em áreas urbanas, detectar concentrações anômalas (milhares de registros no mesmo ponto) ou impor checagens de plausibilidade territorial. A interface Leaflet, ao facilitar a seleção por clique, pode ter incentivado a escolha do ponto mais visível/referencial do município (centro urbano) em detrimento da localização real do imóvel, resultando na criação de uma "sobreposição" massiva que compromete totalmente a rastreabilidade individual desses cadastros.
99.	A nova interface reduziu duplicações em cadastros novos, mas não houve curadoria do passivo histórico: 92,36% dos registros pré-Leaflet possuem duplicatas, enquanto no pós-Leaflet a taxa caiu para 16,59%. O passivo acumulado permanece ativo e sem correção.
Tabela 6. Comparação de duplicações: Entrada Manual (E1) vs. Interface Leaflet (E2)
Categoria	E1 
(Antes Leaftlet)	%E1	E2 
(Depois Leaftlet)	%E2
População total	11.626	100%	10.948	100%
Únicos	883	7,60%	9.006	82,26%
Duplicatas exatas	10.738	92,36%	1.816	16,59%
Duplicatas próximas	5	0,04%	102	0,93%
Clusters densos	0	0,00%	24	0,22%
Total com duplicações	10.743	92,40%	1.942	17,74%
Redução				-74,66 p.p.
Fonte: PT-08 (Análise Estratificada Leaflet; peça 117, p. 14, Tabela 4). Período E1: antes de 15/8/2025 (entrada manual). Período E2: depois de 15/8/2025 (interface Leaflet).
 
Tabela 7. Comparação de duplicações: CAF 2.x – Antes do CAF 3.0 (E3) vs. Depois do CAF 3.0 (E4)
Categoria	E3 
(Antes CAF 3.0)	%E3	E4 
(Depois CAF 3.0)	%E4
População total	11.714	100%	9.524	100%
Únicos	3.891	33,22%	5.624	59,05%
Duplicatas exatas	7.770	66,32%	3.845	40,38%
Duplicatas próximas	53	0,45%	51	0,54%
Clusters densos	0	0,00%	4	0,04%
Total com duplicações	7.823	66,78%	3.900	40,95%
Redução				-25,83 p.p.
Fonte: PT-08 (Análise Estratificada CAF 3.0; peça 117, p. 15, Tabela 5). Período E3: antes de 26/3/2025 (CAF 2.x). Período E4: depois de 26/3/2025 (CAF 3.0).
100.	A análise da distribuição territorial das duplicações espaciais revela concentração crítica em municípios amazônicos e de fronteira agrícola (peça 117, p. 17, 19), indicando que a duplicação não é fenômeno uniforme, mas concentrado territorialmente em regiões com características comuns de ocupação e cadastramento.
Inflação Cadastral Territorial
101.	O município de Penalva/MA representa o caso mais extremo de inflação cadastral (peça 121, p. 9, Memória de Cálculo MC-121), com área cadastrada de 1.801.074 km² — 2.248 vezes a área oficial de 801 km², o que equivale isoladamente a 21,16% do território brasileiro (8.515.767 km²). A análise temporal comparando períodos antes e depois da implementação do CAF 3.0 (26/3/2025) revelou efetividade substancial da transição na redução de novos casos de inflação: a taxa caiu de 10,89% para 0,31%, evidenciando que o CAF 3.0 implementou validações de plausibilidade para cadastros novos. Contudo, a transição não corrigiu o passivo histórico: os 632 municípios com inflação cadastral (peça 121, p. 9, Memória de Cálculo MC-119; análise da base completa, não amostral) incluem predominantemente registros antigos não migrados ou não reavaliados durante a transição para o CAF 3.0.
Tabela 8. Síntese das situações do Achado de Qualidade Cartográfica e de Integridade Geoespacial
Situação	Métrica	Estimativa Pontual	IC 99% / Variação	População Afetada (Projeção)
Qualidade Cartográfica
Deterioração CAF 3.0 (taxa de erro)	Taxa E4 vs E3	45,92% vs 32,66%	Δ = +13,26 p.p. (+40,6%)	1.458.374 registros com erro (E4)
Transformação Leaflet (erros geoespaciais)	Taxa E2 vs E1	32,46% vs 11,83%	Δ = +20,63 p.p. (+174%)	—
Regressão precisão decimal Leaflet	Alta precisão E2 vs E1	76,26% vs 90,59%	Δ = −14,33 p.p. (−15,8%)	≈ 454.863 registros perderam precisão (estimativa)
Inconsistência municipal	Registros fora do município	15,92%	—	≈ 431.000 registros inconsistentes
Integridade Geoespacial
Duplicações espaciais exatas	Coordenadas idênticas	55,27% (alta precisão)	—	24.215 registros duplicados
Inflação cadastral municipal	Municípios com área > área registrada na base do IBGE	11,43% (632/5.528)	Inflação até 2.248×	632 municípios impossíveis
Inflação crítica (>10×)	Municípios extremos	1,07% (59/5.528)	Inclui 12 casos >100×	59 municípios com dados inválidos
Fonte: PT-04 a PT-12, MC_MASTER_INDEX v2.9 (130 Memórias de Cálculo rastreadas; peça 122). Elaboração: equipe de auditoria.
102.	Em conformidade com o parágrafo 159.1 das NAT, as conclusões apresentadas neste achado podem ser generalizadas para a população total de 3.175.345 imóveis rurais cadastrados (peça 110, p. 4), uma vez que a seleção da amostra de 63.588 registros (peça 113, p. 9) — cerca de duas vezes maior que o mínimo estatístico de ~30.860 registros exigido pelo dimensionamento inicial (peça 111, p. 6) — ocorreu de forma probabilística mediante estratificação temporal proporcional, com intervalo de confiança de 99% e margem de erro efetiva de ±0,40 pontos percentuais (peça 122, p. 6, Memória de Cálculo MC-070/PT-06). Tais parâmetros de alta precisão foram adotados deliberadamente para assegurar a máxima robustez das extrapolações, considerando a criticidade do CAF como instrumento habilitador de políticas públicas de alta materialidade (ex.: Pronaf). Quanto à análise de inflação cadastral, trata-se de verificação censitária sobre a totalidade da base ativa, não requerendo extrapolação amostral.
Causas
Causas raiz (processuais e de governança)
Causa raiz 1 – Deficiência na gestão de mudanças e garantia de qualidade tecnológica.
103.	As transições para o CAF 3.0 e a interface Leaflet evidenciam a ausência de testes de regressão capazes de detectar a deterioração de controles e trade-offs negativos antes da entrada em produção da nova versão do sistema. A implementação de novas funcionalidades sem a devida validação de impactos em controles existentes permitiu a regressão da qualidade cartográfica.
Causa raiz 2 – Insuficiência de governança e monitoramento contínuo da qualidade geoespacial.
104.	A inexistência de métricas formais, painéis (dashboards) e rotinas de monitoramento permitiu que taxas elevadas de erro e duplicações espaciais massivas passassem despercebidas pela gestão do sistema ao longo de meses.
Causa raiz 3 – Ausência de processo de curadoria do passivo histórico
105.	A estratégia de melhoria tecnológica focou exclusivamente na interface de novos cadastros, sem estabelecer um plano de remediação para o estoque de dados preexistente. Como resultado, duplicações críticas e a inflação cadastral de transições anteriores permanecem ativas na base.
Causa raiz 4 – Insuficiência na formalização de requisitos de qualidade como requisitos não funcionais.
106.	A inexistência de etapas de controle de qualidade claros e requisitos não funcionais formalizados para a integridade geoespacial permitiu que alterações sistêmicas priorizassem a entrega e usabilidade (Leaflet) em detrimento da consistência semântica dos dados.
Causa raiz 5 – Fragilidades nas práticas e supervisão da rede de cadastradores.
107.	Padrões como a “referência de sede municipal” e as duplicações massivas (caso Salvador) indicam uma prática sistemática de cadastramento inadequado. A causa raiz reside na deficiência de orientação, supervisão e incentivos para a precisão geográfica na ponta, sendo o controle tecnológico apenas o meio mitigador.
Causas contributivas (técnicas e de controle)
Causa contributiva 1 – Insuficiência de controles técnicos de validação e plausibilidade.
108.	A fragilidade dos filtros automatizados na entrada de dados e a ausência de mecanismos de trava baseados em regras de negócio geoespaciais permitem a entrada e permanência de registros com inconsistências severas na base de dados, sem que o sistema realize críticas automáticas de integridade.
Causa contributiva 2 – Interoperabilidade limitada com bases geoespaciais oficiais.
109.	A integração deficiente com APIs de órgãos de referência (IBGE e Incra) reduz a capacidade do sistema de realizar checagens sistemáticas de consistência e integridade territorial no momento da coleta.
Efeitos (Impactos Reais e Concretos)
Inviabilização da rastreabilidade individual e cruzamentos ambientais.
110.	A existência de 1,75 milhão de imóveis com coordenadas idênticas torna impossível distinguir propriedades individualmente para fiscalização de desmatamento ou sobreposição em áreas protegidas.
Comprometimento da validação de elegibilidade quanto ao limite de área
111.	Com taxa de erro cartográfico de 45,92% no CAF 3.0 (afetando ~1,46 milhão de imóveis), não há como validar confiavelmente se as propriedades respeitam o limite legal de 4 módulos fiscais exigido pelo art. 3º, I, da Lei 11.326/2006, fragilizando o controle de acesso a políticas que envolvem bilhões de reais destinados aos beneficiários (como o Pronaf).
Riscos (Impactos Potenciais)
Risco de distorção analítica e de decisões públicas baseadas em evidência inválida.
112.	A fragilidade da base georreferenciada compromete análises territoriais e de planejamento, visto que o CAF é utilizado como insumo para gestão agrária. Dados geográficos incorretos levam a diagnósticos estatísticos distorcidos, o que pode resultar na alocação ineficiente de recursos e em políticas públicas inadequadas à realidade local.
Risco operacional de “poluição” de integrações externas.
113.	Visto que outras instituições (agências de crédito e órgãos ambientais) podem consumir os dados do CAF, os erros sistêmicos identificados podem se propagar para rotinas automatizadas externas. Isso eleva significativamente o custo de governança interorganizacional, exigindo que cada instituição consumidora realize seus próprios saneamentos de dados para evitar o processamento de informações inválidas.
Conclusão
114.	A auditoria identificou indícios relevantes de redução da qualidade cartográfica e fragilidades na integridade geoespacial do CAF, que, no estado atual, podem limitar sua utilização para fins de rastreabilidade fundiária e validação de critérios de elegibilidade baseados em área. As transições tecnológicas recentes, conduzidas sem critério de garantia de qualidade geoespacial, produziram efeitos colaterais críticos: a migração para o CAF 3.0 elevou a taxa de erro cartográfico para 45,92% (afetando 1,46 milhão de registros), enquanto a adoção do Leaflet, embora tenha saneado os erros de formatação (-99,95%), triplicou a incidência de inconsistências geoespaciais (+174%) ao permitir a seleção de coordenadas fora do município declarado. Adicionalmente, a ausência de controles de unicidade permitiu o acúmulo de 1,75 milhão de imóveis com coordenadas duplicadas e a geração de "inflação cadastral" em 632 municípios, chegando a casos extremos de áreas cadastradas 2.000 vezes superiores à extensão territorial oficial.
115.	Os achados demonstram que essas falhas não são meros erros operacionais, mas sintomas de uma lacuna sistêmica de governança de dados. A remoção injustificada de travas de segurança (bounding box) e a ausência de testes de regressão na homologação de novas versões expuseram o sistema a vulnerabilidades que haviam sido mitigadas em versões anteriores. A perpetuação de casos massivos e visíveis evidencia a inexistência de rotinas contínuas de monitoramento e curadoria do passivo, transformando o banco de dados em um repositório cumulativo de inconsistências.
116.	Em consequência, a utilidade pública do dado geoespacial do CAF é limitada. A alta taxa de erro inviabiliza o uso do sistema para cruzamentos automáticos de malhas ambientais e dificulta a verificação confiável do limite legal de quatro módulos fiscais, elevando o risco de concessão indevida de crédito e de formulação de políticas públicas baseadas em diagnósticos territoriais distorcidos. 
117.	Apesar de o Ministério do Desenvolvimento Agrário ter demonstrado esforços para o aprimoramento do Sistema do CAF, as regressões identificadas e a ausência de correção do passivo histórico evidenciam que, apesar dos avanços, permanecem lacunas críticas de controle de qualidade e governança de dados que requerem atenção urgente por parte do órgão gestor do Sistema. Nesse sentido, sem a implementação de medidas de saneamento e governança, o CAF corre o risco de se tornar um cadastro meramente declaratório, despido dos atributos de confiabilidade exigidos para um registro administrativo de Estado.
118.	Os benefícios esperados com a implementação de medidas corretivas incluem:
118.1.	(i) rastreabilidade operacional: a correção de duplicações permitirá análises geoespaciais automatizadas identificarem individualmente cada imóvel, viabilizando fiscalizações em larga escala mediante cruzamento com bases ambientais (DETER, Unidades de Conservação – UCs, CAR); 
118.2.	(ii) controle de elegibilidade: a correção de erros cartográficos permitirá validação automática do requisito legal de área máxima, reduzindo risco de acesso indevido a políticas públicas de agricultura familiar; 
118.3.	(iii) confiabilidade para planejamento: a correção da inflação cadastral permitirá estudos mais acurados sobre distribuição espacial da agricultura familiar e planejamento de investimentos; 
118.4.	(iv) credibilidade institucional: fortalecimento do CAF como fonte oficial de dados geoespaciais perante órgãos governamentais, comunidade científica e sociedade civil; 
118.5.	(v) segurança jurídica: redução de falsos positivos em fiscalizações automatizadas, protegendo agricultores legítimos de autuações indevidas por erros de coordenada; e 
118.6.	(vi) governança de dados: implementação de monitoramento contínuo (dashboards, métricas, metas) criará capacidade de detecção precoce de deteriorações futuras, evitando que problemas se acumulem sem visibilidade da gestão.
Proposta de encaminhamento
119.	D1) Para reduzir o risco de distorções territoriais relevantes no CAF, prevenir a propagação de erros geoespaciais e fortalecer a confiabilidade do cadastro para planejamento e execução de políticas públicas, a Unidade Técnica propõe determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução - TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação, com responsáveis e prazos, para avaliar as falhas na qualidade de dados e de documentos do CAF apontadas no relatório de auditoria e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial:
119.1.	o passivo histórico de dados geoespaciais com falhas, em especial duplicações espaciais, inflação cadastral e inconsistências municipais.
120.	Espera-se que o tratamento estruturado do passivo geoespacial reduza erros sistêmicos na base, melhore a consistência entre localização e unidade federativa/município, aumente a precisão das análises territoriais e reduza a reincidência de retrabalho corretivo decorrente de migrações e evoluções do sistema.
121.	E1) Para reduzir a reincidência de inconsistências geoespaciais no CAF, aumentar a confiabilidade territorial dos registros e preservar ganhos de qualidade e novas versões do sistema, a Unidade Técnica propõe recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução - TCU 315/2020, que:
121.1.	reavalie e aprimore o processo de gestão de mudanças e garantia da qualidade das evoluções do CAF, com foco no ciclo de desenvolvimento, homologação e implementação de novas versões, de forma a prevenir regressões funcionais e de dados, em alinhamento com as boas práticas do Cobit 2019 (BAI10);
121.2.	aperfeiçoe as regras de negócio e implemente controles automatizados de validação cartográfica do CAF para validação espacial e consistência dos dados (ex.: município/UF, unicidade espacial e plausibilidade), incluindo verificações cruzadas com bases oficiais pertinentes (ex.: as malhas do IBGE, o acervo fundiário do Incra e o CAR, entre outras), para detectar anomalias e reduzir a entrada de novos erros;
121.3.	avalie e implemente medidas de orientação e padronização de práticas de captura de coordenadas pela rede cadastradora, de forma a reduzir usos de referências indevidas e padrões anômalos de cadastramento em massa, priorizando localidades com evidências de concentração crítica.
122.	Espera-se que a combinação dessas medidas reduza regressões e erros de origem, aumente a consistência entre localização e território administrativo, melhore a qualidade da base para análises e decisões de política pública e diminua o retrabalho de saneamento geoespacial ao longo do tempo.
3.3.	Achado III: Fragilidades de governança, cadastramento e curadoria dos dados comprometem a qualidade cadastral do CAF, dificultando comunicação com os cadastrados e elevando riscos de focalização das políticas públicas de agricultura familiar
Síntese: A auditoria encontrou falhas sistêmicas de plausibilidade e consistência no CAF: 12.820 CPFs com indicação de óbito na base da RFB, dos quais 3.097 confirmados na base do Sisobi, e 138 menores/adolescentes não aptos como responsáveis por Unidade Familiar de Produção Agrária (UFPA). Os dados de contato são praticamente inutilizáveis: 90,62% de e-mails fictícios e 93,7% de CEPs genéricos, dificultando comunicação com cerca de 2,6 milhões de famílias. Também foram identificadas anomalias de renda (até R$ 167 milhões) e empresas urbanas cadastradas como agricultura familiar. As falhas decorrem de processos de coleta permissivos, ausência de curadoria cadastral e integração insuficiente com bases oficiais.
123.	A qualidade dos dados cadastrais no CAF é determinante para a efetividade das políticas públicas que utilizam essa base como critério de elegibilidade e habilitação. Dados cadastrais de baixa qualidade, como CPFs de pessoas falecidas, menores de idade sem capacidade civil, e-mails fictícios, CEPs genéricos, rendas manifestamente implausíveis ou pessoas jurídicas com atividades incompatíveis comprometem a capacidade do Estado em direcionar recursos públicos exclusivamente a beneficiários legítimos, geram insegurança jurídica para agricultores familiares que podem ter benefícios negados ou questionados posteriormente por erros cadastrais, e criam vulnerabilidade a fraudes mediante uso de cadastros indevidos. Adicionalmente, e-mails e CEPs inválidos dificultam a comunicação efetiva com os beneficiários, e comprometem a transparência e a capacidade de notificação sobre mudanças regulatórias, atualizações obrigatórias e oportunidades de programas, gerando risco de exclusão involuntária de agricultores legítimos por falta de conhecimento.
124.	Diferentemente do Achado II, que investigou a qualidade geoespacial dos imóveis do CAF, o presente achado concentra-se na qualidade dos dados cadastrais de pessoas físicas e jurídicas, abrangendo: capacidade civil dos responsáveis (óbitos, menoridade, emancipação), validade de dados de contato (e-mail, telefone, CEP), consistência de dados de renda e compatibilidade de natureza jurídica e Classificação Nacional de Atividades Econômicas (CNAE) das entidades cadastradas. Essas dimensões de qualidade são complementares e interdependentes: enquanto o Achado II focou no "onde" (localização geográfica dos imóveis rurais), o presente achado foca no "quem" (identidade e qualificação legal dos beneficiários) e no "como contatar" (canais de comunicação institucional). Juntas, essas análises determinam o grau de qualidade total do cadastro e sua capacidade de cumprir a finalidade institucional de identificação e qualificação estabelecida pelo Decreto 9.064/2017 (peça 81).
125.	Diante dos riscos à focalização das políticas públicas identificados no planejamento da auditoria, a presente análise buscou responder às seguintes subquestões sobre a qualidade dos dados cadastrais do CAF: 
(i) Quantas Unidades Familiares de Produção Agrária (UFPA) ativas possuem responsáveis com óbito registrado, menores de 16 anos ou com CPFs não localizados na base da Receita Federal?
(ii)    Qual a taxa de e-mails inválidos e CEPs genéricos cadastrados, e como essa característica se distribui entre pessoas físicas e jurídicas?
(iii)   Quantos registros de renda apresentam valores extremos manifestamente implausíveis, e qual o impacto nas estatísticas agregadas?
(iv)    Quantas pessoas jurídicas cadastradas possuem CNAEs incompatíveis com as atividades permitidas para agricultura familiar, e quantos agricultores estão vinculados a essas entidades?
Situação Encontrada
126.	A análise censitária das 2.905.101 UFPAs revelou comprometimento da qualidade em todas as quatro dimensões investigadas. Tais falhas configuram violação sistemática à finalidade institucional do CAF de identificar e qualificar as UFPAs, estabelecida no art. 4º do Decreto 9.064/2017, manifestando-se desde inconsistências jurídicas críticas, como a presença de responsáveis falecidos ou menores de idade, até a dificuldade operacional da comunicação estatal por meio de dados de e-mail massivamente fictícios.
127.	A Tabela 9 consolida os principais achados quantitativos por dimensão, evidenciando a heterogeneidade dos problemas. A análise revela um padrão de “vazio semântico”: o sistema valida a sintaxe (formato do dado), garantindo que os campos obrigatórios estejam preenchidos, mas ignora o conteúdo (se o dado é verdadeiro ou funcional). Assim, enquanto as falhas nos dados relativos à capacidade civil e à natureza jurídica apresentam baixa incidência absoluta, sua gravidade jurídica é alta por gerarem atos potencialmente nulos ou anuláveis; em contraste, a imprecisão dos dados de contato é um problema sistêmico que afeta quase a totalidade da base. Além disso, a presença de outliers de renda superiores a R$ 1 milhão viola os critérios normativos de elegibilidade (Lei 11.326/2006, Regra de Negócio RN1.32 do CAF 3.0 e Planos Safra), evidenciando ausência de validação de plausibilidade. Por fim, a análise de natureza jurídica identificou que 10.377 agricultores estão vinculados a entidades com atividades incompatíveis (ex: hipermercados), colocando-os em risco potencial de bloqueio de acesso a políticas públicas por irregularidade cadastral da pessoa jurídica (PJ).
Tabela 9. Síntese Quantitativa dos Achados por Dimensão de Qualidade
Sub-achado	Dimensão	Registros Afetados	% da Base	Gravidade	Fonte
III.1	Capacidade Civil	15.811	0,544%	Crítica (nulidade jurídica)	peça 124, p.8
III.2	Dados de contato (e-mail de PF)	5.913.659	90,62%	Alta (dificulta a comunicação)	peça 125, p. 6
III.2	Dados de Contato (CEP genérico)	3.318.270	93,70%	Média (imprecisão geográfica)	peça 125, p. 8
III.3	Consistência de Renda	907	0,027%	Média (falha de validação)	peça 126, p. 7
III.4	Natureza Jurídica de PJ (CNAE)	39	0,40%	Alta (10.377 agricultores em risco)	peça 127, p. 5
Fonte: Elaboração própria com base nos cruzamentos CAF × RFB × SISOBI (PT-01 a PT-04). População base: 2.905.101 responsáveis ativos para identidade civil; 3.340.741 UFPAs ativas para análise de renda.
128.	Essa dicotomia explica por que campos obrigatórios apresentam 100% de preenchimento formal (completude), mas taxas superiores a 90% de invalidade real no CAF (peça 125, p. 6). O sistema viola as dimensões de qualidade de dados da norma ISO/IEC 25012:2008 (Data Quality Model), especialmente quanto à acurácia, atualidade e validade: valida-se a sintaxe (formato de CPF, presença de "@"), mas não se verifica o conteúdo semântico (se o CPF pertence a pessoa viva, se o e-mail é funcional ou se o CEP corresponde ao endereço). O contraste é ainda mais evidente na comparação entre pessoas físicas (PF) e jurídicas (PJ): enquanto 90,62% dos e-mails de PF são fictícios (peça 125, p. 6), 99,70% dos e-mails de PJ são válidos (peça 125, p. 7), uma diferença de 90,32 pontos percentuais (peça 125, p. 8) que demonstra que o problema não é técnico, mas processual.
129.	A metodologia empregada baseou-se em análise censitária (peças 124-127) mediante cruzamento do cadastro CAF com bases oficiais externas disponíveis no banco de dados do ambiente LabContas do TCU: Secretaria Especial da Receita Federal do Brasil (RFB) para validação de CPFs, datas de nascimento, situação cadastral, óbitos e CNAEs de pessoas jurídicas; e Sistema de Óbitos (Sisobi) para confirmação de falecimentos.  
130.	A população-base de 2.905.101 responsáveis atuais por UFPAs ativas (peça 124, p.8) foi obtida mediante consulta estruturada detalhada na Seção 6 do Apêndice V (Metodologia de Extração de Dados), cujos scripts SQL estão documentados no arquivo `scripts_PT01_LABCONTAS_SQLServer.pdf` (peça 129).
Figura 6. Comprometimento da qualidade cadastral do CAF por dimensão de análise
 
Percentual da base de 2.905.101 responsáveis ativos (peça 124, p. 8) afetado por cada tipo de inconsistência. As cores indicam a gravidade potencial: vermelho escuro (crítica – nulidade jurídica), vermelho (alta – impacto operacional ou fiscal relevante) e laranja (média – imprecisão tolerável). Os dados de contato (e-mails e CEPs) apresentam as maiores taxas de comprometimento (>90%) (peça 125, p. 6), enquanto as inconsistências de capacidade civil afetam 0,544% da base (peça 124, p. 8), porém, com consequência jurídica alta.
Fonte: Elaboração própria com base nos cruzamentos CAF × RFB × SISOBI documentados nos PT-01 a PT-04 (peças 124-127).
Subachado III.1 – Capacidade Civil e Legitimidade dos Responsáveis
131.	A primeira dimensão de análise investigou a capacidade civil dos responsáveis cadastrados no CAF, requisito fundamental para a validade jurídica dos atos praticados em nome das UFPAs. Conforme o Código Civil Brasileiro (Lei 10.406/2002), são absolutamente incapazes de exercer pessoalmente os atos da vida civil os menores de 16 anos (art. 3º), e relativamente incapazes os maiores de 16 e menores de 18 anos não emancipados (art. 4º, I). 
 
Tabela 10. Síntese das Inconsistências de Capacidade Civil (Sub-achado III.1)
Categoria	Quantidade	% da Base	Gravidade	Fonte
Óbitos confirmados (SISOBI)	3.097	0,107%	Nulidade absoluta	Peça 124, p. 8
Menores de 16 anos	89	0,003%	Nulidade absoluta	
Adolescentes 16-17 não emancipados	49	0,002%	Nulidade relativa	
Idades negativas (datas futuras)	57	0,002%	Invalidade de dados	
Divergências de nascimento	11.999	0,413%	Comprometimento de cruzamentos	
CPFs não localizados na RFB	520	0,018%	Risco de fraude	
Total	15.811	0,544%		
Nota: Percentuais calculados sobre população de 2.905.101 responsáveis (peça 124, p. 8). Fonte: PT-01 (peça 124).
132.	Adicionalmente, a morte extingue a personalidade jurídica e, consequentemente, a capacidade para qualquer ato civil (art. 6º). A presença de responsáveis falecidos e menores incapazes viola o pressuposto fundamental de gestão familiar estabelecido no art. 3º da Lei 11.326/2006 (Lei da Agricultura Familiar), no art. 2º, II, da Portaria – MDA 19/2025 e na Regra de Negócio RN1.8 do CAF 3.0, uma vez que incapazes não podem gerir o estabelecimento e falecidos não possuem personalidade jurídica, comprometendo a razão de ser do cadastro. Este sub-achado consolidou 15.811 inconsistências críticas (0,544% da população base) (peça 124, p. 8), distribuídas em seis categorias de comprometimento (peça 124, p. 8).
Responsáveis Falecidos
133.	A análise mais grave identificou 3.097 responsáveis com óbito confirmado (peça 124, p. 9) que permanecem como titulares ativos de UFPA no CAF. A verificação foi realizada pela própria equipe de auditoria mediante validação cruzada simultânea do cadastro CAF com duas fontes oficiais disponíveis no ambiente LabContas: a base de CPFs da Receita Federal (RFB) e o Sistema de Óbitos (Sisobi). A Figura 9 compara os resultados, evidenciando que, embora o cruzamento com a RFB tenha indicado 12.820 CPFs com situação "Titular Falecido" (peça 124, p. 15), adotou-se nesta auditoria o critério conservador de contabilizar apenas os registros também confirmados no Sisobi (3.097). Essa opção metodológica visa mitigar falsos positivos, pois apenas o Sisobi fornece a data exata do falecimento necessária para comprovar a inelegibilidade temporal.
134.	A distribuição temporal dos 3.097 óbitos confirmados revela acúmulo histórico de registros não saneados (peça 124, p. 9): 20,8% dos falecimentos ocorreram entre 2010 e 2015, 39,5% entre 2016 e 2020, e 39,7% entre 2021 e 2025. O caso mais antigo identificado refere-se a um responsável falecido em 2011, há mais de quatorze anos, cuja UFPA permanece ativa no sistema. Esse achado evidencia que o sistema falhou em detectar o óbito no momento da ocorrência e não possui mecanismo de verificação periódica que identifique e bloqueie automaticamente cadastros de pessoas falecidas. A estimativa preliminar fornecida pelo MDA no início da auditoria indicava aproximadamente 315 casos de óbitos (peça 124, p. 9), mas a realidade encontrada foi dez vezes maior (peça 124, p. 9).
Menores Absolutamente Incapazes e Adolescentes Não Emancipados
135.	Foram identificados 89 responsáveis menores de 16 anos (peça 124, p. 8) na data de ativação da UFPA, configurando incapacidade civil absoluta nos termos do art. 3º do Código Civil. O caso mais extremo é de um responsável por UFPA com apenas 11 anos de idade (peça 124, p. 26). A existência desses registros ativos evidencia falha nos controles de validação de idade mínima na entrada de dados ou, alternativamente, a ausência de saneamento durante a migração de registros legados, permitindo que inconsistências jurídicas persistam na base produtiva. Esses registros representam nulidade absoluta dos atos eventualmente praticados, uma vez que menores de 16 anos não podem representar legalmente uma unidade produtiva.
136.	Adicionalmente, foram identificados 49 responsáveis com idade entre 16 e 17 anos (peça 124, p. 8), não declarados como emancipados, configurando incapacidade relativa nos termos do art. 4º, I, do Código Civil. Embora a legislação admita a emancipação a partir dos 16 anos mediante escritura pública (art. 5º, parágrafo único, I), o CAF possibilita apenas o registro de uma informação declarativa sem exigir documento comprobatório.
Idades Negativas – Datas de Nascimento Futuras
137.	O achado mais inequívoco de ausência de validação refere-se aos 48 responsáveis com data de nascimento cadastrada no futuro (peça 131, p. 4), resultando em idades calculadas negativas na data de ativação da UFPA. Os casos mais extremos incluem datas de nascimento nos anos 2084, 2083 e 2082 (peça 131, p. 4, Tabela 6), evidenciando erro de digitação do século (ex: 2082 ao invés de 1982). Esses valores são impossíveis e demonstram que o banco de dados contém registros com datas inválidas. A persistência desses registros ativos constitui contundente evidência de falha nos controles de entrada (ausência de bloqueio para datas futuras) ou de integridade (ausência de saneamento/validação periódica), permitindo a permanência de dados incorretos na base produtiva.
Divergências de Data de Nascimento
138.	O cruzamento entre as datas de nascimento cadastradas no CAF e na RFB revelou 11.999 divergências (peça 124, p. 10), classificadas em quatro categorias conforme a magnitude da diferença. A Figura 7 apresenta essa distribuição.
Figura 7. Classificação das divergências de data de nascimento entre CAF e RFB
 
As 11.999 divergências foram classificadas pela magnitude da diferença em dias: divergências estruturais (> 365 dias) representam 41,74% dos casos e sugerem cadastros completamente distintos ou erros grosseiros; o padrão de inversão dia/mês (8-31 dias) responde por 23,78% e indica provável troca de campos durante a digitação (ex: 15/03 cadastrado como 03/15); erros de ano/mês (32-365 dias) somam 22,79%; e pequenas diferenças de até 7 dias (11,69%) são compatíveis com erros de digitação simples.
Fonte: PT-01 – Memória de Cálculo MC-007 (peça 124).
139.	Assim, a tabela abaixo evidencia que as maiores divergências decorrem de erros de digitação de século: o usuário digita "19" como "18" ou "20", resultando em datas de nascimento em 1879 (antes da abolição da escravatura) ou em 2049 (no futuro). Foram identificados 58 registros com divergência igual ou superior a 100 anos e 920 registros com divergência igual ou superior a 50 anos (peça 124, p. 19).
Tabela 11. TOP 10 divergências de data de nascimento
#	CPF	Divergência	Data CAF	Data RFB	Provável Causa
1	075.XXX.XXX-70	110 anos	1879-11-10	1989-11-10	Erro de século (1979→1879)
2	471.XXX.XXX-68	107 anos	2028-12-10	1921-11-20	Erro de século (1928→2028)
3	138.XXX.XXX-04	100 anos	2049-03-12	1949-03-12	Erro de século (1949→2049)
4	465.XXX.XXX-87	100 anos	2041-12-14	1941-12-14	Erro de século (1941→2041)
5	339.XXX.XXX-72	100 anos	2045-05-05	1945-05-05	Erro de século (1945→2045)
6	151.XXX.XXX-91	100 anos	2039-10-24	1939-10-24	Erro de século (1939→2039)
7	290.XXX.XXX-72	100 anos	2048-11-19	1948-11-19	Erro de século (1948→2048)
8	071.XXX.XXX-72	100 anos	2048-09-19	1948-09-19	Erro de século (1948→2048)
9	507.XXX.XXX-91	100 anos	2043-12-13	1943-12-13	Erro de século (1943→2043)
10	293.XXX.XXX-15	100 anos	2042-06-23	1942-06-23	Erro de século (1942→2042)
140.	Essas divergências têm impacto direto na elegibilidade para programas específicos. O Pronaf Jovem, por exemplo, destina-se a agricultores entre 16 e 29 anos. Portanto, uma divergência de data de nascimento pode indevidamente incluir ou excluir beneficiários dessa faixa etária.
CPFs Não Localizados
141.	Por fim, foram identificados 520 CPFs de responsáveis ativos que não constam na base da Receita Federal do Brasil (peça 124, p. 10). Ainda que esses documentos estivessem eventualmente regulares no momento do cadastramento inicial, sua ausência atual na base oficial compromete a verificação da elegibilidade contínua dos beneficiários e a realização de cruzamentos de fiscalização. A persistência dessa inconsistência evidencia a ausência de mecanismos de monitoramento periódico (saneamento contínuo via interoperabilidade) para garantir que alterações na situação cadastral do CPF na Receita Federal reflitam-se tempestivamente na situação da Unidade Familiar no CAF.
142.	A permanência de 15.811 registros com inconsistências de capacidade civil (peça 124, p. 8) — incluindo 3.243 casos de gravidade potencialmente alta (óbitos, menores e idades impossíveis) — indica ausência/falha sistêmica de três controles fundamentais: (i) integração com base de óbitos para detecção automática de falecimentos; (ii) regras de negócio para validação de idade mínima e plausibilidade de datas; e (iii) rotinas periódicas de saneamento cadastral (curadoria). A inexistência de tais mecanismos foi confirmada pela avaliação de conformidade realizada no Papel de Trabalho PT-05 (Peça 128, p. 5), que identificou a ausência de processos estruturados de curadoria no âmbito do MDA, fato materializado pela manutenção de registros de responsáveis falecidos há mais de uma década na base ativa do CAF (Peça 124, p. 9).
Subachado III.2 – Dados de Contato Massivamente Fictícios
143.	A segunda dimensão de análise investigou a qualidade de dados de contato (e-mail e CEP). Os problemas afetam mais de 90% dos registros (peça 125, p. 1 e 6). Essa deficiência não é apenas formal; ela compromete a eficiência operacional e a legalidade dos processos administrativos, pois inviabiliza a notificação eletrônica em massa de baixo custo, forçando a Administração a recorrer a meios onerosos (correspondência física) ou de baixa efetividade real (notificação por edital ou telefone) para contatar beneficiários em caso de irregularidades. 
E-mails de Pessoa Física e Contraste com Pessoa Jurídica
144.	A análise dos 6.525.658 registros de e-mail de pessoas físicas revelou que 90,62% são fictícios ou inválidos (peça 125, p. 6). O padrão mais frequente é "naopossui@mail.com" (75,16% da base).
145.	Em contraste, 99,70% dos e-mails de PJ são válidos (peça 125, p. 7). A disparidade de mais de 90 pontos percentuais demonstra que a causa raiz é processual e não técnica. Para Pessoas Jurídicas, o e-mail é uma ferramenta operacional indispensável para o recebimento de notas fiscais, notificações tributárias e relacionamento bancário, o que cria um incentivo natural para a correção do dado. Já para Pessoas Físicas no contexto do CAF, o e-mail é frequentemente percebido como mera formalidade burocrática sem utilidade prática imediata, favorecendo o preenchimento com valores fictícios apenas para superar a validação sintática do sistema.
Figura 8. Dicotomia na qualidade de e-mails cadastrados no CAF por tipo de pessoa
 
Fonte: PT-02 – Memórias de Cálculo MC-018, MC-020, MC-022, MC-023 (peça 125).
CEPs Genéricos e Inconsistentes
146.	93,7% dos CEPs cadastrados são genéricos (terminam em "-000") (peça 125, p. 1). Mesmo entre os CEPs específicos, 18,9% divergem da UFPA declarada (peça 125, p. 8).
 
Tabela 12. Síntese da Qualidade dos Dados de Contato (Sub-achado III.2)
Dimensão	Total	Problema	% Afetado	Impacto	Fonte
E-mails PF	6.525.658	Fictícios/inválidos	90,62%	Comunicação inviável	peça 125, p. 6
 Padrão “nãopossui”	4.904.403	Declaração explítica	75,16%	---	peça 125, p. 6
E-mails PJ	9.621	Válidos	99,70%	Referência de qualidade	peça 125, p. 7
CEPs	3.540.310	Genéricos (-000)	93,70%	Localização imprecisa	peça 125, p. 1
CEPs específicos	222.040	Inconsistência UF	18,90%	Cruzamentos comprometidos	peça 125, p. 8
Fonte: PT-02 – Análise de dados de contato CAF (Nov/2025).
147.	A magnitude do problema de e-mails fictícios tem implicação direta na governança do programa: o MDA possui um cadastro de aproximadamente 3 milhões de famílias de agricultores familiares (peça 124, p. 1), mas não dispõe de canal eletrônico funcional para comunicar-se com mais de 90% delas (peça 125, p. 6).
148.	A ausência de canais de comunicação direta e eficaz gera três riscos: (i) exclusão involuntária de agricultores legítimos; (ii) dificuldade de notificação sobre irregularidades; e (iii) dependência de terceiros.  A via postal permanece comprometida pela qualidade dos dados atuais (93,7% de CEPs genéricos), cuja correção demandaria, além de validação semântica, a exigência de comprovantes de residência, o que elevaria o custo de conformidade do cadastro.
Subachado III.3 – Consistência de Dados de Renda
149.	A terceira dimensão de análise investigou a consistência estatística dos dados de renda anual declarados no CAF, aplicando o Método de Tukey (detalhamento técnico na Seção 7 do Apêndice V) como técnica exploratória para detecção de anomalias (outliers). A análise abrangeu 3.304.174 UFPAs ativas (peça 130, p. 1). A estatística descritiva revelou distribuição assimétrica típica: mediana de R$ 18.831 e intervalo interquartil (IQR) de R$ 39.435. O limiar estatístico de alerta (Tukey), calculado em R$ 108.027, serviu como ponto de corte inicial para investigar valores que extrapolam o limite para enquadramento na categoria de agricultor familiar no Pronaf (R$ 500 mil/ano, segundo a Regra de Negócio RN1.32 do CAF 3.0).
150.	Acima desse parâmetro, foram identificadas 494.299 UFPAs (14,96%), incluindo casos com renda superior a valores que violam qualquer limite histórico do Pronaf, tais como: 907 casos com renda de R$ 1 milhão (0,027%), 139 acima de R$ 10 milhões (0,0042%) e um extremo superior a R$ 167 milhões, valores incompatíveis com os tetos históricos do Pronaf (R$ 360 mil, R$ 415 mil e R$ 500 mil, conforme o período), o que indica fragilidades de validação e plausibilidade dos dados. Além disso, esses outliers elevam a média nacional de renda de R$ 57.129 para R$ 58.307 (+2,06%), com potencial de distorcer diagnósticos, planejamento orçamentário e dimensionamento de subsídios.
 
Tabela 13. Síntese da Análise de Outliers de Renda (Sub-achado III.3)
Categoria	Quantidade	% da Base	Observação
Total de UFs ativas analisadas	3.340.741	100%	Peça 130, p. 1
Mediana	R$ 18.831	-	Peça 130, p. 3
Limiar de Tukey (Q3 + 3XIQR)	R$ 108.027	-	Peça 130, p. 3
Outliers acima de Tukey	494.299	14,96%	Peça 130, p. 3
Outliers > R$ 1 milhão	907	0,027%	Peça 130, p. 3
Outliers > R$ 10 milhões	139	0,0042%	Peça 130, p. 3
Média com outliers	R$ 58.307	-	Peça 130, p. 4
Média sem outliers	R$ 57.129	-	Peça 130, p. 4
Distorção da média	+2,06%	-	Peça 130, p. 4
Fonte: Peça 130 – Análise de Outliers de Renda (Dez/2025). Método de Tukey aplicado à renda agregada por Unidade Familiar, excluindo autoconsumo.
Método de Tukey para detecção de outliers
O Método de Tukey  é técnica estatística para identificação de valores atípicos (outliers), alinhada às práticas de análise exploratória de dados adotadas pelo TCU (Roteiro de Análise de Dados, 2019, p. 14 ). O método utiliza o intervalo interquartil (IQR = Q3 − Q1), definindo como outliers valores que excedem Q3 + 1,5×IQR 
151.	A Lei 11.326/2006 estabelece que o Conselho Monetário Nacional (CMN) pode estabelecer critérios e condições adicionais de enquadramento para fins de acesso às linhas de crédito destinadas aos agricultores familiares, cujos valores monetários são atualizados periodicamente. Os valores de renda encontrados superiores a R$ 1 milhão violam qualquer limite histórico do Pronaf:
Tabela 14. Evolução do Limite de Renda Bruta Anual (Pronaf)
Período (Plano Safra)	Limite de Renda Bruta (R$)	Situação dos Outliers (>R$ 1mi)
2017/2018 a 2019/2020	360.000,00	Violam o teto em > 240%
2020/2021	415.000,00	Violam o teto em > 240%
2021/2022 a 2024/2025	500.000,00	Violam o teto em > 200%
Fonte: Manuais de Crédito Rural (MCR) e Planos Safra do período.
152.	A aplicação do método revelou 907 UFPAs com renda agregada superior a R$ 1 milhão (0,027%), das quais 139 ultrapassam R$ 10 milhões (peça 130, p. 3-4). O caso mais extremo refere-se a uma unidade familiar com renda anual superior a R$ 167 milhões (peça 130, p. 3). Embora o percentual de casos extremos seja baixo (0,027%), sua existência constitui evidência material de ausência de crítica de dados e compromete a credibilidade da governança do programa.
153.	O impacto estatístico evidencia falha de validação: a presença de valores implausíveis causa distorção de +2,06% na média nacional de renda (peça 130, p. 4). Essa distorção compromete a confiabilidade dos diagnósticos de renda utilizados para o planejamento orçamentário e para o dimensionamento de subsídios, podendo induzir a erro na alocação de recursos públicos e na formulação de metas para o setor.
154.	As hipóteses explicativas incluem: erro de unidade (centavos sem vírgula), renda acumulada de múltiplos anos, faturamento de cooperativa confundido com renda individual, ou erro de digitação.
155.	A consulta à "Especificação de Regras de Negócio – CAF 3.0" (peça 78) revelou que as regras existentes (RN1.22 a RN1.32) tratam apenas da classificação e categorização das UFPAs após a entrada do dado. Especificamente, a RN1.32 estabelece o teto de R$ 500.000,00 para fins de enquadramento, mas não atua como uma trava de entrada, permitindo que valores manifestamente incorretos sejam gravados na base. Portanto, há uma ausência de regras de plausibilidade na entrada e uma insuficiência das regras de integridade no processamento posterior.
156.	O teto de R$ 500.000,00 (Manual de Crédito Rural - MCR, 10-2-1; peça 137, p. 165) funciona como o “corte da categoria”: acima desse valor, o produtor deixa de ser agricultor familiar e passa a ser classificado como médio ou grande produtor. Como o CAF é o instrumento exclusivo de identificação da categoria, a aceitação de rendas milionárias (ex: R$ 167 milhões) constitui erro de enquadramento legal do cadastro inteiro. O efeito cascata é crítico: a manutenção de um CAF indevido por excesso de renda garante acesso irregular a todo o ecossistema de políticas públicas (ex.: PAA, Seguro Defeso, Aposentadoria Rural Especial), evidenciando que a falha de validação no sistema transcende o risco de crédito e pode atingir a integridade da política social como um todo.
Subachado III.4 – Natureza Jurídica e CNAE de Pessoas Jurídicas
157.	A quarta dimensão de análise investigou a compatibilidade entre a natureza jurídica das entidades cadastradas e as atividades econômicas exercidas, mediante cruzamento dos 9.687 CNPJs cadastrados (peça 127, p. 5) com a base da RFB para verificação das CNAEs, em conformidade com o art. 27, II, da Portaria - MDA 19/2025, que veda a inscrição de pessoa jurídica cuja atividade econômica seja incompatível com a agricultura familiar. 
158.	Foram identificadas 39 pessoas jurídicas com CNAE principal incompatível (0,40%) — 17 hipermercados, 8 atacadistas, 4 construtoras e 10 de outras atividades urbanas. Embora numericamente pequenas, essas entidades concentram 10.377 dos 774.405 agricultores vinculados a PJs (1,34%), incluindo caso extremo de um hipermercado com capital social de R$ 12,5 milhões e 1.847 agricultores vinculados. Há, portanto, risco de bloqueio de acesso a políticas públicas para os vinculados (art. 28 da Portaria - MDA 19/2025), além de potencial fragilidade de validação no ingresso cadastral.
159.	A Classificação Nacional de Atividades Econômicas (CNAE) organiza as atividades em seções, sendo a Seção A (Agricultura, Pecuária, Produção Florestal, Pesca e Aquicultura) a única plenamente compatível.
160.	A auditoria encontrou 39 PJs (0,40%) que possuem CNAEs principais incompatíveis: 17 hipermercados, 8 atacadistas, 4 construtoras e 10 outras atividades urbanas (peça 127, p. 5). O caso mais extremo é um hipermercado com capital social de R$ 12,5 milhões e 1.847 agricultores vinculados.
161.	Do total de 774.405 agricultores vinculados a PJs no CAF, 10.377 estão associados às 39 entidades com CNAEs incompatíveis, representando 1,34% dos vínculos (peça 127, p. 5). A média de agricultores por entidade irregular é de 266 — mais de três vezes superior à média geral de 80.
 
Tabela 15. Síntese das Entidades com CNAEs Incompatíveis (Sub-achado III.4)
Categoria	Quantidade	% do Total	Agricultores Vinculados
Total de PJs analisadas	9.687	100%	774.405
PJs com CNAEs compatíveis (Seção A)	9.648	99,60%	764.028
PJs com CNAEs incompatíveis	39	0,40%	10.377
	Hipermercados	17	0,18%	~6.200
	Atacadistas	8	0,08%	~2.100
	Construtoras	4	0,04%	~800
	Outras atividades	10	0,10%	~1.277
Média agricultores/PJ irregular	-	-	266
Caso extremo (hipermercado)	1	-	1.847
Fonte: PT-04 – Cruzamento CAF × RFB para CNAEs em Nov/2025 (peça 127, p. 5-6).
162.	Os 10.377 agricultores vinculados podem estar sujeitos a risco de bloqueio de acesso a políticas públicas, conforme art. 28 da Portaria - MDA 19/2025.
163.	A existência de hipermercados, atacadistas e construtoras cadastrados como "agricultura familiar" evidencia ausência de validação automatizada de CNAE no momento do cadastramento. A correção pode incluir medidas como: (i) validação no cadastramento com consulta à RFB; (ii) saneamento das 39 entidades identificadas; e (iii) monitoramento periódico.
Causas
164.	As inconsistências identificadas decorrem de quatro causas estruturantes interdependentes:
164.1.	Causa-Raíz 1: Desenho processual permissivo. O sistema do CAF aceita — ou não impede — dados inválidos porque prioriza o cadastramento e a fluidez operacional em detrimento da qualidade semântica. O sistema valida corretamente a sintaxe dos campos (formato de CPF, presença de "@" no e-mail), mas não verifica o conteúdo: aceita "naopossui@mail.com" como e-mail válido (peça 125, p. 6), datas de nascimento no futuro (peça 131, p. 4) e valores de renda implausíveis (peça 130, p. 3).
164.2.	Causa-Raíz 2: Ausência/Falhas de rotinas estruturadas de curadoria cadastral. O sistema do CAF não possui processos periódicos e sistematizados de saneamento de dados ou eles operam com falhas.
164.3.	Causa-Raíz 3: Ausência\Insuficiência de interoperabilidade de dados do sistema com bases oficiais. O sistema do CAF operava de forma isolada, sem conexão em tempo real com bases governamentais que permitiriam a validação cruzada automática de dados críticos. Cabe ressaltar, porém, que o CAF 3.0 possui integração com bases da RFB e com o CNIS (peças 71, 72 e 74).
164.4.	Causa-Raíz 4: Insuficiência de governança de dados do CAF. A causa raiz é a insuficiência de uma estrutura formal de governança que assegure a integridade dos ativos de informação do sistema ao longo do tempo. A falta de designação de proprietários e de curadores de dados (data owners e data stewards), de métricas de qualidade monitoradas e de processos de melhoria contínua baseados em detecção de anomalias permite que as falhas de desenho e os acúmulos de inconsistências persistam sem detecção proativa pela gestão.
164.5.	Essas causas estruturantes geram lacunas de controle que facilitam o acúmulo das inconsistências documentadas no Achado III e seus subachados.
Efeitos e Riscos
165.	Não foram mapeados pela equipe efeitos concretos decorrentes da situação encontrada.
166.	Já os efeitos potenciais (riscos) são:
166.1.	Impacto na focalização e elegibilidade de políticas públicas: A manutenção de 3.097 responsáveis falecidos como titulares ativos de UFPA viola o pressuposto legal de existência de personalidade jurídica para gestão do estabelecimento rural. Esses cadastros permanecendo ativos permitem que terceiros (herdeiros, parentes, intermediários desonestos) continuem acessando políticas como Pronaf, PAA e seguros agrícolas em nome de pessoas falecidas, desviando recursos públicos de seus destinatários legítimos. 
166.2.	Impacto na comunicação institucional e transparência: A impossibilidade de contato direto com 90,62% dos beneficiários (aproximadamente 2,6 milhões de famílias) através de e-mail válido compromete a eficiência operacional do Estado em: (i) notificar atualizações de requisitos de elegibilidade; (ii) comunicar mudanças regulatórias em programas que dependem da elegibilidade verificada no CAF; (iii) solicitar correção de dados quando inconsistências são detectadas; (iv) validar continuamente a elegibilidade mediante requerimento periódico de informações atualizadas. 
166.2.1.	A Consequência direta é que agricultores legítimos podem ter benefícios negados ou interrompidos por falta de notificação sobre atualizações obrigatórias, gerando insegurança jurídica e exclusão involuntária do acesso a direitos (Decreto 9.064/2017, art. 4º, § 2º; Peça 81): "O cadastro ativo no CAF será requisito para acesso às ações e às políticas públicas destinadas à UFPA."
A cadeia normativa completa está na Tabela 16 a seguir.
Tabela 16. Cadeia normativa completa
Norma	Artigo	O que estabelece	Peça
Decreto 9.064/2017	art. 4º, § 2º	Cadastro ativo no CAF é requisito obrigatório para acesso a políticas públicas	Peça 81
Lei 11.326/2006	art. 3º, I-IV	Define quem é elegível (≤ 4 módulos fiscais, mão de obra familiar, renda, gestão)	Peça 80, p. 1
Portaria - MDA 19/2025	art. 8º	Documentos obrigatórios para inscrição no CAF	Peça 108, p. 5
166.3.	Impacto na integridade regulatória e risco legal de beneficiários: Os 10.377 agricultores vinculados a 39 pessoas jurídicas com CNAEs incompatíveis (hipermercados, construtoras, atacadistas) podem estar em situação de risco de bloqueio de acesso a políticas públicas. Conforme art. 27 da Portaria - MDA 19/2025, pessoas jurídicas com atividades incompatíveis com agricultura familiar têm inscrição vedada no CAF. A manutenção desses vínculos ativos significa que esses 10.377 agricultores poderão ser considerados inelegíveis ou ter seus benefícios questionados retroativamente.
166.4.	Impacto na capacidade administrativa de remediar inconsistências: A acumulação histórica de 12.820 óbitos distribuídos ao longo dos anos sem detecção ou saneamento demonstra que o sistema operou continuamente sem rotina de limpeza. 
166.5.	Risco de desvio de recursos por fraude facilitada: As fragilidades de qualidade cadastral criam oportunidades para fraude mediante uso de cadastros indevidos. Especificamente, a presença de responsáveis falecidos cujos cadastros continuam ativos possibilita que terceiros utilizem o CPF para acessar políticas públicas. 
166.6.	Risco de questionamento legal de beneficiários legítimos: A manutenção de cadastros de menores de idade (89 registros com < 16 anos, 49 com 16-17 não emancipados) como responsáveis ativos de UFPAs cria nulidade absoluta de qualquer ato administrativo praticado em seu nome. O risco é que políticas públicas que dependem da higidez cadastral (PAA, Pronaf, Seguro Agrícola) venham a negar benefícios ou exigir devolução de recursos sob alegação de inconsistência cadastral do responsável.
166.7.	Risco de exclusão sistêmica de beneficiários por impossibilidade de comunicação: A manutenção de e-mails fictícios como canal de comunicação digital entre o Estado e 2,6 milhões de beneficiários cria risco de que, quando alterações regulatórias ocorrerem, beneficiários não sejam notificados e incorram em automaticamente descumprimento de requisitos atualizados. A impossibilidade de contato efetivo via e-mail forçaria recorrência a meios custosos (correspondência física com CEP genérico seria inefetivo) ou edital (baixa efetividade). Consequência potencial: exclusão involuntária de beneficiários legítimos por falta de conhecimento de atualizações, gerando reclamações administrativas, judiciais e desgaste institucional.
166.8.	Risco de erosão da credibilidade institucional do MDA: A aceitação de um hipermercado com 1.847 agricultores vinculados, construtoras, e atacadistas como parte de um cadastro de "agricultura familiar" pode comprometer a credibilidade do órgão gestor do CAF perante a sociedade civil. 
Benefícios Esperados
167.	Os benefícios esperados das ações corretivas são:
167.1.	Integridade cadastral restaurada (correção de óbitos, menores, etc.).
167.2.	Comunicação institucional facilitada (saneamento de e-mails).
167.3.	Validação de plausibilidade de renda implementada.
167.4.	Redução do risco de desconformidade regulatória (PJs, CNAEs).
167.5.	Detecção proativa de inconsistências.
167.6.	Melhoria na governança de dados do CAF.
Conclusão
168.	A análise censitária do CAF revelou comprometimento da qualidade cadastral em quatro dimensões: capacidade civil (3.097 óbitos confirmados no Sisobi e 138 menores/adolescentes incapazes), dados de contato (90,62% de e-mails fictícios e 93,7% de CEPs genéricos), consistência de renda (907 UFPAs com valores superiores a R$ 1 milhão) e natureza jurídica (39 PJs com CNAEs incompatíveis afetando 10.377 agricultores) (peças 124-127).
169.	As causas raízes identificadas foram: (i) desenho processual permissivo; (ii) ausência de curadoria cadastral; (iii) ausência de integração sistêmica; e (iv) insuficiência de governança de dados do CAF. A superação dessas fragilidades exige medidas de controle coordenadas em frentes tecnológicas, processuais e organizacionais.
170.	O CAF apresenta comprometimento da qualidade do dado que afeta a finalidade institucional de identificar e qualificar os beneficiários da agricultura familiar. Os problemas identificados exigem correção em três frentes: tecnológica (validações e integrações), processual (redesenho dos fluxos de coleta) e organizacional (instituição de curadoria cadastral).
Propostas de Encaminhamento
171.	D1) Para reduzir riscos de irregularidade cadastral, aumentar a confiabilidade do CAF e fortalecer a segurança jurídica e operacional das políticas públicas apoiadas no Cadastro, a Unidade Técnica propõe determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução - TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação, com responsáveis e prazos, para avaliar as falhas na qualidade de dados e de documentos do CAF apontadas no relatório de auditoria e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial:
171.1.	impropriedades de capacidade civil e legitimidade dos responsáveis;
171.2.	dados de contato fictícios;
171.3.	inconsistências de dados de renda; e
171.4.	inconsistências de natureza jurídica de pessoas jurídicas cadastradas.
172.	Espera-se que o saneamento dessas impropriedades aumente a integridade cadastral do CAF, reduza riscos de decisões baseadas em registros inválidos, amplie a efetividade da comunicação com beneficiários e melhore a qualidade das informações utilizadas para focalização, gestão e avaliação das políticas públicas da agricultura familiar.
173.	E1) Para prevenir a reincidência de inconsistências cadastrais no CAF, reduzir retrabalho de saneamento e aumentar a confiabilidade da base para gestão e focalização de políticas públicas, a Unidade Técnica propõe recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução - TCU 315/2020, que:
173.1.	revise e aperfeiçoe os processos de cadastramento e atualização dos dados do CAF e implemente medidas de prevenção à inserção/permanência de dados cadastrais inválidos, incluindo: impedimento de preenchimentos fictícios institucionalizados (ex.: e-mail padrão); validações semânticas e de plausibilidade em campos críticos (identidade civil, datas, renda e contato); e interoperabilidade/verificação automatizada com bases oficiais (ex.: CPF, CNAE, CEP e bases de óbitos), de modo a reduzir retrabalho de saneamento;
173.2.	desenvolva e implemente mecanismos de acompanhamento gerencial contínuo da qualidade cadastral, com métricas que permitam identificar e priorizar correções e avaliar a efetividade das medidas adotadas (ex.: percentuais de óbitos ativos, CPFs não localizados, divergências biográficas, e-mails inválidos, CEPs genéricos/inconsistentes, outliers de renda e CNAEs incompatíveis).
174.	Espera-se que a implementação dessas medidas reduza a entrada de novos erros e a permanência de inconsistências históricas, aumente a tempestividade das correções, fortaleça a integridade cadastral e melhore a qualidade da informação usada na tomada de decisão e no acompanhamento das políticas públicas da agricultura familiar.
3.4.	Achado IV: Falhas na gestão de metadados resultam em dicionário de dados inadequado, comprometendo rastreabilidade e auditabilidade do CAF
Síntese: O dicionário de dados do CAF, artefato que funciona como a "bula" do sistema, explicando o significado de cada campo e tabela, apresenta deficiências críticas em três das quatro dimensões avaliadas: 94,1% das descrições existentes são semanticamente inadequadas, limitando-se a repetir o nome técnico do campo (exemplo: "dt_criacao" descrito como "Data criação"); 84,0% dos campos numéricos não especificam unidade de medida (exemplo: o campo "nr_area" não informa se a área está em hectares, metros quadrados ou outra unidade); e 92,0% dos campos temporais são ambíguos (exemplo: não distingue se uma "data de criação" refere-se ao registro no sistema ou à inscrição do agricultor). Essas falhas tornam o uso dos dados dependente do conhecimento tácito de poucos desenvolvedores, conhecimento que pode se perder com a rotatividade de pessoal, e constituem uma causa estrutural que amplifica os problemas identificados nos Achados I, II e III.
175.	Para que um sistema dessa magnitude funcione de forma transparente e auditável, é indispensável que sua estrutura de dados esteja documentada de maneira clara e completa. Esse papel é cumprido em boa parte pelo dicionário de dados, um artefato de documentação que descreve o significado de cada tabela e campo do banco de dados, permitindo que desenvolvedores, analistas, auditores e gestores compreendam o que cada informação representa.
176.	Em termos simples, o dicionário de dados funciona como a “bula” de um sistema: assim como um medicamento precisa de instruções claras para ser utilizado corretamente, um banco de dados precisa de documentação que explique o que cada campo significa, como se relaciona com outros campos, qual faixa de valores é aceitável, e em que unidade de medida está expresso. Sem essa documentação, o uso dos dados depende de conhecimento tácito, informações que estão na mente dos desenvolvedores que construíram o sistema, mas que não foram formalizadas em lugar nenhum.
177.	Quando um novo interessado precisa elaborar um relatório, ou quando um auditor externo precisa verificar a consistência das informações, a ausência de um dicionário adequado transforma uma tarefa simples em uma investigação demorada, sujeita a erros de interpretação que podem comprometer decisões relevantes. É importante destacar que este achado se diferencia dos anteriores por uma característica fundamental: enquanto os Achados I, II e III analisaram a qualidade dos dados em si (conteúdo das informações, como e-mails fictícios, óbitos não refletidos ou divergências cadastrais), o Achado IV analisa a qualidade dos metadados, isto é, a documentação que explica o significado dos dados.
178.	Este achado identifica uma das raízes dos problemas de qualidade de dados do CAF: sem documentação adequada das regras de validação esperadas, desenvolvedores têm dificuldade em implementar controles que impeçam a entrada de e-mails fictícios ou CPFs inválidos; sem descrições claras que diferenciem campos temporais (datas e horas), a análise de consistência cronológica que revelou os óbitos não refletidos torna-se mais complexa e propensa a erros; sem indicação de qual sistema é a fonte autoritativa para cada informação, divergências cadastrais entre o CAF e as bases da Receita Federal persistem sem critério claro de resolução. Corrigir o dicionário de dados não é, portanto, apenas uma questão de boas práticas de TI, é um pré-requisito para que as correções nos dados sejam sustentáveis a longo prazo.
179.	Diante desse contexto, a presente auditoria buscou responder a quatro subquestões específicas (dimensões) sobre a qualidade do dicionário de dados do CAF:
(i): o dicionário possui cobertura completa de todas as tabelas existentes no banco de dados de produção?
(ii): as descrições dos campos fornecem significado de negócio compreensível, ou são meramente tautológicas e técnicas, limitando-se a repetir o nome do campo em outras palavras?
(iii): os campos numéricos possuem unidades de medida definidas, de modo que se saiba se uma área está expressa em hectares, metros quadrados ou outra unidade?
(iv): os campos temporais têm semântica clara, distinguindo, por exemplo, se uma "data de criação" refere-se ao momento em que o registro foi inserido no banco de dados ou à data em que o agricultor efetivamente se inscreveu no sistema?
180.	Para responder a essas questões, a equipe de auditoria realizou uma análise censitária, abrangendo 100% da população de tabelas e campos da base de dados do CAF, sem amostragem.
181.	A classificação da qualidade semântica das descrições baseou-se nos critérios estabelecidos pela norma ISO/IEC 11179:2015 (Registros de Metadados), que preconiza que descrições devem fornecer significado de negócio e não apenas traduzir nomenclaturas técnicas, e pela norma ISO/IEC 25012:2008 (Modelo de Qualidade de Dados), que estabelece requisitos de completude, compreensibilidade e rastreabilidade. Os resultados detalhados estão documentados em Papéis de Trabalho (PT-A04-01 a PT-A04-04, peças 133-136), nas seções Memórias de Cálculo (MC).
Situação Encontrada
182.	A análise censitária do dicionário de dados do CAF revelou deficiências em três das quatro dimensões avaliadas. Quanto à primeira dimensão, cobertura, a análise identificou que todas as 95 tabelas efetivamente em uso pelo sistema estavam documentadas (peça 70). As demais três dimensões, qualidade semântica, especificação de unidades de medida e clareza de campos temporais, apresentam deficiências significativas descritas a seguir.
183.	Em termos quantitativos, 94,1% das descrições de campos são semanticamente inadequadas, limitando-se a repetir o nome técnico, sem explicar o significado de negócio (496 de 527 campos) (peça 135, p. 4); 84,0% dos campos numéricos não especificam unidade de medida, deixando ambíguo se uma área está em hectares, metros quadrados ou outra unidade (105 de 125 campos) (peça 136, p. 4-5); e 92,0% dos campos temporais apresentam ambiguidade semântica, não distinguindo se uma "data de criação" refere-se ao registro no sistema ou à inscrição do agricultor no CAF (80 de 87 campos) (peça 133, p. 5).
184.	O quadro a seguir consolida os resultados das quatro dimensões analisadas:
Tabela 17. Análise das dimensões do Dicionário de Dados
Dimensão	Universo Analisado	Itens com Problema	Taxa de Deficiência
Cobertura do Dicionário	95 tabelas (peça 70)	-
	-
Qualidade Semântica	527 campos (peça 135, p. 4)	496 inadequados	94,1%
Especificação de Unidades de Medida	125 campos numéricos 
(peça 136, p. 4-5)	105 sem unidade	84,0%
Clareza de Campos Temporais	87 campos de data/hora (peça 133, p. 5)	80 ambíguos	92,0%
Fonte: Papéis de Trabalho PT-A04-01 a PT-A04-05 (peças 133-136) e Memórias de Cálculo.
185.	Em síntese, o dicionário de dados do CAF apresenta limitações significativas em sua capacidade de comunicar significado: ele cumpre um rito burocrático de documentação sem entregar a função essencial de explicar o que cada informação representa.
Subachado IV.1: Qualidade Semântica das Descrições
186.	Se a primeira pergunta sobre um dicionário de dados é "ele documenta tudo?", a segunda, e mais importante, é "o que ele documenta faz sentido?". Dos 527 campos documentados no dicionário oficial (peça 135, p. 4), 496 possuem descrições semanticamente inadequadas, representando uma taxa de inadequação de 94,1% (peça 135, p. 4, Tabela 3). Apenas 31 campos (5,9%) apresentam descrições que efetivamente explicam o significado de negócio da informação armazenada. Em termos práticos, isso significa que o dicionário de dados do CAF é um documento que existe formalmente, mas que não cumpre sua função essencial: quem o consulta encontra palavras, mas não encontra significado.
187.	Para avaliar a qualidade semântica das descrições, a equipe de auditoria desenvolveu uma taxonomia baseada nos critérios das normas ISO/IEC 11179:2015 (Registros de Metadados) e ISO/IEC 25012:2008 (Modelo de Qualidade de Dados), particularmente o requisito de Compreensibilidade (Understandability). Com base nesse princípio, cada descrição foi classificada em uma de quatro categorias:
187.1.	Tautológica: a descrição apenas traduz ou repete o nome do campo, sem agregar informação, por exemplo, o campo `dt_criacao` descrito simplesmente como "Data criação";
187.2.	Genérica: a descrição é vaga, incompleta ou carece de detalhes essenciais, por exemplo, "Tamanho da área imóvel" sem especificar a unidade de medida;
187.3.	Técnica: a descrição informa a função técnica do campo (ex.: é um identificador, é um status) sem explicar o que isso significa no contexto de negócio; e
187.4.	Funcional: a descrição é adequada, explicando o propósito e o contexto de uso do campo; esta é a única categoria considerada conforme aos padrões de qualidade.
188.	A análise censitária dos 527 campos revelou a seguinte distribuição:
Tabela 18. Análise censitária dos campos do dicionário de dados
Categoria	Quantidade	Percentual	Exemplo Real do Dicionário
Tautológica	296	56,2%	`dt_criacao` → "Data criação"
Genérica	181	34,3%	`nr_area` → "Tamanho da área imóvel"
Técnica	19	3,6%	`st_ativo` → "Situação ativo ou inativo"
Funcional	31	5,9%	`st_imovel_principal` → "Se é o imóvel principal da unidade familiar"
Fonte: peça 135, p. 4, Tabelas 2 e 3 – Memórias de Cálculo MC-A04-10 a MC-A04-16.
189.	Como se observa, mais da metade das descrições (56,2%) são meramente tautológicas, repetem o nome do campo em português corrido sem qualquer valor informacional adicional. Um terço (34,3%) são genéricas, fornecem alguma informação, mas insuficiente para uso prático. Somadas às descrições técnicas (3,6%), o total de inadequações alcança 94,1% do universo documentado.
190.	Um padrão de inadequação frequente é o pleonasmo "ID de identificação", que aparece em dezenas de campos do dicionário. Campos como `id_caf`, `id_municipio`, `id_area_imovel` e `id_unidade_familiar` são todos descritos com variações de "ID de identificação de [nome da entidade]", uma redundância, já que "ID" já significa identificador. Esse padrão evidencia que a inadequação não é pontual ou acidental, mas sistêmica.
191.	Como possível consequência, um analista de políticas públicas que precisa elaborar um relatório sobre a distribuição de renda entre agricultores familiares pode ter dificuldades de compreensão de um campo com a descrição "Valor renda auferida", pois ela não esclarece o significado exato do campo, conceito que, por sua vez, está definido na Portaria - MDA 19/2025, art. 2º, inciso XII, e que poderia ter sido utilizado no dicionário de dados.
192.	Em síntese, o Sub-achado IV.1 demonstra que o dicionário de dados do CAF falha em cumprir sua função semântica para os campos que documenta. A taxa de 94,1% de descrições inadequadas, com predomínio de tautologias e descrições genéricas, revela um artefato de documentação que existe para "cumprir tabela" sem entregar valor informacional.
Sub-achado IV.2: Ausência de Unidades de Medida nos Campos Numéricos
193.	Um dicionário de dados completo especifica não apenas o tipo e a descrição de cada campo, mas também a unidade de medida em que seus valores estão expressos, especialmente para campos numéricos. A análise do dicionário do CAF identificou 125 campos numéricos no esquema do banco de dados (peça 136, p. 4). Desses, 105 (84,0%) não possuem unidade de medida definida em suas descrições (peça 136, p. 4-5, Tabela 1). Essa lacuna gera ambiguidade significativa: um campo denominado `nr_area` contém valores em hectares, metros quadrados ou alqueires? Um campo `vl_renda_estimada` expressa valores em reais, salários-mínimos ou outra unidade? Sem essa informação, qualquer interpretação dos dados numéricos torna-se especulativa.
194.	A tabela abaixo apresenta exemplos críticos de campos numéricos cujas descrições no dicionário não especificam a unidade de medida:
Tabela 19. Exemplos Críticos de Campos Numéricos sem Unidade de Medida Definida
Tabela Campo	Descrição	Ambiguidade
`S_RENDA.vl_renda_estimada`	“Valor renda estimada”	R$? Salários-mínimos? (peça 136, p. 6, Tabela 4) 
`S_RENDA.vl_renda_auferida`	“Valor renda auferida”	R$? Mensal? Anual? (peça 136, p. 6, Tabela 4)
`S_MODULO_FISCAL.nr_modulo_fiscal`	"Número módulo fiscal"	Hectares? Quantidade de módulos? (peça 136, p. 6, Tabela 5)
`S_AREA_IMOVEL.nr_area`	“Tamanho da área imóvel”	Hectares? m²? Alqueires? (peça 136, p. 5, Tabela 3)
Fonte: peça 136, p. 5-6, Tabelas 3-5 — Casos críticos identificados.
195.	A ausência de unidades de medida nos campos numéricos acarreta riscos operacionais concretos: (i) soma de valores em unidades incompatíveis, produzindo totais sem significado; (ii) conversões incorretas em relatórios gerenciais, quando o desenvolvedor assume uma unidade diferente da real; e (iii) integração com sistemas externos que utilizam unidades distintas, resultando em dados inconsistentes. Um exemplo ilustra a magnitude do problema: interpretar erroneamente um campo em hectares como se estivesse em metros quadrados resulta em erro de fator 10.000, suficiente para classificar incorretamente um agricultor quanto ao enquadramento na política de agricultura familiar.
196.	A gravidade dessa lacuna acentua-se quando se verifica que as normas legais que regem a agricultura familiar definem explicitamente as unidades de medida aplicáveis, informações que deveriam constar no dicionário de dados:
 
Tabela 20. Unidades de Medida com Definição Legal Omitidas no Dicionário de Dados
Norma	Dispositivo	Unidade Definida	Campo no BD
Portaria - MDA 19/2025	art. 5º, §1º	Área expressa em hectares	`nr_area`
Lei 11.326/2006	art. 3º, §2º, II	Aquicultura: até 2ha ou 500m³	`nr_area`
Portaria - MDA 19/2025	art. 3º, IV	Aquicultura: até 2ha ou 500m³	`nr_area`
Portaria - MDA 19/2025	art. 2º, XI e XII	Valor Monetário em R$ acumulado em doze meses anteriores à emissão do CAF	vl_renda_*
197.	Em síntese, 84% dos campos numéricos do CAF não possuem unidade de medida documentada (peça 136, p. 4), incluindo campos críticos como área do imóvel e renda familiar, cujos valores determinam o enquadramento do agricultor na política.
198.	Observa-se que o dicionário de dados do CAF omite unidades de medida que possuem definição legal expressa. Não se trata apenas de questão de boas práticas de TI — é omissão de informação juridicamente estabelecida, comprometendo a rastreabilidade entre o sistema informatizado e seu marco regulatório.
Sub-achado IV.3: Ambiguidade Semântica em Campos Temporais
199.	A última dimensão de qualidade analisada refere-se à clareza semântica dos campos temporais, datas e timestamps que registram quando eventos ocorreram no sistema. A análise censitária identificou 87 campos temporais no esquema do banco de dados do CAF (tipos: `timestamp`, `date`, `time`) (peça 133, p. 5). Desses, 80 (92,0%) apresentam ambiguidade semântica que impede interpretação inequívoca sem conhecimento tácito da base de dados (peça 133, p. 5, Tabela 2). Apenas 7 campos (8,0%) possuem descrições que permitem compreender claramente qual evento temporal está sendo registrado.
200.	A ambiguidade mais prevalente nos campos temporais decorre da não distinção entre evento de sistema e evento de negócio. Para ilustrar: quando um agricultor familiar se inscreve no CAF em uma Unidade Local de Atendimento (ULA), dois eventos temporais distintos ocorrem, (i) o momento em que o agricultor assinou o formulário de inscrição (evento de negócio, com significado legal) e (ii) o momento em que o atendente digitou os dados no sistema (evento técnico, momento da inserção do registro no banco de dados). Um campo denominado `dt_criacao` descrito simplesmente como "Data criação" não permite saber qual desses dois eventos está sendo registrado, e a diferença pode ser de dias ou semanas, dependendo do fluxo de atendimento.
201.	O caso da tabela `S_UNIDADE_FAMILIAR`, entidade central da base de dados que representa o núcleo familiar de produção agrária, exemplifica de forma emblemática a natureza estrutural do problema. Esta tabela possui 8 campos de data, e nenhum deles tem descrição que permita interpretação inequívoca:
 
Tabela 21. Ambiguidades detectadas no Dicionário de Dados
Campo	Descrição no Dicionário	Ambiguidade Identificada
`dt_criacao`
	“Data criação”
	Criação do registro no Banco de Dados ou inscrição do agricultor?
`dt_atualizacao`	“Data atualização”
	Última alteração de qual campo? Qualquer um ou específico?
`dt_ativacao`	“Data ativação”	Primeira ativação ou mais recente? 
`dt_primeira_ativacao`
	“Data primeira ativação”	Qual a diferença operacional para `dt_ativacao`?
`dt_exclusao`
	“Data exclusão”	Exclusão lógica (soft delete) ou física?
`dt_inativacao`
	“Data inativação”	Diferença para `dt_exclusao`? Inativo ≠ Excluído?
`dt_fim_vigencia`
	“Data fim vigência”	Vigência do quê? Do cadastro? Da inscrição?
Fonte: peça 133, p. 6-8, Tabelas 5-8 — Casos críticos da tabela S_UNIDADE_FAMILIAR.
202.	Em síntese, 92% dos campos temporais do CAF apresentam ambiguidade semântica que impede interpretação inequívoca (peça 133, p. 5, Tabela 2). A tabela central da base de dados (`S_UNIDADE_FAMILIAR`) exemplifica o padrão: possui 8 campos de data sem que o dicionário explique a diferença funcional entre eles (peça 133, p. 6-8). Parâmetros temporais definidos em lei, como a validade de 3 anos da inscrição, não estão documentados. 
Causas
203.	As deficiências identificadas em três das quatro dimensões do dicionário de dados, descrições inadequadas (94,1%), ausência de unidades de medida (84,0%) e ambiguidade temporal (92,0%), não são falhas pontuais ou aleatórias. A magnitude e a uniformidade dos problemas revelam um padrão sistêmico que indica possíveis causas estruturais.
Causas raiz
204.	Causa 1, Ausência de processo de gestão de metadados. O CAF não possui um documento formal que estabeleça padrões de documentação, responsabilidades e processos de controle de qualidade para metadados. Não há definição explícita de quem é responsável pela manutenção do dicionário de dados, quais critérios uma descrição deve atender para ser considerada adequada, nem qual é o fluxo de aprovação para inclusão de novas tabelas ou campos.
205.	Causa 2, Ausência de cultura de "Data Literacy". A governança de dados não foi tratada como prioridade institucional. Documentação de metadados é frequentemente vista como "custo" e não como "investimento", uma burocracia a ser cumprida em vez de um ativo estratégico a ser cultivado. Essa perspectiva ignora que dados sem documentação perdem valor institucional: não podem ser auditados com confiança, não podem ser integrados com segurança, e não podem ser transferidos para novos desenvolvedores sem perda de conhecimento.
Causas contributivas
206.	Causa 3, Documentação "post-mortem" e fragmentada. A análise da estrutura do dicionário indica que a documentação foi elaborada após o desenvolvimento do sistema, não durante, uma prática conhecida como documentação "post-mortem". O resultado são descrições que repetem o nome do campo em outras palavras (56,2% tautológicas) ou que fornecem informação genérica e incompleta (34,3%). Além disso, há fragmentação documental: o documento CAF_DRN (Documento de Regras de Negócio, peça 78) contém definições semânticas relevantes, por exemplo, a regra RN1.19 especifica que a área de aquicultura deve ser expressa em "metros cúbicos" ou "hectares", mas essas informações não foram incorporadas ao dicionário de dados.
207.	Causa 4, Ausência de ferramentas adequadas. O dicionário de dados do CAF é mantido em formato CSV/Excel, um artefato estático que pode desatualizar no instante seguinte à sua criação. Não há integração automatizada entre o esquema do banco de dados e o arquivo de documentação: quando uma tabela é criada ou alterada no banco de dados, essa mudança não se reflete automaticamente no dicionário.
208.	Causa 5, Legado histórico sem revisão. O sistema do CAF está em operação há mais de uma década, tendo evoluído através de múltiplas versões (CAF 1.0, 2.0, 3.0) e gerações de desenvolvedores. Sistemas de longa duração acumulam naturalmente "dívida técnica documental", documentação que era adequada na época de criação, mas que não foi mantida atualizada ao longo das evoluções subsequentes.
209.	Causa 6, Falta de integração entre equipes. A qualidade de um dicionário de dados depende da colaboração entre duas expertises distintas: os desenvolvedores conhecem a estrutura técnica do sistema, enquanto os analistas de negócio conhecem o significado funcional das informações. No sistema do CAF, há evidências de que esse conhecimento existe, mas permanece isolado em silos funcionais.
Efeitos
210.	O único efeito concreto é o seguinte:
210.1.	Efeito 1, Dificuldade de compreensão. A deficiência mais imediata decorrente da baixa qualidade do dicionário de dados é a impossibilidade de compreender plenamente o significado das informações de forma autônoma. 
Riscos
211.	Os riscos são os seguintes:
211.1.	Risco 1, Risco de erros em integrações e análises. Sistemas externos que consomem dados do CAF, como plataformas de crédito rural, sistemas de monitoramento ambiental ou bases estatísticas do IBGE, dependem de interpretação correta dos campos para realizar cruzamentos válidos. Quando 84% dos campos numéricos não especificam unidade de medida e 92% dos campos temporais são ambíguos, o risco de mapeamentos incorretos é substancial.
211.2.	Risco 2, Dependência crítica dos "Gurus do Sistema". Com 94,1% das descrições inadequadas, o conhecimento sobre o significado real dos campos está concentrado em poucos indivíduos, tipicamente desenvolvedores sêniores que participaram da construção e evolução do sistema ao longo dos anos. Se essas pessoas-chave deixarem a organização (por aposentadoria, transferência ou qualquer outro motivo), o conhecimento institucional sobre a estrutura de dados corre o risco de se perder junto.
211.3.	Risco 3, Dificuldade de manutenção evolutiva. Novos desenvolvedores que ingressam na equipe do CAF enfrentam uma curva de aprendizado desnecessariamente íngreme. Em vez de consultar um dicionário de dados para compreender a estrutura do sistema, eles precisam "descobrir" o significado dos campos através de engenharia reversa do código-fonte, análise exploratória dos dados ou consultas repetidas aos colegas mais experientes.
211.4.	Risco 4, Impossibilidade de automatização analítica. Ferramentas modernas de Business Intelligence (BI) e análise de dados dependem de metadados de qualidade para funcionar adequadamente. Um catálogo de dados bem documentado permite que ferramentas de BI gerem automaticamente descrições de campos, sugiram relacionamentos entre tabelas e alertem sobre inconsistências. Quando o dicionário de dados é inadequado, essa automatização torna-se impossível.
Benefícios Esperados
212.	A correção das deficiências identificadas traria benefícios concretos para a gestão e a auditabilidade do CAF:
212.1.	rastreabilidade auditável: auditores poderão validar a estrutura de dados sem depender de explicações verbais;
212.2.	redução de erros: menor risco de interpretações incorretas em integrações e análises;
212.3.	preservação do conhecimento: informações sobre o sistema deixarão de estar concentradas em poucos indivíduos;
212.4.	facilitação de integrações: sistemas externos poderão consumir dados do CAF com segurança semântica e vice-versa;
212.5.	independência operacional: análises e relatórios não dependerão dos "gurus do sistema" para interpretação.
Conclusão
213.	Em síntese, o Achado IV demonstra que o dicionário de dados do CAF apresenta deficiências estruturais em três das quatro dimensões analisadas. Essas deficiências não são meras questões de TI: elas comprometem a capacidade de verificação independente de um sistema que sustenta políticas públicas para milhões de famílias da agricultura familiar brasileira.
214.	Em síntese, o resultado da avaliação realizada pela equipe de auditoria permite concluir que:
214.1.	o dicionário de dados atualizado possui cobertura completa, todas as 95 tabelas efetivamente em uso pelo sistema estão documentadas (peça 70);
214.2.	as descrições dos campos não fornecem significado de negócio compreensível, já que 94,1% são semanticamente inadequadas (496 de 527 campos) (peça 135, p. 4), limitando-se a repetir o nome técnico em outras palavras (56,2% tautológicas) ou fornecer informação genérica e incompleta (34,3%);
214.3.	os campos numéricos não possuem unidades de medida definidas em 84% dos casos (105 de 125 campos) (peça 136, p. 4-5), incluindo campos críticos como área do imóvel e renda familiar, cujas unidades deveriam estar documentadas para evitar ambiguidades;
214.4.	os campos temporais não têm semântica clara em 92,0% dos casos (80 de 87 campos) (peça 133, p. 5), não distinguindo eventos de sistema (momento de inserção no banco de dados) de eventos de negócio (data de inscrição do agricultor).
215.	As deficiências de documentação identificadas neste achado funcionam como uma causa estrutural que amplifica os problemas encontrados nos achados anteriores (I, II e III). Corrigir o dicionário de dados é, portanto, pré-requisito estrutural para que as correções nos dados sejam sustentáveis a longo prazo.
 
Propostas de Encaminhamento
216.	D1) Para reduzir ambiguidades interpretativas, aumentar a confiabilidade do uso dos dados do CAF e dar sustentação técnica às ações de melhoria da qualidade cadastral, a Unidade Técnica propõe determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução - TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação, com responsáveis e prazos, para avaliar as falhas na qualidade de dados e de documentos do CAF apontadas no relatório de auditoria e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial:
216.1.	deficiências de qualidade do dicionário de dados, incluindo descrições semanticamente inadequadas ou ambíguas e ausência de especificação de unidades de medida nas descrições dos campos numéricos.
217.	Espera-se que o saneamento dessas deficiências no dicionário de dados aumente a clareza semântica, a padronização e a rastreabilidade dos dados, reduzindo erros de interpretação entre áreas de negócio e tecnologia, facilitando integrações e fortalecendo a auditabilidade e a governança do CAF.
218.	E1) Para fortalecer a governança de dados do CAF e sustentar, no longo prazo, a qualidade cadastral e a confiabilidade das integrações e análises, a Unidade Técnica propõe recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução TCU 315/2020, que:
218.1.	aperfeiçoe o processo institucional de gestão de metadados do CAF, incluindo a incorporação de definições semânticas no dicionário de dados com base nas regras de negócio do sistema e no marco legal aplicável, com definição de papéis e responsabilidades (data owners e data stewards), padrões mínimos de documentação e revisão contínua integrada ao ciclo de desenvolvimento e implantação do sistema, de modo a reduzir ambiguidades interpretativas e fragmentação documental, em consonância com as boas práticas da ISO/IEC 11179:2015, do DAMA-DMBOK v2 e do COBIT 2019 (BAI08, Gestão do Conhecimento).
219.	Espera-se que a implementação da medida reduza dependência de conhecimento tácito, melhore a interoperabilidade entre sistemas e dê maior previsibilidade à manutenção e evolução do cadastro, com ganhos de auditabilidade, eficiência operacional e qualidade da informação utilizada na formulação e execução de políticas públicas.
4.	Conclusão
220.	De modo geral, esta auditoria analisou quatro dimensões críticas da qualidade do CAF: a adequação dos documentos comprobatórios de elegibilidade (Achado I), a integridade dos dados geoespaciais (Achado II), a consistência dos dados cadastrais de pessoas físicas e jurídicas (Achado III), e a completude da documentação técnica do sistema (Achado IV). De certa forma, todos os achados referem-se a uma causa comum: falhas de governança e de gestão de dados do CAF que estabeleça controles automatizados, integração com bases oficiais e processos de curadoria cadastral.
221.	No que se refere à qualidade dos documentos comprobatórios, verificou-se que 27,1% dos documentos apresentados são semanticamente inadequados — ou seja, não comprovam efetivamente os requisitos legais que declaram comprovar —, projetando-se cerca de 3,08 milhões de documentos problemáticos na população total de 11,44 milhões. Adicionalmente, 53,55% dos documentos com área identificável apresentam divergências críticas superiores a 10%, 33,33% dos documentos de imóveis são de tipo inadequado, e 68,7% possuem resolução inferior ao padrão técnico de 300 DPI estabelecido pela Resolução - CONARQ 31/2010.
222.	Essas deficiências decorrem de cinco causas interdependentes identificadas, referentes à ausência ou falha de: controles de qualidade técnica de digitalização; validação automatizada de documentos no momento do upload; integração com bases georreferenciadas oficiais; além de inviabilidade de revisão manual dada a escala de cerca de 11 milhões de documentos e deficiências na capacitação de cadastradores. 
223.	Quanto à integridade geoespacial, a auditoria identificou deterioração crítica da qualidade cartográfica, com taxa de erro de 45,92% no CAF 3.0 (aumento de 40,6% em relação à versão anterior) e comprometimento massivo da unicidade dos registros: 55,27% dos imóveis com coordenadas de alta precisão compartilham coordenadas geográficas idênticas com outros cadastros (cerca de 1,75 milhão de imóveis que não podem ser distinguidos espacialmente). Outrossim, verificou-se inflação cadastral em 632 municípios (11,43% do total), onde a área cadastrada supera a área oficial estabelecida pelo IBGE.
224.	As causas identificadas incluem a ausência ou falha de: controles automatizados de validação cartográfica (limites geográficos do Brasil, unicidade espacial, consistência municipal); integração com a malha municipal oficial do IBGE; testes de regressão durante transições tecnológicas; processos de curadoria para correção do passivo histórico; e governança e gestão de dados geoespaciais com métricas monitoradas.
225.	No que se refere à qualidade dos dados cadastrais de pessoas, identificaram-se 15.811 inconsistências críticas em dados de identidade civil, incluindo 3.097 responsáveis com óbito confirmado no Sisobi que permanecem ativos, 89 menores de 16 anos cadastrados como responsáveis por Unidades Familiares, e 11.999 divergências de data de nascimento entre CAF e bases de dados da RFB. Ademais, constatou-se que 90,62% dos e-mails de pessoas físicas são fictícios, dificultando comunicação institucional com aproximadamente 5,9 milhões de e-mails. Também foram identificadas 139 Unidades Familiares com renda agregada superior a R$ 10 milhões, evidenciando ausência de validação de plausibilidade, e 39 pessoas jurídicas com CNAEs incompatíveis (hipermercados, atacadistas, construtoras) às quais estão vinculados 10.377 agricultores em situação de risco.
226.	As causas fundamentais identificadas estão relacionadas à ausência ou falha de: controles automatizados de validação semântica (CPF, idade, plausibilidade de renda); processos de coleta permissivos que aceitam valores fictícios para contornar campos obrigatórios; rotinas de curadoria cadastral; integração com bases oficiais; e como causa-raiz principal, ausência ou falha de governança de dados do CAF.
227.	A análise do dicionário de dados do CAF revelou deficiências estruturais em três das quatro dimensões analisadas: 94,1% das descrições existentes são semanticamente inadequadas, 84,0% dos campos numéricos não especificam unidade de medida, e 92,0% dos campos temporais apresentam ambiguidade semântica. Nenhuma das 28 definições formais do art. 2º da Portaria - MDA 19/2025 está refletida no dicionário. Por outro lado, verificou-se que a cobertura do dicionário é completa (100%) para as 95 tabelas ativas do sistema. 
228.	Essas lacunas decorrem de ausência ou falha de processo de gestão de metadados e de implementação da cultura de dados (Data Literacy”) no órgão. Além disso, outras causas possíveis são: documentação elaborada "post-mortem" (após o desenvolvimento) e fragmentada entre múltiplos artefatos não integrados; ausência de ferramentas automatizadas de gestão de metadados; e falta de integração entre equipes técnicas e de negócio.
Governança como Causa Transversal
229.	A ausência de governança de dados, identificada como causa em todos os quatro achados, constitui o fator estrutural que viabiliza a persistência das deficiências documentadas. Sem política formal de qualidade de dados, sem curadores e responsáveis designados (data stewards e data owners), sem métricas monitoradas, sem processos de curadoria cadastral e sem ferramentas adequadas de gestão de metadados, o sistema opera em ciclo de deterioração progressiva: dados inadequados entram sem validação, não são detectados pela ausência de monitoramento, e se acumulam indefinidamente até que uma auditoria externa os identifique.
230.	A magnitude dos problemas identificados — afetando documentos, coordenadas, cadastros) e metadados — combinada com o volume de recursos públicos em risco torna necessária a adoção de medidas corretivas que enderecem simultaneamente as dimensões tecnológica (implementação de controles automatizados e integração com bases oficiais), processual (saneamento do estoque de inconsistências e curadoria cadastral) e organizacional (estabelecimento de governança de dados com responsabilidades claras e métricas de qualidade).
231.	A implementação das recomendações propostas ao longo do relatório e consolidadas no próximo capítulo poderá contribuir para o rompimento desse ciclo, criando capacidade institucional para manutenção sustentada da qualidade cadastral. A designação de papéis e responsabilidades para a gestão do CAF, o estabelecimento de métricas de qualidade monitoradas continuamente e a implementação de dashboards gerenciais possibilitarão a detecção precoce de deteriorações futuras, evitando que problemas se acumulem sem visibilidade da gestão.
232.	Sem essas correções estruturais, o CAF continuará comprometido em sua função primordial de garantir que os benefícios da agricultura familiar alcancem exclusivamente quem demonstra documentalmente e faticamente atender aos requisitos da Lei 11.326/2006. A interdependência das causas identificadas — convergindo para a falhas de governança de dados do CAF— reforça a necessidade de abordagem integrada, já que correções pontuais em uma dimensão serão insustentáveis enquanto as deficiências nas demais dimensões não forem igualmente endereçadas.
233.	Por fim, tendo em vista a existência de propostas de encaminhamento com conteúdo similar em achados distintos ao longo do relatório, optou-se por fazer a consolidação de algumas delas no capítulo 5 deste relatório, porém sem perda de conteúdo. 
5.	Comentários dos gestores
234.	Considerando a possibilidade de construção participativa das deliberações deste Tribunal, nos termos do art. 14 da Resolução-TCU 315/2020, bem como o previsto nas Normas de Auditoria (NAT) aprovadas pela Portaria-TCU 280/2010, referente aos comentários dos gestores, será oportunizado prazo de quinze dias ao Ministério do Desenvolvimento Agrário e Agricultura Familiar para a apresentação de comentários, caso queiram, bem como informações quanto às consequências práticas da implementação das medidas aventadas e eventuais alternativas.
6.	Propostas de Encaminhamento
235.	Ante o exposto, submete-se o presente relatório à consideração superior para que seja enviado ao Ministério do Desenvolvimento Agrário e Agricultura Familiar para apresentação de comentários sobre as propostas a seguir.
236.	Determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução - TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação, com responsáveis e prazos, para avaliar as falhas na qualidade de dados e de documentos do CAF apontadas no relatório de auditoria e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial:
236.1.	documentos inadequados para comprovar os requisitos de elegibilidade;
236.2.	documentos de imóveis que apresentam divergências críticas de área em relação à base de dados;
236.3.	documentos com resolução inferior ao padrão definido pela Resolução - Conarq 31/2010; 
236.4.	o passivo histórico de dados geoespaciais com falhas, em especial duplicações espaciais, inflação cadastral e inconsistências municipais;
236.5.	impropriedades de capacidade civil e legitimidade dos responsáveis;
236.6.	dados de contato fictícios;
236.7.	inconsistências de dados de renda; e
236.8.	inconsistências de natureza jurídica de pessoas jurídicas cadastradas;
236.9.	 deficiências de qualidade do dicionário de dados, incluindo descrições semanticamente inadequadas ou ambíguas e ausência de especificação de unidades de medida nas descrições dos campos numéricos.
237.	Recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução TCU-315/2020, que:
237.1.	reavalie e aperfeiçoe os processos de cadastramento, atualização e controle de qualidade dos dados do CAF, de forma a torná-lo compatível com a escala e a criticidade do cadastro para implementação de políticas públicas da agricultura familiar, contemplando mecanismos de prevenção à inserção e permanência de dados inválidos, em especial:
237.1.1.	padronização de procedimentos para cadastramento e atualização do CAF pela rede de cadastradores, incluindo validação e garantia de qualidade de documentos, regras para coletar e validar coordenadas, revisão periódica baseada em risco/amostragem e mecanismos de orientação e supervisão dos cadastradores;
237.1.2.	aperfeiçoamento das regras de negócio e implementação de controles automatizados de validação em campos críticos, com ênfase em qualificação e validação dos documentos anexados, consistência espacial e cartográfica (ex.: município/UF, unicidade espacial e plausibilidade de área) e verificação de semântica cadastral (ex.: identidade civil, datas, renda e dados de contato);
237.1.3.	interoperabilidade com bases oficiais pertinentes (ex.: CPF, CNAE, CEP, óbitos e bases geoespaciais oficiais, como as malhas do IBGE, o acervo fundiário do Incra e o CAR), para detecção tempestiva de erros e anomalias na entrada de documentos e dados e redução de retrabalho de saneamento;
237.1.4.	adoção de requisitos mínimos de qualidade técnica dos documentos digitalizados, inclusive padrão de resolução compatível que assegure validação automatizada e auditabilidade do acervo, a exemplo do padrão de resolução de 300 DPI definido pela Resolução - Conarq 31/2010;
237.2.	reavalie e aprimore o processo de gestão de mudanças e garantia da qualidade das evoluções do Sistema CAF, com foco no ciclo de desenvolvimento, homologação e implementação de novas versões, de forma a prevenir regressões funcionais e de dados, em alinhamento com as boas práticas do Cobit 2019 (BAI10);
237.3.	 desenvolva e implemente mecanismos de acompanhamento gerencial (tais como relatórios periódicos, painéis de indicadores ou dashboards) para monitoramento contínuo da qualidade dos dados e informações do CAF, de modo a subsidiar a priorização de ações corretivas e a avaliação da efetividade das medidas adotadas para aprimoramento da qualidade cadastral e documental do Cadastro, contemplando indicadores de qualidade, como  percentuais de óbitos ativos, CPFs não localizados, divergências biográficas, e-mails inválidos, CEPs genéricos ou inconsistentes, outliers de renda e CNAEs incompatíveis;
237.4.	aperfeiçoe o processo institucional de gestão de metadados do CAF, incluindo a incorporação de definições semânticas no dicionário de dados com base nas regras de negócio do sistema e no marco legal aplicável, com definição de papéis e responsabilidades (data owners e data stewards), padrões mínimos de documentação e revisão contínua integrada ao ciclo de desenvolvimento e implantação do sistema, de modo a reduzir ambiguidades interpretativas e fragmentação documental, em consonância com as boas práticas da ISO/IEC 11179:2015, do DAMA-DMBOK v2 e do COBIT 2019 (BAI08, Gestão do Conhecimento).
238.	Informar ao Ministério do Desenvolvimento Agrário do acórdão que vier a ser proferido, destacando que o relatório e o voto que fundamentam a deliberação ora encaminhada podem ser acessados por meio do endereço eletrônico www.tcu.gov.br/acordaos.
239.	Nos termos do art. 8º da Resolução - TCU 315, de 2020, fazer constar, na ata da sessão em que estes autos forem apreciados, comunicação do Relator ao colegiado no sentido de autorizar o monitoramento das recomendações propostas neste relatório;
240.	Arquivar os presentes autos, com fundamento no art. 169, V, do Regimento Interno do TCU. 

Dadsis/AudTI, 11/2/2026

Assinado digitalmente
Fernando Lima Gama Júnior
AUFC – Matrícula 6499-8
Coordenador	Assinado digitalmente
Sylvio Xavier Júnior
AUFC – Matrícula 2423-6

Assinado digitalmente
Harley Alves Ferreira
AUFC – Matrícula 5666-9
Supervisor
 
Apêndice I – Método
1.	O método empregado na presente auditoria foi baseado na Matriz de Planejamento aprovada (Apêndice II), que estabeleceu seis grupos de procedimentos: (i) verificação de regras de negócio; (ii) data profiling de qualidade de dados; (iii) rastreabilidade e logs; (iv) cruzamentos de bases governamentais; (v) análise de governança de dados; e (vi) investigação de causas e efeitos. 
2.	O data profiling consiste na análise técnica detalhada dos dados disponíveis em uma fonte de informação, visando compreender sua estrutura, conteúdo e relacionamentos. Essa técnica permite identificar padrões, anomalias e inconsistências (como campos nulos, formatos inválidos ou valores fora do padrão esperado) antes mesmo de se iniciar a análise de negócio propriamente dita, funcionando como um diagnóstico prévio da saúde da base de dados.
3.	Durante a execução, a equipe identificou oportunidades de aprofundamento que levaram à realização de procedimentos adicionais. Todos os achados foram sustentados mediante requisições de informações, análise de documentos normativos e reuniões com gestores do MDA (Atas de reuniões de 07/10/2025 e 21/10/2025, peças 73 e 74), conforme tabela abaixo:
Peça	Reunião	Data
71	Ata de reunião apresentação da equipe	1º/7/2025
72	Ata de reunião de abertura	3/7/2025
73	Ata de reunião de trabalho de campo	7/10/2025
74	Ata de reunião de encerramento	21/10/25
4.	Para essa avaliação, foram adotados como critérios técnicos:
4.1.	Governança de TI: Cobit 2019 (ISACA), domínios APO11 (Gestão da Qualidade), BAI08 (Gestão do Conhecimento) e BAI10 (Gestão de Configuração);
4.2.	Qualidade de Dados: ISO/IEC 25012:2008, que define características de Acurácia, Consistência e Completude;
4.3.	Dados Geoespaciais: ISO 19157-1:2023 (Qualidade de Dados Geográficos);
4.4.	Metadados: ISO/IEC 11179:2015 (Registro de Metadados);
4.5.	Gestão de Dados: DAMA-DMBOK v2.
5.	Foram aplicadas técnicas de Análise de Dados (Data Analytics), Inteligência Artificial para leitura de documentos e cruzamento massivo com bases oficiais (Receita Federal, Sisobi e INCRA). A avaliação revelou um cenário de fragilidade sistêmica na governança e na qualidade dos dados do CAF, materializada em quatro eixos de deficiências:
5.1.	(i) Inadequações nos Documentos Comprobatórios de Elegibilidade (Achado I): insuficiência semântica e técnica dos documentos de terra e renda para habilitação de beneficiários;
5.2.	(ii) Deterioração da Qualidade Cartográfica (Achado II): sobreposições críticas, coordenadas implausíveis e "inflação cadastral" de áreas municipais;
5.3.	(iii) Comprometimento da Qualidade Cadastral (Achado III): responsáveis falecidos, menores de idade, dados fictícios e valores estatisticamente impossíveis;
5.4.	(iv) Incompletude do Dicionário de Dados (Achado IV): documentação deficiente que compromete auditabilidade e manutenção do sistema.
6.	O Achado I (Inadequações nos documentos comprobatórios) implementou os procedimentos 1.2 (adequação de documentos) e 1.1 (verificação de regras de negócio - tamanho de propriedade). A equipe analisou: 
6.1.	(i) Adequação semântica (Procedimento 1.2): Amostra probabilística estratificada de documentos comprobatórios, avaliando se os documentos inseridos no sistema correspondiam semanticamente ao tipo declarado. Durante essa análise, identificou-se oportunidade de aprofundamento: achado incidental sobre resolução de digitalização (DPI), em desconformidade com parâmetros técnicos da Resolução - CONARQ 31/2010;
6.2.	(ii) Acurácia de áreas (Procedimento 1.2): Subamostra de documentos com extração automatizada de áreas via inteligência artificial generativa (Claude Vision AI), comparando valores extraídos dos documentos com os registrados no banco de dados; 
6.3.	(iii) Limite de 4 módulos fiscais (Procedimento 1.1): Análise censitária da população completa de propriedades cadastradas, verificando conformidade com o requisito legal da Lei 11.326/2006, art. 3º, inciso I.
7.	O Achado II (Deterioração da qualidade cartográfica e comprometimento da integridade geoespacial) implementou os procedimentos 1.3 (consistência de coordenadas), 2.3 (duplicados espaciais) e 2.6 (acurácia geoespacial). A equipe realizou: 
7.1.	(i) Análise temporal multiperíodo (Procedimento 1.3): Durante o período de execução, o Sistema CAF passou por duas transições tecnológicas (CAF 3.0 em março/2025 e interface Leaflet em agosto/2025). A equipe aproveitou essa janela de oportunidade para realizar análise comparativa de três períodos, avaliando o impacto das mudanças tecnológicas na qualidade das coordenadas geoespaciais;
7.2.	(ii) Duplicações espaciais (Procedimento 2.3): Análise de coordenadas idênticas para identificar registros que compartilham as mesmas coordenadas geográficas, comprometendo a rastreabilidade espacial individual;
7.3.	(iii) Inflação cadastral (Procedimento 2.6): Achado não planejado identificado durante validação de acurácia geoespacial, comparando a área total cadastrada por município com a área oficial registrada pelo IBGE.
8.	O Achado III (Comprometimento da qualidade de dados cadastrais de pessoas físicas e jurídicas) implementou os procedimentos 3.1 (cruzamentos de dados), 2.4 (atualização de dados), 2.5 (conformidade de domínios) e 2.6 (acurácia de renda). A equipe realizou:
8.1.	(i) Cruzamentos triplos CAF×RFB×SISOBI (Procedimento 3.1): Cruzamentos com bases governamentais disponíveis no LabContas para identificar CPFs com situação cadastral irregular (óbitos, incapazes legais, não localizados na RFB);
8.2.	(ii) Análise de outliers estatísticos (Procedimento 2.6): Análise de distribuição de renda declarada para identificar valores extremos potencialmente incompatíveis com o perfil de agricultura familiar; 
8.3.	(iii) Validação de CNAEs (Procedimento 3.1): Identificação de códigos de atividade econômica incompatíveis com agricultura familiar;
8.4.	(iv) Qualidade de contatos (Procedimento 2.5): Validação de formato de e-mails e análise de CEPs genéricos (Procedimento 2.2).
9.	O Achado IV (Incompletude e baixa qualidade do dicionário de dados) implementou os procedimentos 4.1 (análise documental de governança) e 2.7 (rastreabilidade de origem). A equipe analisou:
9.1.	(i) Cobertura de tabelas (Procedimento 4.1): Análise estruturada por ISO/IEC 11179:2015 da cobertura do dicionário de dados oficial;
9.2.	(ii) Descrições de negócio (Procedimento 4.1): Avaliação da clareza semântica das descrições de campos;
9.3.	(iii) Unidades de medida (Procedimento 4.1): Verificação de padronização de dados numéricos;
9.4.	(iv) Semântica temporal (Procedimento 2.7): Rastreabilidade de metadados (data_criacao, data_atualizacao).
 
Apêndice II – Trabalhos Anteriores do TCU
1.	O Tribunal de Contas da União tem atuado sistematicamente na fiscalização das fragilidades associadas à identificação e qualificação dos agricultores familiares. Este apêndice detalha o histórico de fiscalizações que fundamentam o contexto da presente auditoria.
Auditoria na DAP (Acórdão 1.197/2018-TCU-Plenário)
2.	O trabalho mais emblemático sobre o tema foi consubstanciado no Acórdão 1.197/2018-TCU-Plenário (Relator Min. André de Carvalho), fruto de auditoria na antiga Declaração de Aptidão ao Pronaf (DAP). Naquela ocasião, o Tribunal identificou **1.335.852 DAPs com indícios de irregularidade**.
3.	As inconsistências incluíam titulares falecidos, renda superior ao limite legal, beneficiários detentores de cargos públicos e empresários não agrícolas, evidenciando a fragilidade histórica do modelo baseado majoritariamente em autodeclaração sem a devida validação via cruzamento de dados.
4.	Do relatório daquela auditoria, destacam-se os seguintes trechos:
ACHADO 3.1 (§24 do Relatório de Auditoria, TC 012.700/2017-7, Rel. Ministro André Luís de Carvalho): Foram identificados indícios de irregularidades em 1.335.852 de DAPs emitidas para Unidades Familiares de Produção Rural (UFPR) (11,15% do total de emissões), e em 542 para formas associativas com DAP ativa (7,81% do total de emissões) no período de 2007 a 2017. Deste total, 640.460 DAPs de unidades familiares e 315 de formas associativas acessaram programas e políticas públicas federais direcionados à agricultura familiar analisados no período de 2010 a 2017.
(...)
CAUSAS (§39 do Relatório de Auditoria): As principais causas identificadas para a situação encontrada foram: a regulamentação insuficiente do processo de emissão pela SAF/Sead; a falta de treinamento para os agentes emissores; as deficiências no sistema de gerenciamento do processo de emissão de DAP; e a insuficiência dos controles prévios à emissão desta declaração.
(...)
VALOR EM RISCO (§36 do Relatório de Auditoria): Somados todos os indícios e caso confirmadas as irregularidades apontadas, a aplicação irregular de recursos, dos onze programas avaliados, em UFPR pode chegar a mais de 14 bilhões de reais e aproximadamente 660 milhões de reais em formas associativas.
Sistema Nacional de Crédito Rural (Acórdão 1.708/2017-TCU-Plenário)
5.	A ineficácia dos instrumentos de identificação do público-alvo também foi objeto de análise no Acórdão 1.708/2017-TCU-Plenário (Relator Min. Augusto Nardes), que tratou de Levantamento no Sistema Nacional de Crédito Rural (SNCR).
6.	Naquela oportunidade, o Tribunal constatou que a DAP não era eficaz para blindar o acesso ao Pronaf aos agricultores familiares, uma vez que produtores não familiares conseguiam acessar linhas de crédito subsidiadas, tendo identificado 584.286 indícios de que o enquadramento dos beneficiários do Pronaf para a emissão da DAP foi realizado de maneira irregular. Adicionalmente, o trabalho apontou a ausência de planejamento de longo prazo para a política agrícola, o que gerava riscos de desperdício de recursos públicos em renegociações de dívidas e subvenções.
7.	Sobre a ineficácia da DAP:
9.2.2. auditoria nos processos de emissão da Declaração de Aptidão ao Pronaf (DAP), incluindo análise do sistema informatizado de emissão, verificando se os mecanismos de controle são eficazes para a correta identificação do beneficiário da política de crédito rural;
(...)
Os auditores identificaram 584.286 indícios de que o enquadramento dos beneficiários do Pronaf para a emissão da DAP foi realizado de maneira irregular.” (Parágrafo 152 do voto)
8.	Sobre a ausência de planejamento de longo prazo:
26. É válido destacar, desde já, a necessidade de se conferir estabilidade ao arcabouço normativo. A ausência de um planejamento de longo prazo para a política agrícola, aliada a alterações frequentes e imprevisíveis em marcos regulatórios relevantes, gera insegurança jurídica ao setor produtivo e impede o planejamento de longo prazo das atividades agrícolas. Nesse contexto, Peres e Buainain assinalam os indesejáveis efeitos das instabilidades e incertezas geradas tanto por alterações nas variáveis macroeconômicas como na condução da política agrícola e pelos sinais contraditórios dados por sua instabilidade e, também, pelos antagonismos entre políticas de gestão comercial e as de crédito.” (Parágrafo 26 do voto)
Programa de Aquisição de Alimentos - PAA (Acórdão 646/2017-TCU-Plenário)
9.	O impacto direto dessas fragilidades cadastrais na execução da despesa foi verificado em auditorias de programas finalísticos. No âmbito do Programa de Aquisição de Alimentos (PAA), a fiscalização que deu origem ao Acórdão 646/2017-TCU-Plenário (Relator Min. Augusto Nardes) identificou 15.951 beneficiários com indícios de irregularidade (9,68% da amostra), incluindo casos de renda incompatível e falecidos:
O Tribunal de Contas da União (TCU) identificou 15.951 beneficiários do Programa de Aquisição de Alimentos (PAA) com indícios de irregularidades, o que representa 9,68% do total da amostra analisada. Os problemas detectados incluem: beneficiários com renda incompatível com o perfil de agricultor familiar, declarações de falecidos e propriedades rurais com área superior a quatro módulos fiscais. (Portal TCU, 5 de abril de 2017)  
Reforma Agrária (Acórdãos 775/2016 e 2.028/2015-TCU-Plenário)
10.	De forma análoga, no que tange à Reforma Agrária, as fiscalizações relativas aos Acórdãos 775/2016-TCU-Plenário e 2.028/2015-TCU-Plenário (ambos de relatoria do Min. Augusto Sherman) expuseram a concessão de lotes a políticos, empresários e servidores públicos, evidenciando a falta de integração entre o Sistema de Informações de Projetos de Reforma Agrária (Sipra) e outros cadastros governamentais para validação de elegibilidade.
TCU suspende concessão de benefícios da reforma agrária em todo o país. Decisão atinge quase 600 mil assentados e é resultado de fiscalização que identificou irregularidades na seleção de beneficiários.” (Notícia Portal TCU, 6 de abril de 2016) 
Infraestrutura e Interoperabilidade (Acórdão 2.279/2021-TCU-Plenário)
11.	No tocante à infraestrutura tecnológica necessária para superar esses desafios, a fiscalização que originou o Acórdão 2.279/2021-TCU-Plenário (Relator Min. Aroldo Cedraz) avaliou as plataformas de compartilhamento de dados entre órgãos federais (Conecta gov.br, GovData e Predic).
12.	O trabalho constatou as dificuldades do então Ministério da Agricultura em implantar sistemas interoperáveis, documentando a mora e os entraves para acesso a dados do CPF e do CNIS, geridos respectivamente pela Receita Federal e pelo INSS. A falta de interoperabilidade entre sistemas governamentais foi apontada como gargalo crítico para a validação automatizada de renda familiar, perpetuando a dependência de dados autodeclaratórios.
13.	Sumário oficial do Acórdão:
PLATAFORMAS DE COMPARTILHAMENTO DE DADOS. CONECTA. TRANSPARÊNCIA E CENTRALIZAÇÃO. PEDIDO DE COMPARTILHAMENTO DE DADOS. GOVERNANÇA DE DADOS. CADASTRO DE BASES DE DADOS DA UNIÃO. LGPD. BOAS PRÁTICAS. MONITORAMENTO.
14.	Sobre o processo:
RELATÓRIO DE ACOMPANHAMENTO (RACOM) do processo TC 031.158/2020-0, de que trata o Acórdão 1726/2020 - Plenário, referente a trabalho de acompanhamento das condições de compartilhamento de dados entre órgãos e entidades da Administração Pública Federal por meio de plataformas de interoperabilidade (ex.: GovData, ConectaGov e Predic)
Governança de Solos (Acórdão 1.942/2015-TCU-Plenário)
15.	Por fim, a dimensão territorial e cartográfica, essencial para o CAF 3.0, possui histórico de deficiências apontadas no Acórdão 1.942/2015-TCU-Plenário (Relator Min. Walton Alencar Rodrigues), sobre a Governança de Solos não Urbanos .
16.	Aquele trabalho expôs a insuficiência e a inconsistência de informações oficiais sobre solos, a dispersão da legislação, a falta de integração entre sistemas críticos (SNCR, CAR, Sigef), bem como sobreposições e insegurança jurídica fundiária, contextualizando os riscos cartográficos ora identificados na presente auditoria. O TCU, por meio do referido acórdão, determinou a inclusão de programa nacional de levantamento de solos no PPA, o que posteriormente originou o PronaSolos.
Continuidade da Ação de Controle
17.	A persistência desses riscos, agora em uma nova plataforma tecnológica, fundamenta a relevância e a tempestividade da presente ação de controle, ao passo que serve também para identificar se as determinações pretéritas, como a do item 9.2.6 do Acórdão 1.197/2018-TCU-Plenário, têm contribuído para a melhoria do sistema:
9.2.6. atente para a necessidade de observância das determinações prolatadas por este Acórdão nos estudos e na futura implementação do Cadastro Nacional da Agricultura Familiar (CAF), ao substituir a DAP para efeito de acesso às ações e às políticas destinadas à Unidade Familiar de Produção Agrária (UFPA) e aos empreendimentos familiares rurais, nos termos do Decreto nº 9.064, de 31 de maio de 2017.
18.	Dessa forma, o presente trabalho representa continuidade e aprofundamento das fiscalizações anteriores realizadas pelo TCU em políticas públicas da agricultura familiar, com foco específico na qualidade dos dados que sustentam a concessão de benefícios a 3,3 milhões de unidades familiares e movimentam bilhões anuais em recursos do orçamento.





 
 
Apêndice III – Matriz de Achados
Apêndice III.A – Matriz de Achados – Achado I
Auditoria de Qualidade de Dados no Sistema de Cadastro da Agricultura Familiar (CAF)	Matriz de Achados
TC 011.073/2025-0
OBJETIVO: identificar inconsistências e fragilidades nos dados que possam comprometer a execução das políticas públicas da área ambiental e da agricultura familiar	
Problema identificado: 
A auditoria identificou que 27,1% dos documentos apresentados no CAF são semanticamente inadequados para comprovar os requisitos de elegibilidade, projetando-se cerca de 3 milhões de documentos problemáticos. Adicionalmente, 53,55% dos documentos de imóveis apresentam divergências críticas de área superiores a 10% em relação à base de dados, com viés sistemático de +120,89%. A validação depende exclusivamente de análise documental manual, sem verificação automatizada de requisitos legais, e 68,7% das digitalizações têm resolução inferior ao padrão definido pelo Conselho Nacional de Arquivos (Conarq). As causas incluem processos permissivos, ausência de validação semântica e limitações técnicas na digitalização.
Riscos Mapeados:
R1) Devido a fragilidades sistêmicas na gestão do ciclo de vida dos dados cadastrais de agricultores familiares, que incluem falhas na entrada de dados (autodeclaração de informações e integração deficiente com outras bases governamentais), poderá ocorrer a consolidação da base de dados do CAF com informações fraudulentas ou incorretas (inverídicas, imprecisas, incompletas, desatualizadas e conflitantes), o que poderá levar à concessão indevida de benefícios e à exclusão de agricultores familiares legítimos do acesso a benefícios, como programas de crédito, assistência técnica e comercialização, impactando a efetividade das políticas de incentivo à agricultura familiar.
R2) Devido a limitações sistêmicas na capacidade de verificação e fiscalização dos dados constantes no CAF, decorrente tanto de falhas nos mecanismos de cruzamento de dados quanto da dificuldade em obter e tratar dados de referência externos de qualidade, poderá ocorrer a permanência, sem detecção, de informações fraudulentas ou incorretas, o que poderá levar a perda de recursos públicos por fraudes e desvios de recursos públicos para beneficiários indevidos, impactando a efetividade das políticas de incentivo à agricultura familiar.
Risco 3: Devido à inexistência de estrutura adequada de governança e gestão de dados, poderá ocorrer a indefinição de normas, padrões, papéis e responsabilidades, o que poderá levar à falta de documentação e orientação clara sobre dados, processos e critérios, impactando a transparência e a tomada de decisões baseadas em dados completos e confiáveis.
Questão de Auditoria: 

QST-1: Em que medida os mecanismos de verificação de dados do CAF (versão 3, período: março de 2025 a agosto de 2025) asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio, considerando-se como critérios a Lei 11.326/2006, as Portarias MDA nº 19/2025 e nº 20/2025, a norma ISO/IEC 25012:2008, o framework DAMA-DMBOK v2 e os princípios da Administração Pública? 
Subquestão (i): Os documentos comprobatórios apresentados pelos beneficiários do CAF são adequados para comprovar os requisitos de elegibilidade da agricultura familiar estabelecidos na legislação? 
Subquestão (ii): As áreas de imóveis rurais registradas na base de dados do CAF correspondem aos valores que constam nos documentos apresentados pelos beneficiários?
Achado I: 
Devido à inadequação do processo de validação e asseguramento da qualidade dos documentos e dados do CAF, incompatível com a escala e criticidade do cadastro (Causa raiz 1) e à ausência de um processo efetivo de garantia da qualidade técnica da digitalização (Causa raiz 2), ocorreram inadequações semânticas em 27,1% dos documentos (3,08 milhões), divergências críticas de área em 53,55% dos registros (1,44 milhão, com viés sistemático de +120,89%), digitalização com resolução inferior ao padrão técnico em 68,7% dos arquivos (2,33 milhões) e documentos de tipo inadequado em 33,33% dos casos (1,13 milhão) (Situação Encontrada), contrariando Lei nº 11.326/2006, Art. 3º (requisitos de elegibilidade), Portaria MDA nº 19/2025, Art. 8º (tipos documentais), Resolução Conarq nº 31/2010 (padrão de 300 DPI), ISO/IEC 25012:2008 (Acurácia, Consistência) e ISO 19157-1:2023 (Qualidade de Dados Geográficos) (Critérios), o que levou à impossibilidade prática de atestar a elegibilidade de 3,08 milhões de cadastros, comprometimento da base de dados para validação de requisitos legais de área e obstrução técnica à automação e auditabilidade do acervo documental (Efeitos), gerando risco de desvio de finalidade e aplicação indevida de recursos públicos (Pronaf, PAA, PNAE), insegurança jurídica e responsabilização de gestores e beneficiários, e risco de agravamento sistêmico por inércia operacional (Riscos).
Situação Encontrada	Critério	Efeitos e Riscos	Causas	Boas Práticas	Encaminhamentos	Benefícios esperados
S1) A análise revelou que 27,1% dos documentos são semanticamente inadequados, projetando-se 3,08 milhões de documentos inadequados na população total de 11,4 milhões de documentos cadastrados (IC 99%, margem ±4,5 p.p.). Exemplos: RG classificado como "documento de imóvel", notas fiscais de insumos apresentadas como comprovação de renda, selfies sem valor probatório, arquivos em branco.
S2) 53,55% dos documentos de imóveis com área válida identificável apresentam divergências críticas de área superiores a 10%, com divergência sistemática agregada de +120,89% (áreas cadastradas na base menores que nos documentos apresentados), projetando-se 1,44 milhão de documentos problemáticos (IC 95%, margem ±6,44 p.p.).
S3) 68,7% dos documentos digitalizados possuem resolução inferior a 300 DPI, violando o padrão técnico estabelecido pela Resolução Conarq nº 31/2010, projetando-se 2,33 milhões de documentos inadequados para tecnologias OCR.
S4) 33,33% dos documentos de imóveis rurais são de tipo inadequado para comprovação de propriedade ou posse, não correspondendo aos tipos documentais aceitos no Art. 8º, I, c da Portaria MDA nº 19/2025, projetando-se 1,13 milhão de documentos inadequados na população de 3,39 milhões de documentos de imóveis.
	K1) Lei nº 11.326/2006, Art. 3º: Estabelece os requisitos cumulativos (ex: área até 4 módulos fiscais, mão de obra familiar, renda, gestão familiar).
K2) Portaria MDA nº 19/2025, Art. 8º: Especifica os tipos documentais obrigatórios para inscrição no CAF (identificação, comprovante de residência, documentação de terra e renda).
K3) Resolução Conarq nº 31/2010: Recomenda resolução mínima de 300 DPI para digitalização/OCR.
K4) ISO/IEC 25012:2008: Características de Acurácia (correspondência aos valores reais) e Consistência (conformidade com regras de negócio).
K5) ISO 19157-1:2023: Estabelece princípios para qualidade de dados geoespaciais, incluindo acurácia posicional e consistência lógica de áreas.
	E1) Inviabilidade prática de atestar a elegibilidade de 3,08 milhões de cadastros (aprox. 25% da base), comprometendo a função do CAF como "porteiro" das políticas públicas. 
E2) Comprometimento da base de dados para validação de requisitos legais de área: 1,44 milhão de documentos com divergências críticas superiores a 10% não podem ser utilizados com segurança para planejamento ou monitoramento. 
E3) Obstrução técnica à automação e à auditabilidade do acervo documental: 68,7% dos documentos (2,33 milhões) com resolução inferior a 300 DPI dificultam ou impossibilitam a implementação de tecnologias OCR e validação semântica automatizada.
R1) Risco de desvio de finalidade e aplicação indevida de recursos públicos (Pronaf, PAA, PNAE) devido à elegibilidade não comprovada documentalmente.
R2) Risco de insegurança jurídica e responsabilização de gestores e beneficiários.
R3) Risco de agravamento sistêmico por inércia operacional: em nove meses, documentos inadequados podem ultrapassar 4 milhões	Causa raiz 1: Inadequação do processo de validação e asseguramento da qualidade dos documentos e dados do CAF, incompatível com a escala e criticidade do cadastro. A validação da elegibilidade depende de análise manual executada pela rede de cadastradores, intrinsecamente inviável dada a escala de 11,4 milhões de documentos.
Causa raiz 2: Ausência de um processo efetivo de garantia da qualidade técnica da digitalização, com requisitos e bloqueios mínimos para assegurar legibilidade e futura tratabilidade.
Causa contributiva 1: Insuficiência de controles preventivos/detectivos na entrada documental (validação semântica do conteúdo e aderência do tipo documental).
Causa contributiva 2: Limitações de interoperabilidade/verificação cruzada com bases georreferenciadas oficiais (Sigef, Sicar).
Causa contributiva 3: Fragilidades estruturais na captura/registro de área (potenciais erros sistemáticos de conversão de unidades), não mitigadas por validações de consistência.	BP1) Declarações de Veracidade apresentaram apenas 5,6% de inadequação (vs 36,6% em documentos de imóvel e 30,4% em documentos de renda), demonstrando que documentos estruturados e padronizados têm taxa de conformidade significativamente superior a documentos de livre apresentação. 
BP2) O CAF 3.0 implementou controles que reduziram o cadastramento de propriedades inelegíveis: 98,7% das propriedades que excedem 4 módulos fiscais foram cadastradas antes dessa versão.
BP3) Reconhecimento pelo MDA de desafios operacionais significativos (escala de 11,4 milhões de documentos, diversidade da agricultura familiar brasileira) que justificam a urgência de implementação de controles automatizados.de imóvel rural e 30,4% em renda), demonstrando que documentos estruturados e padronizados pelo próprio sistema têm taxa de conformidade significativamente superior aos de livre apresentação.	D1) Determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação que contemple ações, responsáveis e prazos, para avaliar as falhas apontadas no relatório de auditoria que resultam em problemas de qualidade dos dados do CAF, e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial: documentos inadequados para comprovar os requisitos de elegibilidade; documentos de imóveis que apresentam divergências críticas de área em relação à base de dados; documentos com resolução inferior ao padrão definido pela Resolução Conarq 31/2010. 
1) Recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução TCU 315/2020, que: reavalie e aperfeiçoe os processos de cadastramento, atualização e controle de qualidade do CAF, de forma a torná-lo compatível com a escala e a criticidade do cadastro para implementação de políticas públicas da agricultura familiar, contemplando mecanismos de prevenção à inserção e permanência de dados inválidos, em especial:  padronize procedimentos para cadastramento e atualização do CAF pela rede de cadastradores, incluindo validação e garantia de qualidade de documentos, revisão periódica baseada em risco/amostragem e mecanismos de orientação e supervisão dos cadastradores; aperfeiçoe as regras de negócio e implemente controles automatizados de validação em campos críticos, com ênfase na qualificação e validação dos documentos anexados; implemente interoperabilidade com bases oficiais pertinentes (ex: bases geoespaciais oficiais), para detecção tempestiva de anomalias e redução de retrabalho de saneamento; adote requisitos mínimos de qualidade técnica dos documentos digitalizados, inclusive padrão de resolução compatível que assegure validação automatizada e auditabilidade do acervo; desenvolva e implemente mecanismos de acompanhamento gerencial para monitoramento contínuo da qualidade dos documentos e das informações constantes do CAF.





	Quantificáveis:
B1) Maior confiabilidade da base cadastral: correção dos 3,08 milhões de documentos semanticamente inadequados e dos 1,44 milhão com divergências de área permitirá validar com segurança a elegibilidade de milhões de agricultores familiares.
B2) Economia de recursos públicos: A validação automatizada de requisitos legais e a integração com bases oficiais reduzirão o risco de direcionamento indevido de recursos de programas federais.
B3) Ganhos de eficiência operacional e redução de retrabalho. 
Qualitativos:
B4) Fortalecimento da credibilidade do CAF como instrumento confiável de habilitação prévia.
B5) Segurança jurídica para gestores públicos e beneficiários, mitigando riscos de responsabilização.
B6) Transparência e rastreabilidade das decisões de elegibilidade, permitindo auditabilidade dos critérios aplicados.
B7) Efetividade das políticas públicas de agricultura familiar.

 
Apêndice III.B – Matriz de Achados – Achado II
Auditoria de Qualidade de Dados no Sistema de Cadastro da Agricultura Familiar (CAF)	Matriz de Achados
TC 011.073/2025-0
OBJETIVO: identificar inconsistências e fragilidades nos dados que possam comprometer a execução das políticas públicas da área ambiental e da agricultura familiar	
Problema identificado:
A base de 3,17 milhões de imóveis rurais georreferenciados do Sistema CAF apresenta deterioração crítica da qualidade cartográfica e comprometimento da integridade geoespacial. A migração para o CAF 3.0 causou aumento de 40,6% na taxa total de erros cartográficos (de 32,7% para 45,9%), por relaxamento das validações de bounding box. Foram identificadas 8.527 duplicações espaciais exatas em 4.016 localizações, 147 municípios com "inflação cadastral" (área cadastrada superior à oficial), totalizando 16,5 milhões de hectares excedentes, e passivo de 11,65 milhões de coordenadas com precisão insuficiente. As causas incluem regressão de controles nas transições tecnológicas, ausência de validação cruzada com malha IBGE e acúmulo histórico não saneado.
Riscos Mapeados:
R1) Devido a fragilidades sistêmicas na gestão do ciclo de vida dos dados cadastrais de agricultores familiares, que incluem falhas na entrada de dados (autodeclaração de informações e integração deficiente com outras bases governamentais), poderá ocorrer a consolidação da base de dados do CAF com informações fraudulentas ou incorretas (inverídicas, imprecisas, incompletas, desatualizadas e conflitantes), o que poderá levar à concessão indevida de benefícios e à exclusão de agricultores familiares legítimos do acesso a benefícios, como programas de crédito, assistência técnica e comercialização, impactando a efetividade das políticas de incentivo à agricultura familiar.
R2) Devido a limitações sistêmicas na capacidade de verificação e fiscalização dos dados constantes no CAF, decorrente tanto de falhas nos mecanismos de cruzamento de dados quanto da dificuldade em obter e tratar dados de referência externos de qualidade, poderá ocorrer a permanência, sem detecção, de informações fraudulentas ou incorretas, o que poderá levar a perda de recursos públicos por fraudes e desvios de recursos públicos para beneficiários indevidos, impactando a efetividade das políticas de incentivo à agricultura familiar.
Risco 3: Devido à inexistência de estrutura adequada de governança e gestão de dados, poderá ocorrer a indefinição de normas, padrões, papéis e responsabilidades, o que poderá levar à falta de documentação e orientação clara sobre dados, processos e critérios, impactando a transparência e a tomada de decisões baseadas em dados completos e confiáveis.
Questão de Auditoria:

QST-1: Em que medida os mecanismos de verificação de dados do CAF (versão 3, período: março de 2025 a agosto de 2025) asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio, considerando-se como critérios a Lei 11.326/2006, as Portarias MDA nº 19/2025 e nº 20/2025, a norma ISO/IEC 25012:2008, o framework DAMA-DMBOK v2 e os princípios da Administração Pública?
Subquestão (i): Qual o impacto das mudanças tecnológicas (Interface Leaflet e Sistema CAF 3.0) na taxa de erros cartográficos?
Subquestão (ii): Qual a magnitude das duplicações espaciais e seu impacto na unicidade dos beneficiários?
Subquestão (iii): Qual a extensão do fenômeno da "inflação cadastral" (área cadastrada superior à área oficial do município)?
Achado II:
Devido à deficiência na gestão de mudanças e garantia de qualidade tecnológica (Causa raiz 1), insuficiência de governança e monitoramento contínuo da qualidade geoespacial (Causa raiz 2), ausência de processo de curadoria do passivo histórico (Causa raiz 3), insuficiência na formalização de requisitos de qualidade como requisitos não funcionais (Causa raiz 4) e fragilidades nas práticas e supervisão da rede de cadastradores (Causa raiz 5), ocorreram deterioração crítica da qualidade cartográfica com aumento de 40,6% na taxa de erro do CAF 3.0 (de 32,66% para 45,92%, afetando 1,46 milhão de imóveis), duplicações espaciais em 55,27% dos registros de alta precisão (projetando 1,75 milhão de imóveis sem rastreabilidade individual), inflação cadastral em 632 municípios (11,43%) com área cadastrada superior à área oficial do IBGE, inconsistência municipal em 15,92% dos registros (projetando 431.000 imóveis) e regressão de precisão decimal na interface Leaflet (14,33 p.p.) (Situação Encontrada), contrariando Lei nº 11.326/2006, Art. 3º, I (limite de 4 módulos fiscais), Decreto nº 9.064/2017 (CAF como instrumento de identificação), Decreto nº 10.046/2019, Art. 3º (governança de dados), ISO 19157-1:2023 (Qualidade de Dados Geográficos), ISO/IEC 25012:2008 (Acurácia, Consistência, Unicidade), COBIT 2019 BAI10 (Gestão de Configuração) (Critérios), o que levou à inviabilização da rastreabilidade individual e cruzamentos ambientais, comprometimento da validação de elegibilidade quanto ao limite de área e risco de distorção analítica e de decisões públicas baseadas em evidência inválida (Efeitos).
Situação Encontrada	Critério	Efeitos e Riscos	Causas	Boas Práticas	Encaminhamentos	Benefícios esperados
S1) A transição CAF 3.0 (março/2025) apresentou deterioração da qualidade cartográfica, com aumento da taxa de erro de 32,66% para 45,92% (+13,26 p.p., +40,6%), afetando aproximadamente 1,46 milhão de imóveis (análise de amostra estratificada temporal: n=32.728 registros, IC 99%). Os erros algorítmicos aumentaram de 20,31% para 32,07% (+11,76 p.p., +57,9%) e os erros geoespaciais de 12,35% para 13,85% (+1,50 p.p., +12,1%).
S2) A interface Leaflet (agosto/2025) operou trade-off algorítmico-semântico: eliminou 99,95% dos erros algorítmicos (22,22% → 0,01%), mas aumentou erros geoespaciais em 174% (11,83% → 32,46%), com redução total de apenas 1,58 p.p. (análise de amostra estratificada: n=30.860 registros, IC 99%).
S3) 24.215 registros (55,27% da amostra de alta precisão) compartilham coordenadas idênticas, projetando-se aproximadamente 1,75 milhão de imóveis sem rastreabilidade espacial individual (análise de n=43.812 registros com ≥5 casas decimais).
S4) 632 municípios (11,43% de 5.528) apresentam "inflação cadastral" com área cadastrada superior à área oficial do IBGE, incluindo 59 municípios (1,07%) com inflação >10× e 12 casos >100× (análise censitária — 100% dos municípios). Caso extremo: Penalva/MA com área cadastrada 2.248× superior à oficial.
S5) 15,92% dos registros de alta precisão (6.976 de 43.812) apresentam coordenadas fora dos limites do município declarado, projetando-se aproximadamente 431.000 imóveis com inconsistência municipal. Adicionalmente, 722 registros (1,65%) apresentam coordenadas em Unidade da Federação completamente distinta da declarada.
S6) As transições tecnológicas causaram regressão de precisão decimal: Leaflet reduziu alta precisão em 14,33 p.p. (90,59% → 76,26%).	K1) Lei nº 11.326/2006, Art. 3º, I: Estabelece como requisito cumulativo para caracterização do agricultor familiar não deter área maior que 4 módulos fiscais, cuja validação depende de dados geoespaciais confiáveis e rastreáveis.
 K2) Decreto nº 10.046/2019, Art. 3º: Estabelece princípios de governança pública de dados na Administração Pública Federal, incluindo integridade, rastreabilidade e transparência.
K3) Decreto nº 9.064/2017, Art. 1º: Institui o CAF como instrumento oficial de identificação e qualificação dos agricultores familiares. 
K4) ISO 19157-1:2023 (Qualidade de Dados Geográficos): Estabelece princípios para qualidade de dados geoespaciais, incluindo acurácia posicional, consistência lógica e integridade territorial. 
K5) ISO/IEC 25012:2008: Características de Acurácia (correspondência aos valores reais), Consistência (conformidade com regras de negócio) e Unicidade (ausência de duplicações). 
K6) COBIT 2019 BAI10 (Gestão de Configuração): Recomenda testes de regressão para detectar deterioração de controles antes da entrada em produção.	E1) Inviabilização da rastreabilidade individual e cruzamentos ambientais: A existência de 1,75 milhão de imóveis com coordenadas idênticas torna impossível distinguir propriedades individualmente para fiscalização de desmatamento ou sobreposição em áreas protegidas.
E2) Comprometimento da validação de elegibilidade quanto ao limite de área: Com taxa de erro cartográfico de 45,92% no CAF 3.0 (afetando ~1,46 milhão de imóveis), não há como validar confiavelmente se as propriedades respeitam o limite legal de 4 módulos fiscais.
R1) Risco de distorção analítica e de decisões públicas baseadas em evidência inválida: A fragilidade da base georreferenciada compromete análises territoriais e de planejamento, podendo resultar em alocação ineficiente de recursos.
R2) Risco operacional de "poluição" de integrações externas: Outras instituições (agências de crédito e órgãos ambientais) que consomem dados do CAF podem propagar os erros sistêmicos identificados.	Causa raiz 1: Deficiência na gestão de mudanças e garantia de qualidade tecnológica. As transições para o CAF 3.0 e a interface Leaflet evidenciam a ausência de testes de regressão capazes de detectar a deterioração de controles e trade-offs negativos antes da entrada em produção. 
Causa raiz 2: Insuficiência de governança e monitoramento contínuo da qualidade geoespacial. A inexistência de métricas formais, painéis (dashboards) e rotinas de monitoramento permitiu que taxas elevadas de erro e duplicações espaciais massivas passassem despercebidas.
Causa raiz 3: Ausência de processo de curadoria do passivo histórico. A estratégia de melhoria tecnológica focou exclusivamente na interface de novos cadastros, sem estabelecer um plano de remediação para o estoque de dados preexistente.
Causa raiz 4: Insuficiência na formalização de requisitos de qualidade como requisitos não funcionais.
Causa raiz 5: Fragilidades nas práticas e supervisão da rede de cadastradores.
Causa contributiva 1: Insuficiência de controles técnicos de validação e plausibilidade. 
Causa contributiva 2: Interoperabilidade limitada com bases geoespaciais oficiais. 	BP1) A implementação do CAF 3.0 foi substancialmente eficaz em bloquear inflação cadastral para novos registros: a taxa caiu de 10,89% para 0,31%, evidenciando que validações de plausibilidade foram implementadas para cadastros novos.
BP2) A interface Leaflet eliminou 99,95% dos erros algorítmicos, demonstrando que a mudança de interface de entrada manual para seleção visual pode sanar problemas de digitação.
BP3) A transição Leaflet reduziu drasticamente as duplicações em cadastros novos: de 92,36% (pré-Leaflet) para 16,59% (pós-Leaflet), evidenciando que boas práticas de interface podem prevenir problemas de qualidade.
BP4) O caso Salvador/BA (6.644 imóveis com mesma coordenada) foi identificado e documentado, permitindo ação corretiva focalizada.	D1) Determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação que contemple ações, responsáveis e prazos, para avaliar as falhas apontadas no relatório de auditoria que resultam em problemas de qualidade dos dados do CAF, e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial: o passivo histórico de dados geoespaciais com falhas, em especial duplicações espaciais, inflação cadastral e inconsistências municipais. 
E1) Recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução TCU 315/2020, que: reavalie e aprimore o processo de gestão de mudanças e garantia da qualidade das evoluções do CAF, com foco no ciclo de desenvolvimento, homologação e implementação de novas versões, de forma a prevenir regressões funcionais e de dados, em alinhamento com as boas práticas do Cobit 2019 (BAI10); aperfeiçoe as regras de negócio e implemente controles automatizados de validação cartográfica do CAF para validação espacial e consistência dos dados (ex: município/UF, unicidade espacial e plausibilidade), incluindo verificações cruzadas com bases oficiais pertinentes (ex: malhas do IBGE, acervo fundiário do Incra e CAR); avalie e implemente medidas de orientação e padronização de práticas de captura de coordenadas pela rede cadastradora.	Quantificáveis:
B1) Conformidade legal: Adequação de aproximadamente 1,46 milhão de registros com erros cartográficos e 1,75 milhão de imóveis duplicados espacialmente.
B2) Rastreabilidade operacional: A correção de duplicações permitirá análises geoespaciais automatizadas identificarem individualmente cada imóvel.
 Qualitativos:
B3) Controle de elegibilidade: A correção de erros cartográficos permitirá validação automática do requisito legal de área máxima.
B4) Confiabilidade para planejamento: A correção da inflação cadastral permitirá estudos mais acurados sobre distribuição espacial da agricultura familiar.
B5) Credibilidade institucional: Fortalecimento do CAF como fonte oficial de dados geoespaciais.
B6) Segurança jurídica: Redução de falsos positivos em fiscalizações automatizadas.
B7) Governança de dados: Implementação de monitoramento contínuo (dashboards, métricas, metas) criará capacidade de detecção precoce de deteriorações futuras.



 
Apêndice III.C – Matriz de Achados – Achado III
Auditoria de Qualidade de Dados no Sistema de Cadastro da Agricultura Familiar (CAF)	Matriz de Achados
TC 011.073/2025-0
OBJETIVO: identificar inconsistências e fragilidades nos dados que possam comprometer a execução das políticas públicas da área ambiental e da agricultura familiar	
Problema identificado:
A auditoria encontrou falhas sistêmicas de plausibilidade e consistência no CAF: 12.820 CPFs com indicação de óbito na base da RFB, dos quais 3.097 confirmados na base do Sisobi, e 138 menores/adolescentes não aptos como responsáveis por Unidade Familiar de Produção Agrária (UFPA). Os dados de contato são praticamente inutilizáveis: 90,62% de e-mails fictícios e 93,7% de CEPs genéricos, dificultando comunicação com cerca de 2,6 milhões de famílias. Também foram identificadas anomalias de renda (até R$ 167 milhões) e empresas urbanas cadastradas como agricultura familiar. As falhas decorrem de processos de coleta permissivos, ausência de curadoria cadastral e integração insuficiente com bases oficiais.
R1) Devido a fragilidades sistêmicas na gestão do ciclo de vida dos dados cadastrais de agricultores familiares, que incluem falhas na entrada de dados (autodeclaração de informações e integração deficiente com outras bases governamentais), poderá ocorrer a consolidação da base de dados do CAF com informações fraudulentas ou incorretas (inverídicas, imprecisas, incompletas, desatualizadas e conflitantes), o que poderá levar à concessão indevida de benefícios e à exclusão de agricultores familiares legítimos do acesso a benefícios, como programas de crédito, assistência técnica e comercialização, impactando a efetividade das políticas de incentivo à agricultura familiar.
R2) Devido a limitações sistêmicas na capacidade de verificação e fiscalização dos dados constantes no CAF, decorrente tanto de falhas nos mecanismos de cruzamento de dados quanto da dificuldade em obter e tratar dados de referência externos de qualidade, poderá ocorrer a permanência, sem detecção, de informações fraudulentas ou incorretas, o que poderá levar a perda de recursos públicos por fraudes e desvios de recursos públicos para beneficiários indevidos, impactando a efetividade das políticas de incentivo à agricultura familiar.
Risco 3: Devido à inexistência de estrutura adequada de governança e gestão de dados, poderá ocorrer a indefinição de normas, padrões, papéis e responsabilidades, o que poderá levar à falta de documentação e orientação clara sobre dados, processos e critérios, impactando a transparência e a tomada de decisões baseadas em dados completos e confiáveis.
Questão de Auditoria:

QST-1: Em que medida os mecanismos de verificação de dados do CAF (versão 3, período: março de 2025 a agosto de 2025) asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio, considerando-se como critérios a Lei 11.326/2006, as Portarias MDA nº 19/2025 e nº 20/2025, a norma ISO/IEC 25012:2008, o framework DAMA-DMBOK v2 e os princípios da Administração Pública?
Subquestão (i): (Capacidade Civil): Quantas Unidades Familiares de Produção Agrária (UFPA) ativas possuem responsáveis com óbito registrado, menores de 16 anos ou com CPFs não localizados na base da Receita Federal?
Subquestão (ii): (Dados de Contato): Qual a taxa de e-mails inválidos e CEPs genéricos cadastrados, e como essa característica se distribui entre pessoas físicas e jurídicas?
Subquestão (iii): (Consistência de Renda)’: Quantos registros de renda apresentam valores extremos manifestamente implausíveis, e qual o impacto nas estatísticas agregadas?
Subquestão (iv): (Natureza Jurídica): Quantas pessoas jurídicas cadastradas possuem CNAEs incompatíveis com as atividades permitidas para agricultura familiar, e quantos agricultores estão vinculados a essas entidades?
Achado III:
Devido ao desenho processual permissivo (Causa raiz 1), ausência/falhas de rotinas estruturadas de curadoria cadastral (Causa raiz 2), ausência/insuficiência de integração sistêmica com bases oficiais (Causa raiz 3) e insuficiência de governança de dados do CAF (Causa raiz 4), ocorreram 15.811 inconsistências de identidade civil (3.097 óbitos confirmados no Sisobi, 89 menores <16 anos, 57 idades negativas, 11.999 divergências de nascimento, 520 CPFs inexistentes), 90,62% de e-mails fictícios em pessoas físicas (75,16% "naopossui@mail.com"), 93,7% de CEPs genéricos, 139 UFs com renda >R$10 milhões (máximo R$167 milhões) e 39 pessoas jurídicas com CNAEs incompatíveis afetando 10.377 agricultores (Situação Encontrada), contrariando Lei nº 11.326/2006, Art. 3º (requisitos de agricultura familiar), Decreto nº 9.064/2017, Art. 1º (CAF como instrumento de identificação), Portaria MDA nº 19/2025, Arts. 5º, 17, 22, 27 (requisitos e vedações), Código Civil, Arts. 3º, 4º, 6º (capacidade civil), ISO/IEC 25012:2008 (Acurácia, Consistência, Completude, Atualidade, Validade) e DAMA-DMBOK v2 (governança de dados) (Critérios), o que levou à comunicação institucional inviabilizada com ~2,6 milhões de famílias, nulidade jurídica de atos praticados em nome de 3.243 cadastros (óbitos, menores, idades impossíveis), ausência de validação de plausibilidade evidenciada por rendas de até R$167 milhões, e insegurança jurídica para 10.377 agricultores vinculados a entidades irregulares (Efeitos), impactando políticas que movimentam bilhões anuais (Pronaf, PAA, PNAE).
Situação Encontrada	Critério	Efeitos e Riscos	Causas	Boas Práticas	Encaminhamentos	Benefícios esperados
S1) O cruzamento censitário com Sisobi e RFB identificou 12.820 CPFs com indicação de óbito na RFB e 3.097 confirmados no Sisobi que permanecem como titulares ativos de Unidades Familiares, com acúmulo temporal de 20,8% (2010-2015), 39,5% (2016-2020) e 39,7% (2021-2025). Caso extremo: responsável falecido em 2011 cuja UF recebeu atualizações em 2023-2024.
S2) Foram identificados 89 menores de 16 anos cadastrados como responsáveis (absolutamente incapazes, Art. 3º CC), incluindo caso de criança de 11 anos como "Chefe de Unidade Familiar"; 49 adolescentes 16-17 anos não emancipados (relativamente incapazes); 57 registros com data de nascimento futura (idades negativas, incluindo anos 2084, 2083, 2082); 11.999 divergências de data de nascimento entre CAF e RFB (41,74% >365 dias, sugerindo cadastros distintos ou erros grosseiros); e 520 CPFs não localizados na RFB.
S3) Dos 6.525.658 e-mails de pessoas físicas analisados, 90,62% são fictícios ou inválidos (5.913.659 registros), sendo 75,16% literalmente "naopossui@mail.com" (4.904.403 registros). Em contraste, 99,70% dos e-mails de pessoas jurídicas são válidos — diferença de 90,32 p.p. que evidencia falha processual, não técnica. 
S4) Dos 3.540.310 CEPs analisados, 93,7% são genéricos (terminam em '-000'), inviabilizando localização precisa. Mesmo entre os CEPs específicos (222.040 registros), 18,9% apresentam inconsistência de UF declarada.
S5) A análise estatística (Método de Tukey) das 3.340.741 UFs ativas identificou 907 Unidades Familiares com renda >R$ 1 milhão, das quais 139 apresentam renda total >R$10 milhões (0,0042%), incluindo valor extremo de R$167,3 milhões — 8.852× superior à mediana de R$18.831. Distorção na média: +2,06%.
S6) O cruzamento dos 9.687 CNPJs cadastrados com a RFB revelou 39 pessoas jurídicas com CNAEs incompatíveis (0,40%): 17 hipermercados, 8 atacadistas, 4 construtoras, 10 outras atividades urbanas. Caso extremo: hipermercado com capital social de R$ 12,5 milhões e 1.847 agricultores vinculados. Os 10.377 agricultores vinculados estão em risco de bloqueio de acesso a políticas públicas (Art. 28 da Portaria MDA 19/2025). 	K1) Lei nº 11.326/2006, Art. 3º: Estabelece os requisitos cumulativos para enquadramento como agricultor familiar (área, mão de obra, renda, gestão).
 K2) Decreto nº 9.064/2017, Art. 1º: Institui o CAF como instrumento oficial de identificação e qualificação dos agricultores familiares.
K3) Portaria MDA nº 19/2025, Arts. 5º, 17, 22, 27: Estabelece requisitos de elegibilidade, vedações e documentação obrigatória.
K4) Código Civil, Arts. 3º, 4º, 6º: Estabelece regras de capacidade civil (menores de 16 anos absolutamente incapazes, falecidos sem personalidade jurídica).
K5) ISO/IEC 25012:2008: Dimensões de qualidade de dados — Acurácia (correção), Consistência (uniformidade), Completude (preenchimento), Atualidade (atualização), Validade (conformidade com domínio).
K6) DAMA-DMBOK v2: Framework de governança de dados, incluindo curadoria, data owners e data stewards.	R1) Impacto na focalização e elegibilidade de políticas públicas: Manutenção de 3.097 responsáveis falecidos como titulares ativos permite que terceiros continuem acessando políticas em nome de pessoas falecidas.
R2) Impacto na comunicação institucional e transparência: A impossibilidade de contato direto com 90,62% dos beneficiários (aproximadamente 2,6 milhões de famílias) através de e-mail válido compromete a eficiência operacional do Estado.
R3) Impacto na integridade regulatória e risco legal de beneficiários: Os 10.377 agricultores vinculados a 39 pessoas jurídicas com CNAEs incompatíveis (hipermercados, construtoras, atacadistas) podem estar em situação de risco de bloqueio de acesso a políticas públicas.
R4) Impacto na capacidade administrativa de remediar inconsistências: A acumulação histórica de 12.820 óbitos distribuídos ao longo dos anos sem detecção ou saneamento demonstra que o sistema operou continuamente sem rotina de limpeza.
R5) Risco de desvio de recursos por fraude facilitada: As fragilidades de qualidade cadastral criam oportunidades para fraude mediante uso de cadastros indevidos.
R6) Risco de questionamento legal de beneficiários legítimos: A manutenção de cadastros de menores de idade (89 registros com < 16 anos, 49 com 16-17 não emancipados) como responsáveis ativos de UFPAs cria nulidade absoluta de qualquer ato administrativo praticado em seu nome.
R7) Risco de exclusão sistêmica de beneficiários por impossibilidade de comunicação: A manutenção de e-mails fictícios como canal de comunicação digital entre o Estado e 2,6 milhões de beneficiários cria risco de que, quando alterações regulatórias ocorrerem, beneficiários não sejam notificados e incorram em automaticamente descumprimento de requisitos atualizados.
R8) Risco de erosão da credibilidade institucional do MDA: A aceitação de um hipermercado com 1.847 agricultores vinculados, construtoras, e atacadistas como parte de um cadastro de "agricultura familiar" pode comprometer a credibilidade do órgão gestor do CAF perante a sociedade civil.
	Causa raiz 1: Desenho processual permissivo. O sistema do CAF aceita dados inválidos porque prioriza o cadastramento e a fluidez operacional em detrimento da qualidade semântica. Valida sintaxe (formato de CPF, presença de "@" no e-mail), mas não verifica conteúdo: aceita "naopossui@mail.com", datas de nascimento no futuro e valores de renda implausíveis.
Causa raiz 2: Ausência/falhas de rotinas estruturadas de curadoria cadastral. O sistema não possui processos periódicos e sistematizados de saneamento de dados ou eles operam com falhas.
 Causa raiz 3: Ausência\Insuficiência de integração sistêmica com bases oficiais. O sistema do CAF operava de forma isolada, sem conexão em tempo real com bases governamentais que permitiriam a validação cruzada automática de dados críticos.
Causa raiz 4: Insuficiência de governança de dados do CAF. Ausência de estrutura formal de governança que assegure a integridade dos ativos de informação, com designação de proprietários e curadores de dados (data owners e data stewards), métricas de qualidade monitoradas e processos de melhoria contínua.	BP1) Contraste PF/PJ na qualidade de e-mails: 99,70% dos e-mails de pessoas jurídicas são válidos, contra apenas 9,38% de pessoas físicas (diferença de 90,32 p.p.), demonstrando que o problema não é técnico, mas processual. Para pessoas jurídicas, o e-mail é ferramenta operacional indispensável, criando incentivo natural para correção. 
BP2) O CAF 3.0 possui integração com bases da RFB e com o CNIS, demonstrando avanços na interoperabilidade. 
BP3) A metodologia de cruzamento triplo (CAF × RFB × Sisobi) adotada nesta auditoria demonstra boa prática para mitigação de falsos positivos na identificação de óbitos.	D1) Determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação que contemple ações, responsáveis e prazos, para avaliar as falhas apontadas no relatório de auditoria que resultam em problemas de qualidade dos dados do CAF, e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial: impropriedades de capacidade civil e legitimidade dos responsáveis; dados de contato fictícios; inconsistências de dados de renda; inconsistências de natureza jurídica de pessoas jurídicas cadastradas.
E1) Recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução TCU 315/2020, que: revise e aperfeiçoe os processos de cadastramento e atualização dos dados do CAF e implemente medidas de prevenção à inserção/permanência de dados cadastrais inválidos, incluindo: impedimento de preenchimentos fictícios institucionalizados (ex: e-mail padrão); validações semânticas e de plausibilidade em campos críticos (identidade civil, datas, renda e contato); interoperabilidade/verificação automatizada com bases oficiais (CPF, CNAE, CEP, óbitos); desenvolva e implemente mecanismos de acompanhamento gerencial contínuo da qualidade cadastral, com métricas que permitam identificar e priorizar correções e avaliar a efetividade das medidas adotadas.	Quantificáveis:
B1) Integridade cadastral restaurada: Correção dos 15.811 registros com inconsistências de capacidade civil (3.097 óbitos, 138 menores/adolescentes incapazes).
B2) Comunicação institucional facilitada: Saneamento de 5,9 milhões de e-mails fictícios, viabilizando canal direto com beneficiários.
B3) Redução do risco de desconformidade regulatória: Correção das 39 entidades com CNAEs incompatíveis, protegendo 10.377 agricultores vinculados. 
Qualitativos:
B4) Validação de plausibilidade de renda implementada, evitando distorções estatísticas. 
B5) Detecção proativa de inconsistências através de monitoramento contínuo.
B6) Melhoria na governança de dados do CAF com estabelecimento de métricas e responsabilidades claras.


 
Apêndice III.D – Matriz de Achados – Achado IV
Auditoria de Qualidade de Dados no Sistema de Cadastro da Agricultura Familiar (CAF)	Matriz de Achados
TC 011.073/2025-0
OBJETIVO: identificar inconsistências e fragilidades nos dados que possam comprometer a execução das políticas públicas da área ambiental e da agricultura familiar	
Problema identificado:
O dicionário de dados do Sistema CAF — artefato que funciona como a "bula" do sistema, explicando o significado de cada campo e tabela — apresenta deficiências críticas em três das quatro dimensões avaliadas: 94,1% das descrições existentes são semanticamente inadequadas, limitando-se a repetir o nome técnico do campo (exemplo: "dt_criacao" descrito como "Data criação"); 84,0% dos campos numéricos não especificam unidade de medida (exemplo: o campo "nr_area" não informa se a área está em hectares, metros quadrados ou outra unidade); e 92,0% dos campos temporais são ambíguos (exemplo: não distingue se uma "data de criação" refere-se ao registro no sistema ou à inscrição do agricultor). Essas falhas tornam o uso dos dados dependente do conhecimento tácito de poucos desenvolvedores — conhecimento que pode se perder com a rotatividade de pessoal — e constituem uma causa estrutural que amplifica os problemas identificados nos Achados I, II e III.
R1) Devido a fragilidades sistêmicas na gestão do ciclo de vida dos dados cadastrais de agricultores familiares, que incluem falhas na entrada de dados (autodeclaração de informações e integração deficiente com outras bases governamentais), poderá ocorrer a consolidação da base de dados do CAF com informações fraudulentas ou incorretas (inverídicas, imprecisas, incompletas, desatualizadas e conflitantes), o que poderá levar à concessão indevida de benefícios e à exclusão de agricultores familiares legítimos do acesso a benefícios, como programas de crédito, assistência técnica e comercialização, impactando a efetividade das políticas de incentivo à agricultura familiar.
R2) Devido a limitações sistêmicas na capacidade de verificação e fiscalização dos dados constantes no CAF, decorrente tanto de falhas nos mecanismos de cruzamento de dados quanto da dificuldade em obter e tratar dados de referência externos de qualidade, poderá ocorrer a permanência, sem detecção, de informações fraudulentas ou incorretas, o que poderá levar a perda de recursos públicos por fraudes e desvios de recursos públicos para beneficiários indevidos, impactando a efetividade das políticas de incentivo à agricultura familiar.
Risco 3: Devido à inexistência de estrutura adequada de governança e gestão de dados, poderá ocorrer a indefinição de normas, padrões, papéis e responsabilidades, o que poderá levar à falta de documentação e orientação clara sobre dados, processos e critérios, impactando a transparência e a tomada de decisões baseadas em dados completos e confiáveis.
Questão de Auditoria:
QST-2: Em que medida a estrutura de governança e gestão de dados aplicada ao CAF assegura padrões claros, papéis definidos, rastreabilidade e integridade das informações ao longo de todo o ciclo de vida dos dados, considerando-se os critérios do Decreto nº 10.046/2019, da norma ISO/IEC 11179:2015, do COBIT 2019 e do DAMA-DMBOK v2?
 Subquestão (i) (Cobertura): O dicionário possui cobertura completa de todas as tabelas existentes no banco de dados de produção?
Subquestão (ii) (Qualidade Semântica): As descrições dos campos fornecem significado de negócio compreensível, ou são meramente tautológicas — limitando-se a repetir o nome do campo em outras palavras?
Subquestão (iii) (Unidades de Medida): Os campos numéricos possuem unidades de medida definidas, de modo que se saiba se uma área está expressa em hectares, metros quadrados ou outra unidade?
Subquestão (iv) (Semântica Temporal): Os campos temporais têm semântica clara, distinguindo se uma "data de criação" refere-se ao momento em que o registro foi inserido no banco de dados ou à data em que o agricultor efetivamente se inscreveu no sistema?
Achado IV:
Devido à ausência de processo de gestão de metadados (Causa raiz 1), ausência de cultura de "Data Literacy" (Causa raiz 2), documentação "post-mortem" e fragmentada (Causa contributiva 1), ausência de ferramentas adequadas (Causa contributiva 2), legado histórico sem revisão (Causa contributiva 3) e falta de integração entre equipes técnicas e de negócio (Causa contributiva 4), ocorreram 94,1% de descrições semanticamente inadequadas (496/527 campos: 56,2% tautológicas, 34,3% genéricas, 3,6% técnicas), 84,0% de campos numéricos sem unidade de medida (105/125 campos, incluindo campos críticos como nr_area e vl_renda_estimada), 92,0% de campos temporais ambíguos (80/87 campos, não distinguindo eventos de sistema de eventos de negócio) (Situação Encontrada), contrariando ISO/IEC 11179:2015 (descrições devem explicar significado de negócio), ISO/IEC 25012:2008 (Completude, Compreensibilidade, Rastreabilidade), DAMA-DMBOK v2 (dicionário como artefato central de governança), COBIT 2019 BAI08 (mitigar dependência de conhecimento tácito), LAI Lei 12.527/2011 (informação em linguagem de fácil compreensão) e Decreto 10.046/2019 (governança de dados na APF) (Critérios), o que levou a dificuldade de compreensão, risco de erros em integrações e análises (fator 10.000× se confundir hectares com m²), dependência crítica dos "Gurus do Sistema", dificuldade de manutenção evolutiva, impossibilidade de automatização analítica, e dificuldade de auditoria e controle social (Efeitos), impactando a capacidade de verificação independente de um sistema que sustenta políticas públicas para milhões de unidades familiares.
Situação Encontrada	Critério	Efeitos e Riscos	Causas	Boas Práticas	Encaminhamentos	Benefícios esperados
S1) Cobertura (Positivo): Todas as 95 tabelas em uso estão documentadas no dicionário de dados (100% de cobertura). A análise inicial identificou aparente divergência (109 tabelas no schema vs 94 no dicionário). O MDA esclareceu (Ofício nº 76/2025) que as tabelas restantes eram estruturas de migração já removidas.
S2) Qualidade Semântica: Dos 527 campos documentados, 496 (94,1%) possuem descrições semanticamente inadequadas: 296 (56,2%) tautológicas (ex: dt_criacao → "Data criação"), 181 (34,3%) genéricas (ex: nr_area → "Tamanho da área imóvel" sem unidade), 19 (3,6%) técnicas. Apenas 31 campos (5,9%) são funcionalmente adequados. Padrão recorrente: "ID de identificação" — pleonasmo em dezenas de campos.
S3) Unidades de Medida: Dos 125 campos numéricos, 105 (84,0%) não especificam unidade de medida. Campos críticos afetados: nr_area (hectares? m²? alqueires?), vl_renda_estimada (R$? salários-mínimos?), nr_modulo_fiscal (hectares? quantidade?). O Decreto 9.064/2017 define "módulo fiscal expresso em hectares" — informação omitida no dicionário.
S4) Semântica Temporal: Dos 87 campos temporais, 80 (92,0%) apresentam ambiguidade semântica. A tabela S_UNIDADE_FAMILIAR possui 8 campos de data sem distinção clara: dt_criacao, dt_atualizacao, dt_ativacao, dt_primeira_ativacao, dt_exclusao, dt_inativacao, dt_fim_vigencia, dt_obito_solicitante. O campo dt_fim_vigencia não menciona o prazo de 3 anos (5 anos na região Norte) estabelecido no art. 19 da Portaria MDA 19/2025.	K1) ISO/IEC 11179:2015 (Registros de Metadados): Descrições devem fornecer significado de negócio, não apenas traduzir nomenclaturas técnicas — princípio violado em 94,1% dos campos.
 K2) ISO/IEC 25012:2008 (Qualidade de Dados): Requisitos de Completude (unidades de medida), Compreensibilidade (descrições funcionais) e Rastreabilidade (semântica temporal clara).
K3) DAMA-DMBOK v2: O dicionário de dados é artefato central de governança, deve fornecer semântica de negócio compreensível e ser mantido atualizado.
K4) COBIT 2019 BAI08 (Gestão do Conhecimento): Gestão do conhecimento organizacional deve mitigar dependência de conhecimento tácito individual.
K5) Lei 12.527/2011 (LAI): Informação deve ser disponibilizada em linguagem de fácil compreensão.
K6) Decreto 10.046/2019: Estabelece diretrizes de governança pública de dados na APF, incluindo integridade, rastreabilidade e transparência. 	E1) Dificuldade de compreensão: A deficiência mais imediata é a impossibilidade de compreender plenamente o significado das informações de forma autônoma, sem consultar desenvolvedores experientes.
R1) Risco de erros em integrações e análises: Sistemas externos que consomem dados do CAF dependem de interpretação correta dos campos. Quando 84% dos campos numéricos não especificam unidade de medida e 92% dos campos temporais são ambíguos, o risco de mapeamentos incorretos é substancial. Exemplo: interpretar hectares como metros quadrados resulta em erro de fator 10.000×.
R2) Dependência crítica dos "Gurus do Sistema": Com 94,1% das descrições inadequadas, o conhecimento sobre o significado real dos campos está concentrado em poucos indivíduos. Se essas pessoas-chave deixarem a organização, o conhecimento institucional corre o risco de se perder.
R3) Dificuldade de manutenção evolutiva. 
R4) Impossibilidade de automatização analítica com ferramentas modernas de Business Intelligence.


Comprometimento da rastreabilidade: auditores não conseguem validar estrutura de dados sem explicações verbais de desenvolvedores — verificação independente impossibilitada.
F2) Risco de erros em integrações: interpretar `nr_area` como m² quando está em hectares resulta em erro de fator 10.000× — suficiente para distorcer estatísticas sobre estrutura fundiária.
F3) Dependência crítica dos "Gurus do Sistema": conhecimento concentrado em poucos indivíduos ("bus factor" baixo), vulnerável à rotatividade de pessoal no serviço público.
F4) Dificuldade de manutenção evolutiva: novos desenvolvedores enfrentam curva de aprendizado artificialmente íngreme, necessitando engenharia reversa do código-fonte.
F5) Impossibilidade de automatização analítica: ferramentas de BI dependem de metadados de qualidade; dicionário inadequado bloqueia escalabilidade e dashboards gerenciais.
F6) Dificuldade de auditoria e controle social: auditorias consomem tempo excessivo em compreensão básica; dados públicos, mas incompreensíveis — transparência formal sem transparência real.
R1) Risco de perda de conhecimento institucional por aposentadoria ou transferência dos "gurus do sistema".
R2) Risco de decisões de políticas públicas baseadas em dados incorretamente interpretados.
R3) Risco de integração incorreta com sistemas externos (PRONAF, PAA, PNAE, IBGE).	Causa raiz 1: Ausência de processo de gestão de metadados. O CAF não possui documento formal que estabeleça padrões de documentação, responsabilidades e processos de controle de qualidade para metadados. Não há definição explícita de quem é responsável pela manutenção do dicionário, quais critérios uma descrição deve atender, nem fluxo de aprovação para inclusão de novas tabelas ou campos. 
Causa raiz 2: Ausência de cultura de "Data Literacy". A governança de dados não foi tratada como prioridade institucional. Documentação de metadados é frequentemente vista como "custo" e não como "investimento". 
Causa contributiva 1: Documentação "post-mortem" e fragmentada. A documentação foi elaborada após o desenvolvimento do sistema, não durante. 
Causa contributiva 2: Ausência de ferramentas adequadas. O dicionário é mantido em formato CSV/Excel, artefato estático sem integração automatizada com o banco de dados. 
Causa contributiva 3: Legado histórico sem revisão. O sistema evoluiu através de múltiplas versões (CAF 1.0, 2.0, 3.0) e gerações de desenvolvedores, acumulando "dívida técnica documental". 
Causa contributiva 4: Falta de integração entre equipes. O conhecimento técnico dos desenvolvedores e o conhecimento funcional dos analistas de negócio permanecem isolados em silos.	BP1) O Sistema CAF possui dicionário de dados documentado com 100% das 95 tabelas em uso — situação positiva que demonstra que a infraestrutura básica de documentação existe e pode ser aproveitada para melhorias.
BP2) O Documento de Regras de Negócio (CAF_DRN, peça 78) contém definições semânticas relevantes (ex: RN1.19 especifica unidades de aquicultura), demonstrando que o conhecimento de negócio existe na organização, embora não integrado ao dicionário formal.
	D1) Determinar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 6º, § 3º, I, da Resolução TCU 315/2020, que, no prazo de noventa dias, elabore plano de ação que contemple ações, responsáveis e prazos, para avaliar as falhas apontadas no relatório de auditoria que resultam em problemas de qualidade dos dados do CAF, e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, em especial: deficiências de qualidade do dicionário de dados, incluindo descrições semanticamente inadequadas ou ambíguas e ausência de especificação de unidades de medida nas descrições dos campos numéricos.
 E1) Recomendar ao Ministério do Desenvolvimento Agrário e Agricultura Familiar, nos termos do art. 11 da Resolução TCU 315/2020, que: aperfeiçoe o processo institucional de gestão de metadados do CAF, incluindo a incorporação de definições semânticas no dicionário de dados com base nas regras de negócio do sistema e no marco legal aplicável, com definição de papéis e responsabilidades (data owners e data stewards), padrões mínimos de documentação e revisão contínua integrada ao ciclo de desenvolvimento e implantação do sistema, de modo a reduzir ambiguidades interpretativas e fragmentação documental, em consonância com as boas práticas da ISO/IEC 11179:2015, do DAMA-DMBOK v2 e do COBIT 2019 (BAI08, Gestão do Conhecimento).	Quantificáveis:
B1) Rastreabilidade auditável: Auditores poderão validar estrutura de dados sem depender de explicações verbais. 
B2) Redução de erros: Menor risco de interpretações incorretas em integrações e análises (mitigação do risco de fator 10.000× na confusão de unidades). 
Qualitativos:
B3) Preservação do conhecimento: Informações sobre o sistema deixarão de estar concentradas em poucos indivíduos.
B4) Facilitação de integrações: Sistemas externos poderão consumir dados do CAF com segurança semântica.
B5) Independência operacional: Análises e relatórios não dependerão dos "gurus do sistema" para interpretação.
B6) Possibilidade de automatização analítica: Ferramentas modernas de Business Intelligence poderão ser plenamente aproveitadas.


Apêndice IV – Matriz de Planejamento 
EQUIPE: 
Fernando Lima Gama Júnior (AUFC 6499-8)
Sylvio Xavier Júnior (AUFC 2423-6)
Kalenus Pires da Nóbrega (AUFC 10662-3)	SUPERVISOR:
Harley Alves Ferreira (AUFC 5666-9)  

QUESTÃO DE AUDITORIA 01 (QST-01): Os mecanismos de verificação de dados do CAF (versão 3, período: março de 2025 a agosto de 2025) asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio?
QUESTÃO DE AUDITORIA 02 (QST-02):  A estrutura de governança e gestão de dados aplicada ao CAF assegura padrões claros, papéis definidos, rastreabilidade e integridade das informações ao longo de todo o ciclo de vida dos dados?
RIS-01) Devido a fragilidades sistêmicas na gestão do ciclo de vida dos dados cadastrais de agricultores familiares, que incluem falhas  na entrada de dados (devido a autodeclaração de informações e integração deficiente com outras bases governamentais), poderá ocorrer a consolidação da base de dados do CAF com informações fraudulentas ou incorretas (inverídicas, imprecisas, incompletas, desatualizadas e conflitantes), o que poderá levar à concessão indevida de benefícios e à exclusão de agricultores familiares legítimos do acesso a benefícios, como programas de crédito, assistência técnica e comercialização, impactando a efetividade das políticas de incentivo à agricultura familiar.
RIS-02) Devido a limitações sistêmicas na capacidade de verificação e fiscalização dos dados constantes no CAF, decorrente tanto de falhas nos mecanismos de cruzamento de dados (a ferramenta) quanto da dificuldade em obter e tratar dados de referência externos de qualidade (a matéria-prima) poderá ocorrer a permanência sem detecção de informações fraudulentas ou incorretas, o que poderá levar a perda de recursos públicos por fraudes e desvios de recursos públicos para beneficiários indevidos, impactando efetividade das políticas de incentivo à agricultura familiar.
RIS-03) Devido à inexistência de estrutura adequada de governança e gestão de dados, poderá ocorrer a indefinição de normas, padrões, papéis e responsabilidades, o que poderá levar a falta de documentação e orientação clara sobre dados, processos e critérios, impactando a transparência e a tomada de decisões baseadas em dados (completos e confiáveis).
INFORMAÇÕES REQUERIDAS	FONTES DE INFORMAÇÃO	CRITÉRIOS	DETALHAMENTO DOS PROCEDIMENTOS	POSSÍVEIS EVIDÊNCIAS	POSSÍVEIS ACHADOS
1) Para Procedimento 1.1 
- Declarações de tamanho de propriedade
- Informações sobre gestão familiar declaradas
- Dados de atividade econômica predominante
- Requisitos da agricultura familiar
2) Para Procedimento 1.2 
- Documentos comprobatórios enviados pelos CAFiados
3) Para Procedimento 1.3 
- Precisão das coordenadas informadas
4) Para Procedimento 2.1 
- Lista de campos obrigatórios do CAF
5) Para Procedimento 2.2 
- Lista de atributos críticos do CAF
6) Para Procedimento 2.3 
- Precisão das coordenadas informadas
- Listas de proprietários rurais e de agricultores familiares
7) Para Procedimento 2.4 
- Data da última atualização dos registros CAF
- Informações pessoais e econômicas dos proprietários rurais e dos agricultores familiares
8) Para Procedimento 2.5 
- Coordenadas geográficas das propriedades rurais
- Informações pessoais e econômicas dos proprietários rurais e dos agricultores familiares
9) Para Procedimento 2.6 
- Coordenadas geográficas das propriedades rurais
- Informações sobre a produção das unidades de agricultura familiar
10) Para Procedimento 2.7 
- Metadados de origem dos registros 
- Informações sobre quem declarou e quando
- Métodos de coleta/entrada de dados utilizados
11) Para Procedimento 2.8
- Dados históricos (logs) de alterações (o que foi alterado, quem alterou, quando foi alterado)
12) Para Procedimento 3.1
- Dados sobre pessoas falecidas
- Dados sobre detentores de mandatos eletivos e cargos públicos
- Dados sobre empresas e sócios
- Dados sobre propriedade de bens de alto valor (veículos, por exemplo)
13) Para Procedimento 3.2
- Coordenadas dos imóveis (CAF)
- Dado georreferenciados dos imóveis (CAR)
14) Para Procedimento 4 
- Normativos internos sobre governança e gestão de dados
- Definições de papeis e responsabilidades
	1) Para Procedimento 1.1:
- Base de dados do CAF
- Lei nº 11.326/2006
- Decreto nº 10.046/2019
- Portaria MDA nº 19, de 21 de março de 2025
2) Para Procedimento 1.2:
- Arquivos de documentos enviados pelos CAFiados por meio do Sistema CAF versão 3
3) Para Procedimento 1.3:
- Base de dados do CAF
- Manuais do CAF
- Especificações técnicas, metadados e dicionário de dados do CAF
4) Para Procedimento 2.1, 2.2, 2.3, 2.4, 2.5 e 2.6:
- Base de dados do CAF 
- Manuais do CAF
- Especificações técnicas, metadados e dicionário de dados do CAF
5) Para Procedimento 2.7 e 2.8:
- Base de dados do CAF 
- Manuais do CAF
- Especificações técnicas, metadados e dicionário de dados do CAF
- Logs de auditoria do CAF
6) Para Procedimento 3.1:
- Bases de dados do LabContas
7) Para Procedimento 3.2:
- Base de dados do CAR
8) Para Procedimento 4:
- Documentos normativos do MDA
- Atas de entrevistas com gestores	1) Leis e normativos sobre a agricultura familiar e o CAF:
- Lei nº 11.326/2006 (Lei da Agricultura Familiar)
- Decreto nº 10.046/2019
- Portaria MDA nº 19, de 21 de março de 2025
- Portaria MDA nº 20, de 21 de março de 2025
2) Dimensões de Qualidade de Dados (DAMA-DMBOK2)
3) Critérios Técnicos (ISO/IEC 25012:2008)
4) Decreto nº 10.046/2019 (Governança de Dados)
5) Eventuais acórdãos do TCU sobre Qualidade de Dados
6) Princípios da Administração Pública (Art. 37, CF/88)



	Regras de negócio
1.1) Verificar critérios como tamanho do módulo fiscal, gestão familiar e atividade econômica predominante.
1.2) Verificar a adequabilidade da documentação comprobatória enviada pelos CAFiados.
1.3) Identificar consistência das coordenadas geográficas exigidas.
Data profiling
2.1) Verificar se todos os campos obrigatórios estão preenchidos (ex.: coordenadas geográficas e declaração de renda).
2.2) Identificar ausência de valores nulos ou em branco em atributos críticos.
2.3) Verificar ausência de registros duplicados (ex.: sobreposição de imóveis e CPFs repetidos).
Dados atualizados
2.4) Verificar se os dados estão atualizados:
2.4.1) conforme prazos legais (ex.: atualização anual do CAF).
2.4.2) conforme “background services”, como eventos externos modificadores de dados da base (ex.: falecimento e mudança de condição social/renda)
Domínios dos dados
2.5) Verificar a conformidade com formatos e domínios definidos (ex.: coordenadas geográficas válidas e CNPJ/CPF válidos).
2.6) Verificar se os dados são corretos e próximos da realidade (ex.: declaração fidedigna de produção e coordenadas geográficas do imóvel rural).
2.6.1) Comparação das coordenadas geográficas informadas com os demais dados informados (ex. endereço da área rural)
2.6.2) Comparação de produção declarada no CAF com dados oficiais
Logs/rastreabilidade
2.7) Verificar a rastreabilidade da origem dos dados (ex.: quem declarou, quando e com qual método de coleta).
2.8) Verificar a rastreabilidade de alterações de dados (o que foi alterado, quem alterou, quando foi alterado)
Cruzamentos de dados
3.1) Verificar se não há:
- Titulares falecidos
- Agricultores com alta renda
- Agricultores que exercem atividades não agrícolas
3.2) Verificar se as propriedades rurais estão registradas no CAR
Normas e processos de governança de dados
4.1) Análise documental 
4.2) Entrevistas com gestores
4.3) Requisições de informações
Investigação de causas e efeitos dos achados
5.1. Entrevistas com gestores e usuários do sistema (da rede de emissores) e gestores de políticas públicas
5.2. Requisições de informações
- Investigar sobre causas como: baixa qualidade dos dados migrados de versões anteriores do sistema; deficiências nos controles de entrada de dados; inexistência de acompanhamento/monitoramento o uso do sistema e da qualidade de dados do CAF;
- Investir sobre efeitos como: impedimento/dificuldade/demora para concluir o cadastro devido problemas com o sistema (lentidão, instabilidade); impedimento demora para concluir o cadastro devido à exigência de anexar documentação comprobatória; impedimento/negativa de acesso a políticas devido problemas de qualidade dos dados do CAF.	1) Relatórios de data profiling detalhando campos inconsistentes e incompletos
1.1) Resultados de testes de requisitos básicos de qualidade de dados
- Registros com campos/atributos obrigatórios/críticos em branco ou nulos ou incompletos
- Imóveis rurais em duplicidade
- Números de CPF em duplicidade
- Dados em desconformidade com formatos definidos

2) Resultados de análises e cruzamentos de dados (frente à legislação e regras de negócio)
- Documentos comprobatórios inadequados (Gabichecks)
- Rendas (declaradas) superiores ao limite estabelecido
- Titulares com renda alta (detentores de mandato eletivo/cargo público, empresário não agrícola, proprietários de veículo de alto valor etc.)
- Cônjuges com propriedades distintas
- Áreas superiores a 4 módulos fiscais
- Conflitos identificados por meio de cruzamentos com o CAR
- Conflitos identificados por meio de cruzamentos com outras bases de dados
- Titulares falecidos
3) Cópias de telas do sistema
4) Normas de gestão e uso do sistema
5) Documentação do sistema
6) Documentação da base de dados
7) Normas de governança e gestão de dados
8) Mecanismos de enforcement de normas de governança e gestão de dados	1) Os mecanismos de verificação de dados do CAF não asseguram o pleno atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio.
1.1) O não atendimento pleno das regras de negócio impactam a finalidade de o CAF ser um instrumento para prover a concessão de benefícios e incentivos à agricultura familiar.
2) O CAF apresenta fragilidades sistêmicas na entrada de dados devido à natureza autodeclaratória de algumas informações e deficiências na integração com outras bases governamentais de referência.
3) Capacidade limitada/incapacidade de verificação e fiscalização (“background services”) dos dados constantes no CAF.
4) A base de dados do CAF consolida informações imprecisas, desatualizadas e conflitantes, resultando em um retrato da agricultura familiar de baixa fidedignidade.
5) A descentralização da coleta de dados do CAF pela rede de emissores ocorre sem uma governança central robusta e atuante, comprometendo a padronização dos procedimentos e a qualidade dos dados na origem.
6) Ausência de políticas e/ou enforcement de normas de governança e gestão de dados para promover a qualidades de dados na base de dados do CAF.

 
Apêndice V – Metodologia Estatística da Análise Documental
1.	Objetivo e Escopo 
1.	Este apêndice detalha a fundamentação estatística e os procedimentos metodológicos aplicados na análise documental dos Achados I, II e III.
2.	Desenho Amostral – Achado I: Inadequações da Documentação Comprobatória
2.	Foram realizados dois procedimentos amostrais distintos, dependendo da complexidade do atributo analisado:
2.1.	Análise de Adequação Semântica (Tipo de Documento)
3.	Avaliou se o documento digitalizado corresponde ao tipo declarado (via IA Generativa + Revisão de Auditor), por exemplo: se um arquivo classificado como "Comprovação de Área" é de fato uma matrícula ou contrato).
*   População (N): 11.377.318 documentos (universo total do CAF em 02/09/2025).
*   Amostra (n): 646 documentos.
*   Nível de Confiança: 99%.
*   Margem de Erro: ±4,5,00%.
*   Resultado: 27,1% de inadequação.
2.2.	Análise de Acurácia de Área (Divergência de Hectares)
4.	Avaliou a discrepância entre a área extraída do documento (via IA Generativa + Revisão de Auditor) e a área registrada no banco de dados do CAF
*   População Estimada (N): 2.620.000 documentos (propriedades com área identificável).
*   Amostra (n): 155 documentos.
*   Nível de Confiança: 95%.
*   Margem de Erro: ±6,44%.
*   Resultado: 53,55% de divergências críticas (superior a 10%).
2.3.	Justificativa da Margem de Erro (6,44%)
5.	O Plano de Auditoria previa inicialmente uma margem de erro de 5% para todos os testes. Entretanto, a análise de acurácia de área revelou-se um procedimento de alta densidade técnica, exigindo o uso de Computer Vision (Claude-3-Vision) seguido de revisão especializada por auditores para garantir que a IA não tivesse interpretado erroneamente frações ideais ou unidades de medida.
6.	A decisão de limitar a amostra a 155 itens (aceitando uma margem de ±6,44%) fundamenta-se nos seguintes critérios:
6.1.	 Magnitude do Erro: Como a proporção de divergências encontrada foi muito elevada (53,55%), o Intervalo de Confiança (47,11% a 59,99%) permanece inteiramente em patamares alarmantes, confirmando a falha estrutural de controle sem a necessidade de ampliar a amostra.
6.2.	 Princípio da Economicidade e Tempestividade: O custo operacional de triplicar a amostra para atingir 5% de erro seria desproporcional ao ganho de precisão, visto que a tese de "insegurança dos dados de área" já está plenamente comprovada estatisticamente.
2.4.	Procedimentos de Validação
7.	Os documentos foram selecionados via Amostragem Aleatória Simples estratificada por Unidade da Federação. A extração de dados utilizou um pipeline de processamento:
7.1.	Pré-processamento: Conversão de PDF para imagem de alta resolução.
7.2.	Extração (OCR/Vision): Identificação da área total do imóvel citada no documento.
7.3.	Filtragem de Confiança: Casos onde a IA classificou a imagem como "ilegível" foram mantidos no cômputo de "Baixa Qualidade", mas excluídos do cálculo de acurácia de área para não distorcer o percentual de divergência intencional.
7.4.	Revisão Cruzada: Auditoria manual de 10% da amostra para validar o comportamento da ferramenta de extração.
3.	Metodologia Geoespacial — Achado II: Qualidade Cartográfica e Integridade
3.1.	Métrica de Distância: Fórmula Haversine
8.	Para a análise de duplicações espaciais (PT-08), adotou-se a distância Haversine como métrica padrão. Diferentemente da distância Euclidiana (que assume um plano 2D e gera distorções em coordenadas geográficas), a fórmula Haversine calcula a distância geodésica entre dois pontos na superfície de uma esfera, considerando a curvatura da Terra.
Fórmula Matemática:
 
Onde:
*   d: distância entre os dois pontos (em metros)
*   r: raio da Terra (adotado r = 6.371.000 metros)
*   φ₁, φ₂: latitude dos pontos 1 e 2 (em radianos)
*   λ₁, λ₂: longitude dos pontos 1 e 2 (em radianos)
3.2.	Implementação Computacional (PostGIS)
9.	A validação foi implementada em banco de dados PostgreSQL com extensão PostGIS. Utilizou-se a função nativa `ST_Distance_Sphere`, que aplica a geometria esférica para cálculos de alta performance em grandes volumes de dados.
3.2.1.	Algoritmo de Detecção de Duplicatas (Self-Join Espacial):
10.	A detecção de duplicatas foi realizada mediante self-join da tabela de registros validados, comparando cada ponto com todos os outros pontos da base. Para otimização computacional, aplicou-se índice espacial (GIST) e restrição triangular (`a.id < b.id`).
-- Exemplo do algoritmo de detecção de duplicatas (PT-08)
SELECT 
    a.id_registro AS id_a,
    b.id_registro AS id_b,
    ST_Distance_Sphere(a.geom, b.geom) AS distancia_metros
FROM caf_imoveis_validos a
JOIN caf_imoveis_validos b 
    ON ST_DWithin(a.geom, b.geom, 10) -- Filtro de pré-seleção (box)
WHERE 
    a.id_registro < b.id_registro -- Evita duplicidade simétrica
    AND ST_Distance_Sphere(a.geom, b.geom) < 10;
3.3.	Critérios de Classificação Espacial
11.	Com base na distância calculada (d), os registros foram classificados em três categorias de integridade:
11.1.	Duplicata Exata (d = 0): Coordenadas rigorosamente idênticas. Indica erro de sistema ou duplicidade de cadastro sem variação.
11.2.	Duplicata Próxima (0 < d < 10m): Pontos distintos, mas dentro da margem de precisão de GPS comum (10m). Considerados funcionalmente o mesmo local para fins de auditoria.
11.3.	Cluster Denso: Agrupamento de 3 ou mais pontos em um raio de 100m. Indica possível assentamento ou erro sistemático de "ponto viciado" (proxy).
4.	Metodologia de Extração de Dados — Achado III: Qualidade Cadastral
12.	A população canônica de 2.905.101 responsáveis atuais por unidades familiares ativas (peça 124, p. 8) foi obtida mediante consulta estruturada que encadeia as tabelas S_RESPONSAVEL_UFPR, S_UNIDADE_FAMILIAR, S_UNIDADE_FAMILIAR_PESSOA e S_PESSOA_FISICA (peça 75), aplicando filtros que consideram apenas: (i) unidades familiares efetivamente ativas, determinadas pela lógica de precedência entre datas de ativação e inativação; e (ii) responsáveis sem data de saída registrada:
Quadro 1. Query SQL para obtenção da população canônica de responsáveis ativos
SELECT COUNT(DISTINCT pf.nr_cpf)
FROM S_RESPONSAVEL_UFPR resp
INNER JOIN S_UNIDADE_FAMILIAR uf
    ON resp.id_unidade_familiar = uf.id_unidade_familiar
INNER JOIN S_UNIDADE_FAMILIAR_PESSOA ufp
    ON resp.id_ufpr_pessoa_responsavel = ufp.id_unidade_familiar_pessoa
INNER JOIN S_PESSOA_FISICA pf
    ON ufp.id_pessoa_fisica = pf.id_pessoa_fisica
WHERE
    CASE
        WHEN uf.dt_ativacao IS NULL THEN 'INATIVA'
        WHEN uf.dt_inativacao IS NULL THEN 'ATIVA'
        WHEN DATE(uf.dt_inativacao) < DATE(uf.dt_ativacao) THEN 'ATIVA'
        WHEN DATE(uf.dt_inativacao) = DATE(uf.dt_ativacao)
             AND uf.dt_inativacao < uf.dt_ativacao THEN 'ATIVA'
        ELSE 'INATIVA'
    END = 'ATIVA'
AND resp.dt_saida IS NULL;
5.	Método de Tukey para Detecção de Outliers de Renda — Achado III: Qualidade Cadastral 
13.	Para a análise de consistência dos dados de renda (PT-03), adotou-se o Método de Tukey (ou Boxplot Method), técnica estatística não-paramétrica recomendada pelo TCU para identificação de valores atípicos em distribuições assimétricas, comuns em dados socioeconômicos.
5.1.	Fundamentação Estatística
14.	Diferentemente de métodos baseados em desvios-padrão (que pressupõem distribuição normal), o método de Tukey fundamenta-se na dispersão por quartis, sendo resiliente a outliers extremos que poderiam distorcer a média.
Cálculo dos Limites:
14.1.	Amplitude Interquartil (IQR): Diferença entre o terceiro quartil (Q_3) e o primeiro quartil (Q_1).
    IQR = Q_3 - Q_1 
14.2.	Limite Superior (Upper Fence):
    UF = Q_3 + k(IQR) 
    *   Para detecção de outliers moderados, adota-se k = 1,5.
    *   Para detecção de outliers extremos (utilizados para evidenciar falha de crítica no CAF), adota-se k = 3,0.
5.2.	Aplicação no Achado III
15.	A análise de 3,3 milhões de UFPAs utilizou o limiar de k=3,0 para identificar registros manifestamente implausíveis. Valores acima desse limiar (calculado em R$ 108.027 para a base de 2025) foram confrontados com a realidade econômica da agricultura familiar e com o limite legal do Pronaf (R$ 500.000), servindo como evidência de ausência de travas de integridade no sistema.




 
Apêndice VI – Glossário
Este glossário apresenta definições dos termos técnicos utilizados no relatório de auditoria, organizados em cinco categorias temáticas. As definições foram contextualizadas ao Sistema CAF e às políticas públicas de agricultura familiar.
1.	AGRICULTURA FAMILIAR
Conceitos Fundamentais
Agricultor Familiar	Pessoa que pratica atividades no meio rural, atendendo simultaneamente aos requisitos cumulativos estabelecidos na Lei 11.326/2006, Art. 3º (i) não deter área maior que 4 módulos fiscais; (ii) utilizar predominantemente mão de obra da própria família; (iii) ter percentual mínimo de renda originada de atividades econômicas do estabelecimento (50%); e (iv) dirigir o estabelecimento com sua família.
Elegibilidade	Condição de atendimento aos requisitos cumulativos estabelecidos pela Lei 11.326/2006 para ser considerado agricultor familiar e acessar as políticas públicas vinculadas ao CAF. A comprovação de elegibilidade é feita mediante análise de documentos comprobatórios de terra, renda e composição familiar.
Módulo Fiscal	Unidade de medida de área, expressa em hectares, cujo valor é fixado pelo INCRA para cada município, levando em conta tipo de exploração predominante, renda obtida e conceito de propriedade familiar. O limite máximo para agricultura familiar é 4 módulos fiscais (Lei 11.326/2006, Art. 3º, I). Os valores variam de 5 a 110 hectares conforme o município.
Unidade Familiar de Produção Agrária (UFPA)	Unidade de cadastro no Sistema CAF que representa o estabelecimento ou empreendimento gerido por agricultor familiar, associação ou outra forma coletiva de produção. Cada UFPA recebe um número de identificação único no sistema.
Requisitos Legais
Mão de Obra Familiar	Trabalho realizado predominantemente por membros da família do agricultor nas atividades econômicas do estabelecimento. Constitui o segundo requisito cumulativo da Lei 11.326/2006, Art. 3º, II. A contratação eventual de terceiros é permitida, desde que não seja a força de trabalho predominante.
Propriedade ou Posse de Terra	Documentação que comprova o direito de propriedade ou a posse legítima do imóvel rural, exigida para comprovação do requisito de área na elegibilidade do CAF. Os tipos documentais aceitos estão especificados na Portaria MDA 19/2025, Art. 8º, I, c.
Renda Familiar Agrícola	Percentual mínimo de renda que deve ser originado de atividades econômicas do próprio estabelecimento para comprovação de elegibilidade. Atualmente fixado em 50%, conforme Portaria MDA 19/2025. Constitui o terceiro requisito cumulativo da Lei 11.326/2006, Art. 3º, III.
Requisitos Cumulativos	Conjunto de quatro condições que devem ser atendidas simultaneamente para caracterização de agricultor familiar, conforme Lei 11.326/2006, Art. 3º: área máxima de 4 módulos fiscais, uso predominante de mão de obra familiar, renda mínima de 50% originada de atividades agrícolas, e direção do estabelecimento com a família.
Validação Documental	Processo de análise de documentos comprobatórios para verificação do atendimento aos requisitos de elegibilidade. No Sistema CAF, pode ser realizada manualmente pela rede de emissores ou de forma automatizada pelo sistema.
Políticas Públicas Vinculadas
Declaração de Aptidão ao PRONAF (DAP)	Documento oficial que identificava agricultores familiares para acesso a programas de crédito rural e políticas públicas, antecessor do Sistema CAF. Foi progressivamente substituído pelo CAF 3.0 a partir de março de 2025.
Programa de Aquisição de Alimentos (PAA)	Programa federal que promove a compra direta de produtos da agricultura familiar para suprir demandas de órgãos públicos e entidades sociais. Orçamento aproximado de R$ 750 milhões em 2024.
Programa Nacional de Alimentação Escolar (PNAE)	Programa federal que destina recursos para aquisição de alimentos oriundos da agricultura familiar para merenda escolar. A Lei 11.947/2009 determina que no mínimo 30% dos recursos sejam destinados à agricultura familiar. Aproximadamente R$ 1,6 bilhão destinado à agricultura familiar.
Programa Nacional de Fortalecimento da Agricultura Familiar (PRONAF)	Programa federal que fornece crédito rural com taxas subsidiadas a agricultores familiares cadastrados no CAF. Movimentou R$ 59,6 bilhões na safra 2023/2024, sendo o principal programa de financiamento da agricultura familiar.
Caracterização de Beneficiários
Pessoa Jurídica em Agricultura Familiar	Associação, cooperativa ou outra forma coletiva de produção que se qualifica como beneficiário do CAF, devendo estar vinculada exclusivamente a atividades agrícolas permitidas, conforme classificação CNAE Seção A (Agricultura, Pecuária, Produção Florestal, Pesca e Aquicultura).
2.	QUALIDADE DE DADOS
Dimensões ISO/IEC 25012:2008
Acurácia	Grau em que os dados registrados correspondem aos valores reais do fenômeno representado. No contexto do CAF, medida pelo confronto entre valores na base de dados e valores nos documentos comprobatórios, como áreas de imóveis e coordenadas geográficas.
Atualidade	Grau em que os dados refletem o estado atual do objeto que representam. Inclui a detecção de dados desatualizados, como registros de beneficiários falecidos ou situações cadastrais que não refletem a realidade vigente.
Completude	Grau em que todos os dados necessários para atender às finalidades de uso estão presentes. Avalia a existência de campos obrigatórios preenchidos e a cobertura de informações essenciais para a validação de elegibilidade.
Consistência	Grau em que os dados estão em conformidade com as regras de negócio, formatos e padrões definidos. Inclui consistência lógica entre campos relacionados, como a coerência entre área declarada e módulos fiscais do município.
Integridade	Propriedade dos dados de estarem íntegros, sem alterações não autorizadas, duplicações ou perdas, ao longo de todo o ciclo de vida. Inclui a manutenção de relacionamentos entre entidades e a preservação da unicidade dos registros.
Validade	Conformidade dos valores de dados com os formatos, tipos e domínios de valores definidos como válidos para cada campo. Por exemplo, coordenadas geográficas dentro dos intervalos válidos ou datas em formato reconhecido pelo sistema.
Governança de Dados
Ciclo de Vida dos Dados	Sequência completa de fases que os dados percorrem desde sua coleta/criação, armazenamento, processamento, utilização, até eventual descarte ou arquivamento. A governança adequada deve assegurar qualidade em todas as fases.
Conformidade (de dados)	Grau em que os dados e processos atendem aos requisitos legais, normativos, técnicos e de negócio aplicáveis. No CAF, inclui conformidade com a Lei 11.326/2006, Decreto 10.046/2019 e normas ISO.
Curadoria de Dados	Processo contínuo de saneamento, correção e manutenção da qualidade dos dados ao longo do tempo. A ausência de curadoria sistemática resulta em acúmulo progressivo de inconsistências (passivo histórico), elevando custos futuros de correção.
Data Owner (Proprietário de Dados)	Papel de governança que designa o responsável formal por um domínio específico de dados, com autoridade para definir regras de qualidade, acesso e uso. A ausência de data owners definidos no CAF foi identificada como causa de fragilidades na governança (Achado IV).
Data Profiling	Análise técnica detalhada da qualidade, estrutura e características dos dados armazenados, identificando padrões, anomalias e não conformidades. Técnica utilizada nesta auditoria para diagnóstico da base de dados do CAF.
Dicionário de Dados	Documentação técnica que descreve a estrutura, tipos, formatos, relacionamentos e significados de todos os campos e tabelas de um sistema de informação. Deve fornecer semântica de negócio compreensível, não apenas nomenclatura técnica.
Governança de Dados	Estrutura de papéis, processos, políticas e controles que assegura que os dados sejam gerenciados como ativo estratégico, com padrões claros, rastreabilidade e responsabilidades bem definidas ao longo do ciclo de vida. Regulamentada pelo Decreto 10.046/2019 no âmbito da APF.
Interoperabilidade	Capacidade de integração e troca de dados entre diferentes sistemas e órgãos, permitindo validação cruzada e consistência das informações. Essencial para verificação de elegibilidade mediante cruzamento com bases da RFB, SISOBI e INCRA.
Metadados	Dados sobre dados, incluindo informações sobre origem, data de criação, data de última atualização, tipo de dado, domínio de valores válidos, relacionamentos, e outras propriedades que contextualizam e explicam os dados armazenados.
Rastreabilidade de Dados	Capacidade de rastrear a origem, as transformações e o fluxo de dados desde sua criação até sua utilização final, incluindo registro de quem criou, alterou e quando. Princípio estabelecido pelo Decreto 10.046/2019.
Problemas e Anomalias
Dados Desatualizados	Informações que refletem situações passadas, mas não foram atualizadas quando da mudança das circunstâncias. No CAF, inclui beneficiários falecidos cujo óbito não foi refletido no sistema, ou situações de renda que se alteraram.
Dados Fictícios	Registros cadastrais contendo informações totalmente falsas ou inventadas, sem qualquer fundamentação em documentação real. Exemplo: e-mails com domínios inexistentes como "@teste.com" ou "@exemplo.com".
E-mail Fictício / CEP Genérico	Entradas de dados com valores claramente inválidos ou fictícios, como e-mails "naopossui@mail.com" ou CEPs terminados em "-000". Evidenciam validação apenas sintática (formato correto) sem verificação semântica (valor real e válido).
Fraude de Dados	Inserção deliberada de informações falsas ou fictícias em bases de dados para obtenção indevida de benefícios. Diferencia-se de erro por haver intencionalidade na irregularidade.
Inconsistência de Dados	Conflito entre valores relacionados ou violação de regras de lógica e relacionamento entre campos. Exemplo: coordenadas geográficas que localizam imóvel fora do município declarado.
Inexatidão de Dados	Divergências entre os valores registrados na base de dados e os valores reais ou documentados. No CAF, identificada pela comparação entre áreas cadastradas e áreas nos documentos comprobatórios.
Outliers	Valores extremos ou estatisticamente implausíveis que se afastam significativamente da distribuição normal da população. No CAF, identificados mediante análise de boxplot, como rendas incompatíveis com agricultura familiar.
Passivo Histórico	Conjunto acumulado de registros antigos com erros não saneados (duplicações, inflação cadastral, óbitos não baixados, dados inconsistentes). No CAF, o passivo histórico herdado de sistemas legados representa desafio significativo para a qualidade da base atual.
Tecnologias de Validação
Cruzamento de Dados	Processo de comparação de registros de duas ou mais bases de dados para identificar coincidências, duplicatas ou inconsistências. Técnica fundamental para verificação de elegibilidade no CAF.
Cruzamentos Triplos	Comparação simultânea de informações do CAF com dois ou mais bancos de dados externos (ex. CAF × RFB × SISOBI) para maior precisão na detecção de anomalias e eliminação de falsos positivos.
OCR (Optical Character Recognition)	Tecnologia de reconhecimento óptico de caracteres que permite extrair automaticamente texto a partir de imagens digitalizadas de documentos. Requer resolução mínima de 300 DPI para eficácia, conforme Resolução CONARQ 31/2010.
Teste de Regressão	Verificação sistemática para garantir que mudanças tecnológicas ou atualizações de sistema não degradem a qualidade dos dados existentes nem introduzam novos erros. A ausência de testes de regressão na transição para o CAF 3.0 e na implementação da interface Leaflet foi identificada como causa de deterioração da qualidade cartográfica.
Validação Automatizada	Processo de verificação automática do atendimento a requisitos técnicos e de negócio, realizado pelo sistema no momento da entrada de dados, sem intervenção manual. Essencial para sistemas com volume massivo de cadastros.
Validação Cruzada de Dados	Confronto de informações cadastrais com bases externas de referência (Receita Federal, SISOBI, IBGE) para verificar concordância e detectar inconsistências ou divergências.
Validação Manual	Processo de verificação executado por pessoas (cadastradores, validadores) através de análise visual e interpretação de documentos comprobatórios. Modelo atual do CAF para verificação de elegibilidade.
Validação Semântica	Verificação de adequação lógica e significativa dos documentos para comprovação. Exemplo: não aceitar RG como comprovante de imóvel rural, pois não comprova propriedade ou posse de terra.
Métricas de Qualidade
Amostra	Subconjunto selecionado da população para análise, quando não é viável ou economicamente justificável analisar a população completa. Deve seguir critérios estatísticos para permitir generalização.
Amostra Estratificada	Amostra probabilística em que a população é dividida em estratos (grupos homogêneos) e a seleção aleatória ocorre dentro de cada estrato, garantindo representatividade de subgrupos relevantes.
Amostra Probabilística	Seleção aleatória de elementos de uma população seguindo critérios estatísticos rigorosos, de forma a permitir generalização dos resultados para toda a população com nível de confiança conhecido.
Análise Censitária	Análise que abrange a população completa (100% dos registros) sem amostragem. Utilizada quando a escala técnica permite viabilidade e a criticidade do requisito justifica análise exaustiva.
Intervalo de Confiança (IC)	Faixa de valores que, com certa probabilidade (usualmente 95% ou 99%), contém o verdadeiro valor do parâmetro populacional estimado a partir de amostra. Expressa a precisão da estimativa.
Margem de Erro	Diferença máxima esperada entre a estimativa obtida da amostra e o valor verdadeiro da população, expressa em pontos percentuais. Determina a precisão das projeções para a população total.
Taxa de Não Conformidade	Percentual de registros que não atendem aos critérios técnicos ou legais estabelecidos. Métrica utilizada para quantificar a magnitude dos problemas de qualidade de dados.
3.	AUDITORIA TCU
Conceitos de Auditoria
Achado de Auditoria	Constatação de situação que desvia de critérios técnicos, normativos ou regulatórios, estruturada em cinco elementos situação encontrada, critério, causa, efeito e encaminhamento. Pode constituir não conformidade ou oportunidade de melhoria.
Achado Incidental	Constatação secundária, não planejada originalmente, que emerge durante os procedimentos de auditoria sobre outro tema, mas que reúne materialidade e relevância suficientes para registro e reporte no relatório.
Auditoria Operacional	Trabalho de controle externo que avalia a eficiência, eficácia e economicidade da gestão, bem como a conformidade com leis e regulamentos, em temas específicos de interesse da Administração Pública. Metodologia aplicada nesta fiscalização.
Causa	Fator causal, origem ou razão fundamental que explica por que a não conformidade ocorre. No modelo de achado do TCU, a identificação de causas é essencial para proposição de encaminhamentos efetivos.
Conclusão de Auditoria	Síntese final que responde às questões de auditoria e consolida as principais constatações da análise técnica, fundamentando as propostas de encaminhamento.
Efeito	Impacto concreto, detectável e mensurável resultante de uma situação de não conformidade. Pode ser atual (já materializado) ou potencial (risco de ocorrência futura).
Procedimento de Auditoria	Ação técnica específica e documentada executada para obtenção de evidências e resposta a questões de auditoria. Exemplos: análise de amostra, cruzamento de bases, entrevistas com gestores.
Questão Específica	Desdobramento de questões principais de auditoria em perguntas direcionadas para investigação de aspectos particulares do tema auditado, permitindo análise estruturada e sistemática.
Questões de Auditoria (QST)	Perguntas elaboradas no planejamento da auditoria que norteiam as investigações e estruturam os achados conforme os riscos mapeados. Nesta auditoria: QST-1 (qualidade de dados) e QST-2 (governança).
Risco de Auditoria	Possibilidade de que um evento adverso ocorra e produza impactos significativos na gestão ou na execução de políticas públicas. O mapeamento de riscos orienta a priorização dos trabalhos de auditoria.
Vulnerabilidade	Fragilidade, fraqueza ou deficiência em processos, controles ou sistemas que facilita a materialização de riscos. A identificação de vulnerabilidades fundamenta recomendações de melhoria.
Normas e Critérios
Confiabilidade	Propriedade de um sistema ou dado que permite confiar em sua integridade, veracidade e adequação para fins de tomada de decisão e execução de políticas públicas.
Conformidade	Aderência a critérios técnicos, normativos ou de regulação estabelecidos por lei, decreto, portaria ou norma técnica reconhecida. Base para avaliação de regularidade em auditorias.
Normas de Auditoria do Tribunal (NAT)	Regulamentação técnica que estabelece as exigências para execução de auditorias no TCU, incluindo critérios de materialidade, generalização de conclusões e documentação de evidências.
Marcos Regulatórios
Decreto 9.064/2017	Decreto que regulamenta a Lei 11.326/2006 e institui o Sistema de Cadastro da Agricultura Familiar (CAF) como sucessor da DAP, estabelecendo conceitos e procedimentos para identificação de agricultores familiares.
Decreto 10.046/2019	Decreto que estabelece diretrizes de governança pública de dados na Administração Pública Federal, incluindo princípios de integridade, rastreabilidade e transparência aplicáveis aos sistemas de informação governamentais.
Decreto 10.332/2020	Regulamentação complementar da Lei Geral de Proteção de Dados Pessoais (LGPD) aplicada a órgãos públicos, estabelecendo requisitos para tratamento de dados pessoais pela APF.
Lei 11.326/2006	Lei da Agricultura Familiar. Define o conceito legal de agricultor familiar e estabelece os requisitos cumulativos para caracterização e acesso a políticas públicas. Marco legal fundamental para o Sistema CAF.
Portaria MDA 19/2025	Portaria que operacionaliza a implementação do CAF 3.0 (a partir de 26/3/2025), especificando requisitos de validação documental, critérios de elegibilidade, tipos documentais aceitos e procedimentos de cadastramento.
4.	ESTATÍSTICA
Conceitos e Métodos
Amostra	Ver definição em "2. Qualidade de Dados - Métricas de Qualidade".
Boxplot	Gráfico estatístico que visualiza a distribuição de dados através de quartis, mediana e identificação de valores extremos (outliers). Utilizado nesta auditoria para detectar rendas e áreas estatisticamente implausíveis.
Distribuição Normal	Padrão estatístico em forma de sino (curva de Gauss) onde valores se distribuem simetricamente ao redor da média. Serve como referência para detectar anomalias e outliers em conjuntos de dados.
Outliers	Ver definição em "2. Qualidade de Dados - Problemas e Anomalias".
População	Conjunto completo de elementos que é objeto de estudo estatístico. No CAF, exemplos incluem população de 11.377.318 documentos, população de 3.171.656 imóveis rurais.
População Estimada	Quantidade total de elementos em uma população calculada com base em proporções observadas em amostra, considerando intervalo de confiança e margem de erro estatística.
Proporção Binomial	Método estatístico para cálculo de intervalos de confiança aplicado a proporções (variáveis com dois estados possíveis conforme/não conforme). Utilizado para estimar percentuais de inadequação na população.
Taxa de Erro	Percentual de registros que apresentam desvios de conformidade em relação aos critérios estabelecidos. Métrica fundamental para avaliação de qualidade de dados.
Teste de Significância	Análise estatística que verifica se diferenças observadas entre grupos ou períodos são estatisticamente significativas (não atribuíveis ao acaso). Nesta auditoria, aplicado para comparar taxas de erro entre períodos do CAF.
Valor-p	Medida estatística que indica a probabilidade de um resultado ser observado por acaso, assumindo que não há diferença real. Valores baixos (p<0,05) indicam significância estatística das diferenças observadas.
Análise de Dados
Análise Agregada	Análise que considera o conjunto completo de dados para identificar padrões gerais, como a divergência sistemática agregada de +120,89% entre áreas cadastradas e áreas documentadas.
Análise de Janelas Temporais Equivalentes	Comparação estatística de períodos diferentes mas com tamanhos amostrais semelhantes, garantindo robustez metodológica na análise de mudanças ao longo do tempo.
Data Analytics	Aplicação de técnicas estatísticas e computacionais para análise de grandes volumes de dados com objetivo de identificar padrões, anomalias e insights. Metodologia central desta auditoria.
Divergência Sistemática	 Padrão consistente de desvio em uma direção específica, indicando causa estrutural. No CAF, identificou-se divergência sistemática de +120,89% nas áreas (áreas cadastradas menores que nos documentos).
Falsos Positivos	 Identificação incorreta de anomalia ou erro quando na verdade não há problema real. Risco minimizado através de cruzamentos múltiplos de bases e validação de casos suspeitos.
5.	GEOESPACIAL
Conceitos Cartográficos
Coordenadas Geográficas	Valores de latitude e longitude que identificam a localização espacial de um ponto na superfície terrestre. No Sistema CAF, utilizadas para localizar imóveis rurais. Latitude varia de -90° a +90°; Longitude de -180° a +180°.
Dado Geoespacial	Informação que localiza espacialmente um objeto ou fenômeno, incluindo coordenadas geográficas (latitude/longitude) ou outros identificadores de posição territorial. No CAF, registra a localização dos imóveis rurais.
Georreferenciamento	Processo de atribuição de coordenadas geográficas (latitude/longitude) a pontos, áreas ou objetos territoriais, permitindo localização precisa em mapas e cruzamento com outras bases geoespaciais.
Imóvel Rural	Propriedade ou posse de terra destinada à agricultura familiar, registrada no CAF com localização geoespacial através de coordenadas geográficas e área em hectares. A base do CAF contém 3.171.656 imóveis rurais.
Integridade Geoespacial	Propriedade dos dados cartográficos de estar corretos, sem duplicações, sobreposições indevidas ou conflitos espaciais, mantendo coerência territorial e unicidade de localização.
Latitude	Coordenada geográfica que mede a distância angular, em graus, de um ponto em relação ao Equador. Varia de -90° (Polo Sul) a +90° (Polo Norte). No Brasil, valores típicos entre -34° e +5°.
Longitude	Coordenada geográfica que mede a distância angular, em graus, de um ponto em relação ao Meridiano de Greenwich. Varia de -180° a +180°. No Brasil, valores típicos entre -74° e -35°.
Parcela	Unidade territorial contígua de terra que constitui um imóvel rural, identificável através de seu perímetro e localização geoespacial.
Qualidade Cartográfica
Acurácia Geoespacial	Conformidade geral entre dados cartográficos (coordenadas, áreas, perímetros) registrados e a realidade territorial que representam. Dimensão crítica de qualidade para dados do CAF.
Acurácia Posicional	Grau de proximidade entre as coordenadas geográficas registradas e as coordenadas verdadeiras da localização do imóvel. Pode ser medida em metros de desvio ou percentual de erro.
Consistência de Coordenadas	Verificação de que coordenadas estejam dentro dos intervalos válidos do sistema de coordenadas geográficas e do território brasileiro. Inclui validação algorítmica de limites.
Coordenadas Implausíveis	Coordenadas que, embora possam ser matematicamente válidas, não correspondem à localização real do imóvel ou estão fora de contexto territorial apropriado. Exemplo: coordenadas que localizam imóvel no oceano.
Erro Algorítmico (Sintático)	Violação de regras matemáticas básicas do sistema de coordenadas geográficas, como latitude fora do intervalo [-90, 90] ou longitude fora de [-180, 180]. Erro detectável por validação automatizada.
Erro de Digitação Manual	Erros introduzidos quando coordenadas geográficas são inseridas manualmente por digitação, típicos do sistema CAF anterior à interface Leaflet. Incluem inversão de dígitos, omissão de sinal negativo.
Erro Geoespacial (Semântico)	Desvio entre coordenadas registradas e a localização real do imóvel, mesmo que tecnicamente válidas matematicamente. Exemplo: coordenadas que localizam imóvel em município diferente do declarado.
Precisão Decimal	Número de casas decimais em coordenadas geográficas que determina o grau de exatidão posicional. Exemplo: 6 casas decimais proporcionam precisão de aproximadamente 10 centímetros.
Anomalias Cartográficas
Deterioração da Qualidade Cartográfica	Aumento na taxa de erros em dados geoespaciais ao longo do tempo ou após mudanças tecnológicas. No CAF, identificou-se deterioração de +40,6% na taxa de erro global após implementação do CAF 3.0.
Duplicação Espacial	Existência de múltiplos registros cadastrais que compartilham exatamente as mesmas coordenadas geográficas, comprometendo a unicidade e rastreabilidade espacial dos beneficiários.
Inflação Cadastral	Fenômeno em que a área total cadastrada em um município supera a área territorial oficial daquele município segundo o IBGE, indicando inconsistência sistêmica de dados. Identificada em 632 municípios (11,43%).
Rastreabilidade Espacial	Capacidade de identificar de forma única cada imóvel rural pela sua localização geoespacial. Comprometida quando múltiplos registros compartilham as mesmas coordenadas geográficas.
Sobreposição de Áreas	Situação em que duas ou mais parcelas cadastradas compartilham total ou parcialmente o mesmo espaço territorial, criando conflito de posse/propriedade e impossibilitando validação de áreas.
Sistemas de Referência
Cadastro Ambiental Rural (CAR)	Sistema de cadastro de imóveis rurais com finalidade ambiental, gerido pelo Ministério da Gestão e Inovação em Serviços Públicos (MGI), contendo dados geoespaciais de propriedades rurais para fins de regularização ambiental.
Interface Leaflet	Biblioteca JavaScript de código aberto para mapas interativos, implementada no CAF em 15/8/2025. Permite seleção de localização de imóvel rural mediante clique direto em mapa visual, substituindo a digitação manual de coordenadas.
Malha do IBGE	Base geográfica oficial do Instituto Brasileiro de Geografia e Estatística que contém os limites territoriais de municípios, estados e regiões do Brasil. Utilizada como referência para validação de áreas municipais.
SICAR	Sistema Nacional de Cadastro Ambiental Rural que integra o CAR, gerido pela rede de órgãos ambientais estaduais. Contém dados geoespaciais de propriedades rurais para fins de monitoramento ambiental.
SIRC	Sistema Nacional de Informações de Registro Civil, Sistema instituído pelo Decreto nº 8.270/2014 que centraliza as informações de nascimento, casamento, óbito e natimorto, substituindo o antigo SISOBI. É a base oficial vigente para verificação de óbitos e integridade de dados civis.
SISOBI	Sistema de Controle de Óbitos.
Sistema de Gestão Fundiária (SIGEF)	Sistema oficial do Instituto Nacional de Colonização e Reforma Agrária (INCRA) que registra e georreferencia imóveis rurais com precisão técnica elevada. Fonte potencial para validação cruzada de dados do CAF.


 
Apêndice VII – Listas de Siglas, de Figuras e de Tabelas

Lista de Siglas
ADPF	Arguição de Descumprimento de Preceito Fundamental
APF	Administração Pública Federal
ATER	Assistência Técnica e Extensão Rural
AudSustentabilidade	Unidade de Auditoria Especializada em Sustentabilidade do TCU
AudTI	Unidade de Auditoria Especializada em Tecnologia da Informação do TCU
CAF	Cadastro Nacional da Agricultura Familiar
CAR	Cadastro Ambiental Rural
CEP	Código de Endereçamento Postal
CI/CD	Continuous Integration/Continuous Deployment
CMDRS	Conselho Municipal de Desenvolvimento Rural Sustentável
CNAE	Classificação Nacional de Atividades Econômicas
CNIS	Cadastro Nacional de Informações Sociais
CNPJ	Cadastro Nacional da Pessoa Jurídica
COBIT	Control Objectives for Information and Related Technologies
CONARQ	Conselho Nacional de Arquivos
COP 30	30ª Conferência das Partes da Convenção-Quadro das Nações Unidas sobre Mudança do Clima
COSS	Centre for Open Societal Systems
CPF	Cadastro de Pessoas Físicas
DAMA-DMBOK	Data Management Body of Knowledge
DAP	Declaração de Aptidão ao Pronaf
DETER	Sistema de Detecção de Desmatamento em Tempo Real
DNE	Diretório Nacional de Endereços
DPI	Dots Per Inch (Pontos por Polegada)
DRN	Documento de Regras de Negócio
FUNAI	Fundação Nacional dos Povos Indígenas
IBAMA	Instituto Brasileiro do Meio Ambiente e dos Recursos Naturais Renováveis
IBGE	Instituto Brasileiro de Geografia e Estatística
IC	Intervalo de Confiança
ICMBio	Instituto Chico Mendes de Conservação da Biodiversidade
IEC	International Electrotechnical Commission
iGovSisp	Índice de Governança do Sistema de Administração dos Recursos de TI
INCRA	Instituto Nacional de Colonização e Reforma Agrária
INPE	Instituto Nacional de Pesquisas Espaciais
ISO	International Organization for Standardization
LAI	Lei de Acesso à Informação (Lei nº 12.527/2011)
LAR	Lista de Alto Risco da Administração Pública Federal
LGPD	Lei Geral de Proteção de Dados Pessoais (Lei nº 13.709/2018)
MC	Memória de Cálculo
MDA	Ministério do Desenvolvimento Agrário e Agricultura Familiar
MGI	Ministério da Gestão e da Inovação em Serviços Públicos
NAT	Normas de Auditoria do Tribunal de Contas da União
NORAD	Agência Norueguesa de Cooperação para o Desenvolvimento
OCR	Optical Character Recognition (Reconhecimento Óptico de Caracteres)
OKR	Objectives and Key Results (Objetivos e Resultados-Chave)
PAA	Programa de Aquisição de Alimentos
PNAE	Programa Nacional de Alimentação Escolar
PNHR	Programa Nacional de Habitação Rural
PNRA	Programa Nacional de Reforma Agrária
Proagro 	Programa de Garantia da Atividade Agropecuária da Agricultura Familiar
PRONAF	Programa Nacional de Fortalecimento da Agricultura Familiar
PT	Papel de Trabalho
QST	Questão de Auditoria
RFB	Receita Federal do Brasil
RG	Registro Geral (Carteira de Identidade)
SecexEstado	Secretaria de Controle Externo de Governança, Inovação e Transformação Digital do Estado do TCU
SICAR	 Sistema Nacional de Cadastro Ambiental Rural
SIGEF	Sistema de Gestão Fundiária
SIPRA	Sistema de Informações de Projetos de Reforma Agrária
SISP	Sistema de Administração dos Recursos de Tecnologia da Informação
SIRC	Sistema Nacional de Informações de Registro Civil
SISOBI	Sistema de Controle de Óbitos
SNCR	Sistema Nacional de Cadastro Rural
STF	Supremo Tribunal Federal
TC	Tomada de Contas
TCU	Tribunal de Contas da União
TI	Tecnologia da Informação
UC	Unidade de Conservação
UF	Unidade da Federação ou Unidade Familiar
UFPA	Unidade Familiar de Produção Agrária
ULA	Unidade Local de Atendimento
 
 
Lista de Figuras
Figura 1. Documento de imóvel com área divergente na base de dados.	16
Figura 2. Exemplos de inadequação semântica de documentos comprobatórios no CAF	19
Figura 3. Comparação Visual entre Erros Algorítmicos (Detectáveis por Validação de Formato) e Erros Geoespaciais (Requerem Validação Cruzada com Bases Oficiais)	25
Figura 4. Evolução dos erros ao longo da introdução do CAF 3.0	26
Figura 5. Trade-off algorítmico-semântico na transição Leaflet	27
Figura 6. Comprometimento da qualidade cadastral do CAF por dimensão de análise	37
Figura 7. Classificação das divergências de data de nascimento entre CAF e RFB	39
Figura 8. Dicotomia na qualidade de e-mails cadastrados no CAF por tipo de pessoa	41

 
Lista de Tabelas
Tabela 1. Inadequação Semântica por Tipo de Documento	15
Tabela 2. Divergências de Área por Faixa de Magnitude	17
Tabela 3. Distribuição de Resolução de Documentos (DPI)	18
Tabela 4. Trade-off algorítmico-semântico na transição Leaflet: eliminação de erros de formato às custas de erros de conteúdo	27
Tabela 5. Resumo quantitativo de duplicações espaciais em registros de alta precisão	28
Tabela 6. Comparação de duplicações: Entrada Manual (E1) vs. Interface Leaflet (E2)	29
Tabela 7. Comparação de duplicações: CAF 2.x – Antes do CAF 3.0 (E3) vs. Depois do CAF 3.0 (E4)	30
Tabela 8. Síntese das situações do Achado de Qualidade Cartográfica e de Integridade Geoespacial	30
Tabela 9. Síntese Quantitativa dos Achados por Dimensão de Qualidade	36
Tabela 10. Síntese das Inconsistências de Capacidade Civil (Sub-achado III.1)	38
Tabela 11. TOP 10 divergências de data de nascimento	40
Tabela 12. Síntese da Qualidade dos Dados de Contato (Sub-achado III.2)	42
Tabela 13. Síntese da Análise de Outliers de Renda (Sub-achado III.3)	43
Tabela 14. Evolução do Limite de Renda Bruta Anual (Pronaf)	43
Tabela 15. Síntese das Entidades com CNAEs Incompatíveis (Sub-achado III.4)	45
Tabela 16. Cadeia normativa completa	46
Tabela 17. Análise das dimensões do Dicionário de Dados	50
Tabela 18. Análise censitária dos campos do dicionário de dados	51
Tabela 19. Exemplos Críticos de Campos Numéricos sem Unidade de Medida Definida	52
Tabela 20. Unidades de Medida com Definição Legal Omitidas no Dicionário de Dados	53
Tabela 21. Ambiguidades detectadas no Dicionário de Dados	54

 
Apêndice VIII – Notas de fim
