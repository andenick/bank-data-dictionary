# FFIEC NIC / NPW Institutional-Structure Data Guide

## Overview

The **National Information Center (NIC)** is the Federal Reserve's central repository of
structure and identifier data for every banking organization the Federal Reserve and the
other federal banking agencies supervise. Where the FFIEC *financial* collections (Call
Reports, FR Y-9C, FR Y-14, etc. — see [COLLECTIONS_CATALOG.md](COLLECTIONS_CATALOG.md))
tell you *what a bank reported*, the NIC data tells you *what the entity is, where it sits
in a holding-company structure, and how it was born, merged, or failed*.

The Board of Governors publishes a non-confidential extract of the NIC database as the
**NPW (National Information Center — "NPW" / institution-search) Bulk Data Download** at:

- **Source URL:** <https://www.ffiec.gov/NPW>

The data is officially **non-confidential public data**. The first public iteration covers
the Attributes, Relationships, and Transformations tables documented here; further detail
is available via FOIA.

**Authoritative field source:** Board of Governors of the Federal Reserve System,
*Bulk Data Download — Data Dictionary and Reference Guide*, **Document Version 2.0,
Rev. 4/25**, prepared by the National Information Center. The machine-readable schemas and
code lists in this repository (`csv/NIC_*.csv`) are transcribed verbatim from that PDF.

## The Five Bulk Files

The download is delivered as five pipe/CSV files. Record counts below are from the FFIEC
release and confirmed by on-disk row counts (`wc -l` minus header):

| File | Records | Description |
|------|--------:|-------------|
| `CSV_ATTRIBUTES_ACTIVE.CSV` | 61,080 | Currently open & active institutions (current characteristics) |
| `CSV_ATTRIBUTES_CLOSED.CSV` | 160,494 | Last instance of closed / failed institutions (historical) |
| `CSV_ATTRIBUTES_BRANCHES.CSV` | 172,819 | Last instance of branches whose head office is Active or Closed |
| `CSV_RELATIONSHIPS.CSV` | 284,934 | Ownership-relationship history between entities |
| `CSV_TRANSFORMATIONS.CSV` | 58,749 | Mergers, splits, sales, failures |
| **TOTAL** | **738,076** | — |

**Table-family roles:**

- **Attributes** (3 files) — every entity has exactly one Attributes row carrying its
  legal/common descriptors, classification, regulatory status, geography, identifiers, and
  lifecycle dates. The three files split by status: *Active* (open & active), *Closed*
  (last instance of a closed or failed institution), and *Branches* (last instance of
  branches under an Active or Closed head office). Full schema:
  [`csv/NIC_ATTRIBUTES_SCHEMA.csv`](../csv/NIC_ATTRIBUTES_SCHEMA.csv).
- **Relationships** — the time-series history of ownership/control between two entities
  (parent → offspring). Full schema:
  [`csv/NIC_RELATIONSHIPS_SCHEMA.csv`](../csv/NIC_RELATIONSHIPS_SCHEMA.csv).
- **Transformations** — the event log of mergers, purchases & assumptions, splits, sales,
  and failures. Full schema:
  [`csv/NIC_TRANSFORMATIONS_SCHEMA.csv`](../csv/NIC_TRANSFORMATIONS_SCHEMA.csv).

All code lists for every coded field across all three tables are in
[`csv/NIC_CODE_LISTS.csv`](../csv/NIC_CODE_LISTS.csv) (40 code lists, 274 values).

**Update cadence:** The Federal Reserve refreshes the public NPW bulk extract
periodically (the file set is regenerated from the live NIC database; many derived fields
such as `PRIM_FED_REG` are recomputed nightly inside NIC). Treat each download as a
point-in-time snapshot and re-pull for the latest structure; the dictionary version
(here v2.0, Rev. 4/25) governs the schema.

## The Entity Model

### ID_RSSD — the master key

Every entity in NIC has exactly one **`ID_RSSD`** ("RSSD ID"): a unique one-up number with
a check digit, assigned by the RSSD software when the entity is first entered.

- It **carries no inherent attribute information**.
- It **never changes and is never reused.**
- It belongs to one entity for that entity's entire life cycle and **persists after
  liquidation or closure.**

This makes `ID_RSSD` the universal join key across all NIC tables *and* the bridge to the
FFIEC financial collections (the Call Report / FR Y-9 / FR Y-14 panels all key on RSSD).
See [IDENTIFIERS.md](IDENTIFIERS.md) for how RSSD relates to FDIC Cert, OCC charter, NCUA,
LEI, CUSIP, Tax ID/EIN, and ABA routing numbers (and which of those are reusable — RSSD is
not; ABA routing numbers are reusable across non-concurrent entities).

### Primary keys per table

| Table | Primary key |
|-------|-------------|
| Attributes | `ID_RSSD` + `D_DT_START` |
| Relationships | `ID_RSSD_PARENT` + `ID_RSSD_OFFSPRING` + `D_DT_START` + `RELN_LVL` |
| Transformations | `ID_RSSD_PRECESSOR` + `ID_RSSD_SUCCESSOR` + `D_DT_TRANS` |

> **Spelling caution:** the dictionary prose says "predecessor," but the actual
> Transformations column name is **`ID_RSSD_PRECESSOR`** (the Fed's own typo). Use the
> misspelled form in queries.

### Date-field convention

Every integer date field `DT_*` (format `YYYYMMDD`) has a paired DB2-`DATETIME` field
`D_DT_*` (format `'YYYY-MM-DD HH:MM:SS'`, **must be quoted in SQL**). The sentinel
**`99991231`** means a non-terminated record/entity (i.e., still current). The Attributes
and Relationships rows are valid over a `[DT_START, DT_END]` window; filter
`DT_END = 99991231` to get the current state.

### The parent → offspring relationship model

Relationships rows connect a **Parent** (`ID_RSSD_PARENT`, the controlling entity) to an
**Offspring** (`ID_RSSD_OFFSPRING`, the owned/controlled entity). The key qualifiers:

- **`CTRL_IND`** — whether the parent *controls* the offspring (`1` = controlled,
  `2` = non-controlled). For regulated relationships (`REG_IND = 1`) control means legal
  authority: ≥25% of voting securities, control over a majority of directors, or a
  controlling influence per Reg Y §225.2(e) / 12 CFR 574.
- **`RELN_LVL`** — relationship level: `1` = **Direct** (parent is the immediate holder),
  `2` = **Indirect** (an intervening company ties the offspring to the top-tier U.S. BHC or
  FBO), `3` = 2G3 (repealed 1996, no longer reportable), `4` = Debt Previously Contracted.
- **`PCT_EQUITY`** / `PCT_EQUITY_BRACKET` — the parent's percent of equity/voting control.
  Exact for BHC/bank/FBO direct holders; reported as a bracket (`100*`, `80 - <100`,
  `>50 - <80`, `25 - 50`, `< 25`, `0`) for non-banking offspring.
- **`EQUITY_IND`** / `REG_IND` / `FC_IND` — basis of control, whether the relationship is
  regulated, and whether the offspring is financially consolidated in the parent.

Because both direct and indirect rows are stored, you can build a complete holding-company
tree: indirect rows tie every controlled entity to the **top-tier** parent, while direct
rows give you the immediate ownership edges.

### The transformation / merger-event model

Transformations is an event log. Each row links a **Predecessor**
(`ID_RSSD_PRECESSOR` — in a merger, the non-survivor) to a **Successor**
(`ID_RSSD_SUCCESSOR` — the survivor) on an effective date `DT_TRANS`, classified by
**`TRNSFM_CD`**:

| `TRNSFM_CD` | Event |
|------:|-------|
| 1 | Charter Discontinued (Merger or Purchase & Assumption); one charter ends, no failure |
| 5 | Split (predecessor transfers 40–94% of assets to newly-formed successor(s); both continue) |
| 7 | Sale of Assets (40–94% to an existing successor; both continue) |
| 9 | Charter Retained (≥95% of assets transferred; charter continues under a new `ID_RSSD`) |
| 50 | **Failure, Government Assistance Provided** (predecessor fails and ceases; disposition by FDIC/RTC/NCUA/other) |

For non-failure mergers where the survivor is a commercial bank, non-deposit trust company,
or industrial bank (`CHTR_TYPE_CD` 200/250/340), `ACCT_METHOD` records pooling-of-interests
(`1`) vs purchase/acquisition (`2`).

## Worked Examples

### A. Trace a BHC's subsidiaries

1. Find the holding company's `ID_RSSD` in Attributes (e.g. by `NM_LGL`), confirming
   `BHC_IND = 1` (or `FHC_IND = 1` for a financial holding company).
2. In Relationships, select rows where `ID_RSSD_PARENT = <the BHC's RSSD>` and
   `DT_END = 99991231` (current) and `CTRL_IND = 1` (controlled).
   - Use `RELN_LVL = 1` for the **immediate** (direct) subsidiaries.
   - Use `RELN_LVL = 2` to pull **every** entity indirectly controlled anywhere in the
     structure tree (because indirect rows tie each entity to the top-tier parent).
3. Join each `ID_RSSD_OFFSPRING` back to Attributes on `ID_RSSD` to get the subsidiary's
   name (`NM_LGL`), charter type (`CHTR_TYPE_CD`), entity type (`ENTITY_TYPE`), and
   regulator (`PRIM_FED_REG`).
4. To count just the U.S. *banking* subsidiaries, restrict offspring to `BROAD_REG_CD = 1`
   — this is exactly how NIC derives the Attributes field `BANK_CNT`.

```sql
-- Current banking subsidiaries of a given BHC
SELECT a.ID_RSSD, a.NM_LGL, a.CHTR_TYPE_CD, a.PRIM_FED_REG
FROM relationships r
JOIN attributes a ON a.ID_RSSD = r.ID_RSSD_OFFSPRING
WHERE r.ID_RSSD_PARENT = :bhc_rssd
  AND r.DT_END = 99991231
  AND r.CTRL_IND = 1
  AND a.BROAD_REG_CD = 1;
```

### B. Identify a bank failure

There are two complementary signals; use both for completeness:

- **Attributes (`REASON_TERM_CD`)** — on the head-office row in
  `CSV_ATTRIBUTES_CLOSED.CSV`: `4` = *failure, entity continues to exist* (resolved by
  FDIC/RTC/NCUA/State/other, no Transformation row) and `5` = *failure, entity ceases to
  exist* (a Transformation row may or may not be present). So `REASON_TERM_CD IN (4, 5)`
  flags failed institutions. (Contrast `1` = voluntary liquidation and `2` = closure,
  which are **not** failures.)
- **Transformations (`TRNSFM_CD = 50`)** — *Failure, Government Assistance Provided*: the
  predecessor failed and ceased, with disposition arranged by a resolution authority.

```sql
-- Failed institutions
SELECT ID_RSSD, NM_LGL, DT_EXIST_TERM, REASON_TERM_CD
FROM attributes_closed
WHERE REASON_TERM_CD IN (4, 5);

-- Government-assisted failures (event view)
SELECT ID_RSSD_PRECESSOR, ID_RSSD_SUCCESSOR, DT_TRANS
FROM transformations
WHERE TRNSFM_CD = 50;
```

Link the resulting RSSDs to FDIC failure records via `ID_FDIC_CERT`, and to historical
bank panels (e.g. pre-1990 series) via an RSSD crosswalk. Note that the Fed's RSSD system
generally does not cover institutions closed before ~1960, so very old failures will not
have an `ID_RSSD`.

## Field & Code Reference

The complete, transcribed-verbatim reference lives in the machine-readable CSVs:

| File | Contents |
|------|----------|
| [`csv/NIC_ATTRIBUTES_SCHEMA.csv`](../csv/NIC_ATTRIBUTES_SCHEMA.csv) | All 74 Attributes columns (identifiers, classification, regulatory status, geography, names, dates, termination) |
| [`csv/NIC_RELATIONSHIPS_SCHEMA.csv`](../csv/NIC_RELATIONSHIPS_SCHEMA.csv) | All 22 Relationships columns |
| [`csv/NIC_TRANSFORMATIONS_SCHEMA.csv`](../csv/NIC_TRANSFORMATIONS_SCHEMA.csv) | All 6 Transformations columns |
| [`csv/NIC_CODE_LISTS.csv`](../csv/NIC_CODE_LISTS.csv) | 40 code lists, 274 values (ENTITY_TYPE, CHTR_TYPE_CD, BNK_TYPE_ANALYS_CD, BROAD_REG_CD, ORG_TYPE_CD, EST_TYPE_CD, INSUR_PRI_CD, PRIM_FED_REG, REASON_TERM_CD, TRNSFM_CD, RELN_LVL, etc.) |

A few high-traffic code lists are summarized below; the CSV is authoritative.

**`CHTR_TYPE_CD` (Charter Type):** 200 Commercial Bank · 250 Non-deposit Trust Co ·
300 Savings Bank · 310 Savings & Loan Assoc · 320 Cooperative Bank · 330 Credit Union ·
340 Industrial Bank · 400 Edge/Agreement Corp · 500 Holding Company only ·
700 Securities Broker/Dealer · 720 Other Non-Depository · 110 Government Agency/GSE ·
550 Insurance · 610 ESOP/ESOT · 710 Utility/Co-generator · 0 N/A (branches).

**`PRIM_FED_REG` (Primary Federal Regulator):** FRS · OCC · FDIC · NCUA · FCA · FHFA ·
OTS (valid only through 2011-07-21). Can change over an entity's history; null for
branches/non-bank subs; derived nightly.

**`ENTITY_TYPE`:** 44 derived codes (NAT, SMB, NMB, FSB, SSB, SAL, FCU, SCU, BHC, FHD,
FHF, SLHC, IHC, FBO, FBH, FBK, DBR, IBR, EDB, EDI, etc.) — see CSV.

> **Verification note:** the source-facts digest used during this rebuild labeled
> `ENTITY_TYPE` as "49 codes," but the NPW PDF (and the digest's own enumeration) list
> exactly **44** codes (AGB … USB). This guide and the CSV use the PDF-verified 44.

## Relationship to Other Data

- **FFIEC financial collections** — join on `ID_RSSD` to attach Call Report / FR Y-9C /
  FR Y-14 financials to NIC structure. See [COLLECTIONS_CATALOG.md](COLLECTIONS_CATALOG.md).
- **Identifier crosswalks** — `ID_FDIC_CERT` → FDIC SDI/failure data; `ID_OCC` → OCC;
  `ID_NCUA` → credit unions; `ID_LEI` → GLEIF. See [IDENTIFIERS.md](IDENTIFIERS.md).
- **Historical bank panels** — pre-FFIEC institutions (closed before ~1960) have no RSSD
  and require name/state fuzzy crosswalking.

## Data Sources

- **Bulk data & institution search:** <https://www.ffiec.gov/NPW>
- **Authoritative dictionary:** Board of Governors / NIC, *Bulk Data Download — Data
  Dictionary and Reference Guide*, **Document Version 2.0, Rev. 4/25** (the source of every
  field and code in `csv/NIC_*.csv`).

## Notes

- `ID_RSSD` is the single most important field in the entire dataset: stable, unique,
  never reused — the spine for linking structure to financials and to external identifiers.
- Use `DT_END = 99991231` to filter for current records in Attributes and Relationships.
- Branches (`EST_TYPE_CD > 1`) point to their head office via `ID_RSSD_HD_OFF` and carry
  `0`/N/A in many entity-level fields (`CHTR_TYPE_CD`, `ORG_TYPE_CD`, `BHC_IND`).
- Failure analysis should combine Attributes `REASON_TERM_CD IN (4,5)` with Transformations
  `TRNSFM_CD = 50` — neither alone is complete.
