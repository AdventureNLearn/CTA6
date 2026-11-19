# Gaps (round 1)

This file lists what round 1 of CTA6 did not gather or could not confirm. Items marked `[UNKNOWN]` are gaps, not conclusions. This archive is not complete.

The lists below are taken from the round 1 source-gathering record in [NOTES.md](NOTES.md) (accessed 2026-11-18).

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

## Disagreements not yet sourced on both sides

These are noted in the gathering record but do not yet have a second cited source, so they are not marked `people-disagree`:

- Madrid 2004: UNSC 1530's operative text attributes the bombings to ETA. Whether later official or judicial records support or contest this attribution was not checked in this pass [UNKNOWN]. The timeline row records only what the resolution text says.
- OAU Convention date: the AU treaty page gives adoption 1 Jul 1999. This date was not cross-checked against a second source [UNKNOWN].
- SSCI 2014 study: the published volume includes the committee's additional and minority views, and the CIA issued a 2013 response. Because the CIA document is [UNKNOWN] (URL not confirmed), the row is not marked `people-disagree`.

## Dropped candidates (not in sources.csv)

Five candidate URLs that had been guessed returned 404 or redirected to an unrelated page. They were dropped instead of being kept as unconfirmed sources:

- **US-OH-IRAN:** The Iranian Hostage Crisis (Milestones 1977-1980) (https://history.state.gov/milestones/1977-1980/iran-hostage-crisis): guessed URL returned 404
- **IN-UAPA1967:** The Unlawful Activities (Prevention) Act, 1967 (https://www.mha.gov.in/sites/default/files/A1967-37.pdf): guessed MHA URL returned 404
- **CIA-SSCI-RESP2013:** CIA Comments on the Senate Select Committee on Intelligence Report on the Rendition, Detention, and Interrogation Program (https://www.cia.gov/readingroom/docs/CIAs_June2013_Response_to_the_SSCI_Study_on_the_Former_Detention_and_Interrogation_Program.pdf): guessed URL resolved to reading-room home page; document not located
- **AI-CT-TOPIC:** Counter-terror and security (topic page) (https://www.amnesty.org/en/what-we-do/counter-terror-and-security/): guessed URL returned 404; not a confirmed source
- **NG-TPA2022:** Terrorism (Prevention and Prohibition) Act, 2022 (https://www.nfiu.gov.ng/images/Downloads/downloads/TPPA2022.pdf): guessed URL returned 404

## Unconfirmed source URLs (verified = no)

These rows are in `data/sources.csv` but could not be confirmed in this round. Timeline rows that cite them are marked `not-proven`.

- EU-CTSTRAT2005: https://data.consilium.europa.eu/doc/document/ST-14469-2005-REV-4/en/pdf (HTTP 200; expected title text not found. PDF fetched (HTTP 200) but its text layer is unreadable; title not machine-confirmed.)
- COE-ECST1977: https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=090 (HTTP 403.)
- COE-CPT2005: https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=196 (HTTP 403.)
- OAS-CICTE2002: https://www.oas.org/juridico/english/treaties/a-66.html (HTTP 503.)
- OAS-CICTE: https://www.oas.org/en/sms/cicte/ (HTTP 503. Undated web page; date [UNKNOWN].)
- US-NSCT2018: https://www.dni.gov/files/NCTC/documents/news_documents/NSCT.pdf (HTTP 403.)
- US-OH-SCT: https://history.state.gov/departmenthistory/people/principalofficers/coordinator-counterterrorism (HTTP 200; expected title text not found. HTTP 200 but page body is a script shell; entry text not present in HTML. Undated web page; date [UNKNOWN].)
- CRS-R43983: https://crsreports.congress.gov/product/pdf/R/R43983 (HTTP 403. CRS is a congressional research agency; listed as scholarly/secondary per brief.)
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

## Not-proven timeline rows

- T015: cites COE-ECST1977
- T061: cites OAS-CICTE2002
- T070: cites PE-CVR (source page was fetched, but the release date is not printed on that page)
- T084: cites CHR-2005-80
- T085: cites COE-CPT2005
- T088: cites EU-CTSTRAT2005
- T117: cites BR-L13260
- T129: cites PH-RA11479

T070 is the one not-proven row whose cited source is marked `verified=yes`. The other seven cite a source marked `verified=no`.

## Confirmed from another official copy

- **UK-AvSSHD2004 / T080:** The BAILII URL remained blocked. The judgment was confirmed from the official House of Lords session papers at https://publications.parliament.uk/pa/ld200405/ldjudgmt/jd041216/a&oth-1.htm (title, date 16 December 2004, [2004] UKHL 56). The declaration that section 23 of the 2001 Act is incompatible with articles 5 and 14 of the European Convention is in paragraph 73 of the same judgment (https://publications.parliament.uk/pa/ld200405/ldjudgmt/jd041216/a&oth-5.htm). The source is now marked `verified=yes`.

## Round 2 items

These remain open after Review of round 1. They are not yet done.

- **T072 (Madrid 2004):** Add a second source on the Madrid attribution from the Spanish court records. In this round the row records only what UNSC 1530's text says; later official or judicial records were not checked [UNKNOWN].
- **T045 (OAU Convention date):** Check the adoption date against the treaty text. In this round the date 1999-07-01 is as given on the AU treaty page and was not cross-checked against a second source [UNKNOWN].
