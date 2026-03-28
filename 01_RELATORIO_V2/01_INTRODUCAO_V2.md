# 1. INTRODUÇÃO

1. O Cadastro Nacional da Agricultura Familiar (CAF) é o principal instrumento de identificação e qualificação dos beneficiários de políticas públicas de agricultura familiar no Brasil (Decreto 9.064/2017, art. 4º). O cadastro funciona como habilitação prévia para acesso ao Programa Nacional de Fortalecimento da Agricultura Familiar (Pronaf), que movimentou R$ 59,6 bilhões na safra 2023/2024¹, ao Programa de Aquisição de Alimentos (PAA) e ao Programa Nacional de Alimentação Escolar (PNAE). A qualidade dos dados cadastrais condiciona a capacidade do CAF de atestar a elegibilidade dos cadastrados e, por consequência, a focalização dessas políticas.

2. Fragilidades na qualidade de dados do cadastro que antecedeu o CAF, a Declaração de Aptidão ao Pronaf (DAP), foram documentadas pelo Acórdão 1197/2018-TCU-Plenário, cujas determinações permanecem pendentes de implementação integral após três monitoramentos (Acórdãos 1866/2021-TCU-Plenário e 885/2024-TCU-Plenário). Diante desse cenário, o Tribunal decidiu avaliar a qualidade dos dados da versão atual do cadastro (CAF 3.0).

3. Trata-se de auditoria operacional com o objetivo de avaliar se os mecanismos de verificação de dados do CAF (versão 3, período de março a agosto de 2025) asseguram o atendimento dos requisitos essenciais de qualidade de dados e de regras de negócio, e se a estrutura de governança e gestão de dados aplicada ao cadastro assegura padrões claros, papéis definidos, rastreabilidade e integridade das informações ao longo de todo o ciclo de vida dos dados. A descrição detalhada do objeto consta da Visão Geral do Objeto (Capítulo 2).

4. O escopo abrangeu quatro dimensões de qualidade dos dados: documental, geoespacial, cadastral e de metadados. A profundidade incluiu cruzamento com bases externas (RFB, Sisobi, CNIS, Sigef, Sicar, IBGE), análise de amostra probabilística estratificada e classificação semântica automatizada de documentos. A unidade fiscalizada foi a Secretaria de Agricultura Familiar e Agroecologia do Ministério do Desenvolvimento Agrário e Agricultura Familiar (SAF/MDA), conforme a Portaria de Fiscalização 343/2025-AudTI (peça 3).

5. Os principais critérios de auditoria foram: a Lei 11.326/2006² e o Decreto 9.064/2017³, que estabelecem os requisitos de elegibilidade e a finalidade do CAF; as Portarias MDA 19/2025⁴, 20/2023⁵ e 20/2025, que disciplinam, respectivamente, as condições gerais de inscrição no CAF, os procedimentos gerais de inscrição sob o regime anterior e o ingresso na rede das entidades credenciadas para realizar inscrições; o framework DAMA-DMBOK v2⁶ e a norma ISO/IEC 25012:2008⁷, como referenciais de qualidade e governança de dados; o COBIT 2019 (BAI10)⁸, para gestão de mudanças e configuração; a ISO 19157-1:2023⁹, para qualidade de dados geoespaciais; a ISO/IEC 11179:2015¹⁰, para gestão de metadados; e os Acórdãos 1197/2018-TCU-Plenário (Rel. Min. Subst. André Luís de Carvalho) e 457/2026-TCU-Plenário (Rel. Min. Augusto Nardes).

6. Para responder às questões de auditoria, foram empregadas técnicas de revisão documental, cruzamento massivo de bases de dados governamentais, análise geoespacial, classificação semântica de documentos por inteligência artificial e análise estatística de amostra probabilística. O detalhamento da metodologia consta do Apêndice I deste relatório.

7. As análises e conclusões finais do presente trabalho foram efetuadas em conformidade com as Normas de Auditoria do Tribunal de Contas da União (NAT), aprovadas pela Portaria-TCU 280/2010, em alinhamento com as Normas Internacionais das Entidades Fiscalizadoras Superiores (ISSAI), emitidas pela Organização Internacional de Entidades Fiscalizadoras Superiores (INTOSAI). Todas as evidências coletadas durante a execução do trabalho foram submetidas à aplicação de testes de suficiência, relevância e confiabilidade. Não foram identificadas limitações que comprometessem a suficiência ou a confiabilidade das evidências.

8. O relatório está organizado em sete capítulos: a presente Introdução; a Visão Geral do Objeto; quatro capítulos de achados — qualidade da documentação comprobatória (ACH-01), integridade geoespacial (ACH-02), governança e curadoria cadastral (ACH-03) e gestão de metadados (ACH-04); e a Conclusão, seguida das Propostas de Encaminhamento. Acompanham o relatório três anexos: Análise dos Comentários dos Gestores (Anexo A), Matriz de Achados (Anexo B) e Matriz de Planejamento (Anexo C). Complementam-no seis apêndices: Método (Apêndice I), Metodologia Estatística (Apêndice II), Trabalhos Anteriores do TCU sobre o Tema (Apêndice III), Glossário (Apêndice IV), Lista de Siglas, Figuras e Tabelas (Apêndice V) e Notas de Fim (Apêndice VI).

---

## Notas de Fim (Apêndice VI)

¹ BRASIL. Agência Gov. Com Lula, Pronaf investe R$ 59,6 bilhões na agricultura familiar, aumento de 12,1% em relação à safra 2022/2023. Brasília: Governo Federal, 22 jul. 2024. Disponível em: https://agenciagov.ebc.com.br/noticias/202407/com-lula-pronaf-investe-r-59-6-bilhoes-na-agricultura-familiar-aumento-de-12-1-em-relacao-a-safra-2022-2023. Acesso em: 24 mar. 2026.

² BRASIL. Lei nº 11.326, de 24 de julho de 2006. Estabelece as diretrizes para a formulação da Política Nacional da Agricultura Familiar e Empreendimentos Familiares Rurais. Diário Oficial da União, Brasília, DF, 25 jul. 2006. Disponível em: https://www.planalto.gov.br/ccivil_03/_ato2004-2006/2006/lei/l11326.htm. Acesso em: 24 mar. 2026.

³ BRASIL. Decreto nº 9.064, de 31 de maio de 2017. Dispõe sobre a Unidade Familiar de Produção Agrária, institui o Cadastro Nacional da Agricultura Familiar e regulamenta a Lei nº 11.326/2006. Diário Oficial da União, Brasília, DF, 31 maio 2017. Disponível em: https://www.planalto.gov.br/ccivil_03/_Ato2015-2018/2017/Decreto/D9064.htm. Acesso em: 24 mar. 2026.

⁴ BRASIL. Ministério do Desenvolvimento Agrário e Agricultura Familiar. Portaria MDA nº 19, de 21 de março de 2025. Dispõe sobre as condições e os procedimentos gerais de inscrição no Cadastro Nacional da Agricultura Familiar — CAF. Diário Oficial da União, Brasília, DF, 26 mar. 2025. Disponível em: https://www.gov.br/mda/pt-br/acesso-a-informacao/acoes-e-programas/programas-projetos-acoes-obras-e-atividades/cadastro-nacional-da-agricultura-familiar/PortariaMDAn19.pdf. Acesso em: 24 mar. 2026.

⁵ BRASIL. Ministério do Desenvolvimento Agrário e Agricultura Familiar. Portaria MDA nº 20, de 27 de junho de 2023. Dispõe sobre as condições e os procedimentos gerais de inscrição no Cadastro Nacional da Agricultura Familiar — CAF. Diário Oficial da União, Brasília, DF, 28 jun. 2023. Disponível em: https://www.gov.br/mda/pt-br/acesso-a-informacao/acoes-e-programas/programas-projetos-acoes-obras-e-atividades/cadastro-nacional-da-agricultura-familiar/Portaria_MDA_20_2023.pdf. Acesso em: 24 mar. 2026.

⁶ DAMA INTERNATIONAL. *DAMA-DMBOK: Data Management Body of Knowledge*. 2. ed. Basking Ridge: Technics Publications, 2017. ISBN 978-1-63462-174-4.

⁷ INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. ISO/IEC 25012:2008 — Software engineering — Software product Quality Requirements and Evaluation (SQuaRE) — Data quality model. Geneva: ISO, 2008.

⁸ INFORMATION SYSTEMS AUDIT AND CONTROL ASSOCIATION. COBIT 2019 Framework: Governance and Management Objectives. Schaumburg: ISACA, 2018. BAI10 — Managed Configuration.

⁹ INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. ISO 19157-1:2023 — Geographic information — Data quality — Part 1: General requirements. Geneva: ISO, 2023.

¹⁰ INTERNATIONAL ORGANIZATION FOR STANDARDIZATION. ISO/IEC 11179-1:2015 — Information technology — Metadata registries (MDR) — Part 1: Framework. Geneva: ISO, 2015.
