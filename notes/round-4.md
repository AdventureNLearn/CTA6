# CTA6 round 4: notes

Round 4 adds sources and timeline rows gathered in pass 4, applies the pass 4 corrections that are backed by fetched official copies or by OCR of a scanned original, and fills some `[UNKNOWN]` marks in existing summaries. Pass 4 working files and page captures were not copied into this repository. This archive is not complete.

Accessed: 2026-11-19. The pass 4 gathering record is the basis for the counts, retries and remaining gaps below.

## What was added

- 7 sources appended to `data/sources.csv`, all `verified=yes`: Mexico's 14 March 2014 Diario Oficial decree (Chamber of Deputies copy); three National Human Rights Commission of Korea records (2001, 2002, 2026); Pakistan's Anti-terrorism (Amendment) Act, 2020 (Gazette, Senate-hosted copy); NACTA's page on the 2014 National Action Plan; and an official Peruvian government Spanish copy of the Inter-American Convention against Terrorism (PE-GOB-CIAT2002-ES). PE-GOB-CIAT2002-ES is a separate source, linked to OAS-CICTE2002; it does not replace that entry, whose OAS page is still unverified.
- 6 timeline rows, T231 to T236, appended to `data/timeline.csv`. All are `we-have-a-record`, and each cites a source added in this round.
- No source id or URL duplicated an existing row.

After the official-source merge the archive had 368 sources (338 primary, 30 secondary; 331 verified, 37 not) and 236 timeline rows (219 we-have-a-record, 8 not-proven, 9 people-disagree). After the later addition of 8 labeled secondary stand-ins, it has 376 sources (338 primary, 38 secondary; 331 verified, 45 not) and the same 236 timeline rows.

## Corrections applied and skipped (C071–C087)

Each correction was applied only where the fetched text or the OCR supports it, except as noted.

- **C071–C073 (US-NSCT2018).** The cited dni.gov URL was gone (404). It was replaced by the White House archive copy at https://trumpwhitehouse.archives.gov/wp-content/uploads/2018/10/NSCT.pdf, which was fetched (HTTP 200) and matches a Wayback Machine capture of the original dni.gov URL (https://web.archive.org/web/20191222211347/https://www.dni.gov/files/NCTC/documents/news_documents/NSCT.pdf). `verified` moves to yes. The Wayback capture is recorded in the notes.
- **C074–C075 (CRS-R43983).** The cited crsreports.congress.gov URL still blocks scripted access. It was replaced by the congress.gov official copy of the same report (R43983, "Updated April 14, 2015"), fetched HTTP 200. `verified` moves to yes.
- **C076–C077 (COE-ECST1977) and C078–C079 (COE-CPT2005).** The cited Council of Europe treaty-office pages still return 403. They were replaced by the official rm.coe.int PDFs of the same treaties, both fetched HTTP 200. `verified` moves to yes.
- **C080–C081 (T015) and C083–C084 (T085).** The milestone URLs follow the official PDFs. The "source page not machine-readable" wording is dropped. Confidence stays `not-proven`.
- **C082 and C085 were skipped.** Raising T015 or T085 to `we-have-a-record` was not applied, because the words "opened for signature" rest on an explanatory report that was seen only in a search listing and has not been read. A note on each row records that the report has been identified but not yet read.
- **C086–C087 (G5S-CONV2014-WA).** The cited PDF is an image-only scan. OCR of that scanned original supports the title, the five member states, article 1 (creation of the G5 Sahel), article 3 (seat initially in Nouakchott), article 18 (entry into force after three ratifications) and the closing "Fait à Nouakchott, le 19 décembre 2014" with signature blocks for the five heads of state. `verified` moves to yes; the notes say "verified by OCR of scanned original".
- **T045** was not changed. The adoption-date disagreement remains recorded as T145.

Summaries of the corrected rows were rewritten to match these decisions. The body or provisions of US-NSCT2018, CRS-R43983, COE-ECST1977 and COE-CPT2005 remain `[UNKNOWN]` where they have not been summarized.

## Summary fills

Existing summaries and a few date or place fields were updated from quotes already in the captures:

- Dates of five UN Special Rapporteur country reports (SR-EGY-2009, SR-TUN-2010, SR-PER-2010, SR-CHL-2014, SR-SAU-2018), taken from the "Distr.: General" lines.
- The Human Rights Commission of Sri Lanka 2020 prison-study publication date and place (T225, HRCSL-PRISON-2020): 25 November 2020, Colombo.
- G5 Sahel content (G5S-CONV2014-WA, T217), from the OCR.
- Page-updated dates shown on NATO-ART5, AU-NSLEG and US-DHS-CREATION.
- The attack named in UNSC 1595.
- The holding in R. v. Bush, 542 U.S. 466, according to the syllabus (USSC-2004-542-466, T075).
- EG-NCHR-R18-EN: the publication day and month remain `[UNKNOWN]`; the wording now notes the report covers 1 July 2024 to 30 June 2025 and mentions an event on 2 July 2025.

After these fills, and the new rows, 196 of 604 source and milestone summaries still contain at least one `[UNKNOWN]` mark (213 marks in all). Most remaining marks are unsummarized provisions or findings, or undated web pages whose captures show no date.

## Combined after round 4

| region | sources (361 + 7 = 368) | timeline (230 + 6 = 236) |
|---|---:|---:|
| Global/UN | 67 | 40 |
| Europe | 67 | 49 |
| North America | 45 | 33 |
| Middle East/North Africa | 36 | 21 |
| Sub-Saharan Africa | 35 | 22 |
| South Asia | 35 | 17 |
| East/Southeast Asia | 27 | 18 |
| Latin America | 27 | 18 |
| Russia/Central Asia | 17 | 12 |
| Oceania | 12 | 6 |

Global/UN, Europe and North America still hold 179 of 368 sources (49%) and 122 of 236 timeline rows (52%).

## Retries still blocked

These official sources were tried again in pass 4 and remain `[UNKNOWN]` or `verified=no` at the cited URL:

- OAS / IACHR (OAS-CICTE2002, OAS-CICTE, IACHR-2002-TERR-ES, IACHR-2002-TERR-EN): HTTP 503, maintenance. A Peruvian-government copy of the Convention text is now a separate verified source.
- Kenya POTA (KE-POTA2012, KE-POTA2012-KL): bot check or 403.
- UN Commission on Human Rights resolution 2005/80 (CHR-2005-80): the UN document site served only a language selector or a loader page.
- New Zealand legislation (NZ-TSA2002, NZ-CTLA2021): empty responses or timeouts.
- Kazakhstan law (KZ-LAW416-1999): Adilet served a JavaScript stub.
- Tajikistan law (TJ-LAW845-1999): ncz.tj gave no response.
- Official Urdu texts and some other Pakistan official pages (pakistancode.gov.pk, na.gov.pk, a Supreme Court PDF) could not be read this round. No official Urdu-language text was verified.


## Labeled secondary stand-ins

After the official-source merge, the owner confirmed that publicly available secondary sources may be added if they are labeled, fully cited, and not treated as verified. Eight rows were appended to `data/sources.csv`. Four other leads were dropped and were not added. No timeline rows were added. T084 stays `not-proven`. Working files and page captures were not copied into this repository.

Each added row has `tag=secondary`, `label` = `secondary/unofficial`, and `verified=no`. It records `stands_in_for`, `author_or_publisher` and `access_date`. Summaries use “according to” or “reported by” wording. Official rows were left in place; their summaries now point to the stand-in where one exists, and still mark the official text `[UNKNOWN]` or keep the milestone `not-proven`.

Added:

- SEC-TJ-845-SPINFORM, standing in for TJ-LAW845-1999.
- SEC-KZ-416-PRG, standing in for KZ-LAW416-1999. A Continent Online page with the same doc_id was noted and not added as a separate source.
- SEC-CHR-2005-80-SCR, standing in for CHR-2005-80.
- SEC-KE-POTA-SHERIANET, standing in for KE-POTA2012 and KE-POTA2012-KL; the listing supports the citation Act No. 30 of 2012 only.
- SEC-PK-SC-2019-95, an unofficial copy of a Supreme Court of Pakistan judgment in Criminal Appeals No. 95 and 96 of 2019 (2020 PLD Supreme Court 61). The copy's URL contained a private party's name and is withheld; the party appears only as initials. The official court PDF returned HTTP 403.
- SEC-PK-DAWN-2019, a Dawn news report of 30 October 2019 about that judgment.
- SEC-PK-DAWNURDU-2025 and SEC-PK-BBCURDU-2025, Urdu news reports about Pakistan's Anti-terrorism (Amendment) Bill 2025.

Dropped:

- A Tajikistan site whose official status could not be confirmed from an independent government source.
- Refworld copies of CHR 2005/80 and of the IACHR 2002 report (HTTP 403).
- An NZLII copy of the New Zealand Terrorism Suppression Act (HTTP 403).

`origin` `media` was added to the vocabulary for the three news reports. In the legal-database rows, `origin` describes the underlying instrument and the database is recorded in `author_or_publisher`.

Regional counts after the stand-ins: Global/UN 68, Europe 67, North America 45, Middle East/North Africa 36, Sub-Saharan Africa 36, South Asia 39, East/Southeast Asia 27, Latin America 27, Russia/Central Asia 19, Oceania 12.

After these stand-ins, 196 of 612 source and milestone summaries still contain at least one `[UNKNOWN]` mark (213 marks in all).

## Rules notes

- Private parties in case titles stay as initials. One stand-in cites a 2019 Supreme Court of Pakistan judgment by court, case number, year and publishing database; the party appears only as initials, and a URL that contained a private party's name is withheld from the repository.
- Pass 4 working files, raw captures and backup files were not copied into this repository.
- This archive is not complete.
