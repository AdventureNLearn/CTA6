# CTA6 - Reference Archive Build Kit: data contract

This file says what each field in the two CSV files means, which values are allowed, and how the app must show them. It follows `scripts/schema.py` and `scripts/check.py` in this repository. If this file and those scripts ever disagree, the scripts win, and this file must be fixed.

## The two files

| File | One row is | Rows in round 5 |
|---|---|---|
| `data/sources.csv` | one source: a law, treaty, resolution, ruling, report, history or study | 379 |
| `data/timeline.csv` | one milestone: a dated event backed by one or two sources | 244 |

Both files are UTF-8 CSV with a header row. Fields may contain commas, quotes and line breaks inside double quotes. Use a real CSV parser (RFC 4180). Do not split on commas.

The app must read the column names from the header and check them against the lists below. If the columns differ, stop and show an error. Do not guess.

## Display rules that apply everywhere

1. **Show text as written.** Do not rewrite, shorten into new claims, translate or "fix" any field. Trimming whitespace is fine.
2. **`[UNKNOWN]` stays `[UNKNOWN]`.** Show it exactly as it appears, styled so it is easy to see. Never fill it in, never guess a value, never hide it, and never look it up elsewhere. A date like `1908-[UNKNOWN]-[UNKNOWN]` is shown as is.
3. **Initials stay initials.** Private parties appear only as initials in the data. Show them that way. Never expand, search for or link a full name.
4. **Withheld URLs are never rebuilt.** One source has `url` = `[URL withheld: contains a private party's name]`. Show that text as plain text, not as a link. Never search for, guess or reconstruct the real URL.
5. **Record labels are shown honestly.** Every milestone shows its label in words. No label is upgraded, merged or hidden. See "Record labels" below.
6. **Verified means `verified=yes`.** A "Verified" badge appears only when the source row has `verified=yes`. Every other row shows "Not verified".
7. **Links are links, not fetches.** URLs open in a new tab with `rel="noopener noreferrer"`. The app never fetches, embeds or previews them.
8. **Counts come from the files.** Every count on screen is computed from the loaded rows.

## `data/sources.csv` fields

Columns, in this exact order (from `SOURCE_FIELDS` in `scripts/schema.py`):

| # | Field | Required | Meaning | Allowed values | Display rule |
|---|---|---|---|---|---|
| 1 | `id` | yes | Unique source id. | Unique text. Court cases may use a court-year-number form. | Show small, as a reference. Use it for links between entries. |
| 2 | `title` | yes | Title of the source as issued. | Text. | Entry heading. |
| 3 | `author_or_issuing_body` | yes | Who issued or wrote it. | Text. | Show under the title. |
| 4 | `date` | yes | Date of the source. | `YYYY-MM-DD`, `YYYY-MM`, `YYYY`, or `[UNKNOWN]`. | Show as written. A source with `[UNKNOWN]` date has no place on the time slider; it still appears in lists and search. |
| 5 | `type` | yes | Kind of document. | Free text (not checked against a list). Values in round 5: `statute`, `treaty`, `UN resolution`, `court record`, `commission report`, `agency history`, `scholarly`, `database`, `other`. | Show as a small tag. Build the type filter from values present. |
| 6 | `tag` | yes | Primary or secondary literature. | `primary`, `secondary`. | Show as a tag. |
| 7 | `origin` | yes | What kind of body the source comes from. | `government`, `international`, `academic`, `NGO`, `court`, `oversight`, `media`. | Show as a tag. |
| 8 | `era` | yes | Archive era. | See "Eras". | Era filter and era band. |
| 9 | `region` | yes | Archive region. | See "Regions". | Region filter and drilldown. |
| 10 | `theme` | yes | Archive theme. | See "Themes". | Theme filter. |
| 11 | `url` | yes | Link to the cited copy. | An `http(s)` URL, or the withheld placeholder in rule 4. | Link, except the placeholder, which is plain text. |
| 12 | `accessed` | yes | Date the archive accessed the URL. | Date text. | Show as "Accessed". |
| 13 | `verified` | yes | Whether the cited URL was fetched and matched. | `yes`, `no`. | Badge: "Verified" or "Not verified". |
| 14 | `notes` | no | Checking notes. | Text, may be blank. | Show in a "Notes" fold, closed by default. |
| 15 | `language` | yes | Language of the source text. | Language name, or `[UNKNOWN]`. | Show as written. |
| 16 | `case_citation` | no | Official case number or citation. | Text, may be blank. | Show when present. |
| 17 | `summary` | yes | Two to four sentences on what the item is and why it matters. | Text. May contain `[UNKNOWN]`. | Main body text. |
| 18 | `stands_in_for` | stand-ins only | The official source this unofficial copy stands in for. | A source id or a name. Blank on ordinary rows. | Show in the stand-in warning. If it is a source id that exists, link to that entry. |
| 19 | `author_or_publisher` | stand-ins only | Publisher of the unofficial copy. | Text. Blank on ordinary rows. | Show in the stand-in warning. |
| 20 | `access_date` | stand-ins only | Date the unofficial copy was accessed. | Date text. Blank on ordinary rows. | Show in the stand-in warning. |
| 21 | `label` | stand-ins only | Marks a labeled secondary stand-in. | `secondary/unofficial`, or blank. | Drives the stand-in toggle and warning. |

### Labeled secondary stand-ins

A row is a stand-in when `label` = `secondary/unofficial`. In round 5 there are 8. Every stand-in has `tag=secondary` and `verified=no`. Other `tag=secondary` rows are ordinary secondary literature. They are not stand-ins and are always shown.

- Stand-ins are hidden by default. A separate toggle, "Show secondary stand-ins (unofficial)", is off on every load. Its state is not saved.
- When shown, a stand-in carries a warning box at the top of its entry: "Secondary stand-in (unofficial). Not verified. It stands in for: {stands_in_for}. Published by {author_or_publisher}, accessed {access_date}. It is not proof of any milestone."
- A stand-in is never shown as verified, never counted as proof, and never pinned on the globe.
- No milestone cites a stand-in in round 5. If a later round adds one, the milestone still follows its own label, and its citation card shows the stand-in warning even when the toggle is off.

## `data/timeline.csv` fields

Columns, in this exact order (from `TIMELINE_FIELDS` in `scripts/schema.py`):

| # | Field | Required | Meaning | Allowed values | Display rule |
|---|---|---|---|---|---|
| 1 | `id` | yes | Unique milestone id. | `T` plus three digits. | Show small, as a reference. |
| 2 | `date` | yes | When it happened. | `YYYY-MM-DD`, `YYYY-MM`, `YYYY`, with any part after the year possibly `[UNKNOWN]`, for example `2001-10-[UNKNOWN]`. | Show as written. Use the first four digits as the year for the time slider. |
| 3 | `place` | yes | Where it happened, as recorded. | Text, for example `Strasbourg, France (Council of Europe)`, or text containing `[UNKNOWN]`. | Show as written. Mapped to a country pin by the rules below. |
| 4 | `what_happened` | yes | One-line statement of the event. | Text. | Entry heading. |
| 5 | `citation_source_id` | yes | The main source. | An `id` in `sources.csv`. | Show that source's citation card. |
| 6 | `citation_source_id_2` | no | A second source. | An `id` in `sources.csv`, or blank. Required when the label is `people-disagree`. | Show a second citation card. |
| 7 | `url` | yes | Link for the main source. | Same as that source's `url`. | Link. |
| 8 | `url_2` | when field 6 is set | Link for the second source. | Same as that source's `url`. | Link. |
| 9 | `confidence` | yes | The record label. | `we-have-a-record`, `not-proven`, `people-disagree`. | Label badge in words. See "Record labels". |
| 10 | `era` | yes | Archive era. | See "Eras". | Era filter and band. |
| 11 | `region` | yes | Archive region. | See "Regions". | Region filter and drilldown. |
| 12 | `theme` | yes | Archive theme. | See "Themes". | Theme filter and pin colour. |
| 13 | `notes` | no | Checking notes. | Text, may be blank. | "Notes" fold, closed by default. |
| 14 | `summary` | yes | Two to four sentences. | Text. May contain `[UNKNOWN]`. | Main body text. |

## Record labels

These are the only allowed values of `confidence`. The app shows the label text and this plain meaning, taken from the archive README:

| Label | Badge text | Meaning shown in the app |
|---|---|---|
| `we-have-a-record` | We have a record | The fact comes from a cited source that was fetched and checked. |
| `not-proven` | Not proven | The cited source could not be confirmed. The row is kept but is not treated as confirmed. |
| `people-disagree` | People disagree | The cited sources disagree. Both are linked. The archive does not choose between them. |

Round 5 counts: 230 we-have-a-record, 5 not-proven, 9 people-disagree.

Badges must not use green-for-good and red-for-bad colours that imply a judgment. Use three neutral, distinct colours plus the words. Never show the label by colour alone.

## Verified badge on a milestone

A milestone has no `verified` field. Its entry shows the badge of each cited source. Never show a milestone as "verified". Show its record label instead.

## Eras

From `ERAS` in `scripts/schema.py`, in time order:

`pre-1945`, `1945-1990`, `1990-2001`, `post-9/11 (2001-2014)`, `recent (2014-now)`.

The time slider shows these five as bands. A milestone's band comes from its `era` field, not from its date.

## Regions

From `REGIONS` in `scripts/schema.py`:

`North America`, `Europe`, `Middle East/North Africa`, `Sub-Saharan Africa`, `South Asia`, `East/Southeast Asia`, `Latin America`, `Russia/Central Asia`, `Oceania`, `Global/UN`.

These are archive groups, not map shapes. `Global/UN` has no area on the map. Its milestones are pinned by place like any other row.

## Themes

From `THEMES` and `THEME_DESCRIPTIONS` in `scripts/schema.py`:

| Theme | Description to show |
|---|---|
| `laws and treaties` | National statutes, international and regional treaties, and court rulings that interpret them. |
| `agencies` | Official histories and descriptions of national and international bodies. |
| `major operations` | Major attacks and state or coalition responses, at a public-record level only (no tactics). |
| `UN and international frameworks` | Security Council and General Assembly resolutions, sanctions regimes, and multilateral bodies. |
| `doctrine and strategy` | Published national and regional strategy documents. |
| `studies and evaluations` | Commission reports, inspector-general and oversight reviews, NGO reports, databases and scholarly studies. Listed only; this outline draws no conclusions from them. |

## Place mapping

The app pins milestones by country only. It never pins a city, a building or any precise point. Sources are not pinned. They are reached through milestones, lists and search.

### Rule

1. If `place` contains `[UNKNOWN]`: no pin.
2. If `place` is exactly `Global` or `Organization of American States`: no pin.
3. If `place` names more than one country by exact match on a country name from the table below (not a substring): no pin. A name that only contains another name as a substring, such as Northern Ireland, does not count as Ireland. In round 5 this is one row, matched in full: `Vienna, Austria and New York, United States`.
4. Otherwise remove any text in round brackets, split on commas, and take the last part. Look it up in the country table below. If it is found, pin the milestone at that country's point.
5. If it is not in the table: no pin. Add the row to the "No location" panel and log a build warning. Do not guess.

Every row with no pin is listed in the "No location" panel, with its place text shown as written.

Round 5 result: 229 milestones pinned in 57 countries, and 15 in the "No location" panel: T019, T029, T045, T057, T079, T134, T151, T158, T169, T196, T197, T198, T224, T239, T241.

### Country points

Points are the `LABEL_Y` (latitude) and `LABEL_X` (longitude) fields of Natural Earth 1:50m Admin 0 Countries (`ne_50m_admin_0_countries`, public domain, naturalearthdata.com; GeoJSON from the `nvkelso/natural-earth-vector` repository on GitHub, whose `VERSION` file read `5.2.0-pre` on 19 November 2026). A label point is a representative point inside the country. It is not the place where the event happened. Values below are rounded to two decimals.

Join on `ADM0_A3`, not `ISO_A3`. In this Natural Earth release `ISO_A3` is `-99` for France and Norway.

Use 1:50m, not 1:110m. The 1:110m file has no Singapore, Maldives or Barbados.

| Name in `place` | ADM0_A3 | Lat | Lon |
|---|---|---|---|
| Algeria | DZA | 27.40 | 2.81 |
| Argentina | ARG | -33.50 | -64.17 |
| Australia | AUS | -24.13 | 134.05 |
| Bangladesh | BGD | 24.21 | 89.68 |
| Barbados | BRB | 13.16 | -59.57 |
| Belgium | BEL | 50.79 | 4.80 |
| Brazil | BRA | -12.10 | -49.56 |
| Canada | CAN | 60.32 | -101.91 |
| Chile | CHL | -38.15 | -72.32 |
| China | CHN | 32.50 | 106.34 |
| Colombia | COL | 3.37 | -73.17 |
| Costa Rica | CRI | 10.07 | -84.08 |
| Côte d'Ivoire | CIV | 7.49 | -5.57 |
| Egypt | EGY | 26.19 | 29.45 |
| France | FRA | 46.70 | 2.55 |
| Germany | DEU | 50.96 | 9.68 |
| India | IND | 22.69 | 79.36 |
| Indonesia | IDN | -0.95 | 101.89 |
| Ireland | IRL | 53.08 | -7.80 |
| Israel | ISR | 30.91 | 34.85 |
| Italy | ITA | 44.73 | 11.08 |
| Japan | JPN | 36.14 | 138.44 |
| Kazakhstan | KAZ | 49.05 | 68.69 |
| Kenya | KEN | 0.55 | 37.91 |
| Kyrgyzstan | KGZ | 41.67 | 74.53 |
| Luxembourg | LUX | 49.73 | 6.08 |
| Malaysia | MYS | 2.53 | 113.84 |
| Maldives | MDV | 4.17 | 73.51 |
| Mali | MLI | 18.69 | -2.04 |
| Mauritania | MRT | 19.59 | -9.74 |
| Mexico | MEX | 23.92 | -102.29 |
| Morocco | MAR | 31.65 | -7.19 |
| Nepal | NPL | 28.30 | 83.64 |
| Netherlands | NLD | 52.42 | 5.61 |
| New Zealand | NZL | -39.76 | 172.79 |
| Nigeria | NGA | 9.44 | 7.50 |
| Norway | NOR | 61.36 | 9.68 |
| Pakistan | PAK | 29.33 | 68.55 |
| Papua New Guinea | PNG | -5.70 | 143.91 |
| Peru | PER | -12.98 | -72.90 |
| Philippines | PHL | 11.20 | 122.47 |
| Poland | POL | 51.99 | 19.49 |
| Qatar | QAT | 25.24 | 51.14 |
| Republic of Korea | KOR | 36.38 | 128.13 |
| Russia | RUS | 58.25 | 44.69 |
| Russian Federation | RUS | 58.25 | 44.69 |
| Saudi Arabia | SAU | 23.81 | 44.70 |
| Singapore | SGP | 1.37 | 103.82 |
| South Africa | ZAF | -29.71 | 23.67 |
| Spain | ESP | 40.09 | -3.46 |
| Sri Lanka | LKA | 7.58 | 80.70 |
| Switzerland | CHE | 46.72 | 7.46 |
| Tunisia | TUN | 33.69 | 9.01 |
| Turkmenistan | TKM | 39.86 | 58.68 |
| Türkiye | TUR | 39.35 | 34.51 |
| United Kingdom | GBR | 54.40 | -2.12 |
| United States | USA | 39.54 | -97.48 |
| Uzbekistan | UZB | 41.69 | 64.01 |

`Russia` and `Russian Federation` both map to RUS. The app shows the `place` text from the data, not the Natural Earth country name.

The panel for a pinned milestone says: "Pin shows the country, not the exact place."

## Counts to check (round 5)

These are for testing only. The app computes them; it does not hard-code them.

- Sources: 379. Primary 341, secondary 38. Verified yes 349, no 30. Labeled stand-ins 8.
- Milestones: 244. We-have-a-record 230, not-proven 5, people-disagree 9.
- Milestones with a second citation: 44.
- Pinned milestones: 229 in 57 countries. No location: 15.
- Summaries containing `[UNKNOWN]`: 115 sources and 50 milestones.
- Sources with a withheld URL: 1.
