# Non-Fed Depository-Institution Data Collections + UBPR

Catalogue of **non-Federal-Reserve** depository-institution data collections — **FDIC**
(SDI, Summary of Deposits, Failures), **NCUA** (5300 credit-union Call Report + Profile),
**OCC** (historical national-bank reports) — plus the FFIEC's **Uniform Bank Performance
Report (UBPR)**. These complement the Fed/FFIEC forms documented elsewhere in this repo; the
MDRM meta-dictionary that ties the Fed universe together is covered separately in
**[`MDRM_GUIDE.md`](./MDRM_GUIDE.md)**.

All facts are sourced to official `.gov` sites. Unconfirmed numbers are flagged **UNVERIFIED**.

> **FDIC API host note:** the documented host `banks.data.fdic.gov/api/…` now issues
> `301 Moved Permanently` redirects to `api.fdic.gov/banks/…`. Both are official FDIC hosts;
> the canonical base for live calls is **`https://api.fdic.gov/banks/`**.

---

## 1. FDIC SDI — Statistics on Depository Institutions

| Attribute | Detail |
|---|---|
| **Purpose** | Quarterly financial and structural statistics for every FDIC-insured institution; the FDIC's public presentation layer over Call Report / thrift data. |
| **Who collects** | Federal Deposit Insurance Corporation (FDIC). |
| **Who files** | All FDIC-insured commercial banks and savings institutions (data sourced from their Call Reports). |
| **Frequency** | Quarterly (financial reports), downloadable back to 1984. |
| **Relationship to Call Report** | Derived from the Reports of Condition and Income (FFIEC 031/041/051) + thrift data; repackages them as standardized, queryable financial variables plus computed performance metrics. SDI is the FDIC analog/companion to the FFIEC UBPR. |
| **Official URL** | https://www.fdic.gov/node/118336 (SDI home); downloads https://www.fdic.gov/resources/tools/bank-data-guide/data-download.html |
| **API base** | `https://api.fdic.gov/banks/` (was `https://banks.data.fdic.gov/api/`) |
| **API docs** | https://api.fdic.gov/banks/docs |

### FDIC BankFind Suite API — endpoints (8 datasets)

| Endpoint | Path | Returns |
|---|---|---|
| Institutions | `/banks/institutions` (was `/api/institutions`) | Current + historical institution master records (one per CERT): name, charter/regulator, location, class, status. |
| Financials | `/banks/financials` | The SDI financial data — quarterly balance sheet, income statement, capital and performance metrics per institution-period. |
| History | `/banks/history` | Structure-change events (mergers, charter changes, failures, name/address changes). |
| Locations | `/banks/locations` | Branch/office location records for active institutions. |
| SOD | `/banks/sod` | Summary of Deposits — annual branch-level deposit survey (see §2). |
| Failures | `/banks/failures` | Failed & assisted institution records (see §3). |
| Summary | `/banks/summary` | Annual aggregate financial summaries across all insured institutions. |
| Demographics | `/banks/demographics` | Demographic / aggregate population context data. |

Query syntax is Elasticsearch-style (`NAME:"First Bank"`, `!(STNAME:"Virginia")`, AND/OR,
date ranges `yyyy-mm-dd`, numeric ranges). Output JSON or CSV via `Accept` header / `format=`.
API key optional (recommended, not required).

### SDI / `financials` field groups (representative — hundreds of variables)

| Group | Example fields |
|---|---|
| Assets | `ASSET`, `NAASSET` (noncurrent assets), `P3ASSET`/`P9ASSET` (past-due buckets) |
| Liabilities | `LIAB`, `DEPDOM`, `DEPNIDOM` (noninterest-bearing dom.), `DEPIDOM` (interest-bearing dom.) |
| Equity / capital | `EQ`, `EQTOT`, `EQCDIV`, `RBC1AAJ` (tier-1 leverage), risk-based capital ratios |
| Income | `INTINC`, `NETINC`, `NIM`/`NIMY` (net interest margin) |
| Expense | `EINTEXP`, `INTEXPY` (interest expense) |
| Performance ratios | `ROA`, `ROE`, `ROEINJR`, `NPERFV` |
| Deposits | `DEP`, `COREDEP`, `DEPINS` (insured), `DEPUNINS` (uninsured) |
| Identifiers | `CERT` (FDIC certificate #), `NUMEMP`, `INSDATE`, `ENDEFYMD` |

> Exact total field count per period is **UNVERIFIED** — the live `financials` default
> projection returns ~85 fields, but the full SDI variable set is materially larger. Use the
> API definition file / SDI data dictionary for the authoritative list.

---

## 2. FDIC Summary of Deposits (SOD)

| Attribute | Detail |
|---|---|
| **Purpose** | Branch/office-level deposit totals — the only public source of deposit data at the individual-office level (market-share / branch-network analysis). |
| **Who collects** | FDIC (jointly with OCC for the survey). |
| **Who files** | All FDIC-insured institutions with branch offices, including insured U.S. branches of foreign banks. |
| **Frequency** | Annual snapshot as of **June 30**; history back to 1994. Covers 70,000+ domestic offices of 4,000+ institutions. |
| **Official URL** | https://www.fdic.gov/bank-financial-reports/summary-deposits ; explorer https://banks.data.fdic.gov/bankfind-suite/SOD |
| **Reporting instructions** | https://www.fdic.gov/bank-financial-reports/2025-sod-instructions.pdf |
| **API** | `https://api.fdic.gov/banks/sod` (Summary of Deposits home https://www.fdic.gov/bank-financial-reports/summary-deposits) |

### SOD field groups (live schema — 80 fields)

| Group | Example fields |
|---|---|
| Institution ID | `CERT`, `RSSDID`, `DOCKET`, `FDICNAME`, `NAMEFULL`, `BKCLASS`, `CHARTER`, `NAMEHCR`/`RSSDHCR` (holding co.) |
| Branch ID | `BRNUM`, `UNINUMBR` (unique branch #), `NAMEBR`, `BRSERTYP`, `BKMO` (main office flag) |
| Deposits | `DEPSUMBR` (deposits at this branch), `DEPSUM` (institution total), `DEPDOM` |
| Branch address | `ADDRESBR`, `CITYBR`, `STALPBR`, `ZIPBR`, `CITY2BR` |
| Geography | `STCNTYBR`, `CNTYNAMB`, `MSABR`/`MSANAMB`, `CSABR`/`CSANAMBR`, `CBSA_DIV_NAMB`, `SIMS_LATITUDE`/`SIMS_LONGITUDE`, `PLACENUM` |
| Regulatory | `REGAGNT`/`REGNAME`, `FED`/`FEDNAME`, `OCCDIST`, `FDICDBS`, `SPECGRP`/`SPECDESC`, `CALL`/`CLCODE` |
| Misc | `YEAR`, `ESCROW`, `INSURED`, `UNIT`, `DENOVO`, `CONSOLD` |

---

## 3. FDIC Failures & Assistance (Failed Bank List / RIS lineage)

| Attribute | Detail |
|---|---|
| **Purpose** | Record of every institution failure and FDIC-assisted transaction. The web "Failed Bank List" is a subset (failures since Oct 1, 2000); the `failures` dataset goes back to the 1930s. |
| **Who collects** | FDIC (Research Information System / RIS lineage). |
| **Coverage** | ~4,100+ failure/assistance records (live index May 2026). |
| **Frequency** | Updated weekly (BankFind Suite). |
| **Official URL** | Failed Bank List https://www.fdic.gov/bank-failures/failed-bank-list ; explorer https://banks.data.fdic.gov/bankfind-suite/failures ; CSV https://www.fdic.gov/bank-failures/download-data.csv |
| **API** | `https://api.fdic.gov/banks/failures` |

### Failures field groups (live schema)

| Group | Fields |
|---|---|
| Institution ID | `NAME`, `CERT`, `FIN` (FDIC fund/institution #), `BANKNO`, `ID` |
| Location | `CITY`, `PSTALP`/`STALP`, `CITYST` |
| Failure event | `FAILDATE`, `FAILYR`, `RESTYPE`/`RESTYPE1` (resolution type, e.g. FAILURE, PO=payout), `RESDATE`, `CLOSCD` |
| Charter/class | `CHCLASS`/`CHCLASS1` (e.g. NM = state nonmember), `SAVR` (insurance fund/regulator) |
| Financials at failure | `QBFASSET` (total assets), `QBFDEP` (total deposits), `UNINSDEP` (uninsured deposits), `COST` (estimated resolution cost), `COSTMOSTRECENTASOF` |
| Acquirer / transaction | `BIDNAME`, `BIDCITY`, `BIDSTATE`, `FUND`, `TERMI` |
| Savings/thrift program | `FSL_PROG`, `BSTATUS`, `COMMENTS`, `URL` |

---

## 4. NCUA 5300 Call Report (Credit Unions) + Profile (FS220A)

| Attribute | Detail |
|---|---|
| **Purpose** | The credit-union analog of the bank Call Report — financial condition, income, and operational data for federally insured credit unions. |
| **Who collects** | National Credit Union Administration (NCUA). |
| **Who files** | All federally insured credit unions (FICUs). |
| **Frequency** | Quarterly; due by 11:59:59 p.m. ET on the 30th of January, April, July, October (~30 days after quarter-end). |
| **Account-code system** | Every data point has an **account code** (the "Acct" / **FS220**-series code). The form is delivered as the **FS220** file family; account codes are documented in the "5300 Account Codes" booklet (one of four: Form, Instructions, Account Codes, Changes). |
| **Profile (FS220A)** | The **Credit Union Profile** — non-financial structural/contact/operational data (officials, branches, services, charter info). The Profile must be certified before 5300 corrections can be submitted. |
| **Official URL** | https://ncua.gov/regulation-supervision/regulatory-reporting/cuonline/5300-call-report-faqs ; forms/instructions archive https://ncua.gov/analysis/credit-union-corporate-call-report-data/call-report-forms-instructions-archive |
| **Form (current)** | https://ncua.gov/files/publications/regulations/call-report-form-march-2025.pdf |
| **Instructions** | https://ncua.gov/files/publications/regulations/call-report-instructions-september-2025.pdf |
| **Bulk data** | Quarterly Call Report datasets (downloadable account-code tables) via the Credit Union & Corporate Call Report Data page on ncua.gov; account-code labels in `AcctDesc.txt` inside each quarterly zip. |

### 5300 schedules / sections

| Schedule / Statement | Content |
|---|---|
| Statement of Financial Condition | Balance sheet (assets, liabilities, equity). |
| Statement of Income and Expense | Income statement. |
| Schedule A — Loans | §1 Outstanding loans & YTD grants; §2 Delinquent loans & leases; §3 Charge-offs & recoveries; §4 Other loan info; §5 Indirect loans; §6 Loans purchased/sold (701.22, 701.23); §7 1–4 family residential RE; §8 Commercial loans. |
| Schedule B | Investments and securities (§1–4). |
| Schedule C | Liquidity (§1–5). |
| Schedule D | Member / deposit (shares) data (§1–3). |
| Schedule G | PCA net-worth calculation. |
| Schedule H | Complex credit-union leverage ratio. |
| Schedule I | Risk-based capital ratio calculation. |

> Schedule lettering reflects the September 2025 form; older vintages differ. Schedules E/F are
> not enumerated in the FAQ source — **UNVERIFIED** whether present in the current form.

See **[`csv/MDRM_NAMESPACES.csv`](../csv/MDRM_NAMESPACES.csv)** for the `FS220` namespace.

---

## 5. OCC — Historical National-Bank Reports

| Attribute | Detail |
|---|---|
| **Purpose** | Statutory annual report to Congress; included individual statements of condition (balance sheets) for every national bank — the primary historical bank-level data source for 1863–1941. |
| **Who collects** | Office of the Comptroller of the Currency (OCC), U.S. Treasury (created 1863). |
| **Who files** | National banks (federally chartered commercial banks), via periodic "Reports of Condition" responding to the Comptroller's calls. |
| **Identifiers** | **OCC charter number** — a unique, persistent ID assigned to each national bank; supports panel construction. Reports also record location, president, and cashier. |
| **Coverage** | National Banking Era (1863–1913), Early Fed (1914–1928), Great Depression (1929–1939+). Individual Statements of Condition issued as a separate supplement for 1923–1941 (and 1949). |
| **Publicly available** | **Annual Report of the Comptroller of the Currency** (1863–1980) on **FRASER** (St. Louis Fed): https://fraser.stlouisfed.org/title/annual-report-comptroller-currency-56 . OCC history: https://www.occ.treas.gov/about/who-we-are/history/index-history.html . Records guide: https://www.archives.gov/research/guide-fed-records/groups/101.html (NARA RG 101). |
| **Researcher-digitized datasets** | Bank-level balance sheets 1863–1941 digitized at https://finhist.com/historical-call/index.html ; 1867–1904 set by Sergio Correia https://scorreia.com/data/call-reports.html . Harvard Dataverse (OCC-CLV) DOI 10.7910/DVN/Q22XR1. These are derived (built from the OCC annual reports), not OCC-published. |

### Historical condition-report field groups (as digitized)

| Group | Typical line items |
|---|---|
| Identity | Charter number, bank name, city/state, president, cashier, report (call) date |
| Assets | Loans & discounts, U.S. bonds (to secure circulation / on hand), specie, legal-tender notes, due from banks, real estate, cash items |
| Liabilities | Capital stock paid in, surplus fund, undivided profits, national bank notes outstanding (circulation), individual deposits, due to banks |

> Exact column set varies by report year/era — historical schedules evolved; **UNVERIFIED** as
> a single fixed schema.

---

## 6. UBPR — Uniform Bank Performance Report (FFIEC)

> **Deep dive:** for the parsed official derivation formulas, the full concept
> catalog (`csv/UBPR_CONCEPTS.csv`), and the empirical validation of headline
> ratios against real published UBPR values, see **[`UBPR_GUIDE.md`](./UBPR_GUIDE.md)**.

| Attribute | Detail |
|---|---|
| **Purpose** | Analytical report converting Call Report raw data into standardized **derived ratios, percentages, and dollar figures**, each compared against a **peer-group average** and a **percentile rank**, for examiner/analyst use. |
| **Who produces** | FFIEC (Federal Financial Institutions Examination Council). |
| **Source data** | Each bank's Call Report (FFIEC 031/041/051). UBPR items are computed/derived, not directly filed. |
| **Frequency** | Quarterly (tracks Call Report cadence). |
| **Key concept** | UBPR items carry their own **`UBPR####` codes** (e.g. `UBPRE001` = Interest Income (TE), Summary Ratios page 1). The MDRM mnemonic is `UBPR`; the leading item-code letter denotes the topic group (`E…` earnings, `M…` memoranda). They are formula-defined ratios built from MDRM-coded Call Report items. |
| **Official URL** | https://www.ffiec.gov/data/ubpr/uniform-bank-performance-report |
| **User's Guide** | https://www.ffiec.gov/data/ubpr/report-user-guide ; PDD download https://cdr.ffiec.gov/public/DownloadUBPRUserGuide.aspx |
| **Peer Group Average Report** | https://www.ffiec.gov/data/ubpr/peer-group-average-report |
| **Output columns** | Per report date: `Bank` value, `PG#` (peer-group average), `PCT` (percentile rank). |

### UBPR page/section structure (User's Guide for Individual Pages)

| Page/section | Content |
|---|---|
| Summary Ratios (Page 1) | Headline earnings, capital, asset-quality, growth ratios. |
| Income Statement / Revenues & Expenses | Interest income/expense, noninterest, provisions, net income (as % of avg assets). |
| Balance Sheet % composition | Assets/liabilities as % of total; balance-sheet structure. |
| Asset-quality / Allowance | Past-due, nonaccrual, charge-offs, ALLL adequacy. |
| Liquidity & Funding | Net loans/deposits, wholesale funding, liquid assets. |
| Capital | Capital ratios, growth, dividends. |
| Interest-rate risk / repricing | Repricing/maturity buckets, rate sensitivity. |
| Derivatives / off-balance-sheet | Notional and risk measures (where applicable). |

> Exact page numbering/titles evolve by reporting period; consult the dated User's Guide for
> the canonical page list.

UBPR namespaces — `UBPR` (ratios), `UBPS` (peer stats), `UBPK` (peer rank) — are catalogued in
**[`csv/MDRM_NAMESPACES.csv`](../csv/MDRM_NAMESPACES.csv)**.

---

## Sources (official)

- FDIC API docs — https://api.fdic.gov/banks/docs (redirect from https://banks.data.fdic.gov/docs/)
- FDIC SDI — https://www.fdic.gov/node/118336 ; https://www.fdic.gov/foia/quarterly-financial-reports-statistics-depository-institutions-sdi
- FDIC data downloads — https://www.fdic.gov/resources/tools/bank-data-guide/data-download.html
- FDIC SOD — https://www.fdic.gov/bank-financial-reports/summary-deposits ; instructions https://www.fdic.gov/bank-financial-reports/2025-sod-instructions.pdf ; live schema https://api.fdic.gov/banks/sod
- FDIC failures — https://www.fdic.gov/bank-failures/failed-bank-list ; https://banks.data.fdic.gov/bankfind-suite/failures ; live schema https://api.fdic.gov/banks/failures
- NCUA 5300 — https://ncua.gov/regulation-supervision/regulatory-reporting/cuonline/5300-call-report-faqs ; form https://ncua.gov/files/publications/regulations/call-report-form-march-2025.pdf ; instructions https://ncua.gov/files/publications/regulations/call-report-instructions-september-2025.pdf
- OCC history — https://www.occ.treas.gov/about/who-we-are/history/index-history.html ; FRASER Annual Report https://fraser.stlouisfed.org/title/annual-report-comptroller-currency-56 ; NARA RG 101 https://www.archives.gov/research/guide-fed-records/groups/101.html
- UBPR — https://www.ffiec.gov/data/ubpr/uniform-bank-performance-report ; User's Guide https://www.ffiec.gov/data/ubpr/report-user-guide
