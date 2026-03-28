from __future__ import annotations

from functools import lru_cache
from typing import Protocol

from tenacity import retry, stop_after_attempt, wait_exponential

from caf_audit_knowledge.config import settings


class CompletionProvider(Protocol):
    def complete(self, *, system: str, prompt: str) -> str: ...


class OpenAICompletionProvider:
    def __init__(self) -> None:
        from openai import OpenAI

        api_key = settings.openai_api_key
        if not api_key:
            raise RuntimeError("OPENAI_API_KEY is not set")
        self.client = OpenAI(api_key=api_key)

    @retry(wait=wait_exponential(min=1, max=20), stop=stop_after_attempt(3), reraise=True)
    def complete(self, *, system: str, prompt: str) -> str:
        response = self.client.responses.create(
            model=settings.answering_model,
            temperature=settings.answering_temperature,
            max_output_tokens=settings.answering_max_output_tokens,
            input=[
                {
                    "role": "system",
                    "content": [{"type": "input_text", "text": system}],
                },
                {
                    "role": "user",
                    "content": [{"type": "input_text", "text": prompt}],
                },
            ],
        )
        return response.output_text.strip()


class GeminiCompletionProvider:
    def __init__(self) -> None:
        from google import genai

        api_key = settings.gemini_api_key
        if not api_key:
            raise RuntimeError("GEMINI_API_KEY is not set")
        self.client = genai.Client(api_key=api_key)

    @retry(wait=wait_exponential(min=1, max=20), stop=stop_after_attempt(3), reraise=True)
    def complete(self, *, system: str, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=settings.answering_model,
            contents=f"{system}\n\n{prompt}",
        )
        text = getattr(response, "text", None)
        if not text:
            raise RuntimeError("Gemini returned an empty response")
        return text.strip()


@lru_cache(maxsize=1)
def get_completion_provider() -> CompletionProvider:
    provider = settings.answering_provider.lower()
    if provider == "openai":
        return OpenAICompletionProvider()
    if provider == "gemini":
        return GeminiCompletionProvider()
    raise ValueError(f"Unsupported answering provider: {settings.answering_provider}")
