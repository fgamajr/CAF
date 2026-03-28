#!/usr/bin/env python3
"""
Sincroniza comentários de revisão de um .docx para issues do GitHub.

Escopo intencionalmente enxuto:
- fluxo unidirecional: Word -> GitHub
- comentários apenas; não trata controle de alterações
- âncora por seção/cabeçalho mais próximo e trecho comentado quando disponível

Requer:
- `gh` autenticado com permissão de `repo`

Exemplo:
    python3 scripts/sync_word_comments_to_github.py \
        --docx "idSisdoc_32894821v23-74 - Instrucao_Processo_01107320250.docx" \
        --repo fgamajr/CAF \
        --apply \
        --export-json .local/docx_review_sync/instrucao_processo_01107320250.json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from collections import OrderedDict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable
from xml.etree import ElementTree as ET
from zipfile import ZipFile


NS = {
    "w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main",
    "w14": "http://schemas.microsoft.com/office/word/2010/wordml",
    "w15": "http://schemas.microsoft.com/office/word/2012/wordml",
    "w16cid": "http://schemas.microsoft.com/office/word/2016/wordml/cid",
}

SYNC_MARKER_PREFIX = "docx-comment-sync:key="
LABEL_WORD_REVIEW = "word-review"


def qname(prefix: str, name: str) -> str:
    return f"{{{NS[prefix]}}}{name}"


def normalize_space(value: str | None) -> str:
    if not value:
        return ""
    return re.sub(r"\s+", " ", value).strip()


def slugify(value: str) -> str:
    lowered = value.lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    return lowered.strip("-") or "unknown"


def truncate(value: str, limit: int) -> str:
    if len(value) <= limit:
        return value
    return value[: limit - 1].rstrip() + "…"


def gh(*args: str, capture_output: bool = True) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["gh", *args],
        check=True,
        text=True,
        capture_output=capture_output,
    )


@dataclass
class CommentRecord:
    source_doc: str
    comment_id: str
    durable_id: str
    author: str
    initials: str
    date: str
    resolved: bool
    section: str
    anchor_text: str
    paragraph_text: str
    comment_text: str
    external_key: str
    title: str
    body: str
    author_label: str


def parse_comment_metadata(docx_path: Path) -> tuple[dict[str, dict], dict[str, bool], dict[str, str]]:
    with ZipFile(docx_path) as archive:
        comments_root = ET.fromstring(archive.read("word/comments.xml"))
        comments_ex_root = ET.fromstring(archive.read("word/commentsExtended.xml"))
        comments_ids_root = ET.fromstring(archive.read("word/commentsIds.xml"))

    resolved_by_para_id: dict[str, bool] = {}
    for item in comments_ex_root.findall(".//w15:commentEx", NS):
        para_id = item.get(qname("w15", "paraId"), "")
        resolved_by_para_id[para_id] = item.get(qname("w15", "done"), "0") == "1"

    durable_by_para_id: dict[str, str] = {}
    for item in comments_ids_root.findall(".//w16cid:commentId", NS):
        para_id = item.get(qname("w16cid", "paraId"), "")
        durable_by_para_id[para_id] = item.get(qname("w16cid", "durableId"), "")

    comments: dict[str, dict] = {}
    for comment in comments_root.findall(".//w:comment", NS):
        comment_id = comment.get(qname("w", "id"), "")
        author = comment.get(qname("w", "author"), "") or "Autor desconhecido"
        initials = comment.get(qname("w", "initials"), "") or ""
        date = comment.get(qname("w", "date"), "") or ""
        para = comment.find("w:p", NS)
        para_id = para.get(qname("w14", "paraId"), "") if para is not None else ""
        text = normalize_space(" ".join(comment.itertext()))
        comments[comment_id] = {
            "comment_id": comment_id,
            "author": author,
            "initials": initials,
            "date": date,
            "comment_text": text,
            "comment_para_id": para_id,
            "durable_id": durable_by_para_id.get(para_id, ""),
            "resolved": resolved_by_para_id.get(para_id, False),
        }

    return comments, resolved_by_para_id, durable_by_para_id


def heading_level(style_name: str) -> int | None:
    if not style_name:
        return None
    lowered = style_name.lower()
    if "ttulo" not in lowered and "heading" not in lowered and "titulo" not in lowered:
        return None
    match = re.search(r"(\d+)$", style_name)
    if not match:
        return 1
    return int(match.group(1))


def paragraph_text_and_selections(paragraph: ET.Element) -> tuple[str, dict[str, str], list[str]]:
    active_comment_ids: list[str] = []
    paragraph_fragments: list[str] = []
    selected_fragments: dict[str, list[str]] = {}
    referenced_comment_ids: list[str] = []

    def walk(node: ET.Element) -> None:
        tag = node.tag
        if tag == qname("w", "commentRangeStart"):
            comment_id = node.get(qname("w", "id"), "")
            if comment_id:
                active_comment_ids.append(comment_id)
                referenced_comment_ids.append(comment_id)
            return

        if tag == qname("w", "commentRangeEnd"):
            comment_id = node.get(qname("w", "id"), "")
            if comment_id in active_comment_ids:
                active_comment_ids.remove(comment_id)
                referenced_comment_ids.append(comment_id)
            return

        if tag == qname("w", "commentReference"):
            comment_id = node.get(qname("w", "id"), "")
            if comment_id:
                referenced_comment_ids.append(comment_id)
            return

        if tag == qname("w", "t"):
            text = node.text or ""
            if text:
                paragraph_fragments.append(text)
                for comment_id in active_comment_ids:
                    selected_fragments.setdefault(comment_id, []).append(text)

        if tag == qname("w", "tab"):
            paragraph_fragments.append("\t")
            for comment_id in active_comment_ids:
                selected_fragments.setdefault(comment_id, []).append("\t")

        if tag in {qname("w", "br"), qname("w", "cr")}:
            paragraph_fragments.append("\n")
            for comment_id in active_comment_ids:
                selected_fragments.setdefault(comment_id, []).append("\n")

        for child in list(node):
            walk(child)

    walk(paragraph)
    paragraph_text = normalize_space("".join(paragraph_fragments))
    selections = {
        comment_id: normalize_space("".join(fragments))
        for comment_id, fragments in selected_fragments.items()
    }
    unique_comment_ids = list(OrderedDict.fromkeys(referenced_comment_ids))
    return paragraph_text, selections, unique_comment_ids


def build_section_path(active_headings: dict[int, str]) -> str:
    return " > ".join(active_headings[level] for level in sorted(active_headings))


def parse_document_anchors(docx_path: Path) -> dict[str, dict]:
    with ZipFile(docx_path) as archive:
        document_root = ET.fromstring(archive.read("word/document.xml"))

    anchors: dict[str, dict] = {}
    active_headings: dict[int, str] = {}
    last_non_empty_paragraph = ""
    paragraph_index = 0

    for paragraph in document_root.findall(".//w:body//w:p", NS):
        paragraph_index += 1
        paragraph_text, selected_fragments, referenced_comment_ids = paragraph_text_and_selections(paragraph)

        style_el = paragraph.find("./w:pPr/w:pStyle", NS)
        style_name = style_el.get(qname("w", "val"), "") if style_el is not None else ""
        level = heading_level(style_name)
        if level is not None and paragraph_text:
            active_headings[level] = paragraph_text
            for other_level in list(active_headings):
                if other_level > level:
                    del active_headings[other_level]

        section = build_section_path(active_headings)
        fallback_anchor = paragraph_text or last_non_empty_paragraph

        for comment_id in referenced_comment_ids:
            if comment_id in anchors:
                continue
            anchor_text = selected_fragments.get(comment_id) or fallback_anchor
            anchors[comment_id] = {
                "section": section,
                "anchor_text": anchor_text,
                "paragraph_text": paragraph_text,
                "paragraph_index": paragraph_index,
            }

        if paragraph_text:
            last_non_empty_paragraph = paragraph_text

    return anchors


def build_issue_title(section: str, comment_text: str) -> str:
    tail = truncate(comment_text, 72)
    if section:
        short_section = truncate(section.split(" > ")[-1], 42)
        return truncate(f"[Word Review] {short_section}: {tail}", 120)
    return truncate(f"[Word Review] {tail}", 120)


def build_issue_body(record: CommentRecord) -> str:
    anchor_line = record.anchor_text or "Trecho âncora não identificado."
    section_line = record.section or "Seção não identificada."
    status = "resolvido" if record.resolved else "aberto"

    return "\n".join(
        [
            "Importado automaticamente de comentário do Word.",
            "",
            f"- Documento: `{record.source_doc}`",
            f"- ID do comentário no Word: `{record.comment_id}`",
            f"- Durable ID: `{record.durable_id or 'indisponível'}`",
            f"- Autor no Word: `{record.author}`",
            f"- Data no Word: `{record.date or 'indisponível'}`",
            f"- Status no Word: `{status}`",
            f"- Seção: {section_line}",
            f"- Trecho âncora: \"{anchor_line}\"",
            "",
            "**Comentário**",
            "",
            record.comment_text or "_Comentário sem texto_",
            "",
            f"<!-- {SYNC_MARKER_PREFIX}{record.external_key} -->",
        ]
    )


def extract_records(docx_path: Path) -> list[CommentRecord]:
    comments, _, _ = parse_comment_metadata(docx_path)
    anchors = parse_document_anchors(docx_path)
    source_doc = docx_path.name
    records: list[CommentRecord] = []

    for comment_id, meta in comments.items():
        anchor = anchors.get(comment_id, {})
        durable_id = meta["durable_id"] or f"comment-{comment_id}"
        section = anchor.get("section", "")
        anchor_text = anchor.get("anchor_text", "")
        paragraph_text = anchor.get("paragraph_text", "")
        external_key = f"{source_doc}:{durable_id}"
        author_label = f"reviewer:{slugify(meta['author'])}"
        title = build_issue_title(section, meta["comment_text"])
        record = CommentRecord(
            source_doc=source_doc,
            comment_id=comment_id,
            durable_id=durable_id,
            author=meta["author"],
            initials=meta["initials"],
            date=meta["date"],
            resolved=meta["resolved"],
            section=section,
            anchor_text=anchor_text,
            paragraph_text=paragraph_text,
            comment_text=meta["comment_text"],
            external_key=external_key,
            title=title,
            body="",
            author_label=author_label,
        )
        record.body = build_issue_body(record)
        records.append(record)

    return records


def extract_sync_key(issue_body: str) -> str | None:
    match = re.search(r"<!--\s*docx-comment-sync:key=(.*?)\s*-->", issue_body or "")
    return match.group(1).strip() if match else None


def list_existing_issues(repo: str) -> dict[str, dict]:
    result = gh("issue", "list", "--repo", repo, "--state", "all", "--limit", "500", "--json", "number,title,state,body")
    issues = json.loads(result.stdout or "[]")
    by_key: dict[str, dict] = {}
    for issue in issues:
        key = extract_sync_key(issue.get("body", ""))
        if key:
            by_key[key] = issue
    return by_key


def list_existing_labels(repo: str) -> set[str]:
    result = gh("api", f"repos/{repo}/labels?per_page=100")
    labels = json.loads(result.stdout or "[]")
    return {item["name"] for item in labels}


def ensure_labels(repo: str, records: Iterable[CommentRecord]) -> None:
    existing = list_existing_labels(repo)
    wanted = {
        LABEL_WORD_REVIEW: ("1d76db", "Importado automaticamente de revisão em Word"),
    }
    for record in records:
        wanted.setdefault(record.author_label, ("5319e7", f"Comentário importado de {record.author}"))

    for name, (color, description) in wanted.items():
        if name in existing:
            continue
        gh("label", "create", name, "--repo", repo, "--color", color, "--description", description)


def write_temp_body(content: str) -> str:
    temp = tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False)
    with temp:
        temp.write(content)
    return temp.name


def sync_record(repo: str, record: CommentRecord, existing_issue: dict | None) -> str:
    labels = [LABEL_WORD_REVIEW, record.author_label]
    body_file = write_temp_body(record.body)
    try:
        if existing_issue is None:
            result = gh(
                "issue",
                "create",
                "--repo",
                repo,
                "--title",
                record.title,
                "--body-file",
                body_file,
                *(arg for label in labels for arg in ("--label", label)),
            )
            created_ref = result.stdout.strip()
            if record.resolved:
                created_number = created_ref.rstrip("/").split("/")[-1]
                gh("issue", "close", created_number, "--repo", repo, "--comment", "Fechado automaticamente: comentário no Word marcado como resolvido.")
                return f"created+closed #{created_number}"
            return f"created {created_ref}"

        issue_number = str(existing_issue["number"])
        changed = existing_issue.get("title") != record.title or (existing_issue.get("body") or "") != record.body
        if changed:
            gh(
                "issue",
                "edit",
                issue_number,
                "--repo",
                repo,
                "--title",
                record.title,
                "--body-file",
                body_file,
                *(arg for label in labels for arg in ("--add-label", label)),
            )

        state = (existing_issue.get("state") or "").upper()
        if record.resolved and state != "CLOSED":
            gh("issue", "close", issue_number, "--repo", repo, "--comment", "Fechado automaticamente: comentário no Word marcado como resolvido.")
            return f"updated+closed #{issue_number}" if changed else f"closed #{issue_number}"
        if not record.resolved and state == "CLOSED":
            gh("issue", "reopen", issue_number, "--repo", repo)
            return f"updated+reopened #{issue_number}" if changed else f"reopened #{issue_number}"
        return f"updated #{issue_number}" if changed else f"unchanged #{issue_number}"
    finally:
        Path(body_file).unlink(missing_ok=True)


def export_records(records: list[CommentRecord], export_path: Path) -> None:
    export_path.parent.mkdir(parents=True, exist_ok=True)
    payload = [asdict(record) for record in records]
    export_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sincroniza comentários de Word para issues do GitHub.")
    parser.add_argument("--docx", required=True, type=Path, help="Arquivo .docx de origem")
    parser.add_argument("--repo", required=True, help="Repositório GitHub no formato owner/repo")
    parser.add_argument("--apply", action="store_true", help="Aplica a sincronização no GitHub")
    parser.add_argument("--export-json", type=Path, help="Exporta os comentários normalizados em JSON")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    docx_path = args.docx.resolve()
    if not docx_path.exists():
        raise SystemExit(f"Arquivo não encontrado: {docx_path}")

    records = extract_records(docx_path)
    if args.export_json:
        export_records(records, args.export_json)

    print(f"Arquivo: {docx_path.name}")
    print(f"Comentários encontrados: {len(records)}")

    if not args.apply:
        for record in records[:10]:
            print(f"- {record.external_key} | {record.section or 'sem seção'} | {record.comment_text[:90]}")
        if len(records) > 10:
            print(f"... {len(records) - 10} comentários adicionais omitidos no dry-run")
        print("Dry-run concluído. Use --apply para sincronizar com o GitHub.")
        return 0

    ensure_labels(args.repo, records)
    existing_issues = list_existing_issues(args.repo)

    created = updated = unchanged = reopened = closed = 0
    for record in records:
        action = sync_record(args.repo, record, existing_issues.get(record.external_key))
        print(action)
        if action.startswith("created+closed"):
            created += 1
            closed += 1
        elif action.startswith("created"):
            created += 1
        elif "reopened" in action:
            reopened += 1
            if action.startswith("updated"):
                updated += 1
        elif "closed" in action:
            closed += 1
            if action.startswith("updated"):
                updated += 1
        elif action.startswith("updated"):
            updated += 1
        elif action.startswith("unchanged"):
            unchanged += 1

    print(
        "Resumo: "
        f"created={created} updated={updated} unchanged={unchanged} reopened={reopened} closed={closed}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
