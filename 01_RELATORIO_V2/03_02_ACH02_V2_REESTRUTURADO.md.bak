# ACHADO 02

**Limitações geoespaciais acumuladas ao longo das transições tecnológicas comprometem a integridade cartográfica e a rastreabilidade do CAF**

24. A auditoria concluiu que as transições tecnológicas do CAF, embora tenham trazido avanços pontuais, acumularam limitações na qualidade geoespacial da base por relaxamento de validações na migração para o CAF 3.0, trade-offs de interface na adoção do Leaflet e ausência de curadoria estruturada do estoque legado. O resultado é uma base ativa em que a taxa total de erro cartográfico alcançou 45,92% (peça 119, p. 9), as duplicações espaciais permaneceram em 55,27% dos registros de alta precisão (peça 117, p. 14-15), 15,92% das coordenadas recaem fora do município declarado (peça 116, p. 14) e 632 municípios exibem inflação cadastral (peça 121, p. 9), em desacordo com o dever de melhoria da qualidade e fidedignidade dos dados. Esse quadro reduz a confiabilidade das informações de localização, limita a efetividade de validações baseadas em dados cartográficos e pode comprometer a capacidade do CAF de sustentar análises territoriais e cruzamentos com bases georreferenciadas oficiais.

## 4.1 Qualidade geoespacial do CAF: contexto e referencial de avaliação

25. Os dados geoespaciais do CAF não são mero acessório gráfico. Eles representam a localização do imóvel rural, dão suporte à identificação territorial do beneficiário e ajudam a qualificar a elegibilidade quando a política pública depende de área, município ou inserção territorial. Essa relevância, contudo, precisa ser lida com precisão: conforme sustentado pelo gestor e acolhido pela equipe, o achado não demonstra comprometimento automático da finalidade jurídica do cadastro, mas limitação na qualidade dos dados de localização. É nesse ponto que se instala a tensão narrativa do ACH-02. A evolução tecnológica do sistema não foi linear. A base ativa combina registros herdados da DAP e do CAF 2.x com cadastros produzidos já no CAF 3.0 e, mais recentemente, na interface Leaflet. Cada transição resolveu parte do problema, mas deixou passivos ou introduziu novas fragilidades, de modo que a modernização do fluxo corrente convive, hoje, com um estoque heterogêneo de qualidade desigual.

**Quadro 2** — Evolução do georreferenciamento nas transições tecnológicas do CAF

| Etapa | Ganho principal | Passivo ou trade-off remanescente |
|---|---|---|
| DAP / legado inicial | Formação do acervo territorial inicial | Registros sem curadoria geoespacial uniforme e forte heterogeneidade de origem |
| CAF 2.x | Existência de validações mais restritivas de envelope geográfico | Persistência de duplicações e passivo histórico sem saneamento estruturado |
| CAF 3.0 | Modernização do sistema e melhora funcional geral | Relaxamento de validações de bounding box e elevação da taxa total de erro para 45,92% |
| Leaflet | Redução de duplicações em novos cadastros e eliminação quase total dos erros algorítmicos | Aumento de erros geoespaciais, perda de precisão decimal e permanência do passivo histórico |

*Fonte: elaboração da equipe de auditoria com base nas peças 117, 118, 119, 121, 150 e Matriz de Achados do CAF.*

25a. A análise da qualidade geoespacial do CAF apoia-se em dois referenciais complementares. O primeiro é a ISO 19157-1:2023, norma internacional de qualidade de dados geográficos (peça 83), que estrutura a avaliação em elementos como exatidão posicional (positional accuracy), consistência lógica (logical consistency) e completude (completeness). O segundo é o DAMA-DMBOK v2, que trata de dimensões transversais como acurácia, unicidade, consistência e gestão do ciclo de vida (peça 86, Cap. 13). A convergência entre os dois referenciais permite organizar as constatações em cinco dimensões de qualidade geoespacial: exatidão posicional, unicidade espacial, consistência municipal, integridade territorial e gestão de transições tecnológicas.

25b. Para manter comparabilidade com o ACH-01, a equipe adota a mesma escala sintética de maturidade: 0 = ad-hoc; 1 = inicial; 2 = repetível; 3 = definido; 4 = gerenciado; 5 = otimizado. Trata-se de escala analítica adaptada do DAMA-DMBOK e do CMMI-DMM, não de aplicação literal da taxonomia de nenhum desses referenciais. O propósito é apenas situar o estágio observado em cada dimensão da qualidade geoespacial.

### 4.1.1 Diagnóstico por dimensão de qualidade geoespacial

#### Dimensão 1 — Exatidão posicional (erro cartográfico)

26. A dimensão quantitativa do problema é expressiva. A população analisada compreende 3.175.345 imóveis rurais da base ativa, examinados por amostra estratificada temporal de 63.588 registros, com intervalo de confiança de 99% e margem de erro efetiva de ±0,40 ponto percentual (peça 110, p. 4). A primeira evidência foi a piora global da taxa de erro cartográfico na transição para o CAF 3.0: o indicador subiu de 32,66% para 45,92%, afetando aproximadamente 1,46 milhão de imóveis (peça 119, p. 9). O agravamento decorreu, sobretudo, do relaxamento das validações de envelope geográfico (`bounding box`). Enquanto a versão anterior rejeitava coordenadas fora dos limites territoriais esperados para o Brasil, o CAF 3.0 passou a aceitar coordenadas em qualquer ponto do intervalo mundial válido, sem verificar pertinência ao território brasileiro (peça 119, p. 34). Na linguagem da ISO 19157-1:2023, trata-se de comprometimento da exatidão posicional absoluta — o atributo que mede a proximidade entre os valores de coordenadas informados e os valores aceitos como verdadeiros. Em termos de maturidade, a situação é **Ad-hoc (0)**: a migração de versão não incorporou testes de regressão aptos a proteger o controle posicional existente.

#### Dimensão 2 — Unicidade espacial (duplicações)

26a. A segunda evidência veio da unicidade espacial: entre 43.812 registros de alta precisão, 55,27% compartilham coordenadas idênticas com outros imóveis, projetando-se aproximadamente 1,75 milhão de casos na população (peça 117, p. 14-15). O caso de Salvador/BA materializa o problema: 6.644 imóveis foram cadastrados no mesmo ponto do Centro Histórico, área urbana em que a existência de milhares de propriedades rurais distintas é fisicamente impossível (peça 123, p. 2-3). A observação do gestor de que duplicação espacial não equivale, por si, a duplicidade jurídica de beneficiários é correta e foi incorporada ao texto: famílias agregadas, assentamentos e comunidades tradicionais podem explicar parte das coincidências. Ainda assim, o patamar de 55,27% confirma limitação relevante de rastreabilidade espacial. O Leaflet reduziu a taxa de duplicações em novos cadastros de 92,36% para 16,59% (peça 117, p. 15) — avanço significativo que demonstra capacidade de reação institucional —, mas o passivo histórico de duplicações permanece ativo na base sem curadoria estruturada. Em termos de maturidade, a prática é **Inicial (1)**: o Leaflet contém o fluxo corrente, mas o estoque pré-Leaflet permanece aberto e sem programa de saneamento.

**Tabela 3** — Síntese quantitativa das limitações geoespaciais do ACH-02

| Dimensão | Indicador | Resultado |
|---|---|---:|
| Erro cartográfico global | Taxa total de erro após CAF 3.0 | 45,92% |
| Erro cartográfico global | Imóveis potencialmente afetados | ~1,46 milhão |
| Duplicações espaciais | Registros de alta precisão com coordenadas idênticas | 55,27% |
| Duplicações espaciais | Projeção populacional de duplicações | ~1,75 milhão |
| Consistência municipal | Coordenadas fora do município declarado | 15,92% |
| Inflação cadastral | Municípios com área CAF superior à área oficial | 632 |
| Reanálise ministerial | Municípios com materialidade residual | 50 |

*Fonte: elaboração da equipe de auditoria com base nas peças 116, 117, 119, 121 e 161.*

#### Dimensão 3 — Consistência municipal (coordenadas × município declarado)

27. A terceira frente do conflito é a consistência territorial. A análise identificou que 15,92% dos registros de alta precisão têm coordenadas fora do município declarado, com subconjunto de 722 casos apontando para unidade da federação completamente diversa da informada (peça 116, p. 14). A ISO 19157-1:2023 trata esse tipo de falha sob o elemento de consistência lógica — especificamente a consistência de domínio, que avalia se os valores de um atributo recaem dentro do domínio esperado. Aqui, o domínio é o território do município declarado; 15,92% dos registros o violam. O Leaflet, ao substituir digitação manual por seleção visual em mapa sem validação de aderência municipal, contribuiu para a elevação dos erros geoespaciais em 174% (peça 118, p. 16). Em termos de maturidade, a situação é **Ad-hoc (0)**: não há validação automática de consistência entre coordenada e município na entrada do cadastro.

#### Dimensão 4 — Integridade territorial (inflação cadastral)

27a. A análise censitária encontrou 632 municípios em que a área total cadastrada no CAF supera a área oficial do município, tendo Penalva/MA como caso extremo, com área cadastrada 2.248 vezes maior que a área oficial (peça 121, p. 9). Desses 632, o subconjunto mais crítico era formado por 608 municípios com cobertura igual ou superior a 100% da área oficial. É sobre esse grupo que incidiu a reanálise ministerial (peça 161, p. 1-4), que reclassificou 558 casos como improcedentes e deixou 50 municípios com materialidade residual, dos quais 10 com indício de plausibilidade e 40 dependentes de averiguação complementar. Isso não elimina o problema; apenas redefine seu alcance probatório. A inflação municipal funciona como triagem exploratória de risco, não como conclusão automática de impropriedade cadastral. A integração com o PNRA/Incra introduziu, em parte dos registros, a área total do assentamento sem discriminação da fração ideal por beneficiário, produzindo excesso nominal na leitura agregada por município (peça 161, p. 2-3) — o que é, em si, problema de interoperabilidade que reforça a pertinência de aprimorar a harmonização de dados. Em termos de maturidade, a situação é **Ad-hoc (0)**: não há alerta automático para anomalias territoriais na base.

#### Dimensão 5 — Gestão de transições tecnológicas

27b. A quinta dimensão torna visível problema que, no texto corrido anterior, aparecia diluído nas causas (§§30-31). Cada transição tecnológica do CAF (DAP → CAF 2.x → CAF 3.0 → Leaflet) alterou o modelo de georreferenciamento, mas nenhuma delas foi precedida de testes de regressão aptos a verificar se a qualidade do estoque seria preservada. O caso mais ilustrativo é o trade-off do Leaflet: a interface praticamente zerou os erros algorítmicos (de 22,22% para 0,01%), mas elevou em 174% os erros geoespaciais (peça 118, p. 16) e reduziu em 14,33 pontos percentuais a proporção de registros com alta precisão decimal (peça 115, p. 6). A tabela abaixo sintetiza o trade-off.

**Tabela 4** — Trade-off da transição Leaflet

| Período | Erros algorítmicos | Erros geoespaciais | Taxa total de erro |
|---|---:|---:|---:|
| Pré-Leaflet | 22,22% | 11,83% | 34,05% |
| Pós-Leaflet | 0,01% | 32,46% | 32,47% |
| Variação | -22,21 p.p. | +20,63 p.p. | -1,58 p.p. |

*Fonte: elaboração da equipe de auditoria com base na peça 118, p. 16. Amostra estratificada temporal com IC 99%.*

O DAMA-DMBOK trata a gestão de mudanças como função de governança essencial para que alterações em sistemas não comprometam a integridade dos dados existentes (peça 86, Cap. 13). No caso do CAF, o resultado foi que a modernização do fluxo de entrada coexiste com um estoque herdado cuja qualidade não foi objeto de curadoria estruturada. Além disso, a base não incorpora metadados de origem que permitam distinguir qual versão tecnológica produziu cada registro — informação necessária para priorizar o saneamento por estrato temporal. Em termos de maturidade, a situação é **Ad-hoc (0)**: não há política formal de gestão de mudanças que incorpore qualidade de dados geoespaciais como requisito.

### 4.1.2 Quadro de maturidade da qualidade geoespacial do CAF

| Dimensão (referencial) | Indicador-chave | Prática observada | Nível |
|---|---|---|---|
| Exatidão posicional (ISO 19157) | 45,92% de erro cartográfico | Migração sem teste de regressão; bounding box relaxado | Ad-hoc (0) |
| Unicidade espacial (DAMA-DMBOK) | 55,27% de duplicações | Nova interface de cadastramento reduziu duplicações em novos registros (92,36%→16,59%); estoque sem curadoria | Inicial (1) |
| Consistência lógica territorial (ISO 19157 adaptada) | 15,92% fora do município | Sem validação de aderência municipal na entrada | Ad-hoc (0) |
| Completude territorial (ISO 19157 adaptada) | 632 municípios > IBGE | Sem alerta automático para anomalias territoriais | Ad-hoc (0) |
| Gestão de transições (DAMA-DMBOK / COBIT) | DAP→CAF2→3→Leaflet sem regressão | Sem política formal de mudanças para dados geoespaciais | Ad-hoc (0) |
| **Média aritmética** | | Estágio predominantemente reativo, com avanço pontual em unicidade (Leaflet) | **0,20** |

*Escala adaptada pela equipe com base no DAMA-DMBOK v2, Cap. 13, CMMI-DMM e ISO 19157-1:2023: 0 = Ad-hoc (sem processo formal); 1 = Inicial (processo existente, não repetível); 2 = Repetível; 3 = Definido; 4 = Gerenciado; 5 = Otimizado. Trata-se de escala analítica adaptada — não de aplicação literal da taxonomia de nenhum desses referenciais. As dimensões combinam elementos da ISO 19157 (exatidão posicional, consistência lógica), do DAMA-DMBOK (unicidade, gestão do ciclo de vida) e de adaptações ao contexto do CAF (integridade territorial, gestão de transições), conforme indicado entre parênteses no quadro.*

*Fonte: elaboração da equipe de auditoria com base nas peças 83, 86, 110-122, 150 e 161.*

**Nota comparativa:** a média de maturidade geoespacial (0,20) é inferior à de dados de entrada do ACH-01 (0,43). A comparação é indicativa, não absoluta: os dois quadros utilizam a mesma escala, mas avaliam dimensões distintas — qualidade documental no ACH-01 e qualidade geoespacial no ACH-02. A diferença reflete a maior complexidade técnica da dimensão espacial e a ausência quase total de processos formais de governança geoespacial. A única dimensão acima do nível ad-hoc é a unicidade espacial, justamente onde a nova interface de cadastramento produziu avanço mensurável.

## 4.2 Efeitos potenciais

28. Esses resultados geram, em primeiro lugar, risco de limitação na individualização cartográfica da base cadastral. Se aproximadamente 1,75 milhão de imóveis compartilham coordenadas idênticas, a base perde capacidade de distinguir propriedades individualmente para cruzamentos com outras bases, análises de sobreposição e monitoramento territorial. A observação do gestor de que duplicação espacial não equivale, por si, a duplicidade jurídica de beneficiários é correta e foi incorporada ao texto: famílias agregadas, assentamentos e comunidades tradicionais podem explicar parte das coincidências. Ainda assim, o patamar de 55,27% confirma limitação relevante de rastreabilidade espacial. O segundo efeito potencial é a redução da confiabilidade de validações baseadas em localização. Com taxa de erro cartográfico de 45,92%, o CAF passa a oferecer suporte menos confiável para análises que dependam de localização correta do imóvel, inclusive a verificação espacial do limite de 4 módulos fiscais previsto na Lei 11.326/2006, ainda que essa verificação não se realize exclusivamente dentro do cadastro.

29. O terceiro efeito potencial é a degradação de precisão associada às transições tecnológicas. O Leaflet melhorou o problema da digitação manual, mas o fez à custa de maior erro semântico de localização, o que evidencia insuficiência de gestão de mudanças e de formalização de requisitos não funcionais de qualidade geoespacial. O quarto efeito potencial é a distorção analítica em decisões públicas baseadas em dados territoriais do CAF. Coordenadas incorretas, municípios inconsistentes e áreas agregadas sem harmonização tendem a produzir diagnósticos territoriais menos confiáveis, com repercussão sobre planejamento, monitoramento e priorização de ações públicas. O quinto efeito potencial, mais prospectivo, é a propagação de erros em integrações externas futuras. O gestor demonstrou que o dado georreferenciado não é compartilhado automaticamente pelas APIs sociais do cadastro, o que reduz a materialização imediata desse risco. Ainda assim, se a base for consumida em integrações futuras sem saneamento prévio, o erro tende a se propagar. Em todos esses casos, a auditoria não identificou efeitos concretos consumados nem prejuízos individualizados; os efeitos são apresentados como potenciais, coerentemente com a natureza operacional do trabalho.

## 4.3 Causas

30. As causas do achado mostram que a deterioração cartográfica não decorre de um único defeito, mas da interação entre mudanças de versão, validações insuficientes e ausência de curadoria do passivo. A primeira causa está na migração para o CAF 3.0 sem testes de regressão aptos a proteger a integridade geoespacial. Ao relaxar a validação de envelope geográfico (`bounding box`), o sistema deixou de bloquear coordenadas fora do envelope brasileiro e elevou substancialmente os erros algorítmicos (peça 119, p. 34). A segunda está na implantação do Leaflet sem trava de consistência municipal. A interface tornou a entrada mais amigável e reduziu erros de sintaxe, mas permitiu que o usuário selecionasse livremente um ponto no mapa sem verificação automática de aderência ao município declarado. A terceira causa é a ausência de indicadores formais de qualidade geoespacial que tornassem visível a magnitude do passivo. Sem métricas contínuas de duplicação, inconsistência municipal e inflação cadastral, a gestão melhorou o fluxo de entrada, mas sem programa estruturado de remediação do estoque herdado.

31. Há ainda causas de produto e fatores contribuintes que completam a narrativa. A integração com o PNRA/Incra introduziu, em parte dos registros, a área total do assentamento sem discriminação da fração ideal por beneficiário, produzindo excesso nominal na leitura agregada por município (peça 161, p. 2-3). Isso explica parcela relevante da inflação cadastral aparente, mas também confirma problema de interoperabilidade e harmonização de dados. Além disso, o modelo de dados não impunha restrições suficientes de unicidade espacial nem validava plausibilidade territorial na ingestão, o que permitiu acúmulo de duplicações e incoerências em larga escala. Como fatores contribuintes, a equipe reconheceu a heterogeneidade do passivo, a implantação recente do Leaflet e práticas inadequadas de cadastramento na ponta, como o uso da sede municipal como referência geográfica genérica. Esses elementos explicam a forma do problema, mas não afastam sua reincidência. Desde o Acórdão 1197/2018, o Tribunal já exigia salvaguardas de qualidade de dados e procedimentos de validação e cruzamento, exigências que permanecem sem cumprimento integral. Também aqui, portanto, há um problema novo em sua forma, mas não inédito em sua raiz.

## 4.4 Contexto do gestor e avanços reconhecidos

31a. O contraditório evidenciou avanços que precisam ser reconhecidos para manter a proporcionalidade do achado. O mais significativo foi a implementação do Leaflet, que produziu o maior ganho individual entre todos os achados deste relatório: a taxa de duplicações em novos cadastros caiu de 92,36% para 16,59% (peça 117, p. 15) — redução de 82% —, e os erros algorítmicos foram praticamente eliminados (peça 118, p. 16). Também se observou queda da inflação cadastral em novos registros (de 10,89% para 0,31%; peça 121, p. 9) e redução quase total de coordenadas fora do território brasileiro. Esses ganhos mostram capacidade de inovação técnica e reação institucional. A questão central, portanto, não é ausência de capacidade, mas extensão da curadoria ao estoque acumulado. A base ativa combina registros de quatro gerações tecnológicas distintas, e os avanços do Leaflet, por mais expressivos que sejam, aplicam-se apenas ao fluxo de novos cadastros. A maturação gradual do sistema é consistente com o que o DAMA-DMBOK descreve como evolução por patamares — o que justifica encaminhamentos por risco e materialidade, não saneamento cego e massivo.

## 4.5 Boas práticas

32. No plano das boas práticas, a equipe não identificou experiência que atendesse cumulativamente aos requisitos da NAT §160 para ser formalmente classificada como tal. Houve, porém, avanços parciais que precisam ser reconhecidos para manter a proporcionalidade do achado. O mais importante foi a implementação do Leaflet, que reduziu a taxa de duplicações em novos cadastros de 92,36% para 16,59% (peça 117, p. 15) e eliminou praticamente a totalidade dos erros algorítmicos (peça 118, p. 16). Também se observou queda da inflação cadastral em novos registros e redução quase total de coordenadas fora do território brasileiro. Esses ganhos mostram capacidade de reação institucional e ajudam a distinguir fluxo corrente e passivo histórico. Não bastam, contudo, para converter a experiência em boa prática formal, porque vieram acompanhados de regressão na consistência municipal e na precisão decimal, além de não terem sido estendidos ao estoque acumulado.

## 4.6 Propostas de encaminhamento

33. Os encaminhamentos devem, por isso, combinar saneamento do passivo e prevenção de regressões futuras. A determinação transversal de apresentação de plano de ação em 180 dias permanece cabível, no componente geoespacial, para avaliar as situações identificadas e, uma vez confirmadas, promover o saneamento das inconsistências. No plano das recomendações específicas, o núcleo da resposta está em garantir integridade e consistência dos dados críticos de localização, aprimorar a gestão de mudanças para que novas versões não introduzam regressões funcionais ou comprometam a integridade dos dados, e implantar monitoramento contínuo com indicadores capazes de tornar visível a magnitude do passivo e medir a efetividade das correções. Todas essas medidas foram formuladas como resultados a alcançar, e não como prescrição fechada de solução, preservando a liberdade de meios do gestor e a abordagem prospectiva e orientada por risco defendida no contraditório, em linha com o dever de melhoria da qualidade e fidedignidade dos dados previsto no Decreto 10.046/2019²³.

**Quadro 3** — Síntese do Achado 02

| Componente | Síntese |
|---|---|
| Situação encontrada | 45,92% de erro cartográfico, 55,27% de duplicações espaciais, 15,92% de inconsistência municipal e 632 municípios com inflação cadastral |
| Critério | Lei 11.326/2006, art. 3º, I; Decreto 9.064/2017, art. 4º; Decreto 10.046/2019²³; COBIT 2019; ISO 19157-1:2023 |
| Efeitos potenciais | Limitação da individualização cartográfica, redução da confiabilidade de validações baseadas em localização, regressão de precisão em transições tecnológicas, distorção analítica e risco prospectivo de propagação em integrações |
| Causas principais | Relaxamento de validações no CAF 3.0, Leaflet sem trava de consistência municipal, ausência de indicadores formais, integração PNRA/Incra sem harmonização e passivo histórico sem curadoria |
| Propostas associadas | Plano de ação em 180 dias, integridade de dados críticos, gestão de mudanças e monitoramento contínuo |

*Fonte: elaboração da equipe de auditoria com base na Matriz de Achados do CAF e nas peças 116, 117, 118, 119, 121, 150 e 161.*

## 4.7 Benefícios esperados

34. Os benefícios esperados são, sobretudo, de recuperação da confiabilidade territorial do cadastro. Em termos quantitativos, espera-se reduzir a taxa de erro cartográfico hoje em 45,92%, diminuir o estoque de duplicações espaciais hoje em 55,27%, consolidar os ganhos do Leaflet em novos cadastros e estender a curadoria ao passivo histórico, além de reduzir a inconsistência municipal hoje em 15,92%. Em termos qualitativos, a principal mudança é devolver ao CAF capacidade mais segura de individualização cartográfica, de validação baseada em localização e de produção de informação territorial útil para análises e cruzamentos com bases oficiais. Para a sociedade, isso significa aumentar a confiabilidade do cadastro que serve de suporte às políticas de agricultura familiar, reduzir o risco de diagnósticos territoriais distorcidos e criar condições para que futuras integrações geoespaciais ocorram sobre base mais íntegra. Se o ACH-01 mostrou que documentação insuficiente fragiliza a porta de entrada, o ACH-02 demonstra que localização inconsistente fragiliza o território dessa mesma porta; enfrentar ambos os problemas é condição para que o CAF cumpra, com maior segurança, sua função de identificação e qualificação da agricultura familiar.

---

## Notas de Fim (Apêndice VI)

²³ BRASIL. Decreto nº 10.046, de 9 de outubro de 2019. Dispõe sobre a governança no compartilhamento de dados no âmbito da administração pública federal. Brasília: Presidência da República, 2019.
