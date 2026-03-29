from __future__ import annotations

import json
from functools import cached_property
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from caf_audit_knowledge.constants import CHUNK_TARGET_CHARS, HARD_LIMIT, MAX_CHUNKS_PER_DOC

REPOSITORY_ROOT = Path(__file__).resolve().parents[3]
APP_ROOT = REPOSITORY_ROOT / "caf_audit_knowledge"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(str(REPOSITORY_ROOT / ".env"), str(APP_ROOT / ".env")),
        env_prefix="CAF_",
        extra="ignore",
    )

    repository_root: Path = Field(default_factory=lambda: REPOSITORY_ROOT)
    data_root: Path | None = None
    database_url: str = "sqlite+pysqlite:///caf_audit.db"
    elasticsearch_url: str = "http://localhost:9200"
    elasticsearch_user: str | None = None
    elasticsearch_password: str | None = None
    openai_api_key: str | None = Field(default=None, validation_alias="OPENAI_API_KEY")
    gemini_api_key: str | None = Field(default=None, validation_alias="GEMINI_API_KEY")
    vector_backend: str = "pgvector"
    embedding_provider: str = "openai"
    embedding_model: str = "text-embedding-3-large"
    embedding_version: str = "v1"
    embedding_dimensions: int = 3072
    embedding_batch_size: int = 16
    embedding_max_retries: int = 5
    embedding_max_input_chars: int = 8000
    embedding_request_char_budget: int = 24000
    reranker_enabled: bool = True
    reranker_model: str = "BAAI/bge-reranker-large"
    reranker_device: str = "auto"
    reranker_batch_size: int = 16
    reranker_max_length: int = 512
    reranker_candidate_k: int = 50
    reranker_use_fp16: bool = True
    answering_provider: str = "openai"
    answering_model: str = "gpt-4.1-mini"
    answering_temperature: float = 0.0
    answering_max_output_tokens: int = 1200
    classification_llm_fallback_enabled: bool = True
    classification_llm_fallback_threshold: float = 0.7
    adaptive_classifier_enabled: bool = True
    adaptive_pattern_min_token_length: int = 5
    adaptive_pattern_min_support: int = 1
    answer_top_k_default: int = 5
    answer_top_k_expanded: int = 8
    risk_safe_mode_threshold: float = 0.5
    safe_mode_top_k_bonus: int = 3
    score_weight_bm25: float = 0.15
    score_weight_vector: float = 0.25
    score_weight_reranker: float = 0.45
    score_weight_authority: float = 0.10
    score_weight_entity_density: float = 0.05
    score_weight_evidence: float = 0.0
    graphql_host: str = "127.0.0.1"
    graphql_port: int = 8000
    chunk_target_chars: int = CHUNK_TARGET_CHARS
    max_chunks_per_doc: int = MAX_CHUNKS_PER_DOC
    hard_limit: int = HARD_LIMIT

    @cached_property
    def effective_data_root(self) -> Path:
        return self.data_root or (self.repository_root / "caf_audit_knowledge" / ".data")

    @cached_property
    def pipeline_fingerprint(self) -> str:
        payload = {
            "embedding_model": self.embedding_model,
            "embedding_provider": self.embedding_provider,
            "embedding_version": self.embedding_version,
            "embedding_max_input_chars": self.embedding_max_input_chars,
            "embedding_request_char_budget": self.embedding_request_char_budget,
            "vector_backend": self.vector_backend,
            "chunk_target_chars": self.chunk_target_chars,
            "max_chunks_per_doc": self.max_chunks_per_doc,
            "hard_limit": self.hard_limit,
        }
        return json.dumps(payload, sort_keys=True)

    @cached_property
    def app_root(self) -> Path:
        return APP_ROOT

    @cached_property
    def ledger_root(self) -> Path:
        return self.app_root / "ledger"

    @cached_property
    def manifests_root(self) -> Path:
        return self.app_root / "manifests"

    @cached_property
    def query_patterns_path(self) -> Path:
        return self.ledger_root / "query_patterns.json"

    @cached_property
    def query_feedback_path(self) -> Path:
        return self.ledger_root / "query_feedback.jsonl"

    @cached_property
    def query_logs_path(self) -> Path:
        return self.ledger_root / "query_logs.jsonl"

    @cached_property
    def scoring_profiles_path(self) -> Path:
        return self.ledger_root / "scoring_profiles.json"

    @cached_property
    def scoring_feedback_path(self) -> Path:
        return self.ledger_root / "scoring_feedback.jsonl"


settings = Settings()
