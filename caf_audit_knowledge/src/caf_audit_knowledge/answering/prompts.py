from __future__ import annotations

from caf_audit_knowledge.answering.classifier import QueryClassification, RiskAssessment
from caf_audit_knowledge.retrieval.service import SearchHit


SYSTEM_PROMPT = """You are an audit-grade assistant over the CAF knowledge system.

Rules:
- Answer only from the provided evidence.
- Preserve provenance. Cite evidence inline using [chunk_id, citation].
- Do not hallucinate counts, facts, or legal conclusions.
- If the evidence is insufficient, say so explicitly.
- When sources disagree or multiple source types appear, acknowledge the conflict."""


def _format_context(hits: list[SearchHit]) -> str:
    blocks = []
    for hit in hits:
        citation = None
        if hit.chunk.page_start is not None and hit.chunk.page_end not in {None, hit.chunk.page_start}:
            citation = f"pp. {hit.chunk.page_start}-{hit.chunk.page_end}"
        elif hit.chunk.page_start is not None:
            citation = f"p. {hit.chunk.page_start}"
        snippet = hit.chunk.text.strip()
        if len(snippet) > 1600:
            snippet = f"{snippet[:1600].rstrip()}..."
        blocks.append(
            "\n".join(
                [
                    f"[chunk:{hit.chunk.id}]",
                    f"doc_id={hit.chunk.document_id}",
                    f"source_type={hit.chunk.source_type}",
                    f"audit_object_id={hit.chunk.audit_object_id or 'unscoped'}",
                    f"section_type={hit.chunk.section_type or 'body'}",
                    f"citation={citation or 'n/a'}",
                    f"text={snippet}",
                ]
            )
        )
    return "\n\n".join(blocks)


def build_prompt(
    query: str,
    hits: list[SearchHit],
    classification: QueryClassification,
    conflict: dict,
    risk: RiskAssessment,
) -> str:
    context = _format_context(hits)
    if classification.query_type == "aggregation":
        task = """You are analyzing audit findings.

Task:
- Aggregate ALL relevant evidence.
- Identify distinct issues without duplicating them.
- Count them only when the count is explicit.
- If the count is not explicit, state "não há número explícito".

Rules:
- Do not return partial aggregation as if it were complete.
- Distinguish categories from totals.
- Mention uncertainty when categories overlap.
- Do not merge counts from different ACH objects into one total unless a source explicitly consolidates them.
- If the retrieved evidence spans different ACH objects without a single authoritative consolidation, say the query is ambiguous."""
    elif classification.query_type == "summary":
        task = """You are summarizing an audit finding.

Task:
- Produce a complete summary using all relevant sections.
- Combine synthesis, causes, effects, and risks when available.

Rules:
- Do not rely on a single passage.
- Prefer higher-authority evidence when sources differ.
- Keep the summary concise but complete."""
    elif classification.query_type == "factual":
        task = """You are extracting targeted factual information.

Task:
- Extract only the requested information.
- List the relevant items clearly.

Rules:
- Prefer sections that directly match the request.
- Avoid unrelated sections unless they are needed to clarify ambiguity."""
    elif classification.query_type == "evidential":
        task = """You are identifying evidentiary support.

Task:
- List the evidence pieces that directly support the answer.
- Explain briefly what each evidence item proves.

Rules:
- Prefer direct evidence over narrative summaries.
- If multiple evidence pieces are needed, keep them distinct.
- Do not infer support that is not explicit in the retrieved text."""
    elif classification.query_type == "legal_reference":
        task = """You are extracting legal and normative references.

Task:
- Identify the legislation, norms, or criteria actually used in the evidence.
- Keep references tied to the cited passages.

Rules:
- Prefer explicit legal mentions.
- Do not invent article numbers or normative links.
- If a norm is implied but not named, state that it is not explicit."""
    elif classification.query_type == "accountability":
        task = """You are extracting accountability information.

Task:
- Identify who is responsible, attributed, or implicated, if explicit.
- Distinguish between direct responsibility and contextual mention.

Rules:
- Do not guess unnamed actors.
- If the responsible party is not explicit, say so clearly."""
    elif classification.query_type == "recommendation":
        task = """You are extracting proposals and recommendations.

Task:
- Identify the proposed solution, recommendation, or remediation path.
- Keep recommendations linked to the cited evidence.

Rules:
- Distinguish recommendations from causes and effects.
- If there is no explicit recommendation, say so."""
    elif classification.query_type == "exact_match":
        task = """You are retrieving exact references.

Task:
- Focus on exact mentions and direct evidence tied to the query.

Rules:
- Do not generalize beyond the exact evidence.
- Keep the answer grounded in the cited passages."""
    else:
        task = """You are exploring an audit knowledge base.

Task:
- Identify the most relevant patterns and insights from the evidence.

Rules:
- Synthesize carefully.
- Separate firm findings from weaker indications."""

    hierarchy_note = ""
    if "hierarchical" in classification.facets:
        hierarchy_note = "Preserve the hierarchy between achado and subachado. Do not merge sibling subfindings into one answer.\n\n"
    subscope_note = ""
    if "subscope" in classification.facets:
        subscope_note = (
            "The question targets a sub-achado granularity.\n"
            "- Only answer at that sub-achado level if the retrieved evidence explicitly isolates it.\n"
            '- If the evidence supports only the parent achado, state "não foi possível isolar o subachado solicitado".\n\n'
        )
    safe_mode_note = ""
    if risk.safe_mode:
        safe_mode_note = (
            "Safe mode is active.\n"
            "- Ensure completeness before answering.\n"
            '- If information is missing, explicitly state "não foi possível identificar completamente".\n'
            "- Do not guess.\n\n"
        )
    conflict_note = (
        f"Conflict flag: {conflict['conflict']}. Source types in retrieved evidence: {', '.join(conflict['source_types']) or 'none'}."
    )
    risk_note = f"Risk flags: {', '.join(risk.flags) or 'none'}. Risk score: {risk.score}."
    return (
        f"{task}\n\n"
        f"{hierarchy_note}"
        f"{subscope_note}"
        f"{safe_mode_note}"
        f"{conflict_note}\n\n"
        f"{risk_note}\n\n"
        f"Context:\n{context}\n\n"
        f"Question:\n{query}\n\n"
        "Answer in Portuguese. Keep it concise, cite evidence inline using exact chunk ids like [chunk:abc123, p. 4], and end with a short 'Base probatória' list."
    )
