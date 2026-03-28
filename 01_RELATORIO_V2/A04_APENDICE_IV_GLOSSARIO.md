# APÊNDICE IV — GLOSSÁRIO

Os termos abaixo são definidos no contexto desta auditoria e dos referenciais técnicos adotados. As definições não pretendem esgotar o significado de cada conceito, mas esclarecer o sentido em que foram empregados no relatório.

**Ad-hoc (0)** — Nível mais baixo da escala de maturidade usada no relatório. Indica ausência de processo formal, com atuação reativa, dependente de pessoas específicas e sem padrão estável.

**Acurácia** — Grau de proximidade entre um dado registrado e a realidade que ele pretende representar. No relatório, é uma dimensão central da qualidade de dados.

**API** — Application Programming Interface. Mecanismo padronizado que permite a comunicação automatizada entre sistemas.

**Amostra aleatória simples** — Seleção em que todos os elementos de uma população têm a mesma chance de serem escolhidos. É a forma mais básica de amostragem probabilística.

**Amostragem estratificada** — Tipo de amostragem probabilística em que a população é dividida em grupos relevantes, chamados estratos, e cada grupo recebe uma parcela da amostra. Serve para melhorar a representatividade da estimativa.

**Amostragem probabilística** — Método de seleção em que cada elemento da população tem probabilidade conhecida e não nula de ser incluído. É o que permite inferência estatística com intervalo de confiança e margem de erro.

**Análise censitária** — Análise feita sobre toda a população, e não apenas sobre uma amostra. Por isso, em regra, não depende de margem de erro nem de projeção inferencial.

**ATER** — Assistência Técnica e Extensão Rural. Conjunto de serviços de orientação técnica prestados aos agricultores familiares.

**Auditoria operacional** — Tipo de auditoria voltada a avaliar desempenho, qualidade, governança e resultados de políticas públicas ou processos administrativos. Não se concentra apenas em legalidade formal ou em responsabilização individual.

**BCadastro** — Serviço de consulta cadastral acessado pelo CAF para validar dados junto à Receita Federal. No relatório, aparece como fonte de cruzamentos cadastrais.

**Bounding box** — Limite geográfico definido por latitudes e longitudes mínimas e máximas. Funciona como um retângulo imaginário que impede o sistema de aceitar pontos fora da área esperada.

**CAF** — Cadastro Nacional da Agricultura Familiar. Sistema do MDA usado para identificar e qualificar o público da agricultura familiar para acesso a políticas públicas.

**CAF 2.x** — Geração intermediária do sistema CAF, anterior à versão 3.0. No relatório, serve como referência de comparação para avaliar regressões e melhorias tecnológicas.

**CAF 3.0** — Versão do CAF vigente na base auditada. É a principal referência do relatório para análise de regras de negócio, qualidade de dados e transições tecnológicas.

**Caixa-preta** — Expressão usada quando um sistema funciona, mas seu significado interno não é transparente para usuários externos. No relatório, descreve situação em que só entende plenamente os dados quem já conhece regras implícitas do sistema.

**CEP** — Código de Endereçamento Postal. No relatório, foi usado para testar qualidade de dados de contato e coerência geográfica.

**Ciclo de vida dos dados** — Conjunto de fases pelas quais os dados passam, desde a criação ou coleta até atualização, uso, compartilhamento, arquivamento e descarte. A qualidade precisa ser preservada ao longo de todo esse ciclo.

**Claude API** — Interface de acesso ao modelo de linguagem Claude, da Anthropic. Foi usada como ferramenta auxiliar de classificação semântica de documentos, sem substituir o julgamento final do auditor.

**CMMI-DMM** — Capability Maturity Model Integration for Data Management. Modelo de maturidade usado como inspiração para a escala de níveis adotada no relatório.

**CNAE** — Classificação Nacional de Atividades Econômicas. Código oficial que identifica a atividade econômica principal de uma pessoa jurídica.

**CNIS** — Cadastro Nacional de Informações Sociais. Base governamental usada como referência em cruzamentos cadastrais e de renda.

**CNPJ** — Cadastro Nacional da Pessoa Jurídica. Número que identifica empresas e outras pessoas jurídicas perante a administração pública.

**COBIT 2019** — Framework de governança e gestão de tecnologia da informação publicado pela ISACA. No relatório, foi usado especialmente como referência para gestão de mudanças e configuração.

**Completude** — Dimensão de qualidade que mede se os dados necessários estão presentes. Dado incompleto é aquele que deixa de informar algo essencial para seu uso.

**ConectaGOV** — Plataforma federal de interoperabilidade que permite integração e troca de dados entre órgãos e sistemas governamentais.

**Conformidade integral** — Situação em que um registro atende simultaneamente a todos os critérios de qualidade ou controle examinados. No relatório, aparece também como indicador informado pelo gestor.

**Consistência lógica** — Dimensão de qualidade que verifica se os dados obedecem às regras esperadas do sistema ou do domínio analisado. No contexto geoespacial, inclui coerência entre coordenadas e território declarado.

**Consistência municipal** — Verificação de se as coordenadas do imóvel recaem dentro do município informado no cadastro. É um teste específico de coerência territorial.

**CPF** — Cadastro de Pessoas Físicas. Número que identifica a pessoa perante a Receita Federal.

**Credibilidade** — Dimensão de qualidade ligada à confiança que se pode depositar nos dados. Dados pouco críveis podem até estar preenchidos, mas não são confiáveis para decisão.

**Curadoria de dados** — Conjunto de atividades voltadas a revisar, corrigir, organizar e manter dados ao longo do tempo. No relatório, a ausência dessa curadoria ajuda a explicar a permanência de passivos históricos.

**DAMA-DMBOK v2** — Data Management Body of Knowledge, 2ª edição. Referencial internacional de governança e gestão de dados, usado no relatório como base conceitual para maturidade e qualidade de dados.

**DAP** — Declaração de Aptidão ao Pronaf. Instrumento anterior ao CAF para identificação do público da agricultura familiar.

**Data steward** — Responsável por um conjunto de dados ou domínio informacional, com papel de zelar por definição, qualidade, uso e consistência desses dados. É figura típica de governança de dados.

**Data stewardship** — Função organizacional de curadoria e responsabilidade contínua sobre os dados. Envolve papéis, rotinas e decisões para manter qualidade e coerência do ativo informacional.

**DCAF** — Departamento de Cadastro Nacional da Agricultura Familiar, vinculado ao MDA. É a área gestora do cadastro no âmbito federal.

**Datum geodésico** — Sistema de referência usado para representar a posição de pontos na superfície terrestre. Sem datum definido, latitude e longitude podem perder significado técnico preciso.

**Definido (3)** — Nível de maturidade em que o processo já está padronizado, documentado e institucionalizado. Não depende apenas de prática individual.

**Dicionário de dados** — Documento que descreve campos, significados, tipos, domínios e outros atributos de um banco de dados. No relatório, é o principal artefato de metadados do CAF.

**Documentação post mortem** — Documentação produzida depois que o sistema já está pronto ou em uso, em vez de acompanhar o desenvolvimento. Costuma ser mais superficial e menos sincronizada com a realidade do sistema.

**Domínio de valores** — Conjunto de valores permitidos ou esperados para um campo. Pode ser lista fechada, faixa numérica, padrão textual ou outra regra de preenchimento.

**DPI** — Dots Per Inch, ou pontos por polegada. Medida de resolução de imagem usada para avaliar qualidade de documentos digitalizados.

**Duplicação espacial** — Situação em que dois ou mais registros compartilham coordenadas idênticas ou praticamente idênticas. Pode indicar erro cadastral, preenchimento padronizado indevido ou necessidade de apuração adicional.

**Erro cartográfico** — Inconsistência entre a localização informada no cadastro e a localização geográfica esperada ou aceita como válida. No relatório, é usado como medida ampla de problema geoespacial.

**Exatidão posicional** — Grau de proximidade entre a coordenada registrada e a posição considerada correta. É conceito central da norma ISO 19157 para dados geográficos.

**FPC** — Finite Population Correction, ou correção para população finita. Ajuste estatístico usado quando a amostra representa parcela relevante da população.

**Fonte autoritativa** — Norma, documento oficial ou autoridade institucional que justifica a existência e o significado de um dado. Na ISO 11179, é elemento importante da boa documentação de metadados.

**Georreferenciamento** — Associação de um dado a uma posição geográfica por coordenadas ou geometria. No CAF, refere-se especialmente à localização dos imóveis rurais.

**Gerenciado (4)** — Nível de maturidade em que o processo já é medido e acompanhado por indicadores, metas e controles quantitativos. Pressupõe gestão sistemática do desempenho.

**Governança de dados** — Exercício de autoridade, papéis, regras e decisões sobre como os dados são definidos, usados, protegidos e mantidos. No relatório, é o pano de fundo para avaliar se o CAF tem controles institucionais consistentes sobre seus dados.

**IBGE** — Instituto Brasileiro de Geografia e Estatística. Fornece, entre outros insumos, malhas territoriais e áreas oficiais municipais usadas nas análises do relatório.

**Incra** — Instituto Nacional de Colonização e Reforma Agrária. No relatório, aparece como fonte de dados e de integração territorial, especialmente em temas fundiários e de reforma agrária.

**Inflação cadastral** — Situação em que a área total cadastrada no CAF para um município supera a área oficial desse município segundo a base de referência usada na auditoria. É um indicador de possível incoerência territorial agregada, e não conclusão automática de fraude.

**Inicial (1)** — Nível de maturidade em que a prática existe, mas ainda depende fortemente de pessoas específicas e não é plenamente repetível nem escalável.

**INTOSAI** — International Organization of Supreme Audit Institutions. Organização internacional das entidades superiores de controle, responsável pelas ISSAI.

**Interoperabilidade** — Capacidade de sistemas e organizações de trocar dados e usar esses dados de forma útil e coerente. Não é só conexão técnica: também envolve padronização de significado.

**Intervalo de confiança (IC)** — Faixa de valores em torno da estimativa obtida na amostra, dentro da qual o valor verdadeiro da população é esperado com determinado nível de confiança. É forma de expressar incerteza estatística.

**ISSAI** — International Standards of Supreme Audit Institutions. Conjunto de normas internacionais aplicáveis às entidades de fiscalização superior.

**ISO 19157-1:2023** — Norma internacional de qualidade de dados geográficos. Define conceitos como exatidão posicional, consistência lógica e completude.

**ISO/IEC 11179:2015** — Norma internacional sobre registros de metadados. Orienta como documentar adequadamente elementos de dados, incluindo nome, definição, domínio, unidade e fonte autoritativa.

**ISO/IEC 25012:2008** — Norma internacional de modelo de qualidade de dados. Reúne dimensões como acurácia, completude, consistência, atualidade e credibilidade.

**Kappa** — Medida estatística de concordância entre avaliadores. No relatório, é mencionada como exemplo de métrica que poderia medir concordância entre classificação automatizada e revisão humana.

**Latitude** — Coordenada geográfica que indica posição norte-sul de um ponto na Terra. É sempre interpretada em conjunto com a longitude.

**Leaflet** — Interface de mapa usada para seleção visual de coordenadas. No relatório, representa mudança tecnológica relevante no processo de georreferenciamento do CAF.

**Longitude** — Coordenada geográfica que indica posição leste-oeste de um ponto na Terra. Junto com a latitude, define a localização do imóvel.

**Margem de erro** — Medida da precisão de uma estimativa amostral. Quanto menor a margem de erro, mais estreita tende a ser a faixa de incerteza.

**MDA** — Ministério do Desenvolvimento Agrário e Agricultura Familiar. Órgão responsável pela política pública e pela gestão institucional do CAF.

**MER** — Modelo Entidade-Relacionamento. Diagrama técnico que mostra tabelas, campos e vínculos entre partes de um banco de dados.

**Metadados** — Dados sobre os próprios dados. Descrevem significado, estrutura, formato, origem, restrições e regras de uso de um campo ou conjunto de dados.

**Modelo conceitual** — Representação em linguagem mais compreensível das entidades centrais de um sistema e de suas relações. Difere do MER, que é mais técnico e voltado ao banco de dados.

**Módulo fiscal** — Unidade de medida agrária, definida por município, usada em regras legais da agricultura familiar. A Lei 11.326/2006 utiliza o limite de quatro módulos fiscais como critério relevante de elegibilidade.

**NAT** — Normas de Auditoria do TCU. Conjunto normativo que disciplina planejamento, execução, evidência e comunicação dos trabalhos de auditoria do Tribunal.

**OCR** — Optical Character Recognition, ou reconhecimento óptico de caracteres. Tecnologia que transforma texto contido em imagem em texto pesquisável e tratável por sistema.

**Otimizado (5)** — Nível mais alto da escala de maturidade. Indica processo consolidado, medido e em melhoria contínua, com capacidade de aperfeiçoamento baseada em evidências.

**PAA** — Programa de Aquisição de Alimentos. Política pública voltada à compra de alimentos da agricultura familiar.

**PNRA** — Programa Nacional de Reforma Agrária. No relatório, aparece especialmente em discussões sobre integração de dados territoriais.

**Precisão decimal** — Número de casas decimais usado para registrar coordenadas. Em geral, mais casas decimais significam localização mais precisa.

**Projeção populacional** — Estimativa do quantitativo absoluto de casos na população, obtida a partir da proporção observada em amostra. Exemplo: transformar uma taxa em número estimado de registros afetados.

**Pronaf** — Programa Nacional de Fortalecimento da Agricultura Familiar. Principal política de crédito voltada ao público identificado como agricultor familiar.

**Qualidade de dados** — Grau em que os dados servem adequadamente ao uso pretendido. No relatório, é avaliada por dimensões como acurácia, completude, consistência e atualidade.

**Rastreabilidade** — Capacidade de reconstruir de onde veio um dado, como foi transformado e em que etapa foi usado. É essencial para auditoria e para reprodutibilidade.

**RedeCAF** — Rede de entidades e agentes credenciados que emitem, atualizam ou apoiam o cadastramento no CAF em todo o território nacional.

**Repetível (2)** — Nível de maturidade em que o processo já pode ser reproduzido de forma consistente, embora ainda não esteja plenamente medido ou otimizado.

**RFB** — Receita Federal do Brasil. No relatório, aparece como principal fonte externa de validação cadastral e de capacidade civil.

**SAF** — Secretaria de Agricultura Familiar e Agroecologia do MDA. Unidade à qual se vincula a gestão do CAF.

**Sicar** — Sistema Nacional de Cadastro Ambiental Rural. Base de referência territorial usada de forma subsidiária nas análises.

**SIRGAS 2000** — Sistema geodésico de referência adotado no Brasil. É um dos datums usados para representar coordenadas geográficas com padronização nacional.

**Sigef** — Sistema de Gestão Fundiária do Incra. Reúne dados georreferenciados de imóveis rurais e serve como referência fundiária.

**Sisobi** — Sistema de Controle de Óbitos da Previdência Social. Foi usado no relatório para confirmação conservadora de falecimentos.

**SNCR** — Sistema Nacional de Crédito Rural. Conjunto institucional ligado à concessão de crédito rural, no qual o público da agricultura familiar tem relevância própria.

**Subamostra** — Recorte menor extraído de uma amostra maior ou de um universo específico da análise. É usada quando apenas parte dos casos permite determinado teste.

**Tautológica** — Descrição que apenas repete o nome do campo com outras palavras, sem realmente explicar seu significado. No relatório, é tratada como sinal de baixa qualidade semântica do dicionário de dados.

**UFPA** — Unidade Familiar de Produção Agrária. Unidade cadastral do CAF que organiza o núcleo produtivo familiar, seus responsáveis, imóveis e informações associadas.

**Unidade de medida** — Padrão usado para expressar um valor numérico, como hectare, real ou metro. Sem unidade explícita, o dado pode ser interpretado de forma errada.

**Versionamento semântico** — Registro controlado das mudanças de significado, uso ou regra de um dado ao longo do tempo. É importante para evitar que o sistema mude sem que a documentação acompanhe.

**WGS84** — Sistema de referência geodésica amplamente usado em GPS e aplicações cartográficas. É padrão internacional de coordenadas geográficas.
