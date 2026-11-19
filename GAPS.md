# Gaps (round 2)

This file lists what CTA6 has not gathered or could not confirm as of round 2. Items marked `[UNKNOWN]` are gaps, not conclusions. This archive is not complete.

Round 1 gaps are taken from [NOTES.md](NOTES.md) (accessed 2026-11-18). Round 2 additions, retries and remaining gaps are taken from [notes/round-2.md](notes/round-2.md) (accessed 2026-11-18).

## Remaining gaps and regional imbalance

After round 2 the archive has 303 sources and 192 timeline rows. Global/UN, Europe and North America still hold 179 of 303 sources (59%) and 122 of 192 timeline rows (64%). Oceania (4 sources) and Russia/Central Asia (10) remain thin. South Asia has 22 sources but only 6 timeline rows: five of its sources (Pakistan ATA x2, India UAPA (English), NIA pages) could not be verified.

**Not yet covered, or unverified:**

- **Africa.** Algeria after 1992; Morocco Loi 03-03 (unverified); Kenya POTA (unverified); the G5 Sahel and Mali national agencies; Egypt and Nigeria oversight bodies (only NGO sources so far).
- **Latin America.** Colombia (Ley 1121 dropped); Peru and Mexico agencies; Argentina AMIA prosecutor's unit; Inter-American Court Peru cases (URLs not confirmed); IACHR 2002 report (URL not confirmed).
- **Asia.** The Philippines ATA itself (phase 1, still unverified) and the text of the 2021 decision in G.R. No. 252578 (unverified); Malaysia and Singapore oversight; China oversight (only HRW-CHN-2018); Japan and Korea oversight.
- **Central Asia.** Kyrgyzstan, Tajikistan and Turkmenistan laws; Kazakhstan law (unverified); SCO RATS documents beyond the home page; Russia's NAK (dropped).
- **Regional bodies.** OAS/CICTE (site down); SAARC Secretariat page (404); the OIC Convention (522 error, unverified).
- **Oversight.** India NHRC, Pakistan NCHR, Indonesian Komnas HAM, African Court judgments, Turkish Constitutional Court.
- **Languages.** Urdu has only an index page (unverified), and Hindi has one verified Act text. There are no Persian, Hebrew or Japanese originals, and Arabic is limited (3). Round 1 source languages were not recorded and are marked `[UNKNOWN]`.
- 17 pass 2 sources remain unverified, mostly because government sites in South Asia and Morocco time out or run bot checks. 16 phase 1 sources also remain unverified at their cited URL after a retry (12 were still unreachable; 4 were confirmed only at a different official copy).

**Pre-1945.** Rome 1898 still has no official text online (coverage is secondary only). The procès-verbaux locations given by Jensen 1981 were not checked [UNKNOWN]. The place of signing of the 1904 St Petersburg protocol is not stated in the captured sources, so it is `[UNKNOWN]` in T134. Colonial-era emergency laws were not gathered [UNKNOWN].

## Disagreements recorded in round 2

These were listed as open after round 1 and now have a second cited source, recorded as `people-disagree` rows:

- **T072 / T150 (Madrid 2004):** T150 cites SR-ESP-2008 alongside UNSC 1530. T072 still records only what the resolution text says, with a note pointing to T150.
- **T045 / T145 (OAU Convention date):** T145 cites the UN Treaty Collection copy, the AU status list and OAU decision AHG/Dec.132 (14 July 1999) alongside the phase 1 AU treaty page (1 July 1999). T045 keeps the AU treaty-page date and has a note pointing to T145.
- **T113 / T166 (SSCI study):** T166 cites CIA-SSCI-2013 alongside US-SSCI2014.

A further people-disagree row added in round 2, T173, records a difference between Egypt's Official Gazette (Decree-Law No. 94 of 2015) and Human Rights Watch ("Law 95 of 2015").

## Dropped candidates (not in sources.csv)

### Round 1

Five candidate URLs that had been guessed returned 404 or redirected to an unrelated page. They were dropped instead of being kept as unconfirmed sources:

- **US-OH-IRAN:** The Iranian Hostage Crisis (Milestones 1977-1980) (https://history.state.gov/milestones/1977-1980/iran-hostage-crisis): guessed URL returned 404
- **IN-UAPA1967:** The Unlawful Activities (Prevention) Act, 1967 (https://www.mha.gov.in/sites/default/files/A1967-37.pdf): guessed MHA URL returned 404. (A different India Code URL was added in pass 2 as IN-UAPA1967, still unverified.)
- **CIA-SSCI-RESP2013:** CIA Comments on the Senate Select Committee on Intelligence Report on the Rendition, Detention, and Interrogation Program (https://www.cia.gov/readingroom/docs/CIAs_June2013_Response_to_the_SSCI_Study_on_the_Former_Detention_and_Interrogation_Program.pdf): guessed URL resolved to reading-room home page; document not located. (A confirmed copy was added in pass 2 as CIA-SSCI-2013.)
- **AI-CT-TOPIC:** Counter-terror and security (topic page) (https://www.amnesty.org/en/what-we-do/counter-terror-and-security/): guessed URL returned 404; not a confirmed source
- **NG-TPA2022:** Terrorism (Prevention and Prohibition) Act, 2022 (https://www.nfiu.gov.ng/images/Downloads/downloads/TPPA2022.pdf): guessed URL returned 404

### Round 2

13 candidates were dropped in pass 2 (see notes/round-2.md):

- Seven guessed URLs that failed: EU FRA 2021, IACHR 2002, three IACtHR Peru judgments, Colombia Ley 1121, and Russia's NAK site.
- One archive URL that could not be confirmed (NLS LoN 1937).
- Two search URLs that returned 404 (LK-PTA lawnet, SAARC list).
- Three duplicates of phase 1 rows (ZA POCDATARA, ASEAN ACCT, Arab Convention).

## Unconfirmed source URLs (verified = no)

These rows are in `data/sources.csv` but could not be confirmed in this round.

### Phase 1 sources still unverified at the cited URL after a retry (16)

- OAS-CICTE2002: https://www.oas.org/juridico/english/treaties/a-66.html (HTTP 503/500 on retry.)
- OAS-CICTE: https://www.oas.org/en/sms/cicte/ (HTTP 503/500.)
- US-OH-SCT: https://history.state.gov/departmenthistory/people/principalofficers/coordinator-counterterrorism (Retry via WebFetch: page now shows only a notice that Principal Officers database updates are suspended, posted 12 Jan 2024; coordinator list not displayed.)
- CRS-R43983: https://crsreports.congress.gov/product/pdf/R/R43983 (bot check.)
- UK-MAI: https://manchesterarenainquiry.org.uk/ (human-verification page, including at the National Archives web archive.)
- DE-GTAZ: https://www.bka.de/DE/UnsereAufgaben/Kooperationen/GTAZ/gtaz_node.html (timeout/504.)
- IN-NIA: https://nia.gov.in/ (timeout.)
- KE-POTA2012: http://kenyalaw.org/kl/fileadmin/pdfdownloads/Acts/PreventionofTerrorismAct_No30of2012.pdf (A current Kenya Law URL was also added as KE-POTA2012-KL and is still unverified.)
- PH-RA11479: https://www.officialgazette.gov.ph/2020/07/03/republic-act-no-11479/ (403 and timeout.)
- OHCHR-SR-CT: https://www.ohchr.org/en/special-procedures/sr-terrorism (403 and timeout.)
- CHR-2005-80: https://undocs.org/E/CN.4/RES/2005/80 (ODS returns a loading page.)
- ID-BNPT: https://www.bnpt.go.id/ (BunkerWeb human check.)

Five phase 1 sources that were unverified in round 1 are now `verified=yes` at the cited URL (OHCHR-FS32, CA-LISTED, EU-CTSTRAT2005, UK-AvSSHD2004, BR-L13260). UK-AvSSHD2004 had already been confirmed from the official House of Lords session papers, which is now the cited URL.

Four others were confirmed only at a different official copy, so they remain `verified=no` under the rule that `verified=yes` means the cited URL was fetched and matched:

- COE-ECST1977: https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=090 (cited URL returns HTTP 403. Same document confirmed at official copy: https://rm.coe.int/16800771b2)
- COE-CPT2005: https://www.coe.int/en/web/conventions/full-list?module=treaty-detail&treatynum=196 (cited URL returns HTTP 403. Same document confirmed at official copy: https://rm.coe.int/16808c3f55)
- US-NSCT2018: https://www.dni.gov/files/NCTC/documents/news_documents/NSCT.pdf (cited URL returns HTTP 403. Same document confirmed at official copy: https://trumpwhitehouse.archives.gov/wp-content/uploads/2018/10/NSCT.pdf)
- CAMPBELL2006: https://onlinelibrary.wiley.com/doi/10.4073/csr.2006.2 (cited URL returns HTTP 403. Same document confirmed at official copy: https://www.publicsafety.gc.ca/lbrr/archives/cnmcs-plcng/cn88836819-eng.pdf)

### Pass 2 sources still unverified (17)

- HIST-ROME1898-JCH: https://journals.sagepub.com/doi/10.1177/002200948101600205
- IN-UAPA1967: https://www.indiacode.nic.in/handle/123456789/1470
- IN-NIA-UAPA: https://nia.gov.in/uapa
- PK-ATA1997: https://pakistancode.gov.pk/english/UY2FqaJw1-apaUY2Fqa-apaUY2Npappq-sg-jjjjjjjjjjjjj
- PK-ATA1997-FIA: https://www.fia.gov.pk/public/files/laws/2060818757.pdf
- KE-POTA2012-KL: https://new.kenyalaw.org/akn/ke/act/2012/30
- MA-LOI03-03: https://adala.justice.gov.ma/api/uploads/2026/04/30/%D8%B8%D9%80%D9%87%D9%8A%D8%B1%20%D8%B4%D9%80%D8%B1%D9%8A%D9%81%20%D8%B1%D9%82%D9%85%201.03.140%20%D8%A8%D8%AA%D9%86%D9%81%D9%8A%D8%B0%20%D8%A7%D9%84%D9%82%D8%A7%D9%86%D9%88%D9%86%20%D8%B1%D9%82%D9%85%2003.03%20%D8%A7%D9%84%D9%85%D8%AA%D8%B9%D9%84%D9%82%D8%A9%20%D8%A8%D9%85%D9%83%D8%A7%D9%81%D8%AD%D8%A9%20%D8%A7%D9%84%D8%A5%D8%B1%D9%87%D8%A7%D8%A8-1777546049068.pdf
- MA-CNASNU: https://cnasnu.justice.gov.ma/language/fr/corpus-juridique-national/
- PH-SC-2021-252578: https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/1/67914?5hhplJcmuxsbMr=fHsDQ
- AU-POA2002-PSD: https://www.peaceau.org/uploads/au-anti-terrorism-plan-of-action.pdf
- KZ-LAW416-1999: https://adilet.zan.kz/rus/docs/Z990000416_
- OIC-CONV1999: https://bdrive.oic-oci.org/index.php/s/MRknarXLqNDraSj/download
- SA-CTLAW2017: https://laws.boe.gov.sa/Boelaws/Laws/LawDetails/57694209-3eed-46c7-a5d8-a9ed012761d4/1
- KNCHR-2015: http://www.knchr.org/Portals/0/CivilAndPoliticalReports/The%20Error%20of%20Fighting%20Terror%20With%20Terror.pdf
- CNCDH-2017: https://www.cncdh.fr/sites/default/files/2021-04/170706_avis%20sur%20le%20PJL%20s%C3%A9curit%C3%A9%20int%C3%A9rieure_terrorisme%20p%C3%A0p.pdf
- IN-NIA-UAPA-HI: https://nia.gov.in/hi/uapa
- PK-CODE-URDU: https://www.pakistancode.gov.pk/english/UHyrdu.php

## Not-proven timeline rows

Phase 1:

- T015: cites COE-ECST1977
- T061: cites OAS-CICTE2002
- T070: cites PE-CVR (source page was fetched, but the release date is not printed on that page)
- T084: cites CHR-2005-80
- T085: cites COE-CPT2005
- T088: cites EU-CTSTRAT2005 (source is now `verified=yes` after a pass 2 retry; no correction changed this row's status, so it stays `not-proven`)
- T117: cites BR-L13260 (source is now `verified=yes` after a pass 2 retry; no correction changed this row's status, so it stays `not-proven`)
- T129: cites PH-RA11479

Pass 2:

- T169: cites ACHPR-CT2015 (year taken from a search listing)
- T186: cites PH-SC-2021-252578 (decision text not captured; docket page verified)

## Confirmed from another official copy (round 1 review and pass 2 retries)

- **UK-AvSSHD2004 / T080:** The BAILII URL remained blocked. The judgment was confirmed from the official House of Lords session papers at https://publications.parliament.uk/pa/ld200405/ldjudgmt/jd041216/a&oth-1.htm (title, date 16 December 2004, [2004] UKHL 56). The declaration that section 23 of the 2001 Act is incompatible with articles 5 and 14 of the European Convention is in paragraph 73 of the same judgment (https://publications.parliament.uk/pa/ld200405/ldjudgmt/jd041216/a&oth-5.htm). The source is marked `verified=yes`.
