49. Devido à maturidade ainda incipiente da gestão de metadados do CAF, em que o conhecimento técnico existe, mas permanece fragmentado entre instrumentos não integrados e sem atualização incorporada ao ciclo de desenvolvimento, a única documentação estruturada do banco de dados apresenta insuficiência qualitativa relevante: 94,1% das descrições do dicionário são semanticamente inadequadas, 84% dos campos numéricos não informam unidade de medida e 92% dos campos temporais permanecem ambíguos, embora haja cobertura formal de 100% das 95 tabelas efetivamente em uso. Esse quadro não traduz ausência absoluta de documentação, mas compromete potencialmente a rastreabilidade, a auditabilidade, a interpretação independente dos dados e a manutenção evolutiva do sistema, além de reduzir a sustentabilidade das melhorias recomendadas nos achados anteriores, já que validação, curadoria e monitoramento dependem de metadados claros para se manterem consistentes ao longo do tempo.

50. O tema é mais abstrato do que os dos achados anteriores, porque não trata diretamente de documentos, mapas ou pessoas cadastradas, mas da infraestrutura semântica que permite compreender tudo isso. Em termos simples, o dicionário de dados funciona como o manual de instruções do banco de dados do CAF. É ele que deveria explicar, para cada campo, o que a informação significa, em que unidade está expressa, qual evento temporal registra e como deve ser interpretada. Quando esse manual é insuficiente, o sistema não deixa de funcionar, mas passa a operar como caixa-preta: só compreende plenamente seus dados quem já conhece as regras implícitas. No caso do CAF, isso é especialmente sensível porque a base reúne 527 campos documentados e integra esquema maior com 109 tabelas, das quais 95 estavam efetivamente em uso no momento da análise e cobertas pelo dicionário (peça 70; peça 134, p. 4).

51. A auditoria constatou, assim, um conflito claro entre o que existe e o que deveria existir. De um lado, há infraestrutura básica de documentação, ponto positivo que precisa ser reconhecido: o dicionário cobre integralmente as tabelas em uso e o Documento de Regras de Negócio do CAF 3.0 contém definições funcionais relevantes (peça 78). De outro, a qualidade semântica dessa documentação permanece insuficiente para os padrões de gestão de metadados preconizados pela ISO/IEC 11179, pelo DAMA-DMBOK v2 e pela governança de dados da Administração Pública. A análise censitária dos 527 campos mostrou que 496 descrições, equivalentes a 94,1%, são inadequadas porque apenas repetem o nome técnico da coluna ou empregam fórmulas genéricas que não ajudam o leitor a compreender o dado em contexto de negócio (peça 135, p. 4). Em vez de explicar, o dicionário frequentemente apenas reescreve o nome da variável em português corrido.

**Tabela 7** — Síntese das insuficiências do dicionário de dados do CAF

| Dimensão | Universo analisado | Situação identificada | Resultado |
|---|---:|---|---:|
| Cobertura formal | 95 tabelas em uso | Tabelas documentadas no dicionário | 100% |
| Qualidade semântica | 527 campos | Descrições inadequadas | 94,1% |
| Unidade de medida | 125 campos numéricos | Campos sem unidade especificada | 84% |
| Clareza temporal | 87 campos temporais | Campos ambíguos quanto ao evento registrado | 92% |

*Fonte: elaboração da equipe de auditoria com base nas peças 132, 133, 134, 135 e 136.*

52. A deficiência torna-se mais visível quando se abandona a abstração e se olha para exemplos concretos. O campo `id_area_imovel`, por exemplo, aparece descrito como “ID de identificação de área imóvel”, expressão tautológica que não informa sua função no modelo de dados; `nr_area` surge como “Tamanho da área imóvel”, sem dizer se o valor está em hectares, metros quadrados ou outra unidade; `nr_latitude` e `nr_longitude` não informam datum ou formato; `dt_criacao` e `dt_atualizacao` não distinguem se se referem à criação técnica do registro ou ao evento de negócio subjacente (peça 75; peça 133, p. 6-8; peça 136, p. 5-6). Em outras palavras, o manual existe, mas grande parte de suas instruções é insuficiente para orientar quem precisa operar, integrar, auditar ou evoluir o sistema.

**Tabela 8** — Exemplos de descrições atuais e do conteúdo semântico que deveriam conter

| Campo | Descrição atual no dicionário | O que deveria conter |
|---|---|---|
| `id_area_imovel` | “ID de identificação de área imóvel” | Identificador único da área do imóvel vinculada à unidade familiar e usado para relacionamento entre tabelas |
| `nr_area` | “Tamanho da área imóvel” | Área do imóvel rural em hectares (ha), com precisão definida e uso associado à verificação do limite legal |
| `nr_latitude` | “Latitude da área imóvel” | Latitude em graus decimais, com indicação do datum geodésico adotado |
| `dt_criacao` | “Data criação” | Data e hora de criação técnica do registro no banco de dados, distinta de eventos de negócio |
| `dt_atualizacao` | “Data atualização” | Data e hora da última atualização técnica do registro, com distinção em relação a vigência cadastral |
| `vl_renda_auferida` | “Valor renda auferida” | Valor da renda familiar auferida no período de referência, em reais (R$), conforme regra de negócio aplicável |

*Fonte: elaboração da equipe de auditoria com base nas peças 75, 78, 133 e 136.*

53. Essa lacuna semântica projeta efeitos potenciais relevantes. O primeiro é a limitação da interpretação autônoma dos dados. Se o campo `nr_area` não informa sua unidade, a implementação de validações de área, como as discutidas nos achados anteriores, depende de conhecimento tácito sobre o que o sistema “quer dizer” com aquele valor. Se um campo temporal como `dt_cadastro` ou `dt_atualizacao` não distingue evento de sistema, vigência ou atualização de negócio, a curadoria de registros desatualizados, cancelados ou herdados de versões anteriores torna-se menos confiável. O segundo efeito potencial é a concentração de conhecimento crítico em poucos indivíduos. Quando o significado dos campos não está suficientemente formalizado, ele se preserva por meio da memória dos técnicos mais antigos, e não por documentação institucional durável.

54. O terceiro efeito potencial é o aumento do risco de erro silencioso em integrações, consultas analíticas e manutenção evolutiva. Sistemas externos e equipes novas podem consumir a mesma coluna com premissas diferentes sem perceber a divergência. Também por isso este achado é, em larga medida, um achado-plataforma. As melhorias propostas para documentos comprobatórios, georreferenciamento e dados cadastrais exigem saber, com precisão, o que cada campo representa. Sem isso, validações automáticas podem incidir sobre o atributo errado, integrações com bases oficiais podem ser mapeadas de forma equivocada e o monitoramento contínuo da qualidade fica dependente de engenharia reversa. O quarto efeito potencial é a limitação da auditabilidade futura do CAF. Um sistema relevante para políticas públicas não pode exigir, a cada nova fiscalização, consultas reiteradas aos seus “intérpretes autorizados” para explicar o que cada dado significa.

55. As causas ajudam a entender por que o manual de instruções chegou a esse ponto. A primeira é que o dicionário foi produzido e mantido, em grande medida, como documentação posterior ao desenvolvimento, sem enriquecimento semântico sistemático. O resultado natural de documentação post mortem é a descrição tautológica: registra-se o nome do campo, mas não seu significado de negócio. A segunda é a fragmentação do conhecimento entre o dicionário de dados e o Documento de Regras de Negócio. A peça 78 contém definições úteis, inclusive exemplos de unidades de medida e regras materiais, mas essas informações não foram vinculadas campo a campo ao artefato consultado por quem tenta entender a estrutura do banco. Assim, o conhecimento existe, porém espalhado.

56. A terceira causa é que a gestão de metadados ainda não está plenamente integrada ao ciclo de vida do sistema como artefato obrigatório de mudança, com responsáveis, padrões mínimos e revisão contínua. O dicionário permanece em formato estático, desvinculado de processo robusto de controle de versão semântica. A quarta é a limitação do próprio template documental, que não favorece o registro estruturado de unidade de medida, datum geodésico, domínio de valores e natureza do evento temporal. Essas causas foram agravadas por fatores contribuintes adequadamente descritos no contraditório: pressão operacional, dívida técnica acumulada ao longo das transições do CAF, reconstrução institucional do MDA e priorização legítima de entregas funcionais em detrimento da documentação. O gestor reconheceu essa moldura como problema qualitativo de maturidade, não como vazio absoluto de governança, e acolheu expressamente a recomendação correspondente (peça 150, p. 57-60 e 71).

57. No plano das boas práticas, a equipe não identificou experiência que atendesse cumulativamente aos critérios da NAT §160. Houve, contudo, avanços parciais relevantes. O primeiro é a cobertura integral das 95 tabelas em uso pelo dicionário, o que fornece base concreta para melhoria incremental em vez de reconstrução do zero. O segundo é a existência de 31 campos com descrição funcional adequada, benchmark interno que demonstra viabilidade técnica imediata. O terceiro é o próprio acolhimento, pelo gestor, de implementação progressiva e integrada à gestão de mudanças. Esses pontos não convertem o caso em boa prática formal, mas mostram que o sistema já dispõe de alicerces institucionais para amadurecer a gestão de metadados.

58. Os encaminhamentos, por isso, devem preservar liberdade de meios e concentrar-se no resultado a alcançar. A determinação transversal de apresentação de plano de ação em 180 dias é pertinente também para este achado, porque permite ao gestor organizar, por risco e criticidade, a revisão do passivo documental e a consolidação de critérios mínimos de metadados. Especificamente para o ACH-04, a Proposta 2.4 responde de forma direta ao problema identificado: aprimorar a gestão de metadados do CAF, assegurando definições semânticas documentadas, alinhadas às regras de negócio e ao marco legal, com responsabilidades atribuídas e atualização integrada ao ciclo de vida do sistema. Não se está impondo ferramenta única, modelo fechado ou saneamento massivo imediato; define-se, isto sim, a necessidade de que o manual do sistema passe a explicar, de modo verificável, o que seus dados significam.

**Quadro 5** — Síntese do Achado 04

| Componente | Síntese |
|---|---|
| Situação encontrada | Dicionário de dados com 94,1% de descrições inadequadas, 84% de campos numéricos sem unidade de medida e 92% de campos temporais ambíguos, apesar de cobertura formal de 100% das 95 tabelas em uso |
| Critério | ISO/IEC 11179, DAMA-DMBOK v2, Decreto 10.046/2019, COBIT 2019 e referenciais de governança de dados adotados pelo TCU²⁵²⁶²⁷ |
| Efeitos potenciais | Limitação da interpretação autônoma, concentração de conhecimento tácito, risco de erro em integrações e perda de sustentabilidade das melhorias recomendadas nos achados anteriores |
| Causas principais | Documentação post mortem, fragmentação entre dicionário e regras de negócio, metadados fora do ciclo de desenvolvimento e template sem campos estruturais suficientes |
| Propostas associadas | Plano de ação em 180 dias e aprimoramento da gestão de metadados do CAF com atualização contínua e responsabilidades definidas |

*Fonte: elaboração da equipe de auditoria com base na Matriz de Achados do CAF e nas peças 75, 78, 132, 133, 134, 135, 136 e 150.*

59. Os benefícios esperados são concretos e estruturantes. Em primeiro lugar, espera-se reduzir progressivamente a taxa de 94,1% de descrições inadequadas, especificar unidade para os 105 campos numéricos sem essa informação e eliminar a ambiguidade dos 80 campos temporais cuja semântica ainda é incerta. Em segundo lugar, espera-se diminuir a dependência de conhecimento tácito, preservando institucionalmente informações hoje dispersas entre documentos e memória de equipes. Em terceiro lugar, espera-se ampliar a auditabilidade e a interoperabilidade do CAF. Sobretudo, espera-se dar sustentação às melhorias dos demais achados: corrigir a porta documental do cadastro, a coerência territorial dos imóveis e a curadoria dos registros cadastrais exige saber com precisão o que cada campo representa. Se o ACH-01 tratou do que entra no sistema, o ACH-02 do lugar onde o cadastro se ancora e o ACH-03 da consistência das pessoas e vínculos registrados, o ACH-04 trata da linguagem comum que torna essas correções duráveis. Para a sociedade, o ganho final é um CAF menos opaco, mais auditável e preparado para sustentar, com continuidade, políticas públicas voltadas à agricultura familiar.

---

## Notas de Fim (Apêndice VI)

²⁵ ISO/IEC 11179. Information technology — Metadata registries.

²⁶ BRASIL. Decreto nº 10.046, de 9 de outubro de 2019.

²⁷ ISACA. COBIT 2019. Objective BAI10.
