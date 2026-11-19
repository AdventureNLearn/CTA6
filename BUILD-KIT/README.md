# CTA6 - Reference Archive Build Kit

This kit tells an app builder how to turn the CTA6 archive into a globe app. It is written for the Grok.me app builder, but any builder or developer can follow it.

The kit is a plan. It holds no app code. Nothing in it publishes, uploads or signs in anywhere.

## What the app is

The app is a reader for the CTA6 counterterrorism reference archive. It shows the archive's milestones on a 3D globe and lets people browse the sources behind them.

- Milestones come from `data/timeline.csv`. Sources come from `data/sources.csv`.
- Each milestone is pinned at the level of its country. Rows with no usable place go in a "No location" panel.
- People can filter by region, theme, era and record label, move through time, search, and open a cited entry.
- The app adds no commentary. It shows what the archive holds, including its gaps.

## Who it is for

- Readers who want a neutral, cited overview of counterterrorism laws, treaties, agencies and reviews.
- Students, teachers and researchers who want to follow a citation back to an official text.
- Anyone checking what the archive does and does not yet hold.

## What is in the kit

| File | What it is |
|---|---|
| [`BUILD-PLAN.md`](BUILD-PLAN.md) | Step-by-step build plan, with acceptance checks for each step. |
| [`DATA-CONTRACT.md`](DATA-CONTRACT.md) | Every field, its allowed values, and how the app must display it. Includes the country pin table. |
| [`SAFETY-AND-NEUTRALITY.md`](SAFETY-AND-NEUTRALITY.md) | Neutrality, privacy and credit rules the app must keep. |
| [`TEST-PLAN.md`](TEST-PLAN.md) | Smoke test and release checks. |
| [`GROKME-PROMPT.md`](GROKME-PROMPT.md) | One paste-ready prompt for the Grok.me app builder. |

## Design references

The app reuses features from two public globe apps by the same owner: SeaGlobe and WNTR's Globe. `BUILD-PLAN.md` lists each borrowed feature and the file it comes from. Features from those apps that do not fit an archive reader are listed as left out.

## How to point a builder at it

1. Open the Grok.me app builder.
2. Paste the whole of `GROKME-PROMPT.md` as the first message. It is self-contained.
3. Give the builder the two data files. This repository is public, so the builder may fetch them once at build time from the raw files on the `main` branch:
     - `https://raw.githubusercontent.com/AdventureNLearn/CTA6/main/data/sources.csv`
     - `https://raw.githubusercontent.com/AdventureNLearn/CTA6/main/data/timeline.csv`
   The files may also be uploaded or pasted unchanged.
4. Ask the builder to run the checks in `TEST-PLAN.md` and report the results.
5. Do not publish the app until the owner says yes.

A developer working from a copy of this repository can follow `BUILD-PLAN.md` directly.

## Status

- Written in archive round 5. The data counts in this kit match that round: 379 sources and 244 milestones.
- When the data changes, the app must recount from the CSVs. It must not hard-code these numbers.
- Grok.me's own size limits and file rules are [UNKNOWN]. The kit sets its own limits in `BUILD-PLAN.md`.
