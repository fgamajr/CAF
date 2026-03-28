## {S} ACHADO 01

**Insuficiência dos mecanismos de validação e da documentação comprobatória no CAF compromete a verificação da elegibilidade da agricultura familiar**

23. A auditoria concluiu que os mecanismos de validação documental do CAF permanecem insuficientes para assegurar, em escala compatível com o cadastro, a comprovação dos requisitos cumulativos de elegibilidade previstos no art. 3º da Lei 11.326/2006 e operacionalizados pelos arts. 8º e 22 da Portaria MDA 19/2025. Esse quadro decorre, principalmente, de um processo de ingestão documental desenhado para aceitar arquivos, e não para verificar seu conteúdo, da ausência de controles consistentes sobre dados críticos de área, da inexistência de requisitos mínimos de qualidade técnica na digitalização e da permanência de passivo herdado da DAP e do CAF 2.0.

24. O resultado é a convivência, na base ativa, de 27,1% de documentos semanticamente inadequados (peça 103, p. 9), 33,33% de documentos de imóvel de tipo inadequado (peça 105, p. 7), 53,55% de divergências críticas de área (peça 109, p. 7) e 68,7% de arquivos com resolução inferior a 300 DPI (peça 106, p. 7), situação que reduz a capacidade do cadastro de atestar a elegibilidade dos beneficiários e pode comprometer a focalização das políticas públicas que dele dependem.

### {SS} Governança da qualidade dos dados de entrada do CAF

25. A documentação comprobatória ocupa posição central no desenho do CAF. Como o cadastro é autodeclaratório e funciona como instrumento oficial de identificação e qualificação da agricultura familiar, sua confiabilidade depende de que a documentação anexada permita demonstrar vínculo com a terra, renda compatível e aderência aos critérios legais. Essa centralidade é reforçada pelo Manual de Crédito Rural do Banco Central, segundo o qual o CAF válido é documento suficiente para comprovar o vínculo do beneficiário com a terra e com a atividade produtiva para fins de Pronaf, dispensando inclusive registro em cartório²¹. A análise do contraditório recomenda distinguir o passivo acumulado do fluxo corrente: a base ativa reúne registros produzidos sob diferentes marcos normativos e tecnológicos, e o CAF 3.0 já trouxe avanços. Ainda assim, esse passivo continua ativo e apto a influenciar decisões correntes.

26. À luz do DAMA-DMBOK v2, a qualidade dos dados de entrada deve ser tratada como atributo governado ao longo de todo o ciclo de vida, com controles preventivos, padrões, métricas e monitoramento voltados a assegurar que os dados sejam adequados ao uso pretendido (peça 86, p. 16 e 38). No contexto deste achado, esse referencial permite organizar a análise em dimensões complementares de validação semântica, aderência tipo-documental, consistência e acurácia dos dados críticos, qualidade técnica de ingestão, ciclo de vida e monitoramento contínuo. O objetivo, aqui, é apenas tornar visível onde o CAF já possui controles e onde ainda opera abaixo do nível exigido para a escala da base.

27. Para traduzir essas constatações em linguagem operacional, a equipe adota quadro sintético de maturidade inspirado no DAMA-DMBOK e em escala adaptada de 0 a 5: 0 = ad-hoc; 1 = inicial; 2 = repetível; 3 = definido; 4 = gerenciado; 5 = otimizado. A escala é usada apenas como instrumento analítico para situar o estágio observado em cada dimensão do controle de qualidade dos dados de entrada.

#### {SSS} Diagnóstico por dimensão de qualidade

##### Dimensão 1 — Validação semântica e aderência tipo-documental

28. Foi nesse contexto que surgiu o conflito entre o que o cadastro deveria assegurar e o que de fato assegura. A regra de negócio RN1.17 estabelece que, para cada área cadastrada, deve ser anexado obrigatoriamente documento comprobatório (peça 78, p. 5), mas essa exigência opera no plano da presença do arquivo, não no plano da verificação de seu conteúdo. As validações automatizadas RN1.29 e RN1.30, por sua vez, consultam bases externas da Dataprev e ajudam a testar dados declarados, sem examinar o teor do documento anexado (peça 78, p. 7). Na dimensão semântica, a amostra probabilística de 646 documentos (peça 103, p. 9) mostrou que 27,1% dos arquivos apresentados não comprovam aquilo que declaram comprovar. A inadequação concentra-se nos grupos mais sensíveis à elegibilidade: 37,0% dos documentos de imóvel rural e 30,5% dos documentos de renda (peça 103, p. 10-11).

29. A equipe encontrou, por exemplo, documentos de identidade classificados como prova de posse ou propriedade, notas fiscais de despesa usadas como comprovação de receita, selfies classificadas como comprovante de renda e páginas em branco ou ilegíveis aceitas pelo sistema (peça 103, p. 12-15). A projeção dessa taxa para a população de 11.377.318 documentos indica aproximadamente 3,08 milhões de documentos nessa condição (peça 140, p. 5), ordem de grandeza que não equivale, por si, a inelegibilidade definitiva do beneficiário, mas evidencia incapacidade estrutural do cadastro de provar aquilo que afirma registrar.

30. A comparação interna reforça esse diagnóstico: as Declarações de Veracidade, emitidas em formato padronizado pelo sistema, apresentaram inadequação de apenas 4,9% (peça 103, p. 10). Na mesma linha, a constatação de que 33,33% dos documentos de imóvel analisados são de tipo inadequado para comprovação de propriedade ou posse (peça 105, p. 7) mostra desalinhamento com o art. 8º, I, c, da Portaria MDA 19/2025. Em termos de maturidade, a prática observada é **Inicial (1)**: há exigência documental e há atuação manual da rede emissora, mas o controle ainda não é repetível nem escalável em patamar compatível com a base.

**Tabela 1** — Inadequação semântica por tipo de documento

| Tipo de documento | Analisados | Plenamente adequados | Parcialmente adequados | Inadequados | % inadequação (P + I) |
|---|---:|---:|---:|---:|---:|
| Imóvel rural | 227 | 143 | 19 | 65 | 37,0% |
| Renda | 276 | 192 | 14 | 70 | 30,5% |
| Declarações de Veracidade | 143 | 136 | 5 | 2 | 4,9% |
| Total | 646 | 471 | 38 | 137 | 27,1% |

*Fonte: elaboração da equipe de auditoria com base na peça 103, p. 9-10. Amostra probabilística estratificada (n=646, IC 99%, margem de erro ±4,5 p.p.).*

##### Dimensão 2 — Consistência e acurácia dos dados de área

31. A segunda frente do conflito apareceu nos documentos de imóvel com área válida identificável. Nesse universo específico, distinto do conjunto que gerou a taxa de 27,1%, 53,55% dos casos apresentaram divergência crítica superior a 10% entre a área extraída do documento digitalizado e a área registrada na base (peça 109, p. 7), com projeção de aproximadamente 1,44 milhão de documentos com inconsistência relevante. Os percentuais não medem o mesmo fenômeno: o primeiro mede inadequação semântica da documentação em geral; o segundo, inconsistência de área em documentos de imóvel comparáveis. Aqui, a evidência não aponta erro casual: a divergência agregada foi de +120,89%, pois os documentos somavam 3.827,65 hectares, enquanto a base registrava 1.732,85 hectares para os mesmos imóveis (peça 109, p. 9).

32. A peça 141 já havia ilustrado a situação ao mostrar caso em que o sistema registrava 1,5 hectare, enquanto o documento apontava 5,0 hectares. O padrão sugere causas estruturais, como conversão inadequada entre alqueires e hectares, registro de área útil em vez de área total ou desatualização documental. Também sugere lacuna de controle na entrada: não há cruzamento sistemático entre a área declarada no formulário e a área constante do documento digitalizado, nem interoperabilidade madura com bases oficiais como Sigef e Sicar no momento do cadastramento. Em termos de maturidade, trata-se de prática **Ad-hoc (0)**: o sistema admite dado crítico de alta materialidade sem verificação cruzada automatizada compatível com o risco.

**Tabela 2** — Divergências de área por faixa de magnitude

| Faixa de divergência | Casos | % do total | Projeção populacional |
|---|---:|---:|---:|
| 0-5% (tolerável) | 70 | 45,16% | 1.181.370 |
| 5-10% (moderada) | 2 | 1,29% | 33.753 |
| 10-50% (crítica) | 15 | 9,68% | 253.151 |
| >50% (muito crítica) | 68 | 43,87% | 1.147.617 |
| Total analisado | 155 | 100,0% | 2.615.891 |

*Fonte: elaboração da equipe de auditoria com base na peça 109, p. 9. Subamostra de documentos de imóvel com área válida identificável (n=155).*

##### Dimensão 3 — Qualidade técnica de ingestão documental

33. A terceira dimensão do diagnóstico recai sobre a qualidade técnica da ingestão. A análise incidental da digitalização mostrou que 68,7% dos documentos examinados estavam abaixo de 300 DPI e 12,2% em condição crítica de legibilidade (peça 106, p. 7). O parâmetro do Conarq deve ser lido como referência orientativa de boa prática, não como critério cogente de invalidação automática²²; ainda assim, ele é relevante porque a própria peça 106 o utiliza como padrão técnico para documentos textuais destinados a OCR. O ponto central não é invalidar retroativamente cada arquivo abaixo desse patamar, mas reconhecer que o sistema não estabeleceu requisitos mínimos de resolução, formato e legibilidade em função da finalidade do acervo.

34. Em uma base com vocação para suporte probatório e uso progressivo de automação, essa ausência de política formal de ingestão ajuda a explicar por que o cadastro incorporou arquivos tecnicamente pouco tratáveis. O impacto é duplo: dificulta a extração automatizada de conteúdo e enfraquece a auditabilidade futura do acervo. Sob a ótica de maturidade, a situação é **Inicial (1)**.

##### Dimensão 4 — Monitoramento contínuo, ciclo de vida e data stewardship

35. A quarta dimensão torna visível problema que, no texto corrido anterior, aparecia diluído nas causas (§§19-20) e nos fatores contribuintes (§20). O DAMA-DMBOK trata a qualidade de dados como programa permanente, com procedimentos, métricas, monitoramento e papéis explícitos de stewardship ao longo do ciclo de vida (peça 86, p. 16 e 38). Foi justamente nesse ponto que o CAF revelou a lacuna mais estrutural.

36. O passivo herdado das transições DAP, CAF 2.0 e CAF 3.0 permaneceu ativo sem curadoria estruturada do estoque migrado (peça 74, p. 4), e a equipe não identificou evidência de métricas contínuas de qualidade documental, painéis gerenciais de acompanhamento ou responsabilidades de curadoria claramente formalizadas para saneamento progressivo do acervo. A própria ordem de grandeza do problema recomenda essa leitura: sem correções sistêmicas, e considerando a taxa aproximada de crescimento de 3,5% ao mês da base documental, o estoque problemático tende a crescer e encarecer a remediação posterior (peça 140; peça 141, §62).

37. O monitoramento amostral do gestor, que apontou conformidade integral de 32% (peça 150, p. 22), é relevante como indício de resposta institucional em construção, mas também evidencia que a convergência simultânea dos requisitos ainda permanece baixa; além disso, por ser dado produzido pelo gestor, não foi auditado pela equipe. Em termos de maturidade, a situação é **Ad-hoc (0)**.

**Quadro 3** — Maturidade da governança dos dados de entrada

| Dimensão | Prática observada | Nível |
|---|---|---|
| Validação semântica | Exigência documental e verificação manual pela rede emissora, sem validação semântica automatizada escalável | Inicial (1) |
| Aderência tipo-documental | O sistema exige anexo, mas não bloqueia de forma consistente tipos inadequados para a finalidade declarada | Inicial (1) |
| Consistência e acurácia de área | Não há verificação cruzada automatizada entre documento, formulário e bases oficiais relevantes | Ad-hoc (0) |
| Qualidade técnica de ingestão | Processo de upload existente, sem política formal de resolução, legibilidade e tratabilidade | Inicial (1) |
| Ciclo de vida dos dados | Passivo herdado das transições permanece ativo sem curadoria estruturada do estoque migrado | Ad-hoc (0) |
| Monitoramento contínuo | Ausência de métricas formais e rotina gerencial contínua de acompanhamento da qualidade documental | Ad-hoc (0) |
| Data stewardship | Responsabilidades de curadoria e saneamento não aparecem formalizadas de modo suficiente para a escala da base | Ad-hoc (0) |
| **Média aritmética** | Estágio intermediário entre práticas reativas e primeiros controles estruturados | **0,43** |

*Escala adaptada pela equipe com base no DAMA-DMBOK v2, Cap. 13, e em modelo sintético de maturidade processual inspirado no CMMI-DMM: 0 = Ad-hoc (sem processo formal); 1 = Inicial (processo existente, não repetível); 2 = Repetível; 3 = Definido; 4 = Gerenciado; 5 = Otimizado. Trata-se de escala analítica adaptada, não de aplicação literal da taxonomia do DAMA-DMBOK, que utiliza nomenclatura e faixas próprias.*

*Fonte: elaboração da equipe de auditoria com base nas peças 78, 86, 103, 105, 106, 109, 140, 150 e 74.*

### {SS} Efeitos potenciais

38. Essas distorções são relevantes porque o CAF foi instituído justamente para identificar e qualificar o público da agricultura familiar. Quando cerca de 3,08 milhões de documentos (peça 140, p. 3-4) não permitem comprovar, com base na documentação anexada, o cumprimento dos requisitos legais, surge o primeiro efeito potencial do achado: o cadastro pode deixar de confirmar documentalmente a elegibilidade de parcela expressiva da base. Esse efeito deve ser lido com a cautela registrada no contraditório: inconsistência cadastral não se converte automaticamente em inelegibilidade definitiva, nem em concessão indevida, porque as políticas usuárias possuem filtros próprios.

39. Ainda assim, a limitação é material, sobretudo porque, no caso do Pronaf, o próprio CAF opera como prova suficiente do vínculo do beneficiário com a terra e com a atividade produtiva. O segundo efeito potencial decorre da dimensão área: se cerca de 1,44 milhão de documentos de imóvel têm divergência crítica superior a 10% (peça 109, p. 7), o dado cadastral deixa de oferecer base confiável para validação do limite de 4 módulos fiscais, planejamento e monitoramento das políticas.

40. O terceiro efeito potencial reside na obstrução técnica à automação e à auditabilidade do acervo. Um cadastro com 11,4 milhões de documentos não pode depender indefinidamente de verificação manual, mas a baixa qualidade de digitalização reduz a viabilidade de OCR e de validação semântica automatizada para o subconjunto mais problemático.

41. O quarto efeito potencial é o risco de que programas que usam o CAF como habilitação prévia possam vir a direcionar recursos a beneficiários cuja elegibilidade não possa ser comprovada documentalmente. Também aqui a formulação exige contenção: não se está afirmando desvio consumado de finalidade nem dano ao erário. Registra-se apenas que, se a documentação aceita pelo cadastro não sustenta a elegibilidade, a segurança do sistema de habilitação prévia fica reduzida e passa a depender, em maior medida, da efetividade das camadas complementares de controle mencionadas pelo gestor. Por isso, os quatro efeitos são apresentados como potenciais, e não como eventos consumados.

### {SS} Causas

42. O exame das causas mostra que a distorção não nasceu de um único ponto de falha, mas de um encadeamento de fragilidades de processo e produto. A primeira é o desenho da própria ingestão documental: a regra de negócio RN1.17 exige anexação, mas não verifica se o arquivo anexado corresponde semanticamente à categoria escolhida (peça 78, p. 5). Em termos simples, o sistema foi desenhado para aceitar, não para verificar. As validações automatizadas existentes (RN1.29 e RN1.30) consultam bases externas da Dataprev e ajudam a testar dados declarados, mas não examinam o teor do documento anexado (peça 78, p. 7). A segunda causa está na ausência de validação consistente dos dados de área na entrada. Não há cruzamento sistemático entre a área declarada no formulário e a área constante do documento digitalizado, nem interoperabilidade madura com bases georreferenciadas como Sigef e Sicar no momento do cadastramento, com cruzamentos com Sicar planejados apenas "futuramente" (peça 72, p. 2).

43. A terceira é a inexistência de requisitos mínimos de resolução, formato e legibilidade para o upload documental, o que ajuda a explicar por que o sistema incorporou arquivos tecnicamente pouco tratáveis. A quarta é o passivo herdado das transições DAP, CAF 2.0 e CAF 3.0 sem curadoria estruturada do estoque migrado (peça 74, p. 4).

44. Esse encadeamento ajuda a entender por que o problema persiste mesmo em ambiente que já conta com algumas camadas de controle.

45. Há, ainda, fatores contribuintes que recomendam calibragem, mas não afastam o achado. Entre eles estão a heterogeneidade da rede emissora e do público atendido, o contexto de restrições de TIC, a reconstrução institucional do MDA e o enfrentamento gradual já em curso, materializado no TED DCAF/UFES para 2025-2027 (peça 150, p. 27), na renovação prevista de cerca de 742 mil registros em 2026 (peça 150, p. 29) e no monitoramento amostral conduzido pelo gestor. Esses elementos afastam leitura de inércia administrativa e explicam por que a resposta institucional deve respeitar risco e capacidade de implementação. Não eliminam, porém, a reincidência do problema. Desde o Acórdão 1197/2018, o Tribunal já apontava a necessidade de incorporar salvaguardas de qualidade ao sistema que sucederia a DAP, e os monitoramentos posteriores registraram cumprimento ainda incompleto.

### {SS} Contexto do gestor e avanços reconhecidos

46. O contraditório também evidenciou que o problema precisa ser lido à luz da escala e da heterogeneidade operacional do CAF. A base ativa reúne cerca de 3,3 milhões de unidades familiares, 3,2 milhões de imóveis georreferenciados e 11,4 milhões de documentos comprobatórios digitalizados, produzidos por públicos diversos e por rede emissora ampla e descentralizada. Essa escala ajuda a explicar por que a solução não pode ser formulada como saneamento cego e massivo, mas por risco, criticidade e capacidade de implementação.

47. Também merece registro que o CAF 3.0 já apresentou avanços: as Declarações de Veracidade emitidas em formato padronizado tiveram inadequação de apenas 5,6% (peça 103, p. 10), e 98,7% das propriedades que excedem 4 módulos fiscais são anteriores ao CAF 3.0 (peça 107, p. 12), o que sugere melhora do fluxo corrente sem retroação automática sobre o passivo. A resposta institucional já em curso (TED DCAF/UFES 2025-2027, renovação prevista de cerca de 742 mil registros em 2026 e monitoramento amostral próprio) confirma cenário de maturação gradual.

### {SS} Boas práticas

48. No que se refere a boas práticas, a equipe não identificou, no escopo deste achado, experiência que atendesse cumulativamente aos requisitos da NAT §160 para ser formalmente qualificada nessa condição. O que se verificou foram avanços parciais relevantes, como a melhora do CAF 3.0 na contenção de novos casos críticos, a superior conformidade das Declarações de Veracidade padronizadas e o monitoramento próprio por amostra probabilística, que apontou conformidade integral de 32% (peça 150, p. 22), dado produzido pelo gestor e não auditado pela equipe. Esses avanços qualificam o tom do relatório, mas não convertem o quadro em referência replicável a outros órgãos.

### {SS} Propostas de encaminhamento

49. Daí decorrem os encaminhamentos. O primeiro é a determinação para que o MDA, em 180 dias, apresente plano de ação com responsáveis, prazos e forma de comunicação do cumprimento, destinado a avaliar as situações identificadas e, uma vez confirmadas, promover seu saneamento no âmbito dos dados de entrada, em alinhamento com os critérios de elegibilidade e com a finalidade legal do CAF.

50. No plano das recomendações, a resposta deve começar pela prevenção: assegurar que os processos de cadastramento e atualização produzam dados com qualidade suficiente e impeçam a inserção e a permanência de dados inválidos; garantir integridade e consistência dos dados críticos; e estabelecer requisitos mínimos de qualidade técnica para os documentos digitalizados. Complementarmente, interoperabilidade com bases oficiais relevantes, gestão de mudanças e monitoramento contínuo formam o ambiente necessário para que a correção não se limite ao estoque atual, mas previna regressões futuras. Todos esses encaminhamentos foram formulados como resultados a alcançar, e não como prescrição fechada de solução.

**Quadro 4** — Síntese do Achado 01

| Componente | Síntese |
|---|---|
| Situação encontrada | 27,1% de documentos semanticamente inadequados; 33,33% de tipo documental inadequado; 53,55% de divergência crítica de área; 68,7% de documentos com resolução inferior a 300 DPI |
| Critério | Art. 3º da Lei 11.326/2006; art. 4º do Decreto 9.064/2017; arts. 8º e 22 da Portaria MDA 19/2025 |
| Efeitos potenciais | Redução da capacidade de confirmação documental da elegibilidade; baixa confiabilidade dos dados de área; obstrução à automação e à auditabilidade; risco de direcionamento de recursos a elegibilidade não comprovável |
| Causas principais | Ingestão desenhada para aceitar arquivos sem validar conteúdo; ausência de controles de consistência de área; falta de requisitos mínimos de digitalização; passivo herdado das transições DAP/CAF 2.0/CAF 3.0 |
| Propostas associadas | Plano de ação em 180 dias; prevenção na entrada; integridade dos dados críticos; requisitos mínimos de qualidade técnica; medidas complementares de interoperabilidade, gestão de mudanças e monitoramento |

*Fonte: elaboração da equipe de auditoria com base na Matriz de Achados do CAF e nas peças 103, 106, 109, 140 e 150.*

### {SS} Benefícios esperados

51. Os benefícios esperados são proporcionais ao problema e devem ser lidos como recuperação de capacidade institucional. Em termos quantitativos, espera-se reduzir a taxa de inadequação semântica hoje estimada em 27,1%, diminuir a incidência de divergências críticas de área hoje em 53,55%, elevar a proporção de documentos com resolução igual ou superior a 300 DPI, atualmente restrita a 31,3% do acervo (peça 106, p. 7), e ampliar a conformidade integral dos registros para patamar superior aos 32% observados no monitoramento próprio do gestor (peça 150, p. 22).

52. Em termos qualitativos, o ganho principal é recolocar o CAF em condição mais segura para atestar documentalmente a elegibilidade dos beneficiários, melhorar a confiabilidade dos dados de área, viabilizar o uso progressivo de automação e reforçar a auditabilidade do acervo. Para a sociedade, isso significa elevar a probabilidade de que políticas como Pronaf, PAA e PNAE cheguem ao público da agricultura familiar com base em cadastro mais confiável e verificável.

---

## Notas de Fim (Apêndice VI)

²¹ BANCO CENTRAL DO BRASIL. *Manual de Crédito Rural*. Brasília: BCB. Referência utilizada na peça 137, p. 156 e 166.

²² BRASIL. Conselho Nacional de Arquivos. Resolução Conarq nº 31, de 28 de abril de 2010. Rio de Janeiro: Conarq, 2010. Referência utilizada na peça 79, p. 20.
