# Call Report Schedule RC-E - Deposit Liabilities

> **Deposit Detail for FDIC-Insured Banks**
>
> Form: FFIEC 031/041/051 | Frequency: Quarterly

---

## Overview

Schedule RC-E provides detailed breakdowns of a bank's deposit liabilities by account type, ownership category, and interest-bearing status. This information is critical for:
- Deposit insurance assessment calculations
- Liquidity coverage ratio (LCR) analysis
- Interest rate sensitivity analysis
- Core deposits vs. volatile funding analysis

---

## Machine-readable line items

The full, triple-attested per-line-item code set for this schedule ships as
[`csv/CALL_RC_E_DEPOSITS.csv`](../csv/CALL_RC_E_DEPOSITS.csv) (55 rows; provenance in
`_rebuild/schedules/PROVENANCE_CALL_RC_E.csv`). Each row carries `line_number`,
`item_description`, `column` (A/B/C), `column_description`, `mdrm_code`, `forms`
(031/041/051 applicability), `category`, `start_date`, and `notes`. The tables below are
a human-readable digest of that CSV, reconciled to the FFIEC December 2025 form grids.

### CSV schema

| Column | Meaning |
|--------|---------|
| line_number | Form item number (e.g. `1`, `7`, `M.1.b`) |
| item_description | Official caption from the FFIEC form grid |
| column | Grid column: `A` total transaction, `B` memo total demand, `C` total nontransaction, `-` single-column memorandum |
| column_description | Plain-language column label |
| mdrm_code | Federal Reserve MDRM code (RCON, domestic offices) |
| forms | Which forms report the item (031/041/051) |
| category | `Deposit Categories` or `Memoranda` |
| start_date | MDRM start date for the code |
| notes | Grid-level column/derivation note |

---

## MDRM Prefix Guide for Deposits

| Prefix | Scope | Typical Use |
|--------|-------|-------------|
| RCON | Domestic offices | All RC-E deposit-category and memoranda items |
| RCFN | Foreign offices | Foreign-branch deposit detail (reported elsewhere) |
| RCFD | Total (consolidated) | Combined total where published |

> On the current FFIEC 031/041/051 forms, every Schedule RC-E line item is reported on the
> **RCON (domestic-office)** basis. The codes below are identical across all three forms; the
> `forms` column in the CSV records applicability (four sweep-deposit memoranda are 031-only).

---

## Part I: Deposit categories (columns A / B / C)

Schedule RC-E reports each ownership category in **column A** (total transaction accounts,
including total demand deposits) and **column C** (total nontransaction accounts, including
MMDAs). Item 7 (the total line) adds **column B**, a memorandum for total demand deposits
included in column A.

| Item | Description | Col A (transaction) | Col C (nontransaction) | Forms |
|------|-------------|---------------------|------------------------|-------|
| 1 | Deposits of individuals, partnerships, and corporations | RCONB549 | RCONB550 | 031/041/051 |
| 2 | Deposits of U.S. Government | RCON2202 | RCON2520 | 031/041/051 |
| 3 | Deposits of states and political subdivisions in the U.S. | RCON2203 | RCON2530 | 031/041/051 |
| 4 | Deposits of commercial banks and other depository institutions in the U.S. | RCONB551 | RCONB552 | 031/041/051 |
| 5 | Deposits of banks in foreign countries | RCON2213 | RCON2236 | 031/041/051 |
| 6 | Deposits of foreign governments and official institutions | RCON2216 | RCON2377 | 031/041/051 |
| 7 | Total (sum of items 1 through 6) | RCON2215 | RCON2385 | 031/041/051 |

> Item 7 column B (memo: total demand deposits included in column A) = **RCON2210**.

---

## Deposit Categories Summary

### By Interest Status

| Category | MDRM | Description |
|----------|------|-------------|
| Noninterest-bearing (domestic) | RCON6631 | DDA, zero-rate accounts |
| Interest-bearing (domestic) | RCON6636 | NOW, MMDA, time deposits |
| Noninterest-bearing (foreign) | RCFNB537 | Foreign office NI |
| Interest-bearing (foreign) | RCFNB538 | Foreign office IB |

### By Insurance Status

| Category | Description | MDRM |
|----------|-------------|------|
| Insured deposits | Under $250K FDIC limit | RCONF049 |
| Uninsured deposits | Over FDIC limit | RCONF051 |
| Preferred deposits | Collateralized public | Various |

---

## Key Totals and Reconciliations

### Total Deposits
```
RC Item 13 (RCFD2200) = RC Item 13.a (RCON2200) + RC Item 13.b (RCFNB536)
                       = Domestic deposits + Foreign deposits
```

### Domestic Deposits
```
RCON2200 = RCON6631 (Noninterest) + RCON6636 (Interest-bearing)
```

---

## Deposit Stability Analysis

### Core vs. Non-Core Deposits

| Category | Typical Treatment | LCR Runoff |
|----------|-------------------|------------|
| Retail transaction | Core, stable | 3-10% |
| Retail savings | Core, stable | 3-10% |
| Retail time <$250K | Core | 3-10% |
| Jumbo CDs >$250K | Less stable | 10-40% |
| Brokered deposits | Volatile | 10-40% |
| Public funds | Volatile | 25-40% |

---

## Memoranda Items

The full memoranda set (M.1 through M.7, including the sweep-deposit and IPC-component
breakouts) is in [`csv/CALL_RC_E_DEPOSITS.csv`](../csv/CALL_RC_E_DEPOSITS.csv) with
`category = Memoranda`. Selected high-use items:

| Item | Description | MDRM | Purpose |
|------|-------------|------|---------|
| M.1.a | Total IRAs and Keogh Plan accounts | RCON6835 | Retirement deposit detail |
| M.1.b | Total brokered deposits | RCON2365 | Volatile funding |
| M.1.c | Brokered deposits of $250,000 or less (fully insured) | RCONHK05 | Insured brokered |
| M.1.e | Preferred deposits (uninsured public funds) | RCON5590 | Collateralized public |
| M.1.g | Total reciprocal deposits | RCONJH83 | Network deposits |
| M.2.b | Total time deposits of less than $100,000 | RCON6648 | Small CDs |
| M.2.c | Total time deposits of $100,000 through $250,000 | RCONJ473 | Mid CDs |
| M.2.d | Total time deposits of more than $250,000 | RCONJ474 | Jumbo CDs |
| M.5 | Offers consumer deposit account products? (Yes/No) | RCONP752 | Reporting-scope flag |

> Note: the four `M.1.h.…(a)` retail sweep-deposit sub-items are reported on FFIEC 031 only;
> all other RC-E codes are common to 031/041/051. Estimated insured/uninsured deposit amounts
> are reported on Schedule RC-O, not RC-E.

---

## Cross-Schedule Relationships

| RC-E Ties To | Relationship |
|--------------|--------------|
| RC Item 13 | Total deposits on balance sheet |
| RC-K | Average deposits |
| RC-O | Fiduciary deposits |
| FR 2052a | LCR deposit runoff calculations |

---

## LCR/NSFR Implications

### LCR Deposit Runoff Rates

| Deposit Type | Runoff Rate | Category |
|--------------|-------------|----------|
| Stable retail | 3% | Insured, relationship |
| Less stable retail | 10% | Higher rate, other |
| Small business | 5-10% | Covered, not covered |
| Operational wholesale | 25% | Clearing, custody |
| Non-operational wholesale | 40% | Other wholesale |
| Unsecured wholesale funding | 100% | Short-term |

### NSFR Treatment

| Deposit Type | ASF Factor | Rationale |
|--------------|------------|-----------|
| Stable retail <1yr | 95% | Highly stable |
| Less stable retail <1yr | 90% | Mostly stable |
| Wholesale operational <1yr | 50% | Moderate stability |
| Other wholesale <1yr | 0-50% | Depends on type |

---

## Mapping to FR Y-9C

The FR Y-9C consolidates bank deposits at the holding company level. Note that on Schedule HC, total deposits (line 13) is a caption with no single atomic MDRM code; it is the sum of its domestic and foreign components, each split by interest status:
- Schedule HC Item 13 (total deposits) = Item 13.a (domestic) + Item 13.b (foreign)
- Schedule HC Item 13.a (deposits in domestic offices) = BHDM6631 (noninterest-bearing) + BHDM6636 (interest-bearing)
- Schedule HC Item 13.b (deposits in foreign offices) = BHFN6631 (noninterest-bearing) + BHFN6636 (interest-bearing)

---

---

## Sources and attestation

Line items reconciled to the **FFIEC Call Report forms and instructions (December 2025)**,
cross-checked against the **CDR XBRL taxonomy** (v294 presentation linkbase, per-form concept
inventory) and the **Federal Reserve MDRM** code dictionary, with empirical presence verified
in **FFIEC bulk Call Report data (2001-2026)**. Per-code provenance is in
`_rebuild/schedules/PROVENANCE_CALL_RC_E.csv`; the attestation ledger is in
`_rebuild/empirical/attestations/CALL_ATTESTATION_RCE_RCN_RCR.csv`.

*Last updated: 2026-06-11*
