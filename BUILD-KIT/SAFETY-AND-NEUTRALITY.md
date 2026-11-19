# CTA6 - Reference Archive Build Kit: safety and neutrality

These rules are part of the build. A build that breaks one of them is not done.

## Neutral and objective

- The app shows the archive. It does not interpret it.
- Use the archive's own text for titles, summaries, places and labels. Do not add commentary, opinions, rankings, scores, "key takeaways" or editorial headlines.
- Do not adopt any government's or organisation's label as the app's own voice. Words such as "terrorist" appear only where they are in the data, for example in an official title.
- Where sources disagree, show both, with the label "People disagree". Do not choose a side, and do not order them to suggest a winner. Show the main citation first and the second citation next, as in the data.
- Do not rank countries, regions or eras. Counts are shown as plain numbers, not as "most" or "worst" lists.
- Record-label colours are neutral. Do not use green for good or red for bad. Always show the label in words.
- Do not generate new text with AI at run time. No chat, no "explain this", no generated summaries. The app has no AI features.
- Do not show violent imagery, attack footage or maps of attack sites. The app has no images beyond the globe, country outlines and interface icons.
- Pins sit at a country point. The entry says "Pin shows the country, not the exact place."

## Built in rounds, not complete

- A notice shows on first load and stays reachable from the About page and the footer.
- Text: "CTA6 is built in rounds. This is round {N}. It is not a complete history, and it does not claim to be one. Gaps are marked [UNKNOWN]."
- `{N}` is the round number the owner states at build time. In this kit it is 5. If the round is not stated, show `[UNKNOWN]`.
- The notice can be closed, but it must not be hidden for good. If the app remembers that it was closed, it does so only in the visitor's own browser (local storage), and the footer line stays.

## No user data by default

- No analytics, tracking pixels, heatmaps, session replay or error-reporting services.
- No cookies. No accounts, sign-in, comments, uploads, forms or contact fields.
- No third-party fonts, tag managers or social widgets.
- The app may store only interface choices (for example "notice closed" or panel layout) in the visitor's own browser. It sends nothing anywhere.
- The stand-in toggle is never saved. It is off on every load.
- If the host adds its own analytics, turn it off. If it cannot be turned off, say so in the build report. Whether Grok.me adds any by default is [UNKNOWN].

## No keys or secrets

- No API key, token or password in any client file, setting or URL.
- No paid or keyed map, search or AI service.
- The globe draws from files shipped with the app. Base layers are Natural Earth country shapes, bundled.
- At run time the app makes no network request except to its own files. Outbound links open only when the visitor clicks them.
- Add a Content-Security-Policy that allows only `'self'` for script-src, style-src, font-src, img-src and connect-src, plus `object-src 'none'`, `base-uri 'self'` and `form-action 'none'`. If the host requires one more origin for the app's own files, list only that origin.

## Privacy of people in the data

- Show only names that are in the data. Public officials, states and organisations are named there. Private parties appear only as initials.
- Never expand initials, link a person, or search for a name.
- Never rebuild a withheld URL. Show the placeholder as plain text.
- Never pin a precise location. Country points only.
- Do not add people, photos, addresses or any personal detail from outside the data.

## Credit sources

- Every entry shows its citation: title, issuing body, date, link (or the withheld placeholder), accessed date and verified badge.
- A "Sources and credits" page lists:
  - CTA6 archive: `data/sources.csv` and `data/timeline.csv`, with the round number.
  - Country shapes and points: "Made with Natural Earth. Free vector and raster map data @ naturalearthdata.com." (public domain).
  - The globe library and its licence (for example globe.gl and three.js, MIT), if used.
  - A line that the app is a reader for the archive and that each source belongs to its publisher.
- Country borders come from Natural Earth. The page says: "Borders are from Natural Earth and do not imply any position on disputed boundaries."
- The footer carries the owner's existing credit line, as used in SeaGlobe: "Built by AdventureNLearn — @AdventureNLearn" (linked to https://x.com/AdventureNLearn).

## Content limits

- "Major operations" stays at a public-record level, as in the data. The app adds no tactics, methods or operational detail.
- Outbound links go only to the URLs already in the data.
- The app makes no claim beyond the data, including no claim of completeness, accuracy beyond the labels, or endorsement by any source.
