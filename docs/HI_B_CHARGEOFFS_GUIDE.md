# Schedule HI-B: Charge-Offs and Recoveries on Loans and Leases and Changes in Allowances for Credit Losses Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HI-B - Charge-Offs and Recoveries on Loans and Leases and Changes in Allowances for Credit Losses
**Frequency**: Quarterly (year-to-date)
**Purpose**: Report year-to-date charge-offs and recoveries by loan/lease category (Part I) and roll forward the allowances for credit losses across loans/leases, held-to-maturity securities, and available-for-sale securities (Part II)

---

## Overview

Schedule HI-B has two parts plus memoranda:

- **Part I - Charge-offs and Recoveries on Loans and Leases (Fully Consolidated).** A two-column grid (Column A = Charge-offs, Column B = Recoveries) reporting year-to-date gross charge-offs and recoveries by the same loan/lease categories used in Schedule HC-C.
- **Part II - Changes in Allowances for Credit Losses.** A three-column rollforward (Column A = Loans and leases held for investment; Column B = Held-to-maturity debt securities; Column C = Available-for-sale debt securities) reconciling beginning to ending allowance balances.

Together they connect the income statement's provision expense (HI item 4) to the balance sheet's allowance (HC item 4.c) and to the disaggregated allowance detail in Schedule HI-C.

### Who Files

All FR Y-9C reporters complete HI-B. Several lines are asset-size-conditional: filers with less than $5 billion in total assets report combined lines (4.c, 8.c) and leave the disaggregated lines (4.a/4.b, 8.a/8.b) blank; items 6 and several memoranda apply only to $5B+ filers.

---

## CSV Schema

`HI_B_CHARGEOFFS.csv` is a **grid** schedule and uses up to three column-specific code columns:

`line_number, item_description, mdrm_col_a, mdrm_col_b, mdrm_col_c, call_mdrm_col_a, category, ties_to_hc_line, start_date, notes`

- **Part I rows:** `mdrm_col_a` = Charge-offs, `mdrm_col_b` = Recoveries, `mdrm_col_c` = "-".
- **Part II rows:** `mdrm_col_a` = Loans/leases HFI, `mdrm_col_b` = HTM debt securities, `mdrm_col_c` = AFS debt securities.
- **Single-column memoranda** (PI.M.3, PII.M.1-M.8) put their code in `mdrm_col_a`; B and C are "-".

Line keys are prefixed `PI.*` (Part I) and `PII.*` (Part II) to keep the restarted item numbering unique.

---

## Detailed Line Items

### Part I - Charge-offs (Col A) and Recoveries (Col B), by loan/lease category

| Line | Col A (Charge-offs) | Col B (Recoveries) | Category |
|------|---------------------|--------------------|----------|
| PI.1.a.(1) | BHCKC891 | BHCKC892 | 1-4 family residential construction |
| PI.1.a.(2) | BHCKC893 | BHCKC894 | Other construction / land development |
| PI.1.b. | BHCK3584 | BHCK3585 | Secured by farmland (domestic offices) |
| PI.1.c.(1) | BHCK5411 | BHCK5412 | Revolving open-end 1-4 family (HELOCs) |
| PI.1.c.(2)(a) | BHCKC234 | BHCKC217 | Closed-end 1-4 family, first liens |
| PI.1.c.(2)(b) | BHCKC235 | BHCKC218 | Closed-end 1-4 family, junior liens |
| PI.1.d. | BHCK3588 | BHCK3589 | Multifamily (domestic offices) |
| PI.1.e.(1) | BHCKC895 | BHCKC896 | Owner-occupied nonfarm nonresidential |
| PI.1.e.(2) | BHCKC897 | BHCKC898 | Other nonfarm nonresidential |
| PI.1.f. | BHCKB512 | BHCKB513 | RE in foreign offices |
| PI.3 | BHCK4655 | BHCK4665 | Agricultural production / farmers (item 2 N/A) |
| PI.4.a. | BHCK4645 | BHCK4617 | C&I - U.S. addressees |
| PI.4.b. | BHCK4646 | BHCK4618 | C&I - non-U.S. addressees |
| PI.4.c. | BHCKKX48 | BHCKKX49 | C&I - combined (< $5B filers) |
| PI.5.a. | BHCKB514 | BHCKB515 | Consumer - credit cards |
| PI.5.b. | BHCKK129 | BHCKK133 | Consumer - automobile loans |
| PI.5.c. | BHCKK205 | BHCKK206 | Consumer - other |
| PI.6 | BHCK4643 | BHCK4627 | Foreign governments / official institutions |
| PI.7 | BHCK4644 | BHCK4628 | All other loans |
| PI.8.a. | BHCKF185 | BHCKF187 | Leases to individuals |
| PI.8.b. | BHCKC880 | BHCKF188 | All other leases |
| PI.8.c. | BHCKKX50 | BHCKKX51 | Leases combined (< $5B filers) |
| **PI.9** | **BHCK4635** | **BHCK4605** | **Total (sum of items 1-8)** |
| PI.M.1 | BHCK5409 | BHCK5410 | Memo: CRE/construction/land (not RE-secured) |
| PI.M.2 | BHCK4652 | BHCK4662 | Memo: RE loans to non-U.S. addressees |
| PI.M.3 | BHCKC388 | - | Memo: uncollectible retail credit-card fees reversed (single column) |

### Part II - Allowance rollforward (Col A = Loans/leases HFI, Col B = HTM securities, Col C = AFS securities)

| Line | Col A (Loans/leases) | Col B (HTM sec.) | Col C (AFS sec.) | Description |
|------|----------------------|------------------|------------------|-------------|
| PII.1 | BHCKB522 | BHCKJH88 | BHCKJH94 | Beginning balance (prior year-end, restated) |
| PII.2 | BHCT4605 | BHCKJH89 | BHCKJH95 | Recoveries (Col A = Part I item 9 Col B) |
| PII.3 | BHCKC079 | BHCKJH92 | BHCKJH98 | LESS: Charge-offs |
| PII.4 | BHCK5523 | BHCKJJ00 | BHCKJJ01 | LESS: Write-downs from transfers of financial assets |
| PII.5 | BHCK4230 | BHCKJH90 | BHCKJH96 | Provisions for credit losses |
| PII.6 | BHCKC233 | BHCKJH91 | BHCKJH97 | Adjustments |
| **PII.7** | **BHCT3123** | **BHCKJH93** | **BHCKJH99** | **Ending balance (Col A = HC item 4.c)** |

### Part II memoranda (single column)

| Line | MDRM | Description |
|------|------|-------------|
| PII.M.1 | BHCKC435 | Allocated transfer risk reserve (in item 7 Col A) |
| PII.M.2 | BHCKC389 | Separate valuation allowance for retail credit-card fees |
| PII.M.3 | BHCKC390 | ACL attributable to retail credit-card fees |
| PII.M.5 | BHCKJJ02 | Provisions for credit losses on other financial assets at amortized cost |
| PII.M.6 | BHCKJJ03 | ACL on other financial assets at amortized cost |
| PII.M.7 | BHCKMG93 | Provisions for credit losses on off-balance-sheet credit exposures |
| PII.M.8 | BHCKMG94 | Estimated expected recoveries of amounts previously written off |

(Part II item 4 in the *Memoranda* numbering is "Not applicable.")

---

## Reconciliation / Ties

```
PART I:
  PI.9 Col A (BHCK4635)  =  sum of Part I charge-offs, items 1-8
  PI.9 Col B (BHCK4605)  =  sum of Part I recoveries,  items 1-8

CROSS-PART:
  PII.2 Col A (recoveries)  =  Part I item 9 Col B
  PII.3 Col A (charge-offs)  =  Part I item 9 Col A  −  Part II item 4 Col A

INTO THE INCOME STATEMENT AND BALANCE SHEET:
  PII.5 Cols A+B+C (provisions) + memo M.5 + memo M.7  =  Schedule HI item 4
                                                          (provision for credit losses)
  PII.7 Col A (ending allowance on loans/leases HFI)    =  Schedule HC item 4.c

INTO HI-C:
  PII.7 Col B (ending HTM allowance)  =  Schedule HI-C item 11
  PII.7 Col A (ending loan allowance) ties to HI-C item 6, Col B (allowance balance)
```

HI-B is therefore the rollforward whose ending balances feed both the balance sheet (HC item 4.c) and the disaggregated allowance schedule (HI-C).

---

## Pitfalls

- **Three different column meanings.** Part I columns are Charge-offs / Recoveries; Part II columns are Loans-HFI / HTM-securities / AFS-securities. The same `mdrm_col_a` field means "charge-offs" in Part I and "loans/leases HFI allowance" in Part II. Always read the part.
- **"LESS" lines subtract.** Part II items 3 (charge-offs) and 4 (write-downs) are subtracted in the item-7 formula; they are reported as positive amounts.
- **Asset-size conditional lines.** Filers under $5B report combined C&I (4.c) and combined leases (8.c) and leave 4.a/4.b/8.a/8.b blank; $5B+ filers do the reverse. Both patterns are valid; blanks are not gaps.
- **Total cells use `BHCT`.** PI.9 Col B (`BHCK4605`) is a `BHCK` code, but Part II uses `BHCT4605` for recoveries Col A and `BHCT3123` for the ending loan allowance - the same item number `4605` appears under both `BHCK` (Part I total recoveries) and `BHCT` (Part II Col A recoveries) and must not be conflated.
- **Year-to-date.** Part I charge-offs/recoveries and Part II provisions/charge-offs accumulate from the start of the calendar year.

---

## Verification & Provenance

- **MDRM:** all 79 line×column codes joined to the Federal Reserve MDRM codeset; 79 of 79 verified present, with start/end dates recorded.
- **Warehouse evidence:** every HI-B code is observed in the Federal Reserve bulk BHCF data (1986-2025); the CECL-era HTM/AFS allowance columns (`JH8x`/`JH9x`, `JJ0x`) appear from 2020-2021, consistent with their MDRM start dates.
- **Call analogue:** Part I charge-off/recovery items have same-item `RIAD…` analogues on the Call Report Schedule RI-B (e.g., PI.1.b Col A -> RIAD3584), recorded in `call_mdrm_col_a` where a name-matched code exists.
- **Provenance file:** `_rebuild/schedules/PROVENANCE_HI_B.csv` (one row per line×column cell, so 79 rows).
- **Sources:** Federal Reserve MDRM; FR Y-9C form and instructions (March 2026); Federal Reserve bulk BHCF data (1986-2025).

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C form and instructions (March 2026); Federal Reserve MDRM; Federal Reserve bulk BHCF data (1986-2025)*
