# CHECKLIST DE QUALIDADE NAT - TCU

**Versão:** 1.0
**Base:** Normas de Auditoria do Tribunal (NAT) + Guia Consolidado
**Uso:** Validação automatizada e manual de seções de relatório

---

## **REQUISITOS GLOBAIS DE QUALIDADE (Aplicam-se a todas as seções)**

### ✅ Clareza
- [ ] Frases com no máximo 25 palavras
- [ ] Ordem direta (sujeito-verbo-complemento)
- [ ] Sem jargões desnecessários ou termos técnicos não explicados
- [ ] Leitor entende o conteúdo na primeira leitura

### ✅ Convicção
- [ ] Linguagem assertiva (evitar "parece que", "há indícios")
- [ ] Afirmações baseadas em evidências sólidas
- [ ] Sem linguagem dubitativa em achados confirmados

### ✅ Concisão
- [ ] Cada palavra tem propósito
- [ ] Sem repetições desnecessárias
- [ ] Parágrafos com 3-7 frases

### ✅ Completude
- [ ] Todas as informações necessárias presentes
- [ ] Limitações claramente declaradas
- [ ] Perspectivas dos gestores consideradas

### ✅ Exatidão
- [ ] Evidências suportam conclusões
- [ ] Números e estatísticas verificáveis
- [ ] Citações precisas (artigo, inciso)

### ✅ Relevância
- [ ] Conteúdo alinhado aos objetivos de auditoria
- [ ] Fatos irrelevantes omitidos

### ✅ Tempestividade
- [ ] Relatório emitido em tempo hábil para correções

### ✅ Objetividade
- [ ] Tom imparcial e equilibrado
- [ ] Reconhece pontos fortes e fracos
- [ ] Sem adjetivação excessiva

---

## **SEÇÃO I: CRITÉRIOS DE AUDITORIA**

### Estrutura Obrigatória
- [ ] Contexto (1-3 parágrafos, se primeiro achado sobre o tema)
- [ ] Critérios legais/regulatórios (2-5 parágrafos)
- [ ] Critérios técnicos, se aplicável (COBIT, ISO, etc.)
- [ ] Questões de auditoria (1 parágrafo, formato interrogativo e negrito)

### Critérios Legais
- [ ] Citação específica do dispositivo (Lei nº X/YYYY, Art. Y)
- [ ] Transcrição do texto legal relevante (se curto)
- [ ] Hierarquia clara (critério principal vs. secundários)
- [ ] Sem mistura com evidências ou bases de dados

### Questões de Auditoria
- [ ] Formato interrogativo
- [ ] Em negrito
- [ ] Pode ser respondida com dados
- [ ] Numeradas com (i), (ii), (iii)...

### Erros Críticos a Evitar
- [ ] ❌ Critério genérico sem artigo/inciso
- [ ] ❌ Listar base de dados como critério
- [ ] ❌ Opinião como critério ("deveria ser mais moderno")

---

## **SEÇÃO II: SITUAÇÃO ENCONTRADA**

### Estrutura Obrigatória
- [ ] Parágrafo de abertura com frase de impacto
- [ ] Quantificação clara (números, %, R$)
- [ ] Exemplos concretos e anonimizados
- [ ] Recursos visuais (tabelas e/ou gráficos)

### Quantificação
- [ ] Números em formato brasileiro (25,7% não 25.7%)
- [ ] Se amostra: projeção para população + IC + margem erro
- [ ] Valores financeiros com R$ e separação de milhares
- [ ] Tamanho de amostra declarado (n=X)

### Exemplos Ilustrativos
- [ ] Casos concretos apresentados
- [ ] Dados pessoais anonimizados
- [ ] Ilustram a natureza do problema

### Estatísticas
- [ ] Intervalo de confiança declarado
- [ ] Margem de erro declarada
- [ ] Método de amostragem descrito (se aplicável)

### Erros Críticos a Evitar
- [ ] ❌ Linguagem vaga ("muitos problemas")
- [ ] ❌ Opinião ("é preocupante que...")
- [ ] ❌ Misturar com causas ou efeitos
- [ ] ❌ Estatísticas sem IC ou margem de erro

---

## **SEÇÃO III: EVIDÊNCIAS**

### Categorias Obrigatórias (se aplicável ao achado)
- [ ] Evidências de bases de dados
- [ ] Evidências documentais
- [ ] Evidências testemunhais
- [ ] Evidências analíticas
- [ ] Documentação técnica

### Bases de Dados
- [ ] Nome do arquivo
- [ ] Data da extração
- [ ] Tamanho (registros, GB)
- [ ] Hash SHA-256
- [ ] Peça processual

### Documentos Oficiais
- [ ] Número do ofício/documento
- [ ] Data
- [ ] Signatário
- [ ] Peça processual
- [ ] **NÃO** incluir ofícios de requisição do TCU

### Análises da Equipe
- [ ] Nome do script (SQL, Python)
- [ ] Data de execução
- [ ] Breve descrição da lógica
- [ ] Arquivo de resultado (CSV) gerado
- [ ] Referência cruzada (resultado → script)

### Rastreabilidade
- [ ] Cada afirmação da Seção II tem evidência aqui
- [ ] Referências cruzadas claras
- [ ] Arquivos com hash para integridade

### Erros Críticos a Evitar
- [ ] ❌ Listar critérios (leis) como evidência
- [ ] ❌ Listar gráficos/tabelas-resumo como evidência
- [ ] ❌ Falta de hash em arquivos digitais
- [ ] ❌ Sem data de execução de scripts

---

## **SEÇÃO IV: ANÁLISE DAS CAUSAS**

### Estrutura Obrigatória
- [ ] Introdução às causas (1 parágrafo)
- [ ] 2-5 causas complementares
- [ ] Síntese mostrando interconexão (1 parágrafo)

### Cada Causa
- [ ] Explica "por quê", não "o quê"
- [ ] Baseada em evidências da Seção III
- [ ] Referências claras a parágrafos de evidências
- [ ] Foco em falhas sistêmicas, não individuais

### Fundamentação
- [ ] Cada causa vinculada a evidências específicas
- [ ] Formato: "(Ofício X, parágrafo Y)"
- [ ] Causas abordam diferentes aspectos (tecnológico, processual, contextual)

### Interconexão
- [ ] Síntese mostra como causas se relacionam
- [ ] Explica efeito combinado

### Erros Críticos a Evitar
- [ ] ❌ Repetir a situação ("causa: existem cadastros irregulares")
- [ ] ❌ Apresentar solução como causa ("falta implementar sistema X")
- [ ] ❌ Culpar indivíduos ("gestores negligentes")
- [ ] ❌ Especulação sem evidência

---

## **SEÇÃO V: EFEITOS E RISCOS**

### Estrutura Obrigatória (NAT Acórdão 1.292/2003)
- [ ] Introdução citando classificação NAT (1 parágrafo)
- [ ] Subseção "Efeitos Reais Verificados"
- [ ] Subseção "Efeitos Potenciais (Riscos)"
- [ ] Síntese dos efeitos (1 parágrafo)

### Efeitos Reais
- [ ] Consequências já ocorridas e verificadas
- [ ] Linguagem assertiva ("resulta em", "compromete")
- [ ] Baseados em evidências
- [ ] Quantificados quando possível

### Efeitos Potenciais (Riscos)
- [ ] Consequências que PODEM ocorrer
- [ ] Linguagem cautelosa ("risco de", "pode levar a")
- [ ] Plausíveis e logicamente derivados
- [ ] Não afirmam como fato o que não foi comprovado

### Quantificação
- [ ] Impacto financeiro estimado (R$)
- [ ] Ou impacto operacional (horas, processos)
- [ ] Ou impacto social (cidadãos afetados)
- [ ] Se não quantificável, justificar impossibilidade

### Erros Críticos a Evitar
- [ ] ❌ Afirmar risco como fato ("recursos foram desviados")
- [ ] ❌ Efeitos vagos ("prejudica a gestão")
- [ ] ❌ Confundir efeito com causa

---

## **SEÇÃO VI: CONCLUSÃO**

### Estrutura Obrigatória
- [ ] Introdução aos objetivos de auditoria (1 parágrafo)
- [ ] Subseção "Respostas às Questões de Auditoria"
- [ ] Subseção "Generalização dos Resultados" (NAT 159)
- [ ] Subseção "Pontos Fortes, Oportunidades e Iniciativas" (NAT 160)
- [ ] Subseção "Benefícios Esperados" (NAT 161)
- [ ] Subseção "Impacto nas Contas" (NAT 162, se aplicável)

### Respostas às Questões
- [ ] Todas as questões da Seção I respondidas
- [ ] Formato: "**Questão (i) - [tema]:** A auditoria conclui..."
- [ ] Resposta objetiva e direta
- [ ] Uma questão por parágrafo

### Generalização (NAT 159.1)
- [ ] Declaração explícita: PODE ou NÃO PODE generalizar
- [ ] Justificativa baseada em método de amostragem
- [ ] Se probabilístico: IC e margem de erro citados
- [ ] Se não probabilístico: limitação declarada

### Visão Equilibrada (NAT 160)
- [ ] Pontos fortes identificados
- [ ] Oportunidades de melhoria listadas
- [ ] Dificuldades dos gestores reconhecidas

### Benefícios Esperados (NAT 161)
- [ ] Benefícios quantificados (economia de R$, ganho de eficiência)
- [ ] Ou benefícios qualitativos descritos
- [ ] Vinculados às propostas da Seção VII

### Erros Críticos a Evitar
- [ ] ❌ Ser apenas resumo dos achados
- [ ] ❌ Omitir generalização (obrigatória)
- [ ] ❌ Ser apenas crítico (falta equilíbrio)

---

## **SEÇÃO VII: PROPOSTAS DE ENCAMINHAMENTO**

### Estrutura Obrigatória
- [ ] Introdução vinculando conclusões e causas (1 parágrafo)
- [ ] Subseção "Determinações" (se aplicável)
- [ ] Subseção "Recomendações" (se aplicável)
- [ ] Subseção "Outras Propostas" (ciência, acompanhamento)

### Mapeamento Causa-Proposta
- [ ] Cada causa da Seção IV tem proposta correspondente
- [ ] Propostas abordam as causas-raiz

### Determinações
- [ ] Usado para violação de lei/norma ou risco grave
- [ ] Prazo claro em dias (ex: 180 dias)
- [ ] Formato: **Determinação X - [título] (parágrafos Y, Z):**
- [ ] Especifica órgão destinatário
- [ ] Foca no "quê", não no "como" (NAT 165)

### Recomendações
- [ ] Usado para melhorias de gestão com discricionariedade
- [ ] Geralmente sem prazo
- [ ] Formato: **Recomendação X - [título] (parágrafos Y, Z):**

### Rastreabilidade (NAT 163)
- [ ] Todas as propostas têm referências a parágrafos
- [ ] Formato: (parágrafos 15, 27, 35, 57)

### Ciência e Acompanhamento
- [ ] Proposta de ciência a órgãos interessados
- [ ] Proposta de monitoramento do cumprimento

### Erros Críticos a Evitar
- [ ] ❌ Proposta sem causa correspondente
- [ ] ❌ Determinação sem prazo
- [ ] ❌ Prescrever solução técnica detalhada
- [ ] ❌ Esquecer referências a parágrafos (NAT 163)

---

## **VALIDAÇÕES TÉCNICAS AUTOMATIZADAS**

### Citações Legais
- [ ] Formato padronizado: "Lei nº X/YYYY, Art. Y"
- [ ] Mesma citação sempre grafada igual
- [ ] Sem variações ("nº" vs "n°" vs "numero")

### Estatísticas
- [ ] Formato brasileiro: 25,7% não 25.7%
- [ ] Milhares: 2,74 milhões não 2.74 milhões
- [ ] Cálculos verificados matematicamente

### Referências Cruzadas
- [ ] Parágrafo referenciado existe na seção citada
- [ ] Formato: "parágrafo X" não "par. X" ou "§ X"
- [ ] Referências múltiplas: "parágrafos 15, 27, 35, 57"

### Integridade de Arquivos
- [ ] Hash SHA-256 presente para bases de dados
- [ ] Nome de arquivo corresponde ao listado
- [ ] Data de extração presente

---

## **CRITÉRIOS DE BLOQUEIO vs. AVISO**

### ❌ CRÍTICO (Bloqueia aprovação)
- Referência a parágrafo inexistente
- Cálculo estatístico incorreto
- Citação legal malformada
- Questão de auditoria não respondida na conclusão
- Causa sem proposta correspondente
- Determinação sem prazo
- Proposta sem referências a parágrafos (NAT 163)

### ⚠️ AVISO (Não bloqueia, mas requer atenção)
- Terminologia inconsistente
- Parágrafo com >10 linhas
- Frase com >30 palavras
- Falta de exemplos ilustrativos
- Baixo uso de recursos visuais
- Desequilíbrio (só críticas, sem pontos fortes)

---

**Metadata:**
- **Versão:** 1.0
- **Data:** 2025-10-24
- **Base:** NAT TCU + Guia Consolidado + Achado 2 (CAF)
