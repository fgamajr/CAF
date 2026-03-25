# CLAUDE.md — Projeto CAF-FINAL

## O que é este projeto

Relatório de auditoria operacional do TCU (TC 011.073/2025-0) sobre qualidade de dados do Cadastro Nacional da Agricultura Familiar (CAF 3.0). Prazo: 31/3/2026. Equipe: Fernando (coordenador), Sylvio Xavier, Kalenus Pires, Harley Alves Ferreira (supervisor). Relator: Min. Antonio Anastasia.

## Estrutura da pasta

```
CAF-FINAL/
├── MANIFEST.md                    ← LER PRIMEIRO (contexto + hierarquia + dados-chave)
├── 00_CONTEXTO/                   ← Resumo + Visão Geral (contexto rápido)
├── 01_RELATORIO_V2/               ← 7 seções sendo revisadas
├── 02_FONTE_VERDADE/              ← 🏛️ Matriz de Achados + 📜 Anexo CG
├── 03_RELATORIO_V1/               ← Peça 141 (referência histórica)
├── 04_PECAS_EVIDENCIA/            ← PDFs por achado + txt_extraido/
├── 05_PECAS_TRAMITACAO/           ← Ofícios, atas, contraditório
├── 06_NORMAS_CRITERIOS/           ← Leis, ISOs, NAT, DAMA-DMBOK
├── 07_MODELOS_TCU/                ← Templates de relatório
└── _artefatos_latex/              ← Não indexar
```

## Hierarquia de documentos (INVIOLÁVEL)

| Nível | Documento | Regra |
|---|---|---|
| 🏛️ Constituição | `02_FONTE_VERDADE/PECA170_MATRIZ_DE_ACHADOS_CAF.md` | Números e formulações definitivos. SEMPRE prevalece. |
| 📜 Lei complementar | `02_FONTE_VERDADE/PECA169_codex_anexo_comentarios_gestor_v2.md` | Tom, âncoras, concessões ao gestor |
| 📖 Referência | `03_RELATORIO_V1/relatorio_v1.docx` | Narrativa original. Dados definitivos vêm da Matriz. |

## Regras do relatório

- **Auditoria operacional** — tom propositivo, SEM responsabilização, SEM multa, SEM fraude
- **Efeitos = TODOS potenciais** — nunca "dano consumado ao erário"
- **Método dedutivo** (Bertuol) — parágrafo-síntese primeiro, depois storytelling
- **Liberdade de meios** — propostas definem resultados, não soluções
- **Avanços do gestor reconhecidos** — CAF 3.0, Leaflet, TED DCAF/UFES

## Dados-chave (22 números — Matriz é fonte de verdade)

| Dado | Valor | Achado |
|---|---|---|
| Docs semanticamente inadequados | 27,1% (~3,08M) | ACH-01 |
| Divergência crítica de área | 53,55% (~1,44M) | ACH-01 |
| Tipo documental inadequado | 33,33% | ACH-01 |
| Resolução <300 DPI | 68,7% | ACH-01 |
| Erro cartográfico | 45,92% (~1,46M imóveis) | ACH-02 |
| Duplicações espaciais | 55,27% | ACH-02 |
| Inconsistência municipal | 15,92% | ACH-02 |
| Municípios inflação cadastral | 632 | ACH-02 |
| Falecidos ativos | 3.097 | ACH-03 |
| Menores como titulares | 138 (89+49) | ACH-03 |
| E-mails fictícios PF | 90,62% | ACH-03 |
| CEPs genéricos | 93,7% | ACH-03 |
| Renda > R$1M | 907 | ACH-03 |
| PJs CNAE incompatível | 39 | ACH-03 |
| Descrições dicionário inadequadas | 94,1% (496/527) | ACH-04 |
| Campos numéricos sem unidade | 84% | ACH-04 |
| Campos temporais ambíguos | 92% | ACH-04 |
| Pronaf safra 2023/2024 | R$ 59,6 bi | Contexto |
| Leaflet redução duplicações | 92,36%→16,59% | ACH-02 |
| Amostra ACH-01 | 646 docs | ACH-01 |
| Conformidade integral (gestor) | 32% | ACH-01 |
| Renovação prevista | ~742 mil registros | ACH-01 |

## Ferramentas disponíveis

### Indexador local (Elasticsearch + ChromaDB + Gemini)
```bash
source .venv/bin/activate
python3 search_review.py "query" --k 5
python3 search_review.py "query" --hierarchy constituicao  # só Matriz
python3 search_review.py "query" --hierarchy relatorio_v2  # só V2
python3 search_review.py "query" --hierarchy pecas          # só peças
```

### MCP Servers
- **dev-converge** — painéis adversários (run_panel, swarm_panel, jury_panel)
  - Agentes: kimi, qwen, zai (via DashScope)
  - SEMPRE usar `include_transcript: true`
  - Timeout do MCP client = 120s. Para painéis longos, reduzir contexto ou rodadas.
- **minimax-chat** — avaliação independente com MiniMax 2.7
- **gabi-dou** — busca no DOU + jurisprudência TCU (acórdãos, normas)

### Busca nas peças
```bash
grep -rn "27,1%" 04_PECAS_EVIDENCIA/txt_extraido/
grep -rn "peça 150" 01_RELATORIO_V2/
```

## Bugs conhecidos (pendentes de correção)

1. **Introdução §7** — diz "seis capítulos" mas enumera sete
2. **ACH-01 §21/§23** — dado de 32% sem cautela "dado do gestor, não auditado pela equipe"
3. **ACH-04** — abre no §49 sem título de capítulo (assimetria com ACH-01/02/03)
4. **Resumo §2** — sub-representa ACH-03 e ACH-04 (faltam 93,7% CEPs, 39 PJs, 92% temporais)
5. **ACH-04** — chamada de notas `²⁵²⁶²⁷` colada (sem espaço)
6. **Introdução** — sem bloco local de Notas de Fim (notas ¹–¹⁰ sem referências no arquivo)

## Estado atual

- ✅ Resumo Executivo, Introdução, Visão Geral, ACH-01, ACH-02, ACH-03 — aprovados
- ✅ ACH-04 — redigido pelo Codex (verificar)
- ✅ Indexação — 71/77 testes, Bateria 2: 22/22, MiniMax GO COM RESSALVAS
- ⬜ Revisão adversária dos 7 arquivos do V2 (run_panel + swarm + minimax)
- ⬜ Conclusão (~1 página)
- ⬜ Propostas de Encaminhamento (~2-3 páginas)
- ⬜ Apêndices I-VI
- ⬜ Montagem .docx final

## Prompt de revisão

O arquivo `PROMPT_REVISAO_INTEGRAL_V2.md` contém o roteiro completo de revisão (8 passes manuais + 3 painéis adversários). Ler antes de começar qualquer revisão.

## Convenções

- Parágrafos numerados sequencialmente: §1-7 (Intro), §8-12 (VG), §13-23 (ACH-01), §24-34 (ACH-02), §35-48 (ACH-03), §49+ (ACH-04)
- Tabelas/Quadros numerados sequencialmente no relatório inteiro
- Notas de fim: ¹-¹⁰ (Intro), ¹¹-²⁰ (VG), ²¹-²² (ACH-01), ²³ (ACH-02), ²⁴ (ACH-03), ²⁵+ (ACH-04)
- Referências ABNT para fontes bibliográficas; acórdãos do TCU citados inline