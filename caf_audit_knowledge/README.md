# CAF Audit Knowledge

Production-oriented hybrid search + answer system for the real `CAF-FINAL` audit repository.

This project is not a generic RAG scaffold. It is a repository-aware system that:

- indexes only the semantically allowed source directories
- preserves audit provenance at document, chunk, and page level
- deduplicates overlapping representations of the same content
- links content through `ACH01` to `ACH04`
- combines lexical search, vector search, reranking, calibrated scoring, adaptive scoring, and answer generation
- exposes explainable traces, query feedback, scoring feedback, and operational ledgers

Everything below is based on the actual implementation in this codebase.

## 1. Overview

### What the system does

`caf_audit_knowledge` ingests the `CAF-FINAL` repository, extracts text from supported files, creates deterministic chunks, stores canonical documents and chunk metadata in SQLAlchemy models, pushes BM25-searchable content to Elasticsearch, stores embeddings in PostgreSQL + pgvector, and serves hybrid search and answer generation through both CLI and GraphQL.

Core implementation entry points:

- `src/caf_audit_knowledge/ingest/pipeline.py`
- `src/caf_audit_knowledge/retrieval/service.py`
- `src/caf_audit_knowledge/answering/service.py`
- `src/caf_audit_knowledge/cli.py`
- `src/caf_audit_knowledge/graph/schema.py`

### Implemented capabilities

- Hybrid retrieval: BM25 in Elasticsearch plus vector similarity from pgvector
- Cross-encoder reranking with `BAAI/bge-reranker-large`
- Rule-based query classification with optional LLM fallback
- Adaptive query-pattern learning from classification feedback
- Adaptive scoring profiles per query type
- Hard content filtering for debug, review-artifact, and stack-trace noise
- Risk detection and safe-mode behavior
- Explainable traces for retrieval, rerank, scoring, and final ranking
- Page-aware provenance in chunks and answers
- File watching for incremental reindex on source changes

### How to reason about the system

The implementation is easiest to operate if you separate it into three layers:

1. Retrieval: get enough good candidates from BM25 and vectors.
2. Ranking: reorder those candidates with the reranker and calibrated score weights.
3. Answering: classify the query, choose the right prompt, and produce an answer with provenance.

That separation helps during debugging. If a relevant chunk exists but ranks too low, inspect retrieval and scoring. If the right chunks rank well but the answer is incomplete, inspect prompt routing and answer generation.

## 2. Architecture

### End-to-end pipeline

1. Repository discovery
2. Source-type classification and ignore filtering
3. Text extraction and page mapping
4. Canonical deduplication
5. Deterministic chunking
6. Relationship extraction
7. SQL persistence
8. Elasticsearch indexing
9. Embedding task queueing
10. Embedding worker writes vectors to pgvector
11. Query classification and risk analysis
12. Hybrid retrieval
13. Reranking
14. Dynamic scoring
15. Prompt selection
16. Answer generation

### ASCII flow

```text
CAF-FINAL repository
    |
    v
discover_paths() + should_ignore_path()
    |
    v
classify_source() + extract_document()
    |
    v
doc_id / content_hash / ACH extraction / page_map
    |
    v
_deduplicate() -> canonical docs + duplicate ledger
    |
    v
build_chunks() -> chunk ids + manifest hashes + feature hashes
    |
    +--> build_relations()
    |
    v
SQL tables: documents / chunks / relations / embedding_tasks / pruning_ledger
    |
    +--> Elasticsearch: caf_documents / caf_chunks
    |
    +--> EmbeddingTaskRecord queue
              |
              v
        EmbeddingWorker -> pgvector embeddings on chunks

Query
    |
    v
classify_query() + assess_query_risk()
    |
    v
BM25 candidates + vector candidates
    |
    v
cross-encoder rerank
    |
    v
adaptive scoring profile + policy boosts/penalties
    |
    +--> hard filters for debug / review-artifact / stack-trace noise
    |
    +--> explain trace / logs
    |
    v
prompt selection
    |
    v
LLM answer with inline chunk citations
```

## 3. Indexing

### 3.1 Initial indexing

The initial indexing flow is implemented in `src/caf_audit_knowledge/ingest/pipeline.py`.

What happens during `caf-audit build --full`:

1. Recreate SQL tables and Elasticsearch indices.
2. Walk only the allowed directories:
   - `00_CONTEXTO`
   - `01_RELATORIO_V2`
   - `02_FONTE_VERDADE`
   - `03_RELATORIO_V1`
   - `04_PECAS_EVIDENCIA`
   - `05_PECAS_TRAMITACAO`
   - `06_NORMAS_CRITERIOS`
   - `07_MODELOS_TCU`
3. Ignore forbidden or low-value paths via `should_ignore_path()` in `src/caf_audit_knowledge/repo_semantics.py`:
   - `99_DISCARDED`
   - `01_RELATORIO_V2 copy`
   - `.bak`
   - `.venv`
   - `__pycache__`
4. Extract text and page spans.
5. Compute:
   - `doc_id = sha256(raw bytes)`
   - `content_hash = sha256(extracted text)`
6. Extract semantic metadata:
   - `source_type`
   - `authority_weight`
   - `audit_object_id`
   - `piece_number`
7. Deduplicate by `content_hash`, preferring canonical formats:
   - `.md`
   - `.txt`
   - `.pdf`
   - `.docx`
   - `.doc`
8. Build deterministic chunks.
9. Persist documents, chunks, relations, embedding tasks, and pruning ledger rows.
10. Index canonical documents and chunks into Elasticsearch.

### Text extraction

Extraction lives in `src/caf_audit_knowledge/text_extractors.py`.

Implemented extractors:

- `.md` and `.txt`: direct decode, normalize, treat as one logical page
- `.docx`: `python-docx`
- `.doc`: `textutil -convert txt -stdout` fallback
- `.pdf`: `pypdf.PdfReader().pages[].extract_text()`

Important operational note:

- PDF extraction is text-based, not layout-preserving OCR.
- `structured_markdown` is currently a simple page-structured rendering like `## Page N`, not a semantic parser with tables preserved as structured objects.
- Page numbers are preserved through `page_spans`, `page_start`, and `page_end`.

### Metadata stored

Document-level fields are in `src/caf_audit_knowledge/storage/models.py`:

- `id`
- `source_path`
- `source_type`
- `authority_weight`
- `audit_object_id`
- `content_hash`
- `pipeline_fingerprint`
- `title`
- `text`
- `structured_markdown`
- `page_count`
- `page_map`
- `is_duplicate`
- `duplicate_of`

Chunk-level fields:

- `id`
- `document_id`
- `audit_object_id`
- `text`
- `chunk_seq`
- `char_start`
- `char_end`
- `page_start`
- `page_end`
- `section_type`
- `source_type`
- `authority_weight`
- `chunk_manifest_hash`
- `chunk_feature_hash`
- `entity_density`
- `legal_density`
- `importance_score`
- `embedding_status`
- `embedding_version`
- `embedding`

### Section typing

`section_type` is inferred heuristically in `infer_section_type()` from `src/caf_audit_knowledge/repo_semantics.py`.

Implemented values include:

- `debug`
- `toc`
- `sintese`
- `causa`
- `efeito`
- `risco`
- `metodologia`
- `tabela`
- `intro`
- `analysis`
- `body`

`debug` is operationally significant: retrieval now hard-filters obvious review/debug artifacts before they can reach the final ranking.

### 3.2 Embeddings

Embedding providers live in `src/caf_audit_knowledge/embeddings/providers.py`.

Implemented providers:

- OpenAI
- Gemini

Current default settings from `src/caf_audit_knowledge/config.py`:

- provider: `openai`
- model: `text-embedding-3-large`
- version: `v1`
- dimensions: `3072`
- batch size: `16`

Vectors are stored on `chunks.embedding` in PostgreSQL using pgvector when available. The DB bootstrap creates the extension in:

- `config/postgres/init_pgvector.sql`

Important operational note:

- The package declares an optional `chroma` dependency, but the current query path only implements pgvector in `src/caf_audit_knowledge/retrieval/vector_store.py`.
- For real hybrid retrieval, use PostgreSQL + pgvector. SQLite is not sufficient for vector search here.

### 3.3 Running indexing

Use the real commands exposed by the CLI:

```bash
cd /Users/fgamajr/Desktop/CAF-FINAL/caf_audit_knowledge
source .venv/bin/activate

caf-audit init-stores
caf-audit build --full
```

Then start the embedding worker:

```bash
caf-audit embed-worker
```

Useful validation commands after indexing:

```bash
caf-audit validate
caf-audit debug list-docs --limit 20
caf-audit debug stats
caf-audit debug compare-chunks
```

Operational expectations after a healthy rebuild:

- `caf-audit validate` should report `valid: true`
- `caf-audit debug compare-chunks` should stay identical across repeated full builds
- `caf-audit debug stats` should show fewer indexed canonical docs than discovered files when duplicates are being skipped correctly

## 4. Adding new documents

### Where to place files

Put new files only under the indexed source directories:

- `00_CONTEXTO`
- `01_RELATORIO_V2`
- `02_FONTE_VERDADE`
- `03_RELATORIO_V1`
- `04_PECAS_EVIDENCIA`
- `05_PECAS_TRAMITACAO`
- `06_NORMAS_CRITERIOS`
- `07_MODELOS_TCU`

Do not place files you expect to be indexed under:

- `99_DISCARDED`
- `01_RELATORIO_V2 copy`

### What happens internally

When a new file is indexed:

1. The system classifies its `source_type` from the top-level directory.
2. It extracts text and page spans.
3. It tries to infer `audit_object_id` from:
   - filename
   - path
   - direct `ACHxx` mentions
   - `Achado I/II/III/IV`
   - certain `PEÇA` ranges
4. It assigns `authority_weight` based on `SourceType`.
5. It deduplicates against canonical content via `content_hash`.
6. It chunks deterministically.
7. It writes SQL records and queues embeddings.
8. It reindexes document and chunk search representations in Elasticsearch.

### Triggering ingestion

For a manual rebuild:

```bash
caf-audit build
```

For file-system-triggered incremental indexing:

```bash
caf-audit watch
```

The watcher is implemented in `src/caf_audit_knowledge/cli.py` and watches all source directories recursively. On delete, it removes index state for that path.

## 5. Reindexing

### When to reindex

Use a full rebuild when:

- mappings changed
- chunking logic changed
- section typing changed
- relationship extraction changed
- pipeline fingerprint inputs changed
- you want a clean rebuild of SQL + Elasticsearch

### How to trigger it

Full rebuild:

```bash
caf-audit build --full
```

This recreates SQL tables and Elasticsearch indices.

Initialize or recreate only the indices:

```bash
caf-audit init-stores --recreate-indices
```

### Performance and risk notes

- `build --full` drops and recreates state.
- It requeues every chunk embedding as `pending`.
- The embedding worker must be run again after a full rebuild.
- Determinism can be checked with:

```bash
caf-audit build --full
caf-audit build --full
caf-audit debug compare-chunks
```

## 6. Search system

### 6.1 Hybrid search

Hybrid search is implemented in `src/caf_audit_knowledge/retrieval/service.py`.

BM25 path:

- Elasticsearch index: `caf_chunks`
- query type: `multi_match`
- fields:
  - `text^3`
  - `audit_object_id`
  - `source_type`

Vector path:

- embeds the query text with the configured embedding provider
- queries `chunks.embedding` using cosine distance
- implemented in `src/caf_audit_knowledge/retrieval/vector_store.py`

Candidate merge:

- BM25 candidates and vector candidates are merged by chunk id
- the merged set is truncated by `candidate_limit`
- `candidate_limit` depends on query type and risk level

### 6.2 Reranker

Reranking is implemented in `src/caf_audit_knowledge/retrieval/reranker.py`.

Current model:

- `BAAI/bge-reranker-large`

What the reranker sees for each candidate:

- document title
- source type
- section type
- audit object id
- page range
- chunk text

Why it matters in this codebase:

- BM25 is strong for `ACH01`, `Lei 11326`, and other lexical anchors
- vector search improves semantic recall
- reranking reduces boilerplate and shallow lexical hits

### 6.3 Final scoring

Final scoring is query-type dependent and implemented in:

- `src/caf_audit_knowledge/retrieval/scoring.py`
- `src/caf_audit_knowledge/retrieval/service.py`

Signals currently used:

- `reranker`
- `vector`
- `bm25`
- `authority`
- `entity`
- `evidence` for evidential queries only

`entity` here is derived from `entity_density`, normalized inside retrieval.

The calibrated factual baseline is:

```text
0.45 * reranker +
0.25 * vector +
0.15 * bm25 +
0.10 * authority +
0.05 * entity
```

Those weights are configurable in `src/caf_audit_knowledge/config.py` and are used as the base profile for `factual` queries. Other query types override that base when lexical precision or synthesis requirements differ.

For `evidential` queries the profile also includes an `evidence` signal, derived at ranking time from chunk metadata and textual evidence markers.

Example default scoring profiles:

- `exact_match`: BM25-heavy
- `summary`: reranker-heavy
- `evidential`: BM25 + reranker + authority
- `accountability`: reranker + entity-heavy
- `recommendation`: reranker-heavy

Additional policy multipliers are applied after base scoring:

- hard-filter explicit debug/review artifacts and stack traces before ranking
- penalize `debug`, `analysis`, `toc`, `intro`, `metodologia`
- penalize low entity density
- penalize low evidence density for `evidential` queries
- penalize `metodologia`, `procedimento`, `abordagem` more aggressively for `evidential` queries
- boost `sintese`, `causa`, `efeito`, `risco`
- boost preferred section types by query type
- boost legal-marker matches for `legal_reference`
- boost evidence-bearing chunks for `evidential`
- boost exact term matches
- boost hierarchical queries
- boost `normative` by `1.25`
- boost `ground_truth` by `1.15`

This combination matters for the real corpus. The repository includes review/debug artifacts and report scaffolding that are useful during drafting but are not suitable as top-ranked audit evidence.

## 7. Query types supported

The current classifier supports these primary query types:

- `exact_match`
- `summary`
- `factual`
- `aggregation`
- `evidential`
- `legal_reference`
- `accountability`
- `recommendation`
- `exploratory`

It also uses query facets:

- `hierarchical`
- `subscope`
- `exact_reference`

Examples that match the real classifier:

- `ACH01 inconsistência` -> `exact_match`
- `resuma o achado 3` -> `summary` + `hierarchical`
- `quais são as causas do subachado 1 do achado 1?` -> `factual` + `hierarchical` + `subscope`
- `quais evidências provaram o achado 3.1?` -> `evidential` + `hierarchical` + `subscope`
- `quais documentos comprovam o subachado 1?` -> `evidential` + `hierarchical` + `subscope`
- `qual legislação foi usada no achado 1?` -> `legal_reference` + `hierarchical`
- `quem ficou responsável pelo subachado 1 do achado 1?` -> `accountability` + `hierarchical` + `subscope`
- `qual a proposta de solução para o achado 4?` -> `recommendation` + `hierarchical`

## 8. Query classification

Query classification lives in `src/caf_audit_knowledge/answering/classifier.py`.

### Rule-based classification

The first pass is regex/token based.

Examples of implemented triggers:

- aggregation: `quantos`, `quantidade`, `total`
- summary: `resuma`, `síntese`
- evidential: `evidências`, `prova`, `comprovação`, `documentos`, `base documental`, `foi verificado`
- legal_reference: `legislação`, `norma`, `lei`, `decreto`
- accountability: `responsável`, `responsabilidade`
- recommendation: `proposta`, `solução`, `recomendação`
- factual: `causas`, `efeitos`, `riscos`

### LLM fallback

If rule confidence is below the threshold, the classifier can use the configured LLM provider.

Current config defaults:

- `CAF_CLASSIFICATION_LLM_FALLBACK_ENABLED=true`
- threshold `0.7`

### Adaptive learning

Classification feedback is persisted to:

- `ledger/query_feedback.jsonl`

Learned override patterns are persisted to:

- `ledger/query_patterns.json`

Operational commands:

```bash
caf-audit feedback-query "liste todos os achados" aggregation
caf-audit debug query-patterns
caf-audit debug query-feedback --limit 20
```

## 9. Prompt system

Prompt selection is implemented in `src/caf_audit_knowledge/answering/prompts.py`.

Answer generation itself is implemented in:

- `src/caf_audit_knowledge/answering/service.py`
- `src/caf_audit_knowledge/llm/providers.py`

Current defaults from `src/caf_audit_knowledge/config.py`:

- answering provider: `openai`
- answering model: `gpt-4.1-mini`
- Gemini is also implemented as an alternative provider

There is a dedicated task prompt for:

- `aggregation`
- `summary`
- `factual`
- `evidential`
- `legal_reference`
- `accountability`
- `recommendation`
- `exact_match`
- default exploratory mode

What the prompt system injects:

- conflict note
- risk note
- hierarchy note
- subscope note
- safe-mode note
- chunk-by-chunk context with:
  - `chunk_id`
  - `doc_id`
  - `source_type`
  - `audit_object_id`
  - `section_type`
  - citation (`p.` / `pp.`)

Why it improves answers:

- answer shape matches the question intent
- evidence queries ask for supporting pieces, not summaries
- legal queries emphasize explicit normative references
- safe mode tells the LLM to avoid guessing

## 10. Adaptive scoring

Adaptive scoring is implemented in `src/caf_audit_knowledge/retrieval/scoring.py`.

### Dynamic weights

Each query type has a default profile.

Examples:

- `evidential`: `reranker 0.40`, `vector 0.20`, `bm25 0.25`, `authority 0.15`
- `legal_reference`: `bm25 0.40`, `reranker 0.30`, `vector 0.15`, `authority 0.15`
- `accountability`: `reranker 0.45`, `entity 0.30`

### Auto-tuning

Answer feedback adjusts the profile in place:

- successful feedback slightly reinforces reranker/authority
- failed feedback increases reranker/vector, reduces BM25, and may increase authority/entity depending on query type

Persistence:

- profiles: `ledger/scoring_profiles.json`
- feedback history: `ledger/scoring_feedback.jsonl`

Commands:

```bash
caf-audit feedback-answer "quais evidências provaram o achado 3.1?" --failure
caf-audit debug scoring-profiles
caf-audit debug scoring-feedback --limit 20
```

## 11. Risk detection

Risk detection is implemented in `assess_query_risk()` in `src/caf_audit_knowledge/answering/classifier.py`.

Implemented risk flags:

- `hierarchical_query`
- `subscope_resolution_risk`
- `multi_evidence_required`
- `entity_resolution_risk`
- `aggregation_precision_risk`
- `legal_precision_required`
- `recommendation_synthesis_risk`
- `low_context`
- `cross_source_conflict`
- `ranking_ambiguity`

### Safe mode behavior

When `risk_score >= CAF_RISK_SAFE_MODE_THRESHOLD`:

- retrieval candidate limit is increased
- answer top-k is increased
- prompts instruct the LLM to prefer incompleteness over guessing
- explain logs show `safe_mode: true`

There is also a subscope guardrail in `src/caf_audit_knowledge/answering/service.py`:

- for `achado 3.1` or `subachado 1 do achado 1`
- if the retrieved evidence does not explicitly isolate the requested sub-scope
- the system can return a guarded answer instead of fabricating a precise sub-achado answer

## 12. Explainability / Debugging

### What `--explain` shows

For search:

```bash
caf-audit debug query "quem ficou responsável pelo subachado 1 do achado 1?" --explain
```

The output includes:

- top-level `conflict`
- `source_types`
- ranked results
- `query_context`
- `risk`
- `filtered_out`

Per result, `score_breakdown` includes:

- `bm25Raw`
- `bm25`
- `vectorRaw`
- `vector`
- `rerankerRaw`
- `reranker`
- `authority`
- `entityDensityRaw`
- `penalties`
- `boosts`
- `evidenceScore`
- `evidenceStructural`
- `evidenceBoostApplied`
- `methodologyPenaltyApplied`
- `policyMultiplier`
- `queryType`
- `queryFacets`
- `entityDensity`
- `riskFlags`
- `riskScore`
- `safeMode`
- `scoringProfile`
- `scoringProfileSource`
- `finalScore`

### Real example shape

Representative output from a live debug query:

```json
{
  "query_context": {
    "query_type": "accountability",
    "query_facets": ["hierarchical"],
    "candidate_limit": 70,
    "preferred_section_types": ["efeito", "risco", "sintese"]
  },
  "risk": {
    "flags": ["hierarchical_query", "entity_resolution_risk"],
    "score": 0.5,
    "safe_mode": true
  },
  "results": [
    {
      "chunk_id": "...",
      "score_breakdown": {
        "bm25Raw": 12.219331,
        "bm25": 0.114614,
        "vectorRaw": 0.879102,
        "vector": 0.780537,
        "rerankerRaw": 3.620441,
        "reranker": 0.023576,
        "authority": 0.95,
        "entityDensityRaw": 0.00367,
        "evidenceScore": 0.4,
        "evidenceStructural": false,
        "evidenceBoostApplied": true,
        "methodologyPenaltyApplied": false,
        "penalties": ["penalized: low entity density"],
        "boosts": ["boosted: seção preferida para accountability"],
        "policyMultiplier": 1.134,
        "queryType": "accountability",
        "queryFacets": ["hierarchical"],
        "riskScore": 0.5,
        "safeMode": true,
        "scoringProfileSource": "default",
        "finalScore": 0.507606
      }
    }
  ]
}
```

### Interpreting the signals

- high `bm25`: lexical match is strong
- high `vector`: semantic proximity is strong
- high `reranker`: pairwise relevance is strong
- high `authority`: source domain is authoritative
- `penalties`: soft demotions that still allowed the chunk to rank
- `boosts`: positive policy adjustments for section/query fit
- `evidenceScore`: evidence-bearing strength derived from section metadata and textual heuristics
- `evidenceBoostApplied`: evidential ranking boost fired for this chunk
- `methodologyPenaltyApplied`: stronger evidential penalty fired for methodology-like chunks
- high `entityDensity`: chunk has more ACH/legal/piece anchor content
- high `policyMultiplier`: section/query policy boosted the chunk
- `safeMode=true`: the system considered the query operationally risky
- `filtered_out`: candidates removed entirely before ranking because they matched hard-noise rules

## 13. Logs

### Build-time artifacts

The indexer writes:

- manifests in `manifests/`
- latest build snapshot in `manifests/latest.json`
- pruning ledger in `ledger/pruning.jsonl`

Manifest content includes:

- build id
- pipeline fingerprint
- summary counts
- canonical document list
- duplicate list
- chunk manifest hashes
- chunk feature hashes
- chunk page ranges
- pruning details

### Query and answer logs

Answer traces are persisted to:

- `ledger/query_logs.jsonl`

Each answer log contains:

- `classification`
- `risk`
- `conflict`
- `query_context`
- `retrieval`
- `filtered_out`
- `rerank`
- `scoring`
- `final`
- final answer text

Commands:

```bash
caf-audit debug query-logs --limit 5
```

### Classification and scoring learning logs

- query classifier feedback: `ledger/query_feedback.jsonl`
- learned classifier patterns: `ledger/query_patterns.json`
- scoring feedback: `ledger/scoring_feedback.jsonl`
- learned scoring profiles: `ledger/scoring_profiles.json`

## 14. Known limitations

These are real current limitations of the codebase.

- PDF parsing is text extraction via `pypdf`, not layout-aware parsing.
- `structured_markdown` is page-structured text, not deeply structured tables/sections.
- Chroma is declared as an optional dependency but is not wired into retrieval.
- Hierarchical queries are only partially structured.
  - `achado 3.1` is detected as risky.
  - true `subachado_id` indexing does not yet exist.
- Aggregation answers are prompt-based, not a deterministic aggregation engine.
- Result quality still depends heavily on chunking and `section_type` inference.
- Elasticsearch search uses a relatively simple `multi_match`, not a richer fielded DSL.
- Test coverage is currently narrow.
  - present: deterministic chunking and repo semantics
  - absent: end-to-end indexing, retrieval, answer generation

## 15. Best practices

### Writing good queries

Prefer queries that expose the intent clearly.

Good:

- `resuma o achado 3`
- `quais evidências provaram o achado 3.1?`
- `qual legislação foi usada no achado 1?`
- `quem ficou responsável pelo subachado 1 do achado 1?`

Less precise:

- `me fale do problema`
- `explique isso`

### When to use exact match

Use exact-match style queries when you have stable anchors:

- `ACH01`
- quoted strings
- law references like `Lei 11326`

### How to interpret results

- Prefer `evidence`, `ground_truth`, and `normative` over low-authority sources when they disagree.
- Use `--explain` when results feel surprising.
- Read `reasons` and `section_type` before trusting a top result.
- If `safeMode` is on, treat the answer as cautious rather than exhaustive.

## 16. Future improvements

The following are consistent next steps given the current implementation:

- add structured `subachado_id` extraction and indexing
- add a deterministic aggregation layer for counting/list-all questions
- improve PDF parsing with layout-aware extraction
- expand tests to cover indexing, embeddings, retrieval, and GraphQL
- add richer Elasticsearch query construction
- add learning-to-rank or offline evaluation harnesses

## 17. Operating the system

### Environment

The app loads environment variables from both:

- repository root `.env`
- app-local `.env`

Reference example:

- `.env.example`

Recommended local values:

```bash
CAF_REPOSITORY_ROOT=/Users/fgamajr/Desktop/CAF-FINAL
CAF_DATABASE_URL=postgresql+psycopg://postgres:postgres@localhost:5432/caf_audit
CAF_ELASTICSEARCH_URL=http://localhost:9200
CAF_VECTOR_BACKEND=pgvector
CAF_EMBEDDING_PROVIDER=openai
CAF_EMBEDDING_MODEL=text-embedding-3-large
CAF_ANSWERING_PROVIDER=openai
CAF_ANSWERING_MODEL=gpt-4.1-mini
OPENAI_API_KEY=...
CAF_GRAPHQL_HOST=127.0.0.1
CAF_GRAPHQL_PORT=8000
```

### Local setup

```bash
cd /Users/fgamajr/Desktop/CAF-FINAL/caf_audit_knowledge
python3 -m venv .venv
source .venv/bin/activate
pip install -e .[dev]
docker compose up -d
```

### First build

```bash
caf-audit init-stores
caf-audit build --full
caf-audit embed-worker
```

### Serve GraphQL

```bash
caf-audit serve
```

Endpoints:

- GraphQL: `http://127.0.0.1:8000/graphql`
- health: `http://127.0.0.1:8000/healthz`

### Example GraphQL queries

Search:

```graphql
query {
  search(query: "resuma o achado 3", explain: true) {
    score
    scoreBreakdown {
      bm25
      vector
      reranker
      authority
      queryType
      queryFacets
      riskFlags
      safeMode
      finalScore
    }
    chunk {
      id
      sourceType
      auditObjectId
      sectionType
      pageStart
      pageEnd
      text
    }
  }
}
```

Answer:

```graphql
query {
  answer(query: "quais evidências provaram o achado 3.1?", explain: true) {
    answer
    classification {
      queryType
      confidence
      source
      facets
    }
    risk
    sourceTypes
    explainLog
  }
}
```

Feedback:

```graphql
mutation {
  registerQueryFeedback(query: "liste todos os achados", correctType: "aggregation")
}
```

```graphql
mutation {
  registerAnswerFeedback(
    query: "quais evidências provaram o achado 3.1?"
    success: false
  )
}
```

## 18. Debug checklist

If indexing looks wrong:

```bash
caf-audit debug list-docs --limit 20
caf-audit debug stats
caf-audit validate
```

If determinism looks wrong:

```bash
caf-audit build --full
caf-audit build --full
caf-audit debug compare-chunks
```

If answers look wrong:

```bash
caf-audit debug classify-query "quais evidências provaram o achado 3.1?"
caf-audit debug query "quais evidências provaram o achado 3.1?" --explain
caf-audit answer "quais evidências provaram o achado 3.1?" --explain
caf-audit debug query-logs --limit 1
```

If scoring needs recalibration:

```bash
caf-audit feedback-answer "qual legislação foi usada no achado 1?" --failure
caf-audit debug scoring-profiles
caf-audit debug scoring-feedback --limit 5
```

If embeddings are missing:

```bash
caf-audit debug stats
caf-audit embed-worker
```

If watch mode is preferred:

```bash
caf-audit watch
```

That is the current system as implemented today.
