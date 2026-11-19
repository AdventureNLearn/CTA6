# CTA6 pass 2: notes

Pass 2 adds sources and timeline rows to the phase 1 archive. Phase 1 files were not edited; every change to a phase 1 record is a row in `corrections.csv`.

## Files
- `sources-add.csv`: 107 new sources. Columns are the same as phase 1 `sources.csv`, plus `language`. Where a source gives no English title, the original title is used and `notes` says "English title: [UNKNOWN]".
- `timeline-add.csv`: 60 new rows, T133 to T192, with the same columns as phase 1 `timeline.csv`.
- `corrections.csv`: 62 rows (C001 to C062). Columns: correction_id, phase1_id, field, old_value, new_value, evidence, accessed, case_citation (filled from C016 onward).
  - C001-C015: verified flags, notes and a recorded date disagreement.
  - C016-C035: anonymized case titles and timeline text.
  - C036-C062: source id renames (see "Source id renames").
- `raw/` (local only, not committed, left unchanged): captures (`<id>.html/.pdf/.txt/.meta.json`, `retry-*`, `mirror-*`, `*.hudoc.json`, `*.ocr.txt`). Files are named with the ids in use when they were captured, so some carry pre-rename ids, and their contents may contain party names.
- `work/` (local only, not committed): scripts (`candidates_p2.py`, `fetch.py`, `build_sources.py`, `build_timeline.py`, `rename_ids.py`, `hudoc.py`, `checks.py`), `overrides.json` and `dropped_p2.json`. A rebuild runs the builds and applies `rename_ids.py` automatically.

## Method and verification
- A source is `verified=yes` when one of these holds:
  - curl fetch returned HTTP 200 and the expected text appeared in the capture.
  - The text was confirmed by OCR (DZ-DL92-03) or by checking a page image visually (EG-LAW94-2015, where the PDF text layer is font-encoded).
  - The HUDOC API returned the matching itemid (ECtHR judgments).
  - The page was read through WebFetch because the capture was blocked. These rows say "Verified via WebFetch" in `notes` and have no readable raw capture.
- UN documents are cited at `https://undocs.org/<symbol>` and were verified through the UN ODS API.
- URL policy: a URL is kept only if a fetch confirmed it or it came from a web-search result listing. Kept rows that are unverified say "URL from search index".
- 13 candidates were dropped:
  - Seven guessed URLs that failed: EU FRA 2021, IACHR 2002, three IACtHR Peru judgments, Colombia Ley 1121 and Russia's NAK site.
  - One archive URL that could not be confirmed (NLS LoN 1937).
  - Two search URLs that returned 404 (LK-PTA lawnet, SAARC list).
  - Three duplicates of phase 1 rows (ZA POCDATARA, ASEAN ACCT, Arab Convention).
  - See `work/dropped_p2.json`.
- Dates come from the captured text where possible. Where a date comes only from a search listing, `notes` says so (Peru DL 25475 day and month, ASEAN ACCT, ACHPR 2015).
- SR country report dates are the "Distr.: General" dates. Visit dates in the timeline come from the report text.

## Counts: pass 2 sources (107)
- By region:
  - Sub-Saharan Africa 21
  - Middle East/North Africa 18
  - Europe 17
  - South Asia 17
  - Russia/Central Asia 10 (new region label)
  - East/Southeast Asia 10
  - Latin America 9
  - North America 3
  - Oceania 1
  - Global/UN 1
- By origin: government 41, oversight 21, court 18, international 14, NGO 11, academic 2.
- By language:
  - English 74
  - French 7
  - Spanish 5
  - Russian 5
  - Arabic 3
  - German, Chinese, Hindi and Portuguese 2 each
  - Turkish, Indonesian, Bengali, Korean and Urdu 1 each
- By tag: primary 94, secondary 13.
- Verified: 90 yes, 17 no.
- By era: pre-1945 3, 1945-1990 6, 1990-2001 15, 2001-2014 30, 2014-now 53.

## Counts: pass 2 timeline (60)
- By confidence: we-have-a-record 54, people-disagree 4, not-proven 2.
- By region:
  - Sub-Saharan Africa 12
  - Europe 10
  - Middle East/North Africa 10
  - East/Southeast Asia 7
  - Russia/Central Asia 7
  - Latin America 6
  - South Asia 5
  - Global/UN 1
  - North America 1
  - Oceania 1

## Combined phase 1 + pass 2

| region | sources (196 + 107 = 303) | timeline (132 + 60 = 192) |
|---|---|---|
| Global/UN | 67 | 40 |
| Europe | 67 | 49 |
| North America | 45 | 33 |
| Sub-Saharan Africa | 30 | 18 |
| Middle East/North Africa | 28 | 17 |
| South Asia | 22 | 6 |
| East/Southeast Asia | 15 | 10 |
| Latin America | 15 | 10 |
| Russia/Central Asia | 10 | 7 |
| Oceania | 4 | 2 |

## Retries on the 21 unverified phase 1 sources
Only the same document was used, either at its original URL or at an official mirror.
- **Now verified (9 sources, C001-C006 and C008-C010):**
  - OHCHR-FS32 and CA-LISTED: curl retry of the same URL.
  - EU-CTSTRAT2005: OCR of the same PDF.
  - US-NSCT2018: White House archive mirror.
  - UK-AvSSHD2004: House of Lords publication, via WebFetch.
  - BR-L13260: same Planalto URL, via WebFetch.
  - COE-ECST1977 and COE-CPT2005: rm.coe.int treaty texts.
  - CAMPBELL2006: Public Safety Canada library copy of the same review.
- **Still unverified (12 sources):**
  - OAS-CICTE2002 and OAS-CICTE: oas.org returns 503/500.
  - US-OH-SCT: the page now shows only a notice that database updates are suspended (C007).
  - CRS-R43983: bot check.
  - UK-MAI: human-verification page, including at the National Archives web archive.
  - DE-GTAZ: timeout/504.
  - IN-NIA: timeout.
  - KE-POTA2012: the new Kenya Law URL returns 202/403 (C014).
  - PH-RA11479: 403 and timeout.
  - OHCHR-SR-CT: 403 and timeout.
  - CHR-2005-80: ODS returns a loading page.
  - ID-BNPT: BunkerWeb human check.

## Where sources disagree (new people-disagree rows)
- **OAU Convention adoption date (T145):**
  - Phase 1 T045 used 1 July 1999, from the AU treaty page.
  - UN-OAU1999-COPY, AU-OAU1999-TEXT and AU-AHG-DEC132 (Algiers Assembly, 12-14 July 1999) give 14 July 1999.
  - Both dates are kept; see C011.
- **Madrid, 11 March 2004 (T150):**
  - UNSC1530 attributed the bombings to ETA.
  - SR-ESP-2008 describes them as carried out by members of an international terrorist cell (C012).
- **SSCI study (T166):**
  - The CIA's June 2013 response (CIA-SSCI-2013) states the Agency disagrees with some of the study's assertions.
  - US-SSCI2014 is the committee's study (C013).
- **Egypt 2015 law number (T173):**
  - The Official Gazette shows Decree-Law No. 94 of 2015.
  - Human Rights Watch calls it "Law 95 of 2015".
- **Checked, but no disagreement found:**
  - SCO Convention signing place: the convention text ("Done at Shanghai") and China's MFA treaty database (签署地点：上海) agree, so there is no disagreement row.

## Pre-1945
- **Rome 1898:** no official text found online. Coverage is secondary only: Jensen 2009 (verified; covers November-December 1898) and Jensen 1981 JCH (unverified, bot check). Jensen 1981 states that the procès-verbaux are held at the Italian Foreign Ministry and at the UK PRO; this was not checked [UNKNOWN].
- **St Petersburg Protocol 1904:** the Russian Historical Society's e-library record (HIST-SPB1904-EBID) of the text published in 1918, dated 1/14 March 1904, plus Jensen 2009, which gives 14 March 1904. The place of signing is not stated in either capture, so it is [UNKNOWN] in T134.
- **League of Nations 1937:** phase 1 already holds LON-1937 and LON-1937-LOC. The NLS archive candidate was dropped (unconfirmed).

## Remaining gaps and regional imbalance
- Global/UN, Europe and North America still hold 179 of 303 sources (59%) and 122 of 192 timeline rows (64%).
- Oceania (4 sources) and Russia/Central Asia (10) remain thin.
- South Asia has 22 sources but only 6 timeline rows: five of its sources (Pakistan ATA x2, India UAPA (English), NIA pages) could not be verified.
- **Not yet covered, or unverified:**
  - Africa: Algeria after 1992; Morocco Loi 03-03 (unverified); Kenya POTA (unverified); the G5 Sahel and Mali national agencies; Egypt and Nigeria oversight bodies (only NGO sources so far).
  - Latin America: Colombia (Ley 1121 dropped); Peru and Mexico agencies; Argentina AMIA prosecutor's unit; Inter-American Court Peru cases (URLs not confirmed); IACHR 2002 report (URL not confirmed).
  - Asia: the Philippines ATA itself (phase 1, still unverified) and the text of the 2021 decision in G.R. No. 252578 (unverified); Malaysia and Singapore oversight; China oversight (only HRW-CHN-2018); Japan and Korea oversight.
  - Central Asia: Kyrgyzstan, Tajikistan and Turkmenistan laws; Kazakhstan law (unverified); SCO RATS documents beyond the home page; Russia's NAK (dropped).
  - Regional bodies: OAS/CICTE (site down); SAARC Secretariat page (404); the OIC Convention (522 error, unverified).
  - Oversight: India NHRC, Pakistan NCHR, Indonesian Komnas HAM, African Court judgments, Turkish Constitutional Court.
- **Languages:** Urdu has only an index page (unverified), and Hindi has one verified Act text. There are no Persian, Hebrew or Japanese originals, and Arabic is limited (3).
- 17 pass 2 sources remain unverified, mostly because government sites in South Asia and Morocco time out or run bot checks.

## Rules notes
- No operational or tactical content. Rows describe laws, rulings, reports and dates only.
- Contested labels are attributed to whoever used them (for example "war crimes" to Amnesty International, "disappearances" to HRW, and the ETA attribution to UNSC1530).
- No verdicts on what worked. The Campbell review and ICJ report are listed as sources only.
- Private individuals: case parties are anonymized in titles, text and ids (see the next two sections).
- No government ID numbers. Statute, decree, gazette, case and application numbers are legal identifiers, not personal IDs.
- PII grep: no emails or phone numbers in the CSVs or NOTES. 15 raw captures contain institutional contact emails (publishers, courts, agencies), and none belong to private persons.
- No home-directory paths and no restricted project names in the outputs. No locked paths were opened.
- Everything is local. Nothing was uploaded, sent or pushed.
- Some sources are third-party copies of official texts: ecoi.net (Algeria), AfricanLII (ECOWAS Act), UiO (SAARC), cat-int.org (Jensen 2009) and the s3waas government CDN (Hindi UAPA). `notes` marks each one.

## Anonymized case titles
**Rule (owner decision, 18 Nov 2026):**
- The name of any natural person who is a party or applicant and is not a public official is replaced with initials, the way courts do it.
- Initials come only from the name as printed in the source: one initial per printed word of the surname (a hyphenated surname is one word). Aliases in parentheses are dropped. No names were expanded or invented.
- States, public officials (Bush, Rumsfeld, Holder; Selahattin Demirtaş as a member of parliament and party co-chair), government bodies (Executive Secretary, Council, Commission) and organisations (Al Barakaat, Humanitarian Law Project) are kept.
- Every case keeps or gains its official number or citation: US Reports citation, CJEU case numbers, ECtHR application numbers (from the HUDOC appno field), IACtHR Serie C number and Philippine G.R. number.
- URLs are unchanged.

**Phase 1 (`sources.csv` and `timeline.csv` not edited).** Ids below are the new ids from C036-C045.

| correction | phase 1 record | field | new value |
|---|---|---|---|
| C016 | USSC-2004-542-466 | title | R. v. Bush, 542 U.S. 466 (2004) |
| C017 | USSC-2004-542-507 | title | H. v. Rumsfeld, 542 U.S. 507 (2004) |
| C018 | USSC-2006-548-557 | title | H. v. Rumsfeld, 548 U.S. 557 (2006) |
| C019 | USSC-2008-553-723 | title | B. v. Bush, 553 U.S. 723 (2008) |
| C020 | CJEU-2008-C402-05P | title | K. and Al Barakaat v Council and Commission (Joined Cases C-402/05 P and C-415/05 P) |
| C021 | ECHR-1978-5029 | title | K. and Others v. Germany, no. 5029/71 |
| C022 | ECHR-1988-11209 | title | B. and Others v. the United Kingdom, nos. 11209/84 and others |
| C023 | ECHR-1995-18984 | title | M. and Others v. the United Kingdom, no. 18984/91 |
| C024 | ECHR-2012-39630 | title | E. v. the former Yugoslav Republic of Macedonia, no. 39630/09 |
| C025 | ECHR-2014-28761 | title | A.N. v. Poland, no. 28761/11 |
| C026 | T017 | what_happened | K. and Others v. Germany |
| C027 | T025 | what_happened | B. and Others v. the United Kingdom |
| C028 | T036 | what_happened | M. and Others v. the United Kingdom |
| C029 | T075 | what_happened | R. v. Bush |
| C030 | T076 | what_happened | H. v. Rumsfeld (542 U.S. 507) |
| C031 | T090 | what_happened | H. v. Rumsfeld (548 U.S. 557); the petitioner's name later in the sentence becomes "the petitioner" |
| C032 | T096 | what_happened | B. v. Bush |
| C033 | T097 | what_happened | K. and Al Barakaat (Joined Cases C-402/05 P and C-415/05 P) |
| C034 | T108 | what_happened | E. v. the former Yugoslav Republic of Macedonia |
| C035 | T110 | what_happened | A.N. v. Poland |

- In C016-C035, old_value gives the phase 1 file line and field instead of repeating the original text.
- **Phase 1 records checked and left unchanged:**
  - UK-AvSSHD2004 and T080 ("A and others", already anonymized by the court)
  - ECHR-AvUK2009 ("A. and Others")
  - ECHR-IRELAND1978 (states)
  - US-HLP2010 (public official and organisation)

**Pass 2 (edited in place):**
- `sources-add.csv`, 13 rows (titles, plus notes where they quoted a name): IACTHR-2014-279, PH-SC-2021-252578, ECHR-2008-37201, ECHR-2012-10593, ECHR-1996-21987, ECHR-2014-7511, ECHR-2018-33234, ECHR-2017-26562, ECHR-2011-18299, ECHR-1993-14553, ECHR-2005-46221, ECHR-2012-8139, and ECHR-DEMIRTAS2-2020 (name kept; application number added).
- `timeline-add.csv`, 11 rows (what_happened): T144, T152, T156, T160, T164, T167, T168, T178, T181, T184 (name kept; number added) and T186.

**Pending at merge (phase 1 Markdown not edited, per instruction):**
- `NOTES.md` lines 137, 138 and 139 carry the case names; use the C031, C032 and C033 text.
- The same three lines also carry pre-rename source ids. Replace them with the C038, C039 and C040 new ids (USSC-2006-548-557, USSC-2008-553-723, CJEU-2008-C402-05P). No separate correction rows were written for these lines.

## Source id renames
**Rule (owner decision, 18 Nov 2026):**
- Every source id containing a private person's surname is renamed to a neutral court-year-number id, using the number as the source prints it: ECtHR = HUDOC application number (the first one for multi-application cases), US Supreme Court = US Reports volume and page, CJEU = first case number, IACtHR = Serie C number, Philippines = G.R. number.
- Kept as they are: ECHR-DEMIRTAS2-2020 (public official), and ids naming states, organisations or authors (for example ECHR-IRELAND1978, US-HLP2010, CAMPBELL2006, CRONIN-HTE, HIST-ROME1898-JENSEN, JP-PSIA-AUM).
- URLs are unchanged.
- Old-to-new source id pairs were not written into this repository. `work/` is not committed.

**Phase 1 (10 ids renamed via corrections):**
- C036-C045: field=id. phase1_id gives the sources.csv line, old_value gives the map key, and new_value gives the new id: USSC-2004-542-466, USSC-2004-542-507, USSC-2006-548-557, USSC-2008-553-723, CJEU-2008-C402-05P, ECHR-1978-5029, ECHR-1988-11209, ECHR-1995-18984, ECHR-2012-39630, ECHR-2014-28761.
- C046-C055: the timeline citations that point to them (citation_source_id in T017, T025, T036, T075, T076, T090, T096, T097, T108, T110).
- C056-C062: the phase 1 STRUCTURE.md id lists (lines 16, 21, 26, 38, 43, 87, 127).
- C016-C035 were rewritten to use the new ids, or line numbers, instead of the old ids.

**Pass 2 (13 ids renamed in place):**
- IACTHR-2014-279, PH-SC-2021-252578 (decision text), PH-SC-2021-252578-D (docket page), ECHR-2008-37201, ECHR-2012-10593, ECHR-1996-21987, ECHR-2014-7511, ECHR-2018-33234, ECHR-2017-26562, ECHR-2011-18299, ECHR-1993-14553, ECHR-2005-46221, ECHR-2012-8139.
- Timeline citations pointing to them were updated in place.

**Fallback:**
- PH-SC-2021-252578-D: two pass 2 sources share G.R. No. 252578, so the docket page gets the suffix "-D". Its year (2021) is the decision year, since the docket page itself is undated.
- No id needed a court-year letter sequence: every renamed case had a printed number.
