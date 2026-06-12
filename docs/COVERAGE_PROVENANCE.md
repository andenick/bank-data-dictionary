# Coverage & Provenance

How far back each public US bank-data collection reaches, where the data physically comes
from, when major schedules were introduced, and where the known gaps are. This is a guide
to the **data's temporal coverage and vintage**, written for an outside researcher
assembling a long-run panel from public sources. It does not describe any particular
database build — only the public collections themselves and the eras they cover.

All collections referenced here are published by US regulators (Federal Reserve, FFIEC,
FDIC, OCC, NCUA, CFPB, SEC) or by the academic digitizations of regulator records cited at
the end.

---

## 1. The collection universe at a glance

| Collection | Provider | Native temporal coverage | Granularity |
|------------|----------|--------------------------|-------------|
| OCC historical national-bank balance sheets | OCC Annual Reports (+ academic digitization) | 1863–1941 | Bank-level, periodic call dates |
| Pre-1976 Call Reports ("Luck"/NY Fed dataset) | Federal Reserve Bank of New York (public) | 1959Q4–1975Q4 (dataset spans 1959–2025) | Bank-quarter |
| Call Reports — Fed-direct, pre-2012 | Federal Reserve Bank of Chicago archive | 1976Q1–2011Q4 | Bank-quarter |
| Call Reports — Fed-direct, 2012+ | FFIEC Central Data Repository (CDR) | 2012Q1–present | Bank-quarter |
| FR Y-9C (consolidated BHC financials) | FFIEC / Federal Reserve | 1986Q3–present | BHC-quarter |
| UBPR analytical ratios | FFIEC CDR (UBPR) | 2002Q4–present | Bank-quarter |
| FR Y-15 systemic indicators | FFIEC NIC | 2020–present (annual) | G-SIB-year |
| FDIC SDI financials | FDIC API | 1984Q1–present | Bank-quarter |
| FDIC Summary of Deposits | FDIC API | 1994–present (annual) | Branch-year |
| FDIC failures (BankFind) | FDIC API | 1934–present | Event |
| FDIC institution history | FDIC API | All dates | Event |
| NIC entity attributes / identifiers | FFIEC NIC | Current snapshot | Entity |
| DFAST stress-test results | Federal Reserve | 2013–present (annual) | Bank-year |
| Basel III Pillar 3 disclosures | Bank disclosures (PDF) | ~2024–present | G-SIB-quarter |
| NCUA 5300 credit-union call reports | NCUA | 2022Q1–present (bulk era used here) | Credit-union-quarter |
| HMDA mortgage summary | CFPB HMDA Data Browser | 2018–present | Institution-year |
| FRED banking/macro series | FRED (St. Louis Fed) | 1919–present | Series-observation |
| SEC EDGAR identifiers | data.sec.gov | Current frame | Entity |

---

## 2. Coverage by era

**1863–1941 — National-bank era (OCC).** The earliest machine-usable bank-level balance
sheets come from the Comptroller of the Currency's Annual Reports, which published the
condition of every national bank at periodic call dates from the founding of the national
banking system in 1863 through 1941. These exist publicly today as OCC's own digitized
Annual Reports and as academic digitizations of them (see §5). Coverage is national banks
only; state banks of this era are not in this corpus.

**1942–1958 — Quarterly gap.** There is no public, machine-readable, bank-level *quarterly*
balance-sheet series spanning the years between the OCC historical series and the start of
the modern Call Report digital record. For these years, regulator holdings exist largely as
physical archives. Annual-granularity coverage of this window can be obtained from academic
historical bank panels (see §5), but quarterly coverage remains archive-only.

**1959Q4–1975Q4 — Pre-digital Call Reports (NY Fed / "Luck").** The Federal Reserve Bank of
New York publishes a free dataset of bank balance sheets and income statements
("Balance Sheets and Income Statements", associated with Correia–Luck–Verner) that provides
bank-quarter coverage beginning 1959Q4. For the years before the Fed-direct digital record
begins (1976), this is the authoritative public source of quarterly bank financials. The NY
Fed dataset itself extends forward to the present, but for 1976+ it is redundant with the
Fed-direct record (see §3).

**1976Q1–2011Q4 — Fed-direct Call Reports (Chicago Fed archive).** The Federal Reserve Bank
of Chicago hosts the public archive of Commercial Bank Call Report data beginning 1976Q1.
This is the start of the continuous modern digital Call Report record (FFIEC 031/041, later
also 051).

**2012Q1–present — Fed-direct Call Reports (FFIEC CDR).** From 2012 onward, the public Call
Report bulk data is served from the FFIEC Central Data Repository. The Chicago Fed
(pre-2012) and CDR (2012+) records join into one continuous bank-quarter Call Report series
from 1976 to the present.

**1984+ / 1986+ — Modern supervisory layers.** FDIC SDI financials begin 1984Q1; the FR
Y-9C consolidated BHC report begins 1986Q3; UBPR analytical ratios are offered from 2002Q4
(the FFIEC CDR does not offer the first three quarters of 2002). FDIC Summary of Deposits
(branch-level) begins 1994; FDIC bank-failure records reach back to 1934.

**2013+ — Stress-testing and disclosure era.** DFAST supervisory stress-test results are
published annually from 2013. FR Y-15 G-SIB systemic indicators are available in bulk only
from 2020 onward. Basel III Pillar 3 disclosures are bank-published PDFs concentrated in the
most recent years (~2024+). NCUA 5300 credit-union call reports are used here from 2022Q1;
HMDA institution-year summaries from the CFPB Data Browser begin 2018.

---

## 3. The three-corpus architecture (concept)

A continuous bank-level balance-sheet spine from the 1860s to the present cannot be built
from any single public source. It is assembled by stitching three non-overlapping corpora,
each kept only for the era where it is unique:

- **Corpus A — historical OCC.** OCC Annual Report national-bank balance sheets, native
  1863–1941. Kept for its unique pre-1942 national-bank coverage; nothing else reaches this
  era at bank level.
- **Corpus B — pre-digital Fed (NY Fed / Luck).** The NY Fed public bank balance-sheet
  dataset, native 1959–present. Kept only for its unique **1959Q4–1975Q4** quarters (plus a
  handful of later gap-fill cells); for 1976+ it duplicates Corpus C.
- **Corpus C — Fed-direct.** Chicago Fed (1976–2011) plus FFIEC CDR (2012+). Native
  1976Q1–present, and the **spine** for everything from 1976 onward.

**Why the split is necessary, empirically.** The Fed-direct corpus contains zero rows before
1976, so the NY Fed pre-1976 core is irreplaceable. Conversely, for the post-1976 overlap
the NY Fed dataset is almost entirely redundant: the overwhelming majority of its
1976+ entity-quarter cells are already present in the Fed-direct record, and the few that
are not cluster in the early 2000s and are predominantly non-deposit trust companies — most
of which can be recovered directly from FFIEC CDR. On the variables that can be mapped
across corpora for 1976+, core aggregates (assets, deposits, equity, liabilities, loans)
reconcile to roughly 99.9% between the NY Fed dataset and the Fed-direct record; the handful
of variables that reconcile less well (e.g. securities, fed funds purchased, time deposits)
differ for **definitional/recipe** reasons rather than data loss — the underlying line items
remain present in the Call Report record. The practical implication for a researcher: take
1976+ from the Fed-direct corpus, take 1959–1975 from the NY Fed dataset, take pre-1942 from
the OCC corpus, and treat the small residual NY Fed-only post-1976 cells as targeted
gap-fill rather than a parallel source.

---

## 4. When major schedules / reports were introduced

Even within a continuously-covered collection, individual schedules and line items appear at
different dates. Some milestones a long-run researcher should expect:

- **FR Y-9C** consolidated BHC reporting begins **1986Q3**.
- **Call Report form FFIEC 051** (the streamlined report for smaller, non-complex banks) was
  introduced in **2017**; before that, banks filed FFIEC 031 (with foreign offices) or
  FFIEC 041 (domestic only).
- **Basel III regulatory-capital schedule (Call Report Schedule RC-R)** was substantially
  rebuilt for the Basel III capital framework phased in from **2014**, changing the
  capital-ratio line items and adding common-equity-tier-1 detail.
- **Expanded trading / market-risk and related detail** in the supervisory reports continued
  to be added through the mid-2010s; researchers should expect broader trading-book and
  derivatives detail from roughly **2018** onward relative to earlier filings.
- **UBPR ratios** are offered from **2002Q4**; **FR Y-15** systemic-indicator bulk data only
  from **2020**.
- **CECL retitling.** Under the current-expected-credit-loss (CECL) accounting standard, the
  former "Allowance for Loan and Lease Losses" line items were retitled to "Allowance for
  Credit Losses" across the FR Y-11 / Y-7N and Call Report families.

Because line items are added, retired, and renumbered over time, any item-level series
should be checked against the variable dictionary's first-observed / last-observed dates
before being treated as continuous.

---

## 5. Known public-data gaps and limits

- **1942–1958 quarterly bank financials** are not available publicly at bank-quarter
  granularity; only annual-granularity academic panels and physical archives cover the
  window.
- **FR Y-9LP / Y-9SP parent-only BHC reports** have no public bulk product; they are
  available only as per-institution filings, and the FFIEC NPW interface that serves them
  has at times blocked automated access.
- **Pre-2018 HMDA** is not available through the modern CFPB Data Browser (2018+ only);
  legacy HMDA is keyed by respondent ID rather than LEI, complicating linkage to other
  bank identifiers.
- **FR Y-15 before 2020** has no bulk product (only individual NIC snapshots from 2020 on).
- **Basel III Pillar 3** coverage is thin and bank-published: only the largest institutions
  (G-SIBs) disclose, and only for recent periods.
- **Identifier coverage floor.** Linking historical and modern records depends on the
  Federal Reserve's RSSD identifier system and the FFIEC NIC entity directory, which do not
  reach institutions that ceased to exist before the NIC era; a structural residual of
  historical entities cannot be matched to a modern RSSD.
- **Confidential reports out of public scope.** Several supervisory collections (e.g. FR
  Y-14, FR 2052a) are confidential and are not part of any public data product.

---

## 6. Provenance tiers

A simple way to weight sources by directness:

- **T1 — primary regulator self-serve bulk:** the regulator publishes the data directly for
  download (e.g. Federal Reserve MDRM, FFIEC CDR bulk, FRED, SEC EDGAR data API).
- **T2 — regulator API / portal:** programmatic access to a regulator's own records
  (e.g. FDIC BankFind/SDI, FDIC Summary of Deposits, NCUA 5300, CFPB HMDA).
- **T3 — Fed archive:** a Federal Reserve archive hosting older records (e.g. Chicago Fed
  Call Report archive).
- **T3.5 — public academic-Fed dataset:** a Federal Reserve Bank's public research dataset
  (e.g. the NY Fed balance-sheet / income-statement dataset).
- **T4 — academic digitization:** scholarly digitizations of regulator records (e.g. the
  OCC Annual Report digitizations and historical failing-bank panels).
- **derived:** values computed from one or more of the above rather than reported directly.

---

## 7. Sources

- Federal Reserve MDRM (variable dictionary): https://www.federalreserve.gov/apps/mdrm/
- FFIEC Central Data Repository (Call Report / UBPR bulk): https://cdr.ffiec.gov/public/pws/downloadbulkdata.aspx
- FFIEC NIC / NPW (entity attributes, FR Y-15): https://www.ffiec.gov/NPW/
- Federal Reserve Bank of Chicago Call Report archive: https://www.chicagofed.org/banking/financial-institution-reports/commercial-bank-data
- Federal Reserve Bank of New York — Balance Sheets & Income Statements dataset: https://www.newyorkfed.org/research/banking_research/balance-sheets-income-statements
- OCC Annual Reports: https://www.occ.treas.gov/publications-and-resources/publications/annual-report/index-annual-report.html
- FDIC BankFind / SDI: https://banks.data.fdic.gov/ · https://banks.data.fdic.gov/api/
- FDIC Summary of Deposits: https://www.fdic.gov/bank-financial-reports/summary-deposits
- Federal Reserve DFAST / stress tests: https://www.federalreserve.gov/supervisionreg/dfa-stress-tests.htm
- FRED (St. Louis Fed): https://fred.stlouisfed.org/
- SEC EDGAR: https://data.sec.gov/
- CFPB HMDA: https://ffiec.cfpb.gov/
- NCUA 5300 call-report data: https://ncua.gov/analysis/credit-union-corporate-call-report-data

**Academic digitizations of regulator records.** The OCC historical national-bank series and
the pre-digital Call Report dataset are associated with Correia, Luck & Verner, "Failing
Banks" (QJE, DOI 10.1093/qje/qjaf044), and the OCC digitization is archived at Harvard
Dataverse (DOI 10.7910/DVN/Q22XR1).
