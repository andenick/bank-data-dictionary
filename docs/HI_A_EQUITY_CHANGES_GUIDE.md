# Schedule HI-A: Changes in Holding Company Equity Capital Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HI-A - Changes in Holding Company Equity Capital
**Frequency**: Quarterly (year-to-date rollforward)
**Purpose**: Reconcile beginning-of-year holding company equity capital to end-of-period equity capital, line by line

---

## Overview

Schedule HI-A is the statement of changes in equity for the consolidated holding company. It is a year-to-date *rollforward*: it begins with prior-year-end equity, applies the year's net income, capital issuances and retirements, treasury-stock transactions, dividends, other comprehensive income, and miscellaneous adjustments, and arrives at end-of-period total equity capital. The ending balance is a hard control: it must equal Schedule HC item 27.a.

### Who Files

All FR Y-9C reporters complete HI-A.

---

## Schedule Structure

```
CHANGES IN HOLDING COMPANY EQUITY CAPITAL (year-to-date)
├── 1.  Prior calendar year-end equity capital (as most recently reported)
├── 2.  Cumulative effect of accounting-principle changes / error corrections
├── 3.  Balance end of previous year as restated (= 1 + 2)
├── 4.  Net income (loss) attributable to holding company (= HI item 14)
├── 5.  Perpetual preferred stock: 5.a sale (gross), 5.b conversion/retirement
├── 6.  Common stock: 6.a sale (gross), 6.b conversion/retirement
├── 7.  Sale of treasury stock
├── 8.  LESS: Purchase of treasury stock
├── 9.  Changes incident to business combinations, net
├── 10. LESS: Cash dividends declared on preferred stock
├── 11. LESS: Cash dividends declared on common stock
├── 12. Other comprehensive income
├── 13. Change in ESOP-debt offsetting debit
├── 14. Other adjustments to equity capital
└── 15. TOTAL end-of-period equity capital (= HC item 27.a)
```

---

## Detailed Line Items

| Line | MDRM | Description |
|------|------|-------------|
| 1 | BHCK3217 | Total equity capital most recently reported for end of previous calendar year |
| 2 | BHCKB507 | Cumulative effect of changes in accounting principles and corrections of material errors |
| 3 | BHCKB508 | Balance end of previous calendar year as restated (= 1 + 2) |
| 4 | BHCT4340 | Net income (loss) attributable to holding company |
| 5.a | BHCK3577 | Sale of perpetual preferred stock, gross |
| 5.b | BHCK3578 | Conversion or retirement of perpetual preferred stock |
| 6.a | BHCK3579 | Sale of common stock, gross |
| 6.b | BHCK3580 | Conversion or retirement of common stock |
| 7 | BHCK4782 | Sale of treasury stock |
| 8 | BHCK4783 | LESS: Purchase of treasury stock |
| 9 | BHCK4356 | Changes incident to business combinations, net |
| 10 | BHCK4598 | LESS: Cash dividends declared on preferred stock |
| 11 | BHCK4460 | LESS: Cash dividends declared on common stock |
| 12 | BHCKB511 | Other comprehensive income |
| 13 | BHCK4591 | Change in the offsetting debit to the liability for ESOP debt guaranteed by the holding company |
| 14 | BHCK3581 | Other adjustments to equity capital (not included above) |
| 15 | BHCT3210 | Total holding company equity capital end of current period |

**Other comprehensive income (item 12)** includes, among other things, changes in net unrealized holding gains/losses on available-for-sale debt securities, accumulated gains/losses on cash-flow hedges, foreign-currency translation adjustments, and pension/postretirement-plan adjustments other than net periodic benefit cost.

---

## Reconciliation / Ties

The schedule is a closed arithmetic rollforward:

```
Item 15 (BHCT3210)
   = item 3 + item 4 + item 5 + item 6 + item 7 + item 9 + item 12 + item 13 + item 14
     − item 8 − item 10 − item 11

CONTROL TIES:
  Item 4  (BHCT4340)  =  Schedule HI item 14  (net income attributable to HC)
  Item 15 (BHCT3210)  =  Schedule HC item 27.a (total holding company equity capital)
```

These two ties (HI net income into item 4; ending equity into HC item 27.a) make HI-A the bridge between the income statement (HI) and the equity section of the balance sheet (HC items 26-28 / 27.a). Other comprehensive income (item 12) connects to HC item 26.b (accumulated other comprehensive income).

---

## Pitfalls

- **"LESS" items are subtractions.** Items 8 (treasury-stock purchases), 10 (preferred dividends), and 11 (common dividends) are subtracted in the item-15 formula even though they are reported as positive amounts. Adding them instead of subtracting overstates ending equity.
- **Item 5 and item 6 are two-line groups.** The item-15 formula references "item 5" and "item 6" as the *net* of their .a (sale) and .b (conversion/retirement) sub-lines.
- **Year-to-date, not quarterly.** HI-A accumulates from the start of the calendar year; first-quarter and fourth-quarter figures are not comparable as standalone quarterly flows.
- **Total cells use `BHCT`.** Items 4 and 15 use `BHCT…` total codes (Federal Reserve-edited control cells); the transaction lines use `BHCK…`.

---

## Verification & Provenance

- **MDRM:** all 17 line codes joined to the Federal Reserve MDRM codeset; 17 of 17 verified present, with start/end dates recorded.
- **Warehouse evidence:** every HI-A code is observed in the Federal Reserve bulk BHCF data (1986-2025); the equity-rollforward codes (`3217`, `4340`, `3210`, etc.) span the full history.
- **Call analogue:** because HI-A is an income/equity-statement schedule, most lines have a same-item `RIAD…` analogue on the Call Report (e.g., item 1 -> RIAD3217), recorded in `call_mdrm` where a name-matched code exists.
- **Provenance file:** `_rebuild/schedules/PROVENANCE_HI_A.csv`.
- **Sources:** Federal Reserve MDRM; FR Y-9C form and instructions (March 2026); Federal Reserve bulk BHCF data (1986-2025).

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCK3217 | Prior year-end equity capital |
| 2 | BHCKB507 | Accounting-change / error-correction effect |
| 3 | BHCKB508 | Restated beginning balance (= 1 + 2) |
| 4 | BHCT4340 | Net income (= HI item 14) |
| 5.a / 5.b | BHCK3577 / BHCK3578 | Perpetual preferred: sale / conversion-retirement |
| 6.a / 6.b | BHCK3579 / BHCK3580 | Common stock: sale / conversion-retirement |
| 7 / 8 | BHCK4782 / BHCK4783 | Treasury stock: sale / LESS purchase |
| 9 | BHCK4356 | Business-combination changes, net |
| 10 / 11 | BHCK4598 / BHCK4460 | LESS dividends: preferred / common |
| 12 | BHCKB511 | Other comprehensive income |
| 13 | BHCK4591 | ESOP-debt offsetting-debit change |
| 14 | BHCK3581 | Other equity adjustments |
| **15** | **BHCT3210** | **TOTAL end-of-period equity** (= HC item 27.a) |

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C form and instructions (March 2026); Federal Reserve MDRM; Federal Reserve bulk BHCF data (1986-2025)*
