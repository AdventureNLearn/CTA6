# CTA6 - Reference Archive Build Kit: test plan

Run the smoke test first, then the checks. Expected numbers are for archive round 5. If the data has changed, recompute them from the CSVs, and the app must match the new numbers.

The app should expose read-only test hooks on `window`, as WNTR's Globe does (`js/app.js:1177`), for example `window.__CTA6.counts()`, `window.__CTA6.visibleIds()` and `window.__CTA6.state()`. Hooks only read. They never change data.

## Smoke test

Serve the app folder with any static server and open it in a headless browser at 1440×900, then at 390×844 with touch.

- [ ] The page loads with 0 console errors.
- [ ] Every network request goes to the app's own origin. No other host is contacted.
- [ ] The globe draws, with 57 country pins.
- [ ] The time bar says "All years".
- [ ] The "built in rounds, not complete" notice is visible.
- [ ] The stand-in toggle is off.
- [ ] Opening `#/entry/T001` shows T001 with its label, summary and citation.
- [ ] A screenshot is saved at each size, as WNTR's Globe does in `scripts/smoke.mjs`.

## Counts match the CSVs

Compute each number from the CSV files with a separate script (not the app's own code), then compare with the app.

| Check | Round 5 value |
|---|---|
| Sources loaded | 379 |
| Primary / secondary | 341 / 38 |
| `verified=yes` / `verified=no` | 349 / 30 |
| Labeled stand-ins (`label=secondary/unofficial`) | 8 |
| Milestones loaded | 244 |
| We-have-a-record / not-proven / people-disagree | 230 / 5 / 9 |
| Milestones with a second citation | 44 |
| Pinned milestones / countries with a pin | 229 / 57 |
| No location panel | 15 |
| Milestones up to and including 1945 | 9 |
| Earliest / latest milestone year | 1883 / 2026 |

- [ ] Every value matches.
- [ ] Each region, theme, era and label toggle count matches a count from the CSVs.

## Verified and labels are honest

- [ ] For every source, the app shows "Verified" if and only if `verified=yes`. Check all 379, not a sample.
- [ ] No milestone is shown with a "Verified" badge of its own.
- [ ] Every milestone shows its `confidence` label in words, and the label equals the CSV value.
- [ ] Every "People disagree" entry shows two citation cards.
- [ ] Label colours are not the only way the label is shown.

## Stand-ins

- [ ] The stand-in toggle is off on first load.
- [ ] After turning it on and reloading, it is off again.
- [ ] With it off, none of the 8 stand-in ids appears in lists, search results or region panels.
- [ ] With it on, each of the 8 shows the stand-in warning, "Not verified", and its `stands_in_for`, `author_or_publisher` and `access_date`.
- [ ] No stand-in is pinned.

## [UNKNOWN] and withheld values

- [ ] Every `[UNKNOWN]` in a displayed field is shown as `[UNKNOWN]`. Compare the rendered text of every entry with the CSV text.
- [ ] The withheld-URL source shows `[URL withheld: contains a private party's name]` as plain text, with no `href`.
- [ ] No milestone with `[UNKNOWN]` in `place` has a pin.

## No names beyond the data

- [ ] Collect every word that starts with a capital letter in the app's own files (HTML, CSS, JS), outside the data copies and vendor files. Every name found must be an interface word, a credit (Natural Earth, globe.gl, three.js, AdventureNLearn), or a value that is also in the CSVs.
- [ ] Scan the rendered text of every entry. It must be made only of CSV field text plus fixed interface labels.
- [ ] Search the app files for email addresses, phone numbers, home folder paths, API keys and tokens. Report only file and line, not the match. There must be no hits.
- [ ] No initials are expanded, and no person is linked anywhere.

## Privacy and requests

- [ ] No cookies are set.
- [ ] Local storage holds only interface choices. It never holds the stand-in toggle.
- [ ] The Content-Security-Policy allows only `'self'` (plus the host's own origin if required).
- [ ] No analytics or tracking script is present.
- [ ] Clicking a source link opens a new tab with `rel="noopener noreferrer"`. The app never fetches that URL itself.

## Places

- [ ] Every pin's coordinates equal the country label point in `DATA-CONTRACT.md` for its country.
- [ ] The 15 no-location ids equal the list in `DATA-CONTRACT.md`.
- [ ] Every pinned entry says "Pin shows the country, not the exact place."

## Features

- [ ] Layers: turning off each region, theme, era and label removes exactly those rows.
- [ ] Time slider: "All years" on load; scrubbing to 1945 shows 9 milestones; play stops at the end.
- [ ] Search: a milestone id finds exactly that row; `/` focuses search; keyboard list navigation works.
- [ ] Drilldown: World › Europe › France › an entry, and back with the breadcrumb. Global/UN opens as a list.
- [ ] Export CSV gives the filtered rows with unchanged columns and values.
- [ ] About and Sources and credits pages open from the footer and by hash.

## Phone, desktop and access

- [ ] 390×844 and 360×800 with touch: no overlap or overflow, controls at least 44 px, sheets open and close with ×, swipe, `Esc` and a tap on empty globe.
- [ ] 1536×864 and 1920×1080: panel, globe and time bar do not overlap.
- [ ] Keyboard only: every control is reachable and focus is visible.
- [ ] Reduced motion: no auto-rotate and no animated camera.
- [ ] An automated accessibility check reports no serious or critical issues.

## Limits

- [ ] No file over 5 MiB. Total under 20 MiB. Under 600 files.
- [ ] `data/sources.csv` and `data/timeline.csv` in the app are byte-identical to the archive copies (compare SHA-256).
- [ ] Lite mode works from `file://`.

## Report

List each check as PASS, FAIL or not run. A check that was not run is written as [UNKNOWN], with the reason.
