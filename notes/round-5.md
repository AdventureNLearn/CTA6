# CTA6 round 5: notes

Round 5 adds sources and timeline rows gathered in pass 5, applies the pass 5 corrections that are backed by a headless-browser load or a fresh curl capture of the same cited official URL, and fills some `[UNKNOWN]` marks in existing summaries. Pass 5 working files and page captures were not copied into this repository. This archive is not complete.

Accessed: 2026-11-19. The pass 5 gathering record is the basis for the counts, retries and remaining gaps below.

## What was added

- 4 sources appended to `data/sources.csv`, all `verified=yes`: the Council of Europe explanatory reports to ETS No. 90 (COE-ECST1977-ER) and CETS No. 196 (COE-CPT2005-ER); the OAS treaty status page for the Inter-American Convention against Terrorism (OAS-A66-SIGS); and the Senate-hosted official text of Pakistan's Anti-terrorism (Amendment) Bill 2025, marked as passed by the National Assembly and undated (PK-ATA-BILL2025).
- 8 timeline rows, T237 to T244, appended to `data/timeline.csv`. All are `we-have-a-record`, and each cites a verified official source first. They extend coverage in Oceania (T238, T244), Russia/Central Asia (T237), Sub-Saharan Africa (T243), Latin America (T239, T241), the Middle East/North Africa (T240) and the agencies theme (T242).
- No new labeled secondary stand-ins were added. After review, the duplicate Kenya Law row KE-POTA2012-KL was merged into KE-POTA2012; T243 and the SheriaNet stand-in now cite KE-POTA2012 only.
- No timeline row was added for Senate passage or presidential assent of the 2025 Pakistan bill, because those facts still rest only on the Urdu news reports.

## Verification method (headless browser or fresh curl)

Fourteen existing official rows were marked `verified=yes` after a headless-browser load (`--dump-dom`) or a fresh curl capture of the same cited official URL, with the matched text quoted in the row's notes:

- curl: OAS-CICTE2002, OAS-CICTE, IACHR-2002-TERR-ES, IACHR-2002-TERR-EN, CNCDH-2017, AU-POA2002-PSD (C088, C094, C096, C098, C119, C121, and their notes rows).
- headless Chrome: NZ-TSA2002, NZ-CTLA2021, KE-POTA2012, KZ-LAW416-1999, MA-CNASNU, JP-TFINANCE-2002, ID-BNPT, DE-GTAZ (C100, C103, C106, C109, C111, C113, C115, C117, and their notes and date rows).

The captures stay local and were not committed. Dates read from those pages were applied for NZ-TSA2002 (17 October 2002), NZ-CTLA2021 (4 October 2021) and KE-POTA2012 (12 October 2012).

## Corrections applied and adapted (C088–C135)

- **C088–C099.** OAS and IACHR pages that had been blocked (HTTP 503) are now `verified=yes` at the cited URLs.
- **C090–C093 (T061) were applied.** The milestone claim is that the Inter-American Convention against Terrorism was adopted by the OAS on 3 June 2002 in Bridgetown, Barbados. The cited treaty page (OAS-CICTE2002) is now verified with the full treaty text. The OAS status page (OAS-A66-SIGS), added as the second citation and also `verified=yes`, records "ADOPTED AT: Bridgetown, Barbados DATE: 06/03/2002 ... Thirty-second regular session of the OAS General Assembly". That directly supports the claim, so confidence moves to `we-have-a-record`.
- **C100–C122.** New Zealand, Kenya Law, Kazakhstan, Morocco's sanctions-commission page, Japan's 2002 terrorism-financing Act, BNPT, GTAZ, the CNCDH 2017 opinion and the AU 2002 Plan of Action (Peace and Security Department copy) are now `verified=yes`. T149's note no longer calls AU-POA2002-PSD unverified.
- **C123 was not applied as written.** The owner decision was to point KE-POTA2012 at Kenya Law's current site, mark it `verified=yes`, and keep the earlier PDF URL (still HTTP 500) in the notes. The date is 12 October 2012. After review, the duplicate row KE-POTA2012-KL was merged into KE-POTA2012; T243 and SEC-KE-POTA-SHERIANET now point at KE-POTA2012, and KE-POTA2012-KL was removed.
- **C124–C127 (T015) and C128–C131 (T085).** Both milestones are now `we-have-a-record`, with the official explanatory reports as second citations. T015 quotes the 1977 report exactly as "opened to signature"; its `what_happened` line uses the same wording. T085 keeps "opened for signature", which is the 2005 report's wording.
- **C132–C135.** The stand-ins SEC-KZ-416-PRG, SEC-KE-POTA-SHERIANET, SEC-PK-DAWNURDU-2025 and SEC-PK-BBCURDU-2025 were kept in place, still `verified=no`. Each notes that the official text is now in the archive (KZ-LAW416-1999, KE-POTA2012, PK-ATA-BILL2025). The two Urdu news rows now name PK-ATA-BILL2025 in `stands_in_for`; Senate passage and assent are still not shown in that official text and stay not-proven. No milestone cites a stand-in as proof.
- **T045** was not changed. The adoption-date disagreement remains recorded as T145.
- **T084** stays `not-proven`. CHR 2005/80 could not be read from the UN document system; the unofficial copy SEC-CHR-2005-80-SCR remains a stand-in.

PE-GOB-CIAT2002-ES is still a separate official Spanish copy. Its summary and notes no longer say the OAS page could not be reached, because OAS-CICTE2002 is now verified.

## Summary fills

`summaries-fill.csv` was applied, except the KE-POTA2012 summary, which was rewritten to match the new official URL. The fills clear 39 of the 213 `[UNKNOWN]` marks that were open after round 4, and they rewrite a few already-complete sentences (CA-LISTED was not undated; UK-77OFFICIAL's GOV.UK landing page; T195's reference to Act XXVII of 1997). Four summaries with no mark (AU-POA2002-PSD, T061, T015, T085) were rewritten because their verification or confidence changed.

After these fills and the new rows, 165 of 623 source and milestone summaries still contain at least one `[UNKNOWN]` mark (180 marks in all). Most remaining marks are unsummarized provisions or findings, or undated web pages whose captures show no date.

## Combined after round 5

| region | sources (376 + 4 − 1 Kenya duplicate = 379) | timeline (236 + 8 = 244) |
|---|---:|---:|
| Global/UN | 68 | 40 |
| Europe | 69 | 50 |
| North America | 45 | 33 |
| South Asia | 40 | 17 |
| Middle East/North Africa | 36 | 22 |
| Sub-Saharan Africa | 35 | 23 |
| Latin America | 28 | 20 |
| East/Southeast Asia | 27 | 18 |
| Russia/Central Asia | 19 | 13 |
| Oceania | 12 | 8 |

Global/UN, Europe and North America hold 182 of 379 sources (48%) and 123 of 244 timeline rows (50%). Oceania and Russia/Central Asia remain the smallest regions, though each gained a verified national statute and a milestone.

## Retries still blocked

These official sources were tried again in pass 5 and remain `[UNKNOWN]` or `verified=no` at the cited URL:

- UN Commission on Human Rights resolution 2005/80 (CHR-2005-80): UN document system error page or 403. T084 stays not-proven, with SEC-CHR-2005-80-SCR as a stand-in.
- Tajikistan law 845 (TJ-LAW845-1999): ncz.tj gave no response. SEC-TJ-845-SPINFORM remains a stand-in.
- Other Pakistan official pages: pakistancode.gov.pk (ATA and the Urdu index) did not respond; na.gov.pk (21st Amendment PDF) did not respond; the Supreme Court PDF of the 2019 judgment returned 403; the FIA copy of the ATA returned 500. No official Urdu-language text was read. Senate passage and assent of the 2025 bill still rest only on the two Urdu news reports.
- Still failing of the unverified rows retried in passing: US-OH-SCT (notice only), PH-RA11479, UK-MAI, PH-SC-2021-252578, indiacode, NIA, SG-NAS, OIC, KNCHR, IR, SA, AU-AGD, and the Rome 1898 journal.

## Rules notes

- Private parties in case titles stay as initials. A public official's name in the Pakistan 2025 bill (the minister signing the statement of reasons) was not copied. No government ID numbers were written.
- Pass 5 working files, raw captures and backup files were not copied into this repository.
- This archive is not complete. Pre-1945 and colonial-era laws were not covered this round.
