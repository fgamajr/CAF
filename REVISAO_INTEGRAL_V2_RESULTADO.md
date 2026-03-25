# Revisão Integral do Relatório V2 — TC 011.073/2025-0

**Data:** 2026-03-25  
**Base de prevalência:** `MANIFEST.md` > `02_FONTE_VERDADE/` > `01_RELATORIO_V2/`

## 1. Inconsistências confirmadas

### 1.1 Estrutura do relatório descrita incorretamente na Introdução

Em [INTRODUCAO_V2.md](01_RELATORIO_V2/INTRODUCAO_V2.md), §7, o texto afirma que o relatório está organizado em **seis capítulos**, mas enumera: Introdução, Visão Geral, quatro achados, Conclusão e Propostas de Encaminhamento. Isso totaliza **sete** capítulos, não seis. Além disso, no acervo atual em `01_RELATORIO_V2/`, a Conclusão e as Propostas ainda não estão presentes como arquivos autônomos, o que reforça a necessidade de ajuste redacional para evitar promessa estrutural não materializada nesta versão.

### 1.2 Uso do dado de 32% sem a cautela metodológica da Matriz

Em [ACH01_V2.md](01_RELATORIO_V2/ACH01_V2.md), §§21 e 23, o texto utiliza o índice de conformidade integral de **32%** do monitoramento do gestor como elemento de reforço narrativo. Na [PECA170_MATRIZ_DE_ACHADOS_CAF.md](02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md), o mesmo dado aparece com ressalva explícita de que se trata de **dado do gestor, não auditado pela equipe**. Essa cautela deveria voltar ao V2 para evitar leitura de endosso probatório mais forte do que o admitido na fonte de verdade.

### 1.3 Assimetria formal no ACH-04

[ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md) abre diretamente no §49, sem título de capítulo e sem frase-síntese destacada, ao contrário de ACH-01, ACH-02 e ACH-03. O conteúdo está substantivamente alinhado, mas a ausência dessa moldura quebra a simetria do relatório e dificulta leitura isolada, remissão interna e eventual extração para voto ou instrução.

### 1.4 Introdução com chamadas de notas sem bloco local de notas

[INTRODUCAO_V2.md](01_RELATORIO_V2/INTRODUCAO_V2.md) usa chamadas `¹` a `¹⁰`, inclusive após a recente inclusão da Portaria MDA `20/2025`, mas o arquivo não contém bloco próprio de `## Notas de Fim`. Isso impede verificação autônoma da seção e quebra a rastreabilidade formal das referências no capítulo.

### 1.5 ACH-04 com marcação de notas colada

Em [ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md), no quadro-síntese do critério, a remissão aparece como `²⁵²⁶²⁷`, em vez de notas separadas ou padronizadas. O bloco de notas existe, mas a chamada consolidada dessa forma prejudica leitura, remissão e padronização editorial.

### 1.6 Acórdãos do TCU lançados como notas de fim na Visão Geral

[VISAO_GERAL_V2.md](01_RELATORIO_V2/VISAO_GERAL_V2.md) utiliza as notas `¹⁷` a `²⁰` para registrar acórdãos e processos conexos do TCU. Pelo critério desta revisão, acórdãos do Tribunal deveriam permanecer como referências processuais internas no corpo do texto, e não como notas bibliográficas de fim.

## 2. Tensões narrativas

- O [RESUMO_EXECUTIVO_V2.md](01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md), §2, está numericamente correto, mas sub-representa ACH-03 e ACH-04 ao omitir três dados fortes já estabilizados no corpo: `93,7%` de CEPs genéricos, `39` PJs com CNAE incompatível e `92%` de campos temporais ambíguos. Não é erro factual, mas enfraquece a percepção de completude dos achados 3 e 4.
- O tom geral do V2 está bem calibrado com a [PECA169_codex_anexo_comentarios_gestor_v2.md](02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md): efeitos são apresentados como potenciais, há distinção entre passivo e fluxo corrente e não há extrapolação para dano consumado ao erário.

## 3. Passe 1 — Integridade numérica

Critério aplicado: quando o dado aparece no V2, o valor foi confrontado com a [PECA170_MATRIZ_DE_ACHADOS_CAF.md](02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md). O resultado foi de **consistência material dos 22 dados-chave**. Nem todos os números precisam aparecer em todas as seções; a tabela abaixo registra presença textual, não obrigatoriedade de repetição.

| Dado | Valor Matriz | Resumo | Introdução | Visão Geral | ACH-01 | ACH-02 | ACH-03 | ACH-04 |
|---|---|---|---|---|---|---|---|---|
| Inadequação semântica | Sim | Sim | — | Sim | Sim | — | — | — |
| Divergência área | Sim | Sim | — | Sim | Sim | — | — | — |
| Tipo documental | Sim | — | — | — | Sim | — | — | — |
| Resolução <300 DPI | Sim | — | — | — | Sim | — | — | — |
| Erro cartográfico | Sim | Sim | — | Sim | — | Sim | — | — |
| Duplicações espaciais | Sim | Sim | — | — | — | Sim | — | — |
| Inconsist. municipal | Sim | — | — | — | — | Sim | — | — |
| Municípios inflação | Sim | Sim | — | — | — | Sim | — | — |
| Falecidos ativos | Sim | Sim | — | Sim | — | — | Sim | — |
| Menores titulares | Sim | Sim | — | Sim | — | — | Sim | — |
| E-mails fictícios PF | Sim | Sim | — | — | — | — | Sim | — |
| CEPs genéricos | Sim | — | — | — | — | — | Sim | — |
| Renda > R$1M | Sim | Sim | — | — | — | — | Sim | — |
| PJs CNAE | Sim | — | — | — | — | — | Sim | — |
| Descrições dicionário | Sim | Sim | — | Sim | — | — | — | Sim |
| Campos s/ unidade | Sim | Sim | — | — | — | — | — | Sim |
| Campos temporais | Sim | Sim | — | Sim | — | Sim | — | Sim |
| Pronaf safra | Sim | Sim | Sim | Sim | — | — | Sim | — |
| Leaflet redução | Sim | Sim | — | Sim | — | Sim | — | — |
| Amostra ACH-01 | Sim | — | — | Sim | Sim | — | — | — |
| Conformidade gestor | Sim | — | — | — | Sim | — | — | — |
| Renovação prevista | Sim | Sim | — | — | Sim | — | — | — |

Síntese do Passe 1:

- Não foi identificada divergência numérica entre V2 e Matriz nos dados-chave verificados.
- A Introdução é deliberadamente pouco numérica; isso não é erro, mas limita sua utilidade como peça de conferência factual.
- O Resumo Executivo cobre bem ACH-01 e ACH-02, mas resume menos ACH-03 e ACH-04.

## 4. Passe 2 — Coerência de citações e notas de fim

Resultado por arquivo:

- [ACH01_V2.md](01_RELATORIO_V2/ACH01_V2.md): chamadas `²¹` e `²²` com bloco de notas correspondente. Sem falha formal.
- [ACH02_V2.md](01_RELATORIO_V2/ACH02_V2.md): chamada `²³` com bloco correspondente. Sem falha formal.
- [ACH03_V2.md](01_RELATORIO_V2/ACH03_V2.md): chamada `²⁴` com bloco correspondente. Sem falha formal.
- [ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md): bloco existe, mas a chamada `²⁵²⁶²⁷` está colada e deve ser normalizada.
- [INTRODUCAO_V2.md](01_RELATORIO_V2/INTRODUCAO_V2.md): usa `¹` a `¹⁰`, mas não tem bloco local de notas.
- [VISAO_GERAL_V2.md](01_RELATORIO_V2/VISAO_GERAL_V2.md): bloco de notas existe e cobre `¹` a `²⁰`, mas inclui acórdãos/processos do TCU como notas bibliográficas, o que contraria o critério desta revisão.
- [RESUMO_EXECUTIVO_V2.md](01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md): não usa superscritos nem exige bloco de notas.

Síntese do Passe 2:

- Há problema estrutural na Introdução, que não pode circular isoladamente com chamadas sem notas.
- Há problema pontual de formatação em ACH-04.
- Há problema de política de citação na Visão Geral: acórdãos e processos do TCU foram tratados como notas de fim.

## 5. Passe 3 — Harmonia narrativa

Leitura sequencial aplicada: `Resumo → Introdução → Visão Geral → ACH-01 → ACH-02 → ACH-03 → ACH-04`.

Síntese do Passe 3:

- O macrofluxo está bem desenhado: o [RESUMO_EXECUTIVO_V2.md](01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md) sintetiza problema, achados, propostas e benefícios; a [INTRODUCAO_V2.md](01_RELATORIO_V2/INTRODUCAO_V2.md) fixa objeto, escopo, critérios e método; a [VISAO_GERAL_V2.md](01_RELATORIO_V2/VISAO_GERAL_V2.md) faz o storytelling institucional; e os quatro achados aprofundam tecnicamente os vetores de risco.
- Não há saltos na numeração de parágrafos: `§§1-5`, `§§1-7`, `§§8-12`, `§§13-23`, `§§24-34`, `§§35-48` e `§§49-59` estão internamente consistentes.
- A progressão narrativa também funciona: síntese executiva, depois critérios e escopo, depois contextualização, depois evidência analítica e encaminhamento por achado.
- O ponto mais fraco da cadeia é o [ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md), que perde a moldura visual e dedutiva dos demais achados ao abrir direto no §49. A transição lógica existe, porque o §59 amarra ACH-04 aos três anteriores, mas a transição formal ficou assimétrica.
- Há repetição controlada, não redundância grave: a Introdução não antecipa indevidamente a Visão Geral; a Visão Geral retoma números já vistos para montar o eixo “avanço no fluxo corrente versus passivo histórico”; e os achados voltam a esses dados com granularidade adequada.
- O tom permanece operacional e propositivo nas sete peças. Não há ruptura de registro entre capítulos.

Tensões narrativas adicionais:

- O [RESUMO_EXECUTIVO_V2.md](01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md) continua mais forte em ACH-01 e ACH-02 do que em ACH-03 e ACH-04.
- O [ACH02_V2.md](01_RELATORIO_V2/ACH02_V2.md), §34, faz boa ponte retrospectiva com ACH-01; o [ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md), §59, fecha bem o arco dos quatro achados. A transição mais fraca é da [VISAO_GERAL_V2.md](01_RELATORIO_V2/VISAO_GERAL_V2.md) para o [ACH01_V2.md](01_RELATORIO_V2/ACH01_V2.md): ela é lógica, mas pouco sinalizada por frase de passagem.

## 6. Passe 4 — Componentes obrigatórios NAT §138

Critério aplicado: confronto do V2 com a estrutura mínima de achado resumida em [NAT_QUICK_REFERENCE.md](06_NORMAS_CRITERIOS/nat_tcu/NAT_QUICK_REFERENCE.md) e [nat_checklist.md](06_NORMAS_CRITERIOS/nat_tcu/nat_checklist.md).

| Componente NAT §138 | ACH-01 | ACH-02 | ACH-03 | ACH-04 |
|---|---|---|---|---|
| Parágrafo-síntese dedutivo | Sim | Sim | Sim | Parcial |
| Situação encontrada | Sim | Sim | Sim | Sim |
| Critério de auditoria | Sim | Sim | Sim | Sim |
| Evidências em peças | Sim | Sim | Sim | Sim |
| Causas | Sim | Sim | Sim | Sim |
| Efeitos potenciais | Sim | Sim | Sim | Sim |
| Boas práticas / avanços | Sim | Sim | Sim | Sim |
| Proposta de encaminhamento | Sim | Sim | Sim | Sim |
| Benefícios esperados | Sim | Sim | Sim | Sim |
| Quadro-resumo visual | Sim | Sim | Sim | Sim |

Síntese do Passe 4:

- Os quatro achados atendem materialmente aos componentes da NAT §138, ainda que o V2 não use subtítulos formais do tipo “Situação encontrada”, “Critério” ou “Evidências” dentro de cada capítulo.
- As evidências estão embutidas na narrativa por remissões a peças e consolidadas no quadro-síntese; isso é funcional, mas menos explícito do que a decomposição da Matriz.
- O único déficit estrutural relevante continua sendo o ACH-04: ele tem conteúdo equivalente a uma frase-síntese dedutiva, mas sem cabeçalho/título destacado, o que o deixa apenas **parcialmente** conforme nesse item.
- Ponto crítico validado: **não identifiquei apresentação de efeitos como fatos consumados**. Os quatro achados usam formulações de risco, limitação potencial, redução de capacidade ou possibilidade de comprometimento, em linha com a natureza operacional da auditoria.

## 7. Passe 5 — Consistência com Matriz de Achados

Critério aplicado: confronto narrativo com a [PECA170_MATRIZ_DE_ACHADOS_CAF.md](02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md).

Síntese do Passe 5:

- Os títulos dos achados **não são idênticos** aos da Matriz. No V2, ACH-01, ACH-02 e ACH-03 foram convertidos em formulações mais dedutivas e orientadas a efeito; isso melhora a legibilidade do relatório, mas reduz a identidade literal com a fonte de verdade. Em [ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md), o problema é maior: o título da Matriz simplesmente não foi reproduzido.
- As causas centrais da Matriz estão representadas na narrativa do V2. Em termos materiais, o encadeamento C1-C6 foi preservado, ainda que sem rotulação alfanumérica.
- Os efeitos da Matriz também estão representados, com boa aderência ao tratamento de efeitos potenciais e com caveats incorporados do contraditório.
- A **Proposta 1** (plano de ação em 180 dias) aparece nos quatro achados do V2, em coerência com a Matriz.
- A **Proposta 2.1.3** (interoperabilidade com bases oficiais relevantes) aparece de forma expressa em [ACH03_V2.md](01_RELATORIO_V2/ACH03_V2.md), §47, e de forma material em [ACH01_V2.md](01_RELATORIO_V2/ACH01_V2.md), §22, ao mencionar interoperabilidade com bases oficiais relevantes. Isso está coerente com a Matriz, que a associa a ACH-01 e ACH-03, não a ACH-02 nem a ACH-04.
- Não identifiquei proposta “inventada” no V2 em desacordo com a Matriz. O que há é compressão narrativa das propostas, não desvio de conteúdo.

## 8. Passe 6 — Tom e equilíbrio

Síntese do Passe 6:

- O tom está adequadamente calibrado para auditoria operacional. Não há linguagem de fraude, punição ou imputação indevida de irregularidade como conclusão do trabalho.
- [ACH01_V2.md](01_RELATORIO_V2/ACH01_V2.md), §§17-18, usa caveats corretos: não converte inconsistência documental em inelegibilidade definitiva nem em dano consumado ao erário.
- [ACH02_V2.md](01_RELATORIO_V2/ACH02_V2.md), §§28-29, também preserva a distinção entre limitação cartográfica e comprometimento automático da finalidade jurídica do cadastro.
- [ACH03_V2.md](01_RELATORIO_V2/ACH03_V2.md), §§39 e 42-45, faz o tratamento mais sensível do relatório: reconhece exclusão digital, trata falecidos e menores como problema de curadoria/governança e não de fraude demonstrada, e incorpora a concordância do gestor sobre governança de dados imatura.
- [ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md), §§50 e 53-59, usa analogias acessíveis (“manual de instruções”, “caixa-preta”) e torna o tema de metadados compreensível para leitor não técnico.
- O relatório reconhece avanços do gestor em pontos relevantes: CAF 3.0, Leaflet, TED DCAF/UFES, renovação de `~742 mil` registros e providências prospectivas. Isso atende ao requisito de visão equilibrada.
- A liberdade de meios está preservada de modo consistente. Os achados falam em “resultados a alcançar”, “não prescrição fechada” ou fórmula equivalente.

## 9. Passe 7 — Elementos visuais

Inventário:

| Seção | Tabelas | Quadros | Figuras | Têm fonte? | Numeração OK? |
|---|---:|---:|---:|---|---|
| Resumo | 0 | 0 | 0 | n/a | Sim |
| Introdução | 0 | 0 | 0 | n/a | Sim |
| Visão Geral | 0 | 2 | 0 | Sim | Sim |
| ACH-01 | 2 | 1 | 0 | Sim | Sim |
| ACH-02 | 2 | 2 | 0 | Sim | Sim |
| ACH-03 | 2 | 1 | 0 | Sim | Sim |
| ACH-04 | 2 | 1 | 0 | Sim | Sim |

Síntese do Passe 7:

- A numeração visual está sequencial no conjunto do relatório: `Tabela 1-8` e `Quadro 1-5`, sem colisões ou saltos.
- Cada achado cumpre o mínimo operacional pedido nesta revisão: pelo menos uma tabela de dados e um quadro-resumo.
- Resumo e Introdução não têm elementos visuais. Isso não é erro, mas reforça a dependência da Visão Geral e dos achados para comunicação gráfica.
- Não foram identificadas figuras, o que não compromete a peça, mas reduz variedade visual em tema com forte componente geoespacial.

## 10. Passe 8 — Conformidade com modelos TCU

Critério aplicado: confronto com [07_MODELOS_TCU/README.md](07_MODELOS_TCU/README.md) e checklist NAT.

Síntese do Passe 8:

- A estrutura principal do V2 está alinhada ao modelo TCU: Resumo, Introdução, Visão Geral e Achados. O problema é que, no estado atual da pasta `01_RELATORIO_V2/`, **Conclusão** e **Propostas de Encaminhamento** ainda não existem como arquivos autônomos.
- A Introdução não abre por acórdão; abre pelo objeto e sua relevância para políticas públicas, o que é adequado.
- A [VISAO_GERAL_V2.md](01_RELATORIO_V2/VISAO_GERAL_V2.md) cumpre bem a função de storytelling e mapeamento de riscos, com extensão compatível com uma visão geral de objeto.
- Os achados 1 a 3 seguem método dedutivo de abertura. O achado 4 rompe esse padrão formal.
- O V2 está coerente com a expectativa de anexos e apêndices do template, mas essa promessa ainda é programática: Introdução menciona Anexos A-C e Apêndices I-VI, enquanto a pasta em revisão contém apenas os sete capítulos principais.
- Em termos de modelo TCU, o V2 está **próximo de conforme**, mas ainda não completo como relatório fechado.

## 11. Sugestões de harmonização

- Corrigir o §7 da Introdução para refletir a estrutura real do V2 atual.
- Reintroduzir, onde aparecer o dado de `32%`, a fórmula: “dado produzido pelo gestor, não auditado pela equipe”.
- Inserir em [ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md) um cabeçalho equivalente aos demais achados: título, frase-síntese e abertura narrativa.
- Inserir bloco próprio de `## Notas de Fim` em [INTRODUCAO_V2.md](01_RELATORIO_V2/INTRODUCAO_V2.md), incluindo a Portaria MDA `20/2025`.
- Normalizar a chamada `²⁵²⁶²⁷` em [ACH04_V2.md](01_RELATORIO_V2/ACH04_V2.md).
- Remover da [VISAO_GERAL_V2.md](01_RELATORIO_V2/VISAO_GERAL_V2.md) a dependência de notas para acórdãos/processos internos do TCU, preservando-os como referências processuais no corpo.
- Reforçar o Resumo Executivo com pelo menos um dado adicional de ACH-03 e um de ACH-04 para evitar desbalanceamento do panorama.

## 12. Observações finais

O V2 está numericamente consistente com a Matriz nos dados centrais testados e, no essencial, preserva a calibragem exigida pelo contraditório. Os passes 3 a 8 confirmam que o texto já tem base sólida de mérito, boa progressão argumentativa e tom adequado de auditoria operacional. Os ajustes pendentes seguem localizados: concentram-se em simetria formal do ACH-04, política de notas de fim, aderência literal seletiva à Matriz e completude estrutural do relatório fechado.
