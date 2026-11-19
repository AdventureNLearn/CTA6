# CTA6

CTA6 is a private archival collection of published official and scholarly records on the history of counterterrorism. It is global in scope and is built in rounds. This is **round 4**. It is not a complete history, and it does not claim to be one.

The canonical records are the spreadsheets in `data/`. The pages under `timeline/` and `sources/` are a readable view generated from those spreadsheets. Do not edit the generated pages by hand.

The private GitHub repository exists at [`AdventureNLearn/CTA6`](https://github.com/AdventureNLearn/CTA6).

## What is in round 4

- 368 sources in [`data/sources.csv`](data/sources.csv) (338 primary, 30 secondary; 331 verified, 37 not)
- 236 timeline milestones in [`data/timeline.csv`](data/timeline.csv)
- Milestone status in this round: 219 we-have-a-record, 8 not-proven, 9 people-disagree
- A readable timeline, one file per era, in [`timeline/`](timeline/)
- Sources grouped by region and theme in [`sources/`](sources/)
- The outline of eras, regions and themes in [`docs/STRUCTURE.md`](docs/STRUCTURE.md)
- Known gaps, dropped candidates and unconfirmed URLs in [`GAPS.md`](GAPS.md)
- The round 1 source-gathering record in [`NOTES.md`](NOTES.md)
- The round 2 source-gathering record in [`notes/round-2.md`](notes/round-2.md)
- The round 3 source-gathering record in [`notes/round-3.md`](notes/round-3.md)
- The round 4 source-gathering record in [`notes/round-4.md`](notes/round-4.md)

Round 4 added 7 sources and 6 milestones (T231–T236) to the 361 sources and 230 milestones from round 3. It applied selected pass 4 corrections: official-copy URL swaps for US-NSCT2018, CRS-R43983, COE-ECST1977 and COE-CPT2005 (now `verified=yes`); OCR verification of the G5 Sahel convention scan; and summary-date fills. T015 and T085 stay `not-proven` because the words “opened for signature” rest on an explanatory report that has been identified but not yet read. T045 is unchanged. Sources were chosen by hand and are not a systematic sample. Counts describe the archive as of this round. This archive is not complete. Later rounds should fill the gaps listed in `GAPS.md`.

## Neutrality method

- Use neutral wording. The archive does not adopt a government's or organisation's label as its own.
- Credit contested labels to whoever used them (for example, a designation by a named government body). Words such as "terrorist" or "terrorism" appear when they are part of an official title or a quoted instrument name, as issued.
- Where sources disagree, record each side with its own citation and mark the timeline row `people-disagree`. The archive does not pick a winner.
- Tag every source `primary` or `secondary`, and record its origin: `government`, `international`, `academic`, `NGO`, `court`, or `oversight`.
- Official records and independent oversight, court and NGO records are all in scope, so criticism and limits appear alongside statutes and resolutions.
- Do not invent. If a fact, date or document is missing, mark it `[UNKNOWN]`. Do not guess a URL, a date, or a conclusion.

## Names in case titles

Private individuals who are parties or applicants in a case, and who are not public officials, are named by initials taken from the name as printed in the source. Public officials, states and organisations stay named. Every case keeps its official number or citation. Source ids that would otherwise contain a private person's surname use a court-year-number form instead. URLs are unchanged.

## Language

Every source has a `language` column. Pass 2 recorded the language of the source text. Round 1 rows, gathered before that column existed, are marked `[UNKNOWN]`; that is a gap, not a claim that the language was never known. Where a source has no English title, the original title is used and `notes` says "English title: [UNKNOWN]".

An optional `case_citation` column holds the official case number or citation when one was recorded in the pass 2 corrections.

## Summaries

Every source and every timeline row has a required `summary` column: two to four short sentences on what the item is and why it matters. The summary sits beside the original fields; it does not replace `title`, `what_happened`, `notes`, the citations or the URLs, and the built pages show it under each entry with the citation and link still shown.

Summaries are written only from what the archive already holds for that row: its own fields, the rows it links to, the round notes and the local page captures. They follow the same rules as the rest of the archive. Contested claims are attributed to whoever made them. Where a source is `verified=no`, the summary says the cited copy could not be confirmed. Where a row is `not-proven` or `people-disagree`, the summary says what is and is not backed. Private individuals stay as initials. Where the archive does not show why an item matters, the summary says what it is and marks the rest `[UNKNOWN]`.

## Status labels

Every timeline row has one of these status labels, in the `confidence` column:

| Label | Meaning |
|---|---|
| `we-have-a-record` | The fact is taken from a cited source that was fetched and checked in this round. |
| `not-proven` | The cited source could not be confirmed in this round (for example the URL was blocked, the document was not reached, or a date could not be checked). The row is kept, but it is not treated as confirmed. |
| `people-disagree` | Cited sources disagree. Both sides are linked. The archive does not choose between them. |

`[UNKNOWN]` marks a gap or an unknown value (for example an incomplete date). It is not a substitute for a guess.

Sources also carry `verified=yes` or `verified=no`, which records whether the cited URL was fetched and matched in this round. A timeline row that cites an unverified source is marked `not-proven`, except where a different confirmation problem is noted in the row itself.

## How to add to the archive

1. Add a row to `data/sources.csv` with every required field: `id`, `title`, `author_or_issuing_body`, `date`, `type`, `tag`, `origin`, `era`, `region`, `theme`, `url`, `accessed`, `verified`, `language` and `summary`. Use the vocabularies already used in the spreadsheet (see `docs/STRUCTURE.md`). If a date or language is not known, write `[UNKNOWN]`. Put confirmation details in `notes`. If the record is a case, add the official citation in `case_citation` and follow the naming rule above.
2. If the record is also a milestone, add a row to `data/timeline.csv`. `citation_source_id` must be an `id` that already exists in `data/sources.csv`. Every statement in `what_happened` and `summary` must come from the cited source or the archive's own records. Set `confidence` to one of the three status labels above. If sources disagree, fill `citation_source_id_2` and `url_2`, and mark the row `people-disagree`.
3. From the repository root, run `python3 scripts/check.py` and fix any errors.
4. Run `python3 scripts/build.py` to regenerate `timeline/`, `sources/` and `docs/STRUCTURE.md`.
5. Do not invent facts, do not commit page captures or working maps of old names, and do not add personal data or secrets.

## Page captures

When sources were gathered, page captures were saved locally (HTML or PDF, extracted text, and fetch metadata). Those files are large and are **not part of this repository**. They remain on the local machine only. The `.gitignore` file is set so a `raw/` or `work/` folder is not committed.

## Scripts

- `python3 scripts/check.py` — confirms that the spreadsheets parse, that every timeline row cites an existing source id, and that no row is missing a URL or a status label. A surname scan is not part of the check: a committed list would only be useful if it contained names, and those names are not committed.
- `python3 scripts/build.py` — rebuilds the readable timeline and source pages, and `docs/STRUCTURE.md`, from the spreadsheets.
