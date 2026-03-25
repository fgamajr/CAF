# PROMPT: Revisão Integral do Relatório V2 — Auditoria CAF (TC 011.073/2025-0)

## Quem é você nesta tarefa

Você é um **revisor independente** de um relatório de auditoria do Tribunal de Contas da União (TCU), o órgão supremo de controle externo do Brasil. Você NÃO participou da elaboração do relatório — seu papel é revisar com olhos frescos, verificar integridade e harmoniza do conjunto.

---

## PASSO ZERO — Ler o MANIFEST.md

**ANTES DE QUALQUER COISA**, leia o arquivo `MANIFEST.md` na raiz do projeto. Ele contém:
- Contexto completo da auditoria
- Hierarquia de documentos (o que prevalece sobre o quê)
- Mapa de todas as pastas
- Índice de peças por achado
- 22 dados-chave para verificação cruzada
- Instruções de indexação e busca

```bash
cd /Users/fgamajr/Desktop/CAF-FINAL
cat MANIFEST.md
```

---

## ESTRUTURA DO PROJETO (já reorganizado)

```
CAF-FINAL/
├── MANIFEST.md                          ← LER PRIMEIRO
├── ANALISE_ESTRUTURA.md                 ← Relatório de reorganização
│
├── 00_CONTEXTO/        (3 arquivos)     ← Resumo + Visão Geral (ler segundo)
│   └── README.md
│
├── 01_RELATORIO_V2/    (7 arquivos)     ← O QUE ESTÁ SENDO REVISADO
│   ├── README.md
│   ├── RESUMO_EXECUTIVO_V2.md           §1-5
│   ├── INTRODUCAO_V2.md                 §1-7
│   ├── VISAO_GERAL_V2.md               §8-12
│   ├── ACH01_V2.md                      §13-23
│   ├── ACH02_V2.md                      §24-34
│   ├── ACH03_V2.md                      §35-48
│   └── ACH04_V2.md                      §49+
│
├── 02_FONTE_VERDADE/   (4 arquivos)     ← HIERARQUIA MÁXIMA
│   ├── README.md
│   ├── MATRIZ_DE_ACHADOS_CAF.md         ← 🏛️ Constituição
│   ├── MATRIZ_DE_ACHADOS_CAF.docx
│   └── ANEXO_COMENTARIOS_GESTOR.md      ← 📜 Lei complementar
│
├── 03_RELATORIO_V1/    (4 arquivos)     ← Referência histórica
│   ├── README.md
│   ├── relatorio_v1.docx                ← Peça 141
│   ├── relatorio_v1.md
│   └── CODEX_UPGRADED_V1_FINDINGS.md
│
├── 04_PECAS_EVIDENCIA/ (180 arquivos)   ← Peças por achado + texto extraído
│   ├── README.md
│   ├── ACH01_documental/    (7 PDFs)    ← peças 103-109
│   ├── ACH02_geoespacial/   (13 PDFs)   ← peças 110-123
│   ├── ACH03_cadastral/     (11 PDFs)   ← peças 124-131
│   ├── ACH04_metadados/     (4 PDFs)    ← peças 132-136
│   ├── TRANSVERSAIS/        (16 PDFs)   ← peças 75-86, 137-140
│   └── txt_extraido/        (129 .txt)  ← texto de TODOS os PDFs
│
├── 05_PECAS_TRAMITACAO/ (50 arquivos)   ← Ofícios, atas, contraditório
│   └── README.md
│
├── 06_NORMAS_CRITERIOS/ (15 arquivos)   ← Leis, ISOs, DAMA-DMBOK, NAT
│   └── README.md
│
├── 07_MODELOS_TCU/      (3 arquivos)    ← Templates e exemplos
│   └── README.md
│
└── _artefatos_latex/    (14 arquivos)   ← Isolados (não indexar)
```

---

## PASSO 1 — Indexação

### 1a. Instalar dependências

```bash
pip install google-genai faiss-cpu numpy tqdm pypdf chromadb elasticsearch sentence-transformers --break-system-packages
```

### 1b. Indexar com Gemini Embedding 2

O projeto já tem um script `index_gemini.py` pronto. Se estiver disponível no workspace, use-o. Se não, criar um novo:

```bash
# Verificar se index_gemini.py existe
ls index_gemini.py 2>/dev/null

# Se existir, reindexar
python3 index_gemini.py --index-all

# Se não existir, indexar manualmente:
# Para cada pasta (exceto _artefatos_latex), extrair texto e criar embeddings
```

**O que indexar (prioridade):**

| Prioridade | Pasta | Por quê |
|---|---|---|
| 1 | `02_FONTE_VERDADE/` | Matriz = fonte de verdade para números |
| 2 | `01_RELATORIO_V2/` | O que está sendo revisado |
| 3 | `04_PECAS_EVIDENCIA/txt_extraido/` | Evidências que sustentam os achados |
| 4 | `03_RELATORIO_V1/` | Contexto e narrativa original |
| 5 | `06_NORMAS_CRITERIOS/` | Critérios de auditoria |
| 6 | `05_PECAS_TRAMITACAO/` | Ofícios e contraditório |
| ❌ | `_artefatos_latex/` | NÃO indexar — lixo |

### 1c. Alternativa simples (sem infraestrutura pesada)

Se não conseguir montar Elasticsearch + ChromaDB + Gemini, usar busca por grep + leitura direta:

```bash
# Buscar um número na Matriz
grep -n "27,1%" 02_FONTE_VERDADE/MATRIZ_DE_ACHADOS_CAF.md

# Buscar em todas as peças extraídas
grep -rn "3.097" 04_PECAS_EVIDENCIA/txt_extraido/

# Buscar em todo o projeto
grep -rn "Acórdão 1197" --include="*.md" --include="*.txt" .
```

---

## PASSO 2 — Ler os documentos na ordem correta

```bash
# 1. MANIFEST (contexto e instruções)
cat MANIFEST.md

# 2. Fonte de verdade (hierarquia máxima)
cat 02_FONTE_VERDADE/MATRIZ_DE_ACHADOS_CAF.md
cat 02_FONTE_VERDADE/ANEXO_COMENTARIOS_GESTOR.md

# 3. Relatório V2 (o que revisar) — na ordem do relatório
cat 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md
cat 01_RELATORIO_V2/INTRODUCAO_V2.md
cat 01_RELATORIO_V2/VISAO_GERAL_V2.md
cat 01_RELATORIO_V2/ACH01_V2.md
cat 01_RELATORIO_V2/ACH02_V2.md
cat 01_RELATORIO_V2/ACH03_V2.md
cat 01_RELATORIO_V2/ACH04_V2.md

# 4. Modelos TCU (padrão a seguir)
cat 07_MODELOS_TCU/README.md
# Ler os templates para comparar estrutura

# 5. NAT e normas (critérios)
cat 06_NORMAS_CRITERIOS/README.md
cat 06_NORMAS_CRITERIOS/normas_auditoria_nat_tcu.md
cat 06_NORMAS_CRITERIOS/NAT_QUICK_REFERENCE.md
```

---

## PASSO 3 — Executar os 8 passes de revisão

### PASSE 1 — Integridade numérica (CRITICAL)

Todo número no V2 deve conferir EXATAMENTE com a Matriz (`02_FONTE_VERDADE/MATRIZ_DE_ACHADOS_CAF.md`).

```bash
# Para cada número-chave, verificar em TODOS os arquivos que o citam:
grep -rn "27,1%" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
grep -rn "53,55%" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
grep -rn "45,92%" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
grep -rn "3\.097" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
grep -rn "90,62%" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
grep -rn "94,1%" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
grep -rn "55,27%" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
grep -rn "632" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
grep -rn "59,6" 01_RELATORIO_V2/ 02_FONTE_VERDADE/
```

**Tabela de verificação (preencher):**

| Dado | Valor Matriz | Resumo | Introdução | Visão Geral | ACH-01 | ACH-02 | ACH-03 | ACH-04 | OK? |
|---|---|---|---|---|---|---|---|---|---|
| Inadequação semântica | 27,1% | | | | | | | | |
| Divergência área | 53,55% | | | | | | | | |
| Tipo documental | 33,33% | | | | | | | | |
| Resolução <300 DPI | 68,7% | | | | | | | | |
| Erro cartográfico | 45,92% | | | | | | | | |
| Duplicações espaciais | 55,27% | | | | | | | | |
| Inconsist. municipal | 15,92% | | | | | | | | |
| Municípios inflação | 632 | | | | | | | | |
| Falecidos ativos | 3.097 | | | | | | | | |
| Menores titulares | 138 | | | | | | | | |
| E-mails fictícios PF | 90,62% | | | | | | | | |
| CEPs genéricos | 93,7% | | | | | | | | |
| Renda > R$1M | 907 | | | | | | | | |
| PJs CNAE | 39 | | | | | | | | |
| Descrições dicionário | 94,1% | | | | | | | | |
| Campos s/ unidade | 84% | | | | | | | | |
| Campos temporais | 92% | | | | | | | | |
| Pronaf safra | R$59,6 bi | | | | | | | | |
| Leaflet redução | 92,36%→16,59% | | | | | | | | |
| Amostra ACH-01 | 646 docs | | | | | | | | |
| Conformidade gestor | 32% | | | | | | | | |
| Renovação prevista | ~742 mil | | | | | | | | |

### PASSE 2 — Coerência de citações e notas de fim

```bash
# Listar todas as notas de fim em cada arquivo
for f in 01_RELATORIO_V2/*.md; do
    echo "=== $f ==="
    grep -n '¹\|²\|³\|⁴\|⁵\|⁶\|⁷\|⁸\|⁹\|⁰\|Notas de Fim' "$f"
done

# Verificar sequência: Introdução ¹-¹⁰, Visão Geral ¹¹-²⁰, ACH-01 ²¹+, etc.
# Verificar que cada chamada no texto tem referência correspondente no bloco de Notas
```

**Verificar:**
1. Numeração sequencial sem saltos ou duplicações
2. Cada chamada ¹²³ tem referência ABNT no bloco de Notas de Fim
3. Formato ABNT correto (autor, título, local, editora, data, URL)
4. Acórdãos do TCU NÃO estão como notas (são referências processuais internas)
5. Referências a peças (ex: "peça 103, p. 9") são consistentes entre seções

### PASSE 3 — Harmonia narrativa

Ler os 7 arquivos **sequencialmente** e verificar:

1. **Fluxo:** Resumo → Introdução → Visão Geral → ACH-01 → ACH-02 → ACH-03 → ACH-04. Cada seção prepara a seguinte?
2. **Não repetição:** Visão Geral não repete Introdução? Achados não repetem Visão Geral?
3. **Progressão:** Síntese → Técnica → Contexto/storytelling → Detalhe com evidências?
4. **Tom consistente:** Operacional/propositivo em TODAS as seções?
5. **Numeração §§:** §1-5 (Resumo), §1-7 (Introdução), §8-12 (VG), §13-23 (ACH-01), §24-34 (ACH-02), §35-48 (ACH-03), §49+ (ACH-04). Sem saltos?
6. **Tabelas/Quadros:** Numeração sequencial no relatório inteiro?
7. **Transições:** Final de cada seção → início da próxima?

### PASSE 4 — Componentes obrigatórios NAT §138

```bash
# Ler as NAT para referência
cat 06_NORMAS_CRITERIOS/normas_auditoria_nat_tcu.md | grep -A20 '138\|componentes do achado'
cat 06_NORMAS_CRITERIOS/nat_checklist.md
```

Para CADA achado (ACH-01, 02, 03, 04):

| Componente | ACH-01 | ACH-02 | ACH-03 | ACH-04 |
|---|---|---|---|---|
| Parágrafo-síntese (dedutivo) | | | | |
| Situação encontrada | | | | |
| Critério de auditoria | | | | |
| Evidências (peças) | | | | |
| Causas | | | | |
| Efeitos (POTENCIAIS?) | | | | |
| Boas práticas | | | | |
| Proposta de encaminhamento | | | | |
| Benefícios esperados | | | | |
| Quadro-resumo visual | | | | |

**CRITICAL:** Se qualquer efeito for apresentado como REAL/CONSUMADO (não potencial) → bug CRITICAL.

### PASSE 5 — Consistência com Matriz de Achados

```bash
# Confrontar formulações
cat 02_FONTE_VERDADE/MATRIZ_DE_ACHADOS_CAF.md
```

Verificar:
1. Títulos dos achados idênticos à Matriz?
2. Causas C1-C6 todas representadas na narrativa?
3. Efeitos EP1-EP4 todos representados?
4. Propostas = texto da Matriz (não inventado)?
5. Proposta 1 (plano de ação 180 dias) em TODOS os 4 achados?
6. Proposta 2.1.3 (interoperabilidade) presente onde a Matriz indica?

### PASSE 6 — Tom e equilíbrio

Para CADA seção:
1. Linguagem de fraude, irregularidade, punição? → **CRITICAL**
2. Reconhece avanços do gestor? (CAF 3.0, Leaflet, TED DCAF/UFES, 742 mil)
3. Efeitos com caveats? ("não significa automaticamente...")
4. Liberdade de meios? ("resultados a alcançar, não prescrição")
5. **ACH-03:** Falecidos/menores = curadoria, NÃO fraude? Exclusão digital reconhecida?
6. **ACH-04:** Metadados acessíveis para não-técnico? Analogia presente?

### PASSE 7 — Elementos visuais

Inventariar:

| Seção | Tabelas | Quadros | Figuras | Têm fonte? | Numeração OK? |
|---|---|---|---|---|---|
| Resumo | | | | | |
| Introdução | | | | | |
| Visão Geral | | | | | |
| ACH-01 | | | | | |
| ACH-02 | | | | | |
| ACH-03 | | | | | |
| ACH-04 | | | | | |

Mínimo por achado: 1 tabela de dados + 1 quadro-resumo.

### PASSE 8 — Conformidade com modelos TCU

```bash
# Ler os modelos
cat 07_MODELOS_TCU/README.md
# Comparar estrutura do V2 com o template
```

Verificar:
1. Estrutura: Resumo → Introdução → Visão Geral → Achados → Conclusão → Propostas?
2. Introdução: não abre com acórdão? Tem 7 componentes?
3. Visão Geral: storytelling? ~2 páginas?
4. Achados: método dedutivo? Parágrafo-síntese primeiro?
5. Anexos/Apêndices: A (CG), B (Matriz), C (Planejamento) + I-VI (Apêndices)?

---

## PASSO 4 — Revisão adversária massiva (3 etapas)

### ⚠️ TIMEOUT CRÍTICO — ESTE PROCESSO VAI RODAR A NOITE TODA

As 3 etapas abaixo fazem dezenas de chamadas LLM sequenciais. **O tempo total pode ser de 2-4 horas.** NÃO cancelar por timeout. Configurar o ambiente para aceitar execução longa.

**Se alguma etapa falhar por timeout:** registrar o transcript parcial (que já terá as palavras de cada agente até o ponto da falha) e prosseguir para a próxima etapa. O transcript parcial já é valioso.

**CRÍTICO:** Todos os painéis usam `include_transcript: true`. Isso garante que as palavras de CADA agente individual ficam registradas no output, mesmo que o painel não complete. Se der timeout após 2 de 3 rodadas, você ainda tem 2 rodadas de análise completa.

---

### Etapa 1 — dev-converge: run_panel (3 agentes × 3 rodadas = refinamento iterativo)

**Objetivo:** Cada agente revisa, vê a crítica dos outros, e refina. 3 rodadas de melhoria progressiva.

**Foco:** Integridade numérica + consistência com Matriz + componentes NAT §138.

Antes de chamar, **concatenar os 7 arquivos do V2 em um texto único** para enviar como contexto:

```bash
cat 01_RELATORIO_V2/RESUMO_EXECUTIVO_V2.md > /tmp/v2_completo.txt
echo -e "\n\n---\n\n" >> /tmp/v2_completo.txt
cat 01_RELATORIO_V2/INTRODUCAO_V2.md >> /tmp/v2_completo.txt
echo -e "\n\n---\n\n" >> /tmp/v2_completo.txt
cat 01_RELATORIO_V2/VISAO_GERAL_V2.md >> /tmp/v2_completo.txt
echo -e "\n\n---\n\n" >> /tmp/v2_completo.txt
cat 01_RELATORIO_V2/ACH01_V2.md >> /tmp/v2_completo.txt
echo -e "\n\n---\n\n" >> /tmp/v2_completo.txt
cat 01_RELATORIO_V2/ACH02_V2.md >> /tmp/v2_completo.txt
echo -e "\n\n---\n\n" >> /tmp/v2_completo.txt
cat 01_RELATORIO_V2/ACH03_V2.md >> /tmp/v2_completo.txt
echo -e "\n\n---\n\n" >> /tmp/v2_completo.txt
cat 01_RELATORIO_V2/ACH04_V2.md >> /tmp/v2_completo.txt
```

Depois chamar:

```
dev-converge: run_panel

task: "REVISÃO INTEGRAL do Relatório V2 de auditoria do TCU (TC 011.073/2025-0).

Você recebeu o texto COMPLETO do relatório (7 seções: Resumo, Introdução, Visão Geral, ACH-01 a ACH-04).

VERIFICAR SISTEMATICAMENTE:

A) INTEGRIDADE NUMÉRICA — Para cada número abaixo, verificar se aparece CORRETO em todas as seções que o citam. Qualquer divergência = CRITICAL.
- 27,1% (docs inadequados), 53,55% (área), 33,33% (tipo), 68,7% (DPI)
- 45,92% (erro cartográfico), 55,27% (duplicações), 15,92% (municipal), 632 (municípios)
- 3.097 (falecidos), 138 (menores), 90,62% (e-mails), 93,7% (CEPs), 907 (renda), 39 (PJs)
- 94,1% (metadados), 84% (numéricos), 92% (temporais)
- R$ 59,6 bi (Pronaf), 92,36%→16,59% (Leaflet), 646 (amostra), 32% (conformidade), ~742 mil (renovação)

B) COMPONENTES NAT §138 — Cada achado tem: parágrafo-síntese, SE, critério, evidências, causas, efeitos POTENCIAIS, boas práticas, proposta, benefícios, quadro-resumo?

C) TOM — Auditoria operacional: ZERO linguagem de fraude, punição ou responsabilização. Efeitos TODOS potenciais. Avanços do gestor reconhecidos.

D) HARMONIA — Os 7 textos formam conjunto coerente? Não repetição? Fluxo lógico? Numeração §§ e tabelas sequencial?

E) CITAÇÕES — Notas de fim sequenciais? Formato ABNT? Chamada↔referência?

Para cada bug: classificar CRITICAL / HIGH / LOW com § e seção."

context: "[COLAR CONTEÚDO DE /tmp/v2_completo.txt AQUI]

DADOS DA MATRIZ DE ACHADOS PARA CONFRONTO:
[COLAR OS PRINCIPAIS NÚMEROS E FORMULAÇÕES DA MATRIZ AQUI - extrair de 02_FONTE_VERDADE/MATRIZ_DE_ACHADOS_CAF.md]"

agent_names: ["kimi", "qwen", "zai"]
rounds: 3
temperature: 0.3
max_tokens: 8000
include_transcript: true
```

**Salvar o output COMPLETO** (incluindo transcript de cada agente) em:
```
01_RELATORIO_V2/REVISAO_RUN_PANEL.md
```

---

### Etapa 2 — dev-converge: swarm_panel (N personas especializadas → convergência)

**Objetivo:** Cada persona foca num aspecto diferente. Cobertura ampla.

**Foco:** Tom, acessibilidade, storytelling, consistência com contraditório.

```
dev-converge: swarm_panel

task: "REVISÃO ESPECIALIZADA do Relatório V2 de auditoria do TCU (TC 011.073/2025-0).

Cada persona avalia o relatório completo sob sua perspectiva especializada.

PERSONA 1 — AUDITOR SÊNIOR TCU (20 anos de experiência):
- Os achados atendem NAT §138 (todos os componentes)?
- O método dedutivo está correto (parágrafo-síntese primeiro)?
- As propostas são proporcionais e factíveis?
- A liberdade de meios está preservada?
- Os processos conexos e a reincidência (Ac. 1197/2018) estão bem documentados?

PERSONA 2 — ASSESSOR DE MINISTRO RELATOR:
- O Ministro entende o relatório em 30 minutos de leitura?
- O Resumo funciona em 2 minutos?
- A Visão Geral dá contexto suficiente sem ser prolixa?
- Os benefícios são convincentes para fundamentar o voto?
- Algum trecho geraria constrangimento em Plenário?

PERSONA 3 — PROCURADOR DO MP JUNTO AO TCU:
- As evidências são suficientes para sustentar os achados?
- Os efeitos estão corretamente classificados como potenciais?
- Há base legal adequada para as determinações e recomendações?
- O contraditório foi adequadamente analisado?
- A reincidência (Ac. 1197/2018) justifica a determinação?

PERSONA 4 — GESTOR DO MDA (lendo o relatório para se defender):
- Algum trecho é injusto ou desproporcional?
- Os avanços do CAF 3.0 e do Leaflet foram adequadamente reconhecidos?
- A exclusão digital do público rural foi considerada no ACH-03?
- O tom é propositivo ou acusatório?
- A liberdade de meios está real ou é retórica?
- O prazo de 180 dias é razoável?

PERSONA 5 — ESPECIALISTA EM QUALIDADE DE DADOS (DAMA-DMBOK):
- Os critérios técnicos (ISO 25012, ISO 19157, ISO 11179, DAMA-DMBOK) são aplicados corretamente?
- O ACH-04 (metadados) é acessível para não-técnico?
- As métricas são válidas e as amostras representativas?
- Os números são estatisticamente corretos?
- A analogia de metadados funciona?

Para cada bug encontrado, cada persona deve:
1. Identificar a seção e §
2. Citar o trecho problemático
3. Classificar: CRITICAL / HIGH / LOW
4. Sugerir correção
5. Assinar com nome da persona"

context: "[COLAR CONTEÚDO DE /tmp/v2_completo.txt AQUI]"

agent_names: ["kimi", "qwen", "zai"]
temperature: 0.3
max_tokens: 8000
include_transcript: true
```

**Salvar o output COMPLETO** (incluindo o que CADA persona de CADA agente disse) em:
```
01_RELATORIO_V2/REVISAO_SWARM_PANEL.md
```

---

### Etapa 3 — minimax-chat: avaliação final independente com MiniMax 2.7

**Objetivo:** Perspectiva completamente independente — modelo diferente, treinamento diferente, vieses diferentes.

```
minimax-chat: chat

message: "Você é o revisor final de um relatório de auditoria que será votado em Plenário pelo Tribunal de Contas da União. O relatório já passou por 2 rodadas de revisão adversária com 3 agentes cada. Sua função é a última linha de defesa antes da entrega.

O RELATÓRIO COMPLETO (7 seções) SEGUE ABAIXO.

SUAS TAREFAS:

1. LEITURA INTEGRAL — Leia o relatório do início ao fim, como faria um assessor de Ministro recebendo o documento pela primeira vez.

2. PRIMEIRA IMPRESSÃO — Em 3 frases, qual sua impressão geral? O relatório convence? Está bem escrito? O Ministro ficaria confortável em votar?

3. BUGS REMANESCENTES — Após as 2 rodadas adversárias anteriores, o que AINDA está errado? Liste APENAS bugs que não foram pegos. Para cada um: seção, §, descrição, severidade, correção.

4. CONSISTÊNCIA INTERNA — Leia o Resumo e depois os achados. Os números batem? O tom é o mesmo? As propostas do Resumo conferem com as dos achados?

5. TESTE DO 'E DAÍ?' — Para cada achado, pergunte: 'E daí? Por que isso importa para a sociedade?' Se a resposta não estiver clara no texto, é bug HIGH.

6. TESTE DO GESTOR — Se você fosse o gestor do MDA, acharia o relatório justo? Equilibrado? Sentiria que seus argumentos foram ouvidos? Se não, onde está o problema?

7. TESTE DA IMPRENSA — Se a Folha de São Paulo recebesse este relatório, qual seria a manchete? O relatório sustenta essa manchete com dados? A manchete seria justa?

8. NOTAS DE FIM — As referências ABNT estão completas? Falta alguma? Alguma está errada?

9. VEREDICTO FINAL — APROVADO / AJUSTES / REPROVADO. Com fundamentação.

TEXTO COMPLETO DO RELATÓRIO:

[COLAR CONTEÚDO DE /tmp/v2_completo.txt AQUI]"

system: "Você é o revisor mais experiente do TCU — 25 anos de auditoria, 10 como assessor de Ministro, 5 como Secretário de Controle Externo. Você já viu centenas de relatórios. Seu padrão é alto. Você não tem medo de dizer quando algo está errado, mas também reconhece quando está bom. Responda em português formal, com a profundidade de quem vai assinar embaixo do parecer. Não economize palavras — este é o parecer final."
temperature: 0.3
max_tokens: 8000
```

**Salvar o output COMPLETO** em:
```
01_RELATORIO_V2/REVISAO_MINIMAX_FINAL.md
```

---

### Consolidação dos 3 painéis

Após as 3 etapas, produzir tabela consolidada:

```markdown
## Consolidação dos painéis adversários

| Fonte | Tempo | Bugs encontrados | CRITICAL | HIGH | LOW |
|---|---|---|---|---|---|
| run_panel (kimi/qwen/zai × 3 rodadas) | ~Xmin | X | X | X | X |
| swarm_panel (5 personas × 3 agentes) | ~Xmin | X | X | X | X |
| minimax-chat 2.7 (independente) | ~Xmin | X | X | X | X |
| **TOTAL (deduplicado)** | | **X** | **X** | **X** | **X** |

### Bugs únicos por fonte
| Bug | Encontrado por | Confirmado por | Ação |
|---|---|---|---|
| ... | run_panel (kimi, r2) | swarm (persona 3) | Corrigir |
| ... | swarm (persona 4) | minimax | Corrigir |
| ... | run_panel (zai, r1) | — | Falso positivo? |
```

Se um bug foi encontrado por **2+ fontes independentes**, é quase certamente real.
Se foi encontrado por **apenas 1 fonte**, avaliar se é falso positivo antes de corrigir.

Incluir esta consolidação no `REVISAO_INTEGRAL_V2.md` final.

---

## PASSO 5 — Produzir relatório de revisão final

Combinar os resultados dos 8 passes manuais + 3 painéis adversários em um único relatório:

```
01_RELATORIO_V2/REVISAO_INTEGRAL_V2.md
```

Estrutura:

```markdown
# Relatório de Revisão Integral — V2 (TC 011.073/2025-0)

**Revisor:** [agente LLM]
**Data:** [data]
**Escopo:** 7 seções do Relatório V2
**Painéis adversários:** run_panel (3×3) + swarm_panel (5 personas) + minimax 2.7

## Resumo
- Total de bugs: X (CRITICAL: X, HIGH: X, LOW: X)
- Bugs confirmados por 2+ fontes: X
- Veredicto: APROVADO / AJUSTES / REPROVADO

## Passe 1 — Integridade numérica
[tabela 22 dados × 7 seções]

## Passe 2 — Citações e notas de fim
[lista de inconsistências]

## Passe 3 — Harmonia narrativa
[análise de fluxo]

## Passe 4 — Componentes NAT §138
[matriz 4 achados × 10 componentes]

## Passe 5 — Consistência com Matriz
[divergências]

## Passe 6 — Tom e equilíbrio
[mapa por seção]

## Passe 7 — Elementos visuais
[inventário]

## Passe 8 — Conformidade modelos TCU
[checklist]

## Painel adversário 1 — run_panel (kimi/qwen/zai × 3 rodadas)
[síntese + bugs encontrados]

## Painel adversário 2 — swarm_panel (5 personas × 3 agentes)
[síntese por persona + bugs encontrados]

## Painel adversário 3 — minimax 2.7 (independente)
[parecer completo + bugs encontrados]

## Consolidação dos painéis
[tabela de deduplicação: bug × fonte × confirmação]

## Bugs a corrigir (priorizados — deduplicados)
| # | Severidade | Seção | § | Bug | Encontrado por | Confirmado por | Correção sugerida |
```

**Adicionalmente, salvar os transcripts brutos:**
- `01_RELATORIO_V2/REVISAO_RUN_PANEL.md` — transcript completo do run_panel
- `01_RELATORIO_V2/REVISAO_SWARM_PANEL.md` — transcript completo do swarm_panel (com cada persona de cada agente)
- `01_RELATORIO_V2/REVISAO_MINIMAX_FINAL.md` — parecer completo do MiniMax 2.7

---

## REGRAS INVIOLÁVEIS

1. **NÃO corrija os arquivos** — apenas identifique problemas. A equipe corrige.
2. **Matriz = fonte de verdade** — se o texto diverge da Matriz, o texto está errado.
3. **Auditoria operacional** — qualquer linguagem de fraude/punição/responsabilização = CRITICAL.
4. **Efeitos = potenciais** — se algum for apresentado como real = CRITICAL.
5. **O relatório será votado em Plenário** — padrão de qualidade de apresentação a Ministros do TCU.
6. **Hierarquia:** Matriz > Anexo CG > V1. Se houver conflito, Matriz prevalece.
7. **TIMEOUT: 4 HORAS** — este processo foi desenhado para rodar a noite toda. NÃO cancelar nenhuma etapa antes de 4 horas de execução total. Se uma etapa individual travar por mais de 60 minutos, registrar o transcript parcial e prosseguir para a próxima.
8. **TRANSCRIPTS:** Todos os painéis usam `include_transcript: true`. Salvar SEMPRE o output completo, mesmo que parcial. As palavras de cada agente individual são valiosas mesmo sem a síntese final.
9. **4 arquivos de output obrigatórios:** `REVISAO_INTEGRAL_V2.md` (consolidado), `REVISAO_RUN_PANEL.md` (transcript run), `REVISAO_SWARM_PANEL.md` (transcript swarm), `REVISAO_MINIMAX_FINAL.md` (parecer MiniMax).