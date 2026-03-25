# Referência Rápida - Normas de Auditoria do TCU (NAT)

## 📋 Índice Rápido

| NAT | Título | Seção Aplicável | Criticidade |
|-----|--------|-----------------|-------------|
| 129 | Requisitos de Qualidade | Todas | ⚠️ AVISO (maioria) |
| 138 | Matriz de Achados - Estrutura | Todas | ❌ CRÍTICA |
| 140 | Quantificação de Achados | II - Situação | ❌ CRÍTICA |
| 156-162 | Conclusões | VI - Conclusão | ❌ CRÍTICA |
| 163-166 | Propostas de Encaminhamento | VII - Propostas | ❌ CRÍTICA |

---

## 📖 NAT 129 - Requisitos de Qualidade (Todas as Seções)

| Requisito | Descrição | Validação | Tipo |
|-----------|-----------|-----------|------|
| **CLAREZA** | Textos de fácil compreensão, frases curtas | Frases ≤30 palavras, siglas em glossário | ⚠️ AVISO |
| **CONVICÇÃO** | Expor achados com firmeza | Evitar: "supõe-se", "parece que", "talvez" | ⚠️ AVISO |
| **CONCISÃO** | Máximo de informações de forma breve | Relatório ≤30 páginas, parágrafos ≤10 linhas | ⚠️ AVISO |
| **COMPLETUDE** | Toda informação necessária presente | Relações objetivos↔critérios↔achados↔conclusões claras | ❌ CRÍTICA |
| **EXATIDÃO** | Evidências sustentam achados | Cálculos corretos, citações exatas, dados verificáveis | ❌ CRÍTICA |
| **RELEVÂNCIA** | Apenas o que tem importância | Fatos contribuem para conclusões e propostas | ⚠️ AVISO |
| **TEMPESTIVIDADE** | Emissão tempestiva | Cumprir prazos sem comprometer qualidade | ⚠️ AVISO |
| **OBJETIVIDADE** | Evidências imparciais, tom equilibrado | Evitar adjetivos/advérbios que impliquem crítica sem suporte | ❌ CRÍTICA |

---

## 🧩 NAT 138 - Matriz de Achados (Estrutura Completa do Achado)

> **Papel de trabalho que estrutura o desenvolvimento dos achados**

| Aspecto | Seção | Skill Responsável | Crítico? |
|---------|-------|-------------------|----------|
| **I. Descrição/Título** | - | (manual) | ❌ SIM |
| **II. Situação Encontrada** | II | `tcu-secao-ii-situacao` | ❌ SIM |
| **III. Objetos Constatados** | II | `tcu-secao-ii-situacao` | ❌ SIM |
| **IV. Critério de Auditoria** | I | `tcu-secao-i-criterios` | ❌ SIM |
| **V. Evidências** | III | `tcu-secao-iii-evidencias` | ❌ SIM |
| **VI. Causas** | IV | `tcu-secao-iv-causas` | ❌ SIM |
| **VII. Efeitos Reais/Potenciais** | V | `tcu-secao-v-efeitos` | ❌ SIM |
| **VIII. Responsável** | - | (manual) | ❌ SIM |
| **IX. Esclarecimentos** | - | (manual) | ⚠️ Não |
| **X. Conclusão da Equipe** | VI | `tcu-secao-vi-conclusao` | ❌ SIM |
| **XI. Propostas** | VII | `tcu-secao-vii-propostas` | ❌ SIM |

### Observações Importantes

- **Aspecto II (Situação)**: Descrição factual do que foi encontrado, **com quantificação obrigatória**
- **Aspecto IV (Critério)**: Norma legal/técnica **específica** (Art. X), não lei genérica
- **Aspecto V (Evidências)**: Provas **rastreáveis e reprodutíveis** (hashes SHA-256)
- **Aspecto VI (Causas)**: **Por quê** ocorreu (causas-raiz), não "o quê" ocorreu (sintomas)
- **Aspecto VII (Efeitos)**: Distinguir claramente **efeitos reais** vs. **riscos potenciais**
- **Aspecto XI (Propostas)**: Foco no **"quê"**, não no **"como"** (NAT 165)

---

## 📊 NAT 140 - Quantificação de Achados (Seção II)

> **Relatar achados descrevendo natureza e extensão do trabalho**

### Requisitos Obrigatórios

✅ **Quantificar em termos de**:
- População ou número de casos examinados (n=X)
- Percentuais (formato brasileiro: 25,7% não 25.7%)
- Valores monetários ou outras medidas
- Intervalo de confiança (IC 99%)
- Tamanho de amostra

### Exemplo Conforme

```markdown
27. Análise da base de dados CAF (11.377.318 registros, Peça 45)
identificou 8.764.123 documentos comprobatórios (77,0% do total) que
não atendem aos requisitos estabelecidos pela Portaria MDA nº 19/2025,
art. 4º, quanto à legibilidade e completude das informações. Amostra
aleatória de 646 documentos (IC=99%, erro=3,5%, seed=42) confirmou o
padrão: 497 documentos inadequados (76,9% da amostra).
```

### Bloqueios Comuns

❌ **NÃO CONFORME**:
- "Muitos documentos estão inadequados" (sem quantificação)
- "A maioria dos processos" (vago)
- "25.7% dos casos" (formato americano, usar 25,7%)
- Estatísticas sem IC informado

---

## ✅ NAT 156-162 - Conclusões (Seção VI)

### NAT 156 - Resposta à Questão Fundamental

❌ **CRÍTICO**: Trazer resposta à **questão fundamental** da auditoria (objetivo) e às **questões do escopo**

### NAT 157 - Força das Conclusões

Conclusões dependem de:
- Suficiência e adequação das evidências
- Solidez da lógica
- Concordância dos usuários com propostas

### NAT 158 - Conclusões como Afirmações Deduzidas

Conclusões são **afirmações deduzidas dos achados**, considerando:
- Diferença entre situação encontrada e critério
- Efeitos avaliados

### NAT 159 - Generalização dos Resultados ⭐

❌ **CRÍTICO**: Mencionar **expressamente** se resultados podem ou não ser generalizados

| Tipo de Amostra | Generalização? | O que Informar |
|----------------|----------------|----------------|
| **Probabilística** (aleatória) | ✅ SIM | Informar IC e erro embutidos nos cálculos |
| **Não Probabilística** (intencional) | ❌ NÃO | Conclusões aplicam-se **exclusivamente** aos elementos examinados |

**Exemplo (Probabilística)**:
```markdown
As conclusões deste achado podem ser generalizadas para toda a população
de documentos CAF (11.377.318 registros), com intervalo de confiança de
99% e margem de erro de 3,5%, conforme amostra probabilística de 646
documentos (seed=42).
```

**Exemplo (Não Probabilística)**:
```markdown
As conclusões deste achado aplicam-se exclusivamente aos 15 contratos
examinados (seleção intencional com base em valor e complexidade), não
sendo possível generalização estatística para o universo de contratos.
```

### NAT 160 - Visão Equilibrada (Auditorias Operacionais)

❌ **CRÍTICO**: Destacar de forma **equilibrada**:
- ✅ Pontos fortes do objeto
- ⚠️ Oportunidades de melhoria
- 📈 Benefícios esperados (quantificar sempre que possível)
- 🤝 Dificuldades enfrentadas pelos gestores
- 💡 Iniciativas positivas dos gestores

### NAT 161 - Benefício Total Estimado

⚠️ **AVISO**: Relatar benefício total estimado ou esperado das propostas

### NAT 162 - Impacto nas Contas

⚠️ **AVISO**: Indicar eventual impacto dos achados nas contas das entidades auditadas

---

## 📝 NAT 163-166 - Propostas de Encaminhamento (Seção VII)

### NAT 163 - Consistência e Referências ⭐

❌ **CRÍTICO**:
1. Propostas **consistentes** com achados
2. Decorrentes **logicamente** dos achados e conclusões
3. Focadas nas **causas** identificadas
4. **Indicar entre parênteses** os números dos parágrafos onde achados foram apresentados

**Exemplo Conforme**:
```markdown
Determinar à Secretaria Nacional de Agricultura Familiar que implante
validações semânticas automatizadas no upload de documentos do Sistema
CAF, conforme Portaria MDA nº 19/2025, art. 4º (parágrafos 27, 32 e 45).
```

### NAT 164 - Tipos de Proposta

Podem ser formuladas:
- Recomendações
- Determinações
- Medidas saneadoras
- Medidas cautelares
- Outras previstas legal/regimentalmente

### NAT 165 - Foco no "Quê", Não no "Como" ⭐

❌ **CRÍTICO**: Propostas devem focar **"o quê"** deve ser aperfeiçoado/corrigido, NÃO **"o como"**

**Razão**: Discricionariedade do gestor + equipe não detém única/melhor solução

**Exceção**: Quando se justifica proposta específica (ex: alterar legislação)

| ✅ CONFORME (Foco no "Quê") | ❌ NÃO CONFORME (Prescreve "Como") |
|------------------------------|-------------------------------------|
| "Implante validações semânticas automatizadas" | "Implante validações usando biblioteca Python pdfplumber versão 0.5.28" |
| "Estabeleça controles de qualidade para documentos" | "Contrate 15 analistas de qualidade e crie departamento específico" |
| "Corrija as inconsistências nos registros" | "Execute o script correcao_v2.sql fornecido pela equipe" |

### NAT 166 - Requisitos para Determinações

❌ **CRÍTICO**: Determinações exigem avaliação de **requisitos indispensáveis** (norma específica do TCU)

---

## 🧮 Matriz de Validações por Seção

### Seção I - Critérios de Auditoria

| Validação | Tipo | NAT |
|-----------|------|-----|
| Critérios legais específicos (Art. X, não lei genérica) | ❌ CRÍTICA | 138-IV |
| Hierarquia normativa respeitada (Lei → Decreto → Portaria) | ❌ CRÍTICA | - |
| Questões em formato interrogativo e negrito | ❌ CRÍTICA | - |
| Contexto muito longo (>3 parágrafos) | ⚠️ AVISO | 129-CONCISÃO |
| Questões muito amplas ou vagas | ⚠️ AVISO | 129-CLAREZA |

### Seção II - Situação Encontrada

| Validação | Tipo | NAT |
|-----------|------|-----|
| Quantificação presente (%, valores absolutos, IC) | ❌ CRÍTICA | 140 |
| Tom factual (sem opiniões ou adjetivos valorativos) | ❌ CRÍTICA | 129-OBJETIVIDADE |
| Exemplos concretos incluídos | ❌ CRÍTICA | 129-COMPLETUDE |
| Falta de intervalo de confiança em estatísticas | ⚠️ AVISO | 140 |
| Ausência de tamanho de amostra (n=X) | ⚠️ AVISO | 140 |

### Seção III - Evidências

| Validação | Tipo | NAT |
|-----------|------|-----|
| Rastreabilidade total (hashes SHA-256 para arquivos digitais) | ❌ CRÍTICA | 138-V |
| Cada afirmação da Seção II tem evidência correspondente | ❌ CRÍTICA | 129-COMPLETUDE |
| Referências cruzadas claras | ❌ CRÍTICA | 129-EXATIDÃO |
| Reprodutibilidade (informações para reexecutar análises) | ❌ CRÍTICA | 129-EXATIDÃO |
| Falta de datas de extração | ⚠️ AVISO | 129-COMPLETUDE |
| Evidências sem responsável pela coleta | ⚠️ AVISO | 129-COMPLETUDE |

### Seção IV - Causas

| Validação | Tipo | NAT |
|-----------|------|-----|
| Causas explicam 'por quê', não 'o quê' | ❌ CRÍTICA | 138-VI |
| Fundamentação em evidências | ❌ CRÍTICA | 129-EXATIDÃO |
| Causas atacáveis por propostas | ❌ CRÍTICA | 163 |
| Causas muito genéricas | ⚠️ AVISO | 129-RELEVÂNCIA |
| Falta de síntese de interconexão | ⚠️ AVISO | 129-COMPLETUDE |

### Seção V - Efeitos e Riscos

| Validação | Tipo | NAT |
|-----------|------|-----|
| Distinção clara: Efeitos Reais vs. Riscos | ❌ CRÍTICA | 138-VII |
| Linguagem assertiva (reais) vs. cautelosa (riscos) | ❌ CRÍTICA | 129-CONVICÇÃO |
| Efeitos derivam logicamente da situação encontrada | ❌ CRÍTICA | 129-COMPLETUDE |
| Falta de quantificação de impacto | ⚠️ AVISO | 140 |
| Riscos sem probabilidade estimada | ⚠️ AVISO | 129-COMPLETUDE |

### Seção VI - Conclusão

| Validação | Tipo | NAT |
|-----------|------|-----|
| Todas as questões de Seção I respondidas | ❌ CRÍTICA | 156 |
| Generalização explícita (NAT 159) | ❌ CRÍTICA | 159 |
| Visão equilibrada (pontos fortes + oportunidades) | ❌ CRÍTICA | 160 |
| Conclusões deduzidas dos achados | ❌ CRÍTICA | 158 |
| Falta de benefícios esperados | ⚠️ AVISO | 161 |
| Ausência de impacto nas contas | ⚠️ AVISO | 162 |

### Seção VII - Propostas de Encaminhamento

| Validação | Tipo | NAT |
|-----------|------|-----|
| Mapeamento Causa → Proposta completo | ❌ CRÍTICA | 163 |
| Referências a parágrafos entre parênteses | ❌ CRÍTICA | 163 |
| Foco no 'quê', não no 'como' | ❌ CRÍTICA | 165 |
| Determinações com prazo, Recomendações sem prazo | ❌ CRÍTICA | - |
| Proposta muito genérica | ⚠️ AVISO | 129-RELEVÂNCIA |
| Falta de justificativa para determinação vs. recomendação | ⚠️ AVISO | 166 |

---

## 🔍 Uso Prático

### Para Auditores

1. **Durante Redação**: Consultar validações da seção correspondente
2. **Antes de Validação**: Revisar requisitos críticos (❌)
3. **Após Bloqueio**: Localizar NAT correspondente para entender requisito

### Para Skills

1. **Durante Geração**: Aplicar requisitos críticos da seção
2. **Durante Validação**: Verificar conformidade com NATs aplicáveis
3. **Ao Bloquear**: Citar NAT específico no relatório de erro

### Referências Cruzadas

- **Índice Completo**: `common/nat_tcu/nat_index.json`
- **NAT Completas**: `common/nat_tcu/normas_auditoria_nat_tcu.md`
- **Manual de Auditoria**: `common/nat_tcu/Manual_auditoria_operacional_4_edicao.pdf`
- **Checklist Operacional**: `common/nat_checklist.md`

---

**Última Atualização**: 25/10/2025
**Versão**: 1.0
