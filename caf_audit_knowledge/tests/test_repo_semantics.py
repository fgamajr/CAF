from pathlib import Path

from caf_audit_knowledge.repo_semantics import canonical_rank, extract_audit_object_id, should_ignore_path


def test_ignore_discards_and_backups():
    assert should_ignore_path(Path("99_DISCARDED/foo.md"))
    assert should_ignore_path(Path("01_RELATORIO_V2/bar.md.bak"))
    assert should_ignore_path(Path(".venv/lib/site.py"))


def test_extract_ach_from_piece_range_and_filename():
    assert extract_audit_object_id("", Path("04_PECAS_EVIDENCIA/ACH02_geoespacial/peca111_PT02_dimensionamento_leaflet.pdf")) == "ACH02"
    assert extract_audit_object_id("## ACH-01", Path("foo.md")) == "ACH01"
    assert extract_audit_object_id("", Path("04_PECAS_EVIDENCIA/TRANSVERSAIS/peca080_lei_11326_2006.pdf")) is None


def test_canonical_prefers_markdown_before_pdf():
    assert canonical_rank(Path("doc.md")) < canonical_rank(Path("doc.pdf"))
