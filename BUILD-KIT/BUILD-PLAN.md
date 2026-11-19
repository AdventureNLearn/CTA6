# CTA6 - Reference Archive Build Kit: build plan

Follow the steps in order. Each step ends with acceptance checks. Do not start a step until the checks for the step before it pass.

Read `DATA-CONTRACT.md` and `SAFETY-AND-NEUTRALITY.md` first. They are part of every step.

## Step 0. Know what to borrow

The app reuses features from two public globe apps by the same owner. Each row names the file the feature was read from, in that app's own repository. Only features found in those files are listed.

### From SeaGlobe

| Feature | Where it is in SeaGlobe | Use in CTA6 |
|---|---|---|
| Globe engine: globe.gl 2.46.2, which includes three.js 0.187.0, vendored, no CDN | `web/vendor/README.md`, `web/vendor/VERSION-globe.gl.txt`; created in `web/js/app.js:172` with an atmosphere at `:175` | Same engine and same "no CDN" rule. |
| Classic scripts loaded by relative path, no app build step | script list at the end of `web/lite.html` (from `:148`) | Same. |
| Content-Security-Policy meta tag that lists every allowed host | `web/lite.html:6` | Same, but `'self'` only. |
| Lite tier for `?lite=1` or `file://`, with a pixel-ratio cap of 1.5 (lite) or 2 | `web/js/app.js:30`, `web/js/app.js:212` | Same. |
| Glass top bar: wordmark, era name and date, Focus chip with a clear button, status badges | `web/lite.html:18`, `:33`, `:35` | Top bar with era, year, Focus chip and a "Built in rounds" badge. |
| Side panel with tabs | `web/lite.html:42`, tabs at `:53` | Tabs: Entry, List, Layers, No location. |
| Info card: kicker, title, pills, facts list, notes, citation | `web/lite.html:61` | Entry panel (Step 7). |
| Layers tab with toggles, legend and evidence pills | `web/lite.html:87` | Layers tab (Step 5). |
| "Go deeper" tab of outbound links that are not bundled | `web/lite.html:103` | Not used. Links come only from the data. |
| Timeline bar: play, 1×/5×/20× speeds, era chips, era bands, year scrubber, active count | `web/lite.html:111` | Time slider (Step 6). |
| Catalogue panel: search box, filters, keyboard listbox, Export CSV made in the browser | `web/lite.html:130`; keys at `web/js/app.js:884`–`:893`; CSV at `web/js/app.js:967` | List tab and search (Step 9). |
| Keyboard: `/` search, `L` panel, `C` hide chrome, `Esc` clear focus | `web/js/app.js:690`–`:694` | Same keys, except `F` (follow camera), which has no use here. |
| Drilldown with a layer registry, levels and camera-altitude ranges, lazy packs, Natural Earth data, opt-in live layer with a health check and SKIP | `web/js/regions.js:1`–`:17`; region index at `web/data/regions/index.js` | Region › country › entry drilldown (Step 10). No live layer. |
| Encyclopedia with hash routes and Browse, A–Z, Timeline, Bibliography, Sources and licences, About tabs | `web/js/encyclopedia.js:1`–`:3`, `:19`, About view at `:218` | Hash routes for entries, sources and About (Step 11). |
| One shared entity and citation model with evidence labels and `[UNKNOWN]` gaps | `web/js/atlas.js:1`–`:4` | One data object built from the two CSVs (Step 2). |
| Phone layout at `max-width: 820px`: menu button, slide-up sheets, Esc closes | `web/js/mobile.js:1`–`:5`, `:79`; menu button `web/lite.html:127` | Same breakpoint and sheets (Step 12). |
| Reduced transparency support | `web/app.css:155` | Same. |
| Footer credits, owner credit, About link and version | `web/lite.html:108` | Same shape (Step 11). |
| Version check: one read-only request, silent on failure | `web/js/update.js:1`–`:3` | Not used. The app makes no outside requests. |
| Dismissible help note that remembers it was closed in local storage | `web/js/help.js:1`–`:20` | Pattern for the "built in rounds" notice. |
| Shared floating-window system with a saved layout | `web/js/windows.js:1`–`:4` | Optional. Not required. |

### From WNTR's Globe

| Feature | Where it is in WNTR's Globe | Use in CTA6 |
|---|---|---|
| MapLibre GL JS 5.24.1 with globe projection | `index.html:9`, `:119`; `js/app.js:856` | Not used. It loads from a CDN and needs outside tiles. |
| Clustered locators that expand on click | `js/app.js:602`–`:604`, `:694`–`:698` | Replaced by one count pin per country (Step 4). |
| "Not on the map" feed for rows whose place is `[UNKNOWN]` | `index.html:43`; `README.md` "How cases are drawn" | "No location" panel (Step 8). |
| Rule: never invent coordinates and never tighten source precision | `README.md`; badge text at `js/app.js:14` | Country-level pins only (Step 3). |
| Time slider that opens in "All years", with previous and next year buttons | `index.html:98`, `:106`; `js/app.js:455` | Same default (Step 6). |
| Layer panel of coloured layers with a default on/off state | `js/app.js:16`–`:22`; `index.html:30` | Layers tab (Step 5). |
| Status filter toggle | `index.html:34` | Record-label toggles (Step 5). |
| Case card: kicker, title, place, date, precision note, status gloss, summary, unknowns, gaps, sources, close button | `index.html:70` | Entry panel (Step 7). |
| Looks: Night, Schematic, Receipts, with a reset | `index.html:52`–`:56`, `:67`; `js/app.js:24` | Two looks: Night and Plain (high contrast). |
| Panel toggle buttons with `aria-expanded` | `index.html:27`, `:28` | Same. |
| Panels change layout at 900 px | `css/app.css:594`; `js/app.js:1125` | Mid-width rule (Step 12). |
| Reduced motion support | `js/app.js:262`; `css/app.css:663` | Same (Step 13). |
| Map attribution control and credits | `js/app.js:834`, `:1232`; `README.md` attribution list | Credits page (Step 11). |
| Data banner for example or placeholder data | `index.html:24` | Banner if the data fails to load or columns differ. |
| Star background | `index.html:13` | Optional decoration. |
| Test hooks on `window` and a headless smoke test with a 390 px phone shot | `js/app.js:1177`; `scripts/smoke.mjs:2`–`:4` | Test hooks and smoke test (`TEST-PLAN.md`). |

### Left out on purpose

- From SeaGlobe: moving vehicles, the sampler, routes, wind, night lights, satellites, radio, chat with a visitor's own key, the read-aloud control and the version check. They do not fit an archive reader, and some make outside requests.
- From WNTR's Globe: street-level view, 3D terrain, period maps and OpenStreetMap geocoding. Geocoding would create precise points, which this app must not do.

Acceptance checks:

- [ ] The builder can name the source file for every borrowed feature it uses.
- [ ] No feature from the "left out" list is in the app.

## Step 1. Set up the stack

- One static web app. Plain HTML, CSS and classic JavaScript files. No app build step and no server code.
- Globe: globe.gl 2.46.2 (MIT). Its browser build includes three.js. Copy the file into `vendor/` with its licence. Do not load it from a CDN at run time.
- If the builder cannot add a vendor file, it must stop and say so. Whether Grok.me allows vendored files is [UNKNOWN].
- All paths are relative, so the app runs from a static host, a local server and `file://`.
- Content-Security-Policy: `'self'` only for script-src, style-src, font-src, img-src and connect-src; object-src 'none'; base-uri 'self'; form-action 'none'. If the host requires one more origin for the app's own files, list only that origin.
- Folder layout:

```
index.html
app.css
js/app.js          (start-up, state, globe)
js/data.js         (load and check the data)
js/places.js       (place to country rule)
js/ui.js           (panels, list, search, filters)
js/mobile.js       (phone layout only)
data/sources.csv   (unchanged copy)
data/timeline.csv  (unchanged copy)
data/cta6-data.js  (generated copy of the two CSVs)
data/countries.js  (simplified Natural Earth shapes and label points)
vendor/globe.gl.min.js
vendor/LICENSE-globe.gl.txt
```

- Size limits, set by this kit because Grok.me's are [UNKNOWN]: 20 MiB total, 5 MiB per file, 600 files. Target under 6 MiB total.

Acceptance checks:

- [ ] `index.html` opens from a local static server with 0 console errors.
- [ ] The network log shows requests only to the app's own origin.
- [ ] No file is over 5 MiB and the total is under 20 MiB.

## Step 2. Load and check the data

- Ship `data/sources.csv` and `data/timeline.csv` byte for byte.
- Make `data/cta6-data.js` from them with a small script. It sets `window.CTA6_DATA = { round, sources: [...], timeline: [...] }`, one object per row, keys from the header. This lets the app run from `file://`. Do not hand-edit it.
- Parse with a real CSV parser. Fields can hold commas, quotes and line breaks.
- At start-up, check:
  - the columns match `DATA-CONTRACT.md` exactly, in order;
  - `id` values are unique in each file;
  - every `citation_source_id` and `citation_source_id_2` exists in sources;
  - `confidence`, `verified`, `tag`, `origin`, `era`, `region`, `theme` and `label` use only allowed values.
- If a check fails, show a banner: "The archive data did not pass its checks: {reason}." Still show what loaded, but do not hide or fix bad rows.
- Build one in-memory model: sources by id, milestones by id, and for each source the milestones that cite it.

Acceptance checks:

- [ ] Loaded counts equal the CSV row counts (379 sources, 244 milestones in round 5).
- [ ] `cta6-data.js` gives the same rows and values as parsing the CSVs.
- [ ] Changing a column name in a test copy shows the banner.
- [ ] No field value is changed on load except trimming whitespace.

## Step 3. Map places to countries

- Follow "Place mapping" in `DATA-CONTRACT.md` exactly.
- Make `data/countries.js` from Natural Earth 1:50m Admin 0 Countries. Keep only `ADM0_A3`, `NAME`, `LABEL_X`, `LABEL_Y` and simplified outlines. Join on `ADM0_A3`.
- Use the country table in `DATA-CONTRACT.md` for the name lookup. It holds the label points for every country in round 5.
- No geocoding, no city points and no outside lookup.

Acceptance checks:

- [ ] 229 milestones get a country, in 57 countries (round 5).
- [ ] The 15 rows listed in `DATA-CONTRACT.md` get no pin.
- [ ] Every pin's coordinates equal its country's label point.
- [ ] No coordinate in the app comes from anywhere but Natural Earth.

## Step 4. Draw the globe

- Full-window globe with a dark ocean, Natural Earth country outlines and a soft atmosphere. No satellite imagery is needed.
- One pin per country that has visible milestones. The pin shows the count. Its size grows with the count, with a cap so the United States pin does not cover its neighbours.
- Hover shows the country name and count. Click or tap opens the country panel (Step 10).
- Opening view: whole globe, slow auto-rotate that stops on the first touch and never runs under reduced motion.
- Two looks, from WNTR's Globe: Night (default) and Plain (high contrast). A reset button returns to Night.
- The canvas has `role="img"` and an `aria-label`, as in SeaGlobe (`web/lite.html:15`). All content is also reachable from the lists.

Acceptance checks:

- [ ] The globe renders with 57 country pins when all filters are on.
- [ ] Pin counts add up to the visible pinned milestones.
- [ ] Clicking a pin opens the right country.
- [ ] Auto-rotate is off when the browser asks for reduced motion.

## Step 5. Layers

The Layers tab has four groups of toggles and one separate toggle. Each group filters which milestones are visible. Pins and lists recount at once.

| Group | Toggles | Default |
|---|---|---|
| Region | the 10 regions | all on |
| Theme | the 6 themes, each with a colour in the legend | all on |
| Era | the 5 eras | all on |
| Record label | We have a record, Not proven, People disagree | all on |

- Each toggle shows its count, computed from the data.
- "All" and "None" buttons per group.
- Separate toggle: "Show secondary stand-ins (unofficial)". Off on every load. Never saved. When on, the 8 stand-in sources appear in lists, search and region panels, each with its warning. They are never pinned.
- The legend explains each record label in the words from `DATA-CONTRACT.md`.

Acceptance checks:

- [ ] Turning off a region removes its milestones from pins and lists, and the counts change to match.
- [ ] The stand-in toggle is off after every reload, including after it was turned on.
- [ ] With the toggle off, no stand-in appears anywhere except inside the warning on a citation card that cites one (none in round 5).

## Step 6. Time slider

- A bottom bar, as in SeaGlobe: play, speeds (1, 5 and 20 years per second), era chips, era bands and a year scrubber.
- It opens in "All years", as in WNTR's Globe.
- Moving the scrubber switches to "Up to {year}": milestones whose year is that year or earlier.
- Previous and next year buttons. Play steps year by year and stops at the last year.
- The range runs from the earliest to the latest milestone year in the data, read at load. Do not hard-code it.
- The year of a milestone is the first four digits of `date`. The rest of the date is shown as written, `[UNKNOWN]` parts included.
- Era chips jump to the end of that era and filter to it. Era bands use the five eras in order.
- A count shows how many milestones are visible.

Acceptance checks:

- [ ] On load the label says "All years" and all 244 milestones are counted.
- [ ] At year 1945, only milestones dated 1945 or earlier are visible.
- [ ] A date such as `1908-[UNKNOWN]-[UNKNOWN]` is placed in 1908 and shown with its `[UNKNOWN]` parts.
- [ ] Play stops at the last year and does not loop.

## Step 7. Entry panel

Opens when a milestone or a source is chosen. On a phone it is a bottom sheet.

For a milestone, in this order:

1. Record label badge in words, with its one-line meaning.
2. `what_happened` as the title.
3. Date and place, as written. If pinned: "Pin shows the country, not the exact place."
4. Region, theme and era tags.
5. `summary`.
6. Citation card for `citation_source_id`. A second card for `citation_source_id_2` if set. For "People disagree", head the two cards "One source" and "Another source". Do not rank them.
7. "Notes" fold, closed, if `notes` is set.
8. The milestone `id`.

Each citation card shows: title, issuing body, date, type, tag, origin, language, case citation if any, the link (or the withheld placeholder as plain text), accessed date, and the badge "Verified" or "Not verified". If the source is a stand-in, the stand-in warning comes first.

For a source, show the same card in full, then its `summary`, then "Cited by" with links to the milestones that cite it.

Close with ×, `Esc`, or a click on empty globe.

Acceptance checks:

- [ ] Every field shown matches the CSV text.
- [ ] A source with `verified=no` never shows "Verified".
- [ ] The withheld URL shows as plain text with no link.
- [ ] A "People disagree" entry shows both citations.

## Step 8. No location panel

- A tab and a button, "No location ({count})".
- It lists every milestone with no pin, with date, place as written, label badge and title.
- It follows the same filters and time slider as the globe.
- Choosing a row opens the entry panel. The globe does not move.

Acceptance checks:

- [ ] It lists 15 milestones with all filters on (round 5).
- [ ] Pinned count plus No location count equals the visible milestone count.

## Step 9. Search and list

- A List tab with every visible milestone, and a Sources view with every source (stand-ins only when their toggle is on).
- Type filter: build it from the `type` values present in the loaded sources. It filters the Sources view and source search results. All types are on by default.
- Search box. `/` focuses it. It matches all typed words, ignoring case and accents, against: `id`, `what_happened`, `title`, `summary`, `place`, `author_or_issuing_body`, `case_citation`, `type` and `language`. Wait 120 ms after typing before searching.
- Search never reaches outside the loaded data.
- Sort by date (oldest first, newest first) or by title.
- Keyboard: arrows, Home, End, PageUp, PageDown, Enter to open, Esc to close. The list is a `listbox` with `aria-activedescendant`, as in SeaGlobe.
- Export CSV of the filtered rows, made in the browser, with the original columns. Nothing is sent.

Acceptance checks:

- [ ] Searching a milestone id finds exactly that milestone.
- [ ] A search for a word only found in a stand-in finds nothing while the toggle is off.
- [ ] The type filter is built from the type values present, and turning a type off hides those sources from the Sources view and from source search results.
- [ ] Exported CSV rows match the source rows exactly.

## Step 10. Drilldown: region › country › entry

This is a new three-level design. SeaGlobe's drilldown goes world › country › state › county › town (`web/js/regions.js`). CTA6 has no finer place than country, so it stops at country.

- **World.** The opening view. Pins per country.
- **Region.** Chosen from a region list in the panel. The panel shows the region name, its milestone count and source count, and a list of countries with counts. The camera fits the box around that region's pinned countries. `Global/UN` has no map area: it opens as a list only, and the camera stays where it is.
- **Country.** Chosen from the region panel or by clicking a pin. The camera flies to the country point. The outline is highlighted. The panel lists that country's milestones by date.
- **Entry.** Chosen from the country list. The entry panel opens (Step 7).
- A breadcrumb shows the path, for example "World › Europe › France". Each part is a link back.
- List picks fly the camera. Clicking a country outline on the globe selects it and opens the panel.
- Regions come from the row's `region` field, not from the map. A country can appear in more than one region, for example the United States in North America and in Global/UN.
- Camera moves take about 2 seconds, and are instant under reduced motion.

Acceptance checks:

- [ ] World › Europe › France › an entry works with the mouse, the keyboard and on a phone.
- [ ] Global/UN opens a list and does not move the camera.
- [ ] Every breadcrumb link goes back to the right level.

## Step 11. About, notice, credits and links

- First-load notice: the "built in rounds" text from `SAFETY-AND-NEUTRALITY.md`. A footer line repeats it.
- About page at `#/about`: what CTA6 is, the three record labels, what `[UNKNOWN]` means, what a stand-in is, that pins are country-level, and that the app adds no commentary.
- Sources and credits page at `#/sources`: as listed in `SAFETY-AND-NEUTRALITY.md`.
- Hash routes, as in SeaGlobe: `#/entry/{milestone id}`, `#/source/{source id}`, `#/region/{region}`, `#/country/{ADM0_A3}`, `#/about`, `#/sources`. An unknown id shows "Not found in this round of the archive."
- Footer: "Built by AdventureNLearn — @AdventureNLearn" linked to https://x.com/AdventureNLearn, a link to About, and the round number.

Acceptance checks:

- [ ] The notice shows on first load in a fresh browser.
- [ ] `#/entry/T001` opens T001.
- [ ] The credits page names Natural Earth and the globe library with its licence.

## Step 12. Phone and tablet layout

- Phone at `max-width: 820px`, as in SeaGlobe `web/js/mobile.js`. Use the same media query in CSS and script, so the desktop is unchanged.
- Phone: a slim top strip (name, era, year), one bottom bar (play, scrubber, count, menu). The menu opens one slide-up sheet with the tabs. The entry opens as a bottom sheet. Close with ×, swipe down on the sheet header, `Esc`, or a tap on empty globe.
- No hover tooltips on touch. Every control is at least 44 px.
- From 821 px to 900 px the side panel becomes a short bottom sheet (WNTR's Globe changes its panels at 900 px).
- Desktop: side panel about 360 px on the right, time bar at the bottom leaving a gap for the panel.

Acceptance checks:

- [ ] At 390×844 and 360×800 nothing overlaps or overflows, and all controls are at least 44 px.
- [ ] At 1536×864 and 1920×1080 the desktop layout shows the panel, globe and time bar with no overlap.
- [ ] Tapping a pin on a phone opens the country sheet, and a list tap opens the entry sheet.

## Step 13. Accessibility

- All features work by keyboard. Focus is always visible.
- Text contrast is at least 4.5:1. Labels are never shown by colour alone.
- Honour `prefers-reduced-motion` (no auto-rotate, instant camera moves) and `prefers-reduced-transparency` (solid panels).
- `lang="en"` on the page. Source titles in other languages keep their text as written.
- Panels use headings in order. Toggles are real checkboxes with labels. Tabs use `role="tablist"`.
- Everything on the globe is also in a list, so screen-reader users reach every entry.

Acceptance checks:

- [ ] Tab order reaches every control. `Esc` closes the top panel.
- [ ] An automated accessibility check (for example axe) reports no serious or critical issues.
- [ ] With reduced motion on, nothing moves on its own.

## Step 14. Performance limits

- Pixel ratio capped at 2, or 1.5 in lite mode, as in SeaGlobe.
- Country outlines simplified so `data/countries.js` is under 1.5 MiB.
- At most one pin per country. No per-row globe objects.
- Lists show 200 rows at a time with "Show more".
- Search waits 120 ms after typing.
- First view in under 3 seconds on a mid-range laptop over a local server. The real time on Grok.me is [UNKNOWN]; report it.
- Stop rendering when the tab is hidden.

Acceptance checks:

- [ ] The size limits in Step 1 hold.
- [ ] Moving the scrubber across all years keeps the globe responsive.
- [ ] Lite mode loads and works from `file://`.

## Step 15. Test and report

- Run every check in `TEST-PLAN.md`.
- Report: what was built, the file list with sizes, the test results, any check not run (as [UNKNOWN]), and any place the builder could not follow this plan.
- Do not publish until the owner says yes.

Acceptance checks:

- [ ] All checks in `TEST-PLAN.md` pass or are reported as not run.
- [ ] The report lists every deviation from this plan.
