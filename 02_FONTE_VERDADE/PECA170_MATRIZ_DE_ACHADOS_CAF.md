# Matriz de Achados — TC 011.073/2025-0

**OBJETO:** Cadastro Nacional da Agricultura Familiar — CAF, sob gestão do Ministério do Desenvolvimento Agrário e Agricultura Familiar (MDA)

**OBJETIVO(S):** Avaliar se os mecanismos de verificação de dados do CAF (versão 3, período: março de 2025 a agosto de 2025) asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio, considerando-se como critérios a Lei 11.326/2006, a Portaria MDA 19/2025, a Portaria MDA 20/2023, no que se refere às condições e aos procedimentos gerais de inscrição no CAF, e a Portaria MDA 20/2025, no que se refere ao ingresso na rede das entidades credenciadas para realizar inscrições, além da norma ISO/IEC 25012:2008, do framework DAMA-DMBOK v2 e dos princípios da Administração Pública; e avaliar se a estrutura de governança e gestão de dados aplicada ao CAF assegura padrões claros, papéis definidos, rastreabilidade e integridade das informações ao longo de todo o ciclo de vida dos dados.

---

## ACH-01 — Insuficiência dos mecanismos de validação e da documentação comprobatória

**Frase-síntese:**

Devido à insuficiência dos mecanismos de validação semântica e de consistência na ingestão documental do CAF, **ocorreu** a aceitação e permanência de documentos comprobatórios inadequados em escala expressiva — 27,1% semanticamente inadequados e 53,55% com divergência crítica de área, em dimensões distintas e complementares da base documental —, em desacordo com os critérios de elegibilidade do art. 3º da Lei nº 11.326/2006 e com os requisitos documentais do art. 8º da Portaria MDA nº 19/2025, **o que levou** à redução da capacidade do cadastro de atestar a elegibilidade dos cadastrados, **impactando** a confiabilidade do CAF como instrumento de habilitação prévia para políticas públicas de agricultura familiar.

---

### Situação Encontrada

A auditoria identificou limitações nos mecanismos de validação que reduzem a capacidade do CAF de atestar a elegibilidade dos cadastrados com base em documentação comprobatória. O modelo de verificação do CAF envolve múltiplas camadas — atuação da rede emissora, regras sistêmicas e possibilidade de monitoramento posterior (peça 150, p. 24-26) —, e o diagnóstico não afirma ausência absoluta de controles, mas insuficiência dos mecanismos existentes para assegurar integridade documental em escala compatível com o volume do cadastro. As constatações abrangem quatro dimensões complementares, cada uma medindo universo distinto da base documental. A análise da equipe considerou os argumentos apresentados pelo gestor (peça 150) e a contestação específica de peças de trabalho (peças 153, 157, 158, 163, 166), cujas análises constam do Anexo — Análise dos Comentários dos Gestores.

**Dimensão 1 — Adequação semântica dos documentos comprobatórios.** A análise de amostra estratificada de 646 documentos, selecionados por amostragem aleatória estratificada com intervalo de confiança de 99% e margem de erro de ±4,5 pontos percentuais, revelou que 27,1% dos documentos apresentados são semanticamente inadequados, ou seja, não comprovam efetivamente os requisitos legais que declaram comprovar (peça 103, p. 9). A inadequação concentra-se nas categorias mais sensíveis para determinação de elegibilidade: 36,6% dos documentos de imóvel rural e 30,4% dos documentos de renda são inadequados (peça 103, p. 10-11). Os tipos de inadequação identificados incluem documentos de identidade ou comprovantes de residência anexados na categoria "documentos de imóvel rural", notas fiscais de despesa apresentadas como comprovação de receita, selfies sem valor probatório e arquivos em branco salvos como PDF (peça 103, p. 12-14). As Declarações de Veracidade — documentos padronizados emitidos pelo próprio sistema — apresentam taxa de inadequação de apenas 5,6%, demonstrando que documentos estruturados têm conformidade significativamente superior a documentos de livre apresentação (peça 103, p. 10). Projetando-se a taxa de 27,1% para a população total de 11.377.318 documentos cadastrados no CAF, estima-se aproximadamente 3,08 milhões de documentos nessa condição, com intervalo de confiança de 99% compreendendo de 2,57 a 3,60 milhões (peça 140, p. 5, Tabela "Valores Oficiais para o Relatório de Auditoria").

A base reúne registros produzidos sob diferentes contextos normativos e tecnológicos (DAP, CAF 2.0 e CAF 3.0), e a heterogeneidade temporal recomenda cautela na leitura e priorização do saneamento (ARG-01). As projeções são relevantes como ordem de grandeza do problema e para justificar a necessidade de avaliação estruturada, sem que se pretenda equiparar automaticamente cada inconsistência documental a inelegibilidade definitiva do cadastrado (ARG-02). O CAF é instrumento de identificação e qualificação, e o problema recai sobre a capacidade do cadastro de comprovar e sustentar a elegibilidade — não sobre decisão final de concessão em cada política pública. A esse respeito, registre-se que o Manual de Crédito Rural do Banco Central estabelece que o CAF válido é documento suficiente para comprovar o vínculo do beneficiário com a terra e com a atividade produtiva para fins de contratação de financiamento do Pronaf (peça 137, p. 166), dispensando inclusive registro em cartório da documentação pertinente (peça 137, p. 156).

**Dimensão 2 — Consistência de área dos documentos de imóvel.** A análise de 155 documentos de imóveis rurais com área válida identificável — de uma amostra aleatória de 201 documentos, com nível de confiança de 95% e margem de erro de ±6,44 pontos percentuais (peça 109, p. 4) — revelou que 53,55% apresentam divergências críticas superiores a 10% entre a área extraída do documento digitalizado e a área registrada na base de dados (peça 109, p. 7). As divergências não se distribuem simetricamente: a análise agregada revelou divergência sistemática de +120,89%, com os documentos indicando área total de 3.827,65 hectares enquanto a base registra apenas 1.732,85 hectares para os mesmos imóveis (peça 109, p. 9). Esse padrão sistemático não é compatível com erros aleatórios de digitação — que produziriam divergências com tendência à compensação estatística — e sugere causas estruturais como erro de conversão de unidades alqueires/hectares, registro de área útil quando o documento apresenta área total, ou desatualização entre documentos e dados cadastrados (peça 109, p. 9-10). Projetando-se para a população estimada de 2,62 milhões de documentos de imóveis com área válida — correspondente a 77,1% dos 3.392.881 documentos de imóveis cadastrados (peça 109, p. 7) —, estima-se aproximadamente 1,44 milhão de documentos com divergências significativas (cálculo: 53,55% × 2,62M; peça 109, p. 7).

As métricas das Dimensões 1 e 2 não se contradizem e não devem ser comparadas como se medissem o mesmo fenômeno: a taxa de 27,1% mede inadequação semântica da documentação em geral (todos os tipos documentais); a taxa de 53,55% mede inconsistência de área especificamente em documentos de imóvel com área válida identificável. Tratam de universos distintos e complementares.

**Dimensão 3 — Tipo documental.** A análise identificou que 33,33% dos documentos de imóveis rurais analisados são de tipo inadequado para comprovação de propriedade ou posse de terra (peça 105, p. 7), não correspondendo aos tipos documentais especificados no art. 8º, I, c, da Portaria MDA nº 19/2025 (peça 108, p. 5). Projetando-se para a população de 3.392.881 documentos de imóveis (peça 109, p. 7), estima-se 1,13 milhão de documentos em desconformidade com as regras da Portaria (cálculo: 33,33% × 3.392.881). Registre-se que o gestor questionou a aderência da peça 105 (peça 166, p. 1), e a contestação foi analisada no Anexo de Comentários (ARG-13 e ARG-14). A verificação dessa peça específica não desloca o diagnóstico central do achado, sustentado pela convergência dos demais papéis de trabalho — especialmente a peça 109 (divergência de área) e a peça 103 (inadequação semântica). O gestor apresentou reanálise indicando que 64% dos casos seriam conformes à sua leitura normativa (peça 166, p. 2); registra-se a controvérsia, observando-se a diferença metodológica entre inferência amostral da auditoria e rechecagem dirigida do gestor (ARG-14).

**Dimensão 4 — Qualidade técnica de digitalização.** A equipe identificou que 68,7% dos documentos digitalizados (444 de 646 analisados) apresentam resolução inferior a 300 DPI, sendo 12,2% em nível crítico com texto borrado (peça 106, p. 7). O parâmetro de 300 DPI da Resolução Conarq nº 31/2010 (peça 79, p. 20, Tabela 1) é utilizado como referência orientativa de boa prática para documentos textuais destinados a OCR, não como critério normativo vinculante (ARG-10). A constatação indica limitação técnica na qualidade de ingestão, sem implicar invalidação automática dos documentos abaixo desse patamar. Essa limitação, contudo, dificulta a implementação futura de validação automatizada por OCR, reduz a confiabilidade da extração automatizada de valores numéricos de área e limita a auditabilidade futura do acervo documental (peça 106, p. 9 e 15).

**Contexto temporal e distinção passivo/corrente.** A base ativa do CAF, no período de março a agosto de 2025, compreende documentos produzidos sob diferentes contextos normativos e tecnológicos (DAP, CAF 2.0 e CAF 3.0). O fato de 98,7% das propriedades que excedem 4 módulos fiscais terem sido cadastradas antes do CAF 3.0 (peça 107, p. 12) indica que os controles da versão atual reduziram — embora não tenham eliminado — o cadastramento de propriedades inelegíveis. O gestor apresentou elementos concretos de enfrentamento gradual do passivo: Plano de Formação via TED DCAF/UFES para o período 2025-2027 (peça 150, p. 27) e vencimento previsto de cerca de 742 mil registros em 2026, que ensejará renovação cadastral com reapresentação documental (peça 150, p. 29). Esses elementos afastam leitura de inércia administrativa e contextualizam o prazo da resposta institucional, sem dispensar o aprimoramento dos mecanismos de validação.

Registre-se, ainda, que o próprio monitoramento realizado pelo gestor no segundo semestre de 2024, com amostra probabilística estratificada por unidade da federação, alcançou índice de conformidade integral — parcela da amostra em que todos os quesitos verificados foram simultaneamente atendidos — de 32% (peça 150, p. 22). Embora os níveis individuais por quesito tenham registrado média em torno de 75%, a convergência simultânea de todos os requisitos permanece baixa. Esse dado, produzido pelo gestor e não auditado pela equipe, corrobora a ordem de grandeza do problema e reforça a necessidade de resposta institucional estruturada, organizada por risco e materialidade (ARG-09).

---

### Critérios da Situação Encontrada

**C1. Lei nº 11.326/2006, art. 3º, incisos I a IV** (peça 80, p. 1) — Estabelece os requisitos cumulativos para caracterização de agricultor familiar e empreendedor familiar rural, incluindo limite de área de 4 módulos fiscais (inciso I), uso predominante de mão-de-obra familiar (inciso II), percentual mínimo de renda do estabelecimento (inciso III) e direção familiar do empreendimento (inciso IV). **Aplicação:** o CAF existe para atestar o cumprimento desses requisitos; se os mecanismos de validação são insuficientes para comprovar que os cadastrados os atendem, a função primordial do cadastro fica limitada.

**C2. Decreto nº 9.064/2017, art. 4º** (peça 81) — Institui o CAF como instrumento de identificação e qualificação da agricultura familiar. **Aplicação:** define a finalidade institucional do cadastro — identificar e qualificar —, contra a qual se mede a suficiência dos mecanismos de validação.

**C3. Portaria MDA nº 19/2025, arts. 8º e 22** (peça 108, p. 5) — Operacionaliza a validação documental especificando os tipos documentais obrigatórios para inscrição no CAF (documento de identificação, comprovante de residência, documentação de propriedade ou posse, documentação de renda) e estabelece requisitos para validação dos dados declarados. **Aplicação:** define os requisitos documentais de entrada contra os quais se confronta a situação encontrada. A adequação documental pode, em casos individuais, exigir leitura do regime normativo vigente quando o cadastro foi emitido (ARG-08).

**C4. DAMA-DMBOK v2** (peça 86, p. 38 — prevenção na entrada; p. 16 — custo de corrigir) — Referencial técnico de governança de qualidade de dados adotado na Matriz de Planejamento desta auditoria. Estabelece que controles preventivos na entrada de dados são mais eficazes e economicamente viáveis do que inspeção e correção posterior. **Aplicação:** fundamenta a tese de que a prevenção na entrada é preferível à correção retroativa do passivo — exatamente o cenário documentado no achado (ARG-07). O modelo de verificação do CAF envolve camadas complementares (rede emissora, regras sistêmicas, monitoramento), e o diagnóstico não nega essas camadas; sustenta que a validação na entrada é insuficiente para a escala do cadastro. **Ancoragem jurisprudencial:** o DAMA-DMBOK v2 foi expressamente adotado como critério de auditoria pelo Acórdão 457/2026-TCU-Plenário (unanimidade), com 7 referências ao framework na fundamentação, inclusive para aferir maturidade de governança de dados em órgãos federais.

**C5. Acórdão 906/2009-TCU-Plenário** — Consolida tese do TCU de que a validação de dados na entrada é obrigação do gestor de bases de dados administrativas. **Aplicação:** ancora a responsabilidade do MDA de assegurar qualidade no momento da ingestão, não apenas na guarda posterior.

**C6. Acórdãos 1197/2018-TCU-Plenário → 1866/2021-TCU-Plenário → 885/2024-TCU-Plenário** — Cadeia de deliberações sobre o antigo sistema DAP/CAF: o item 9.2.6 do Ac. 1197/2018 determinou que o CAF incorporasse salvaguardas de qualidade de dados. Após três monitoramentos, os itens 9.2.2, 9.2.6 e 9.3 permanecem pendentes de cumprimento integral. Ficou consignado em ata, na reunião de trabalho de 07/10/2025, por consenso entre equipe e gestor, que o sistema carece de mecanismos automatizados de validação (peça 73, p. 3). Na reunião de encerramento, a conclusão formal registrou que muitos dos problemas identificados se originam do legado do CAF 2.0, sistema anterior que não possuía validações robustas (peça 74, p. 4). **Aplicação:** demonstra que os problemas não são inéditos — há reincidência — e que deliberações anteriores permanecem sem cumprimento integral.

**C7. ISO/IEC 25012:2008** (peça 85) — Define dimensões de qualidade de dados: completude, acurácia, consistência, credibilidade, atualidade. **Aplicação:** complementa o DAMA-DMBOK como referencial técnico para aferir a qualidade dos dados de entrada. Utilizado como critério secundário, não como critério primário isolado.

**C8. Resolução Conarq nº 31/2010** (peça 79, p. 20, Tabela 1) — Recomenda resolução mínima de 300 DPI para documentos textuais destinados a OCR. **Aplicação:** parâmetro técnico **orientativo** (não cogente) utilizado como benchmark de boa prática (ARG-10). A constatação indica limitação na qualidade de ingestão, não descumprimento de norma vinculante.

---

### Evidências da Situação Encontrada

**Evidências analíticas (bases de dados e scripts):**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E1 | 103 | p. 5 | Relatório de análise semântica documental — metodologia (Claude Vision AI, validação cruzada >95% de concordância) | Metodologia da Dimensão 1 |
| E2 | 103 | p. 9 | Taxa de 27,1% de inadequação semântica (amostra de 646 docs, IC 99%, ±4,5 p.p.) | Dimensão 1 — taxa geral |
| E3 | 103 | p. 10-11 | Desagregação por categoria: 36,6% imóvel, 30,4% renda, 5,6% Declarações de Veracidade | Dimensão 1 — concentração e benchmark interno |
| E4 | 103 | p. 12-14 | Exemplos de inadequação: RG como "documento de imóvel", NF de despesa como "renda", selfies, PDFs em branco | Dimensão 1 — tipologia das inadequações |
| E5 | 109 | p. 4 | Metodologia de análise de área (155 docs com área válida, IC 95%, ±6,44 p.p.) | Metodologia da Dimensão 2 |
| E6 | 109 | p. 7 | Taxa de 53,55% de divergências críticas >10%; 77,1% dos docs de imóvel com área identificável | Dimensão 2 — taxa de divergência |
| E7 | 109 | p. 9 | Divergência agregada de +120,89% (3.827,65 ha nos docs vs. 1.732,85 ha na base) | Dimensão 2 — viés sistemático |
| E8 | 109 | p. 9-10 | Análise de causas estruturais: conversão alqueires/hectares, área útil vs. total, desatualização | Dimensão 2 — padrão não aleatório |
| E9 | 105 | p. 7 | Taxa de 33,33% de documentos de imóvel com tipo inadequado para comprovação de posse/propriedade. **Nota:** peça contestada pelo gestor (peça 166, p. 1); análise da contestação no Anexo CG, ARG-13 e ARG-14. O indicador central de divergência de área (53,55%, peça 109) permanece íntegro. | Dimensão 3 — tipo documental (com ressalva) |
| E10 | 106 | p. 7 | Taxa de 68,7% de documentos com resolução inferior a 300 DPI (444 de 646), sendo 12,2% em nível crítico | Dimensão 4 — qualidade de digitalização |
| E11 | 106 | p. 9 | Impacto da baixa resolução nas três frentes de validação | Dimensão 4 — limitação transversal |
| E12 | 106 | p. 15 | Limitação à implementação de OCR e validação semântica automatizada | Dimensão 4 — viabilidade de automação futura |
| E13 | 140 | p. 5 | Projeções estatísticas: 3,08M docs inadequados (IC 99%, 2,57M-3,60M); população de 11.377.318 docs | Projeção populacional — Dimensão 1 |

**Evidências documentais (normas e regras de negócio):**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E14 | 78 | p. 5 | Regra de Negócio RN1.17 — exige anexação de documentos, sem verificação de conteúdo semântico | Mecanismo de ingestão: apenas anexação |
| E15 | 78 | p. 7 | Regras de Negócio RN1.29-30 — validações automatizadas consultam bases Dataprev, não conteúdo dos documentos | Validações existentes: não cobrem conteúdo |
| E16 | 108 | p. 5 | Portaria MDA 19/2025, art. 8º — tipos documentais obrigatórios para inscrição | Critério documental (Dimensão 3) |
| E17 | 137 | p. 156 e 166 | MCR/BACEN — CAF como documento suficiente para Pronaf, dispensa cartório | Centralidade do CAF no acesso ao crédito |

**Evidências testemunhais e consensuais:**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E18 | 73 | p. 3 | Ata de reunião de trabalho (07/10/2025): consenso de que o sistema carece de mecanismos automatizados de validação | Reconhecimento mútuo da insuficiência |
| E19 | 74 | p. 4 | Ata de encerramento: conclusão formal de que muitos problemas se originam do legado do CAF 2.0 | Contexto passivo/corrente |
| E20 | 72 | p. 2 | Reunião técnica com gestão do MDA: cruzamentos automáticos com Sicar (CAR) planejados apenas "futuramente" | Ausência de integração georreferenciada |

**Elementos do contraditório incorporados:**

| Ref. | Peça | Página | Descrição | Calibração aplicada |
|---|---|---|---|---|
| E21 | 150 | p. 18-19 | Manifestação do gestor sobre heterogeneidade temporal e extrapolação amostral (ARG-01) | Distinção passivo/corrente; projeções como ordem de grandeza |
| E22 | 150 | p. 22 | Monitoramento do gestor (2º sem/2024): conformidade integral de 32% (dado do gestor, não auditado) | Corroboração da ordem de grandeza do problema (ARG-09) |
| E23 | 150 | p. 24-26 | Descrição do modelo híbrido de validação (rede emissora + regras sistêmicas + monitoramento) (ARG-07) | Reconhecimento das múltiplas camadas |
| E24 | 150 | p. 27, 29 | Elementos de enfrentamento: TED DCAF/UFES 2025-2027; vencimento de 742 mil registros em 2026 (ARG-09) | Afasta leitura de inércia; contextualiza prazo |
| E25 | 166 | p. 1-2 | Contestação do gestor à peça 105; reanálise com 64% de conformidade (ARG-13, ARG-14) | Ressalva na Dimensão 3; distinção amostral vs. dirigida |

---

### Efeitos

A discrepância entre a situação encontrada e os critérios de elegibilidade e qualidade documental produz efeitos potenciais — consequências adversas cuja concretização depende de fatores adicionais além da própria inconsistência cadastral. Conforme registrado pelo gestor (ARG-02, ARG-11), inconsistência no cadastro não equivale automaticamente a inelegibilidade definitiva nem a concessão indevida: o CAF é porta de entrada, e as políticas usuárias possuem filtros próprios de elegibilidade, contratação e execução (peça 150, p. 27-29, 46). A equipe não identificou, no escopo desta auditoria, efeitos concretos consumados — eventos adversos com vítimas ou prejuízos individualizados — decorrentes das insuficiências documentadas. Os efeitos descritos a seguir, classificados como potenciais, foram extraídos do relatório de auditoria (§§57-62) e calibrados pelas análises do contraditório.

**Efeitos potenciais:**

**EP1 — Risco de comprometimento da capacidade de confirmação documental da elegibilidade para parcela expressiva da base.** A presença de aproximadamente 3,08 milhões de documentos semanticamente inadequados (27,1% da base) resulta na impossibilidade prática de o sistema do CAF atestar que os beneficiários correspondentes cumprem os requisitos cumulativos estabelecidos na Lei 11.326/2006 (peça 140, p. 3-4). Para cerca de um quarto da base de cadastros, não há como confirmar, com base na documentação apresentada, se os beneficiários atendem às condições legais — comprometendo a função primordial do cadastro como instrumento de habilitação prévia (peça 141, §57). Esse efeito recai sobre a *capacidade do cadastro de comprovar e sustentar a elegibilidade*, e não sobre a decisão final de concessão em cada política pública, distinção que preserva o enquadramento operacional do achado (ARG-02). A centralidade do CAF no acesso ao crédito rural reforça a materialidade do efeito: o Manual de Crédito Rural do Banco Central estabelece que o CAF válido é documento suficiente para comprovar o vínculo do beneficiário com a terra e com a atividade produtiva para fins de contratação de financiamento do Pronaf, dispensando inclusive registro em cartório (peça 137, p. 156 e 166).

**EP2 — Risco de comprometimento da base de dados para validação de requisitos legais de área.** A identificação de 1,44 milhão de documentos com divergências críticas de área superiores a 10%, agravada pela divergência sistemática agregada de +120,89%, resulta em dados de área não confiáveis para fins de validação do requisito legal de 4 módulos fiscais (peça 109, p. 7). Dados com essa magnitude de divergência não podem ser utilizados com segurança para planejamento, dimensionamento de recursos ou monitoramento de programas, comprometendo a capacidade do sistema de cumprir sua função regulatória (peça 141, §58).

**EP3 — Risco de obstrução técnica à automação e à auditabilidade do acervo documental.** A constatação de que 68,7% dos documentos digitalizados (aproximadamente 2,33 milhões) apresentam resolução inferior a 300 DPI dificulta ou impossibilita a implementação de tecnologias de OCR e a validação semântica automatizada (peça 106, p. 15). Essa deficiência limita a viabilidade de automação para o subconjunto afetado e, combinada com a escala total do acervo (11,4 milhões de documentos, que torna a validação manual igualmente inviável), compromete a auditabilidade futura do acervo (peça 141, §59). Registre-se que o parâmetro de 300 DPI é utilizado como referência orientativa de boa prática (ARG-10), e a constatação indica limitação técnica na qualidade de ingestão, sem implicar invalidação automática de todo documento abaixo desse patamar.

**EP4 — Risco de direcionamento de recursos a beneficiários cuja elegibilidade não pode ser comprovada documentalmente.** Uma vez que a elegibilidade de aproximadamente 3,08 milhões de cadastros não pode ser comprovada com base na documentação apresentada (peça 140, p. 3-4), existe o risco de que recursos de programas que utilizam o CAF como habilitação prévia — Pronaf, PAA e PNAE — possam vir a ser direcionados a beneficiários cujo atendimento aos critérios legais não possa ser verificado documentalmente (peça 141, §60). Esse risco, contudo, não decorre linearmente do CAF: as políticas usuárias possuem filtros próprios de elegibilidade, contratação e execução, e inconsistência cadastral não equivale a desvio de finalidade consumado (ARG-11; peça 150, p. 27-29, 46). O modelo de verificação do CAF envolve camadas complementares — atuação da rede emissora, regras sistêmicas e possibilidade de monitoramento posterior —, de modo que a materialização do risco depende da efetividade dessas camadas complementares (ARG-07; peça 150, p. 24-26). Por essas razões, o efeito é classificado como potencial.

**EP5 — Risco de insegurança jurídica para gestores e beneficiários.** A taxa de inadequação documental de 27,1% pode gerar insegurança jurídica tanto para gestores públicos — risco de responsabilização por concessão baseada em documentação insuficiente — quanto para beneficiários — risco de suspensão de direitos e questionamento posterior da elegibilidade, mesmo após anos de participação regular nos programas (peça 141, §61). A base normativa desse risco reside na centralidade do CAF como documento habilitador: se o MCR/BACEN aceita o CAF como prova suficiente para Pronaf (peça 137, p. 156, 166) e determinações anteriores do TCU já exigiram salvaguardas de qualidade (Acórdão 1197/2018, item 9.2.6), a persistência de documentação insuficiente em escala expressiva expõe gestores ao risco de questionamento posterior e beneficiários à possibilidade de revisão de elegibilidade. A proporcionalidade do tratamento desse risco deve considerar a materialidade e a criticidade de cada situação (ARG-12; peça 150, p. 30, 56, 72-73), bem como os elementos de enfrentamento gradual já em curso pelo gestor (ARG-09).

**EP6 — Risco de agravamento sistêmico por inércia operacional.** Caso não sejam implementadas correções sistêmicas, os problemas documentados tendem a se agravar: considerando a taxa de crescimento de aproximadamente 3,5% ao mês (peça 140), em nove meses a quantidade de documentos inadequados pode ultrapassar 4 milhões, tornando a correção progressivamente mais complexa e custosa (peça 141, §62). Essa projeção é aproximada — baseada na taxa observada aplicada ao ponto central do intervalo de confiança — e tem finalidade de ilustrar a ordem de grandeza do risco de agravamento, não de quantificação precisa. Esse risco é mitigado, em parte, pelos elementos de enfrentamento apresentados pelo gestor — Plano de Formação via TED DCAF/UFES para 2025-2027 e vencimento previsto de cerca de 742 mil registros em 2026 com renovação cadastral (ARG-09; peça 150, p. 27, 29) —, que afastam leitura de inércia administrativa mas não dispensam resposta institucional estruturada.

---

**Nota sobre quantificação de prejuízos financeiros.** A natureza operacional desta auditoria — focada na qualidade dos dados e na capacidade do sistema de atestar elegibilidade — não permitiu quantificar prejuízos financeiros diretos ao erário. Tal quantificação exigiria cruzamento individualizado entre os aproximadamente 3,08 milhões de cadastros com documentação insuficiente e os benefícios efetivamente concedidos via políticas públicas, análise que extrapola o escopo deste trabalho de avaliação de qualidade de dados. Registra-se, contudo, a ordem de grandeza do universo financeiro que depende do CAF como instrumento de habilitação prévia: o Pronaf movimentou R$ 59,6 bilhões na safra 2023/2024 (peça 141, §30.1); o PAA operou com orçamento aproximado de R$ 750 milhões em 2024 (peça 141, glossário); e o PNAE destinou aproximadamente R$ 1,6 bilhão à agricultura familiar (peça 141, glossário). Essa dimensão financeira reforça a materialidade dos efeitos documentados, sem que se pretenda afirmar dano ao erário consumado — coerentemente com a distinção entre inconsistência cadastral e inelegibilidade definitiva (ARG-02) e com o reconhecimento de que as políticas usuárias possuem filtros próprios de elegibilidade (ARG-11).

**Prejuízos sociais potenciais.** A insuficiência dos mecanismos de validação pode produzir consequências adversas não apenas para a capacidade institucional do cadastro, mas também para os próprios agricultores familiares que dele dependem. Tais prejuízos, ainda que de difícil quantificação monetária, são relevantes para a calibração dos encaminhamentos, conforme orientação das Normas de Auditoria do TCU. Os riscos sociais identificáveis a partir das evidências do processo são:

(i) *Risco de exclusão de beneficiários legítimos em eventual saneamento indiscriminado:* caso o enfrentamento do passivo documental seja conduzido de forma massiva e indiferenciada — sem escalonamento por risco e materialidade —, agricultores cuja elegibilidade é real mas cuja documentação é formalmente insuficiente podem ter o acesso ao CAF e, por consequência, ao crédito rural e às políticas assistenciais temporariamente comprometido. Esse risco é reconhecido pelo próprio gestor, que propõe abordagem escalonada por materialidade e criticidade (ARG-12; peça 150, p. 30, 72-73), e pela equipe, que incorporou essa calibração nos encaminhamentos.

(ii) *Risco de questionamento retroativo da elegibilidade de beneficiários regulares:* agricultores que participam de programas há anos podem ter sua elegibilidade questionada em razão de documentação que foi aceita pelo sistema sem verificação semântica no momento da inscrição (peça 141, §61). Esse risco é potencial e deve ser tratado com proporcionalidade, considerando que o problema reside na insuficiência do mecanismo de validação, não na conduta do beneficiário.

(iii) *Limitação na capacidade de comunicação com os cadastrados:* embora documentada em maior detalhe no Achado III, a constatação de que 90,62% dos e-mails de pessoa física cadastrados são fictícios (peça 125, p. 6) limita a capacidade do Estado de comunicar avisos, prazos de renovação, mudanças normativas ou suspensões ao público do CAF, gerando risco de que beneficiários percam direitos por falta de informação, não por inelegibilidade (peça 141, §166.7). Essa limitação deve ser contextualizada à realidade material do público rural — baixa escolaridade, conectividade limitada e preferência por canais alternativos como WhatsApp (ARG-23; peça 150, p. 49) —, de modo que o prejuízo social não decorre de culpa do agricultor, mas de insuficiência dos mecanismos de cadastramento em ambiente de exclusão digital.

---

**Critérios dos efeitos:**

Os critérios abaixo fundamentam *por que* os efeitos identificados são adversos. São distintos dos critérios da Situação Encontrada (C1-C8), que fundamentam o desvio entre o que é e o que deveria ser.

**CE1. Lei nº 11.326/2006, art. 3º** (peça 80, p. 1) — A função do CAF é atestar o cumprimento dos requisitos cumulativos de elegibilidade. A limitação na capacidade de fazê-lo para parcela expressiva da base (EP1) compromete a finalidade legal do cadastro.

**CE2. Decreto nº 9.064/2017, art. 4º** (peça 81) — O CAF é instrumento de *identificação e qualificação*. Dados de área não confiáveis (EP2) e documentos não processáveis por OCR (EP3) limitam a capacidade de qualificação adequada.

**CE3. MCR/BACEN — Manual de Crédito Rural** (peça 137, p. 156, 166) — O CAF válido dispensa registro em cartório para fins de Pronaf. A centralidade do CAF na cadeia de crédito rural amplifica a materialidade dos efeitos EP1 e EP4: se o cadastro aceita documentação insuficiente e é utilizado como prova suficiente para concessão de crédito, a qualidade documental torna-se condição direta de segurança do sistema de financiamento.

**CE4. DAMA-DMBOK v2** (peça 86, p. 16 e 38) — Estabelece que obter dados corretos na origem custa menos do que corrigir depois. A obstrução à automação (EP3) e o risco de agravamento (EP6) decorrem da violação desse princípio: a ausência de prevenção na entrada converteu problemas de qualidade em passivo acumulado de tratamento crescentemente custoso.

**CE5. Acórdão 1197/2018-TCU-Plenário, item 9.2.6** — Determinou que o CAF incorporasse salvaguardas de qualidade de dados ao substituir a DAP. A persistência de documentação insuficiente em escala expressiva, após dois ciclos de monitoramento (Ac. 1866/2021 e Ac. 885/2024), expõe gestores ao risco de responsabilização e beneficiários à possibilidade de revisão de elegibilidade (EP5).

---

**Evidências dos efeitos:**

| Ref. | Peça | Página | Descrição | Efeito sustentado |
|---|---|---|---|---|
| EE1 | 140 | p. 3-4 | Nota Técnica: elegibilidade de 3,08M cadastros não comprovável documentalmente | EP1 (capacidade de confirmação) |
| EE2 | 140 | p. 5 | Projeções estatísticas: 3,08M docs inadequados (IC 99%, 2,57M-3,60M) | EP1 (magnitude), EP6 (projeção de agravamento) |
| EE3 | 103 | p. 9-11 | Taxa de 27,1% de inadequação semântica; 36,6% imóvel, 30,4% renda | EP1 (distribuição por categoria) |
| EE4 | 109 | p. 7 | 53,55% de divergências críticas de área >10%; população estimada de 1,44M | EP2 (dados de área não confiáveis) |
| EE5 | 109 | p. 9 | Divergência agregada de +120,89% (3.827,65 ha docs vs. 1.732,85 ha base) | EP2 (viés sistemático) |
| EE6 | 106 | p. 7, 15 | 68,7% com resolução <300 DPI; limitação à implementação de OCR | EP3 (obstrução à automação) |
| EE7 | 137 | p. 156, 166 | MCR/BACEN: CAF é documento suficiente para Pronaf, dispensa cartório | EP1 e EP4 (centralidade no crédito) |
| EE8 | 140 | cálculo da equipe | Taxa de crescimento de ~3,5% ao mês na base documental (cálculo da equipe a partir dos dados da peça 140) | EP6 (risco de agravamento — projeção aproximada, sem propagação formal de incerteza) |
| EE9 | 150 | p. 27-29, 46 | Manifestação do gestor: risco não decorre linearmente do CAF; políticas têm filtros próprios (ARG-11) | EP4 (calibração) |
| EE10 | 150 | p. 24-26 | Modelo híbrido de validação: rede emissora + regras sistêmicas + monitoramento (ARG-07) | EP4 (calibração — camadas complementares) |
| EE11 | 150 | p. 9-13 | CAF como cadastro autodeclaratório e porta de entrada (ARG-02) | EP1 e EP4 (calibração — inconsistência ≠ inelegibilidade) |
| EE12 | 150 | p. 27, 29 | TED DCAF/UFES 2025-2027; vencimento de 742 mil registros em 2026 (ARG-09) | EP6 (mitigação parcial do risco de agravamento) |
| EE13 | 150 | p. 30, 56, 72-73 | Escalonamento por materialidade e revisão de encaminhamentos (ARG-12) | EP5 (proporcionalidade do tratamento) |
| EE14 | 137 | p. 156, 166 | MCR/BACEN: CAF como documento habilitador suficiente para Pronaf | EP5 (base normativa da exposição jurídica) |
| EE15 | Ac. 1197/2018 | item 9.2.6 | Determinação de incorporar salvaguardas de qualidade; pendente após 2 ciclos de monitoramento | EP5 (histórico de deliberações não cumpridas integralmente) |
| EE16 | 141 | §30.1 | Pronaf: R$ 59,6 bilhões na safra 2023/2024; PAA: ~R$ 750 milhões; PNAE: ~R$ 1,6 bilhão à agricultura familiar | Nota de quantificação financeira (ordem de grandeza do universo em risco) |
| EE17 | 125 | p. 6 | 90,62% dos e-mails de pessoa física cadastrados no CAF são fictícios | Prejuízo social (iii) — limitação de comunicação com cadastrados |
| EE18 | 141 | §166.7 | Risco de exclusão sistêmica de beneficiários por impossibilidade de comunicação (2,6 milhões de famílias) | Prejuízo social (iii) — consequência para o agricultor |
| EE19 | 150 | p. 30, 72-73 | Gestor propõe escalonamento por materialidade para evitar tratamento indiscriminado (ARG-12) | Prejuízo social (i) — risco de exclusão de legítimos em saneamento |

### Causas

As causas a seguir explicam *por que* a situação encontrada no ACH-01 ocorreu — os mecanismos específicos no processo de cadastramento, no sistema e no contexto institucional que permitiram a aceitação e permanência de documentos inadequados e inconsistências em escala expressiva. As causas foram extraídas do relatório de auditoria (peça 141, §§52-56) e calibradas pelas análises do contraditório. O modelo de verificação do CAF envolve camadas complementares (ARG-07), e o diagnóstico não afirma ausência absoluta de controles, mas insuficiência dos mecanismos existentes para assegurar integridade documental na escala do cadastro.

**Causas de processo:**

**CP1 — Mecanismo de ingestão documental desenhado para aceitar, não para verificar.** A regra de negócio RN1.17 do CAF 3.0 exige a anexação obrigatória de documentos comprobatórios, porém o sistema aceita qualquer arquivo sem verificação do conteúdo semântico nem do tipo documental em relação à categoria selecionada (peça 78, p. 5; peça 141, §54). As validações automatizadas existentes (RN1.29 e RN1.30) consultam bases externas da Dataprev — relações trabalhistas, enquadramento de renda, benefícios —, mas não verificam o teor dos documentos anexados (peça 78, p. 7; peça 162, p. 7). O resultado é que o processo de ingestão funciona como porta aberta para documentos de qualquer natureza, desde que um arquivo seja anexado. Esse mecanismo é a causa direta da taxa de 27,1% de inadequação semântica (Dimensão 1 da SE) e dos 33,33% de tipo documental inadequado (Dimensão 3). *Corrigível pela Proposta 2.1.1 (prevenção na entrada).*

**CP2 — Ausência de validação de consistência de área na entrada.** O sistema não dispõe de mecanismo automatizado de cruzamento entre a área declarada no formulário e a área constante do documento digitalizado, nem de integração com bases georreferenciadas oficiais (Sigef, Sicar) para validação no momento do cadastramento (peça 141, §55). Em relação ao Sicar (CAR), a gestão do MDA informou que cruzamentos automáticos são planejados apenas "futuramente" (peça 72, p. 2). Essa lacuna de controle permitiu o acúmulo de divergências críticas de área documentadas na Dimensão 2 da SE (53,55% dos documentos com divergência >10%, com viés sistemático de +120,89%), que sugerem causas estruturais como erro de conversão de unidades alqueires/hectares, registro de área útil vs. total e desatualização entre documentos e dados cadastrados (peça 141, §56). *Corrigível pelas Propostas 2.1.2 (integridade de dados críticos) e 2.1.3 (interoperabilidade).*

**Causas de produto:**

**CD1 — Ausência de requisitos mínimos de qualidade técnica na digitalização.** O sistema não estabelece requisitos de resolução, formato ou legibilidade para os documentos digitalizados aceitos no upload, nem dispõe de mecanismo de bloqueio para arquivos com resolução inferior a padrões técnicos mínimos ou verificação automatizada de legibilidade (peça 141, §53; peça 106, p. 7). Esse mecanismo é a causa direta da taxa de 68,7% de documentos com resolução inferior a 300 DPI (Dimensão 4 da SE). *Corrigível pela Proposta 2.1.4 (requisitos de qualidade de digitalização).*

**CD2 — Passivo documental herdado das transições tecnológicas sem curadoria estruturada.** A base ativa do CAF reúne registros produzidos sob diferentes contextos normativos e tecnológicos — DAP, CAF 2.0 e CAF 3.0 — que foram migrados sem processo de curadoria ou revalidação documental (peça 141, §§52, 64). Na reunião de encerramento, a conclusão formal registrou que muitos dos problemas identificados se originam do legado do CAF 2.0, que não possuía validações robustas (peça 74, p. 4). O resultado é que melhorias implementadas no CAF 3.0 — como controles que reduziram o cadastramento de propriedades inelegíveis (98,7% das que excedem 4 MF são pré-CAF 3.0; peça 141, §65) — não retroagiram sobre o passivo, que permanece ativo e apto a influenciar decisões correntes. *Corrigível pelas Propostas 2.2 (gestão de mudanças) e 2.3 (monitoramento contínuo).*

**Fatores contribuintes (contexto institucional):**

Os fatores a seguir contextualizam a situação sem constituir causas diretas das insuficiências documentadas. São relevantes para dimensionar proporcionalmente os encaminhamentos, mas não dispensam a correção dos mecanismos identificados em CP1, CP2, CD1 e CD2.

**FC1 — Heterogeneidade da rede emissora e complexidade operacional.** O CAF atende públicos diversos — agricultores familiares, extrativistas, pescadores, quilombolas, indígenas, assentados — por meio de rede emissora ampla e descentralizada (ARG-04; peça 150, p. 12-16; peça 153, p. 4). A diversidade de perfis e a multiplicidade de atores dificultam a padronização dos procedimentos de cadastramento, sem dispensar a necessidade de controles mínimos de qualidade na entrada.

**FC2 — Restrições estruturais de TIC e dependências interinstitucionais.** O ambiente operacional do CAF foi marcado por contratos de TIC compartilhados com o MAPA, infraestrutura limitada e intermitência do CAFWeb (ARG-05; peça 154, p. 1; peça 155, p. 2-4; peça 160, p. 1).

**FC3 — Reconstrução institucional do MDA e transição normativa.** A reorganização do MDA e a edição da Portaria MDA nº 20/2023 recolocaram o CAF em novas bases normativas (ARG-03; peça 150, p. 4-7). Esse contexto contribuiu para a coexistência de registros produzidos sob diferentes marcos normativos na mesma base ativa.

**FC4 — Enfrentamento gradual em curso.** O gestor apresentou elementos concretos de enfrentamento: celebração de TED DCAF/UFES para o período 2025-2027 (peça 150, p. 27) e vencimento previsto de aproximadamente 742 mil registros em 2026, que ensejará renovação cadastral com reapresentação documental (peça 150, p. 29). Esses elementos evidenciam resposta institucional em andamento e contextualizam o prazo de implementação das medidas recomendadas (ARG-09).

**Conexão causa → proposta:** as causas de processo e produto (CP1, CP2, CD1, CD2) são corrigíveis pelas Propostas 2.1.1 a 2.3, conforme indicado em cada causa. A Proposta 1 (determinação transversal de plano de ação) endereça o conjunto das causas identificadas nos quatro achados, incluindo o saneamento do passivo documental (CD2). A Proposta 2.4 (gestão de metadados) pertence ao escopo do ACH-04, não ao ACH-01.

---

**Critérios das causas:**

Os critérios abaixo fundamentam *por que* os mecanismos identificados constituem causas — ou seja, qual norma ou referencial deveria ter sido aplicada no processo e cuja não-aplicação produziu a situação encontrada. São distintos dos critérios da SE e dos critérios dos Efeitos.

**CC1. DAMA-DMBOK v2 — prevenção na entrada** (peça 86, p. 38) — A melhor forma de assegurar qualidade é impedir a entrada de dados inadequados na origem. **Mecanismo técnico da violação:** a RN1.17 opera como validação *fail-open* — exige que um arquivo seja anexado (controle de presença), mas não verifica se o conteúdo do arquivo corresponde à categoria documental selecionada pelo usuário, se o formato é legível nem se o documento contém informação probatória relevante (peça 78, p. 5). Qualquer PDF, JPEG ou arquivo em branco satisfaz a regra, desde que a operação de upload seja concluída. As validações existentes (RN1.29 e RN1.30) consultam bases externas da Dataprev para dados declarados, mas não tocam o conteúdo dos documentos anexados (peça 78, p. 7). A ausência de gate de verificação semântica na ingestão é o mecanismo que permitiu a entrada e permanência dos 27,1% de documentos inadequados e dos 33,33% de tipo documental incorreto. **Ancoragem:** Ac. 457/2026-Plenário e Ac. 906/2009-Plenário.

**CC2. Portaria MDA nº 19/2025, art. 8º** (peça 108, p. 5) — Especifica tipos documentais obrigatórios. A ausência de validação automatizada do tipo documental na ingestão (CP1) cria lacuna entre requisito normativo e controle efetivo.

**CC3. COBIT 2019, BAI10 — Gestão de mudanças** — Recomenda testes de regressão antes de produção. A migração sem curadoria do passivo (CD2) constitui insuficiência de gestão de mudanças.

**CC4. Acórdão 1197/2018-TCU-Plenário, itens 9.2.2 e 9.2.6** — Determinou procedimentos de validação (9.2.2) e salvaguardas ao substituir a DAP (9.2.6). Após dois ciclos de monitoramento, pendentes de cumprimento integral.

---

**Evidências das causas:**

| Ref. | Peça | Página | Descrição | Causa sustentada |
|---|---|---|---|---|
| EC1 | 78 | p. 5 | RN1.17: anexação obrigatória sem verificação de conteúdo semântico | CP1 (mecanismo de ingestão) |
| EC2 | 78 | p. 7 | RN1.29-30: validações consultam Dataprev, não conteúdo dos documentos | CP1 (lacuna de cobertura) |
| EC3 | 162 | p. 7 | Dataprev: informações de renda, benefícios — não conteúdo documental | CP1 (confirmação do escopo) |
| EC4 | 72 | p. 2 | Reunião técnica: cruzamentos com Sicar planejados apenas "futuramente" | CP2 (ausência de interoperabilidade) |
| EC5 | 141 | §56 | Divergência agregada +120,89% sugere causas estruturais (conversão, área útil vs. total) | CP2 (padrão não aleatório) |
| EC6 | 141 | §53 | Ausência de controles de qualidade técnica na digitalização | CD1 (mecanismo) |
| EC7 | 74 | p. 4 | Ata de encerramento: problemas do legado CAF 2.0 sem validações robustas | CD2 (passivo herdado) |
| EC8 | 73 | p. 3 | Ata de reunião: consenso sobre carência de mecanismos automatizados | CP1, CP2, CD1 (reconhecimento mútuo) |
| EC9 | 141 | §65 | 98,7% das propriedades > 4 MF cadastradas antes do CAF 3.0 | CD2 (melhoria não retroativa) |
| EC10 | 150 | p. 12-16 | Heterogeneidade: públicos diversos, rede emissora ampla (ARG-04) | FC1 (fator contribuinte) |
| EC11 | 154 | p. 1 | NT CGTI-MDA: serviços de TIC extrapolam contratos com MAPA (ARG-05) | FC2 (restrições de TIC) |
| EC12 | 150 | p. 4-7 | Reconstrução institucional do MDA; Portaria MDA 20/2023 (ARG-03) | FC3 (contexto de transição) |
| EC13 | 150 | p. 22, 27, 29 | Monitoramento: 32% conformidade; TED DCAF/UFES; 742 mil registros vencem em 2026 (ARG-09) | FC4 (enfrentamento gradual) |

### Boas Práticas e Avanços

Não foram identificadas, no escopo deste achado, boas práticas no sentido estrito da NAT §160 — práticas que, cumulativamente, ultrapassem o cumprimento do dever legal, sejam significativas, inovadoras e efetivas, e possam ser propostas para extensão a outros órgãos. Os avanços implementados pelo gestor — migração para o CAF 3.0 com elevação da taxa de propriedades > 4 MF cadastradas após o novo sistema para 98,7%, padronização de Declarações de Veracidade com taxa de inadequação 5× inferior à média geral (5,6% *vs.* 27,1%) e realização de monitoramento próprio com amostra probabilística estratificada por UF (conformidade integral de 32%) — foram factualmente reconhecidos na Situação Encontrada e nos Fatores Contribuintes (FC1–FC4), onde contextualizam a capacidade de resposta institucional e informam a proporcionalidade dos encaminhamentos.

### Encaminhamentos

Os encaminhamentos a seguir definem resultados a alcançar, com liberdade de meios para a unidade gestora, em conformidade com o compromisso firmado no Anexo — Análise dos Comentários dos Gestores. A determinação estabelece obrigação de resultado com prazo; as recomendações indicam direções de aprimoramento sem prescrever soluções específicas, cabendo ao MDA definir a forma de implementação mais adequada à sua realidade operacional.

**Determinação:**

**Proposta 1.** Determinar ao MDA que, no prazo de 180 dias, elabore e encaminhe ao TCU plano de ação, com responsáveis, prazos e forma de comunicação do cumprimento, para avaliar as situações identificadas neste relatório e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, abrangendo as inconsistências documentadas na qualidade dos **dados de entrada**, dos **dados geoespaciais**, dos **dados cadastrais** e dos **metadados** do CAF, em conformidade com os critérios de elegibilidade previstos no art. 3º da Lei 11.326/2006 e com a finalidade de identificação e qualificação estabelecida no art. 4º do Decreto 9.064/2017.

*Justificativa do vínculo:* a determinação decorre diretamente da situação encontrada nas quatro dimensões do ACH-01 — inadequação semântica (27,1%), divergência de área (53,55%), tipo documental (33,33%) e baixa qualidade de digitalização (68,7%) — e dos efeitos potenciais documentados (EP1-EP6), que evidenciam comprometimento da capacidade do CAF de atestar elegibilidade. O componente "dados de entrada" da determinação corresponde ao escopo deste achado.

**Recomendações:**

**Proposta 2.1.1.** Assegurar que processos de cadastramento e atualização produzam dados com qualidade suficiente, incluindo mecanismos que previnam inserção e permanência de dados inválidos no CAF.

*Justificativa do vínculo:* decorre da Dimensão 1 (27,1% de documentos semanticamente inadequados aceitos pelo sistema) e da Dimensão 3 (33,33% de tipo documental inadequado), que evidenciam insuficiência dos mecanismos de prevenção na entrada — cenário documentado no DAMA-DMBOK v2 como preferível à correção retroativa (CE4).

**Proposta 2.1.2.** Garantir integridade e consistência dos dados críticos do CAF, por meio de controles que reduzam erros e anomalias em campos essenciais à identificação do beneficiário, localização do imóvel e elegibilidade cadastral.

*Justificativa do vínculo:* decorre da Dimensão 2 (53,55% de divergências críticas de área com viés sistemático de +120,89%), que demonstra insuficiência de controles de consistência em campos essenciais à verificação do requisito de 4 módulos fiscais (C1).

**Proposta 2.1.3.** Estabelecer mecanismos de interoperabilidade com bases de dados oficiais relevantes, para detecção tempestiva de inconsistências e irregularidades nos dados cadastrais.

*Justificativa do vínculo:* decorre da constatação de ausência de integração do CAF com bases georreferenciadas oficiais como Sigef e Sicar — cruzamentos planejados apenas "futuramente" (peça 72, p. 2) —, limitando a validação automática de dados de área e o efeito potencial EP1 (comprometimento da capacidade de confirmação de elegibilidade).

**Proposta 2.1.4.** Estabelecer requisitos mínimos de qualidade técnica para documentos digitalizados do CAF, assegurando legibilidade, indexação e auditoria do acervo documental.

*Justificativa do vínculo:* decorre da Dimensão 4 (68,7% dos documentos com resolução inferior a 300 DPI) e do efeito potencial EP3 (risco de obstrução à automação e à auditabilidade do acervo), que demonstram limitação técnica na qualidade de ingestão documental. O parâmetro Conarq é tratado como referência orientativa de boa prática (ARG-10).

**Proposta 2.2.** Aprimorar gestão de mudanças e garantia da qualidade do Sistema CAF, prevenindo que novas versões introduzam regressões funcionais ou comprometam integridade dos dados.

*Justificativa do vínculo:* decorre do contexto temporal documentado na SE (transições DAP → CAF 2.0 → CAF 3.0 com gaps de validação) e do efeito potencial EP6 (risco de agravamento sistêmico se correções não forem implementadas). A gestão de mudanças é necessária para prevenir que futuras evoluções do sistema repitam o padrão de regressões documentado.

**Proposta 2.3.** Implementar monitoramento contínuo da qualidade dos dados do CAF, com indicadores que permitam identificar e priorizar ações corretivas e avaliar efetividade das medidas.

*Justificativa do vínculo:* decorre do efeito potencial EP6 (risco de agravamento por inércia operacional) e da constatação de que o monitoramento próprio do gestor registrou conformidade integral de apenas 32% (peça 150, p. 22), evidenciando necessidade de acompanhamento estruturado por indicadores.

### Benefícios Esperados

**Benefícios quantitativos:**

a) Redução da taxa de inadequação semântica de 27,1% da base documental (aproximadamente 3,08 milhões de documentos), com meta a definir pelo gestor no plano de ação (Proposta 1) — reversão parcial de EP1.

b) Redução da taxa de divergências críticas de área de 53,55% (aproximadamente 1,44 milhão de documentos com divergência superior a 10%, viés sistemático de +120,89%), com meta a definir pelo gestor (Proposta 2.1.2) — reversão parcial de EP2.

c) Elevação da proporção de documentos digitalizados com resolução igual ou superior a 300 DPI (atualmente 31,3% do acervo), com meta a definir pelo gestor (Proposta 2.1.4) — reversão parcial de EP3.

d) Elevação da taxa de conformidade integral dos dados de entrada, a partir do patamar de 32% apurado pelo monitoramento próprio do gestor, com meta a definir no plano de ação (Proposta 2.3) — reversão parcial de EP6.

**Benefícios qualitativos:**

a) Fortalecimento da capacidade do CAF de atestar documentalmente a elegibilidade dos beneficiários (reversão de EP1), assegurando que a documentação comprobatória sustente a função habilitadora do cadastro para Pronaf, PAA e PNAE (Proposta 2.1.1).

b) Melhoria da confiabilidade dos dados de área para validação do requisito legal de 4 módulos fiscais (reversão de EP2), mediante controles de consistência na entrada e interoperabilidade com bases georreferenciadas oficiais (Propostas 2.1.2 e 2.1.3).

c) Viabilização da automação e da auditabilidade do acervo documental (reversão de EP3), mediante requisitos mínimos de qualidade técnica na digitalização que permitam implementação de OCR e validação semântica automatizada (Proposta 2.1.4).

d) Redução do risco de direcionamento de recursos a beneficiários cuja elegibilidade não pode ser comprovada documentalmente (reversão de EP4), mediante prevenção na entrada e monitoramento contínuo (Propostas 2.1.1 e 2.3).

e) Redução da insegurança jurídica para gestores e beneficiários (reversão de EP5), mediante aprimoramento dos mecanismos de validação que afastem risco de responsabilização posterior e de revisão retroativa de elegibilidade (Propostas 2.1.1 a 2.1.4).

f) Prevenção do agravamento do passivo documental (reversão de EP6), mediante gestão de mudanças que previna regressões em futuras evoluções do sistema e monitoramento que detecte desvios tempestivamente (Propostas 2.2 e 2.3).

---

## ACH-02 — Limitações geoespaciais acumuladas ao longo das transições tecnológicas do CAF

**Frase-síntese:**

Devido a limitações acumuladas na gestão de qualidade geoespacial ao longo das transições tecnológicas do CAF — incluindo relaxamento de validações na migração para o CAF 3.0 e trade-offs de interface na adoção do Leaflet —, **ocorreu** elevação da taxa total de erro cartográfico de 32,66% para 45,92%, permanência de duplicações espaciais em patamar elevado e acúmulo de inconsistências territoriais em nível municipal, em desacordo com o dever de melhoria da qualidade e fidedignidade dos dados, **o que levou** à redução da confiabilidade das informações de localização e da efetividade de validações baseadas em dados cartográficos, **impactando** a capacidade do CAF de sustentar análises territoriais e cruzamentos com bases georreferenciadas oficiais.

---

### Situação Encontrada

A auditoria identificou limitações na qualidade geoespacial do CAF que se acumularam ao longo das transições tecnológicas recentes (CAF 2.x → CAF 3.0 → interface Leaflet), reduzindo a confiabilidade das informações de localização. O diagnóstico não afirma colapso uniforme em toda subdimensão cartográfica: o efeito combinado do passivo histórico, do relaxamento de validações e dos trade-offs de interface produziu piora global do resultado, com deterioração em algumas dimensões e melhoria em outras (ARG-15, ARG-16, ARG-20). A análise considerou os argumentos apresentados pelo gestor (peça 150, p. 34-49) e a reanálise ministerial de inflação municipal (peça 161, p. 1-4), cujas análises constam do Anexo — Análise dos Comentários dos Gestores. Cabe registrar que o achado descreve limitação geoespacial acumulada, sem conversão automática em comprometimento da finalidade jurídica do cadastro (ARG-15).

A população analisada compreende 3.175.345 imóveis rurais cadastrados na base ativa (extração de 2/9/2025; peça 110, p. 4), dos quais foram extraídas quatro amostras estratificadas temporais (n = 63.588 registros, peça 113, p. 9), correspondentes às transições tecnológicas: baseline CAF 2.x, implementação CAF 3.0 (março/2025), período pré-Leaflet e implementação Leaflet (agosto/2025). A amostragem é probabilística, com IC 99% e margem de erro efetiva de ±0,40 p.p. (peça 122, p. 6). A análise de inflação cadastral é censitária sobre a totalidade da base ativa.

**Dimensão 1 — Taxa de erro cartográfico global.** O advento do CAF 3.0 em 26/3/2025, apesar de ter introduzido melhorias significativas no sistema em relação à versão anterior, resultou em elevação de 40,6% na taxa total de erro cartográfico, que subiu de 32,66% para 45,92%, afetando aproximadamente 1,46 milhão de imóveis (peça 119, p. 9). Os erros algorítmicos — coordenadas que violam regras básicas do sistema de coordenadas geográficas — aumentaram de 20,31% para 32,07% (+11,76 p.p.), e os erros geoespaciais — coordenadas sintaticamente válidas mas localizadas em município diferente do declarado — aumentaram de 12,35% para 13,85% (+1,50 p.p.) (peça 114, p. 6-7; peça 119, p. 9). A elevação dos erros algorítmicos decorreu do relaxamento das validações de bounding box (envelope geográfico do Brasil) na migração para o CAF 3.0: enquanto a versão anterior rejeitava coordenadas fora do território brasileiro, o CAF 3.0 passou a aceitar coordenadas no intervalo mundial válido sem verificar pertinência ao envelope brasileiro (peça 119, p. 34).

**Dimensão 2 — Duplicações espaciais.** A análise de 43.812 registros de alta precisão revelou que 55,27% (24.215 registros) compartilham coordenadas idênticas com outros imóveis, projetando-se para aproximadamente 1,75 milhão de imóveis na população (peça 117, p. 14-15). A coincidência de coordenadas não equivale, por si, a duplicidade jurídica de inscrições ou multiplicidade indevida de beneficiários, podendo decorrer de situações legítimas como famílias agregadas em mesma base territorial (ARG-17; peça 150, p. 36). Registre-se que a nova interface Leaflet reduziu a taxa de duplicações em cadastros novos de 92,36% para 16,59% (peça 117, p. 15) — avanço significativo. Contudo, o passivo histórico de duplicações permanece ativo na base sem curadoria estruturada: 92,36% dos registros pré-Leaflet possuem duplicatas (peça 117, p. 15). O caso mais emblemático é Salvador/BA, com 6.644 imóveis cadastrados na mesma coordenada (-12,960000°, -38,510000°), correspondente ao Centro Histórico — área urbana onde a existência de milhares de propriedades rurais distintas é fisicamente impossível (peça 123, p. 2-3).

**Dimensão 3 — Consistência municipal.** A análise de consistência espacial identificou que 15,92% dos registros de alta precisão (6.976 de 43.812) apresentam coordenadas localizadas fora do município declarado, projetando-se para aproximadamente 431 mil imóveis na população de alta precisão (peça 116, p. 14). Dentre esses 6.976 registros, 722 (1,65% da amostra de alta precisão) apontam para UF completamente diferente da declarada, configurando erro de maior gravidade (peça 116, p. 14 e 21). A implementação do Leaflet, ao substituir digitação manual por seleção visual em mapa sem validação de consistência municipal, elevou a incidência de erros geoespaciais em 174% (de 11,83% para 32,46%), especialmente em municípios de pequena extensão ou áreas de fronteira (peça 118, p. 16, 24 e 36).

**Dimensão 4 — Inflação cadastral municipal.** A análise censitária identificou 632 municípios com área cadastrada superior à área oficial do município (peça 121, p. 9), dos quais 608 apresentam cobertura igual ou superior a 100% da área municipal. O caso extremo é Penalva/MA, com área cadastrada de 1.801.074 km² — 2.248 vezes a área oficial de 801 km². A transição para o CAF 3.0 demonstrou efetividade na redução de novos casos: a taxa de inflação caiu de 10,89% para 0,31% (peça 121, p. 9). A reanálise ministerial (peça 161, p. 1-4) reclassificou 558 dos 608 municípios com cobertura ≥ 100% como improcedentes — por envolver beneficiários do PNRA, extrativistas, indígenas, quilombolas e comunidades tradicionais —, restando materialidade residual em 50 municípios: 10 com indício de plausibilidade e 40 com necessidade de averiguação complementar (peça 161, p. 3) (ARG-18). A integração com o PNRA/Incra introduziu área total do assentamento sem discriminação da fração individual, gerando excesso nominal na leitura agregativa (peça 161, p. 2) — o que é, em si, um problema de qualidade na integração que reforça a pertinência de aprimorar a interoperabilidade (ARG-19). O indicador de inflação funciona como triagem exploratória de risco, não como conclusão individual de irregularidade.

**Dimensão 5 — Precisão decimal e regressão Leaflet.** A interface Leaflet causou perda de 14,33 p.p. na proporção de registros com alta precisão (≥ 5 casas decimais) (peça 115, p. 6). Essa degradação é interpretada como trade-off da implantação recente (ARG-16): o Leaflet eliminou erros de digitação (-99,95% nos erros algorítmicos), mas incentivou imprecisão geográfica por falta de travas de consistência municipal (peça 118, p. 16). A implementação do Leaflet ocorreu durante a execução da auditoria, após a equipe ter comunicado erros preliminares ao gestor na reunião de abertura (peça 72, p. 1), sendo considerada benefício indireto da ação de controle.

**Contexto temporal e distinção passivo/corrente.** A base compreende registros de diferentes gerações tecnológicas (DAP, CAF 2.x, CAF 3.0, Leaflet). Os avanços recentes são factualmente relevantes: o Leaflet reduziu duplicações em novos cadastros (92,36% → 16,59%), a inflação municipal caiu (10,89% → 0,31%), e coordenadas fora do Brasil caíram de 1.688 para 1. A questão central é estender os avanços ao passivo acumulado e formalizar gestão de mudanças que previna regressões nas transições tecnológicas futuras. Mesmo que o dado geoespacial seja acessório no regime jurídico do CAF, ele integra o acervo informacional do cadastro e é insumo para análises de risco, monitoramento e interoperabilidade (ARG-20). A existência de 1,75 milhão de imóveis com coordenadas idênticas e de taxa de erro de 45,92% são dados que afetam validações baseadas em localização independentemente da natureza jurídica do campo.

---

### Critérios da Situação Encontrada

**C1. Lei nº 11.326/2006, art. 3º, inciso I** (peça 80, p. 1) — Estabelece limite de área de 4 módulos fiscais como requisito de elegibilidade. **Aplicação:** a verificação desse requisito depende de dados confiáveis de localização e área. Com taxa de erro cartográfico de 45,92% (peça 119, p. 9), a validação automatizada desse limite fica limitada.

**C2. Decreto nº 9.064/2017, art. 4º** (peça 81) — Institui o CAF como instrumento de identificação e qualificação. **Aplicação:** a localização do imóvel integra a função de identificação e qualificação; limitações na qualidade geoespacial reduzem a capacidade dessa função.

**C3. Decreto nº 10.046/2019, art. 1º, inciso IV** — Estabelece o dever de promover a melhoria da qualidade e fidedignidade dos dados. **Aplicação:** a elevação da taxa de erro de 32,66% para 45,92% na migração para o CAF 3.0 (peça 119, p. 4 e 9) contraria esse dever.

**C4. DAMA-DMBOK v2** (peça 86) — Referencial técnico de governança de qualidade de dados. **Aplicação:** fundamenta a necessidade de gestão de mudanças que incorpore qualidade de dados como requisito, não apenas funcionalidade. A ausência de testes de regressão e de requisitos não funcionais para integridade geoespacial é incompatível com as boas práticas do referencial. **Ancoragem:** Ac. 457/2026-TCU-Plenário (unanimidade).

**C5. COBIT 2019, objetivo BAI10** — Gestão de configuração e mudanças. **Aplicação:** a migração para o CAF 3.0 removeu validações de bounding box sem testes de regressão, e o Leaflet foi implementado sem validação de consistência municipal — ambas situações que boas práticas de gestão de mudanças preveniriam.

**C6. Acórdãos 1197/2018-TCU-Plenário → 1866/2021-TCU-Plenário → 885/2024-TCU-Plenário** — Cadeia de deliberações sobre qualidade de dados do DAP/CAF. **Aplicação:** demonstra reincidência; determinações pendentes incluem salvaguardas de qualidade de dados (item 9.2.6) e procedimentos de validação e cruzamento (item 9.2.2).

**C7. ISO/IEC 25012:2008** (peça 85) — Dimensões de qualidade de dados: consistência e acurácia. **Aplicação:** complementa DAMA-DMBOK para aferir qualidade dos dados de localização. Critério secundário.

**C8. ISO 19157-1:2023** (peça 83) — Qualidade de dados geoespaciais: acurácia posicional, consistência lógica, metaqualidade. **Aplicação:** referencial técnico específico para dados geoespaciais, adotado na avaliação das dimensões de erro cartográfico e consistência municipal.

---

### Evidências da Situação Encontrada

**Evidências analíticas (bases de dados e scripts):**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E1 | 110 | p. 4 | Filtro UF e população ativa: 3.175.345 imóveis cadastrados (extração 2/9/2025) | População analisada |
| E2 | 113 | p. 4-9 | Extração amostral estratificada: 4 estratos temporais, n = 63.588 registros | Metodologia de amostragem |
| E3 | 122 | p. 6 | Memória de Cálculo MC-070/PT-06: IC 99%, margem de erro ±0,40 p.p. | Parâmetros estatísticos |
| E4 | 119 | p. 9 | Taxa total de erro: 32,66% → 45,92% (+40,6%) na migração CAF 3.0 | Dimensão 1 — piora global |
| E5 | 119 | p. 34 | Relaxamento de validações de bounding box na migração para CAF 3.0 | Dimensão 1 — mecanismo da piora |
| E6 | 114 | p. 6-7 | Classificação de erros: algorítmicos (20,31% → 32,07%) e geoespaciais (12,35% → 13,85%) | Dimensão 1 — desagregação por tipo |
| E7 | 117 | p. 14 | Duplicações: 55,27% dos registros de alta precisão com coordenadas idênticas (24.215 de 43.812) | Dimensão 2 — taxa de duplicação |
| E8 | 117 | p. 15 | Redução pós-Leaflet: 92,36% → 16,59% em novos cadastros | Dimensão 2 — avanço |
| E9 | 123 | p. 2-3 | Caso Salvador/BA: 6.644 imóveis na mesma coordenada (Centro Histórico) | Dimensão 2 — caso emblemático |
| E10 | 116 | p. 14 | Inconsistência municipal: 15,92% dos registros de alta precisão fora do município declarado (~431 mil) | Dimensão 3 |
| E11 | 116 | p. 14, 21 | 722 registros (1,65%) em UF completamente diferente da declarada | Dimensão 3 — casos severos |
| E12 | 118 | p. 16 | Trade-off Leaflet: erros algorítmicos -99,95%, erros geoespaciais +174% | Dimensão 5 — trade-off |
| E13 | 118 | p. 24, 36 | Leaflet: seleção livre sem validação de consistência municipal | Dimensão 3/5 — mecanismo |
| E14 | 121 | p. 9 | Inflação cadastral: 632 municípios; taxa 10,89% → 0,31% após CAF 3.0 | Dimensão 4 — magnitude e avanço |
| E15 | 115 | p. 6 | Perda de precisão decimal: -14,33 p.p. em alta precisão (≥ 5 casas) pós-Leaflet | Dimensão 5 — precisão |

**Evidências documentais (normas e regras de negócio):**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E16 | 83 | (documento integral, 112 p.) | ISO 19157-1:2023 — qualidade de dados geoespaciais: acurácia posicional, consistência lógica, metaqualidade | Critério C8 |
| E17 | 85 | (documento integral) | ISO/IEC 25012:2008 — dimensões de qualidade de dados: completude, acurácia, consistência | Critério C7 |

**Evidências testemunhais e consensuais:**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E18 | 72 | p. 1 | Reunião de abertura: equipe comunicou erros preliminares ao gestor | Leaflet como benefício indireto |
| E19 | 73 | p. 3 | Ata de reunião de trabalho: consenso sobre carência de mecanismos automatizados | Reconhecimento mútuo |
| E20 | 74 | p. 4 | Ata de encerramento: muitos problemas originados do legado CAF 2.0 | Passivo/corrente |

**Elementos do contraditório incorporados:**

| Ref. | Peça | Página | Descrição | Calibração aplicada |
|---|---|---|---|---|
| E21 | 150 | p. 34-35 | Delimitação como problema geoespacial, não de finalidade jurídica (ARG-15) | Evitar sobreleitura; limitação ≠ comprometimento jurídico |
| E22 | 150 | p. 35, 40 | Leaflet como trade-off de implantação recente (ARG-16) | Registrar dois lados: melhorou duplicações, piorou precisão |
| E23 | 150 | p. 35-37 | Duplicação ≠ duplicidade jurídica; famílias agregadas (ARG-17) | Explicitar na Dimensão 2; cautela de linguagem |
| E24 | 161 | p. 1-4 | Reanálise municipal: 558/608 reclassificados, 50 residuais (ARG-18) | Dimensão 4: triagem exploratória, materialidade residual |
| E25 | 161 | p. 2 | PNRA: área total sem fração individual gera excesso nominal (ARG-19) | Reforça pertinência de aprimorar interoperabilidade |
| E26 | 150 | p. 40-49 | Dado geoespacial acessório no regime jurídico; risco superestimado (ARG-20) | Delimitação de efeitos; manter que integra acervo informacional |

---

### Efeitos

As limitações geoespaciais acumuladas ao longo das transições tecnológicas do CAF produzem efeitos potenciais — consequências adversas cuja concretização depende de fatores adicionais além da própria limitação cartográfica. A análise dos efeitos incorpora a distinção estabelecida pelo gestor (ARG-15, ARG-20): o achado descreve limitação na qualidade dos dados de localização, sem conversão automática em comprometimento da finalidade jurídica do cadastro. O dado geoespacial é acessório no regime jurídico do CAF (peça 150, p. 43) e a informação georreferenciada não é compartilhada automaticamente pelas APIs sociais do cadastro (peça 150, p. 44). Essas calibrações delimitam o alcance dos efeitos: consequências de confiabilidade e capacidade informacional, não de irregularidade jurídica. A equipe não identificou, no escopo desta auditoria, efeitos concretos consumados — eventos adversos com vítimas ou prejuízos individualizados — decorrentes das limitações geoespaciais. Os efeitos descritos a seguir, classificados como potenciais, foram extraídos do relatório de auditoria (§§110-113) e calibrados pelas análises do contraditório.

**Efeitos potenciais:**

**EP1 — Risco de limitação na individualização cartográfica da base cadastral.** A existência de aproximadamente 1,75 milhão de imóveis com coordenadas idênticas (55,27% dos registros de alta precisão; peça 117, p. 14-15) limita a capacidade de distinguir propriedades individualmente com base em dados de localização (peça 141, §110). Essa limitação afeta a efetividade de análises geoespaciais automatizadas que dependam de individualização cartográfica — como cruzamentos com bases ambientais (DETER, UCs, CAR) ou fiscalizações de sobreposição em áreas protegidas. Registre-se que a coincidência de coordenadas não equivale, por si, a duplicidade jurídica de inscrições ou multiplicidade indevida de beneficiários: situações legítimas como famílias agregadas em mesma base territorial podem explicar parte das coincidências (ARG-17; peça 150, p. 36). O efeito recai sobre a *capacidade de individualização cartográfica*, não sobre a regularidade jurídica dos cadastros. A interface Leaflet reduziu a taxa de duplicações em novos cadastros de 92,36% para 16,59% (peça 117, p. 15), mas o passivo histórico permanece na base ativa sem curadoria estruturada.

**EP2 — Risco de redução da confiabilidade de validações baseadas em dados cartográficos.** A taxa de erro cartográfico de 45,92% no CAF 3.0, afetando aproximadamente 1,46 milhão de imóveis (peça 119, p. 9), reduz a confiabilidade de validações que dependam de dados de localização — incluindo a verificação do limite legal de 4 módulos fiscais exigido pelo art. 3º, I, da Lei 11.326/2006 (peça 141, §111). A magnitude dos erros (algorítmicos: 32,07%; geoespaciais: 13,85%; peça 114, p. 6-7) compromete a capacidade do sistema de produzir informação confiável de localização para fins de análise e monitoramento. Registre-se que o dado geoespacial é acessório no regime jurídico do CAF (ARG-20; peça 150, p. 43): a verificação do limite de módulos fiscais não é realizada exclusivamente pelo CAF, e as políticas usuárias possuem instâncias próprias de aferição. O efeito recai sobre a *capacidade do cadastro de sustentar validações baseadas em localização*, não sobre a concessão final de benefícios.

**EP3 — Risco de degradação de precisão em transição tecnológica.** A implementação do Leaflet, embora tenha eliminado 99,95% dos erros algorítmicos (peça 118, p. 16), causou elevação de 174% nos erros geoespaciais (de 11,83% para 32,46%) e perda de 14,33 p.p. na proporção de registros com alta precisão decimal (peça 115, p. 6). Esse trade-off evidencia regressão de qualidade associada a transição tecnológica conduzida sem validação de consistência municipal (peça 118, p. 24, 36), situação que boas práticas de gestão de mudanças preveniriam (COBIT 2019, BAI10). O V1 registra que as transições tecnológicas recentes produziram efeitos colaterais críticos na qualidade cartográfica (peça 141, §114-115). A degradação é interpretada como consequência da insuficiência no processo de gestão de mudanças, sem prejuízo de reconhecer que a implementação do Leaflet representou, no balanço global, avanço relevante (ARG-16). Tal como nos demais efeitos, o impacto recai sobre a *confiabilidade técnica dos dados de localização*, não sobre a finalidade jurídica do cadastro (ARG-15, ARG-20).

**EP4 — Risco de distorção analítica em decisões públicas baseadas em dados geoespaciais do CAF.** A fragilidade da base georreferenciada pode comprometer análises territoriais e de planejamento quando o CAF é utilizado como insumo para gestão agrária. Dados geográficos incorretos tendem a produzir diagnósticos estatísticos distorcidos, o que pode resultar na alocação ineficiente de recursos e em políticas públicas inadequadas à realidade local (peça 141, §112). A materialidade desse risco depende da extensão em que as informações geoespaciais do CAF são efetivamente utilizadas como insumo analítico por órgãos de planejamento. No contexto da inflação cadastral, a reanálise ministerial (peça 161, p. 1-4) reclassificou 558 dos 608 municípios com cobertura ≥ 100% como improcedentes, restando materialidade residual em 50 municípios — 10 com indício de plausibilidade e 40 com necessidade de averiguação complementar (ARG-18; peça 161, p. 3). Esse dimensionamento residual deve orientar a proporcionalidade do efeito potencial.

**EP5 — Risco de propagação de erros em integrações externas.** Caso outras instituições — agências de crédito e órgãos ambientais — venham a consumir dados geoespaciais do CAF, os erros sistêmicos identificados podem se propagar para rotinas automatizadas externas, elevando o custo de governança interorganizacional (peça 141, §113). Esse risco, contudo, deve ser lido com cautela: o gestor demonstrou que a informação georreferenciada não é compartilhada automaticamente pelas APIs sociais do cadastro (ARG-20; peça 150, p. 44), de modo que a propagação atual por canais automatizados existentes está limitada. O risco é classificado como potencial e prospectivo — relevante para o desenho de integrações futuras, mas sem evidência de materialização nas interfaces atuais do sistema.

---

**Nota sobre quantificação de prejuízos financeiros.** A quantificação de prejuízo financeiro direto decorrente de limitações geoespaciais exigiria demonstrar que coordenadas incorretas resultaram em validações territoriais equivocadas, com concessão ou negação indevida de benefícios em casos específicos — análise que extrapola o escopo desta auditoria de qualidade de dados. Registra-se que o dado geoespacial é acessório no regime jurídico do CAF (ARG-20; peça 150, p. 43) e não é compartilhado pelas APIs sociais do cadastro (peça 150, p. 44), o que limita a transmissão direta do erro a outras bases. A materialidade dos efeitos geoespaciais reside menos no prejuízo financeiro direto e mais na limitação da capacidade do sistema de sustentar validações baseadas em localização e de produzir informação confiável para políticas públicas.

**Prejuízos sociais potenciais.** As limitações geoespaciais podem afetar indiretamente os agricultores familiares, ainda que de forma menos imediata do que as insuficiências documentais do ACH-01. Os riscos sociais identificáveis são:

(i) *Risco de classificação territorial equivocada:* coordenadas incorretas — presentes em 45,92% dos registros do CAF 3.0 (peça 119, p. 9) — podem levar à associação do imóvel a município diferente do real, potencialmente afetando a validação do limite de 4 módulos fiscais (que varia por município) e o enquadramento em programas territorializados. Esse risco é mitigado pelo fato de que o dado geoespacial não é o único elemento utilizado para validação de elegibilidade (ARG-20), e as políticas usuárias possuem instâncias próprias de aferição.

(ii) *Risco de invisibilidade geográfica:* a existência de aproximadamente 1,75 milhão de imóveis com coordenadas idênticas a outros (peça 117, p. 14-15) pode dificultar a individualização de propriedades em análises territoriais de planejamento — afetando, por exemplo, a alocação de recursos ou a definição de prioridades por região. Esse risco deve ser lido com cautela: coincidência de coordenadas pode decorrer de situações legítimas como famílias agregadas (ARG-17; peça 150, p. 36), e o impacto depende da extensão em que as análises territoriais efetivamente utilizam os dados de localização do CAF.

Os prejuízos sociais geoespaciais são potenciais e indiretos, coerentemente com a natureza acessória do dado de localização no regime jurídico do cadastro. No escopo desta auditoria, não foram identificadas evidências de que limitações cartográficas tenham resultado em exclusão efetiva de beneficiários legítimos, sem prejuízo de que verificação futura possa documentar casos específicos.

---

**Critérios dos efeitos:**

Os critérios abaixo fundamentam *por que* os efeitos identificados são adversos. São distintos dos critérios da Situação Encontrada (C1-C8), que fundamentam o desvio entre o que é e o que deveria ser.

**CE1. Lei nº 11.326/2006, art. 3º, inciso I** (peça 80, p. 1) — Estabelece o limite de 4 módulos fiscais como requisito de elegibilidade. A verificação desse requisito depende de dados de localização confiáveis. A taxa de erro de 45,92% (EP2) limita a capacidade de validação automatizada desse limite, ainda que a verificação não seja realizada exclusivamente pelo CAF (ARG-20).

**CE2. Decreto nº 9.064/2017, art. 4º** (peça 81) — O CAF é instrumento de identificação e qualificação. A localização do imóvel integra a função de qualificação; a limitação na individualização cartográfica (EP1) e a redução de confiabilidade dos dados de localização (EP2) afetam essa capacidade.

**CE3. Decreto nº 10.046/2019, art. 1º, inciso IV** — Dever de melhoria da qualidade e fidedignidade dos dados. A elevação da taxa de erro de 32,66% para 45,92% na migração para o CAF 3.0 (EP2) e a degradação de precisão na transição Leaflet (EP3) contrariam esse dever.

**CE4. COBIT 2019, BAI10** — Gestão de mudanças. A remoção de validações de bounding box sem testes de regressão e a implementação do Leaflet sem validação de consistência municipal configuram insuficiência no processo de gestão de mudanças, cujo efeito é a degradação documentada em EP3.

**CE5. DAMA-DMBOK v2** (peça 86) — Governança de qualidade de dados e interoperabilidade. Dados geoespaciais de baixa confiabilidade limitam a capacidade de produzir análises territoriais fidedignas (EP4) e elevam o custo de governança interorganizacional quando há consumo externo de dados (EP5). O referencial fundamenta por que dados incorretos em um sistema tendem a propagar-se como problema de qualidade em sistemas consumidores.

---

**Evidências dos efeitos:**

| Ref. | Peça | Página | Descrição | Efeito sustentado |
|---|---|---|---|---|
| EE1 | 117 | p. 14-15 | 55,27% dos registros de alta precisão com coordenadas idênticas; projeção de 1,75M imóveis | EP1 (limitação na individualização cartográfica) |
| EE2 | 117 | p. 15 | Leaflet reduziu duplicações: 92,36% → 16,59% em novos cadastros | EP1 (avanço parcial; passivo permanece) |
| EE3 | 123 | p. 2-3 | Caso Salvador/BA: 6.644 imóveis na mesma coordenada (Centro Histórico) | EP1 (caso emblemático) |
| EE4 | 119 | p. 9 | Taxa de erro cartográfico: 32,66% → 45,92% (+40,6%), afetando ~1,46M imóveis | EP2 (redução da confiabilidade) |
| EE5 | 114 | p. 6-7 | Erros algorítmicos: 20,31% → 32,07% (+11,76 p.p.); geoespaciais: 12,35% → 13,85% (+1,50 p.p.) | EP2 (desagregação por tipo — valores absolutos e variação) |
| EE6 | 118 | p. 16 | Trade-off Leaflet: erros algorítmicos -99,95%, erros geoespaciais +174% | EP3 (degradação em transição) |
| EE7 | 115 | p. 6 | Perda de precisão decimal: -14,33 p.p. em alta precisão pós-Leaflet | EP3 (regressão de qualidade) |
| EE8 | 118 | p. 24, 36 | Leaflet: seleção visual sem validação de consistência municipal | EP3 (mecanismo da degradação) |
| EE9 | 161 | p. 1-4 | Reanálise ministerial: 558/608 reclassificados; materialidade residual em 50 municípios | EP4 (dimensionamento residual da distorção) |
| EE10 | 161 | p. 2 | PNRA: área total sem fração individual gera excesso nominal na leitura agregativa | EP4 (calibração — causa da inflação aparente) |
| EE11 | 150 | p. 43 | Dado geoespacial é acessório no regime jurídico do CAF (ARG-20) | EP2 e EP5 (calibração — delimitação do alcance) |
| EE12 | 150 | p. 44 | APIs sociais não compartilham dado georreferenciado automaticamente (ARG-20) | EP5 (calibração — propagação limitada) |
| EE13 | 150 | p. 34-35 | Achado II é problema geoespacial, não de finalidade jurídica (ARG-15) | Todos os efeitos (calibração — tom operacional) |
| EE14 | 150 | p. 35-37 | Duplicação ≠ duplicidade jurídica; famílias agregadas (ARG-17) | EP1 (calibração — não presunção de fraude) |
| EE15 | 150 | p. 65-67 | Encaminhamentos prospectivos e orientados por risco (ARG-21) | EP4 e EP5 (calibração — proporcionalidade da resposta) |
| EE16 | 119 | p. 9 | Taxa de erro de 45,92% no CAF 3.0 — coordenadas podem associar imóvel a município diferente | Prejuízo social (i) — risco de classificação territorial equivocada |
| EE17 | 117 | p. 14-15 | 1,75M imóveis com coordenadas idênticas — dificuldade de individualização em análises territoriais | Prejuízo social (ii) — risco de invisibilidade geográfica |

### Causas

As causas a seguir explicam *por que* as limitações geoespaciais se acumularam ao longo das transições tecnológicas do CAF — os mecanismos específicos de validação, integração e gestão de mudanças cuja insuficiência permitiu a deterioração documentada. As causas foram extraídas do relatório de auditoria (peça 141, §§103-109) e calibradas pelas análises do contraditório. Conforme reconhecido pelo gestor (ARG-20), as causas são de mecanismos cartográficos específicos, não de deficiência estrutural genérica de governança.

**Causas de processo:**

**CP1 — Remoção da validação de bounding box na migração para o CAF 3.0 sem testes de regressão.** O CAF 2.x rejeitava coordenadas fora do envelope geográfico do Brasil; a migração para o CAF 3.0, em 26/3/2025, relaxou essa validação, passando a aceitar coordenadas no intervalo mundial válido sem verificar pertinência ao território brasileiro (peça 119, p. 34; peça 141, §103). A alteração foi implementada sem testes de regressão que detectassem a deterioração do controle antes da entrada em produção. Esse mecanismo é a causa direta da elevação dos erros algorítmicos documentada na Dimensão 1 da SE. *Corrigível pela Proposta 2.2 (gestão de mudanças — prevenção de regressões).*

**CP2 — Implementação do Leaflet sem validação de consistência municipal.** A interface Leaflet, implementada em agosto/2025, substituiu a digitação manual de coordenadas por seleção visual em mapa, eliminando erros de digitação. Contudo, a seleção livre em mapa não incorporou trava de validação que verifique se o ponto selecionado está dentro dos limites do município declarado (peça 118, p. 24, 36; peça 141, §106). A ausência dessa validação é a causa direta da elevação dos erros geoespaciais documentada nas Dimensões 3 e 5 da SE. A causa não é a interface em si — que trouxe ganhos relevantes reconhecidos em FC1 —, mas a insuficiência de validação de consistência municipal no seu desenho. *Corrigível pelas Propostas 2.1.2 (integridade de dados críticos) e 2.2 (gestão de mudanças).*

**CP3 — Ausência de indicadores formais de qualidade geoespacial que tornassem visível a magnitude do passivo.** O sistema não dispunha de métricas formais que medissem taxas de duplicação, consistência municipal ou inflação cadastral da base ativa (peça 141, §104). Sem visibilidade sobre a magnitude do problema — 55,27% de duplicações e 15,92% de inconsistências municipais —, a gestão não tinha como priorizar ações de saneamento nem dimensionar o esforço necessário. A consequência foi que a melhoria tecnológica implementada (Leaflet) aplicou-se apenas à interface de novos cadastros, sem que houvesse evidência quantitativa que justificasse investimento no passivo (peça 141, §105). A ausência de métricas é mecanismo causal distinto da existência de duplicatas em si: o passivo geoespacial foi gerado pelos defeitos documentados em CP1 (bounding box) e CD2 (ingestão sem unicidade), enquanto CP3 explica por que o passivo permaneceu invisível e intocado. *Corrigível pela Proposta 2.3 (monitoramento contínuo com indicadores).*

**Causas de produto:**

**CD1 — Ausência de harmonização de dados na integração PNRA/Incra.** A integração com a base do Incra/PNRA, disciplinada pela Portaria Conjunta MDA-INCRA nº 3/2025, migrou registros de beneficiários de assentamentos com a área total do assentamento, sem discriminação da fração ideal do lote por beneficiário (peça 161, p. 2; ARG-19). A ausência de etapa de transformação ou normalização dos dados migrados — que compatibilizasse a modelagem de área do PNRA com a granularidade individual exigida pelo CAF — produziu excesso nominal na leitura agregativa por município, contribuindo para a inflação cadastral documentada na Dimensão 4 da SE. Na reanálise ministerial, 535 dos 608 municípios com cobertura ≥ 100% tinham incidência de beneficiários do PNRA (peça 161, p. 2-3). *Corrigível pela Proposta 2.1.2 (integridade de dados críticos) e, prospectivamente, pela Proposta 2.2 (gestão de mudanças — prevenção de regressões em futuras integrações).*

**CD2 — Modelo de dados sem restrição de unicidade espacial e sem validação de plausibilidade geográfica na ingestão.** O modelo de dados do CAF não impõe restrição de unicidade composta sobre o par (id_imovel, coordenada_geográfica), permitindo que múltiplos registros sejam gravados com coordenadas idênticas sem alerta nem bloqueio — mecanismo que gerou o acúmulo de 55,27% de duplicações (peça 141, §108). No caso emblemático de Salvador/BA, 6.644 imóveis foram cadastrados na mesma coordenada (-12,960000°, -38,510000°) porque o sistema aceita qualquer ponto dentro do intervalo válido sem verificar plausibilidade de concentração (peça 123, p. 2-3). Adicionalmente, a ingestão não realizava verificação cruzada com malhas oficiais do IBGE para validar se a coordenada informada pertencia ao município declarado (peça 141, §109), permitindo o acúmulo de inconsistências territoriais. A falha é preventiva, na camada de ingestão e persistência, e não meramente de detecção posterior. *Corrigível pelas Propostas 2.1.2 (integridade) e 2.2 (gestão de mudanças).*

**Fatores contribuintes (contexto):**

**FC1 — Implantação recente do Leaflet como trade-off operacional.** A implementação ocorreu durante a execução da auditoria, após comunicação de erros preliminares ao gestor na reunião de abertura (peça 72, p. 1), e trouxe ganhos relevantes — eliminação da quase totalidade dos erros algorítmicos e redução expressiva de duplicações em novos cadastros (ARG-16; peça 150, p. 35, 40) —, mas com trade-offs em precisão geoespacial e consistência municipal.

**FC2 — Heterogeneidade do passivo (DAP, CAF 2.x, CAF 3.0, Leaflet).** A base compreende registros de diferentes gerações tecnológicas com padrões de qualidade distintos, dificultando curadoria uniforme.

**FC3 — Práticas de cadastramento inadequado pela rede.** Padrões como a "referência de sede municipal" e duplicações massivas (caso Salvador/BA) indicam práticas sistemáticas na ponta que o controle tecnológico pode mitigar, mas não eliminar integralmente (peça 141, §107; peça 123, p. 2-3).

**Conexão causa → proposta:** as causas de processo e produto (CP1-CP3, CD1-CD2) são corrigíveis pelas Propostas 2.1.2, 2.2 e 2.3, conforme indicado em cada causa. A Proposta 1 (determinação transversal) endereça o conjunto das causas dos quatro achados, incluindo o passivo geoespacial.

---

**Critérios das causas:**

Os critérios abaixo fundamentam *por que* os mecanismos identificados constituem causas. São distintos dos critérios da SE e dos Efeitos.

**CC1. COBIT 2019, BAI10 — Gestão de mudanças** — Recomenda testes de regressão e controles de qualidade antes de colocar novas versões em produção. **Mecanismo causal:** na migração para o CAF 3.0, a alteração do intervalo de aceitação de coordenadas (de envelope brasileiro para intervalo mundial) não passou por bateria de testes de regressão que comparasse a distribuição de erros antes e depois da mudança — o que teria detectado a elevação de 20,31% para 32,07% em erros algorítmicos antes da entrada em produção (CP1). Analogamente, o Leaflet foi implantado sem teste de consistência que verificasse se pontos selecionados em mapa caíam dentro do município declarado — teste que teria revelado a elevação de 174% em erros geoespaciais antes de afetar cadastros reais (CP2). Em ambos os casos, o mecanismo é o mesmo: ausência de gate de qualidade no pipeline de deploy que compare métricas de integridade geoespacial entre versões.

**CC2. DAMA-DMBOK v2 — prevenção na entrada e curadoria** (peça 86, p. 38) — Controles preventivos na origem são mais eficazes que inspeção posterior. A ausência de controles de unicidade e plausibilidade (CD2) e de curadoria do passivo (CP3) viola esse princípio. **Ancoragem:** Ac. 457/2026-Plenário.

**CC3. ISO 19157-1:2023 — Qualidade de dados geoespaciais** (peça 83) — Acurácia posicional e consistência lógica. A ausência de validação de pertinência territorial (CP1, CP2) e de controles de unicidade (CD2) contraria as dimensões de qualidade desse referencial.

**CC4. Decreto nº 10.046/2019, art. 1º** (peça 82) — Governança de dados na APF: interoperabilidade e melhoria da qualidade. A integração PNRA sem harmonização (CD1) e a interoperabilidade limitada com IBGE/Incra (CD2) contrariam esse dever.

---

**Evidências das causas:**

| Ref. | Peça | Página | Descrição | Causa sustentada |
|---|---|---|---|---|
| EC1 | 119 | p. 34 | Relaxamento de bounding box: CAF 3.0 aceita intervalo mundial sem verificar envelope brasileiro | CP1 (mecanismo) |
| EC2 | 118 | p. 24, 36 | Leaflet: seleção visual sem trava de consistência municipal | CP2 (mecanismo) |
| EC3 | 141 | §103 | Transições evidenciam ausência de testes de regressão antes da produção | CP1, CP2 (insuficiência de gestão de mudanças) |
| EC4 | 141 | §104 | Inexistência de métricas formais e rotinas de monitoramento geoespacial | CP3 (ausência de curadoria) |
| EC5 | 141 | §105 | Estratégia focou em novos cadastros, sem plano de remediação do passivo | CP3 (foco prospectivo sem retroação) |
| EC6 | 161 | p. 2 | PNRA: área total do assentamento sem fração individual por beneficiário | CD1 (modelo de integração) |
| EC7 | 161 | p. 2-3 | 535/608 municípios com cobertura ≥ 100% tinham incidência PNRA | CD1 (magnitude da contribuição) |
| EC8 | 141 | §108 | Fragilidade dos filtros automatizados; sem críticas automáticas de integridade | CD2 (ausência de controles) |
| EC9 | 141 | §109 | Integração deficiente com IBGE e Incra para checagens de consistência territorial | CD2 (interoperabilidade limitada) |
| EC10 | 72 | p. 1 | Reunião de abertura: equipe comunicou erros preliminares ao gestor (Leaflet como resposta) | FC1 (contexto de implantação) |
| EC11 | 123 | p. 2-3 | Caso Salvador/BA: 6.644 imóveis na mesma coordenada — prática de cadastramento inadequado | FC3 (padrão na rede) |
| EC12 | 141 | §106 | Inexistência de requisitos não funcionais formalizados para integridade geoespacial | CP1, CP2 (insuficiência de formalização) |
| EC13 | 150 | p. 40-41 | Gestor prefere "insuficiência de validações específicas" a "deficiência estrutural de governança" (ARG-20) | Calibração: causas específicas, não genéricas |

### Boas Práticas e Avanços

Não foram identificadas, no escopo deste achado, boas práticas no sentido estrito da NAT §160 — práticas que, cumulativamente, ultrapassem o cumprimento do dever legal, sejam significativas, inovadoras e efetivas, e possam ser propostas para extensão a outros órgãos. Os avanços implementados pelo gestor — implementação da interface Leaflet que reduziu duplicações em novos cadastros de 92,36% para 16,59% e eliminou 99,95% dos erros algorítmicos, implantação de controles que reduziram a inflação cadastral de 10,89% para 0,31%, e redução de coordenadas fora do território brasileiro de 1.688 para 1 registro — foram factualmente reconhecidos na Situação Encontrada e nos Fatores Contribuintes (FC1–FC3), onde contextualizam a capacidade de resposta institucional e informam a proporcionalidade dos encaminhamentos. Registre-se que a interface Leaflet, embora represente avanço na redução de duplicações, foi implementada durante a execução da auditoria em resposta a erros preliminares comunicados, e introduziu regressão de 174% em erros geoespaciais e perda de 14,33 p.p. em precisão decimal — circunstâncias que, somadas ao caráter reativo da implementação, impedem seu enquadramento como achado positivo.

### Encaminhamentos

**Determinação:**

**Proposta 1.** Determinar ao MDA que, no prazo de 180 dias, elabore e encaminhe ao TCU plano de ação, com responsáveis, prazos e forma de comunicação do cumprimento, para avaliar as situações identificadas neste relatório e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, abrangendo as inconsistências documentadas na qualidade dos **dados de entrada**, dos **dados geoespaciais**, dos **dados cadastrais** e dos **metadados** do CAF, em conformidade com os critérios de elegibilidade previstos no art. 3º da Lei 11.326/2006 e com a finalidade de identificação e qualificação estabelecida no art. 4º do Decreto 9.064/2017.

*Justificativa do vínculo:* a determinação decorre da situação encontrada nas cinco dimensões do ACH-02 — taxa de erro cartográfico (45,92%), duplicações espaciais (55,27%), inconsistência municipal (15,92%), inflação cadastral (632 municípios) e degradação de precisão (Leaflet) — e dos efeitos potenciais documentados (EP1-EP5). O componente "dados geoespaciais" da determinação corresponde ao escopo deste achado.

**Recomendações:**

**Proposta 2.1.2.** Garantir integridade e consistência dos dados críticos do CAF, por meio de controles que reduzam erros e anomalias em campos essenciais à identificação do beneficiário, localização do imóvel e elegibilidade cadastral.

*Justificativa do vínculo:* decorre da Dimensão 1 (taxa de erro cartográfico de 45,92%) e da Dimensão 3 (15,92% de registros fora do município declarado), que evidenciam insuficiência de controles de consistência em campos de localização. O componente "localização do imóvel" da proposta é diretamente aplicável.

**Proposta 2.2.** Aprimorar gestão de mudanças e garantia da qualidade do Sistema CAF, prevenindo que novas versões introduzam regressões funcionais ou comprometam integridade dos dados.

*Justificativa do vínculo:* decorre diretamente da Dimensão 1 (relaxamento de validações de bounding box na migração para o CAF 3.0) e da Dimensão 5 (trade-off Leaflet sem validação de consistência municipal), que configuram regressões funcionais introduzidas por novas versões do sistema sem testes de regressão adequados (CE4 — COBIT 2019, BAI10).

**Proposta 2.3.** Implementar monitoramento contínuo da qualidade dos dados do CAF, com indicadores que permitam identificar e priorizar ações corretivas e avaliar efetividade das medidas.

*Justificativa do vínculo:* decorre dos efeitos potenciais EP4 (distorção analítica) e EP5 (propagação de erros), e da constatação de que taxas elevadas de erro e duplicações massivas passaram despercebidas sem rotinas de monitoramento, conforme documentado na SE (Dimensão 2: 92,36% de duplicações pré-Leaflet sem detecção).

### Benefícios Esperados

**Benefícios quantitativos:**

a) Redução da taxa de erro cartográfico de 45,92% (aproximadamente 1,46 milhão de imóveis afetados), com meta a definir pelo gestor no plano de ação (Proposta 1) — reversão parcial de EP2.

b) Redução da taxa de duplicações espaciais de 55,27% (aproximadamente 1,75 milhão de imóveis com coordenadas idênticas a outros registros), com meta a definir pelo gestor (Proposta 2.1.2) — reversão parcial de EP1.

c) Consolidação dos ganhos do Leaflet em novos cadastros (duplicações reduzidas de 92,36% para 16,59%) e extensão da curadoria ao passivo histórico, com meta a definir pelo gestor (Propostas 2.1.2 e 2.2) — reversão parcial de EP1.

d) Redução da taxa de inconsistência municipal de 15,92% dos registros com coordenadas fora do município declarado, com meta a definir pelo gestor (Proposta 2.1.2) — reversão parcial de EP2.

**Benefícios qualitativos:**

a) Fortalecimento da capacidade de individualização cartográfica da base cadastral (reversão de EP1), viabilizando cruzamentos com bases ambientais e fiscalizações de sobreposição em áreas protegidas (Proposta 2.1.2).

b) Melhoria da confiabilidade de validações baseadas em dados cartográficos (reversão de EP2), com recuperação da capacidade do sistema de sustentar a verificação do requisito legal de 4 módulos fiscais (Proposta 2.1.2).

c) Prevenção de regressões de qualidade em futuras transições tecnológicas (reversão de EP3), mediante gestão de mudanças com testes de regressão que comparem métricas de integridade geoespacial entre versões (Proposta 2.2).

d) Redução do risco de distorção analítica em decisões públicas baseadas em dados geoespaciais do CAF (reversão de EP4), mediante monitoramento contínuo com indicadores de qualidade cartográfica que tornem visível a magnitude do passivo (Proposta 2.3).

e) Mitigação do risco de propagação de erros em integrações externas futuras (reversão de EP5), mediante aprimoramento da confiabilidade da base geoespacial antes da ampliação de integrações com agências de crédito e órgãos ambientais (Propostas 2.1.2 e 2.3).

---

## ACH-03 — Lacunas na governança, no cadastramento e na curadoria dos dados do CAF

**Frase-síntese:**

Devido a lacunas nos processos de cadastramento, curadoria e integração com bases oficiais do CAF, **ocorreu** a permanência de inconsistências cadastrais em múltiplas dimensões — capacidade civil, dados de contato, consistência de renda e compatibilidade de atividade econômica —, em desacordo com a finalidade de identificação e qualificação estabelecida no art. 4º do Decreto nº 9.064/2017, **o que levou** à limitação da qualidade cadastral do sistema, **impactando** a capacidade de comunicação com os cadastrados e a precisão da focalização das políticas públicas de agricultura familiar.

---

### Situação Encontrada

A auditoria identificou lacunas na governança, no cadastramento e na curadoria dos dados do CAF que limitam a qualidade cadastral do sistema em quatro dimensões interdependentes: capacidade civil dos responsáveis, dados de contato, consistência de renda e compatibilidade de atividade econômica. O diagnóstico descreve o padrão de "vazio semântico" documentado no V1: o sistema valida a sintaxe dos dados (formato de CPF, presença de "@" no e-mail, preenchimento dos campos obrigatórios), mas não verifica adequadamente o conteúdo semântico — se o dado é verdadeiro, funcional e plausível. A análise baseou-se em verificação censitária da base de 2.905.101 responsáveis ativos por UFPAs (peça 124, p. 8) e considerou os argumentos apresentados pelo gestor (peça 150, p. 48-56), cujas análises constam do Anexo — Análise dos Comentários dos Gestores.

**Dimensão 1 — Capacidade civil e identidade dos responsáveis.** O cruzamento censitário do cadastro CAF com a base da Receita Federal e o Sistema de Óbitos (Sisobi) identificou 15.811 inconsistências de capacidade civil (0,544% da população base), distribuídas em seis categorias de comprometimento (peça 124, p. 8). A constatação mais grave refere-se a 3.097 responsáveis com óbito confirmado no Sisobi que permanecem como titulares ativos de UFPA (peça 124, p. 9). Adotou-se o critério conservador de contabilizar apenas óbitos confirmados simultaneamente na base da RFB e no Sisobi — o cruzamento inicial com a RFB indicou 12.820 CPFs com situação "Titular Falecido" (peça 124, p. 15), mas a equipe adotou o critério mais restritivo (confirmação em ambas as fontes) para mitigar falsos positivos, porque apenas o Sisobi fornece a data exata do falecimento necessária para comprovar a inelegibilidade temporal. Complementam o quadro 89 menores de 16 anos absolutamente incapazes (peça 124, p. 8), 49 adolescentes de 16-17 anos não declarados como emancipados, 57 registros com datas de nascimento futuras — incluindo casos com anos 2084, 2083 e 2082 (peça 131, p. 4) —, 11.999 divergências de data de nascimento entre CAF e RFB (peça 124, p. 10) e 520 CPFs não localizados na base da Receita Federal (peça 124, p. 10).

A proporção de 0,544% na base é baixa em termos relativos, e o CAF 3.0 incorporou controles sistêmicos voltados à capacidade civil — consulta à RFB via BCadastro/ConectaGOV (RN 1.2) e vedação de responsabilidade por UFPA a menores (RN 1.8) (peça 150, p. 48) (ARG-22). Esses controles justificam tratamento proporcional e distinção entre passivo acumulado (registros pré-CAF 3.0) e situação corrente. Todavia, a baixa materialidade relativa não reduz a gravidade qualitativa dos casos individuais: a manutenção de 3.097 responsáveis falecidos como titulares ativos configura inconsistência de alta sensibilidade jurídico-administrativa, como o próprio gestor reconhece (peça 150, p. 53). A distribuição temporal dos óbitos revela acúmulo de registros não saneados: 20,8% entre 2010-2015, 39,5% entre 2016-2020 e 39,7% entre 2021-2025, incluindo caso com falecimento há mais de quatorze anos (peça 124, p. 9).

**Dimensão 2 — Dados de contato.** A análise dos 6.525.658 registros de e-mail de pessoas físicas revelou que 90,62% são fictícios ou inválidos, com o padrão mais frequente sendo "naopossui@mail.com" (75,16% da base) (peça 125, p. 6). Em contraste, 99,70% dos e-mails de pessoas jurídicas são válidos (peça 125, p. 7) — uma diferença de 90,32 pontos percentuais (peça 125, p. 8) que demonstra que o problema não é técnico (o sistema aceita e-mails válidos quando o perfil do cadastrado o propicia), mas processual: para PJ o e-mail é ferramenta operacional indispensável; para PF no contexto do CAF é frequentemente percebido como formalidade. Quanto aos CEPs, 93,7% são genéricos, com terminação -000 (peça 125, p. 1).

Essas métricas devem ser lidas à luz da realidade material do público rural (ARG-23). O gestor demonstra que aproximadamente dois terços das pessoas inscritas no CAF possuem baixa escolaridade, que o uso de correio eletrônico pelo público rural é limitado — com preferência por aplicativos como WhatsApp — e que a declaração de e-mail foi tornada não obrigatória no registro das UFPAs (peça 150, p. 49). Quanto aos CEPs, existem 1.469 municípios brasileiros com apenas um CEP — o CEP genérico (terminação -000) — conforme Censo IBGE 2022 (peça 150, p. 49-50), o que significa que parte expressiva dos CEPs genéricos no CAF decorre da estrutura do endereçamento postal brasileiro, não de falha de cadastramento. Essas considerações contextualizam a causa, mas não eliminam a limitação funcional: independentemente da origem, a qualidade dos dados de contato reduz a capacidade do Estado de se comunicar com o público do CAF quando necessário — o problema documentado é de capacidade de comunicação, não de culpa do cadastrado.

**Dimensão 3 — Consistência de renda.** A análise censitária de 3.304.174 UFPAs ativas identificou 907 registros com renda anual declarada superior a R$ 1 milhão (0,027%), dos quais 141 ultrapassam R$ 10 milhões, incluindo caso extremo com renda anual superior a R$ 167 milhões (peça 130, p. 3; peça 126, p. 25; peça 128, changelog: correção de 139 para 141 registros). As hipóteses explicativas incluem erro de unidade (centavos sem vírgula), renda acumulada de múltiplos anos, faturamento de cooperativa confundido com renda individual ou erro de digitação. A consulta às Regras de Negócio do CAF 3.0 revelou que a RN1.32 estabelece teto de R$ 500 mil para enquadramento no Pronaf, mas funciona como filtro de classificação, não como trava de entrada — permitindo que valores manifestamente implausíveis sejam gravados na base (peça 78).

Registre-se que o marco normativo do CAF não estabelece teto geral de renda bruta familiar para inscrição (ARG-24). A Lei nº 11.326/2006, inciso III do art. 3º, disciplina a composição da renda — percentual mínimo originado do estabelecimento —, e não seu valor absoluto. O Decreto nº 9.064/2017 regulamenta esse requisito como ao menos metade da renda. Os limites de renda são estabelecidos pelas políticas públicas específicas (Pronaf, PAA), não pelo cadastro em si. Os registros com valores extremos permanecem úteis como indícios de risco que justificam monitoramento e curadoria — erro de preenchimento, desatualização ou necessidade de verificação individual —, mas não constituem prova automática de inelegibilidade ao CAF.

**Dimensão 4 — Compatibilidade de atividade econômica (CNAE).** O cruzamento dos 9.687 CNPJs cadastrados com a base da RFB identificou 39 pessoas jurídicas (0,40%) com CNAE principal incompatível com a agricultura familiar — 17 hipermercados, 8 atacadistas, 4 construtoras e 10 de outras atividades (peça 127, p. 5). Embora numericamente pequenas, essas entidades concentram 10.377 dos 774.405 agricultores vinculados a PJs (1,34%), incluindo caso extremo de hipermercado com capital de R$ 12,5 milhões e 1.847 agricultores vinculados (peça 127, p. 5-6).

Registre-se que o Decreto nº 9.064/2017, inciso VI do art. 2º, admite como atividades do empreendimento familiar rural não apenas a produção agropecuária (Seção A da CNAE), mas também beneficiamento, processamento, comercialização e turismo rural (ARG-25). Isso significa que a Seção A não é a única seção com atividades potencialmente compatíveis, de modo que o CNAE funciona como ferramenta auxiliar de triagem e curadoria, não como critério exclusivo de inelegibilidade. A existência de CNAEs manifestamente incompatíveis — hipermercados, construtoras, atacadistas — permanece como indício que justifica verificação individualizada, como o próprio gestor reconhece (peça 150, p. 52).

**Contexto e concordância parcial do gestor.** O gestor concordou expressamente com a causa raiz 4 — insuficiência de governança de dados — admitindo que a insuficiência se relaciona ao processo de maturação e implementação da política de governança de dados do órgão (peça 150, p. 53) (ARG-26). Essa concordância preserva a sustentação central do achado. O CAF 3.0 representa avanço em relação às versões anteriores, com integração com bases da RFB e do CNIS (peças 71, 72 e 74). Os problemas cadastrais identificados são compatíveis com um sistema em fase de maturação: existem controles, mas sua cobertura e tempestividade ainda não alcançam a totalidade do passivo acumulado.

---

### Critérios da Situação Encontrada

**C1. Lei nº 11.326/2006, art. 3º, incisos I a IV** (peça 80, p. 1) — Requisitos cumulativos de elegibilidade da agricultura familiar. **Aplicação:** o inciso III disciplina a composição da renda (percentual mínimo do estabelecimento), não valor absoluto — registros com renda extrema são indícios de risco, não prova de inelegibilidade (ARG-24).

**C2. Decreto nº 9.064/2017, arts. 2º e 4º** (peça 81) — Art. 2º, VI: atividades compatíveis incluem beneficiamento, processamento, comercialização e turismo rural, não apenas Seção A da CNAE (ARG-25). Art. 4º: finalidade do CAF como instrumento de identificação e qualificação. **Aplicação:** os dados cadastrais (identidade, contato, renda, atividade) são os insumos primários dessa função de identificação e qualificação.

**C3. Portaria MDA nº 19/2025, arts. 8º, 27 e 28** (peça 108) — Art. 8º: documentos obrigatórios. Art. 27, II: veda inscrição de PJ com atividade incompatível. Art. 28: bloqueio por inconsistência cadastral. **Aplicação:** os 10.377 agricultores vinculados a 39 PJs com CNAEs incompatíveis podem estar sujeitos ao art. 28.

**C4. Código Civil (Lei nº 10.406/2002), arts. 3º, 4º e 6º** — Art. 3º: absolutamente incapazes (< 16 anos). Art. 4º, I: relativamente incapazes (16-17 não emancipados). Art. 6º: morte extingue personalidade jurídica. **Aplicação:** fundamenta a gravidade jurídica dos 3.097 falecidos e 138 menores/adolescentes incapazes como titulares de UFPA.

**C5. DAMA-DMBOK v2** (peça 86) — Curadoria do ciclo de vida dos dados, qualidade preventiva, governança. **Aplicação:** a ausência de curadoria periódica permitiu acúmulo de 3.097 óbitos ao longo de mais de uma década sem detecção. **Ancoragem:** Ac. 457/2026-TCU-Plenário (unanimidade).

**C6. Acórdãos 1197/2018-TCU-Plenário → 1866/2021-TCU-Plenário → 885/2024-TCU-Plenário** — Reincidência DAP/CAF. **Aplicação:** problemas de qualidade cadastral não são inéditos; deliberações anteriores permanecem pendentes.

**C7. ISO/IEC 25012:2008** (peça 85) — Completude, acurácia, atualidade, consistência. **Aplicação:** o sistema atinge 100% de completude formal (campos preenchidos), mas menos de 10% de validade real em e-mails de PF — evidenciando a distinção entre completude sintática e acurácia semântica. Critério secundário.

---

### Evidências da Situação Encontrada

**Evidências analíticas (cruzamentos censitários):**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E1 | 124 | p. 8 | População base: 2.905.101 responsáveis ativos; total de 15.811 inconsistências (0,544%) | Dimensão 1 — magnitude total |
| E2 | 124 | p. 9 | Óbitos confirmados no Sisobi: 3.097 responsáveis falecidos ativos | Dimensão 1 — constatação principal |
| E3 | 124 | p. 15 | Cruzamento inicial RFB: 12.820 CPFs "Titular Falecido" (triagem bruta, antes da confirmação Sisobi) | Dimensão 1 — distinção triagem vs. confirmação |
| E4 | 124 | p. 9 | Distribuição temporal: 20,8% (2010-15), 39,5% (2016-20), 39,7% (2021-25); caso mais antigo: 2011 | Dimensão 1 — acúmulo histórico |
| E5 | 124 | p. 8 | Menores: 89 (< 16 anos) + 49 (16-17 não emancipados); datas futuras: 57 registros | Dimensão 1 — outras categorias |
| E6 | 124 | p. 10 | Divergências de nascimento: 11.999; CPFs não localizados: 520 | Dimensão 1 — comprometimento de cruzamentos |
| E7 | 131 | p. 4 | Datas de nascimento futuras: anos 2084, 2083, 2082 (erro de digitação de século) | Dimensão 1 — evidência de ausência de validação |
| E8 | 125 | p. 6 | E-mails PF: 90,62% fictícios; padrão "naopossui@mail.com" = 75,16% | Dimensão 2 — e-mails |
| E9 | 125 | p. 7 | E-mails PJ: 99,70% válidos | Dimensão 2 — contraponto PJ |
| E10 | 125 | p. 8 | Diferença PF/PJ: 90,32 p.p.; CEPs específicos com divergência de UF: 18,9% | Dimensão 2 — dicotomia processo/público |
| E11 | 125 | p. 1 | CEPs genéricos (-000): 93,7% (3.318.270 de 3.540.310) | Dimensão 2 — CEPs |
| E12 | 130 | p. 3 | Outliers de renda: 907 > R$ 1M; 141 > R$ 10M (corrigido de 139, peça 128 changelog); extremo > R$ 167M | Dimensão 3 — magnitude |
| E13 | 130 | p. 4 | Distorção da média nacional: +2,06% (R$ 57.129 → R$ 58.307) | Dimensão 3 — impacto estatístico |
| E14 | 127 | p. 5 | CNAEs incompatíveis: 39 PJs (0,40%), 10.377 agricultores (1,34% dos vínculos PJ) | Dimensão 4 — magnitude |
| E15 | 127 | p. 5-6 | Detalhamento: 17 hipermercados, 8 atacadistas, 4 construtoras, 10 outras; caso extremo: 1.847 agricultores | Dimensão 4 — tipologia |

**Evidências documentais (normas e regras de negócio):**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E16 | 78 | p. 7-8 (RN1.22-RN1.32) | Regras de Negócio CAF 3.0: RN1.32 estabelece teto R$ 500 mil para Pronaf como filtro de classificação, não trava de entrada | Dimensão 3 — ausência de trava de plausibilidade |
| E17 | 108 | p. 5 | Portaria MDA 19/2025, arts. 8º, 27 e 28 — requisitos de cadastramento e vedações | Critério C3 |
| E18 | 137 | p. 165 | MCR/BACEN: teto de renda do Pronaf (evolução R$ 360 mil → R$ 500 mil) | Dimensão 3 — parâmetros de referência |

**Evidências testemunhais e consensuais:**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E19 | 72 | p. 2 | Reunião técnica: CPF sem chave primária gera dificuldades de cruzamento e pagamentos a falecidos | Dimensão 1 — reconhecimento do problema |
| E20 | 73 | p. 3 | Ata de reunião: consenso sobre carência de mecanismos automatizados de validação | Reconhecimento mútuo |
| E21 | 74 | p. 4 | Ata de encerramento: problemas originados do legado CAF 2.0 | Passivo/corrente |

**Elementos do contraditório incorporados:**

| Ref. | Peça | Página | Descrição | Calibração aplicada |
|---|---|---|---|---|
| E22 | 150 | p. 48 | Controles CAF 3.0: RN1.2 (BCadastro/ConectaGOV), RN1.8 (vedação menores) (ARG-22) | Dimensão 1: existência de controles, materialidade < 1%, proporcionalidade |
| E23 | 150 | p. 49-50 | Realidade do público rural: 2/3 baixa escolaridade, e-mail não obrigatório, 1.469 municípios CEP genérico IBGE 2022 (ARG-23) | Dimensão 2: contextualização à realidade rural |
| E24 | 150 | p. 50-51 | Renda: composição (Lei 11.326 III), não teto absoluto; RN1.32 filtra na API do Pronaf (ARG-24) | Dimensão 3: indício de risco, não inelegibilidade |
| E25 | 150 | p. 51-52 | CNAE: Decreto 9.064 art. 2º VI admite beneficiamento, processamento, turismo; triagem, não exclusão (ARG-25) | Dimensão 4: ferramenta de triagem, não critério determinístico |
| E26 | 150 | p. 53 | Gestor concorda expressamente com causa raiz 4 (insuficiência de governança de dados) (ARG-26) | Concordância parcial preserva sustentação do achado |
| E27 | 128 | changelog | Correção: 139 → 141 UFPAs com renda > R$ 10M (upgrade) | Dimensão 3: número corrigido |

---

### Efeitos

A equipe não mapeou efeitos concretos (reais) decorrentes da situação encontrada no Achado III (peça 141, §165). As inconsistências cadastrais identificadas — capacidade civil, dados de contato, consistência de renda e compatibilidade de atividade econômica — produzem efeitos potenciais cuja concretização depende de fatores adicionais, como a forma de operação das políticas usuárias e a conduta de eventuais terceiros. A análise dos efeitos incorpora a recalibragem proposta pelo gestor (ARG-26; peça 150, p. 54): o risco mais diretamente verificável não é o de desvio automático de recursos — pois o CAF é condição necessária, mas não suficiente, para acesso às políticas —, e sim o de aumento do custo operacional e da complexidade de controle para gestores e executores das políticas. Essa formulação é mais precisa e compatível com a natureza operacional da auditoria.

**Efeitos potenciais:**

**EP1 — Risco de comprometimento da focalização de políticas públicas.** A manutenção de 3.097 responsáveis falecidos (confirmados no Sisobi) como titulares ativos de UFPAs (peça 124, p. 9) viola o pressuposto legal de existência de personalidade jurídica para gestão do estabelecimento rural e permite que cadastros permaneçam ativos sem titular juridicamente capaz (peça 141, §166.1). Esses cadastros, permanecendo na base ativa, podem ser utilizados por terceiros para acesso a políticas como Pronaf, PAA e seguros agrícolas, comprometendo a focalização dos recursos nos destinatários legítimos. Registre-se que a materialidade é relativamente baixa — menos de 1% da base de cadastros ativos (ARG-22; peça 150, p. 48) — e que o CAF 3.0 incorporou controles de capacidade civil, incluindo consulta à Receita Federal via BCadastro/ConectaGOV (RN 1.2) e vedação de responsabilidade a menores (RN 1.8) (peça 150, p. 48). A gravidade é qualitativa, não quantitativa: o próprio gestor reconhece a sensibilidade jurídico-administrativa desses casos (peça 150, p. 53). O risco de comprometimento da focalização depende dos filtros próprios de cada política usuária (ARG-11), de modo que inconsistência no CAF não se converte automaticamente em concessão indevida.

**EP2 — Risco de exclusão involuntária de beneficiários legítimos por impossibilidade de comunicação.** A constatação de que 90,62% dos e-mails de pessoa física cadastrados no CAF são fictícios e 93,7% dos CEPs são genéricos (peça 125, p. 6) compromete a capacidade do Estado de comunicar avisos, prazos de renovação, mudanças normativas e suspensões ao público do CAF (peça 141, §166.2). A consequência potencial é que agricultores legítimos podem ter benefícios negados ou interrompidos por falta de notificação sobre atualizações obrigatórias, gerando insegurança jurídica e exclusão involuntária do acesso a direitos, conforme o Decreto 9.064/2017, art. 4°, § 2°: o cadastro ativo no CAF é requisito para acesso às políticas públicas destinadas à UFPA (peça 81; peça 141, §166.2.1). Essa limitação deve ser contextualizada à realidade material do público rural: aproximadamente dois terços das pessoas inscritas no CAF possuem baixa escolaridade, o uso de correio eletrônico pelo público rural é limitado e a preferência recai sobre aplicativos de mensagem como o WhatsApp (ARG-23; peça 150, p. 49). A existência de 1.469 municípios com apenas um CEP genérico (Censo IBGE 2022) confirma que a repetição de CEPs decorre, em grande medida, da estrutura do endereçamento postal brasileiro, e não de falha no cadastramento (peça 150, p. 49-50). O prejuízo potencial não decorre de culpa do agricultor, mas da insuficiência dos mecanismos de cadastramento em ambiente de exclusão digital.

**EP3 — Risco regulatório para agricultores vinculados a PJs com CNAE incompatível.** Os 10.377 agricultores vinculados a 39 pessoas jurídicas com CNAEs manifestamente incompatíveis com a agricultura familiar — hipermercados, atacadistas, construtoras — podem estar sujeitos a risco de bloqueio de acesso a políticas públicas, conforme art. 27 da Portaria MDA 19/2025 (peça 141, §166.3; dados quantitativos em §162). A manutenção desses vínculos ativos significa que esses agricultores poderão ter seus benefícios questionados retroativamente. Registre-se que o CNAE deve funcionar como ferramenta de triagem e análise de risco, não como critério exclusivo e autoexecutável de inelegibilidade (ARG-25; peça 150, p. 51-52): o Decreto 9.064/2017, art. 2°, VI, permite que o empreendimento familiar rural inclua atividades de beneficiamento, processamento, comercialização ou turismo rural (peça 150, p. 52). A materialidade é circunscrita — 39 PJs, correspondendo a 0,40% das PJs cadastradas — e o efeito é proporcional a essa escala.

**EP4 — Risco de aumento do custo operacional e da complexidade de controle.** A acumulação histórica de inconsistências cadastrais sem detecção ou saneamento — incluindo 12.820 CPFs com indicação de óbito na RFB distribuídos ao longo de mais de uma década (peça 141, §166.4) — eleva o custo operacional e a complexidade de controle para gestores e executores das políticas que utilizam o CAF. Essa formulação, proposta pelo gestor como risco mais diretamente verificável que o desvio automático de recursos (ARG-26; peça 150, p. 54), é acolhida pela equipe por ser mais precisa e compatível com a natureza operacional da auditoria.

**Cautela para os encaminhamentos — risco de exclusão de beneficiários legítimos em saneamento indiscriminado.** Embora não constitua efeito do achado em si — pois decorre da forma da resposta institucional, e não da situação encontrada —, o gestor sustenta que medidas massivas de saneamento, quando desacopladas de critérios de risco, materialidade e verificabilidade, tendem a impor ônus desproporcional e podem gerar exclusão de beneficiários legítimos cujos dados cadastrais apresentam inconsistências formais (ARG-30; peça 150, p. 55-56, 72-73). Essa cautela é relevante para a calibração dos encaminhamentos.

---

**Nota sobre quantificação de prejuízos financeiros.** A natureza operacional desta auditoria — focada na qualidade dos dados cadastrais e na capacidade do sistema de sustentar a identificação e qualificação dos beneficiários — não permitiu quantificar prejuízos financeiros diretos ao erário. Tal quantificação exigiria cruzamento individualizado entre os cadastros com inconsistências e os benefícios efetivamente concedidos, análise que extrapola o escopo deste trabalho. Registra-se a ordem de grandeza do universo financeiro que depende do CAF: Pronaf R$ 59,6 bilhões na safra 2023/2024 (peça 141, §30.1); PAA ~R$ 750 milhões em 2024 (peça 141, glossário); PNAE ~R$ 1,6 bilhão à agricultura familiar (peça 141, glossário). No caso específico do Achado III, o risco mais diretamente verificável é o de aumento do custo operacional e da complexidade de controle (ARG-26; peça 150, p. 54), e não o de desvio consumado de recursos — coerentemente com a distinção entre inconsistência cadastral e inelegibilidade definitiva (ARG-02) e com o reconhecimento de que as políticas usuárias possuem filtros próprios (ARG-11).

**Prejuízos sociais potenciais.** Conforme orientação das Normas de Auditoria do TCU (§4 do material didático sobre Efeitos), prejuízos sociais são relevantes para a calibração dos encaminhamentos, mesmo que a materialidade financeira não seja elevada. O Achado III apresenta a dimensão social mais relevante entre os quatro achados desta auditoria. Os riscos sociais a seguir são potenciais — coerentemente com a classificação de todos os efeitos deste achado (peça 141, §165) — e estão documentados nas peças do processo:

(i) *Risco de vulnerabilidade cadastral das famílias cujo titular faleceu:* as 3.097 famílias cujo responsável pela UFPA faleceu — confirmados no Sisobi (peça 124, p. 9; peça 141, §131) — podem encontrar-se em situação de fragilidade cadastral: sem processo estruturado de sucessão no CAF, a família pode ter o acesso às políticas públicas comprometido ou permanecer em situação irregular sem ciência. O acúmulo temporal — 20,8% dos registros de óbito referem-se ao período 2010-2015 (peça 141, §131) — indica que parte dessas famílias pode estar nessa condição há anos.

(ii) *Risco de perda de direitos por falta de notificação:* a limitação nos canais de comunicação — e-mail fictício em 90,62% dos casos, CEP genérico em 93,7% (peça 125, p. 6), afetando aproximadamente 2,6 milhões de famílias (peça 141, §166.2) — pode impedir que o Estado notifique agricultores sobre prazos de renovação, mudanças normativas ou suspensões. Em ambiente de baixa escolaridade e conectividade limitada (ARG-23; peça 150, p. 49), essa limitação pode resultar em perda de direitos por falta de informação, não por inelegibilidade (peça 141, §166.7). O gestor reconhece o desafio e informa providências em curso — formação de mais de 10 mil agentes cadastradores da RedeCAF para 2026 e testes de comunicação via plataforma Gov.BR (peça 150, p. 50).

(iii) *Risco de penalização de agricultores vinculados a PJs com CNAE incompatível:* os 10.377 agricultores vinculados a 39 PJs com CNAEs manifestamente incompatíveis (peça 141, §§162, 166.3) não são necessariamente responsáveis pela irregularidade da pessoa jurídica, mas podem sofrer consequências — bloqueio de acesso a políticas, questionamento retroativo — em razão de vínculo cadastral que não controlam diretamente.

---

**Critérios dos efeitos:**

Os critérios abaixo fundamentam *por que* os efeitos identificados são adversos. São distintos dos critérios da Situação Encontrada.

**CE1. Decreto nº 9.064/2017, art. 4°, § 2°** (peça 81) — O cadastro ativo no CAF é requisito obrigatório para acesso às ações e políticas públicas destinadas à UFPA. A presença de inconsistências cadastrais (titulares falecidos, dados de contato fictícios, PJs incompatíveis) cria risco de comprometimento dessa função habilitadora, tanto por manter cadastros que não deveriam estar ativos (EP1) quanto por gerar risco de exclusão involuntária de beneficiários legítimos (EP2).

**CE2. Lei nº 11.326/2006, art. 3°** (peça 80, p. 1) — Requisitos cumulativos de elegibilidade. A manutenção de titulares que não atendem ao pressuposto de capacidade civil para gestão do estabelecimento (falecidos, menores) frustra a lógica de identificação e qualificação da Lei.

**CE3. Portaria MDA nº 19/2025, art. 27** (peça 108) — Veda inscrição no CAF de PJs com atividades incompatíveis. A permanência de 39 PJs com CNAEs manifestamente incompatíveis na base ativa expõe os 10.377 agricultores vinculados a risco regulatório (EP3).

**CE4. DAMA-DMBOK v2** (peça 86, p. 16 — custo da má qualidade de dados) — Estabelece que o custo de correção de dados cresce exponencialmente com o tempo de permanência do erro na base. A acumulação de 12.820 inconsistências de capacidade civil ao longo de mais de uma década — sem detecção nem saneamento — materializou esse padrão: o esforço de correção retroativa exige cruzamento individualizado com Sisobi/RFB, contato com famílias e atualização cadastral caso a caso, gerando custo operacional significativamente superior ao que teria sido necessário com rotinas tempestivas de detecção (EP4).

---

**Evidências dos efeitos:**

| Ref. | Peça | Página | Descrição | Efeito sustentado |
|---|---|---|---|---|
| EE1 | 124 | p. 9 | 3.097 CPFs com óbito confirmado no Sisobi como titulares ativos; acúmulo temporal: 20,8% (2010-2015), 39,5% (2016-2020), 39,7% (2021-2025) | EP1 (focalização), prejuízo social (i) |
| EE2 | 125 | p. 6 | 90,62% dos e-mails de PF fictícios; 93,7% dos CEPs genéricos | EP2 (comunicação), prejuízo social (ii) |
| EE3 | 141 | §131 | 12.820 CPFs com indicação de óbito na RFB; 138 menores/adolescentes como titulares | EP1 (magnitude), EP4 (acúmulo) |
| EE4 | 141 | §162 | 39 PJs com CNAEs incompatíveis afetando 10.377 agricultores | EP3 (risco regulatório), prejuízo social (iii) |
| EE5 | 141 | §166.1 | Cadastros de falecidos ativos permitem acesso por terceiros a Pronaf, PAA, seguros | EP1 (mecanismo do risco) |
| EE6 | 141 | §166.2 | Impossibilidade de contato com ~2,6 milhões de famílias via e-mail | EP2 (dimensionamento) |
| EE7 | 141 | §166.2.1 | Consequência: exclusão involuntária por falta de notificação (Decreto 9.064/2017, art. 4°, §2°) | EP2 (cadeia normativa) |
| EE8 | 141 | §166.4 | Acumulação de 12.820 óbitos ao longo de anos sem detecção ou saneamento | EP4 (custo operacional acumulado) |
| EE9 | 141 | §166.7 | Risco de exclusão sistêmica por impossibilidade de comunicação (2,6 milhões de famílias) | EP2 e prejuízo social (ii) |
| EE10 | 150 | p. 48 | Materialidade <1%; controles CAF 3.0 existentes (RN 1.2, RN 1.8) (ARG-22) | EP1 (calibração — proporcionalidade) |
| EE11 | 150 | p. 49-50 | E-mail: baixa escolaridade, WhatsApp como alternativa; CEP: 1.469 municípios com CEP genérico (ARG-23) | EP2 (calibração — realidade rural) |
| EE12 | 150 | p. 50 | Providências em curso: formação de 10 mil agentes RedeCAF para 2026; testes Gov.BR | EP2 (mitigação em curso) |
| EE13 | 150 | p. 51-52 | CNAE como triagem, não exclusão; Decreto 9.064/2017, art. 2°, VI (ARG-25) | EP3 (calibração — proporcionalidade) |
| EE14 | 150 | p. 53 | Gestor reconhece gravidade qualitativa da capacidade civil (ARG-22) | EP1 (concordância parcial) |
| EE15 | 150 | p. 54 | Risco mais verificável = custo operacional, não desvio automático (ARG-26) | EP4 (recalibragem acolhida) |
| EE16 | 141 | §30.1, glossário | Pronaf R$ 59,6 bi; PAA ~R$ 750 mi; PNAE ~R$ 1,6 bi | Nota de quantificação financeira |

### Causas

As causas a seguir explicam *por que* as inconsistências cadastrais documentadas nas quatro dimensões do ACH-03 persistiram — os mecanismos específicos de validação, integração e curadoria cuja insuficiência permitiu o acúmulo de dados sintaticamente aceitos, porém semanticamente inválidos ou implausíveis. As causas foram extraídas do relatório de auditoria (peça 141, §§163-164.4) e calibradas pelas análises do contraditório (ARGs 22-26). O diagnóstico não afirma inexistência absoluta de controles — o CAF 3.0 incorporou avanços documentados em FC1 e FC2 —, mas identifica insuficiências específicas nos mecanismos existentes para cada dimensão. No plano das causas, registre-se que o gestor contestou a formulação de "permissividade estrutural" (causa raiz 1 do V1), mas concordou expressamente com a insuficiência de governança de dados (causa raiz 4), reconhecendo que "a insuficiência se relaciona ao processo de maturação e implementação da política de governança de dados do órgão" (peça 150, p. 53; ARG-26).

**Causas de processo:**

**CP1 — Ausência de rotina automatizada de cruzamento periódico com a base de óbitos (Sisobi).** O sistema do CAF não dispõe de rotina automatizada que consulte periodicamente a base do Sisobi e atualize a situação cadastral dos responsáveis ativos (peça 141, §164.2; peça 141, §164.3). Os cruzamentos realizados nesta auditoria foram pontuais e ad hoc — a equipe executou o confronto censitário como procedimento de auditoria, não como funcionalidade do sistema (peça 124, p. 8-9). A distribuição temporal dos óbitos não detectados ao longo de mais de uma década demonstra que o sistema operou continuamente sem rotina de limpeza (peça 150, p. 54). O contraste com o Sistema CadÚnico — que realiza cruzamento mensal automatizado com o Sisobi/RFB, alcançando taxa de detecção de óbitos de 99,87% em até 30 dias (peça 124, p. 15) — confirma que a rotina é tecnicamente viável e praticada por cadastro congênere da Administração Pública Federal. Essa lacuna permitiu o acúmulo de inconsistências de capacidade civil documentadas na Dimensão 1 da SE. *Corrigível pelas Propostas 2.1.3 (interoperabilidade) e 2.3 (monitoramento contínuo).*

**CP2 — Processo de cadastramento de e-mail sem validação funcional.** O sistema valida a sintaxe do campo de e-mail (presença de "@"), porém aceita qualquer cadeia de caracteres sem verificação de funcionalidade — admitindo padrões declaradamente fictícios, como "naopossui@mail.com" (peça 125, p. 6; peça 78). A regra de negócio não distingue entre string sintaticamente válida e endereço eletrônico funcional. A disparidade acentuada entre a taxa de validade dos e-mails de pessoa jurídica e de pessoa física evidencia que o mecanismo de cadastramento — e não uma limitação técnica do sistema — é o fator determinante: para PJ, o e-mail é ferramenta operacional indispensável; para PF no contexto do CAF, é frequentemente percebido como formalidade (peça 125, p. 7-8). A declaração de e-mail foi tornada não obrigatória para PF pelo gestor (peça 150, p. 49), decisão coerente com o perfil do público, mas que não resolve a presença de dados não funcionais já gravados na base. Essa lacuna é a causa direta da limitação de comunicação documentada na Dimensão 2 da SE. *Corrigível pela Proposta 2.1.1 (prevenção na entrada).*

**CP3 — Ausência de trava de plausibilidade para valores de renda na entrada do CAF.** A RN1.32 funciona como filtro de classificação na API do Pronaf — filtra as UFPAs compartilhadas com entidades executoras conforme enquadramento de renda (peça 150, p. 51) —, mas não opera como trava de entrada no CAF: valores manifestamente implausíveis são gravados na base sem alerta ou bloqueio (peça 130, p. 3; peça 78). O marco normativo do CAF não estabelece teto geral de renda bruta familiar para inscrição — a Lei nº 11.326/2006, inciso III do art. 3º, disciplina a composição da renda, e o Decreto nº 9.064/2017 regulamenta como ao menos metade da renda (peça 150, p. 50-51; ARG-24). Entretanto, a ausência de qualquer mecanismo de plausibilidade permite a gravação de valores que sinalizam erro de preenchimento (confusão de unidade centavos/reais), desatualização ou acúmulo de exercícios, comprometendo a confiabilidade das estatísticas agregadas de renda do cadastro (peça 130, p. 4). Essa lacuna permitiu o acúmulo de outliers documentados na Dimensão 3 da SE. *Corrigível pelas Propostas 2.1.1 (prevenção na entrada) e 2.1.2 (integridade de dados críticos).*

**Causas de produto:**

**CD1 — Ausência de verificação automatizada de compatibilidade de CNAE na inscrição de pessoa jurídica.** O sistema aceita qualquer CNAE no cadastramento de PJ sem realizar cruzamento automatizado com lista de atividades compatíveis com a agricultura familiar (peça 127, p. 5; peça 141, §163). O Decreto nº 9.064/2017, inciso VI do art. 2º, admite como atividades do empreendimento familiar rural não apenas a produção agropecuária (Seção A da CNAE), mas também beneficiamento, processamento, comercialização e turismo rural — de modo que a verificação deve operar como ferramenta de triagem, não como critério exclusivo de exclusão (peça 150, p. 52; ARG-25). A ausência de qualquer mecanismo automatizado de triagem na entrada permitiu a inscrição de entidades com atividades manifestamente incompatíveis — hipermercados, construtoras, atacadistas —, que o próprio gestor reconhece como destoantes das finalidades da agricultura familiar (peça 150, p. 52). *Corrigível pelas Propostas 2.1.1 (prevenção na entrada) e 2.1.2 (integridade de dados críticos).*

**CD2 — Ausência de rotina de saneamento periódico do passivo cadastral herdado.** O CAF não dispõe de processo periódico e sistematizado de saneamento dos registros herdados das versões anteriores (DAP, CAF 2.0), conforme reconhecido no V1 (peça 141, §164.2). Os controles prospectivos incorporados no CAF 3.0 — documentados em FC2 — não retroagiram sobre o passivo preexistente. Essa lacuna permitiu que inconsistências de múltiplas naturezas — óbitos não detectados ao longo de mais de uma década, e-mails fictícios gravados antes da retirada da obrigatoriedade, valores extremos de renda e vínculos com PJs incompatíveis — permanecessem ativas e aptas a influenciar decisões correntes. O próprio gestor reconhece que "o sistema operou continuamente sem rotina de limpeza" (peça 150, p. 54), e concordou expressamente com a insuficiência de governança de dados como causa estruturante (peça 150, p. 53; ARG-26). *Corrigível pela Proposta 2.3 (monitoramento contínuo).*

**Fatores contribuintes (contexto):**

Os fatores a seguir contextualizam a situação sem constituir causas diretas das insuficiências documentadas. São relevantes para dimensionar proporcionalmente os encaminhamentos, mas não dispensam a correção dos mecanismos identificados em CP1-CP3, CD1 e CD2.

**FC1 — Realidade de exclusão digital do público rural.** Aproximadamente dois terços das pessoas inscritas no CAF possuem baixa escolaridade, o uso de correio eletrônico pelo público rural é limitado e a preferência recai sobre aplicativos de mensagem como o WhatsApp (peça 150, p. 49; ARG-23). Quanto aos CEPs, existem 1.469 municípios brasileiros com apenas um CEP genérico (terminação -000), em sua maioria municípios de pequeno porte que correspondem ao perfil de localização da maioria das UFPAs (peça 150, p. 49-50). Esse contexto explica parte expressiva dos padrões de e-mail e CEP documentados na Dimensão 2, sem eliminar a limitação funcional de comunicação, e informa que as soluções devem ser compatíveis com o perfil do público (ex.: integração com Gov.BR, WhatsApp institucional).

**FC2 — Controles existentes no CAF 3.0 como avanço parcial.** O CAF 3.0 incorporou controles sistêmicos voltados à capacidade civil: consulta à base da RFB via BCadastro/ConectaGOV (RN 1.2) e vedação de responsabilidade por UFPA a menores (RN 1.8) (peça 150, p. 48; ARG-22). Esses controles demonstram capacidade técnica e disposição institucional para aprimoramento, justificando tratamento proporcional e distinção entre passivo acumulado e situação corrente. Os avanços reforçam a viabilidade das propostas: se o gestor já implementou controles prospectivos, a extensão da cobertura ao passivo e a ampliação a outras dimensões (renda, CNAE, óbitos) são tecnicamente factíveis.

**FC3 — Providências em curso.** O gestor informou formação de mais de 10 mil agentes cadastradores da RedeCAF para 2026 e testes de comunicação via plataforma Gov.BR (peça 150, p. 50), o que afasta leitura de inércia e contextualiza o prazo da resposta institucional.

**Conexão causa → proposta:** as causas de processo e produto (CP1-CP3, CD1-CD2) são corrigíveis pelas Propostas 2.1.1, 2.1.2, 2.1.3 e 2.3, conforme indicado em cada causa. A Proposta 1 (determinação transversal de plano de ação) endereça o conjunto das causas dos quatro achados, incluindo o saneamento do passivo cadastral (CD2). A concordância expressa do gestor com a causa raiz 4 do V1 — insuficiência de governança de dados como processo de maturação (peça 150, p. 53; ARG-26) — preserva a sustentação central do achado e reforça a pertinência de resposta institucional, particularmente nas Propostas 2.1.3 (interoperabilidade) e 2.3 (monitoramento contínuo), que operacionalizam os mecanismos de governança cuja insuficiência o próprio gestor reconhece.

| Causa | Proposta que a corrige |
|---|---|
| CP1 (sem cruzamento periódico Sisobi) | 2.1.3 (interoperabilidade) + 2.3 (monitoramento) |
| CP2 (e-mail sem validação funcional) | 2.1.1 (prevenção na entrada) |
| CP3 (sem trava de plausibilidade de renda) | 2.1.1 (prevenção na entrada) + 2.1.2 (integridade) |
| CD1 (CNAE sem verificação automatizada) | 2.1.1 (prevenção na entrada) + 2.1.2 (integridade) |
| CD2 (sem saneamento periódico do passivo) | 2.3 (monitoramento contínuo) |
| Proposta 1 (determinação transversal) | Cobre o conjunto das causas |

---

**Critérios das causas:**

Os critérios abaixo fundamentam *por que* os mecanismos identificados constituem causas — qual norma ou referencial deveria ter sido aplicado no processo e cuja não-aplicação produziu a situação encontrada. São distintos dos critérios da SE e dos critérios dos Efeitos.

**CC1. DAMA-DMBOK v2 — prevenção na entrada** (peça 86, p. 38) — A melhor forma de assegurar qualidade é impedir a entrada de dados inadequados na origem. A aceitação de e-mails fictícios (CP2), valores de renda sem plausibilidade (CP3) e CNAEs sem triagem (CD1) viola esse princípio: o sistema valida a sintaxe, mas não o conteúdo semântico. **Ancoragem:** Ac. 457/2026-Plenário.

**CC2. Decreto nº 10.046/2019, art. 1º** (peça 82) — Dispõe sobre governança no compartilhamento de dados na APF, incluindo dever de interoperabilidade e melhoria da qualidade. A ausência de cruzamento periódico com o Sisobi (CP1) e a falta de verificação automatizada de CNAE via base da RFB (CD1) contrariam esse dever.

**CC3. Benchmark CadÚnico — cruzamento mensal com Sisobi/RFB** (peça 124, p. 15) — O CadÚnico, cadastro congênere da APF, realiza cruzamento mensal automatizado com a base Sisobi/RFB, alcançando taxa de detecção de óbitos de 99,87% em até 30 dias. A rotina demonstra que a solução é tecnicamente viável e praticada por sistema público de escala comparável. A ausência dessa rotina no CAF (CP1) e a permanência do passivo sem curadoria (CD2) configuram descompasso com prática já consolidada na APF.

**CC4. Acórdão 1606/2025-Plenário**, Rel. Min. Jorge Oliveira — O TCU reconheceu, em contexto análogo, que fragilidades estruturais na gestão de dados de óbitos do SIRC comprometem a fidedignidade dos cadastros e acarretam pagamento indevido de benefícios. A manutenção de responsáveis falecidos como titulares ativos no CAF configura situação análoga.

**CC5. ISO/IEC 25012:2008 — Atualidade e Acurácia** (peça 84) — Dados devem ser atualizados e corresponder a valores reais. A permanência de registros de responsáveis falecidos, e-mails não funcionais e valores de renda implausíveis viola as características de atualidade (CP1, CD2) e acurácia (CP2, CP3, CD1).

---

**Evidências das causas:**

| Ref. | Peça | Página | Descrição | Causa sustentada |
|---|---|---|---|---|
| EC1 | 124 | p. 8-9 | Cruzamento censitário com Sisobi realizado como procedimento de auditoria, não como funcionalidade do sistema | CP1 (ausência de rotina automatizada) |
| EC2 | 124 | p. 15 | CadÚnico: cruzamento mensal com Sisobi/RFB, detecção de 99,87% em 30 dias | CP1 (benchmark de viabilidade) |
| EC3 | 150 | p. 54 | Gestor reconhece: sistema operou continuamente sem rotina de limpeza | CP1, CD2 (reconhecimento mútuo) |
| EC4 | 125 | p. 6-8 | Disparidade de 90,32 p.p. PF-PJ em e-mails válidos — falha processual, não técnica | CP2 (mecanismo de cadastramento) |
| EC5 | 78 | p. 5 | RN1.17: campo aceita qualquer string com "@" sem verificação de funcionalidade | CP2 (desenho da regra de negócio) |
| EC6 | 150 | p. 49 | E-mail tornado não obrigatório para PF; baixa escolaridade; WhatsApp preferido | FC1 (contexto de exclusão digital) |
| EC7 | 130 | p. 3-4 | Outliers de renda: valores >R$ 10M gravados sem alerta ou bloqueio | CP3 (ausência de trava) |
| EC8 | 78 | p. 7 | RN1.32: filtro de classificação Pronaf, não trava de entrada no CAF | CP3 (desenho da regra de negócio) |
| EC9 | 150 | p. 50-51 | Lei 11.326/2006 disciplina composição da renda, não valor absoluto (ARG-24) | CP3 (calibração normativa) |
| EC10 | 127 | p. 5 | Ausência de validação automatizada de CNAE no cadastramento de PJ | CD1 (mecanismo) |
| EC11 | 150 | p. 52 | Decreto 9.064/2017, art. 2°, VI: CNAE como triagem, não exclusão (ARG-25) | CD1 (calibração normativa) |
| EC12 | 150 | p. 48 | RN 1.2 (BCadastro/ConectaGOV) e RN 1.8 (vedação menores): aplicam-se prospectivamente | FC2 (avanço parcial — controles não retroativos) |
| EC13 | 141 | §164.2 | CAF sem processos periódicos e sistematizados de saneamento de dados | CD2 (ausência de curadoria) |
| EC14 | 150 | p. 53 | Gestor concorda expressamente com causa raiz 4 (insuficiência de governança) (ARG-26) | Sustentação processual do achado |
| EC15 | 150 | p. 50 | Providências em curso: 10 mil agentes RedeCAF para 2026; testes Gov.BR | FC3 (mitigação em andamento) |
| EC16 | 72 | p. 2 | Reunião técnica: CPF sem chave primária em sistemas públicos gera dificuldades de cruzamento | FC2 (contexto institucional — barreira parcial superada pelo CadÚnico) |

### Boas Práticas e Avanços

Não foram identificadas, no escopo deste achado, boas práticas no sentido estrito da NAT §160 — práticas que, cumulativamente, ultrapassem o cumprimento do dever legal, sejam significativas, inovadoras e efetivas, e possam ser propostas para extensão a outros órgãos. Os avanços implementados pelo gestor — implementação da RN 1.2 (consulta BCadastro/ConectaGOV para validação de capacidade civil) e da RN 1.8 (vedação de cadastramento de menores), além da formação de 10 mil agentes RedeCAF prevista para 2026 — foram factualmente reconhecidos na Situação Encontrada e nos Fatores Contribuintes (FC2–FC3), onde contextualizam a capacidade de resposta institucional e informam a proporcionalidade dos encaminhamentos. Registre-se que a integração BCadastro/ConectaGOV constitui cumprimento do item 9.2.2 do Acórdão 1197/2018-TCU-Plenário e obrigação básica de validação, não configurando prática além do dever legal.

### Encaminhamentos

**Determinação:**

**Proposta 1.** Determinar ao MDA que, no prazo de 180 dias, elabore e encaminhe ao TCU plano de ação, com responsáveis, prazos e forma de comunicação do cumprimento, para avaliar as situações identificadas neste relatório e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, abrangendo as inconsistências documentadas na qualidade dos **dados de entrada**, dos **dados geoespaciais**, dos **dados cadastrais** e dos **metadados** do CAF, em conformidade com os critérios de elegibilidade previstos no art. 3º da Lei 11.326/2006 e com a finalidade de identificação e qualificação estabelecida no art. 4º do Decreto 9.064/2017.

*Justificativa do vínculo:* a determinação decorre da situação encontrada nas quatro dimensões do ACH-03 — capacidade civil (3.097 falecidos, 138 menores), dados de contato (90,62% e-mails fictícios, 93,7% CEPs genéricos), consistência de renda (907 UFPAs > R$ 1 milhão) e natureza jurídica (39 PJs com CNAE incompatível) — e dos efeitos potenciais documentados (EP1-EP4). O componente "dados cadastrais" da determinação corresponde ao escopo deste achado.

**Recomendações:**

**Proposta 2.1.1.** Assegurar que processos de cadastramento e atualização produzam dados com qualidade suficiente, incluindo mecanismos que previnam inserção e permanência de dados inválidos no CAF.

*Justificativa do vínculo:* decorre da Dimensão 1 (3.097 responsáveis falecidos e 138 menores como titulares ativos) e da Dimensão 2 (90,62% de e-mails fictícios), que evidenciam insuficiência na prevenção da entrada de dados inválidos em campos críticos de identificação e contato.

**Proposta 2.1.2.** Garantir integridade e consistência dos dados críticos do CAF, por meio de controles que reduzam erros e anomalias em campos essenciais à identificação do beneficiário, localização do imóvel e elegibilidade cadastral.

*Justificativa do vínculo:* decorre da Dimensão 3 (907 UFPAs com renda > R$ 1 milhão, incluindo 141 > R$ 10 milhões) e da Dimensão 4 (39 PJs com CNAEs incompatíveis afetando 10.377 agricultores), que evidenciam insuficiência de controles de plausibilidade e consistência em campos de renda e atividade econômica.

**Proposta 2.1.3.** Estabelecer mecanismos de interoperabilidade com bases de dados oficiais relevantes, para detecção tempestiva de inconsistências e irregularidades nos dados cadastrais.

*Justificativa do vínculo:* decorre da constatação de que o cruzamento censitário com Sisobi e RFB foi o mecanismo que identificou as inconsistências de capacidade civil (peça 124), demonstrando o valor da interoperabilidade para detecção de anomalias que controles internos não captaram — e a necessidade de que esses cruzamentos sejam tempestivos, não apenas pontuais em auditoria.

**Proposta 2.3.** Implementar monitoramento contínuo da qualidade dos dados do CAF, com indicadores que permitam identificar e priorizar ações corretivas e avaliar efetividade das medidas.

*Justificativa do vínculo:* decorre do efeito potencial EP4 (aumento do custo operacional por acúmulo sem detecção) e da constatação de que 12.820 óbitos se distribuíram ao longo de mais de uma década sem saneamento (peça 141, §166.4), evidenciando ausência de monitoramento contínuo de indicadores de qualidade cadastral. O gestor concordou expressamente com a causa raiz 4 (insuficiência de governança de dados; peça 150, p. 53).

### Benefícios Esperados

**Benefícios quantitativos:**

a) Saneamento dos 3.097 cadastros com titulares falecidos confirmados no Sisobi e dos 138 cadastros com menores como titulares, com meta e priorização a definir pelo gestor no plano de ação (Proposta 1) — reversão parcial de EP1.

b) Verificação individualizada dos 907 registros com renda superior a R$ 1 milhão, incluindo os 141 com renda superior a R$ 10 milhões, com meta a definir pelo gestor (Proposta 2.1.2) — reversão parcial de EP4.

c) Melhoria da capacidade de comunicação com os aproximadamente 2,6 milhões de famílias afetadas por dados de contato não funcionais (90,62% de e-mails fictícios e 93,7% de CEPs genéricos), com meta e estratégia de contato a definir pelo gestor, compatíveis com o perfil do público rural (Proposta 2.1.1) — reversão parcial de EP2.

d) Implantação de rotina automatizada de cruzamento periódico com Sisobi, com meta de detecção tempestiva a definir pelo gestor, tendo como referência a taxa de 99,87% do CadÚnico em até 30 dias (Proposta 2.1.3) — reversão parcial de EP1 e reversão parcial de EP4.

**Benefícios qualitativos:**

a) Fortalecimento da focalização de políticas públicas (reversão de EP1), assegurando que cadastros ativos no CAF correspondam a titulares juridicamente capazes de gestão do estabelecimento rural (Propostas 2.1.1 e 2.1.3).

b) Redução do risco de exclusão involuntária de beneficiários legítimos por impossibilidade de comunicação (reversão de EP2), mediante estratégias de contato compatíveis com a realidade de exclusão digital do público rural (Proposta 2.1.1).

c) Mitigação do risco regulatório para os 10.377 agricultores vinculados a 39 PJs com CNAE incompatível (reversão de EP3), mediante triagem automatizada na entrada e saneamento dos vínculos existentes (Propostas 2.1.1 e 2.1.2).

d) Redução do custo operacional e da complexidade de controle para gestores e executores das políticas (reversão de EP4), mediante monitoramento contínuo que previna o acúmulo de inconsistências sem detecção ao longo de anos (Proposta 2.3).

---

## ACH-04 — Maturidade incipiente na gestão de metadados do CAF

**Frase-síntese:**

Devido à maturidade incipiente na gestão de metadados do CAF — com conhecimento técnico existente mas fragmentado entre instrumentos de documentação não integrados —, **ocorreu** insuficiência qualitativa na documentação semântica dos dados, com 94,1% de descrições inadequadas, 84% de campos numéricos sem unidade de medida e 92% de campos temporais ambíguos, apesar de cobertura formal de 100% das tabelas em uso, **o que levou** à limitação da rastreabilidade e da auditabilidade do cadastro, **impactando** a capacidade de interpretação independente e manutenção evolutiva do sistema, bem como a sustentabilidade das melhorias de qualidade de dados recomendadas nos Achados I, II e III — uma vez que metadados de qualidade são pré-requisito para validação, curadoria e monitoramento sustentáveis (DAMA-DMBOK v2, peça 86, p. 13).

---

### Situação Encontrada

A auditoria identificou que a gestão de metadados do CAF opera em nível incipiente de maturidade, com deficiências qualitativas que limitam a documentação semântica dos dados, a rastreabilidade e a auditabilidade do cadastro. Cabe registrar, de início, que o achado não revela inexistência absoluta de documentação: o CAF dispõe de dicionário de dados com cobertura integral das 95 tabelas efetivamente em uso (peça 70; peça 134, p. 4) e de Documento de Regras de Negócio com definições semânticas relevantes (peça 78) (ARG-27). Essa infraestrutura básica é reconhecida como ponto positivo — o aspecto mais maduro da gestão de metadados do sistema. O problema documentado recai sobre a qualidade, a granularidade e a utilidade auditável dos metadados existentes, em três dimensões específicas. A análise baseou-se na avaliação de 527 campos do dicionário de dados (peça 135, p. 4) e considerou os argumentos apresentados pelo gestor (peça 150, p. 56-71), cujas análises constam do Anexo — Análise dos Comentários dos Gestores.

**Dimensão 1 — Qualidade semântica das descrições.** A avaliação dos 527 campos documentados no dicionário de dados revelou que 496 (94,1%) apresentam descrições semanticamente insuficientes (peça 135, p. 4). As descrições seguem padrão tautológico que repete o nome técnico do campo sem acrescentar contexto de negócio — por exemplo, `id_area_imovel` descrito como "ID de identificação de área imóvel" (peça 75). Campos críticos como `nr_area` (área do imóvel) e coordenadas geográficas (`nr_latitude`, `nr_longitude`) não especificam unidade de medida nem sistema geodésico de referência, informações essenciais para interpretação correta dos dados. Em contrapartida, 31 campos (5,9%) já possuem descrições funcionais adequadas (peça 135, p. 4) — benchmark interno que demonstra que a equipe técnica do sistema conhece o padrão desejável e sabe produzi-lo. A insuficiência não decorre de incapacidade técnica, mas de falta de aplicação sistemática desse padrão a todo o dicionário.

**Dimensão 2 — Especificação de unidades de medida.** Dos 125 campos numéricos identificados no dicionário, 105 (84%) não especificam unidade de medida (peça 136, p. 4-5). A ausência é particularmente crítica em campos como `nr_area` (sem indicação se hectares, metros quadrados ou alqueires), coordenadas geográficas `nr_latitude`/`nr_longitude` (sem indicação de formato ou datum) e campos monetários (sem indicação se reais ou centavos) — exemplos extraídos do dicionário (peça 75) e detalhados na peça 136, p. 5-6, Tabelas 3-5. Sem essa especificação, a interpretação dos dados depende de conhecimento tácito — quem sabe que `nr_area` está em hectares é quem participou do desenvolvimento, não quem consulta o dicionário. Erros de interpretação de unidade (como confundir hectares com metros quadrados, fator de 10.000×) podem propagar-se silenciosamente em integrações e análises automatizadas.

**Dimensão 3 — Ambiguidade temporal.** Dos 87 campos temporais (datas e timestamps) identificados, 80 (92%) são ambíguos quanto ao evento de negócio que registram (peça 133, p. 5). Campos como `dt_cadastro` ou `dt_atualizacao` não especificam se se referem à data de criação do registro no sistema, à data do evento no mundo real, ou à data de aprovação administrativa. Essa ambiguidade compromete análises temporais e cruzamentos — por exemplo, verificar se um cadastro foi feito antes ou depois de determinada transição normativa depende de saber qual evento a data registra.

**Fragmentação do conhecimento.** O conhecimento semântico sobre os dados do CAF existe, mas está fragmentado entre dois instrumentos não integrados: o dicionário de dados (peça 75), que documenta a estrutura técnica com descrições predominantemente tautológicas, e o Documento de Regras de Negócio versão 0.3 (peça 78), que contém definições semânticas relevantes mas foi produzido em quatro dias por consultores externos e não está vinculado campo-a-campo ao dicionário. A consequência é que o significado completo de cada campo só se obtém consultando ambos os documentos e, frequentemente, recorrendo à memória dos técnicos do sistema — situação de dependência de conhecimento tácito que o DAMA-DMBOK v2 identifica como indicador de baixa maturidade em gestão de metadados (peça 86, p. 13).

**Contexto e posicionamento do gestor.** O gestor reconhece o problema como deficiência qualitativa na documentação semântica, e não como vazio estrutural de governança (ARG-28). Qualifica as causas contributivas — passivo documental, dívida técnica acumulada sob pressão operacional, falta de integração entre equipes técnicas e de negócio — como pertinentes, sem tratá-las como omissão deliberada (peça 150, p. 59-60). Aceita os quatro riscos apontados pela equipe (comprometimento da rastreabilidade, dependência de conhecimento tácito, amplificação dos problemas dos demais achados e dificuldade de manutenção evolutiva), ponderando que se trata de risco de governança documental e semântica (peça 150, p. 60). Registre-se que o gestor acolheu expressamente a recomendação de aprimorar a gestão de metadados, avaliando-a como pertinente e convergente com o aperfeiçoamento da governança do CAF, e propondo execução gradual integrada à gestão de mudanças (peça 150, p. 71) (ARG-29). Esse acolhimento é elemento relevante para a sustentação processual do achado e do encaminhamento correspondente.

---

### Critérios da Situação Encontrada

**C1. DAMA-DMBOK v2, capítulo 12 — Gestão de Metadados** (peça 86, p. 13) — Estabelece que metadados são o principal meio de esclarecer as expectativas de qualidade de dados: sem definições formalizadas, a organização não tem como medir nem gerenciar a qualidade de seus dados. **Aplicação:** fundamenta o diagnóstico de que a insuficiência qualitativa dos metadados do CAF (94,1% de descrições inadequadas) limita a capacidade de gestão da qualidade do cadastro como um todo. O achado descreve maturidade incipiente, não inexistência — distinção que o próprio referencial sustenta ao tratar níveis de maturidade. **Ancoragem:** o DAMA-DMBOK v2 foi expressamente adotado como critério pelo Ac. 457/2026-TCU-Plenário (unanimidade), que identificou fragilidades análogas em 3 dos 5 órgãos auditados: inexistência de catálogo de dados, informações limitadas sobre metadados e glossário de termos insuficiente.

**C2. ISO/IEC 11179-1:2023** (peça 84, documento integral) — Registro de metadados: especificação de elementos de dados, domínios de valor, unidades de medida, definições de negócio. **Aplicação:** referencial técnico para aferir a qualidade do dicionário de dados — especialmente a ausência de unidades de medida (84%) e a ambiguidade semântica das descrições (94,1%).

**C3. Decreto nº 10.046/2019, art. 1º** — Governança de dados na Administração Pública Federal: compartilhamento, interoperabilidade, documentação. **Aplicação:** a insuficiência qualitativa dos metadados limita a interoperabilidade do CAF com outras bases — sem definições claras de unidades e semântica, integrações ficam sujeitas a erros silenciosos.

**C4. Acórdão 390/2024-TCU-Plenário** — Estratégia GovDados 2023-2028. Identificou baixa maturidade de governança de dados na APF. **Aplicação:** contextualiza o achado no cenário mais amplo de maturidade da APF — o CAF não é caso isolado, mas exemplifica padrão documentado pelo próprio Tribunal.

**C5. Acórdãos 1197/2018-TCU-Plenário → 1866/2021-TCU-Plenário → 885/2024-TCU-Plenário** — Reincidência DAP/CAF. **Aplicação:** problemas de documentação e governança de dados não são inéditos; deliberações anteriores permanecem pendentes.

**C6. ISO/IEC 25012:2008** (peça 85, documento integral) — Dimensões de qualidade: completude e acurácia. **Aplicação:** ilustra a distinção central do achado — o dicionário tem 100% de completude formal (todos os campos documentados) mas menos de 6% de acurácia semântica (descrições que efetivamente explicam o dado). Critério secundário.

---

### Evidências da Situação Encontrada

**Evidências analíticas (papéis de trabalho):**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E1 | 135 | p. 4 | Qualidade semântica: 496/527 campos (94,1%) com descrições inadequadas; 31 (5,9%) adequadas | Dimensão 1 — taxa e benchmark |
| E2 | 135 | p. 4, Tab. 2-3 | Tipologia das inadequações: tautológicas, genéricas, sem contexto de negócio | Dimensão 1 — padrão das insuficiências |
| E3 | 136 | p. 4-5 | Unidades de medida: 105/125 campos numéricos (84%) sem especificação | Dimensão 2 — magnitude |
| E4 | 136 | p. 5-6, Tab. 3-5 | Casos críticos: área sem unidade, coordenadas sem datum, valores monetários ambíguos | Dimensão 2 — exemplos de risco |
| E5 | 133 | p. 5 | Ambiguidade temporal: 80/87 campos (92%) sem evento de negócio claro | Dimensão 3 — magnitude |
| E6 | 133 | p. 6-8, Tab. 5-8 | Casos críticos: dt_cadastro, dt_atualizacao sem distinção de evento | Dimensão 3 — exemplos |
| E7 | 134 | p. 4 | Cobertura: 95 tabelas em uso, 100% documentadas | Ponto positivo — cobertura |
| E8 | 132 | p. 3 | Índice mestre do Achado IV: universo de análise (527 campos, 125 numéricos, 87 temporais) | Denominadores de todas as dimensões |

**Evidências documentais (dicionário e regras de negócio):**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E9 | 75 | (documento integral) | Dicionário de dados do CAF — 95 tabelas, descrições tautológicas, sem unidades, sem datum | Evidência direta das deficiências qualitativas |
| E10 | 78 | (documento integral) | Documento de Regras de Negócio CAF 3.0, versão 0.3 — definições semânticas relevantes não integradas ao dicionário | Fragmentação do conhecimento |
| E11 | 84 | (documento integral) | ISO/IEC 11179-1:2023 — metamodelo de elementos de dados | Critério C2 |
| E12 | 86 | p. 13 | DAMA-DMBOK v2 — metadados como pré-requisito para medir qualidade | Critério C1 |

**Evidências testemunhais e consensuais:**

| Ref. | Peça | Página | Descrição | Afirmação sustentada |
|---|---|---|---|---|
| E13 | 73 | p. 3 | Ata de reunião: consenso sobre carência de mecanismos automatizados | Contexto geral |
| E14 | 74 | p. 4 | Ata de encerramento: problemas do legado CAF 2.0 | Passivo/corrente |

**Elementos do contraditório incorporados:**

| Ref. | Peça | Página | Descrição | Calibração aplicada |
|---|---|---|---|---|
| E15 | 150 | p. 56-57 | Cobertura 100% reconhecida; insuficiência qualitativa, não vazio absoluto (ARG-27) | Abrir com ponto positivo; maturidade incipiente |
| E16 | 150 | p. 57-60 | Problema qualitativo, não inexistência estrutural; causas contributivas aceitas (ARG-28) | Contextualizar como dívida técnica, não omissão |
| E17 | 150 | p. 60 | Gestor aceita os 4 riscos apontados (rastreabilidade, conhecimento tácito, amplificação, manutenção) | Validação dos riscos pelo gestor |
| E18 | 150 | p. 71 | Gestor acolhe expressamente a recomendação de aprimorar gestão de metadados (ARG-29) | Ouro processual — sustentação do encaminhamento |
| E19 | 150 | p. 59-60 | Causas contributivas: passivo documental, dívida técnica, pressão operacional (ARG-28) | Fase 3 (Causas) — registrado como contexto |

---

### Efeitos

A insuficiência qualitativa dos metadados do CAF — 94,1% de descrições semanticamente inadequadas, 84% de campos numéricos sem unidade de medida, 92% de campos temporais ambíguos — produz efeitos potenciais que comprometem a capacidade de interpretação autônoma dos dados e a sustentabilidade das melhorias recomendadas nos Achados I, II e III. A equipe não identificou, no escopo desta auditoria, efeitos concretos consumados — eventos adversos com prejuízos individualizados — decorrentes das insuficiências de metadados. Registre-se que o dicionário de dados possui cobertura integral de 100% das 95 tabelas em uso (ponto positivo reconhecido — ARG-27; peça 150, p. 56-57); o problema é de qualidade semântica, não de ausência documental. Os efeitos descritos foram extraídos do relatório de auditoria (§§210-211) e calibrados pelas análises do contraditório. O gestor reconhece o problema como deficiência de maturidade em metadados (ARG-28) e acolheu expressamente a recomendação de aprimoramento (ARG-29; peça 150, p. 71) — concordância que reforça a pertinência do achado.

**Efeitos potenciais:**

**EP1 — Risco de comprometimento da interpretação autônoma dos dados.** A insuficiência qualitativa dos metadados — 94,1% de descrições tautológicas ou genéricas (peça 135, p. 4; peça 141, §210.1), 84% de campos numéricos sem unidade de medida (peça 136, p. 4-5), 92% de campos temporais sem distinção entre evento de sistema e evento de negócio (peça 133, p. 5) — limita a capacidade de compreender o significado das informações de forma autônoma, sem recorrer a consultas informais aos técnicos que desenvolveram o sistema (peça 141, §210.1). O caso do campo `nr_area` é ilustrativo: sem especificação de unidade (hectares, metros quadrados, alqueires), a interpretação correta depende de quem conhece o sistema — e a divergência de +120,89% documentada no Achado I (peça 109, p. 9) pode decorrer, em parte, de ambiguidades dessa natureza. O benchmark interno de 5,9% de descrições adequadas (31 de 527 campos; peça 135, p. 4) demonstra que o padrão de qualidade é conhecido pela equipe técnica, mas não foi aplicado sistematicamente.

**EP2 — Risco de concentração de conhecimento crítico em poucos indivíduos.** Com 94,1% das descrições inadequadas, o conhecimento sobre o significado real dos campos está concentrado em desenvolvedores sêniores que participaram da construção e evolução do sistema. Se essas pessoas-chave deixarem a organização — por aposentadoria, transferência ou qualquer outro motivo —, o conhecimento institucional sobre a estrutura de dados corre o risco de se perder (peça 141, §211.2). Essa dependência de conhecimento tácito é reconhecida pelo DAMA-DMBOK v2 como indicador de baixa maturidade em gestão de metadados (peça 86, p. 13) e pelo próprio gestor, que aceita esse risco expressamente (peça 150, p. 60).

**EP3 — Risco de erros em integrações e análises.** Sistemas externos que consomem dados do CAF — plataformas de crédito rural, sistemas de monitoramento ambiental, bases estatísticas — dependem de interpretação correta dos campos para realizar cruzamentos válidos. Quando 84% dos campos numéricos não especificam unidade e 92% dos temporais são ambíguos, o risco de mapeamentos incorretos é substancial (peça 141, §211.1). A ausência de especificação de datum geodésico nas coordenadas (peça 136, p. 5-6) agrava esse risco para integrações geoespaciais.

**EP4 — Risco de comprometimento da sustentabilidade das melhorias dos Achados I, II e III.** O risco de erros em integrações e análises (peça 141, §211.1) e a dificuldade de manutenção evolutiva (peça 141, §211.3) tendem a limitar a efetividade das melhorias recomendadas nos demais achados, uma vez que validações automáticas, curadoria periódica e monitoramento por indicadores dependem de metadados claros para funcionar corretamente. O próprio relatório registra que as deficiências de metadados funcionam como causa estrutural que amplifica os problemas documentados nos achados anteriores, e que corrigir o dicionário de dados é pré-requisito estrutural para que as correções nos dados sejam duradouras (peça 141, §215 — contextualização conclusiva). Esse efeito transversal é ancorado no DAMA-DMBOK v2, que estabelece que metadados são o principal meio de esclarecer as expectativas de qualidade de dados (peça 86, p. 13). Registre-se que se trata de risco potencial: não há evidência de que melhorias específicas tenham sido comprometidas por insuficiência de metadados até o momento.

**EP5 — Risco de limitação à auditabilidade futura.** A insuficiência qualitativa dos metadados limita a capacidade de verificação independente do sistema por parte de órgãos de controle (peça 141, §213). Auditorias futuras enfrentariam as mesmas dificuldades de interpretação que esta equipe encontrou, sendo forçadas a recorrer a engenharia reversa do código-fonte, análise exploratória dos dados ou consultas repetidas aos técnicos — processo custoso e sujeito a erros (peça 141, §211.3).

---

**Nota sobre quantificação de prejuízos financeiros.** O ACH-04 não envolve prejuízo financeiro direto quantificável — insuficiências de metadados não geram custo ao erário por si. O prejuízo é de eficiência e sustentabilidade: retrabalho para interpretar dados sem documentação adequada, dependência de consultas informais, risco de erros silenciosos em integrações. A quantificação do custo de retrabalho exigiria mensuração de horas técnicas dedicadas a consultas e interpretação — dados não disponíveis no escopo desta auditoria.

**Prejuízos sociais potenciais.** Os prejuízos sociais do ACH-04 são de natureza transversal e indireta: a insuficiência qualitativa dos metadados pode comprometer a sustentabilidade das melhorias de qualidade de dados recomendadas nos Achados I, II e III. Se os campos do CAF não estão semanticamente documentados, as validações automáticas, a curadoria periódica e o monitoramento — ferramentas necessárias para enfrentar os problemas que afetam 3,08 milhões de documentos inadequados (ACH-01), 1,75 milhão de imóveis com coordenadas duplicadas (ACH-02) e 3.097 famílias com titular falecido (ACH-03) — tendem a ser implementados com menor robustez e previsibilidade. A insuficiência de metadados pode, assim, perpetuar indiretamente as limitações de capacidade documentadas nos demais achados, com as consequências sociais potenciais ali registradas.

---

**Critérios dos efeitos:**

Os critérios abaixo fundamentam *por que* os efeitos identificados são adversos. São distintos dos critérios da Situação Encontrada.

**CE1. DAMA-DMBOK v2, capítulo 12** (peça 86, p. 13) — Metadados são pré-requisito para medir e gerenciar qualidade de dados. A insuficiência qualitativa dos metadados do CAF (EP1, EP2, EP4) limita a capacidade da organização de gerenciar a qualidade do cadastro de forma sustentável.

**CE2. ISO/IEC 11179-1:2023** (peça 84, documento integral) — Especificação de elementos de dados: unidades de medida, domínios, definições de negócio. A ausência de unidades de medida em 84% dos campos numéricos (EP3) e de definições semânticas em 94,1% dos campos (EP1) contraria as boas práticas desse referencial.

**CE3. Decreto nº 10.046/2019, art. 1º** (peça 82) — Governança de dados na APF: interoperabilidade e documentação. A insuficiência de metadados limita a interoperabilidade do CAF com outras bases (EP3) e a sustentabilidade de integrações futuras.

---

**Evidências dos efeitos:**

| Ref. | Peça | Página | Descrição | Efeito sustentado |
|---|---|---|---|---|
| EE1 | 135 | p. 4 | 94,1% de descrições semanticamente inadequadas (496/527 campos); 5,9% adequadas | EP1 (interpretação), EP2 (conhecimento tácito) |
| EE2 | 136 | p. 4-5 | 84% de campos numéricos sem unidade de medida (105/125) | EP1 (interpretação), EP3 (integrações) |
| EE3 | 133 | p. 5 | 92% de campos temporais sem evento de negócio claro (80/87) | EP1 (interpretação), EP3 (integrações) |
| EE4 | 136 | p. 5-6 | Casos críticos: nr_area sem unidade, coordenadas sem datum, valores monetários ambíguos | EP3 (risco de erro silencioso) |
| EE5 | 141 | §210.1 | Efeito: impossibilidade de compreensão autônoma do significado dos dados | EP1 (efeito documentado no V1) |
| EE6 | 141 | §211.1 | Risco de erros em integrações e análises (sistemas externos) | EP3 (risco documentado no V1) |
| EE7 | 141 | §211.2 | Risco de dependência crítica de "gurus do sistema" | EP2 (risco documentado no V1) |
| EE8 | 141 | §211.3 | Risco de dificuldade de manutenção evolutiva (curva de aprendizado) | EP5 (auditabilidade e manutenção) |
| EE9 | 141 | §215 | Deficiências de metadados como causa estrutural que amplifica problemas dos ACH-01/02/03 | EP4 (efeito transversal) |
| EE10 | 86 | p. 13 | DAMA-DMBOK v2: metadados como pré-requisito para medir qualidade | EP4 (fundamentação teórica) |
| EE11 | 150 | p. 56-57 | Cobertura 100% reconhecida; insuficiência qualitativa (ARG-27) | Calibração — ponto positivo |
| EE12 | 150 | p. 60 | Gestor aceita os 4 riscos apontados (ARG-28) | EP1-EP5 (validação pelo gestor) |
| EE13 | 150 | p. 71 | Gestor acolhe expressamente a recomendação (ARG-29) | Sustentação processual do achado |
| EE14 | 109 | p. 9 | Divergência de +120,89% em dados de área — possível conexão com ausência de unidade em nr_area | EP3 (ilustração do risco) |

### Causas

As causas a seguir explicam *por que* o dicionário de dados do CAF apresenta insuficiência qualitativa em três dimensões — os mecanismos específicos de produção, manutenção e estruturação da documentação de metadados cuja inadequação produziu o padrão de descrições tautológicas, ausência de unidades de medida e ambiguidade temporal documentados na SE. As causas foram extraídas do relatório de auditoria (peça 141, §§204-209) e calibradas pelas análises do contraditório (ARGs 27-29). O diagnóstico não afirma inexistência de documentação — o CAF possui dicionário com cobertura integral e Documento de Regras de Negócio com definições relevantes (FC1 e FC2) —, mas identifica os mecanismos que impediram a tradução dessa infraestrutura básica em documentação semântica de qualidade. O gestor reconhece todas as causas contributivas como pertinentes, qualificando-as como passivo documental e dívida técnica acumulados sob pressão operacional (peça 150, p. 59-60; ARG-28).

**Causas de processo:**

**CP1 — Dicionário de dados produzido como documentação post-mortem, sem enriquecimento semântico.** O dicionário (peça 75) foi elaborado após o desenvolvimento do sistema, e não durante — prática conhecida como documentação post-mortem (peça 141, §206). As descrições dos campos foram derivadas dos nomes técnicos das colunas do banco de dados por processo mecânico, sem etapa de revisão que vinculasse cada campo ao seu significado de negócio. O resultado é que as descrições repetem o nome técnico em formato textualizado — por exemplo, `id_area_imovel` descrito como "ID de identificação de área imóvel" (peça 75) — sem acrescentar contexto funcional, regras de validação ou relação com o marco legal. Essa lacuna no processo de produção do dicionário é a causa direta do padrão de descrições inadequadas documentado na Dimensão 1 da SE. *Corrigível pela Proposta 2.4 (gestão de metadados).*

**CP2 — Produção do DRN por equipe externa sem etapa de mapeamento campo-a-campo com o dicionário.** O DRN versão 0.3 (peça 78) foi produzido em quatro dias por consultores externos (peça 78, p. 3) como documento autônomo, sem que o escopo de trabalho incluísse etapa de vinculação das definições de negócio aos campos do dicionário de dados existente (peça 141, §206). A RN1.19, por exemplo, especifica que a área de aquicultura deve ser expressa em "metros cúbicos" ou "hectares", mas essa informação não foi transposta para o campo `nr_area` do dicionário. O mecanismo causal não é a inexistência de integração em si (que é a constatação da SE), mas a decisão de escopo que gerou a fragmentação: ao contratar o DRN como artefato independente — sem requisito de alinhamento com o dicionário pré-existente —, o processo de documentação produziu dois repositórios de conhecimento com sobreposição parcial e sem ponte. Essa decisão é agravada pelo isolamento funcional entre equipes de desenvolvimento e de negócio (peça 141, §209): cada grupo documentou o que conhecia no instrumento que lhe era disponível, sem processo que reunisse ambas as perspectivas. *Corrigível pela Proposta 2.4 (gestão de metadados).*

**CP3 — Metadados não integrados ao ciclo de desenvolvimento como artefato obrigatório de entrega.** O CAF não possui documento formal que estabeleça padrões de documentação, responsabilidades e processos de controle de qualidade para metadados (peça 141, §204). Não há definição explícita de quem é responsável pela manutenção do dicionário, quais critérios uma descrição deve atender para ser considerada adequada, nem qual é o fluxo de aprovação para inclusão de novas tabelas ou campos (peça 141, §204). O dicionário é mantido em formato CSV/Excel — artefato estático sem integração automatizada com o esquema do banco de dados: quando uma tabela é criada ou alterada, essa mudança não se reflete automaticamente no dicionário (peça 141, §207). A consequência é que a documentação de metadados não acompanha a evolução do sistema: ao longo de mais de uma década e múltiplas versões (CAF 1.0, 2.0, 3.0), a dívida técnica documental acumulou-se sem processo de revisão (peça 141, §208). Essa lacuna é a causa estrutural da desatualização e da estagnação qualitativa do dicionário. *Corrigível pela Proposta 2.4 (gestão de metadados).*

**Causas de produto:**

**CD1 — Template do dicionário sem campos estruturais para unidade de medida, datum geodésico e domínio de valores.** O dicionário de dados é mantido em formato CSV/Excel — artefato estático cuja estrutura não prevê campos dedicados para registrar unidade de medida, sistema geodésico de referência, domínio de valores aceitos nem evento de negócio associado a campos temporais (peça 75; peça 141, §207). A ISO/IEC 11179-1:2023 considera essas informações elementos essenciais do metamodelo de dados (peça 84). Essa limitação estrutural — derivada da insuficiência de ferramentas documentada no V1 (peça 141, §207) — significa que, mesmo que um desenvolvedor quisesse documentar que `nr_area` está em hectares ou que `nr_latitude` utiliza o datum WGS84, não há campo designado no template para registrar essa informação. A ausência desses campos estruturais é a causa direta das lacunas de unidades de medida e ambiguidade temporal documentadas nas Dimensões 2 e 3 da SE. *Corrigível pela Proposta 2.4 (gestão de metadados — inclui redesenho do template conforme ISO 11179).*

**Fatores contribuintes (contexto):**

Os fatores a seguir contextualizam a situação sem constituir causas diretas das insuficiências documentadas. São relevantes para dimensionar proporcionalmente os encaminhamentos.

**FC1 — Cobertura integral das tabelas como infraestrutura básica existente.** O dicionário de dados cobre a totalidade das 95 tabelas efetivamente em uso pelo sistema (peça 70; peça 134, p. 4; ARG-27). Essa cobertura demonstra que o esforço de documentação existiu e que a infraestrutura básica está disponível — o problema não é de inexistência, mas de qualidade semântica insuficiente. A infraestrutura existente reforça a viabilidade das propostas: aprimorar um dicionário que já existe e tem cobertura integral é significativamente menos complexo que construí-lo do zero.

**FC2 — Conhecimento semântico existente mas fragmentado.** O DRN (peça 78) e o benchmark interno de 31 campos com descrições funcionais adequadas (peça 135, p. 4) demonstram que a equipe técnica do sistema conhece o padrão desejável e sabe produzi-lo. A insuficiência não decorre de incapacidade técnica, mas da falta de processo que aplique sistematicamente esse padrão a todo o dicionário.

**FC3 — Pressão operacional e dívida técnica.** O sistema foi desenvolvido sob pressão de implantação e evolução contínua, priorizando funcionalidade em detrimento de documentação — padrão reconhecido pelo gestor como passivo documental e dívida técnica, não como omissão deliberada (peça 150, p. 59-60; ARG-28). A transição tecnológica em curso com a Dataprev tende a favorecer a consolidação de práticas de governança de dados (peça 150, p. 58-59).

**FC4 — Acolhimento expresso da recomendação pelo gestor.** O gestor avaliou que a recomendação sobre gestão de metadados pode ser acolhida, por ser pertinente e convergente com o aperfeiçoamento da governança, e propôs implementação progressiva integrada à gestão de mudanças (peça 150, p. 71; ARG-29). Esse acolhimento é elemento relevante para a sustentação processual do encaminhamento e afasta leitura de inércia ou resistência institucional.

**Conexão causa → proposta:** todas as causas de processo e produto (CP1-CP3, CD1) convergem para a Proposta 2.4 (gestão de metadados). Essa convergência é coerente com a natureza monotemática do ACH-04: as quatro causas descrevem facetas distintas de um único problema — a insuficiência no processo de produção, integração, governança e estruturação de metadados —, e a resposta institucional adequada é um único encaminhamento abrangente que endereça o processo como um todo. A Proposta 1 (determinação transversal de plano de ação) endereça o conjunto das causas dos quatro achados, incluindo o componente "metadados". O acolhimento expresso da recomendação pelo gestor (peça 150, p. 71; ARG-29) preserva a sustentação processual e reforça a viabilidade da implementação.

| Causa | Proposta que a corrige |
|---|---|
| CP1 (dicionário post-mortem sem enriquecimento semântico) | 2.4 (gestão de metadados) |
| CP2 (DRN não integrado ao dicionário) | 2.4 (gestão de metadados) |
| CP3 (metadados fora do ciclo de desenvolvimento) | 2.4 (gestão de metadados) |
| CD1 (template sem campos para unidade/datum/domínio) | 2.4 (gestão de metadados) |
| Proposta 1 (determinação transversal) | Cobre o conjunto das causas |

---

**Critérios das causas:**

Os critérios abaixo fundamentam *por que* os mecanismos identificados constituem causas — qual norma ou referencial deveria ter sido aplicado no processo e cuja não-aplicação produziu a situação encontrada. São distintos dos critérios da SE e dos critérios dos Efeitos.

**CC1. DAMA-DMBOK v2, cap. 12 — Gestão de metadados como processo** (peça 86, p. 13) — Metadados devem ser geridos como processo contínuo integrado ao ciclo de vida dos dados, com responsáveis designados, padrões definidos e revisão periódica. A ausência desse processo no CAF (CP3) e a produção do dicionário como documentação post-mortem (CP1) violam esse princípio. **Aplicação na causa** (distinta da SE): na SE, o DAMA-DMBOK fundamenta o diagnóstico de qualidade; nas causas, fundamenta a necessidade de processo de governança como condição prévia para a qualidade. **Ancoragem:** Ac. 457/2026-Plenário.

**CC2. ISO/IEC 11179-1:2023 — Metamodelo de elementos de dados** (peça 84) — Especifica que a documentação de cada elemento de dado deve incluir definição semântica, domínio de valores, unidade de medida e contexto de uso. A ausência desses campos no template do dicionário (CD1) configura insuficiência estrutural na modelagem do artefato de documentação. **Aplicação na causa** (distinta da SE): na SE, a ISO 11179 mede a qualidade do dicionário; nas causas, demonstra que o template de documentação é estruturalmente incompleto.

**CC3. COBIT 2019, BAI10 — Gestão de configuração** (peça 141, §207) — Recomenda que artefatos de documentação sejam integrados ao processo de gestão de mudanças. A manutenção do dicionário em formato estático desconectado do banco de dados (CP3) e a produção do DRN como documento avulso (CP2) contrariam esse princípio.

**CC4. Decreto nº 10.046/2019, art. 1º** (peça 82) — Governança de dados na APF, incluindo documentação e compartilhamento. A fragmentação do conhecimento entre dicionário e DRN (CP2) e a ausência de processo formal (CP3) contrariam o dever de governança documentada.

---

**Evidências das causas:**

| Ref. | Peça | Página | Descrição | Causa sustentada |
|---|---|---|---|---|
| EC1 | 75 | (doc. integral) | Dicionário: descrições tautológicas derivadas dos nomes técnicos das colunas | CP1 (mecanismo de produção) |
| EC2 | 141 | §206 | Documentação post-mortem e fragmentada; DRN com definições não incorporadas ao dicionário | CP1 (produção após desenvolvimento), CP2 (fragmentação) |
| EC3 | 78 | p. 3 | DRN v0.3: histórico de revisões — produzido em 4 dias (11-15/07/2025) por consultores externos | CP2 (contexto de produção) |
| EC4 | 78 | p. 5 | RN1.19: especifica unidades (m³, hectares) para aquicultura — informação não transferida ao dicionário | CP2 (exemplo de fragmentação) |
| EC5 | 141 | §204 | Ausência de processo formal: sem responsável, sem critérios, sem fluxo de aprovação | CP3 (mecanismo) |
| EC6 | 141 | §207 | Dicionário em CSV/Excel — artefato estático sem integração automatizada com o banco | CP3 (ferramenta inadequada) |
| EC7 | 141 | §208 | Legado histórico: múltiplas versões (CAF 1.0, 2.0, 3.0) sem revisão documental | CP3 (dívida técnica acumulada) |
| EC8 | 141 | §209 | Conhecimento de negócio e conhecimento técnico isolados em silos funcionais | CP2 (falta de integração entre equipes) |
| EC9 | 75; 141 | (doc. integral); §207 | Template em CSV/Excel sem campos para unidade de medida, datum, domínio — insuficiência de ferramentas | CD1 (limitação estrutural, ancorada em §207) |
| EC10 | 84 | (doc. integral) | ISO 11179: metamodelo requer definição semântica, domínio, unidade | CD1 (referencial de completude) |
| EC11 | 150 | p. 56-57 | Cobertura 100% das 95 tabelas reconhecida — infraestrutura básica existente (ARG-27) | FC1 (ponto positivo) |
| EC12 | 135 | p. 4 | 31 campos com descrições funcionais adequadas — benchmark interno de viabilidade | FC2 (conhecimento existente) |
| EC13 | 150 | p. 59-60 | Gestor reconhece causas como passivo documental e dívida técnica, não omissão (ARG-28) | FC3 (contexto operacional) |
| EC14 | 150 | p. 71 | Gestor acolhe expressamente a recomendação 2.4 — implementação progressiva (ARG-29) | FC4 (sustentação processual) |

### Boas Práticas e Avanços

Não foram identificadas, no escopo deste achado, boas práticas no sentido estrito da NAT §160 — práticas que, cumulativamente, ultrapassem o cumprimento do dever legal, sejam significativas, inovadoras e efetivas, e possam ser propostas para extensão a outros órgãos. Os avanços implementados pelo gestor — cobertura de 100% das 95 tabelas em uso pelo dicionário de dados, publicação do DRN v0.3 com definições funcionais relevantes em 31 campos, e acolhimento expresso da recomendação 2.4 com proposta de implementação progressiva integrada à gestão de mudanças — foram factualmente reconhecidos na Situação Encontrada e nos Fatores Contribuintes (FC1–FC4), onde contextualizam a infraestrutura existente e informam a proporcionalidade dos encaminhamentos. Registre-se que a cobertura integral do dicionário constitui requisito básico de governança de dados, e o acolhimento da recomendação configura cooperação institucional esperada, não práticas além do dever legal.

### Encaminhamentos

**Determinação:**

**Proposta 1.** Determinar ao MDA que, no prazo de 180 dias, elabore e encaminhe ao TCU plano de ação, com responsáveis, prazos e forma de comunicação do cumprimento, para avaliar as situações identificadas neste relatório e, uma vez confirmadas, adotar as medidas necessárias para seu saneamento, abrangendo as inconsistências documentadas na qualidade dos **dados de entrada**, dos **dados geoespaciais**, dos **dados cadastrais** e dos **metadados** do CAF, em conformidade com os critérios de elegibilidade previstos no art. 3º da Lei 11.326/2006 e com a finalidade de identificação e qualificação estabelecida no art. 4º do Decreto 9.064/2017.

*Justificativa do vínculo:* a determinação decorre da situação encontrada no ACH-04 — 94,1% de descrições semanticamente inadequadas, 84% de campos numéricos sem unidade de medida, 92% de campos temporais ambíguos — e dos efeitos potenciais documentados (EP1-EP5), especialmente EP4 (risco de comprometimento da sustentabilidade das melhorias dos demais achados). O componente "metadados" da determinação corresponde ao escopo deste achado.

**Recomendações:**

**Proposta 2.4.** Aprimorar gestão de metadados do CAF, assegurando definições semânticas documentadas, alinhadas às regras de negócio e ao marco legal, com responsabilidades atribuídas e atualização integrada ao ciclo de vida do sistema.

*Justificativa do vínculo:* decorre integralmente da situação encontrada no ACH-04 — insuficiência qualitativa do dicionário de dados em três das quatro dimensões analisadas — e dos efeitos potenciais EP1 (interpretação autônoma), EP2 (concentração de conhecimento), EP3 (erros em integrações) e EP4 (sustentabilidade das melhorias). Registre-se que o gestor acolheu expressamente esta recomendação, avaliando-a como pertinente e convergente com o aperfeiçoamento da governança do CAF, e propondo execução gradual integrada à gestão de mudanças (ARG-29; peça 150, p. 71). Esse acolhimento explícito constitui elemento relevante para a sustentação processual do encaminhamento.

### Benefícios Esperados

**Benefícios quantitativos:**

a) Redução da taxa de 94,1% de descrições semanticamente inadequadas no dicionário de dados (496 de 527 campos), com meta a definir pelo gestor no plano de ação (Propostas 1 e 2.4) — reversão parcial de EP1.

b) Especificação de unidade de medida para os 84% de campos numéricos atualmente sem essa informação (105 de 125 campos), com meta a definir pelo gestor (Proposta 2.4) — reversão parcial de EP3.

c) Eliminação da ambiguidade em 92% dos campos temporais (80 de 87 campos) mediante distinção entre evento de sistema e evento de negócio, com meta a definir pelo gestor (Proposta 2.4) — reversão parcial de EP1 e EP3.

**Benefícios qualitativos:**

a) Fortalecimento da capacidade de interpretação autônoma dos dados do CAF (reversão de EP1), reduzindo dependência de consultas informais aos técnicos do sistema e permitindo que novos integrantes e sistemas externos compreendam o significado dos campos sem recurso a engenharia reversa (Proposta 2.4).

b) Mitigação do risco de concentração de conhecimento crítico em poucos indivíduos (reversão de EP2), mediante documentação semântica que preserve o conhecimento institucional independentemente de turnover de pessoal (Proposta 2.4).

c) Redução do risco de erros em integrações com sistemas externos (reversão de EP3), mediante especificação de unidades de medida, datum geodésico e domínios de valores que previnam mapeamentos incorretos em cruzamentos automatizados (Proposta 2.4).

d) Fortalecimento da sustentabilidade das melhorias recomendadas nos Achados I, II e III (reversão de EP4), assegurando que validações automáticas, curadoria periódica e monitoramento por indicadores operem com base em metadados claros — condição estrutural para que as correções nos dados sejam duradouras (Proposta 2.4 como pré-requisito transversal).

e) Melhoria da auditabilidade futura do CAF (reversão de EP5), possibilitando verificação independente do sistema por órgãos de controle sem necessidade de engenharia reversa do código-fonte ou consultas repetidas aos técnicos (Proposta 2.4).
