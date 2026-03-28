from caf_audit_knowledge.ingest.chunking import build_chunks


def test_chunking_is_deterministic_and_bounded():
    text = "\n\n".join(f"Paragraph {idx} with Lei 11326 and PEÇA 103." for idx in range(20))
    chunks_a, ledger_a = build_chunks("doc-1", text, "evidence", 0.95, "ACH01")
    chunks_b, ledger_b = build_chunks("doc-1", text, "evidence", 0.95, "ACH01")
    assert [chunk["id"] for chunk in chunks_a] == [chunk["id"] for chunk in chunks_b]
    assert len(chunks_a) <= 8
    assert ledger_a == ledger_b
