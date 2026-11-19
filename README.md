# CTA6

CTA6 is a private archival collection of published official and scholarly records on the history of counterterrorism. It is global in scope and is built in rounds. This is **round 1**. It is not a complete history, and it does not claim to be one.

The canonical records are the spreadsheets in `data/`. The pages under `timeline/` and `sources/` are a readable view generated from those spreadsheets. Do not edit the generated pages by hand.

This repository is meant for later publication as the private GitHub repository `AdventureNLearn/CTA6`. That GitHub repository has not been created in this round.

## What is in round 1

- 196 sources in [`data/sources.csv`](data/sources.csv) (180 primary, 16 secondary)
- 132 timeline milestones in [`data/timeline.csv`](data/timeline.csv)
- Milestone status in this round: 119 we-have-a-record, 8 not-proven, 5 people-disagree
- A readable timeline, one file per era, in [`timeline/`](timeline/)
- Sources grouped by region and theme in [`sources/`](sources/)
- The outline of eras, regions and themes in [`docs/STRUCTURE.md`](docs/STRUCTURE.md)
- Known gaps, dropped candidates and unconfirmed URLs in [`GAPS.md`](GAPS.md)
- The round 1 source-gathering record in [`NOTES.md`](NOTES.md)

Sources were chosen by hand and are not a systematic sample. Counts describe this round only. Later rounds should fill the gaps listed in `GAPS.md`.

## Neutrality method

- Use neutral wording. The archive does not adopt a government's or organisation's label as its own.
- Credit contested labels to whoever used them (for example, a designation by a named government body). Words such as "terrorist" or "terrorism" appear when they are part of an official title or a quoted instrument name, as issued.
- Where sources disagree, record each side with its own citation and mark the timeline row `people-disagree`. The archive does not pick a winner.
- Tag every source `primary` or `secondary`, and record its origin: `government`, `international`, `academic`, `NGO`, `court`, or `oversight`.
- Official records and independent oversight, court and NGO records are all in scope, so criticism and limits appear alongside statutes and resolutions.
- Do not invent. If a fact, date or document is missing, mark it `[UNKNOWN]`. Do not guess a URL, a date, or a conclusion.

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

1. Add a row to `data/sources.csv` with every required field: `id`, `title`, `author_or_issuing_body`, `date`, `type`, `tag`, `origin`, `era`, `region`, `theme`, `url`, `accessed`, and `verified`. Use the vocabularies already used in the spreadsheet (see `docs/STRUCTURE.md`). If a date is not known, write `[UNKNOWN]`. Put confirmation details in `notes`.
2. If the record is also a milestone, add a row to `data/timeline.csv`. `citation_source_id` must be an `id` that already exists in `data/sources.csv`. Every statement in `what_happened` must come from the cited source. Set `confidence` to one of the three status labels above. If sources disagree, fill `citation_source_id_2` and `url_2`, and mark the row `people-disagree`.
3. From the repository root, run `python3 scripts/check.py` and fix any errors.
4. Run `python3 scripts/build.py` to regenerate `timeline/`, `sources/` and `docs/STRUCTURE.md`.
5. Do not invent facts, do not commit page captures, and do not add personal data or secrets.

## Page captures

When sources were gathered, page captures were saved locally (HTML or PDF, extracted text, and fetch metadata). Those files are large and are **not part of this repository**. They remain on the local machine only. The `.gitignore` file is set so a `raw/` folder is not committed.

## Scripts

- `python3 scripts/check.py` — confirms that the spreadsheets parse, that every timeline row cites an existing source id, and that no row is missing a URL or a status label.
- `python3 scripts/build.py` — rebuilds the readable timeline and source pages, and `docs/STRUCTURE.md`, from the spreadsheets.
