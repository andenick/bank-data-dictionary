# Schedule HC-V: Variable Interest Entities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-V - Variable Interest Entities
**Frequency**: Quarterly
**Purpose**: Disclose the assets and liabilities of consolidated variable interest entities (VIEs), split between securitization vehicles and other VIEs, plus asset-backed commercial paper (ABCP) conduit totals

---

## Overview

Under ASC 810 (consolidation of variable interest entities), a holding company that is the primary beneficiary of a VIE consolidates that entity onto its balance sheet. Schedule HC-V isolates the portion of the consolidated balance sheet that belongs to VIEs whose assets can be used only to settle VIE obligations and whose creditors have no recourse to the general credit of the reporting holding company. This lets analysts separate "ring-fenced" VIE assets/liabilities from the holding company's own.

### Who Files

Schedule HC-V is completed by holding companies with **$5 billion or more in total assets** (asset-size test based on prior-year June 30 total assets).

---

## CSV Schema

`HC_V_VIES.csv` is a **two-column grid** schedule. Each line reports the same item under two VIE types, so the CSV uses column-specific code columns:

`line_number, item_description, mdrm_col_a_securitization, mdrm_col_b_other_vies, call_mdrm_col_a, category, ties_to_hc_line, start_date, notes`

- **Column A = Securitization Vehicles** (`mdrm_col_a_securitization`)
- **Column B = Other VIEs** (`mdrm_col_b_other_vies`)

Items 5 and 6 (ABCP conduit totals) are single-column; their amounts go in the column-A field and column B is "-".

---

## Schedule Structure

```
VARIABLE INTEREST ENTITIES                    Col A: Securitization | Col B: Other VIEs
├── 1. Assets of consolidated VIEs (settle only VIE obligations)
│   ├── 1.a Cash and balances due from depository institutions
│   ├── 1.b Securities not held for trading
│   ├── 1.c Loans and leases HFI (net of allowance) and HFS
│   ├── 1.d Other real estate owned
│   └── 1.e Other assets
├── 2. Liabilities of consolidated VIEs (no recourse to general credit)
│   ├── 2.a Other borrowed money
│   └── 2.b Other liabilities
├── 3. All other assets of consolidated VIEs (not in 1.a-1.e)
├── 4. All other liabilities of consolidated VIEs (not in 2.a-2.b)
├── 5. Total assets of ABCP conduit VIEs (single column)
└── 6. Total liabilities of ABCP conduit VIEs (single column)
```

---

## Detailed Line Items

### Assets and liabilities of consolidated VIEs (two columns)

| Line | Col A (Securitization) | Col B (Other VIEs) | Description |
|------|------------------------|--------------------|-------------|
| 1.a | BHCKJ981 | BHCKJF84 | Cash and balances due from depository institutions |
| 1.b | BHCKHU20 | BHCKHU21 | Securities not held for trading |
| 1.c | BHCKHU22 | BHCKHU23 | Loans and leases HFI (net of allowance) and HFS |
| 1.d | BHCKK009 | BHCKJF89 | Other real estate owned |
| 1.e | BHCKJF91 | BHCKJF90 | Other assets |
| 2.a | BHCKJF92 | BHCKJF85 | Other borrowed money |
| 2.b | BHCKJF93 | BHCKJF86 | Other liabilities |
| 3 | BHCKK030 | BHCKJF87 | All other assets of consolidated VIEs (not in 1.a-1.e) |
| 4 | BHCKK033 | BHCKJF88 | All other liabilities of consolidated VIEs (not in 2.a-2.b) |

### ABCP conduit totals (single column)

| Line | MDRM | Description |
|------|------|-------------|
| 5 | BHCKJF77 | Total assets of asset-backed commercial paper (ABCP) conduit VIEs |
| 6 | BHCKJF78 | Total liabilities of ABCP conduit VIEs |

**Items 1-2** report only VIE assets/liabilities meeting the ring-fencing criteria (assets usable only to settle VIE obligations; liabilities without recourse to the holding company's general credit). **Items 3-4** capture the residual consolidated-VIE assets/liabilities that do not meet those criteria or fall outside the named categories. **Items 5-6** are memo totals for ABCP conduit VIEs specifically.

---

## Reconciliation / Ties

HC-V does not have a single schedule total; its lines are *subset* disclosures whose balances are already consolidated into the corresponding Schedule HC lines:

```
HC-V 1.a (cash)            ⊂  HC item 1   (cash and balances due)
HC-V 1.b (securities)      ⊂  HC item 2   (securities not held for trading)
HC-V 1.c (loans/leases)    ⊂  HC item 4   (loans and leases)
HC-V 1.d (OREO)            ⊂  HC item 7   (premises / OREO)
HC-V 2.a (other borrowed)  ⊂  HC item 16  (other borrowed money)
HC-V 2.b (other liab.)     ⊂  HC item 20  (other liabilities)
```

The HC-V amounts identify how much of each HC balance-sheet line is attributable to consolidated VIEs; they are not added on top of HC.

---

## Pitfalls

- **Two columns with distinct codesets.** Column A (securitization vehicles) and Column B (other VIEs) use different MDRM codes for the same caption (e.g., 1.a is `BHCKJ981` in A but `BHCKJF84` in B). Collapsing on the caption loses the VIE-type split.
- **Items 5-6 are single-column.** The ABCP conduit totals have only one code each; do not expect a column-B value.
- **Subset, not additive.** HC-V is a "look-through" into HC; summing HC-V into HC double-counts. Use HC-V to *attribute* HC balances to VIEs.
- **Conditional schedule.** Only $5B+ filers complete HC-V; many filers leave it blank.

---

## Verification & Provenance

- **MDRM:** all 20 line×column codes joined to the Federal Reserve MDRM codeset; 20 of 20 verified present, with start/end dates recorded.
- **Warehouse evidence:** every HC-V code is observed in the Federal Reserve bulk BHCF data (1986-2025); the VIE codes appear from 2010-2011 (post-ASU 2009-17 consolidation), consistent with their MDRM start dates.
- **Provenance file:** `_rebuild/schedules/PROVENANCE_HC_V.csv` (one row per line×column cell, so 20 rows for 11 lines).
- **Sources:** Federal Reserve MDRM; FR Y-9C form and instructions (March 2026); Federal Reserve bulk BHCF data (1986-2025).

---

## MDRM Quick Reference

| Line | Col A | Col B | Description |
|------|-------|-------|-------------|
| 1.a | BHCKJ981 | BHCKJF84 | Cash and balances due |
| 1.b | BHCKHU20 | BHCKHU21 | Securities not held for trading |
| 1.c | BHCKHU22 | BHCKHU23 | Loans and leases HFI/HFS |
| 1.d | BHCKK009 | BHCKJF89 | Other real estate owned |
| 1.e | BHCKJF91 | BHCKJF90 | Other assets |
| 2.a | BHCKJF92 | BHCKJF85 | Other borrowed money |
| 2.b | BHCKJF93 | BHCKJF86 | Other liabilities |
| 3 | BHCKK030 | BHCKJF87 | All other VIE assets |
| 4 | BHCKK033 | BHCKJF88 | All other VIE liabilities |
| 5 | BHCKJF77 | - | ABCP conduit total assets |
| 6 | BHCKJF78 | - | ABCP conduit total liabilities |

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C form and instructions (March 2026); Federal Reserve MDRM; Federal Reserve bulk BHCF data (1986-2025)*
