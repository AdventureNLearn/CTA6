# CTA6 Phase 1: NOTES

Prepared during the research pass (source gathering only). Accessed 2026-11-18. This pack contains no verdicts, scoring or rankings.

## Method

1. I drafted candidate citations for official and scholarly sources across the five eras, nine regions and six themes in the brief.
2. I fetched every URL with curl (desktop browser user-agent, 25-second timeout) and saved captures in raw/ (<id>.html or .pdf, extracted text in <id>.txt, fetch metadata in <id>.meta.json).
3. Verification: verified=yes means the URL returned the document and its text contained the expected title words. Variants, each noted per row:
   - UN documents: the undocs.org symbol URL is cited, and the English PDF was fetched from documents.un.org (ODS).
   - ECtHR judgments: the HUDOC URL is cited, and the case name and date were read from the HUDOC metadata API.
   - Scanned treaty PDFs: OCR of the first pages (raw/<id>.ocr.txt).
   - Sites that blocked curl: the public page was read with the WebFetch tool, and no raw HTML was saved for those rows.
4. Five candidate URLs that I had guessed returned 404 or redirected to an unrelated page. I dropped those rows instead of keeping URLs that were never confirmed (listed below). Rows on sites that block bots (403, 503, timeout) were kept with verified=no.
5. Timeline facts were checked against the text of the cited capture where it was readable, for example UK royal-assent dates from legislation.gov.uk 'enacted' introductions and UN adoption dates from the resolution text. Timeline rows whose cited source is verified=no are marked not-proven.
6. Neutral wording: labels are attributed (for example, 'designated ... by'). The words 'terrorist' and 'terrorism' appear in official titles and quoted instrument names as issued.

## Counts

- sources.csv: 196 rows (the brief targeted 80-150; the spec addition for oversight sources pushed it higher).
- timeline.csv: 132 rows (the brief asked for about 100).
- Verified: 175 yes, 21 no.

### Sources by tag

| tag | n |
|---|---|
| primary | 180 |
| secondary | 16 |

### Sources by origin

| origin | n |
|---|---|
| government | 57 |
| international | 93 |
| academic | 9 |
| NGO | 3 |
| court | 16 |
| oversight | 18 |

### Sources by era

| era | n |
|---|---|
| pre-1945 | 7 |
| 1945-1990 | 23 |
| 1990-2001 | 21 |
| post-9/11 (2001-2014) | 81 |
| recent (2014-now) | 64 |

### Sources by region

| region | n |
|---|---|
| North America | 42 |
| Europe | 50 |
| Middle East/North Africa | 10 |
| Sub-Saharan Africa | 9 |
| South Asia | 5 |
| East/Southeast Asia | 5 |
| Latin America | 6 |
| Oceania | 3 |
| Global/UN | 66 |

### Sources by theme

| theme | n |
|---|---|
| laws and treaties | 70 |
| agencies | 22 |
| major operations | 7 |
| UN and international frameworks | 55 |
| doctrine and strategy | 7 |
| studies and evaluations | 35 |

### Timeline by era / region / confidence

| era | n |
|---|---|
| pre-1945 | 7 |
| 1945-1990 | 22 |
| 1990-2001 | 20 |
| post-9/11 (2001-2014) | 59 |
| recent (2014-now) | 24 |

| region | n |
|---|---|
| North America | 32 |
| Europe | 39 |
| Middle East/North Africa | 7 |
| Sub-Saharan Africa | 6 |
| South Asia | 1 |
| East/Southeast Asia | 3 |
| Latin America | 4 |
| Oceania | 1 |
| Global/UN | 39 |

| confidence | n |
|---|---|
| we-have-a-record | 119 |
| not-proven | 8 |
| people-disagree | 5 |

### Origin by region (sources)

| region | government | international | academic | NGO | court | oversight |
|---|---|---|---|---|---|---|
| North America | 27 | 0 | 0 | 1 | 5 | 9 |
| Europe | 21 | 12 | 1 | 1 | 10 | 5 |
| Middle East/North Africa | 0 | 10 | 0 | 0 | 0 | 0 |
| Sub-Saharan Africa | 2 | 7 | 0 | 0 | 0 | 0 |
| South Asia | 3 | 2 | 0 | 0 | 0 | 0 |
| East/Southeast Asia | 3 | 2 | 0 | 0 | 0 | 0 |
| Latin America | 1 | 3 | 0 | 0 | 1 | 1 |
| Oceania | 0 | 2 | 0 | 0 | 0 | 1 |
| Global/UN | 0 | 55 | 8 | 1 | 0 | 2 |

## Coverage gaps and regional imbalance

- **Regional imbalance.** Europe (50), North America (42) and Global/UN (66) make up most of the sources. Sub-Saharan Africa (9), Latin America (6), East/Southeast Asia (5), South Asia (5) and Middle East/North Africa (10) are thin. Several of their rows are UN resolutions, not national records.
- **Africa.** There are no verified national statutes except South Africa (2004). The Kenya 2012 Act URL returned HTTP 500, and a Nigeria 2022 Act URL was dropped (404). Nothing was gathered for Algeria, Egypt, Mali, Somalia, Uganda or the AU's 2002 Plan of Action [UNKNOWN].
- **Latin America.** Coverage is the OAS (site in maintenance, 503), Peru's CVR, Brazil's 2016 law (not reached) and Colombia's JEP home page. There is nothing on Argentina, Colombia's statutes, or Mexico [UNKNOWN].
- **East/Southeast Asia.** Coverage is ASEAN 2007, Indonesia's BNPT (bot page), Japan's PSIA and the Philippines' 2020 Act (blocked). There is nothing on China, Malaysia, Singapore or Thailand legislation, or on Japan's 1995 Tokyo subway attack records [UNKNOWN].
- **South Asia.** Coverage is India's NIA (timeout), Pakistan's NACTA and UNSC Taliban sanctions. The India UAPA 1967 official URL was dropped (404). There is nothing on TADA, POTA, Pakistan's Anti-Terrorism Act 1997, Sri Lanka's PTA 1979, or the official records of the 2008 Mumbai attacks [UNKNOWN].
- **Middle East/North Africa.** Coverage is mainly UN resolutions and the Arab Convention 1998. There are no national statutes (for example Israel, Egypt, Saudi Arabia, Turkey or Iraq) and no GCC or OIC instruments [UNKNOWN].
- **Non-English sources.** Only France (2 laws), Germany (§129a StGB, GTAZ), Spain (LO 2/2015), Norway (NOU 2012:14), Brazil, Peru, Colombia and Japan are represented. Arabic, Russian, Chinese, Hindi, Urdu, Indonesian and Turkish official sources were not gathered [UNKNOWN].
- **Russia and Central Asia.** There is no national record. The only entries are UNSC 1440 (Moscow 2002) and the 2002-2004 resolutions; the SCO convention and RATS were not gathered [UNKNOWN].
- **Oversight balance.** US oversight is relatively well covered (DOJ OIG x4, PCLOB, GAO, SSCI). Elsewhere it is the UK IRTL and ISC, Norway and New Zealand commissions, ECtHR, and the UN Special Rapporteur. OHCHR pages were blocked by Cloudflare (403). Council of Europe treaty pages were blocked or timed out. There are 3 NGO reports (HRW x2, Amnesty x1). The CIA's 2013 response to the SSCI study was not located at a confirmed URL [UNKNOWN].
- **Studies of what worked.** RAND MG-741, Cronin (2009), the Campbell review (blocked), GTD, RDWTI, GTI and ICCT are listed only. No conclusions are drawn from them. Peer-reviewed evaluation literature beyond these is not yet gathered [UNKNOWN].
- **Pre-1945.** The pack has 7 sources. Not gathered: the 1898 Rome anti-anarchist conference, the 1904 St Petersburg protocol, and colonial-era emergency laws [UNKNOWN].

## Where sources disagree (people-disagree rows)

- T079 (2004-10-08): UNSC1566 vs LON-1937-LOC. Definitions differ: Security Council resolution 1566 (2004) describes terrorist acts in its own wording, while the 1937 League of Nations convention used a different definition; no single definition is agreed across sources.
- T080 (2004-12-16): UK-AvSSHD2004 vs UK-ATCSA2001. Positions differed on Part 4 detention powers: the UK government had enacted them in the 2001 Act, and the House of Lords in A v Secretary of State held the related provision incompatible with the European Convention on Human Rights.
- T090 (2006-06-29): USSC-2006-548-557 vs US-MILORDER2001. Positions differed on military commissions: the 2001 Military Order created them, and the US Supreme Court in H. v. Rumsfeld, 548 U.S. 557 (2006), held that the military commission convened to try the petitioner lacked power to proceed.
- T096 (2008-06-12): USSC-2008-553-723 vs US-MCA2006. Positions differed on habeas corpus for Guantanamo detainees: the Military Commissions Act of 2006 restricted it, and the US Supreme Court in B. v. Bush, 553 U.S. 723 (2008), held detainees have the constitutional privilege of habeas corpus.
- T097 (2008-09-03): CJEU-2008-C402-05P vs UNSC1267. Positions differed on implementing UN sanctions listings: the Court of Justice in K. and Al Barakaat (Joined Cases C-402/05 P and C-415/05 P) annulled the EU regulation as it concerned the applicants, on fundamental-rights grounds, while the UN 1267 listing regime continued.

Other disagreements noted but not yet sourced on both sides:
- Madrid 2004: UNSC 1530's operative text attributes the bombings to ETA. Whether later official or judicial records support or contest this attribution was not checked in this pass [UNKNOWN]. The timeline row records only what the resolution text says.
- OAU Convention date: the AU treaty page gives adoption 1 Jul 1999. This date was not cross-checked against a second source [UNKNOWN].
- SSCI 2014 study: the published volume includes the committee's additional and minority views, and the CIA issued a 2013 response. Because the CIA document is [UNKNOWN] (URL not confirmed), the row is not marked people-disagree.

## Definitions people disagree on

- There is no single agreed legal definition of 'terrorism'. The 1937 League convention (Art. 1), UNSC 1566 (para. 3), the 1999 Financing Convention (Art. 2), EU Directive 2017/541 and national statutes (for example UK Terrorism Act 2000 s.1) all use different formulations. See T-row marked people-disagree.
- Designation lists (US State Department FTO list, UN 1267 list, Australian and Canadian listings) are each government's or body's own designations. They are attributed as such and are not adopted in this pack.
- 'Counterterrorism' versus 'countering violent extremism' versus 'preventing violent extremism' are treated as distinct by some sources (for example GAO-17-300). This pack keeps each source's own term.

## Unreachable or unconfirmed URLs (verified = no)

- EU-CTSTRAT2005: https://data.consilium.europa.eu/doc/document/ST-14469-2005-REV-4/en/pdf (HTTP 200; expected title text not found. PDF fetched (HTTP 200) but its text layer is unreadable; title not machine-confirmed.)
- COE-ECST1977: https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=090 (HTTP 403.)
- COE-CPT2005: https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=196 (HTTP 403.)
- OAS-CICTE2002: https://www.oas.org/juridico/english/treaties/a-66.html (HTTP 503.)
- OAS-CICTE: https://www.oas.org/en/sms/cicte/ (HTTP 503. Undated web page; date [UNKNOWN].)
- US-NSCT2018: https://www.dni.gov/files/NCTC/documents/news_documents/NSCT.pdf (HTTP 403.)
- US-OH-SCT: https://history.state.gov/departmenthistory/people/principalofficers/coordinator-counterterrorism (HTTP 200; expected title text not found. HTTP 200 but page body is a script shell; entry text not present in HTML. Undated web page; date [UNKNOWN].)
- CRS-R43983: https://crsreports.congress.gov/product/pdf/R/R43983 (HTTP 403. CRS is a congressional research agency; listed as scholarly/secondary per brief.)
- UK-AvSSHD2004: https://www.bailii.org/uk/cases/UKHL/2004/56.html (HTTP 200; expected title text not found. BAILII served a bot-check page (curl and WebFetch 403).)
- UK-MAI: https://manchesterarenainquiry.org.uk/ (HTTP 405. Human-verification page (HTTP 405). Undated web page; date [UNKNOWN].)
- DE-GTAZ: https://www.bka.de/DE/UnsereAufgaben/Kooperationen/GTAZ/gtaz_node.html (HTTP 000. Undated web page; date [UNKNOWN].)
- IN-NIA: https://nia.gov.in/ (HTTP 000. Undated web page; date [UNKNOWN].)
- KE-POTA2012: http://kenyalaw.org/kl/fileadmin/pdfdownloads/Acts/PreventionofTerrorismAct_No30of2012.pdf (HTTP 500. URL not confirmed (HTTP 500).)
- PH-RA11479: https://www.officialgazette.gov.ph/2020/07/03/republic-act-no-11479/ (HTTP 403.)
- BR-L13260: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2016/lei/l13260.htm (HTTP 200; expected title text not found. Request redirected to the Planalto home page (https://www.gov.br/planalto/pt-br); law text not reached.)
- CAMPBELL2006: https://onlinelibrary.wiley.com/doi/10.4073/csr.2006.2 (HTTP 403.)
- OHCHR-SR-CT: https://www.ohchr.org/en/special-procedures/sr-terrorism (HTTP 403. Undated web page; date [UNKNOWN].)
- OHCHR-FS32: https://www.ohchr.org/sites/default/files/Documents/Publications/Factsheet32EN.pdf (HTTP 403.)
- CHR-2005-80: https://undocs.org/E/CN.4/RES/2005/80 (HTTP 200; expected title text not found. UN ODS returned a loading page instead of the PDF.)
- ID-BNPT: https://www.bnpt.go.id/ (HTTP 200; expected title text not found. Bot-detection page. Undated web page; date [UNKNOWN].)
- CA-LISTED: https://www.publicsafety.gc.ca/cnt/ntnl-scrt/cntr-trrrsm/lstd-ntts/crrnt-lstd-ntts-en.aspx (HTTP 000. Undated web page; date [UNKNOWN].)

## Dropped candidates (guessed URLs that failed; not in sources.csv)

- US-OH-IRAN: The Iranian Hostage Crisis (Milestones 1977-1980) (https://history.state.gov/milestones/1977-1980/iran-hostage-crisis): guessed URL returned 404
- IN-UAPA1967: The Unlawful Activities (Prevention) Act, 1967 (https://www.mha.gov.in/sites/default/files/A1967-37.pdf): guessed MHA URL returned 404
- CIA-SSCI-RESP2013: CIA Comments on the Senate Select Committee on Intelligence Report on the Rendition, Detention, and Interrogation Program (https://www.cia.gov/readingroom/docs/CIAs_June2013_Response_to_the_SSCI_Study_on_the_Former_Detention_and_Interrogation_Program.pdf): guessed URL resolved to reading-room home page; document not located
- AI-CT-TOPIC: Counter-terror and security (topic page) (https://www.amnesty.org/en/what-we-do/counter-terror-and-security/): guessed URL returned 404; not a confirmed source
- NG-TPA2022: Terrorism (Prevention and Prohibition) Act, 2022 (https://www.nfiu.gov.ng/images/Downloads/downloads/TPPA2022.pdf): guessed URL returned 404

## Not-proven timeline rows

- T015: cites COE-ECST1977
- T061: cites OAS-CICTE2002
- T070: cites PE-CVR
- T084: cites CHR-2005-80
- T085: cites COE-CPT2005
- T088: cites EU-CTSTRAT2005
- T117: cites BR-L13260
- T129: cites PH-RA11479

## Caveats

- Sources were chosen by hand and are not a systematic sample. Counts describe this pack only.
- Era, region and theme tags are single-valued. Many sources span several categories.
- Origin 'international' covers UN, treaty and regional bodies. 'Oversight' covers inspectors general, parliamentary committees, independent reviewers, inquiries and commissions, and UN special procedures. RAND, IEP and ICCT are tagged academic.
- Undated web pages carry date [UNKNOWN]. Their content may change after 2026-11-18.
- The pack contains no operational or tactical content. Attacks are recorded only as dated public events that drove policy.
- The pack contains no personal data about private individuals. Named people appear only where an official title or record names them (for example, a court case name or a head of state).
- Everything is local. Nothing was uploaded or pushed.

