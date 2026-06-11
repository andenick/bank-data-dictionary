# Schedule HI-C: Disaggregated Data on the Allowance for Credit Losses Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HI-C - Disaggregated Data on the Allowance for Credit Losses
**Frequency**: Semiannual (June and December) for the filers in scope
**Purpose**: Disaggregate the allowance for credit losses (and, for loans, the associated amortized cost) across loan/lease portfolio segments and held-to-maturity security types

---

## Overview

Schedule HI-C provides a portfolio-segment breakdown of the allowance for credit losses (ACL) under the CECL model (ASC 326). It has two blocks:

- **Loans and Leases Held for Investment (items 1-6)** - a two-column grid: Column A = Amortized Cost, Column B = Allowance Balance, by portfolio segment (real estate, commercial, credit cards, other consumer), plus an unallocated line and a total.
- **Held-to-Maturity Securities (items 7-11)** - a single-column block (Allowance Balance) by security type, plus a total.

It is the disaggregated companion to the HI-B Part II allowance rollforward: HI-B says *how* the allowance changed; HI-C says *where* the ending allowance sits.

### Who Files

Items 1 through 11 are completed **semiannually in the June and December reports by holding companies with less than $5 billion in total assets** (asset-size test based on prior-year June 30 total assets).

---

## CSV Schema

`HI_C_ALLOWANCE.csv` is a partial-grid schedule and uses two code columns:

`line_number, item_description, mdrm_col_a_amortized_cost, mdrm_col_b_allowance, call_mdrm_col_a, category, ties_to_hc_line, start_date, notes`

- **Items 1-6 (loans HFI):** Column A = Amortized Cost (`mdrm_col_a_amortized_cost`), Column B = Allowance Balance (`mdrm_col_b_allowance`).
- **Item 5 (Unallocated) and items 7-11 (HTM securities):** Allowance Balance only - the code goes in `mdrm_col_b_allowance` and column A is "-".

---

## Schedule Structure

```
DISAGGREGATED ALLOWANCE FOR CREDIT LOSSES
├── Loans and Leases Held for Investment   (Col A: Amortized Cost | Col B: Allowance)
│   ├── 1. Real estate loans
│   │   ├── 1.a Construction loans
│   │   ├── 1.b Commercial real estate loans
│   │   └── 1.c Residential real estate loans
│   ├── 2. Commercial loans
│   ├── 3. Credit cards
│   ├── 4. Other consumer loans
│   ├── 5. Unallocated, if any            (Allowance Balance only)
│   └── 6. Total (sum of 1.a through 5)   (Col B = HC item 4.c)
└── Held-to-Maturity Securities           (Allowance Balance only)
    ├── 7.  States and political subdivisions in the U.S.
    ├── 8.  Total mortgage-backed securities (MBS)
    ├── 9.  Asset-backed securities and structured financial products
    ├── 10. Other debt securities
    └── 11. Total (sum of 7 through 10)    (= HI-B Part II item 7 Col B)
```

---

## Detailed Line Items

### Loans and Leases Held for Investment (two columns)

| Line | Col A (Amortized Cost) | Col B (Allowance) | Description |
|------|------------------------|-------------------|-------------|
| 1.a | BHCKJJ04 | BHCKJJ12 | Real estate - construction loans |
| 1.b | BHCKJJ05 | BHCKJJ13 | Real estate - commercial real estate loans |
| 1.c | BHCKJJ06 | BHCKJJ14 | Real estate - residential real estate loans |
| 2 | BHCKJJ07 | BHCKJJ15 | Commercial loans |
| 3 | BHCKJJ08 | BHCKJJ16 | Credit cards |
| 4 | BHCKJJ09 | BHCKJJ17 | Other consumer loans |
| 5 | - | BHCKJJ18 | Unallocated, if any (allowance only) |
| **6** | **BHCKJJ11** | **BHCKJJ19** | **Total (sum of 1.a through 5); Col B = HC item 4.c** |

**Commercial loans (item 2)** is a residual: it includes all loans and leases not reported as real estate loans (item 1), credit cards (item 3), or other consumer loans (item 4).

### Held-to-Maturity Securities (allowance balance only)

| Line | MDRM (Allowance) | Description |
|------|------------------|-------------|
| 7 | BHCKJJ20 | Securities issued by states and political subdivisions in the U.S. |
| 8 | BHCKJJ21 | Total mortgage-backed securities (incl CMOs, REMICs, stripped MBS) |
| 9 | BHCKJJ23 | Asset-backed securities and structured financial products |
| 10 | BHCKJJ24 | Other debt securities |
| **11** | **BHCKJJ25** | **Total (sum of 7 through 10); = HI-B Part II item 7 Col B** |

---

## Reconciliation / Ties

```
LOANS HFI:
  Item 6 Col A (BHCKJJ11)  =  sum of amortized cost, items 1.a through 5 (Col A)
  Item 6 Col B (BHCKJJ19)  =  sum of allowance,       items 1.a through 5 (Col B)
                           =  Schedule HC item 4.c (allowance for loan/lease losses)
                           =  Schedule HI-B Part II item 7 Col A (ending loan allowance)

HTM SECURITIES:
  Item 11 (BHCKJJ25)  =  sum of allowance, items 7 through 10
                      =  Schedule HI-B Part II item 7 Col B (ending HTM allowance)
```

HI-C thus pins the HI-B Part II ending allowance balances to portfolio-segment detail: the loans total (item 6 Col B) reconciles to HC item 4.c and HI-B Part II item 7 Col A; the HTM total (item 11) reconciles to HI-B Part II item 7 Col B.

---

## Pitfalls

- **Item 5 and items 7-11 have no amortized-cost column.** Only loan segments 1-4 and the total (item 6) carry Column A (amortized cost); the unallocated line and all HTM-security lines are allowance-only. Expecting a Column A value there is an error.
- **Item 2 "Commercial loans" is a catch-all.** It absorbs everything not classed as real estate, credit cards, or other consumer; do not treat it as C&I-only.
- **Semiannual, small-filer schedule.** HI-C is completed only by < $5B filers, and only in June and December. Most large-bank panels will show HI-C blank in March/September and for $5B+ filers - by design.
- **CECL-era codes.** All HI-C codes (`BHCKJJ04`-`BHCKJJ25`) are CECL-era (effective 2021), so HI-C has no pre-CECL history.

---

## Verification & Provenance

- **MDRM:** all 20 line×column codes joined to the Federal Reserve MDRM codeset; 20 of 20 verified present, with start/end dates recorded.
- **Warehouse evidence:** every HI-C code is observed in the Federal Reserve bulk BHCF data (1986-2025); first appearance is 2021, consistent with the CECL effective date and the MDRM start dates.
- **Provenance file:** `_rebuild/schedules/PROVENANCE_HI_C.csv` (one row per line×column cell, so 20 rows for 13 lines).
- **Sources:** Federal Reserve MDRM; FR Y-9C form and instructions (March 2026); Federal Reserve bulk BHCF data (1986-2025).

---

## MDRM Quick Reference

| Line | Col A (Amortized Cost) | Col B (Allowance) | Description |
|------|------------------------|-------------------|-------------|
| 1.a | BHCKJJ04 | BHCKJJ12 | RE - construction |
| 1.b | BHCKJJ05 | BHCKJJ13 | RE - commercial |
| 1.c | BHCKJJ06 | BHCKJJ14 | RE - residential |
| 2 | BHCKJJ07 | BHCKJJ15 | Commercial loans |
| 3 | BHCKJJ08 | BHCKJJ16 | Credit cards |
| 4 | BHCKJJ09 | BHCKJJ17 | Other consumer |
| 5 | - | BHCKJJ18 | Unallocated |
| 6 | BHCKJJ11 | BHCKJJ19 | Total loans HFI (= HC 4.c) |
| 7 | - | BHCKJJ20 | HTM - states/political subdivisions |
| 8 | - | BHCKJJ21 | HTM - total MBS |
| 9 | - | BHCKJJ23 | HTM - ABS / structured products |
| 10 | - | BHCKJJ24 | HTM - other debt securities |
| 11 | - | BHCKJJ25 | HTM total (= HI-B Pt II item 7 Col B) |

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C form and instructions (March 2026); Federal Reserve MDRM; Federal Reserve bulk BHCF data (1986-2025)*
