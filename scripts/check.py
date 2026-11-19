#!/usr/bin/env python3
"""Check CTA6 spreadsheets and scan the repo for personal data or secrets."""

from __future__ import annotations

import csv
import re
import sys
from collections import Counter
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import schema as S  # noqa: E402

URL_RE = re.compile(r"^https?://\S+$", re.IGNORECASE)
EMAIL_RE = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
HOME_RE = re.compile(r"(?:/home/|/Users/)[A-Za-z0-9._-]+")
WIN_USER_RE = re.compile(r"C:\\Users\\[A-Za-z0-9._-]+", re.IGNORECASE)
SSN_RE = re.compile(r"\b\d{3}-\d{2}-\d{4}\b")
AWS_RE = re.compile(r"AKIA[0-9A-Z]{16}")
PRIVKEY_RE = re.compile(r"BEGIN (?:RSA |OPENSSH |EC )?PRIVATE KEY")
SECRET_RE = re.compile(
    r"(?i)(?:api[_-]?key|secret|token|password|bearer)\s*[:=]\s*\S+"
)

SCAN_SKIP_DIRS = {".git", "__pycache__", ".venv", "venv", "raw"}
SCAN_SKIP_SUFFIXES = {".pyc", ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".zip"}


def error(problems: list[str], msg: str) -> None:
    problems.append(msg)


def load(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fields = list(reader.fieldnames or [])
        rows = [{k: (v or "") for k, v in row.items()} for row in reader]
    return fields, rows


def blank(value: str) -> bool:
    return not value.strip()


def check_sources(rows: list[dict[str, str]], fields: list[str], problems: list[str]) -> None:
    if fields != S.SOURCE_FIELDS:
        error(problems, f"data/sources.csv columns {fields!r} do not match {S.SOURCE_FIELDS!r}")
    ids: set[str] = set()
    for i, row in enumerate(rows, start=2):
        loc = f"data/sources.csv:{i} ({row.get('id') or 'missing-id'})"
        for key in S.SOURCE_REQUIRED:
            if key not in row or blank(row[key]):
                error(problems, f"{loc} missing required field {key}")
        sid = row.get("id", "").strip()
        if sid:
            if sid in ids:
                error(problems, f"{loc} duplicate source id {sid}")
            ids.add(sid)
        if row.get("tag") and row["tag"] not in S.TAGS:
            error(problems, f"{loc} unexpected tag {row['tag']!r}")
        if row.get("origin") and row["origin"] not in S.ORIGINS:
            error(problems, f"{loc} unexpected origin {row['origin']!r}")
        if row.get("era") and row["era"] not in S.ERAS:
            error(problems, f"{loc} unexpected era {row['era']!r}")
        if row.get("region") and row["region"] not in S.REGIONS:
            error(problems, f"{loc} unexpected region {row['region']!r}")
        if row.get("theme") and row["theme"] not in S.THEMES:
            error(problems, f"{loc} unexpected theme {row['theme']!r}")
        if row.get("verified") and row["verified"] not in S.VERIFIED:
            error(problems, f"{loc} unexpected verified value {row['verified']!r}")
        url = row.get("url", "").strip()
        if url and not URL_RE.match(url):
            error(problems, f"{loc} URL is not an http(s) URL: {url!r}")


def check_timeline(
    rows: list[dict[str, str]],
    fields: list[str],
    source_ids: set[str],
    sources: dict[str, dict[str, str]],
    problems: list[str],
) -> None:
    if fields != S.TIMELINE_FIELDS:
        error(problems, f"data/timeline.csv columns {fields!r} do not match {S.TIMELINE_FIELDS!r}")
    ids: set[str] = set()
    for i, row in enumerate(rows, start=2):
        loc = f"data/timeline.csv:{i} ({row.get('id') or 'missing-id'})"
        for key in S.TIMELINE_REQUIRED:
            if key not in row or blank(row[key]):
                error(problems, f"{loc} missing required field {key}")
        tid = row.get("id", "").strip()
        if tid:
            if tid in ids:
                error(problems, f"{loc} duplicate timeline id {tid}")
            ids.add(tid)
        status = row.get("confidence", "").strip()
        if not status:
            error(problems, f"{loc} missing status (confidence)")
        elif status not in S.STATUSES:
            error(problems, f"{loc} unexpected status {status!r}")
        s1 = row.get("citation_source_id", "").strip()
        s2 = row.get("citation_source_id_2", "").strip()
        if s1 and s1 not in source_ids:
            error(problems, f"{loc} citation_source_id {s1} is not in data/sources.csv")
        if s2 and s2 not in source_ids:
            error(problems, f"{loc} citation_source_id_2 {s2} is not in data/sources.csv")
        if status == "people-disagree" and not s2:
            error(problems, f"{loc} people-disagree row is missing citation_source_id_2")
        url = row.get("url", "").strip()
        if url and not URL_RE.match(url):
            error(problems, f"{loc} URL is not an http(s) URL: {url!r}")
        url2 = row.get("url_2", "").strip()
        if s2 and not url2:
            error(problems, f"{loc} has a second citation but is missing url_2")
        if url2 and not URL_RE.match(url2):
            error(problems, f"{loc} url_2 is not an http(s) URL: {url2!r}")
        if s1 and s1 in sources and url and url != sources[s1]["url"]:
            error(problems, f"{loc} url does not match sources.csv for {s1}")
        if s2 and s2 in sources and url2 and url2 != sources[s2]["url"]:
            error(problems, f"{loc} url_2 does not match sources.csv for {s2}")
        if row.get("era") and row["era"] not in S.ERAS:
            error(problems, f"{loc} unexpected era {row['era']!r}")
        if row.get("region") and row["region"] not in S.REGIONS:
            error(problems, f"{loc} unexpected region {row['region']!r}")
        if row.get("theme") and row["theme"] not in S.THEMES:
            error(problems, f"{loc} unexpected theme {row['theme']!r}")


def iter_repo_files() -> list[Path]:
    files = []
    for path in S.ROOT.rglob("*"):
        if not path.is_file():
            continue
        if any(part in SCAN_SKIP_DIRS for part in path.parts):
            continue
        if path.suffix.lower() in SCAN_SKIP_SUFFIXES:
            continue
        files.append(path)
    return files


def scan_repo(problems: list[str]) -> None:
    """Scan committed-path files for personal data, secrets, and expanded home paths."""
    for path in iter_repo_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            error(problems, f"{path.relative_to(S.ROOT)} is not valid UTF-8")
            continue
        rel = str(path.relative_to(S.ROOT))
        for name, regex in (
            ("email address", EMAIL_RE),
            ("expanded home path", HOME_RE),
            ("Windows user path", WIN_USER_RE),
            ("SSN-like number", SSN_RE),
            ("AWS access key", AWS_RE),
            ("private key block", PRIVKEY_RE),
            ("secret-like assignment", SECRET_RE),
        ):
            hits = regex.findall(text)
            if not hits:
                continue
            # Show the pattern, not a secret value, if a secret-like assignment is found.
            if name in {"AWS access key", "private key block", "secret-like assignment"}:
                error(problems, f"{rel} contains a {name}")
            else:
                shown = ", ".join(sorted({h if isinstance(h, str) else h[0] for h in hits}))
                error(problems, f"{rel} contains a {name}: {shown}")


def main() -> int:
    problems: list[str] = []
    try:
        source_fields, sources = load(S.SOURCES_CSV)
    except csv.Error as exc:
        print(f"FAIL: data/sources.csv did not parse: {exc}")
        return 1
    try:
        timeline_fields, timeline = load(S.TIMELINE_CSV)
    except csv.Error as exc:
        print(f"FAIL: data/timeline.csv did not parse: {exc}")
        return 1

    check_sources(sources, source_fields, problems)
    source_map = {row["id"]: row for row in sources if row.get("id")}
    check_timeline(timeline, timeline_fields, set(source_map), source_map, problems)
    scan_repo(problems)

    status = Counter(row["confidence"] for row in timeline)
    tags = Counter(row["tag"] for row in sources)
    verified = Counter(row["verified"] for row in sources)
    print("CTA6 check")
    print(f"  sources: {len(sources)} (primary {tags.get('primary', 0)}, secondary {tags.get('secondary', 0)}; verified yes {verified.get('yes', 0)}, no {verified.get('no', 0)})")
    print(f"  milestones: {len(timeline)}")
    for label in S.STATUSES:
        print(f"    {label}: {status.get(label, 0)}")
    if problems:
        print(f"FAIL: {len(problems)} problem(s)")
        for msg in problems:
            print(f"  - {msg}")
        return 1
    print("PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
