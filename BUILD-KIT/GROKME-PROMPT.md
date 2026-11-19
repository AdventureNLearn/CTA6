# CTA6 - Reference Archive Build Kit: Grok.me prompt

Paste everything below the line into the Grok.me app builder as one message. Then give it the two CSV files (see "Data"). This prompt is self-contained. The builder does not need to read the CTA6 repository.

---

Build a static globe app called **CTA6 Reference Archive**. It is a neutral reader for the CTA6 counterterrorism reference archive. Follow this prompt exactly. Do not redesign it, add features, add commentary, or add any outside service, analytics, key or secret. If a step cannot be done, stop and say which step and why.

## Data

The app reads two CSV files and nothing else: `sources.csv` (379 rows in round 5) and `timeline.csv` (244 rows). The CTA6 repository is public. The owner may upload or paste the files; if they are not provided, fetch them once at build time from:

- https://raw.githubusercontent.com/AdventureNLearn/CTA6/main/data/sources.csv
- https://raw.githubusercontent.com/AdventureNLearn/CTA6/main/data/timeline.csv

If neither works, stop and ask for the files. Never invent rows.

Ship both CSVs unchanged. Also generate `data/cta6-data.js` from them (`window.CTA6_DATA = {round: 5, sources: [...], timeline: [...]}`) so the app runs from `file://`. Use a real CSV parser: fields hold commas, quotes and line breaks. Check at load that the columns match exactly, ids are unique, every citation id exists in sources, and the fields below use only allowed values. On failure show a banner with the reason. Never fix or drop rows.

**sources.csv columns, in order:** id, title, author_or_issuing_body, date, type, tag, origin, era, region, theme, url, accessed, verified, notes, language, case_citation, summary, stands_in_for, author_or_publisher, access_date, label. Optional: notes, case_citation, and the last four (filled only on stand-ins).

**timeline.csv columns, in order:** id, date, place, what_happened, citation_source_id, citation_source_id_2, url, url_2, confidence, era, region, theme, notes, summary. Optional: citation_source_id_2, url_2, notes.

**Allowed values:**
- tag: primary, secondary. origin: government, international, academic, NGO, court, oversight, media. verified: yes, no. label: secondary/unofficial or blank.
- confidence (the record label): we-have-a-record, not-proven, people-disagree.
- era, in order: pre-1945, 1945-1990, 1990-2001, post-9/11 (2001-2014), recent (2014-now).
- region: North America, Europe, Middle East/North Africa, Sub-Saharan Africa, South Asia, East/Southeast Asia, Latin America, Russia/Central Asia, Oceania, Global/UN. These are archive groups, not map shapes.
- theme: laws and treaties, agencies, major operations, UN and international frameworks, doctrine and strategy, studies and evaluations.
- type is free text. Build its filter from the values present.
- Dates are YYYY-MM-DD, YYYY-MM or YYYY. Any part may be [UNKNOWN] (for example 1908-[UNKNOWN]-[UNKNOWN]); a source date may be just [UNKNOWN].

## Display rules (never break these)

1. Show every field as written. Do not rewrite, translate or summarise.
2. **[UNKNOWN] stays [UNKNOWN].** Show it, styled so it is easy to see. Never fill it in or look it up.
3. **Initials stay initials.** Never expand, search for or link a name.
4. **Withheld URL:** one source has url = `[URL withheld: contains a private party's name]`. Show it as plain text, not a link. Never reconstruct it.
5. **Record labels in words**, with neutral colours (no green-good, red-bad): "We have a record" = the fact comes from a cited source that was fetched and checked. "Not proven" = the cited source could not be confirmed; kept but not treated as confirmed. "People disagree" = sources disagree; both are linked; the archive does not choose.
6. **"Verified" badge only when verified=yes.** Otherwise "Not verified". A milestone has no badge of its own; show its label.
7. Links open in a new tab with rel="noopener noreferrer". The app never fetches them.
8. All counts are computed from the data.

## Stand-ins

Rows with label=secondary/unofficial (8 in round 5) are unofficial stand-ins. A separate Layers toggle, "Show secondary stand-ins (unofficial)", is **off on every load and never saved**. When off, stand-ins appear nowhere. When on, they appear in lists and search with a warning at the top: "Secondary stand-in (unofficial). Not verified. It stands in for: {stands_in_for}. Published by {author_or_publisher}, accessed {access_date}. It is not proof of any milestone." Never pin them. Other tag=secondary rows are ordinary and always shown. Milestones never cite a stand-in as proof. No milestone cites a stand-in in round 5. If a later round adds one, the milestone still follows its own label, and its citation card shows the stand-in warning even when the toggle is off.

## Places (country pins only)

Never pin a city, building or precise point. No geocoding.

1. place contains [UNKNOWN] → no pin.
2. place is "Global" or "Organization of American States" → no pin.
3. place is "Vienna, Austria and New York, United States" (two countries) → no pin.
4. Else remove text in round brackets, split on commas, take the last part, look it up below, and pin at that point.
5. Not found → no pin, and log a warning.

Unpinned rows go in a **No location** panel (15 in round 5). Pinned entries say: "Pin shows the country, not the exact place." Show the place text from the data, not the map's country name.

Country points (name in place, ADM0_A3, lat,lon). They are LABEL_Y and LABEL_X from Natural Earth 1:50m Admin 0 Countries (public domain):

Algeria DZA 27.40,2.81; Argentina ARG -33.50,-64.17; Australia AUS -24.13,134.05; Bangladesh BGD 24.21,89.68; Barbados BRB 13.16,-59.57; Belgium BEL 50.79,4.80; Brazil BRA -12.10,-49.56; Canada CAN 60.32,-101.91; Chile CHL -38.15,-72.32; China CHN 32.50,106.34; Colombia COL 3.37,-73.17; Costa Rica CRI 10.07,-84.08; Côte d'Ivoire CIV 7.49,-5.57; Egypt EGY 26.19,29.45; France FRA 46.70,2.55; Germany DEU 50.96,9.68; India IND 22.69,79.36; Indonesia IDN -0.95,101.89; Ireland IRL 53.08,-7.80; Israel ISR 30.91,34.85; Italy ITA 44.73,11.08; Japan JPN 36.14,138.44; Kazakhstan KAZ 49.05,68.69; Kenya KEN 0.55,37.91; Kyrgyzstan KGZ 41.67,74.53; Luxembourg LUX 49.73,6.08; Malaysia MYS 2.53,113.84; Maldives MDV 4.17,73.51; Mali MLI 18.69,-2.04; Mauritania MRT 19.59,-9.74; Mexico MEX 23.92,-102.29; Morocco MAR 31.65,-7.19; Nepal NPL 28.30,83.64; Netherlands NLD 52.42,5.61; New Zealand NZL -39.76,172.79; Nigeria NGA 9.44,7.50; Norway NOR 61.36,9.68; Pakistan PAK 29.33,68.55; Papua New Guinea PNG -5.70,143.91; Peru PER -12.98,-72.90; Philippines PHL 11.20,122.47; Poland POL 51.99,19.49; Qatar QAT 25.24,51.14; Republic of Korea KOR 36.38,128.13; Russia RUS 58.25,44.69; Russian Federation RUS 58.25,44.69; Saudi Arabia SAU 23.81,44.70; Singapore SGP 1.37,103.82; South Africa ZAF -29.71,23.67; Spain ESP 40.09,-3.46; Sri Lanka LKA 7.58,80.70; Switzerland CHE 46.72,7.46; Tunisia TUN 33.69,9.01; Turkmenistan TKM 39.86,58.68; Türkiye TUR 39.35,34.51; United Kingdom GBR 54.40,-2.12; United States USA 39.54,-97.48; Uzbekistan UZB 41.69,64.01

For outlines, use Natural Earth `ne_50m_admin_0_countries` (not 1:110m, which lacks Singapore, Maldives and Barbados), from https://github.com/nvkelso/natural-earth-vector at build time. Join on ADM0_A3 (ISO_A3 is -99 for France and Norway). Simplify to under 1.5 MiB and bundle it.

## Stack

- Static HTML, CSS and classic JavaScript. No server, no app build step, relative paths only.
- Globe: globe.gl 2.46.2 (MIT; its browser build includes three.js), copied into `vendor/` with its licence. No CDN at run time.
- Content-Security-Policy: `'self'` only for script-src, style-src, font-src, img-src and connect-src; object-src 'none'; base-uri 'self'; form-action 'none'.
- `?lite=1` or `file://` → lite mode. Pixel ratio cap 2 (lite 1.5).

## What to build

- **Globe:** full window, dark ocean, country outlines, soft atmosphere. One pin per country with visible milestones, showing the count, size capped. Hover shows country and count. Slow auto-rotate that stops on touch and is off under reduced motion. Looks: Night (default) and Plain (high contrast), with reset. Stop rendering when the tab is hidden.
- **Top bar:** name, current era and year, a Focus chip naming active filters (× or Esc clears), and a "Built in rounds" badge.
- **Side panel (~360 px, right), tabs:** Entry, List, Layers, No location.
- **Layers:** toggle groups for the 10 regions, 6 themes (each with a legend colour), 5 eras and 3 record labels, all on by default, each with a count and All/None buttons. Plus the stand-in toggle. Pins and lists recount at once.
- **Time slider (bottom bar):** opens in "All years". Scrubbing switches to "Up to {year}" (year = first four digits of date). Play at 1, 5 or 20 years per second; stops at the end. Previous/next year buttons. Era chips and five era bands. Range read from the data (1883 to 2026 in round 5). Visible count.
- **Entry panel (milestone):** label badge and meaning; what_happened as title; date and place as written; region, theme, era tags; summary; a citation card for each cited source (for people-disagree, "One source" and "Another source", unranked); notes in a closed fold; the id. **Citation card:** title, issuing body, date, type, tag, origin, language, case citation, link or withheld text, accessed date, Verified/Not verified badge. **Source entry:** the card, summary and "Cited by" links.
- **No location panel:** every unpinned milestone with date, place, label and title; follows filters and slider.
- **Search and list:** `/` focuses search. Match all words, ignoring case and accents, in id, what_happened, title, summary, place, author_or_issuing_body, case_citation, type and language. 120 ms debounce. Sort by date or title. Listbox with arrow, Home, End, PageUp, PageDown, Enter and Esc keys. Export CSV of filtered rows, made in the browser. 200 rows at a time with "Show more". Type filter: build it from the type values present in the loaded sources; it filters the Sources view and source search results, with all types on by default.
- **Drilldown:** World › Region › Country › Entry with a breadcrumb. A region list fits the camera to that region's pinned countries; Global/UN opens as a list only and does not move the camera. A country (from a list or a pin) flies the camera to its point, highlights it and lists its milestones. Regions come from the row's region field; a country can be in more than one region.
- **Hash routes:** #/entry/{id}, #/source/{id}, #/region/{name}, #/country/{ADM0_A3}, #/about, #/sources. Unknown id → "Not found in this round of the archive."
- **Notice on first load and in the footer:** "CTA6 is built in rounds. This is round 5. It is not a complete history, and it does not claim to be one. Gaps are marked [UNKNOWN]." It can be closed; the footer line stays.
- **About:** what CTA6 is, the three labels, what [UNKNOWN] means, what a stand-in is, that pins are country-level, and that the app adds no commentary.
- **Sources and credits:** the CTA6 archive files and round; "Made with Natural Earth. Free vector and raster map data @ naturalearthdata.com."; globe.gl and three.js (MIT); "Borders are from Natural Earth and do not imply any position on disputed boundaries."; each source belongs to its publisher.
- **Footer:** Built by AdventureNLearn — [@AdventureNLearn](https://x.com/AdventureNLearn), About link, round number.
- **Phone (max-width 820px, same query in CSS and JS):** slim top strip, one bottom bar (play, scrubber, count, menu), menu opens one slide-up sheet with the tabs, entries open as a bottom sheet; close with ×, swipe down, Esc or a tap on empty globe; 44 px targets; no hover tooltips. 821–900 px: side panel becomes a short bottom sheet.
- **Accessibility:** full keyboard use, visible focus, contrast at least 4.5:1, labels never by colour alone, prefers-reduced-motion and prefers-reduced-transparency honoured, canvas role="img" with a label, everything on the globe also in a list.
- **Test hooks (read only):** window.__CTA6.counts(), .visibleIds(), .state().

## Neutrality and privacy

No commentary, rankings, "key takeaways", AI text, chat, images of violence, or tactics. No analytics, cookies, accounts, forms, third-party fonts or widgets. Local storage holds interface choices only, never the stand-in toggle. No requests at run time except the app's own files. If Grok.me adds analytics by default, turn it off or report it.

## Limits (self-imposed)

Grok.me's own size limits are [UNKNOWN]. Caps: 20 MiB total, 5 MiB per file, 600 files. Target under 6 MiB.

## Checks before you report

- 0 console errors; requests only to the app's own origin.
- Counts: sources 379 (primary 341, secondary 38; verified yes 349, no 30; stand-ins 8); milestones 244 (we-have-a-record 230, not-proven 5, people-disagree 9); 44 with a second citation; 229 pinned in 57 countries; 15 in No location (T019, T029, T045, T057, T079, T134, T151, T158, T169, T196, T197, T198, T224, T239, T241); 9 milestones up to 1945.
- "Verified" shows if and only if verified=yes, for all 379 sources.
- Stand-in toggle off on load and after reload; with it off, no stand-in id appears anywhere.
- Every [UNKNOWN] is shown as is; the withheld URL has no link; no names beyond the data; no emails, keys or tokens in app files.
- The shipped CSVs are byte-identical to the ones given.
- Phone 390×844 and 360×800, desktop 1536×864 and 1920×1080: no overlap.
- `#/entry/T001` opens T001. World › Europe › France › entry works.

## Report back

What you built, the file list with sizes, each check as PASS, FAIL or [UNKNOWN] (not run, with the reason), and any place you could not follow this prompt. Do not publish until the owner says yes.

## Gaps marked [UNKNOWN]

- Grok.me's size limits and whether it allows vendored library files.
- Whether Grok.me adds analytics or cookies by default.
- Load time on Grok.me.
