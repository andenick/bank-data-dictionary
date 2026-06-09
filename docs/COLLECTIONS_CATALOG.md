# Universe of US Bank Regulatory Data - Master Collections Catalogue

> **bank-data-dictionary v6.0.** A single map of *every* major US bank/credit-union
> regulatory data collection and its sub-schedules. Every fact here is sourced from an
> official `.gov` (or, for the Pillar 3 international standard, `bis.org`) document. The
> machine-readable companions are [`../csv/COLLECTIONS_CATALOG.csv`](../csv/COLLECTIONS_CATALOG.csv),
> [`../csv/SCHEDULES_CATALOG.csv`](../csv/SCHEDULES_CATALOG.csv), and
> [`../json/collections.json`](../json/collections.json). Captured 2026-06-09.

This catalogue spans **42 collections** and **265 enumerated schedules / sub-schedules /
templates**. It is organised by the body that collects the data:

- **Federal Reserve** - the FR Y-series (holding-company financials, structure/ownership,
  capital & stress testing, liquidity, deposits) plus the MDRM data dictionary.
- **FFIEC (joint FDIC / Federal Reserve / OCC)** - the Call Report (FFIEC 031/041/051), the
  foreign-bank and country-exposure reports (FFIEC 002/002S, 009/009a), the advanced-capital
  and market-risk reports (FFIEC 101, 102), and the derived UBPR.
- **FDIC** - Statistics on Depository Institutions (SDI), Summary of Deposits (SOD), and the
  failures / Research Information System (RIS) record.
- **NCUA** - the 5300 Call Report for credit unions.
- **OCC** - the historical national-bank Reports of Condition (1863-1941).
- **SEC** - EDGAR filings of public bank holding companies.
- **CFPB / FFIEC** - HMDA loan-level mortgage data.
- **International standard / cross-cutting** - the Basel III **Pillar 3** public-disclosure
  templates, the FFIEC **NIC/NPW** institutional-structure bulk data, and the **MDRM**
  meta-dictionary that codes the whole Fed/FFIEC universe.

> **Identifier note.** RSSD ID is the spine that joins the Fed/FFIEC universe; FDIC datasets
> key on CERT, SEC EDGAR on CIK, and HMDA (2018-forward) on LEI. See
> [IDENTIFIERS.md](IDENTIFIERS.md) for the full crosswalk and reuse rules.

## Master table - all collections

| Form / collection | Name | Filer | Frequency | Primary ID | OMB | Source |
|---|---|---|---|---|---|---|
| FR Y-9C | Consolidated Financial Statements for Holding Companies | Top-tier BHCs, SLHCs, IHCs and SHCs with total consolidated assets of $3 billion or more | Quarterly | RSSD ID | 7100-0128 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-9C) |
| FR Y-9LP | Parent Company Only Financial Statements for Large Holding Companies | Parent of each top-tier holding company that files the FR Y-9C | Quarterly | RSSD ID | 7100-0128 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-9LP) |
| FR Y-9SP | Parent Company Only Financial Statements for Small Holding Companies | Top-tier domestic BHCs, SLHCs and SHCs with total consolidated assets of less than $3 billion | Semiannual | RSSD ID | 7100-0128 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-9SP) |
| FR Y-9ES | Financial Statements for Employee Stock Ownership Plan Holding Companies | All ESOP bank holding companies and ESOP savings-and-loan holding companies | Annual | RSSD ID | 7100-0128 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-9ES) |
| FR Y-9CS | Supplement to the Consolidated Financial Statements for Holding Companies | Domestic BHCs, SLHCs, IHCs and SHCs filing the FR Y-9C or FR Y-9SP, as designated when activated | Quarterly or semiannual when activated | RSSD ID | 7100-0128 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-9CS) |
| FR Y-7 | Annual Report of Foreign Banking Organizations | Each FBO engaged in banking in the US through a subsidiary bank, Edge/agreement corporation, commercial-lending company, or its own branches/agencies | Annual | RSSD ID | 7100-0125 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-7) |
| FR Y-7N | Financial Statements of U.S. Nonbank Subsidiaries Held by FBOs | FBOs, per US nonbank subsidiary, by asset-size thresholds | Quarterly or annual | RSSD ID | 7100-0073 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-7NFR_Y-7NS) |
| FR Y-7NS | Abbreviated Financial Statements of U.S. Nonbank Subsidiaries Held by FBOs | FBOs with US nonbank subsidiaries of assets $250M-$500M | Annual | RSSD ID | 7100-0073 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-7NFR_Y-7NS) |
| FR Y-7Q | Capital and Asset Report for Foreign Banking Organizations | All FBOs with US banking operations | Quarterly (FHC FBOs) or annual | RSSD ID | 7100-0125 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-7Q) |
| FR Y-10 | Report of Changes in Organizational Structure | Top-tier BHCs/FHCs, top-tier SLHCs, state member banks not controlled by a BHC/FBO, Edge and agreement corporations, FBOs, and SHCs | Event-based (within 30 days) | RSSD ID | 7100-0297 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-10) |
| FR Y-11 | Financial Statements of U.S. Nonbank Subsidiaries of U.S. Holding Companies | Top-tier holding companies, per nonbank subsidiary, by thresholds | Quarterly or annual | RSSD ID | 7100-0244 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-11FR_Y-11S) |
| FR Y-11S | Abbreviated Financial Statements of U.S. Nonbank Subsidiaries of U.S. Holding Companies | Top-tier holding companies with nonbank subsidiaries of assets $250M-$500M | Annual | RSSD ID | 7100-0244 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-11FR_Y-11S) |
| FR Y-12 | Consolidated Holding Company Report of Equity Investments in Nonfinancial Companies | Top-tier domestic holding companies that file the FR Y-9C or FR Y-9SP and meet the investment-size thresholds | Quarterly or semiannual | RSSD ID | 7100-0300 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-12) |
| FR Y-12A | Annual Report of Merchant Banking Investments Held for an Extended Period | Financial holding companies holding nonfinancial merchant-banking investments beyond the routine holding period | Annual | RSSD ID | 7100-0300 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-12A) |
| FR Y-6 | Annual Report of Holding Companies | All top-tier holding companies (BHCs, SLHCs, SHCs; certain ESOPs; non-QFBO foreign organizations) | Annual | RSSD ID | 7100-0124 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-6) |
| FR Y-8 | The Bank Holding Company Report of Insured Depository Institutions' Section 23A Transactions | All top-tier US BHCs (incl. FHCs and IHCs), all SLHCs, and all FBOs that directly own a US subsidiary bank | Quarterly | RSSD ID | 7100-0126 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-8) |
| FR Y-14A | Capital Assessments and Stress Testing Report - Annual | US BHCs, IHCs of foreign banking organizations, and covered SLHCs with total consolidated assets of $100 billion or more | Annual | RSSD ID | 7100-0341 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14A) |
| FR Y-14Q | Capital Assessments and Stress Testing Report - Quarterly | US BHCs, IHCs, covered SLHCs with $100 billion or more in total consolidated assets | Quarterly | RSSD ID | 7100-0341 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14Q) |
| FR Y-14M | Capital Assessments and Stress Testing Report - Monthly | US BHCs, IHCs, covered SLHCs with $100 billion or more in total consolidated assets that hold the relevant portfolios | Monthly | RSSD ID | 7100-0341 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-14M) |
| FR Y-15 | Banking Organization Systemic Risk Report | US BHCs and covered SLHCs >= $100B; FBOs with combined US assets >= $100B; and US firms designated as G-SIBs | Quarterly | RSSD ID | 7100-0352 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-15) |
| FR 2052a | Complex Institution Liquidity Monitoring Report | Large banking organizations subject to LCR/NSFR - primarily Category I-III firms | Daily (largest) or monthly | RSSD ID | 7100-0361 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_2052a) |
| FR 2900 | Report of Transaction Accounts, Other Deposits, and Vault Cash | Depository institutions under Regulation D | Weekly or quarterly | RSSD ID | 7100-0087 | [link](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_2900_(Commercial_Banks)) |
| FFIEC 031 | Consolidated Reports of Condition and Income (domestic and foreign offices) | Banks with a foreign office; also domestic-only advanced-approaches banks or banks with total assets >= $100 billion | Quarterly | RSSD ID | n/a | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec031) |
| FFIEC 041 | Consolidated Reports of Condition and Income (domestic offices only) | Banks with domestic offices only and total consolidated assets < $100 billion, not advanced-approaches | Quarterly | RSSD ID | n/a | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec041) |
| FFIEC 051 | Consolidated Reports of Condition and Income (streamlined, small domestic banks) | Banks with domestic offices only and total assets < $5 billion (eligible) | Quarterly | RSSD ID | n/a | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec051) |
| FFIEC 002 | Report of Assets and Liabilities of U.S. Branches and Agencies of Foreign Banks | All US branches and agencies of foreign (and Puerto Rican) banks, including their IBFs | Quarterly | RSSD ID | 7100-0032 | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec002) |
| FFIEC 002S | Report of a Non-U.S. Branch Managed or Controlled by a U.S. Branch or Agency of a Foreign Bank | Any US branch/agency filing the FFIEC 002 that manages or controls non-US branches of its parent bank | Quarterly | RSSD ID | 7100-0032 | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec002s) |
| FFIEC 009 | Country Exposure Report | US banks, savings associations, bank/SLHC and IHCs with >= $30M in total claims on foreign residents | Quarterly | RSSD ID | 7100-0035 | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec009) |
| FFIEC 009a | Country Exposure Information Report | Same filers as FFIEC 009 with material foreign-country exposures | Quarterly | RSSD ID | 7100-0035 | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec009) |
| FFIEC 101 | Regulatory Capital Reporting (Advanced Capital Adequacy Framework) | Banks, savings associations, BHCs and SLHCs subject to the advanced approaches (generally >= $250B assets or >= $10B foreign exposure) | Quarterly | RSSD ID | 7100-0319 / 1557-0239 / 3064-0159 | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec101) |
| FFIEC 102 | Market Risk Regulatory Report | Banks/BHCs/SLHCs subject to the market-risk capital rule | Quarterly | RSSD ID | 7100-0365 / 1557-0325 / 3064-0199 | [link](https://www.ffiec.gov/resources/reporting-forms/ffiec102) |
| UBPR | Uniform Bank Performance Report | All banks - derived from each bank's Call Report, not directly filed | Quarterly | RSSD ID | n/a | [link](https://www.ffiec.gov/data/ubpr/uniform-bank-performance-report) |
| FDIC SDI | Statistics on Depository Institutions | All FDIC-insured commercial banks and savings institutions | Quarterly | FDIC CERT | n/a | [link](https://www.fdic.gov/node/118336) |
| FDIC SOD | Summary of Deposits | All FDIC-insured institutions with branch offices | Annual (June 30) | FDIC CERT | n/a | [link](https://www.fdic.gov/bank-financial-reports/summary-deposits) |
| FDIC Failures | Failures and Assistance Transactions (RIS) | Failed and FDIC-assisted institutions | Updated weekly | FDIC CERT | n/a | [link](https://www.fdic.gov/bank-failures/failed-bank-list) |
| NCUA 5300 | NCUA 5300 Call Report (Credit Unions) and Profile (FS220A) | All federally insured credit unions (FICUs) | Quarterly | NCUA Charter / ID | n/a | [link](https://ncua.gov/regulation-supervision/regulatory-reporting/cuonline/5300-call-report-faqs) |
| OCC Historical | OCC Historical National Bank Reports (Annual Report of the Comptroller of the Currency) | National banks via periodic Reports of Condition, 1863-1941 | Annual / periodic (historical) | OCC Charter | n/a | [link](https://fraser.stlouisfed.org/title/annual-report-comptroller-currency-56) |
| SEC EDGAR | SEC EDGAR (bank holding company filings) | Public bank holding companies and other registrants | Event-based / periodic | CIK | n/a | [link](https://www.sec.gov/edgar/search/) |
| HMDA | Home Mortgage Disclosure Act LAR | Covered depository and non-depository mortgage lenders meeting coverage tests | Annual | LEI (pre-2018: Agency Code + Respondent ID) | n/a | [link](https://ffiec.cfpb.gov) |
| Pillar 3 | Basel III Public Disclosure Templates and Tables | Internationally large/advanced banks; in the US, advanced-approaches and market-risk-rule institutions | Mixed by template | N/A | n/a | [link](https://www.bis.org/bcbs/publ/d455.pdf) |
| NIC/NPW | National Information Center / NPW Institutional-Structure Bulk Data | All entities the Fed tracks | Refreshed regularly | RSSD ID (ID_RSSD) | n/a | [link](https://www.ffiec.gov/NPW) |
| MDRM | Micro Data Reference Manual | Meta-dictionary across (nearly) every Fed/FFIEC reporting form | N/A | 8-char MDRM code | n/a | [link](https://www.federalreserve.gov/apps/mdrm/) |

> The FFIEC 031/041/051, UBPR and FDIC/NCUA/OCC/SEC/HMDA cells show OMB as **n/a** because the
> source files did not state an OMB control number for those collections; treat as not-yet-verified
> rather than absent. Per-schedule enumeration with 031/041/051 coverage flags lives in
> [`../csv/SCHEDULES_CATALOG.csv`](../csv/SCHEDULES_CATALOG.csv).

---

## By family

### Federal Reserve FR Y-9 family (holding-company financials)

FR Y-9C, FR Y-9LP, FR Y-9SP, FR Y-9ES, FR Y-9CS - all under **OMB 7100-0128**. The FR Y-9C is
the flagship consolidated report (22 schedules: 4 income-statement "HI" schedules plus 18
balance-sheet "HC" schedules, with HI-B and HC-R each split into Part I and Part II). The MDRM
prefix **BHCK is the consolidated prefix** (BHDM = domestic offices only); BHCP = FR Y-9LP
parent-only, BHSP = FR Y-9SP, ESOP = FR Y-9ES.

- Detailed guide: [CALL_REPORT_GUIDE.md](CALL_REPORT_GUIDE.md) (Call Report / FR Y-9C structural overlap) and the per-schedule HC*/HI guides in this `docs/` directory.
- Forms index: https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-9C

### Call Report - FFIEC 031 / 041 / 051

The bank-level Reports of Condition and Income, collected jointly by the FDIC, Federal Reserve
and OCC. Three forms by office type, asset size, and capital framework: **FFIEC 031** (domestic
and foreign offices, or advanced-approaches / >= $100B), **FFIEC 041** (domestic only, < $100B),
**FFIEC 051** (streamlined, domestic-only < $5B; adds Schedule SU). The foreign-office schedules
**RC-H, RC-I, RI-D** and the three-column **RCFD / RCON / RCFN** structure are **031-only**; the
**051** drops RC-A, RC-D, RC-P, RC-Q, RC-S, RC-V. Coverage per form is flagged in
`SCHEDULES_CATALOG.csv` (`in_031` / `in_041` / `in_051`).

> **Schedule-count convention (read this before comparing numbers).** The number of
> **distinct lettered schedules** per form is **27 (031) / 24 (041) / 19 (051)** — each lettered
> schedule counted once. The machine-readable catalog (`SCHEDULES_CATALOG.csv` coverage flags and
> the per-form `schedule_count` in `collections.json`) counts schedule **parts** as separate rows,
> giving **30 / 27 / 22**. The +3 on each form is exactly the three Part I/Part II schedules
> (**RI-B**, **RC-C**, **RC-R**), each carried as two rows. These are real Call Report parts, not
> invented schedules. See [CALL_REPORT_GUIDE.md](CALL_REPORT_GUIDE.md) for the full breakdown.

- Detailed guide: [CALL_REPORT_GUIDE.md](CALL_REPORT_GUIDE.md)
- Instructions (Mar 2025): https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202503_i.pdf
- FFIEC 051 instructions (Dec 2024): https://www.ffiec.gov/sites/default/files/data/reporting-forms/hv-051/FFIEC051_202412_i.pdf

### Foreign banking organizations, international exposure & Fed structure reports

FFIEC 002 / 002S (US branches/agencies of foreign banks), FFIEC 009 / 009a (country exposure),
and the Fed structure/ownership series: FR Y-7, Y-7N, Y-7NS, Y-7Q, Y-10, Y-11, Y-11S, Y-12,
Y-12A, Y-6, Y-8.

- Detailed guide: [FOREIGN_AND_STRUCTURE_GUIDE.md](FOREIGN_AND_STRUCTURE_GUIDE.md)
- FFIEC 002: https://www.ffiec.gov/resources/reporting-forms/ffiec002 - FFIEC 009: https://www.ffiec.gov/resources/reporting-forms/ffiec009

### Capital, risk, stress-test & liquidity collections

FFIEC 101 (advanced-approaches capital, Schedules A-S), FFIEC 102 (market risk), FR Y-14A/Q/M
(CCAR/DFAST, OMB 7100-0341), FR Y-15 (G-SIB systemic-risk indicators), FR 2052a (liquidity),
FR 2900 (deposits & vault cash), and the Basel III **Pillar 3** public-disclosure templates.

- Detailed coverage in the per-form guides: [FFIEC_101_ADVANCED_CAPITAL_GUIDE.md](FFIEC_101_ADVANCED_CAPITAL_GUIDE.md), [FFIEC_102_MARKET_RISK_GUIDE.md](FFIEC_102_MARKET_RISK_GUIDE.md), [FR_Y14_CAPITAL_ASSESSMENT_GUIDE.md](FR_Y14_CAPITAL_ASSESSMENT_GUIDE.md), [FR_Y15_SYSTEMIC_RISK_GUIDE.md](FR_Y15_SYSTEMIC_RISK_GUIDE.md), [FR_2052a_LIQUIDITY_GUIDE.md](FR_2052a_LIQUIDITY_GUIDE.md), [PILLAR3_DISCLOSURE_GUIDE.md](PILLAR3_DISCLOSURE_GUIDE.md).
- Pillar 3 standard (BCBS d455): https://www.bis.org/bcbs/publ/d455.pdf

> **Pillar 3 template count.** `SCHEDULES_CATALOG.csv` enumerates **77 Pillar 3 templates and
> tables** — the full consolidated Basel disclosure (DIS) set as updated by BCBS d455: the
> ~18 qualitative **tables** (A-suffix: OVA, LIA, CRA, CRB, CRB-A, CRC, CRD, CRE, CCRA, SECA, MRA,
> MRB, CVAA, CVAB, ORA, IRRBBA, REMA, LIQA) plus the ~59 quantitative **templates** (KM/OV/CC/LR/
> TLAC/GSIB/CCyB/LIQ/CR/CCR/SEC/MR/CVA/OR/IRRBB/REM/ENC/CMS/PV/CDC). This is larger than the
> "~55" figure in some summaries because those count only quantitative templates or a single
> framework vintage. All 77 ids were checked against the BCBS DIS framework: **no invented or
> duplicate ids** (CDC = "Capital distribution constraints" and CRB-A = "prudential treatment of
> problem assets" are both genuine BCBS templates; MR4 is the legacy pre-FRTB VaR-backtesting
> template, retained for the transition period and noted as such). The TLAC templates remain
> flagged UNVERIFIED for US-jurisdiction inclusion.

### FDIC, NCUA, OCC & UBPR (non-Fed depository data)

FDIC SDI (Statistics on Depository Institutions), FDIC SOD (Summary of Deposits), FDIC
Failures/RIS, NCUA 5300 (credit-union Call Report), OCC historical national-bank reports, and the
FFIEC's derived UBPR.

- Detailed guide: [FDIC_NCUA_OCC_UBPR_GUIDE.md](FDIC_NCUA_OCC_UBPR_GUIDE.md)
- FDIC BankFind Suite API: https://api.fdic.gov/banks/docs - NCUA 5300: https://ncua.gov/regulation-supervision/regulatory-reporting/cuonline/5300-call-report-faqs - UBPR: https://www.ffiec.gov/data/ubpr/uniform-bank-performance-report

### Identifiers, NIC/NPW structure data, and cross-cutting collections

The identifier systems (RSSD, FDIC CERT, OCC/NCUA charter, LEI, ABA RTN, EIN, CIK, CUSIP) and the
FFIEC National Information Center (NIC) / NPW bulk structure data that crosswalks them, plus the
cross-cutting SEC EDGAR and HMDA collections.

- Detailed guides: [NIC_STRUCTURE_GUIDE.md](NIC_STRUCTURE_GUIDE.md) and [IDENTIFIERS.md](IDENTIFIERS.md)
- NIC/NPW: https://www.ffiec.gov/NPW - SEC EDGAR: https://www.sec.gov/edgar/search/ - HMDA: https://ffiec.cfpb.gov

### MDRM - the meta-dictionary

The Micro Data Reference Manual is the Federal Reserve's master dictionary of the coded variables
used across (nearly) every Fed/FFIEC form. Each 8-character MDRM code = a 4-char mnemonic prefix
(e.g. RCON, RCFN, RCFD, BHCK) + a 4-char item number, with the same item number reused across
mnemonics for the same concept measured at a different scope.

- Detailed guide: [MDRM_GUIDE.md](MDRM_GUIDE.md)
- MDRM app & download: https://www.federalreserve.gov/apps/mdrm/ - https://www.federalreserve.gov/apps/mdrm/download_mdrm.htm

---

## UNVERIFIED items (carried forward from the cited sources)

The following facts could not be confirmed against a primary source at capture time and are flagged
UNVERIFIED in the source files; they are reproduced here so downstream users do not treat them as
settled:

- **FR Y-9ES** - any asset-size cutoff for ESOP holding companies.
- **FR Y-9CS** - has no fixed lettered schedule structure; schedule enumeration is not applicable / unverified per as-of date.
- **FFIEC 031 / 041 / 051, UBPR, FDIC SDI/SOD/Failures, NCUA 5300, OCC, SEC EDGAR, HMDA** - OMB control numbers were not stated in the source files (shown as n/a).
- **FFIEC 101** - the exact per-letter content of the wholesale counterparty/netting block (Schedules H, I, J) and the exact titles of retail Schedules M and N.
- **FR 2052a** - the exact label of supplemental table S.L (Liquidity Risk Measurement); an `S.C` code seen once in the form is treated as an artifact and not listed.
- **Pillar 3** - jurisdictional inclusion of the TLAC templates (TLAC1, TLAC2, TLAC3).
- **FFIEC 002** - exact title of Schedule C Part II.
- **FFIEC 009** - exact title of Schedule C Part II.
- **NCUA 5300** - whether Schedules E and F are present in the current form (not enumerated in the FAQ source).
- **OCC historical** - the exact column set varies by report year/era; there is no single fixed schema.
- **Call Report RC-R** - the line-item RCOA-vs-RCFA column-prefix assignment is not line-item-confirmed against the MDRM download.
- **MDRM** - the commonly cited "~87,000 codes" figure is an order-of-magnitude estimate, not an official count.
- **NIC/NPW** - the exact published refresh interval of the bulk-download files (use the as-of date embedded in each file).
- **SEC EDGAR** - no official CIK<->RSSD crosswalk is known to be published; the exact current API rate-limit wording was not verifiable against the live page.

> **Repo correction note.** The legacy `csv/MDRM_PREFIX_DEFINITIONS.csv` labels **BHCK** as
> "domestic operations only / pre-2018". The official FR Y-9C form heads its *consolidated* income
> statement and balance sheet with BHCK; the domestic-only prefix is **BHDM**. Treat BHCK as the
> consolidated prefix.
