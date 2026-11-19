# CTA6 round 3: notes

Round 3 adds sources and timeline rows gathered in pass 3, and applies the pass 3 corrections that are backed by the captured quotes. Pass 3 working files and page captures were not copied into this repository. This archive is not complete.

Accessed: 2026-11-19. The pass 3 gathering record is the basis for the counts, retries and remaining gaps below.

## What was added

- 58 sources appended to `data/sources.csv` (46 `verified=yes`, 12 `verified=no`). The add file had no `case_citation` column; official case numbers from the titles were later copied into `case_citation` for the six new court records. No source id or URL duplicated an existing row.
- 38 timeline rows, T193 to T230, appended to `data/timeline.csv`. All are `we-have-a-record`, and each cites an existing source id (including sources added in this round). The add file had no `notes` column, so that field is blank on the new rows.
- Corrections C063 to C070, all applied (see below).

After this merge the archive has 361 sources (331 primary, 30 secondary; 319 verified, 42 not) and 230 timeline rows (213 we-have-a-record, 8 not-proven, 9 people-disagree).

## Counts: pass 3 sources (58)

| Region | Sources | Verified | Timeline rows |
|---|---:|---:|---:|
| South Asia | 11 | 9 | 9 |
| Latin America | 10 | 8 | 7 |
| East/Southeast Asia | 9 | 7 | 5 |
| Middle East/North Africa | 8 | 7 | 4 |
| Oceania | 8 | 5 | 4 |
| Russia/Central Asia | 7 | 6 | 5 |
| Sub-Saharan Africa | 5 | 4 | 4 |

- Origin: government 35, oversight 14, court 6, international 3.
- Languages: English 25, Spanish 9, Russian 7, French 4, Japanese 4, Arabic 2, and one each of Turkish, Hebrew, Persian, Hindi, Dhivehi, Indonesian and Korean. There is still no Urdu source in this round.
- Tag: primary 57, secondary 1.
- By era: 1945-1990 1, 1990-2001 5, post-9/11 (2001-2014) 25, recent (2014-now) 27.
- Unverified (12): IR-CFT-LAW1394, G5S-CONV2014-WA (scanned PDF; the text layer could not be read and OCR was not run in this round), IACHR-2002-TERR-ES and IACHR-2002-TERR-EN (OAS site 503, maintenance), TJ-LAW845-1999, NZ-TSA2002, NZ-CTLA2021, AU-AGD-INSLM-RESP, IN-NIA-ACT2008, PK-CONST21-2015, JP-TFINANCE-2002 (JavaScript page), SG-NAS-MHA2002.

## Combined after round 3

| region | sources (303 + 58 = 361) | timeline (192 + 38 = 230) |
|---|---:|---:|
| Global/UN | 67 | 40 |
| Europe | 67 | 49 |
| North America | 45 | 33 |
| Middle East/North Africa | 36 | 21 |
| Sub-Saharan Africa | 35 | 22 |
| South Asia | 33 | 15 |
| Latin America | 25 | 17 |
| East/Southeast Asia | 24 | 15 |
| Russia/Central Asia | 17 | 12 |
| Oceania | 12 | 6 |

Global/UN, Europe and North America still hold 179 of 361 sources (50%) and 122 of 230 timeline rows (53%).

## Corrections applied (C063–C070)

Each correction was applied only where the quotes in the pass 3 notes support it. All eight were applied. None was skipped.

- **C063 / C064 (T117, Lei 13.260).** The cited Planalto page supports the date ("LEI Nº 13.260, DE 16 DE MARÇO DE 2016."), the place ("Brasília, 16 de março de 2016") and the enactment ("A PRESIDENTA DA REPÚBLICA Faço saber que o Congresso Nacional decreta e eu sanciono a seguinte Lei:"). Confidence moves from `not-proven` to `we-have-a-record`, and the caveat "(source page not machine-verified)" is dropped.
- **C065 / C066 (T088, EU Counter-Terrorism Strategy).** The cited Council document supports the date (30 November 2005), Brussels and the document number 14469/4/05 REV 4. It does not support "The Council of the EU issued". The cover page is a note from the Presidency and CT Co-ordinator forwarded to the Council for agreement, for onward transmission to the European Council; the adoption date is not printed. `what_happened` is reworded to that claim, and confidence moves to `we-have-a-record` together with that wording.
- **C067 (OHCHR-SR-CT).** The cited URL was read via WebFetch on 2026-11-19 and contains "In April 2005, the Commission on Human Rights, in resolution 2005/80, created a mandate ...". `verified` moves from no to yes. A retry note was appended so the source notes match that result.
- **C068 (CAMPBELL2006).** WebFetch of the cited DOI URL returned the Wiley page for "The Effectiveness of Counter-Terrorism Strategies", Lum et al., Campbell Systematic Reviews, "First published: 16 January 2006". `verified` moves from no to yes. A retry note was appended so the source notes match that result. No author contact details were copied.
- **C069 (MA-LOI03-03).** curl of the cited PDF returned HTTP 200; the Arabic text layer reads "القانون رقم 03.03 المتعلق بمكافحة الإرهاب" and "ظهير شريف رقم 1.03.140". `verified` moves from no to yes. A retry note was appended so the source notes match that result.
- **C070 (US-NSCT2018).** A note was appended: on 2026-11-19 curl of the cited dni.gov URL returned HTTP 403 and WebFetch returned 404, so the file may have been removed [UNKNOWN]. `verified` stays no. Nothing was substituted for the cited URL. The White House archives copy recorded in round 2 is unchanged and was not used to flip the verified flag.

## Retries

**Phase 1, 16 URLs, one attempt each.** Two are now `verified=yes` at the cited URL (OHCHR-SR-CT, CAMPBELL2006). Fourteen remain unverified at the cited URL:

- OAS-CICTE2002 and OAS-CICTE: 503, maintenance.
- US-OH-SCT: state archive "updates suspended" notice.
- CRS-R43983: Cloudflare 403; WebFetch timed out.
- UK-MAI: human-verification page; WebFetch timed out.
- DE-GTAZ: timeout; WebFetch 504.
- IN-NIA: timeout.
- KE-POTA2012: HTTP 500; WebFetch 403.
- PH-RA11479: Cloudflare; WebFetch timed out.
- CHR-2005-80: the UN documents site served only its language selector and "LOADING" pages.
- ID-BNPT: bot-protection page.
- COE-ECST1977 and COE-CPT2005: 403; WebFetch 500.
- US-NSCT2018: curl 403 and WebFetch 404; the file may have been removed from dni.gov [UNKNOWN]; nothing was substituted.

**South Asia (pass 2), one retry each.** All still unverified at the original cited URLs: PK-ATA1997, PK-ATA1997-FIA, IN-UAPA1967, IN-NIA-UAPA, IN-NIA-UAPA-HI, PK-CODE-URDU.

The ATA 1997 text is now verified through a different official copy (PK-FMU-ATA1997, Financial Monitoring Unit), and the NIA Act through the Hindi text (IN-NIA-ACT2008-HI). These were added as separate sources, not as substitutes for the original URLs.

**Other pass 2.**

- MA-LOI03-03: now verified by curl (C069).
- KE-POTA2012-KL: still unverified (202, then WebFetch 403).
- KZ-LAW416-1999: still unverified (JavaScript shell; WebFetch showed only a "test version" page).

## Dropped candidates (not in sources.csv)

- 404s or soft 404s: Papua New Guinea parliament Act PDF and bills page; the NAK (nac.gov.ru) decree page; old NHRC India URLs.
- Duplicates of kept entries: 5.
- No terrorism content: an African Court Tanzania judgment; a Pacific Islands Forum declaration page.
- Third-party law index only: Morocco Bulletin officiel 5114.
- Scanned and unreadable: Kenya POTA legal notice.

## Remaining gaps

See [GAPS.md](../GAPS.md) for the full list. In short:

- Kenya POTA official text, New Zealand legislation pages, OAS/CICTE and the IACHR 2002 report, Council of Europe cited URLs, the UN documents system for CHR-2005-80, and the Kazakhstan and Tajikistan law texts remain blocked or unverified.
- No official URL was found for Mexico's 2014 terrorism-financing reform, and no official Korean human rights commission document was found.
- The G5 Sahel convention PDF was fetched but is a scan without a text layer; OCR was not run in this round. Ratification is verified via Mali's SGG (ML-SGG-CONV).
- Iran's CFT law is unverified. There is still no verified Urdu official text.
- The place of the IACtHR judgments and of the African Court judgment is not in the captured text and is marked [UNKNOWN]. Day and month are [UNKNOWN] for the 1979 Sri Lanka PTA, the 1997 Pakistan ATA, the 2002 Australian SLAT Act, the 2004 UFI-AMIA unit, the 2013 NACTA Act and the 2020 HRCSL study.
- Egypt NCHR annual reports are listed as reports; their content was not summarized.
- Round 1 source languages remain `[UNKNOWN]`.

## Rules notes

- Neutral wording only. No verdicts were drawn. The Turkish Constitutional Court row (T216) states the case, petitioners and law, but not the outcome.
- Private parties in five case titles are initials. States, officials and organisations stay named, and case numbers are kept. The private working map of those names is not in this repository and is not named here.
- Page captures and other working files stay on the local machine and are not committed. Some captures contain author or staff contact details; none were copied into the spreadsheets or these notes.
- Three captures used to verify sources were labelled excerpts, not full pages (AU-INSLM, OHCHR-SR-CT and the T117 Planalto page).
- A scan of the tracked files for email addresses, phone numbers and the names in the private working map was clean.
- Nothing was uploaded or pushed.
