# Bank-Entity Identifier Systems Guide

The definitive guide to the identifier systems that link US bank datasets together —
RSSD ID, FDIC Certificate, OCC Charter, NCUA Charter/ID, LEI, ABA Routing Number,
OTS Docket/Thrift ID, EIN/Tax ID, CIK, and CUSIP/ticker. For each identifier this
guide gives the issuer, format, scope, persistence/reuse rule, and the datasets that
key on it; the **Crosswalk** section then explains how the identifiers map to one
another and the hazards of joining across sources.

All facts below are drawn from official sources (`.gov`, `gleif.org`, `sec.gov`) and
from the FFIEC NPW Data Dictionary (Board of Governors of the Federal Reserve System,
*Bulk Data Download — Data Dictionary and Reference Guide*, Document Version 2.0,
Rev. 4/25, prepared by the National Information Center). Items that could not be
verified against an official source are marked **UNVERIFIED**.

For the institutional-structure data (NIC/NPW Attributes / Relationships /
Transformations tables, ownership graph, merger lineage), see
[docs/NIC_STRUCTURE_GUIDE.md](NIC_STRUCTURE_GUIDE.md).

*Last compiled: 2026-06-09.*

---

## 1. Identifier Reference

### 1.1 RSSD ID

- **Also known as:** ID_RSSD, RSSD9001, the "NIC" id.
- **Issuer:** Federal Reserve Board — *Research, Statistics, Supervision & Regulation,
  and Discount & Credit* database / National Information Center (NIC).
- **Format:** Sequential integer (1, 2, 3, …) with a check digit, assigned by the RSSD
  software at first entry; no fixed length. Carries no inherent attribute information.
- **Scope:** Every entity the Fed tracks — banks, BHCs/FHCs, branches, savings
  institutions, holding-company tiers, and some foreign and non-bank entities.
- **Persistence / reuse rule:** **Stable for the life of the entity. Never changes,
  never reused.** Each entity has one and only one RSSD ID for its entire life cycle;
  it persists after liquidation or closure. The legal name can change while the RSSD
  ID stays fixed. New entities receive the next integer.
- **Datasets that key on it:** NIC/NPW (master key), FFIEC Call Reports / FFIEC
  031/041 (RSSD9001), FR Y-9C and the entire FR Y-series, FFIEC CDR, FRED bank series,
  and most academic bank panels.
- **Why it matters:** Because it never changes and never recycles, the RSSD ID is the
  most stable join key across charter changes and over time — the canonical spine for
  linking institutional structure to financial data.

### 1.2 FDIC Certificate Number

- **Also known as:** CERT, FDIC Cert ID, FED_CERT; `ID_FDIC_CERT` in NIC.
- **Issuer:** Federal Deposit Insurance Corporation.
- **Format:** Sequential integer (no check digits).
- **Scope:** Every FDIC-insured depository institution (banks and savings
  institutions). Assigned per head-office depository.
- **Persistence / reuse rule:** Unique per insured institution; assigned at insurance
  and retained through the institution's life; **not recycled in practice.** As a
  sequential-integer system it is not globally unique without an agency qualifier (see
  Crosswalk §2).
- **Datasets that key on it:** FDIC BankFind / SDI (Statistics on Depository
  Institutions) / Summary of Deposits / failures lists; pre-2018 HMDA respondent id
  (agency code 3). FDIC records also carry the RSSD as `FED_RSSD`.

### 1.3 OCC Charter Number

- **Issuer:** Office of the Comptroller of the Currency.
- **Format:** Sequential integer. (`ID_OCC` in NIC.)
- **Scope:** National banks and — since July 21, 2011 — federal savings associations /
  federal thrifts.
- **Persistence / reuse rule:** Assigned at chartering and retained through the
  institution's life. Beginning **July 21, 2011** the OCC absorbed OTS thrift
  supervision; the OCC Charter field now also stores national thrifts as **thrift
  docket + 700,000**.
- **Datasets that key on it:** OCC chartering data; pre-2018 HMDA respondent id (agency
  code 1). Carried as an attribute on the NIC RSSD record.

### 1.4 NCUA Charter / ID Number

- **Issuer:** National Credit Union Administration.
- **Format:** Sequential integer. (`ID_NCUA` in NIC.) Banded by insurance/charter
  type: **1–59,999** = Federal; **60,000–79,999** = Federally Insured, State Chartered;
  **80,000+** = Non-Federally Insured.
- **Scope:** Federally insured credit unions (and some non-federally-insured).
- **Persistence / reuse rule:** Assigned at chartering and retained through life.
  Sequential-integer system.
- **Datasets that key on it:** NCUA Call Report / Research-a-Credit-Union; pre-2018
  HMDA respondent id (agency code 5).

### 1.5 LEI (Legal Entity Identifier, ISO 17442)

- **Issuer:** GLEIF governs; codes are issued by accredited **Local Operating Units
  (LOUs)**, overseen by the LEI Regulatory Oversight Committee (ROC).
- **Format:** 20-character alphanumeric — chars 1–4 = LOU prefix, chars 5–18 =
  entity-unique string, chars 19–20 = MOD-97-10 checksum (ISO/IEC 7064). (`ID_LEI` in
  NIC.)
- **Scope:** Any legal entity participating in financial transactions, globally.
- **Persistence / reuse rule:** Permanently unique to one entity; **never reused.**
  Must be renewed annually to keep an "issued/active" registration status, but the code
  itself persists regardless.
- **Datasets that key on it:** **HMDA filer id (2018-forward)**, SEC/CFTC swap
  reporting, FR Y-series LEI fields, and the GLEIF golden-copy file.
- **Coverage caveat:** LEIs exist only from ~2012 forward and only for entities that
  obtained one; they cannot back-fill pre-2012 panels (see Crosswalk §2).

### 1.6 ABA Routing Transit Number (RTN)

- **Issuer:** American Bankers Association via its registrar (currently LexisNexis Risk
  Solutions; historically Accuity / Thomson Financial), in coordination with the FRB
  district. (`ID_ABA_PRIM` in NIC.)
- **Format:** 9 digits, `FFFF AAAA C` — Fed routing symbol (4) + ABA institution id
  (4) + MOD-10 check digit (1).
- **Scope:** Financial institutions eligible for a Federal Reserve master account;
  identifies a payment-routing **account**, not the legal entity.
- **Persistence / reuse rule:** Tied to payment routing, not entity identity.
  **Reassignable / retirable after mergers**, and **reusable across non-concurrent
  entities** (no two concurrent entities share one). One institution may hold many
  RTNs.
- **Datasets that key on it:** Fedwire/ACH routing files, FedACH, the E-Payments
  Routing Directory.
- **Why it matters:** **An RTN is not an entity key** — never use one as a persistent
  entity identifier (see Crosswalk §2).

### 1.7 OTS Docket Number / Thrift ID

- **Issuer:** (former) Office of Thrift Supervision — **defunct since July 21, 2011**.
  (`ID_THRIFT` in NIC; the related `ID_THRIFT_HC` is the OTS-assigned "H"+5-digit
  holding-company id for owners of S&Ls / federal savings banks.)
- **Format:** Numeric docket. The NIC `ID_THRIFT` field is 9 characters but only the
  right-most 5 are used; populated for charter types 300/310 that are FHLB members.
- **Scope:** Savings institutions / thrifts (legacy).
- **Persistence / reuse rule:** Legacy identifier. OTS functions transferred to
  OCC/FDIC/Fed under Dodd-Frank; new thrift supervision uses OCC Charter / RSSD.
- **Datasets that key on it:** Legacy thrift datasets; historical TFR (Thrift Financial
  Report) data; pre-2018 HMDA agency code 4 (legacy).

### 1.8 Federal Tax ID / EIN

- **Issuer:** Internal Revenue Service. (`ID_TAX` in NIC, effective 2008-12-31.)
- **Format:** 9 digits, `NN-NNNNNNN`.
- **Scope:** Any US entity with tax obligations.
- **Persistence / reuse rule:** Permanently assigned to a legal entity; **not recycled**
  to another entity. Multiple entities under one parent each have their own EIN.
- **Datasets that key on it:** Pre-2018 HMDA fallback respondent id; SEC filings. It is
  **not** a primary bank-regulatory key.

### 1.9 CIK (Central Index Key)

- **Issuer:** SEC EDGAR.
- **Format:** Integer, zero-padded to 10 digits in API paths
  (`CIK##########`).
- **Scope:** Any EDGAR filer — companies (including public bank holding companies),
  funds, and individuals.
- **Persistence / reuse rule:** Assigned at filer signup; **unique to the filer and
  not recycled.** Maps a filer to all of its filings.
- **Datasets that key on it:** SEC EDGAR submissions / XBRL APIs and all SEC filings.
- **Linking caveat:** CIK is independent of RSSD/CERT; joining public-BHC financials to
  regulatory data requires an external CIK↔RSSD crosswalk. The NIC/NPW Attributes table
  *does* carry an SEC **reporting-status** indicator (`SEC_RPTG_STATUS`, an integer code
  0–5 keyed to §13(a)/15(d) of the Securities Exchange Act of 1934 and §404 of
  Sarbanes-Oxley), but it **does not carry the CIK itself** — there is no CIK column in
  NIC/NPW. No official SEC↔Fed CIK↔RSSD mapping is published by the SEC, FFIEC, or NIC,
  so the link is commonly built **CIK → FDIC cert → RSSD**.

### 1.10 CUSIP / Ticker

- **CUSIP issuer:** CUSIP Global Services (operated for the American Bankers
  Association). (`ID_CUSIP` in NIC.)
  - **Format:** 9 characters — 6-char issuer + 2-char issue + 1 check digit.
  - **Scope:** *Securities* (equity/debt) of issuers, including public BHCs.
  - **Persistence / reuse rule:** Identifies a **security, not the legal entity**;
    reassignment is governed by CGS rules.
  - **Datasets that key on it:** SEC EDGAR full-text search (searchable field) and
    securities datasets; for public BHCs it is a join to market data.
- **Ticker symbol issuer:** Listing exchange (NYSE/Nasdaq).
  - **Format:** 1–5 alpha characters.
  - **Scope:** Exchange-listed securities.
  - **Persistence / reuse rule:** Can change or be reused over time across issuers —
    **not a stable entity key.**
  - **Datasets that key on it:** Market-data joins for public BHCs.

---

## 2. Crosswalk — How the Identifiers Map to Each Other

### 2.1 Which identifier is primary in which dataset

| Dataset / family | Primary key | Also carries |
|---|---|---|
| NIC / NPW, FFIEC Call Report, FR Y-9C / FR Y-series | **RSSD ID** | FDIC Cert, OCC Charter, NCUA id, LEI, ABA RTN, CUSIP, EIN as *attribute* columns |
| FDIC datasets (BankFind / SDI / SOD) | **FDIC CERT** | RSSD (`FED_RSSD`) |
| SEC EDGAR | **CIK** | CUSIP, ticker (searchable) |
| HMDA, 2018-forward | **LEI** | — |
| HMDA, 2017 and prior | **Agency Code + Respondent ID** | Respondent ID = OCC Charter (agency 1), FRS/RSSD (agency 2), FDIC Cert (agency 3), OTS docket (agency 4, legacy), NCUA charter (agency 5), or HUD/CFPB-assigned (non-depository) |

NIC carries the FDIC Cert, OCC Charter, NCUA id, LEI, and other identifiers as
attribute columns on the RSSD record, which makes **NIC the canonical crosswalk hub**.
The CFPB publishes the **ARID2017 → LEI Reference Table** (CSV / pipe-delimited) to
bridge the pre-2018 and post-2018 HMDA regimes
([identifiers FAQ](https://ffiec.cfpb.gov/documentation/faq/identifiers-faq)).

### 2.2 Mapping hazards

- **Sequential-integer collision.** RSSD, FDIC Cert, OCC Charter, and NCUA charter are
  *all* independent sequential integers starting near 1. The same small integer
  (e.g. "5") exists in every system as a different institution → **an id is not
  globally unique without its agency/issuer qualifier.** HMDA's pre-2018 Agency Code
  exists precisely to disambiguate. Always carry an agency qualifier when storing or
  joining these ids.
- **One BHC → many bank certs.** A single top-tier holding company (one RSSD) can own
  many insured banks, each with its own FDIC Cert and its own RSSD. RSSD↔Cert is
  therefore many-to-many at the corporate-family level; only at the *insured-institution*
  level is RSSD↔Cert roughly 1:1. (See the lead-bank rows in
  `csv/GSIB_ENTITY_IDENTIFIERS.csv` — e.g. one JPMorgan BHC RSSD vs. the JPMorgan Chase
  Bank NA cert.)
- **Charter conversions.** A bank converting between national (OCC) and
  state-member/non-member status changes the OCC Charter relevance and supervisory
  agency, but **the RSSD ID is designed to persist** — making RSSD the most stable join
  key across charter changes.
- **Merger / acquisition lineage.** When entities merge, the acquired RSSD is closed
  (moves to NPW "Attributes — Closed") and linked to the survivor via the NIC
  **Transformations** table; Certs are retired. A naive id join across vintages that
  ignores the transformation history will *lose* merged entities. See
  [docs/NIC_STRUCTURE_GUIDE.md](NIC_STRUCTURE_GUIDE.md) for the Transformations event
  model (predecessor → successor RSSD, with a transformation type code and date).
- **LEI coverage gap.** LEIs exist only from ~2012 forward and only for entities that
  obtained one; historical and small entities may lack an LEI, so **LEI cannot
  back-fill pre-2012 panels.**
- **RTN is not an entity key.** Routing numbers map many-to-one to institutions, are
  reassigned on merger, and are reusable across non-concurrent entities; never use an
  RTN as a persistent entity identifier.
- **CIK is independent.** NIC/NPW carries only an SEC *reporting-status* flag
  (`SEC_RPTG_STATUS`, per the NPW Data Dictionary) — **not** the CIK; no official
  CIK↔RSSD crosswalk is published by the SEC, FFIEC, or NIC. Linking SEC public-company
  data to Fed/FDIC regulatory data therefore requires an external crosswalk, commonly
  built **CIK → FDIC cert → RSSD**.

### 2.3 Real-world example — the difficulty of cross-source linking

A concrete illustration of how hard it is to link historical bank panels to the modern
RSSD universe: consider a research crosswalk that maps a long-run historical
bank-failure panel (covering 1863–1989+) to FFIEC RSSD identifiers via name + state
fuzzy matching.

- **Universe:** **14,286 historical banks** (panel coverage 1863–1989+).
- **Matched to RSSD: 943 (6.6%)**; unmatched (historical): **13,343 (93.4%)**.
- The low overall match rate is **by design**, not failure: the modern-era (1990+)
  match rate is **100%**, while the pre-FFIEC eras match at 0% — 1934–1959 (5,004
  banks), 1914–1933 (5,470), pre-1914 (2,869) are all unmatched because the Fed's RSSD
  system does not cover banks closed before ~1960. The historical panel's distinctive
  value *is* this pre-FFIEC coverage.
- Of the matched banks: FDIC cert linked on **495 (52%)**; BHC linked on **199 (21%)**.
- **Match quality:** built with a fuzzy-matching threshold of **≥85% similarity**
  (rapidfuzz, grouped by state, +10% city-match bonus); achieved **avg confidence
  95.4%** (min 85.0%, max 100.0%, median 96.7%).

The lesson: even with a robust fuzzy-matching pipeline and a 95%+ average confidence on
the matches it *does* make, an entire era of bank history simply has no RSSD to map to —
because the identifier system did not exist yet. Cross-source entity linking is bounded
not just by match quality but by the temporal coverage of each identifier system.

---

## 3. Sources (official)

- FFIEC National Information Center (NIC/NPW): https://www.ffiec.gov/NPW
- **NPW Data Dictionary** (authoritative field reference; Doc. Ver. 2.0, Rev. 4/25):
  https://www.ffiec.gov/npw/StaticData/DataDownload/NPW%20Data%20Dictionary.pdf
- NPW Bulk Data download: https://www.ffiec.gov/npw/FinancialReport/DataDownload
- CFPB/FFIEC HMDA — Institution Identifiers FAQ (RSSD/Cert/OCC/NCUA/Tax ID/LEI +
  ARID2017→LEI table): https://ffiec.cfpb.gov/documentation/faq/identifiers-faq
- GLEIF — ISO 17442 LEI code structure:
  https://www.gleif.org/en/about-lei/iso-17442-the-lei-code-structure
- GLEIF — LEI data access & use: https://www.gleif.org/en/lei-data/access-and-use-lei-data
- FDIC BankFind Suite — API docs: https://api.fdic.gov/banks/docs ; portal:
  https://banks.data.fdic.gov/bankfind-suite
- ABA — Routing Number / registrar: https://www.aba.com/about-us/routing-number
- NCUA — Research a Credit Union: https://mapping.ncua.gov/ResearchCreditUnion
- SEC EDGAR — Accessing EDGAR Data (REST APIs):
  https://www.sec.gov/search-filings/edgar-search-assistance/accessing-edgar-data ;
  Full-text search: https://www.sec.gov/edgar/search/

## See also

- [docs/NIC_STRUCTURE_GUIDE.md](NIC_STRUCTURE_GUIDE.md) — NIC/NPW institutional-structure
  data: Attributes / Relationships / Transformations tables, the ownership graph, and
  merger lineage.
- `csv/IDENTIFIERS.csv`, `json/identifiers.json` — machine-readable versions of the
  identifier reference in this guide.
- `csv/GSIB_ENTITY_IDENTIFIERS.csv` — worked example of RSSD / Cert / LEI / OCC across
  G-SIB holding companies and their lead banks.
