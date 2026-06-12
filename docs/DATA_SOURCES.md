# Data Sources

Where the underlying data comes from. This is an annotated directory of the public
suppliers behind the U.S. bank regulatory data universe that this dictionary catalogues —
the regulators who collect and publish the filings, the historical and research
distributions that reach back before the modern digital record, and the related sites that
query and download the harmonized result. Each entry says what the source provides, what it
covers, and what it is best used for; citation requirements are reproduced verbatim where a
source asks for them.

This dictionary itself is a **catalogue / mapping reference** — it documents what these
datasets are, how their fields are structured, and how their schedules and forms reconcile
to one another. The sources below are where you go to read the authoritative definitions and
acquire the actual filings.

---

## Official regulatory sources

The primary points where U.S. regulators define and distribute their data collections.

### [FFIEC Central Data Repository (CDR)](https://cdr.ffiec.gov/public/)

- **Provides:** The official public distribution point for U.S. bank Call Report and FR Y-9C
  filings. Its Bulk Data section offers per-period downloads of the full reporting universe,
  and its Taxonomies section publishes the XBRL taxonomy that defines every reported field,
  its schedule, and the validation edits that govern it. The CDR is also the source for UBPR
  bulk extracts and the FFIEC 101/102/002/009 reports.
- **Coverage:** Call Report and FR Y-9C current cycles plus archived historical periods; the
  underlying bulk filings used here run 2012Q1–2026Q1 for Call Reports and the FR Y-9C from
  1986Q3 onward.
- **Use for:** Acquiring authoritative, machine-readable regulatory filings at scale, and
  reading the official field definitions and edit checks behind them.

### [Federal Reserve Micro Data Reference Manual (MDRM)](https://www.federalreserve.gov/apps/mdrm/)

- **Provides:** The master data dictionary for the Federal Reserve and FFIEC reporting
  system. Every variable code (e.g. BHCK2170, RCFD2170) maps to a human-readable name, full
  description, item type, the reporting forms that carry it, and the date range over which it
  was collected. The manual is downloadable as a zipped CSV dictionary.
- **Coverage:** The full active and historical code universe (tens of thousands of variable
  codes across all Fed/FFIEC forms), with per-code start and end reporting dates.
- **Use for:** Decoding any regulatory variable, resolving code prefixes and scopes, and
  tracing when a series was active.

### [Federal Reserve Reporting Forms](https://www.federalreserve.gov/apps/reportingforms/)

- **Provides:** A searchable catalogue of the forms the Federal Reserve uses to collect data
  from bank holding companies, depository institutions, and other entities. Each entry links
  to the blank form, the line-by-line reporting instructions, and the OMB documentation. The
  FR Y-9C (consolidated holding-company financial statements) and the rest of the FR Y-series
  are filed here.
- **Coverage:** All current FR-numbered and FFIEC reporting forms, with instructions;
  superseded form vintages are retained.
- **Use for:** Reading the authoritative form layout and instructions that define what each
  schedule and line item means.

### [FFIEC National Information Center (NIC)](https://www.ffiec.gov/NPW/)

- **Provides:** The authoritative registry of financial-institution identity and structure.
  NIC publishes the entity master (legal names, RSSD identifiers, charter and regulator
  codes, geography), parent-child ownership relationships, and predecessor/successor
  transformation events for mergers and charter changes. It is the source of record for
  resolving who owns whom and how institutions map across the regulatory ID systems (RSSD,
  LEI, FDIC cert, OCC, NCUA).
- **Coverage:** Current institution, branch, relationship, and transformation snapshots
  covering active and closed/merged entities (the structure record stretches back across the
  full NIC history).
- **Use for:** Tracing corporate hierarchies, linking identifiers across regulators, and
  attaching entity context to filing data.

### [FFIEC Uniform Bank Performance Report (UBPR)](https://www.ffiec.gov/ubpr.htm)

- **Provides:** The FFIEC's standardized analytical report that turns raw Call Report
  filings into comparable performance ratios (profitability, capital, asset quality,
  liquidity, and efficiency) and benchmarks each bank against its peer group. The User's
  Guide documents how every ratio is derived, annualized, and averaged. UBPR bulk data and
  the peer-group statistics are distributed through the FFIEC CDR.
- **Coverage:** UBPR ratios and peer-group benchmarks from 2002Q4 to the current quarter (the
  floor offered in bulk by the CDR).
- **Use for:** Reading standardized, peer-relative bank performance ratios without
  recomputing them from raw line items.

### [FDIC BankFind Suite / Financial Data API](https://banks.data.fdic.gov/)

- **Provides:** The FDIC's open data platform for insured depository institutions. It serves
  the Statistics on Depository Institutions (SDI) quarterly financials, the Summary of
  Deposits branch survey, the failed-bank list, and institution structure-change history, all
  through a documented REST API returning JSON or CSV. The web BankFind tool offers the same
  data interactively.
- **Coverage:** SDI quarterly financials 1984Q1–2026Q1; Summary of Deposits 1994–2025;
  failure records from 1934 to present; institution history across all dates.
- **Use for:** Pulling an independent, FDIC-collected view of bank financials, deposits,
  branches, and failures to cross-check or extend the Fed/FFIEC filings.

### [Federal Reserve Stress Tests (DFAST)](https://www.federalreserve.gov/supervisionreg/dfa-stress-tests.htm)

- **Provides:** The Federal Reserve's hub for the Dodd-Frank Act Stress Test program. It
  publishes the annual supervisory stress-test results by bank, the macroeconomic scenario
  definitions (baseline, adverse, and severely adverse paths for GDP, unemployment, rates,
  and asset prices), and the historical archive of prior exercises and CCAR results.
- **Coverage:** DFAST results from 2013 to the current annual exercise; supervisory scenario
  paths published each cycle, plus historical CCAR exercises (2011–2021).
- **Use for:** Capital-adequacy and tail-risk analysis: comparing projected losses and
  post-stress capital ratios against the published supervisory scenarios.

### [Chicago Fed Commercial Bank Data](https://www.chicagofed.org/banking/financial-institution-reports/commercial-bank-data)

- **Provides:** The Federal Reserve Bank of Chicago's archive of machine-readable
  commercial-bank Call Report data, the standard source for pre-CDR historical micro filings.
  It distributes the bulk Call Report files (SAS transport format) that predate the FFIEC
  CDR's bulk coverage, alongside related bank structure and BHC reference files.
- **Coverage:** Historical Call Report bulk files from 1976Q1 through 2011Q4 (the digital
  micro-filing record before the CDR bulk era).
- **Use for:** Building long historical Call Report panels that reach back before the FFIEC
  CDR's modern bulk downloads begin.

---

## Historical & research distributions

Digitizations of the regulator record that extend bank-level panels back before the modern
Fed/FFIEC digital era. These sources ask to be cited; the required citation language is
reproduced verbatim.

### [NY Fed Historical Bank Balance Sheets / finhist.com](https://www.newyorkfed.org/research/banking_research/balance-sheets-income-statements)

- **Provides:** The Correia-Luck-Verner distribution of digitized historical commercial-bank
  balance sheets and income statements, released through the Federal Reserve Bank of New
  York's banking-research page (also mirrored at finhist.com). It reconstructs the pre-1976
  micro record from the underlying FFIEC Reports of Condition and Income, for which no Fed
  bulk microdata otherwise exists.
- **Coverage:** Commercial-bank balance sheets and income statements from 1959 onward (the
  1959Q4–1975Q4 window is the only machine-readable source for that period); the companion
  finhist.com site also hosts digitized OCC national-bank balance sheets 1863–1941.
- **Use for:** Extending bank-level financial panels back before the modern Fed/FFIEC digital
  record begins.
- **Citation:** Citation required. Cite: Correia, Sergio, Stephan Luck, and Emil Verner,
  "Failing Banks," *Quarterly Journal of Economics* (DOI: 10.1093/qje/qjaf044).

### [Harvard Dataverse — CLV / OCC Historical Layer](https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/Q22XR1)

- **Provides:** The archived, DOI-citable deposit of the Correia-Luck historical
  national-bank dataset on Harvard Dataverse. It supplies digitized OCC national-bank
  balance-sheet data and the extended historical layer that fills the early span and
  additional banks not available elsewhere as machine-readable data.
- **Coverage:** Digitized OCC national-bank balance sheets spanning 1863–1941.
- **Use for:** Obtaining a permanently archived, citable copy of the historical OCC/CLV layer
  for reproducible historical banking research.
- **Citation:** Citation required. Cite the Correia-Luck dataset (DOI: 10.7910/DVN/Q22XR1)
  and the associated "Failing Banks" research (DOI: 10.1093/qje/qjaf044).

---

## Related sites

The query and download surfaces for the harmonized warehouse that brings these sources
together.

### [FreeNIC](https://freenic.org/)

- **Provides:** The query and explorer surface for the unified U.S. banking regulatory data
  set. FreeNIC brings the Fed, FFIEC, FDIC, NCUA, OCC, and historical sources into one
  harmonized warehouse with a shared identifier spine, so you can look up institutions,
  browse schedules, and run cross-source queries against the actual filings rather than just
  their definitions.
- **Coverage:** A unified warehouse spanning 1863–2026 across Call Reports, FR Y-9C, FDIC
  SDI, NCUA 5300, UBPR, NIC structure, and historical layers.
- **Use for:** Exploring and querying the real filing data, and linking entities across
  regulators via the identifier crosswalk.

### [FreeNIC Bulk Data (data.freenic.org)](https://data.freenic.org/)

- **Provides:** The bulk download surface for the FreeNIC warehouse. Every table is published
  as a columnar Parquet file (institutions, branches, relationships, Call Report and FR Y-9C
  filings, FDIC financials, UBPR ratios, the dictionary taxonomy tables, and more), ready to
  load directly into DuckDB, pandas, or Spark.
- **Coverage:** The full set of FreeNIC tables as individual Parquet files, mirroring the
  warehouse's 1863–2026 span.
- **Use for:** Downloading the entire data set for offline, programmatic analysis without an
  API.
