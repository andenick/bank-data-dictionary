# Schedule HC-P: 1-4 Family Residential Mortgage Banking Activities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-P - Closed-End 1-4 Family Residential Mortgage Banking Activities in Domestic Offices
**Frequency**: Quarterly
**Purpose**: Measure the volume and income of the holding company's 1-4 family residential mortgage origination, sale, securitization, and servicing activity, plus repurchase exposure and representation-and-warranty reserves

---

## Overview

Schedule HC-P captures the *flow* of residential mortgage banking activity during the quarter (originations, sales, repurchases, income) and the *stock* of mortgages held for sale and of representation-and-warranty reserves at quarter-end. It lets analysts size a holding company's mortgage-banking franchise and gauge its gain-on-sale income and put-back (repurchase) risk.

### Who Files

Schedule HC-P is completed by holding companies with **$5 billion or more in total assets** at which **any one** of the following exceeds **$10 million for two consecutive quarters** in domestic offices:

- 1-4 family residential mortgage loan originations and purchases for resale (from all sources), or
- loan sales, or
- quarter-end loans held for sale or trading.

The asset-size test is based on total assets reported as of the prior-year June 30 report date.

---

## Schedule Structure

```
1-4 FAMILY RESIDENTIAL MORTGAGE BANKING ACTIVITIES (domestic offices)
├── 1. Retail originations during the quarter (loans for sale)
├── 2. Wholesale originations and purchases during the quarter (loans for sale)
├── 3. 1-4 family residential mortgages sold during the quarter
├── 4. 1-4 family residential mortgages held for sale/trading at quarter-end
├── 5. Noninterest income from sale/securitization/servicing
├── 6. Repurchases and indemnifications during the quarter
└── 7. Representation and warranty reserves
    ├── 7.a To U.S. government agencies and government-sponsored agencies
    ├── 7.b To other parties
    └── 7.c Total (= 7.a + 7.b)
```

Items 1-3 and 6 are quarterly *flows*; items 4 and 7 are quarter-end *stocks*; item 5 is a quarterly *income* flow.

---

## Detailed Line Items

| Line | MDRM | Description |
|------|------|-------------|
| 1 | BHCKHT81 | Retail originations during the quarter of 1-4 family residential mortgage loans for sale |
| 2 | BHCKHT82 | Wholesale originations and purchases during the quarter of 1-4 family residential mortgage loans for sale |
| 3 | BHCKFT04 | 1-4 family residential mortgages sold during the quarter |
| 4 | BHCKFT05 | 1-4 family residential mortgages held for sale or trading at quarter-end |
| 5 | BHCKHT85 | Noninterest income from the sale, securitization, and servicing of 1-4 family residential mortgage loans |
| 6 | BHCKHT86 | Repurchases and indemnifications of 1-4 family residential mortgage loans during the quarter |
| 7.a | BHCKL191 | Representation and warranty reserves - to U.S. government agencies and GSEs |
| 7.b | BHCKL192 | Representation and warranty reserves - to other parties |
| 7.c | BHCKM288 | Total representation and warranty reserves (= 7.a + 7.b) |

**Originations for sale (items 1-2)** exclude loans originated or purchased to be *held for investment*; only the resale pipeline is reported here. **Item 5 income** is a subset of several HI fee lines (see ties). **Items 7.a/7.b** disaggregate the put-back reserve by counterparty; only the **total (7.c)** is carried in the public bulk BHCF data (see Pitfalls).

---

## Reconciliation / Ties

```
HC-P item 4 (BHCKFT05)   ⊂  Schedule HC items 4.a (loans HFS) and 5 (trading assets)
HC-P item 5 (BHCKHT85)   ⊂  Schedule HI items 5.c, 5.f, 5.g, and 5.i (mortgage-
                            banking-related noninterest income)
HC-P item 7.c (BHCKM288)  =  HC-P items 7.a + 7.b (rep & warranty reserve total)
```

These are *subset* ties (the HC-P amounts are components included within the broader HC/HI lines), not standalone control totals - HC-P has no schedule total.

---

## Pitfalls

- **Domestic offices, closed-end, 1-4 family only.** The schedule scope is narrow: closed-end first/junior-lien 1-4 family residential mortgages in domestic offices. Open-end (HELOC), multifamily, and commercial mortgages are out of scope.
- **"For sale" vs. "held for investment."** Items 1-2 deliberately exclude loans originated to hold; mixing in held-for-investment originations overstates the mortgage-banking pipeline.
- **7.a / 7.b not in public bulk data.** Items 7.a and 7.b are MDRM-valid (effective 2012-06) but the Federal Reserve does **not** carry these two sub-components in the public bulk BHCF download; only the total (7.c, `BHCKM288`) is populated there. This is a known public-data gap, not a reporting error - filers do report 7.a/7.b on the form. The provenance file records this (BHCF first/last seen blank for `BHCKL191`/`BHCKL192`).
- **Conditional schedule.** Many holding companies leave HC-P blank because they fall below the $5B / $10M two-consecutive-quarters thresholds. A blank schedule is a valid filing.

---

## Verification & Provenance

- **MDRM:** all 9 line codes joined to the Federal Reserve MDRM codeset; 9 of 9 verified present, with start/end dates recorded.
- **Warehouse evidence:** 7 of the 9 codes are observed in the Federal Reserve bulk BHCF data (1986-2025); items 7.a (`BHCKL191`) and 7.b (`BHCKL192`) are absent from the public bulk numeric data by Federal Reserve design (see Pitfalls), while their total 7.c (`BHCKM288`) is present from 2012 Q3.
- **Provenance file:** `_rebuild/schedules/PROVENANCE_HC_P.csv`.
- **Sources:** Federal Reserve MDRM; FR Y-9C form and instructions (March 2026); Federal Reserve bulk BHCF data (1986-2025).

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCKHT81 | Retail originations for sale |
| 2 | BHCKHT82 | Wholesale originations and purchases for sale |
| 3 | BHCKFT04 | Mortgages sold during the quarter |
| 4 | BHCKFT05 | Mortgages held for sale/trading at quarter-end |
| 5 | BHCKHT85 | Noninterest income from sale/securitization/servicing |
| 6 | BHCKHT86 | Repurchases and indemnifications |
| 7.a | BHCKL191 | Rep & warranty reserves - U.S. govt agencies / GSEs |
| 7.b | BHCKL192 | Rep & warranty reserves - other parties |
| **7.c** | **BHCKM288** | **Total rep & warranty reserves** (= 7.a + 7.b) |

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C form and instructions (March 2026); Federal Reserve MDRM; Federal Reserve bulk BHCF data (1986-2025)*
