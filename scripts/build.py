#!/usr/bin/env python3
"""Rebuild CTA6 readable pages from data/sources.csv and data/timeline.csv.

Invent nothing. Every fact on a generated page is taken from those spreadsheets.
"""

from __future__ import annotations

import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPTS))

import schema as S  # noqa: E402


def load_csv(path: Path, expected_fields: list[str]) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames != expected_fields:
            raise SystemExit(
                f"{path}: unexpected columns {reader.fieldnames!r}; "
                f"expected {expected_fields!r}"
            )
        return [{k: (v or "") for k, v in row.items()} for row in reader]


def md_cell(text: str) -> str:
    """Escape characters that would break markdown emphasis or accidental links."""
    return text.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def md_link(label: str, url: str) -> str:
    safe = label.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]").replace("(", "\\(").replace(")", "\\)")
    return f"[{safe}]({url})"


def source_index(sources: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    return {row["id"]: row for row in sources}


def citations_for(sources_by_id: dict[str, dict[str, str]], row: dict[str, str], from_timeline: bool) -> str:
    parts = []
    for key, url_key in (("citation_source_id", "url"), ("citation_source_id_2", "url_2")):
        sid = row[key].strip()
        if not sid:
            continue
        src = sources_by_id[sid]
        href = f"{S.region_href(src['region'], from_timeline=from_timeline)}#{sid}"
        url = row[url_key] or src["url"]
        parts.append(f"{md_link(sid, href)} ({md_link(url, url)})")
    if not parts:
        return "[UNKNOWN]"
    if len(parts) == 1:
        return parts[0]
    return "\n".join(f"- {p}" for p in parts)


def timeline_entry_md(row: dict[str, str], sources_by_id: dict[str, dict[str, str]], from_timeline: bool) -> str:
    lines = [
        f'<a id="{row["id"]}"></a>',
        f'## {row["id"]}',
        "",
        f'- Date: {md_cell(row["date"])}',
        f'- Place: {md_cell(row["place"])}',
        f'- Region: {md_cell(row["region"])}',
        f'- Theme: {md_cell(row["theme"])}',
        f'- Status: `{row["confidence"]}`',
        "",
        row["what_happened"],
        "",
    ]
    if (row.get("summary") or "").strip():
        lines.append(f'Summary: {md_cell(row["summary"])}')
        lines.append("")
    if (row.get("notes") or "").strip():
        lines.append(f'- Notes: {md_cell(row["notes"])}')
        lines.append("")
    cites = citations_for(sources_by_id, row, from_timeline=from_timeline)
    if cites.startswith("- "):
        lines.append("Citations:")
        lines.append("")
        lines.append(cites)
    else:
        lines.append(f"Citation: {cites}")
    lines.append("")
    return "\n".join(lines)


def source_entry_md(
    src: dict[str, str],
    cited_by: list[dict[str, str]],
    *,
    from_region_page: bool,
) -> str:
    lines = [
        f'<a id="{src["id"]}"></a>',
        f'## {src["id"]}',
        "",
        f'**{md_cell(src["title"])}**',
        "",
    ]
    if (src.get("summary") or "").strip():
        lines += [f'Summary: {md_cell(src["summary"])}', ""]
    lines += [
        f'- Issuing body: {md_cell(src["author_or_issuing_body"])}',
        f'- Date: {md_cell(src["date"])}',
        f'- Type: {md_cell(src["type"])}',
        f'- Tag: `{src["tag"]}`',
        f'- Origin: `{src["origin"]}`',
        f'- Era: {md_cell(src["era"])}',
        f'- Region: {md_cell(src["region"])}',
        f'- Theme: {md_cell(src["theme"])}',
        f'- URL: {md_link(src["url"], src["url"])}',
        f'- Accessed: {md_cell(src["accessed"])}',
        f'- Verified: `{src["verified"]}`',
    ]
    if (src.get("language") or "").strip():
        lines.append(f'- Language: {md_cell(src["language"])}')
    if (src.get("case_citation") or "").strip():
        lines.append(f'- Case citation: {md_cell(src["case_citation"])}')
    if src.get("notes", "").strip():
        lines.append(f'- Notes: {md_cell(src["notes"])}')
    lines.append("")
    if cited_by:
        links = []
        for t in cited_by:
            href = f"{S.era_href(t['era'], from_sources=True)}#{t['id']}"
            links.append(md_link(t["id"], href))
        lines.append("Cited by: " + ", ".join(links))
    else:
        lines.append("Cited by: none in `data/timeline.csv`.")
    lines.append("")
    return "\n".join(lines)


def status_counts(rows: list[dict[str, str]]) -> str:
    c = Counter(r["confidence"] for r in rows)
    return "\n".join(f"- `{label}`: {c.get(label, 0)}" for label in S.STATUSES)


def write(path: Path, body: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    text = S.GENERATED_HEADER + "\n\n" + body
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8")


def clear_generated() -> None:
    for folder in (S.TIMELINE_DIR, S.REGIONS_DIR, S.THEMES_DIR, S.SOURCES_DIR):
        if not folder.exists():
            continue
        for path in folder.glob("*.md"):
            path.unlink()


def build_timeline_pages(
    sources: list[dict[str, str]],
    timeline: list[dict[str, str]],
    sources_by_id: dict[str, dict[str, str]],
) -> None:
    by_era: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in timeline:
        by_era[row["era"]].append(row)

    index = [
        "# Timeline",
        "",
        "Round 1 of an ongoing archive. This list is not complete. "
        "Every entry is taken from `data/timeline.csv`.",
        "",
        f"{len(timeline)} milestones in this round.",
        "",
        status_counts(timeline),
        "",
        "| Era | Milestones | File |",
        "|---|---:|---|",
    ]
    for era in S.ERAS:
        rows = by_era.get(era, [])
        slug = S.ERA_SLUGS[era]
        index.append(f"| {md_cell(era)} | {len(rows)} | [{slug}.md]({slug}.md) |")
        page = [
            f"# Timeline: {era}",
            "",
            "Round 1 of an ongoing archive. This list is not complete. "
            "Every entry is taken from the cited row in `data/timeline.csv`.",
            "",
            f"{len(rows)} milestone{'s' if len(rows) != 1 else ''} in this era.",
            "",
            status_counts(rows),
            "",
            "See [GAPS.md](../GAPS.md) for what this round did not gather.",
            "",
        ]
        if not rows:
            page.append("No milestones were gathered for this era in this round. [UNKNOWN]")
            page.append("")
        for row in rows:
            page.append(timeline_entry_md(row, sources_by_id, from_timeline=True))
        write(S.era_path(era), "\n".join(page))

    index += [
        "",
        "The canonical records are in [`data/timeline.csv`](../data/timeline.csv). "
        "Citations point to the source pages under [`sources/`](../sources/).",
        "",
    ]
    write(S.TIMELINE_DIR / "README.md", "\n".join(index))


def build_source_pages(
    sources: list[dict[str, str]],
    timeline: list[dict[str, str]],
) -> None:
    cited: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in timeline:
        cited[row["citation_source_id"]].append(row)
        if row["citation_source_id_2"].strip():
            cited[row["citation_source_id_2"]].append(row)

    by_region: dict[str, list[dict[str, str]]] = defaultdict(list)
    by_theme: dict[str, list[dict[str, str]]] = defaultdict(list)
    for src in sources:
        by_region[src["region"]].append(src)
        by_theme[src["theme"]].append(src)

    def render_source_list(rows: list[dict[str, str]]) -> str:
        chunks = []
        for src in rows:
            chunks.append(source_entry_md(src, cited.get(src["id"], []), from_region_page=True))
        return "\n".join(chunks)

    region_index_rows = []
    for region in S.REGIONS:
        rows = by_region.get(region, [])
        slug = S.REGION_SLUGS[region]
        region_index_rows.append(f"| {md_cell(region)} | {len(rows)} | [{slug}.md](regions/{slug}.md) |")
        origins = Counter(s["origin"] for s in rows)
        origin_line = ", ".join(f"`{o}` {origins[o]}" for o in S.ORIGINS if origins.get(o))
        page = [
            f"# Sources: {region}",
            "",
            "Round 1 of an ongoing archive. This list is not complete. "
            "Every field is taken from `data/sources.csv`.",
            "",
            f"{len(rows)} source{'s' if len(rows) != 1 else ''} in this region"
            + (f" ({origin_line})." if origin_line else "."),
            "",
            "See [GAPS.md](../../GAPS.md) for what this round did not gather.",
            "",
        ]
        if not rows:
            page.append("No sources were gathered for this region in this round. [UNKNOWN]")
            page.append("")
        else:
            page.append(render_source_list(rows))
        write(S.region_path(region), "\n".join(page))

    theme_index_rows = []
    for theme in S.THEMES:
        rows = by_theme.get(theme, [])
        slug = S.THEME_SLUGS[theme]
        theme_index_rows.append(f"| {md_cell(theme)} | {len(rows)} | [{slug}.md](themes/{slug}.md) |")
        page = [
            f"# Sources: {theme}",
            "",
            S.THEME_DESCRIPTIONS[theme],
            "",
            "Round 1 of an ongoing archive. This list is not complete. "
            "Every field is taken from `data/sources.csv`.",
            "",
            f"{len(rows)} source{'s' if len(rows) != 1 else ''} in this theme.",
            "",
            "See [GAPS.md](../../GAPS.md) for what this round did not gather.",
            "",
        ]
        if not rows:
            page.append("No sources were gathered for this theme in this round. [UNKNOWN]")
            page.append("")
        else:
            page.append(render_source_list(rows))
        write(S.theme_path(theme), "\n".join(page))

    oversight = [s for s in sources if s["origin"] in S.OVERSIGHT_ORIGINS]
    ov_counts = Counter(s["origin"] for s in oversight)
    ov_line = ", ".join(f"`{o}` {ov_counts[o]}" for o in S.OVERSIGHT_ORIGINS if ov_counts.get(o))
    ov_page = [
        "# Sources: independent oversight and criticism",
        "",
        "Sources whose origin is `oversight`, `court`, or `NGO`. "
        "This is a sub-list from the round 1 outline in `docs/STRUCTURE.md`. "
        "These records also appear on their region and theme pages. "
        "The list is not complete, and this page draws no conclusions from it.",
        "",
        f"{len(oversight)} sources ({ov_line}).",
        "",
        render_source_list(oversight),
    ]
    write(S.THEMES_DIR / f"{S.OVERSIGHT_SLUG}.md", "\n".join(ov_page))

    index = [
        "# Sources",
        "",
        "Round 1 of an ongoing archive. This list is not complete. "
        "Every field is taken from `data/sources.csv`.",
        "",
        f"{len(sources)} sources in this round "
        f"({sum(1 for s in sources if s['tag']=='primary')} primary, "
        f"{sum(1 for s in sources if s['tag']=='secondary')} secondary).",
        "",
        "Sources are grouped by region and by theme. A source has one region and one theme in this spreadsheet; many records span more than one category in practice.",
        "",
        "## By region",
        "",
        "| Region | Sources | File |",
        "|---|---:|---|",
        *region_index_rows,
        "",
        "## By theme",
        "",
        "| Theme | Sources | File |",
        "|---|---:|---|",
        *theme_index_rows,
        "",
        "## Independent oversight and criticism",
        "",
        f"{len(oversight)} sources whose origin is `oversight`, `court`, or `NGO` "
        f"are also listed in [{S.OVERSIGHT_SLUG}.md](themes/{S.OVERSIGHT_SLUG}.md).",
        "",
        "The canonical records are in [`data/sources.csv`](../data/sources.csv).",
        "",
    ]
    write(S.SOURCES_DIR / "README.md", "\n".join(index))


def ids_line(rows: list[dict[str, str]], key: str, value: str) -> str:
    found = [r["id"] for r in rows if r[key] == value]
    if not found:
        return "[UNKNOWN] (none gathered yet)"
    return ", ".join(found)


def build_structure(sources: list[dict[str, str]], timeline: list[dict[str, str]]) -> None:
    lines = [
        "# CTA6: structure (round 1)",
        "",
        "This outline is generated from `data/sources.csv` and `data/timeline.csv`. "
        "It draws no conclusions. Each section lists the source ids and timeline ids that map to it. "
        "A source maps to one era, one region and one theme; timeline rows take their era from their date "
        "and their region and theme from their first cited source.",
        "",
        "Wording rule: contested labels are attributed to whoever applied them "
        "(for example, a designation by a named government body). "
        "Where sources disagree, both are cited and the timeline row is marked people-disagree.",
        "",
        "This is round 1 of an ongoing archive. It is not complete.",
        "",
        "Every source and timeline row carries a `summary` column: two to four short sentences on what the item is "
        "and why it matters, written only from what the archive holds. Gaps are marked [UNKNOWN]. "
        "The pages show the summary under each entry, with the citation and link still shown.",
        "",
        "## Part A: Eras",
        "",
    ]
    for era in S.ERAS:
        n_s = sum(1 for s in sources if s["era"] == era)
        n_t = sum(1 for t in timeline if t["era"] == era)
        lines += [
            f"### {era}",
            "",
            f"- Sources ({n_s}): {ids_line(sources, 'era', era)}",
            f"- Timeline ({n_t}): {ids_line(timeline, 'era', era)}",
            "",
        ]
    lines += ["## Part B: Regions", ""]
    for region in S.REGIONS:
        n_s = sum(1 for s in sources if s["region"] == region)
        n_t = sum(1 for t in timeline if t["region"] == region)
        lines += [
            f"### {region}",
            "",
            f"- Sources ({n_s}): {ids_line(sources, 'region', region)}",
            f"- Timeline ({n_t}): {ids_line(timeline, 'region', region)}",
            "",
        ]
    lines += ["## Part C: Themes", ""]
    for theme in S.THEMES:
        n_s = sum(1 for s in sources if s["theme"] == theme)
        n_t = sum(1 for t in timeline if t["theme"] == theme)
        lines += [
            f"### {theme}",
            "",
            S.THEME_DESCRIPTIONS[theme],
            "",
            f"- Sources ({n_s}): {ids_line(sources, 'theme', theme)}",
            f"- Timeline ({n_t}): {ids_line(timeline, 'theme', theme)}",
            "",
        ]
    oversight = [s for s in sources if s["origin"] in S.OVERSIGHT_ORIGINS]
    lines += [
        "### Sub-list: independent oversight and criticism (origin = oversight, court or NGO)",
        "",
        "- " + ", ".join(f"{s['id']} ({s['origin']})" for s in oversight),
        "",
        "## Part D: Repository layout",
        "",
        "```",
        "CTA6/",
        "  README.md",
        "  GAPS.md",
        "  NOTES.md",
        "  data/sources.csv",
        "  data/timeline.csv",
        "  docs/STRUCTURE.md",
        "  scripts/build.py",
        "  scripts/check.py",
        "  timeline/<era>.md",
        "  sources/regions/<region>.md",
        "  sources/themes/<theme>.md",
        "```",
        "",
        "Page captures stay on the local machine and are not part of this repository.",
        "",
    ]
    write(S.STRUCTURE_MD, "\n".join(lines))


def main() -> None:
    sources = load_csv(S.SOURCES_CSV, S.SOURCE_FIELDS)
    timeline = load_csv(S.TIMELINE_CSV, S.TIMELINE_FIELDS)
    sources_by_id = source_index(sources)
    clear_generated()
    build_timeline_pages(sources, timeline, sources_by_id)
    build_source_pages(sources, timeline)
    build_structure(sources, timeline)
    print(
        f"built {len(sources)} sources, {len(timeline)} milestones "
        f"-> {S.TIMELINE_DIR.relative_to(S.ROOT)}/, {S.SOURCES_DIR.relative_to(S.ROOT)}/, "
        f"{S.STRUCTURE_MD.relative_to(S.ROOT)}"
    )


if __name__ == "__main__":
    main()
