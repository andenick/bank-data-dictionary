# MDRM — Micro Data Reference Manual (the meta-dictionary)

The **MDRM (Micro Data Reference Manual)** is the Federal Reserve's master catalog of the
micro and macro data items collected from depository institutions and other respondents. It is
the **meta-dictionary that ties the entire Fed/FFIEC reporting universe together** — Call
Reports (FFIEC 031/041/051), the FR Y-9 holding-company family, the FFIEC 101/102 capital and
market-risk reports, the Thrift Financial Report, and dozens of other forms all draw their
coded variables from it. Every variable used elsewhere in this repository ultimately resolves
to an MDRM code.

> Naming note: the official expansion is **Micro Data Reference Manual**. "Master Data
> Reference Manual" appears in some downstream documentation as a variant — both refer to the
> same Fed MDRM. (Source: `federalreserve.gov/apps/mdrm/about_mdrm.htm`.)

---

## 1. What the MDRM is

Per the Fed's *About MDRM* page, the MDRM is "a catalog of micro and macro data collected from
depository institutions and other respondents." It documents the labels and values associated
with each data item, organized into **reports/data series**. The public web application
(`https://www.federalreserve.gov/apps/mdrm/`) exposes two main sections:

1. **Reporting Forms and Mnemonics** — links each reporting form's public name to its MDRM
   series mnemonic(s), with a brief description of each series.
2. **Data Dictionary** — defines each *item* (the numeric portion of the code) and lists every
   series on which that item is available, with applicable dates and full descriptions.

---

## 2. The 8-character code: mnemonic + item number

Every MDRM reference number is **8 characters = a 4-character series mnemonic + a 4-character
item code**:

```
  B H C K   2 1 7 0
  └──┬──┘   └──┬──┘
  mnemonic   item code
 (series/form) (the concept)
```

- The **mnemonic** is unique to a data series and names the reporting form / scope (e.g.
  `RCON`, `RCFD`, `BHCK`, `SVGL`).
- The **item number** is *reused across mnemonics* so the same concept can be compared across
  series. The Fed's own example: item **2170 = Total Assets** appears as `RCON2170`
  (domestic), `RCFD2170` (bank consolidated), `BHCK2170` (BHC consolidated), and `SVGL2170`
  (Thrift Financial Report). (Source: `about_mdrm.htm`.)

This mnemonic/item split is exactly what a cross-form bank-data dictionary keys on, and why the
**prefix/namespace system** (below) is the backbone of this repository.

---

## 3. The BHCK scope finding (v6.0 correction)

**Question resolved:** earlier drafts of this repo labeled `BHCK` as "BHC domestic operations
only." That is **wrong**.

> **FINDING — VERIFIED: `BHCK` is the FR Y-9C *consolidated* series (domestic + foreign
> combined).** It is the primary/dominant FR Y-9C prefix.

Authoritative evidence:

- **Fed MDRM, item 2170 (Total Assets):** `BHCK2170` is described as consolidated total assets
  for bank holding companies (domestic **and** foreign operations); `RCON2170` is the
  domestic-only analog, `RCFD2170` the bank-level consolidated analog.
  (`federalreserve.gov/apps/mdrm/data-dictionary/search/item?keyword=2170`)
- **Fed MDRM, item 3792 (Total risk-based capital):** `BHCK3792` is described as the
  consolidated FR Y-9C total risk-based capital (Schedule HC-R).
  (`.../search/item?keyword=3792`)
- **Federal Reserve Bank of Chicago — Holding Company Data FAQ:** "Variables for Y9C, LP and SP
  data are differentiated by their prefix… **the prefix BHCK is for Y9C data**, BHCP is for
  Y9LP data, and BHSP for Y9SP data."
  (`chicagofed.org/banking/financial-institution-reports/bhc-data-faq`)

The scope split on the FR Y-9C is therefore:

| Prefix | FR Y-9C scope | Status |
|---|---|---|
| **BHCK** | **Consolidated** (domestic + foreign) — the main series | **VERIFIED** |
| **BHDM** | **Domestic offices only** (e.g. `BHDM6631`/`BHDM6636` domestic deposits) | **VERIFIED** |
| **BHFN** | **Foreign offices only** / Edge & Agreement subs / IBFs (e.g. `BHFN6631`) | **VERIFIED** |
| **BHCA** | **Consolidated** — Schedule HC-R risk-based (standardized) capital | **VERIFIED** (item 3792) |
| **BHCW** | **Consolidated** — Schedule HC-R advanced-approaches/Basel III capital (2014+) | **VERIFIED** (item 3792) |
| **BHCP** | **Parent company only** — reported on **FR Y-9LP** (not Y-9C) | **VERIFIED** |
| **BHSP** | **Parent company only** (small HCs) — **FR Y-9SP** | **VERIFIED** |
| BHCT, BHCM, BHCB, BHCAP, BHCFA | scope **UNVERIFIED** — see below | **UNVERIFIED** |

**Still UNVERIFIED** (could not confirm against an official MDRM item page; prior labels are
*not* corroborated — do **not** treat the old labels as fact):

- `BHCT` — prior label "total consolidated" is unconfirmed; note `BHCK` is already the confirmed
  consolidated-total series. Candidate: a per-schedule "total" variant.
- `BHCM` — prior label "domestic post-2018 breakout" is unconfirmed. Candidate readings:
  memoranda items, or domestic-office items.
- `BHCB` — not confirmed against MDRM.
- `BHCAP` — prior label "advanced approaches" is unconfirmed; the **confirmed** advanced-
  approaches capital series is `BHCW`, not `BHCAP`.
- `BHCFA` — prior label "regulatory capital" is unconfirmed; confirmed HC-R series are `BHCA`
  and `BHCW`.

These are flagged `UNVERIFIED` in `csv/MDRM_PREFIX_DEFINITIONS.csv` and
`csv/MDRM_NAMESPACES.csv` with their candidate readings. Resolve them by looking up a known
item on each series at the Fed MDRM Data Dictionary before relying on them.

---

## 4. The prefix / namespace system

The 4-character mnemonic encodes both **form family** and **scope** (consolidation /
domestic / foreign / parent-only). The repository ships two machine-readable catalogues:

- **[`csv/MDRM_PREFIX_DEFINITIONS.csv`](../csv/MDRM_PREFIX_DEFINITIONS.csv)** — the headline
  prefixes most analysts touch (BHCK/BHDM/BHFN, RCON/RCFD/RCFN/RIAD, UBPR…), with scope and
  consolidation flags.
- **[`csv/MDRM_NAMESPACES.csv`](../csv/MDRM_NAMESPACES.csv)** — the fuller namespace catalogue:
  the whole FR Y-9 family (BHCK, BHDM, BHFN, BHCT, BHCM, BHCP, BHCB, BHCA, BHCAP, BHCFA, BHCW,
  BHSP), the Call Report family (RCFD, RCON, RCFN, RCOA, RCFA, RIAD, RCFW), UBPR
  (UBPR/UBPRE/UBPRM + peer UBPS/UBPK), FR Y-15 (RISK), NCUA 5300 (FS220), and the Thrift
  Financial Report (SVGL).

Quick reference — the consolidation pattern that recurs across form families:

| Concept | BHC (FR Y-9C) | Bank (Call Report) |
|---|---|---|
| Consolidated (domestic + foreign) | `BHCK` | `RCFD` |
| Domestic offices only | `BHDM` | `RCON` |
| Foreign offices only | `BHFN` | `RCFN` |
| Risk-based capital (RC-R / HC-R) | `BHCA` (std), `BHCW` (advanced) | `RCFA`/`RCOA` (std), `RCFW` (advanced) |
| Income statement (YTD flow) | `RIAD` (HI) | `RIAD` (RI) |
| Parent company only | `BHCP` (Y-9LP), `BHSP` (Y-9SP) | — |

> Important: UBPR codes like `UBPRE001` are the **`UBPR` mnemonic** + a 4-char item code
> beginning with a topic letter (`E…` = earnings, `M…` = memoranda). `UBPRE`/`UBPRM` are
> **not** separate 4-character MDRM mnemonics; they are convenience groupings, flagged as such
> in the CSVs. The genuinely distinct peer namespaces are `UBPS` (peer stats) and `UBPK`
> (peer rank).

---

## 5. The `MDRM_CSV.csv` data file

The downloadable dictionary (`MDRM_CSV.csv`) carries one row per mnemonic+item. A typical
ingest parses it into an 11-column table — the 10 source columns plus a derived
`variable_id = mnemonic + item_code`:

| # | Column | Meaning |
|---|---|---|
| 1 | Mnemonic | 4-char series/form code |
| 2 | Item Code (Item Number) | 4-char item — the concept |
| 3 | Item Name | Human label (e.g. "Total Assets") |
| 4 | Start Date | First reporting date the item applies |
| 5 | End Date | Last reporting date (open if still active) |
| 6 | Confidentiality | `Y`/`N` — whether the item is confidential |
| 7 | Item Type | Category: financial/reported, structure, rate, examination, percentage, or derived (per *About MDRM*) |
| 8 | Reporting Form | The specific form the item appears on |
| 9 | Description | What is to be reported for the item |
| 10 | Series Glossary | Series-level (mnemonic) descriptive info |
| (+) | variable_id | Derived `mnemonic‖item_code` |

Parse mechanics (typical, for the raw `MDRM_CSV.csv`):

- The file begins with a literal `PUBLIC` header line that is skipped (rewind if absent).
- UTF-8-sig; `csv.DictReader`; rows with empty mnemonic or item code are dropped.
- Dates parsed `"%m/%d/%Y %I:%M:%S %p"` (fallback `"%m/%d/%Y"`) → `YYYY-MM-DD`, else NULL.
- Descriptions are `html.unescape`d and whitespace-collapsed (the raw file contains HTML
  entities and quoted fields).
- A confidential-items-only list can be generated from the download page via a checkbox.

---

## 6. Downloading the MDRM

| | |
|---|---|
| **Web app / search** | https://www.federalreserve.gov/apps/mdrm/ |
| **About** | https://www.federalreserve.gov/apps/mdrm/about_mdrm.htm |
| **Download** | https://www.federalreserve.gov/apps/mdrm/download_mdrm.htm |
| **File** | `MDRM.zip` (~6.6 MB) containing `MDRM_CSV.csv` + `README.txt` |
| **Search by** | item number, item name, series mnemonic, or reporting-form name |

**Item count:** a full parse of the dictionary yields on the order of **87,000+ rows**
(observed ~87,351 in one recent load). The official download page does **not** publish a
count, so treat **~87,000+** as an order-of-magnitude figure — **UNVERIFIED** as an exact total.

---

## 7. Sources (official)

- Fed MDRM home — https://www.federalreserve.gov/apps/mdrm/
- About MDRM — https://www.federalreserve.gov/apps/mdrm/about_mdrm.htm
- Download MDRM — https://www.federalreserve.gov/apps/mdrm/download_mdrm.htm
- MDRM Data Dictionary, item 2170 (Total Assets) — https://www.federalreserve.gov/apps/mdrm/data-dictionary/search/item?keyword=2170
- MDRM Data Dictionary, item 3792 (Total risk-based capital) — https://www.federalreserve.gov/apps/mdrm/data-dictionary/search/item?keyword=3792
- Federal Reserve Bank of Chicago — Holding Company Data FAQ (BHCK/BHCP/BHSP prefixes) — https://www.chicagofed.org/banking/financial-institution-reports/bhc-data-faq
- FR Y-9C File Upload User Guide (BHDM/BHFN deposit items) — https://www.frbservices.org/binaries/content/assets/crsocms/central-bank/reporting-central/fr-y-9c-user-guide.pdf

See also: **[`csv/MDRM_PREFIX_DEFINITIONS.csv`](../csv/MDRM_PREFIX_DEFINITIONS.csv)** and
**[`csv/MDRM_NAMESPACES.csv`](../csv/MDRM_NAMESPACES.csv)**.
