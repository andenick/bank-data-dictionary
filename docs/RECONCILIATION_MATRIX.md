# FR Y-9C Cross-Schedule Reconciliation Matrix

**Purpose**: Document all tie-outs between FR Y-9C schedules
**Version**: 1.0
**Last Updated**: 2026-01-28

---

## Overview

This matrix documents how all FR Y-9C schedules interconnect. Each schedule detail ties back to the master Schedule HC (Consolidated Balance Sheet) or Schedule HI (Consolidated Income Statement).

---

## Master Reconciliation Hierarchy

```
SCHEDULE HC (Balance Sheet)
│
├─── Item 2 (Securities)
│    └── HC-B Item 8 (Total Securities)
│        ├── Column B: AFS Fair Value → HC Item 2.b
│        ├── Column C: HTM Amortized Cost → HC Item 2.a
│        └── Detail: Items 1-7 by security type
│
├─── Item 4 (Loans)
│    └── HC-C (Loan Portfolio)
│        ├── Items 1-9: Gross loans by type
│        ├── Item 10: Unearned income
│        ├── Item 11: Allowance → HC Item 4.c
│        ├── Item 12: Net loans → HC Item 4.b
│        └── Links to: HC-N (Past Due Detail)
│
├─── Item 5 (Trading Assets)
│    └── HC-D Item 12 (Total Trading Assets)
│        ├── Items 1-5: Securities
│        ├── Item 6: Loans
│        ├── Item 9: Other trading assets
│        └── Item 11: Derivatives → HC-L Fair Values
│
├─── Item 11 (Other Assets)
│    └── HC-F Item 12 (Total Other Assets)
│        └── Items 1-11: Other asset components
│
├─── Item 15 (Trading Liabilities)
│    └── HC-D Item 15 (Total Trading Liabilities)
│        ├── Item 13: Short positions
│        └── Item 14: Derivatives → HC-L Fair Values
│
├─── Item 20 (Other Liabilities)
│    └── HC-G Item 6 (Total Other Liabilities)
│        └── Items 1-5: Other liability components
│
├─── Item 28 (Total Equity)
│    └── HC-R Part I (Regulatory Capital)
│        ├── CET1 components from equity
│        ├── Deductions
│        └── Capital ratios
│
└─── All Items
     ├── HC-H: Interest sensitivity buckets
     ├── HC-K: Quarterly averages
     ├── HC-Q: Fair value hierarchy
     └── HC-S: Securitization activities


SCHEDULE HI (Income Statement)
│
├─── Item 3 (NII)
│    └── Item 1 (Interest Income) - Item 2 (Interest Expense)
│
├─── Item 6.b (Trading Revenue)
│    └── HI-M: Trading revenue by product type
│
└─── Item 12 (Net Income)
     └── Flows to HC Item 26 (Retained Earnings)
```

---

## Detailed Tie-Out Formulas

### Schedule HC ↔ Schedule HC-B (Securities)

| HC Item | HC-B Item | Formula | MDRM |
|---------|-----------|---------|------|
| 2 | 8 | Total securities | *(no single Y-9C code — see note)* |
| 2.a | 8 Col C | HTM amortized cost | BHCKJJ34 |
| 2.b | 8 Col B | AFS fair value | BHCT1773 |
| 2.c | M5 | Equity securities w/ FV | BHCKJA22 |

**Validation**:
```
HC Item 2 = HC Item 2.a + HC Item 2.b + HC Item 2.c
(total securities) = BHCKJJ34 + BHCT1773 + BHCKJA22
```
> **Note:** the FR Y-9C has **no single consolidated total-securities MDRM**; total securities
> is the sum of its three components above. `8641` ("TOTAL SECURITIES") is a **Call Report**
> code (`RCFD8641` / `RCON8641`), not a Y-9C `BHCK`/`BHCT` code.

---

### Schedule HC ↔ Schedule HC-C (Loans)

| HC Item | HC-C Item | Description | MDRM |
|---------|-----------|-------------|------|
| 4.a | 10 | Loans held for sale | BHCT5369 |
| 4.b | Items 1-9 - 10 | Loans net of unearned | BHCTB528 |
| 4.c | 11 | Allowance for loan losses | BHCT3123 |
| 4.d | 12 | Net loans and leases | BHCKB529 |

**Validation**:
```
HC-C Item 12 = Sum(Items 1-9) - Item 10 - Item 11
BHCKB529 = [Real Estate + Ag + C&I + Consumer + Other + Leases] - Unearned - Allowance

HC Item 4.d = HC Item 4.a + HC Item 4.b - HC Item 4.c
```

---

### Schedule HC ↔ Schedule HC-D (Trading)

| HC Item | HC-D Item | Description | MDRM |
|---------|-----------|-------------|------|
| 5 | 12 | Total trading assets | BHCT3545 |
| 15 | 15 | Total trading liabilities | BHCT3548 |

**Validation**:
```
HC Item 5 = HC-D Item 12 (exact match)
HC Item 15 = HC-D Item 15 (exact match)

HC-D Item 12 = Items 1 + 2 + 3 + 4 + 5 + 6 + 9 + 11
HC-D Item 15 = Items 13 + 14
```

---

### Schedule HC-D ↔ Schedule HC-L (Derivatives)

| HC-D Item | HC-L Items | Description |
|-----------|------------|-------------|
| 11 | Fair Value Positive | Derivatives positive FV |
| 14 | Fair Value Negative | Derivatives negative FV |

**Validation**:
```
HC-D Item 11 (BHCT3543) =
  Trading Positive FV (BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736)
  + Non-Trading Positive FV (BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744)

HC-D Item 14 (BHCT3547) =
  Trading Negative FV (BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740)
  + Non-Trading Negative FV (BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748)
```

---

### Schedule HC ↔ Schedule HC-F (Other Assets)

| HC Item | HC-F Item | Description | MDRM |
|---------|-----------|-------------|------|
| 6 | 6 | Premises and fixed assets | BHCK2145 |
| 7 | 7 | Other real estate owned | BHCT2150 |
| 8 | 8 | Investments in unconsolidated subs | BHCK2130 |
| 9 | 9 | RE venture investments | BHCK3656 |
| 10.a | 10.a | Goodwill | BHCK3163 |
| 10.b | 10.b | Other intangible assets | BHCK0426 |
| 11 | 12 | Total other assets | BHCT2160 |

**Validation**:
```
HC-F Item 12 = Sum(Items 1-11)
HC Item 11 = HC-F Item 12
```

---

### Schedule HC ↔ Schedule HC-G (Other Liabilities)

| HC Item | HC-G Item | Description | MDRM |
|---------|-----------|-------------|------|
| 20 | 6 | Total other liabilities | BHCK2750 |

**Validation**:
```
HC-G Item 6 = Sum(Items 1-5)
HC Item 20 = HC-G Item 6
```

---

### Schedule HC-C ↔ Schedule HC-N (Past Due)

HC-N breaks down the same loan categories as HC-C by delinquency status:

| Loan Category | HC-C | HC-N 30-89 | HC-N 90+ | HC-N Nonaccrual |
|---------------|------|------------|----------|-----------------|
| Real estate | Item 1 | BHCK5526 | BHCK1422 | BHCK3492 |
| C&I | Item 4 | BHCK1606 | BHCK1607 | BHCK1608 |
| Consumer | Item 5 | BHCK5383 | BHCK5384 | BHCK5385 |
| Total | Item 12 | BHCK5524 | BHCK5525 | BHCK1403 |

**Validation**:
```
For each loan category:
HC-N (30-89 + 90+ + Nonaccrual) ≤ HC-C balance
(Past due amounts cannot exceed total loan balance)
```

---

### Schedule HC ↔ Schedule HC-R (Capital)

| HC Item | HC-R Part I Item | Description |
|---------|------------------|-------------|
| 28 (Equity) | Starting point | CET1 calculation |
| 10.a (Goodwill) | Item 7 | Deducted from CET1 |
| 10.b (Intangibles) | Item 8 | Deducted from CET1 |

**Validation**:
```
Starting equity reconciliation:
HC Item 28 (Total Equity) ≈
  HC-R Item 1 (Common stock + surplus)
  + HC-R Item 2 (Retained earnings)
  + AOCI adjustments
  + Minority interest

Capital ratio validation:
CET1 Ratio = HC-R Item 19 / HC-R Part II Item 31
Tier 1 Ratio = HC-R Item 24 / HC-R Part II Item 31
Total Capital Ratio = HC-R Item 30 / HC-R Part II Item 31
```

---

### Schedule HC-H (Interest Sensitivity) Validation

HC-H totals should approximate balance sheet items:

| HC-H Item | HC Item | Description |
|-----------|---------|-------------|
| Item 4 Total | ~Items 1-4 | Total IB assets |
| Item 7 Total | ~Items 13-16,19 | Total IB liabilities |

**Validation**:
```
HC-H Item 4, Total ≈ Securities + Loans + Other earning assets
HC-H Item 7, Total ≈ Deposits + Borrowings + Sub debt
```

---

### Schedule HC-K (Averages) Validation

| HC-K Item | Related HC Item | Description |
|-----------|-----------------|-------------|
| Item 9 | Item 12 | Average total assets |
| Item 14 | Item 21 | Average total liabilities |
| Item 15 | Item 28 | Average total equity |

**Validation**:
```
HC-K Item 9 ≈ (Beginning HC Item 12 + Ending HC Item 12) / 2
HC-K Item 9 ≈ HC-K Item 14 + HC-K Item 15 (Assets = Liabilities + Equity)
```

---

### Schedule HC ↔ Schedule HI (Income Statement)

| Connection | From | To |
|------------|------|-----|
| Net Income | HI Item 12 | HC Item 26 (Retained Earnings) |
| Provision | HI Item 4 | Change in HC Item 4.c (Allowance) |
| Trading Revenue | HI Item 6.b | HC-D trading positions |

**Validation**:
```
Change in Retained Earnings ≈ Net Income - Dividends

Allowance change ≈ Provision - Charge-offs + Recoveries
```

---

### Schedule HC-Q (Fair Value) Reconciliation

| HC-Q Item | Related Schedule | MDRM |
|-----------|------------------|------|
| Item 7 (Total assets at FV) | HC (recurring FV assets) | BHCKG502 (Col A, row "Total assets measured at fair value") |
| Item 2 (AFS Securities) | HC-B Item 8 Col B | BHCK1773 |
| Item 14 (Total liabs at FV) | HC (recurring FV liabilities) | BHCKG531 (Col A, row "Total liabilities measured at fair value") |

**Validation**:
```
HC-Q per row: Column A (Total FV on HC) = Level 1 + Level 2 + Level 3 − netting
HC-Q Item 7 (BHCKG502) = Σ items 1-6 (each column)
HC-Q Item 14 (BHCKG531) = Σ items 8-13 (each column)
```

---

## Quick Reference: Primary Tie-Outs

| HC Item | Detail Schedule | Detail Item | MDRM Match |
|---------|-----------------|-------------|------------|
| 2 | HC-B | 8 | *(sum: 1773+JJ34+JA22)* |
| 4.c | HC-C | 11 | BHCT3123 |
| 4.d | HC-C | 12 | BHCKB529 |
| 5 | HC-D | 12 | BHCT3545 |
| 11 | HC-F | 12 | BHCT2160 |
| 15 | HC-D | 15 | BHCT3548 |
| 20 | HC-G | 6 | BHCK2750 |

---

## Data Quality Validation Checklist

### Balance Sheet Validations

- [ ] Total Assets (Item 12) = Sum(Items 1-11)
- [ ] Total Liabilities (Item 21) = Sum(Items 13-20)
- [ ] Item 12 = Item 21 + Item 22 + Item 28
- [ ] HC Item 5 = HC-D Item 12
- [ ] HC Item 11 = HC-F Item 12
- [ ] HC Item 15 = HC-D Item 15
- [ ] HC Item 20 = HC-G Item 6

### Derivatives Validations

- [ ] HC-D Item 11 = Sum(HC-L positive fair values)
- [ ] HC-D Item 14 = Sum(HC-L negative fair values)

### Capital Validations

- [ ] CET1 Ratio within expected range (4.5%+)
- [ ] Tier 1 Ratio ≥ CET1 Ratio
- [ ] Total Capital Ratio ≥ Tier 1 Ratio
- [ ] Leverage Ratio within expected range (4%+)

### Cross-Period Validations

- [ ] YTD figures ≥ prior quarter YTD
- [ ] Averages between beginning and ending balances
- [ ] No unexplained large period-over-period changes

---

## Common Discrepancy Sources

| Issue | Likely Cause | Resolution |
|-------|--------------|------------|
| Small $ differences | Rounding | Accept if < $1M |
| Prefix mismatches | Domestic vs. consolidated | Verify BHCK vs. BHCT |
| Date misalignment | Code changes | Check HISTORICAL_CODE_TRANSITIONS.csv |
| Missing data | Below threshold | Verify reporting requirements |

---

*Last Updated: 2026-01-28*
