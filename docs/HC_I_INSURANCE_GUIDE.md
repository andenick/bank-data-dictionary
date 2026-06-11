# Schedule HC-I: Insurance-Related Underwriting Activities (Including Reinsurance) Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-I - Insurance-Related Underwriting Activities (Including Reinsurance)
**Frequency**: Quarterly
**Purpose**: Report the assets, liabilities, equity, and net income of the holding company's insurance and reinsurance *underwriting* subsidiaries, split between property/casualty and life/health lines

---

## Overview

Schedule HC-I collects condensed financial-statement data for the holding company's insurance-underwriting subsidiaries. It is organized into two parts that mirror the two main insurance business models:

- **Part I - Property and Casualty Underwriting**
- **Part II - Life and Health Underwriting**

Each part reports a short balance sheet (selected assets and liabilities), total equity, and net income for the relevant underwriting subsidiaries. The schedule isolates insurance-underwriting risk - reserves, unearned premiums, separate accounts, policyholder benefits - that is otherwise blended into the consolidated balance sheet.

### Who Files

Schedule HC-I must be completed by **all top-tier holding companies** that have insurance or reinsurance underwriting activities. Within the schedule, **item 1 of each part (Reinsurance recoverables)** is completed only by holding companies with **$10,000,000 or more in reinsurance recoverables** as of the effective date each quarter.

---

## Schedule Structure

```
INSURANCE-RELATED UNDERWRITING ACTIVITIES
├── Part I: Property and Casualty Underwriting
│   ├── Assets
│   │   ├── 1. Reinsurance recoverables (>= $10M filers)
│   │   └── 2. Total assets
│   └── Liabilities / Equity / Income
│       ├── 3. Claims and claims adjustment expense reserves
│       ├── 4. Unearned premiums
│       ├── 5. Total equity
│       └── 6. Net income
└── Part II: Life and Health Underwriting
    ├── Assets
    │   ├── 1. Reinsurance recoverables (>= $10M filers)
    │   ├── 2. Separate account assets
    │   └── 3. Total assets
    └── Liabilities / Equity / Income
        ├── 4. Policyholder benefits and contractholder funds
        ├── 5. Separate account liabilities
        ├── 6. Total equity
        └── 7. Net income
```

Because both parts restart their item numbering at "1", this dictionary disambiguates with line keys `PCI.n` (Part I, Property & Casualty) and `LH.n` (Part II, Life & Health) so that each MDRM code maps to a unique row.

---

## Detailed Line Items

### Part I - Property and Casualty Underwriting

| Line | MDRM | Description |
|------|------|-------------|
| PCI.1 | BHCKB988 | Reinsurance recoverables |
| PCI.2 | BHCKC244 | Total assets |
| PCI.3 | BHCKB990 | Claims and claims adjustment expense reserves |
| PCI.4 | BHCKB991 | Unearned premiums |
| PCI.5 | BHCKC245 | Total equity |
| PCI.6 | BHCKC246 | Net income |

**Claims and claims adjustment expense reserves (PCI.3)** are the P&C loss reserve - the estimated cost of incurred but unpaid claims plus the cost of adjusting them. **Unearned premiums (PCI.4)** are the portion of premiums collected for coverage that has not yet elapsed.

### Part II - Life and Health Underwriting

| Line | MDRM | Description |
|------|------|-------------|
| LH.1 | BHCKC247 | Reinsurance recoverables |
| LH.2 | BHCKB992 | Separate account assets |
| LH.3 | BHCKC248 | Total assets |
| LH.4 | BHCKB994 | Policyholder benefits and contractholder funds |
| LH.5 | BHCKB996 | Separate account liabilities |
| LH.6 | BHCKC249 | Total equity |
| LH.7 | BHCKC250 | Net income |

**Separate account assets/liabilities (LH.2, LH.5)** isolate variable-product assets where investment risk passes to the policyholder. **Policyholder benefits and contractholder funds (LH.4)** are the life/health analogue of the P&C loss reserve - the liability for future policy benefits and deposit-type contract balances.

---

## Reconciliation / Ties

HC-I is a *standalone disclosure* of underwriting-subsidiary financials; its asset/liability lines are not separately added back into a specific HC balance-sheet item (those balances are already consolidated into the relevant HC lines). The clearest tie is at the income level:

```
HC-I net income (PCI.6 + LH.7)  ⊂  Schedule HI item 14 (net income attributable
                                    to the holding company), as a component
```

There is no schedule-total row in HC-I; each line stands on its own. Net income of the underwriting subsidiaries is a *subset* of consolidated net income, not an additive reconciliation.

---

## Pitfalls

- **Two parts, restarted numbering.** Item "1" appears in both Part I and Part II (and "Total assets" is item 2 in Part I but item 3 in Part II). Always key on the part to avoid code collisions; this dictionary uses `PCI.*`/`LH.*` prefixes.
- **No clean Call analogue.** Insurance-underwriting financials are a holding-company-level disclosure; insured-depository Call Reports do not have a corresponding schedule, so every HC-I line has `call_mdrm` = "-".
- **Conditional Reinsurance-recoverables line.** Item 1 of each part is reported only by filers with $10M+ in reinsurance recoverables; a blank here is a valid filing, not a data gap.
- **Total assets is not the sum of the listed asset lines.** The schedule lists only *selected* assets; "Total assets" (PCI.2 / LH.3) is the complete underwriting-subsidiary asset total and will exceed the itemized lines.

---

## Verification & Provenance

- **MDRM:** all 13 line codes joined to the Federal Reserve MDRM codeset; 13 of 13 verified present, with start/end dates recorded.
- **Warehouse evidence:** every HC-I code is observed in the Federal Reserve bulk BHCF data (1986-2025); the `C2xx` codes appear from the mid-2000s consistent with their MDRM start dates.
- **Provenance file:** `_rebuild/schedules/PROVENANCE_HC_I.csv`.
- **Sources:** Federal Reserve MDRM; FR Y-9C form and instructions (March 2026); Federal Reserve bulk BHCF data (1986-2025).

---

## MDRM Quick Reference

| Line | MDRM | Description |
|------|------|-------------|
| PCI.1 | BHCKB988 | P&C - Reinsurance recoverables |
| PCI.2 | BHCKC244 | P&C - Total assets |
| PCI.3 | BHCKB990 | P&C - Claims and claims adjustment reserves |
| PCI.4 | BHCKB991 | P&C - Unearned premiums |
| PCI.5 | BHCKC245 | P&C - Total equity |
| PCI.6 | BHCKC246 | P&C - Net income |
| LH.1 | BHCKC247 | L&H - Reinsurance recoverables |
| LH.2 | BHCKB992 | L&H - Separate account assets |
| LH.3 | BHCKC248 | L&H - Total assets |
| LH.4 | BHCKB994 | L&H - Policyholder benefits and contractholder funds |
| LH.5 | BHCKB996 | L&H - Separate account liabilities |
| LH.6 | BHCKC249 | L&H - Total equity |
| LH.7 | BHCKC250 | L&H - Net income |

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C form and instructions (March 2026); Federal Reserve MDRM; Federal Reserve bulk BHCF data (1986-2025)*
