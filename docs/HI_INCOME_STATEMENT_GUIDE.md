# Schedule HI: Consolidated Income Statement Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HI - Consolidated Statement of Income
**Frequency**: Quarterly (Year-to-Date)
**Purpose**: Report all income and expenses for the consolidated BHC

---

## Overview

Schedule HI is the income statement for bank holding companies. It provides the P&L structure from interest income through net income, plus detailed breakdowns of non-interest income and expense.

### Key Characteristics

- **Reporting Basis**: Year-to-date (cumulative)
- **MDRM Prefix**: BHCK or BHCT (point-in-time concepts have RIAD Call equivalents)
- **Primary Metric**: Net Income (Item 12)

---

## Income Statement Structure

```
INTEREST INCOME (Item 1)
├── 1.a: Interest and fees on loans
├── 1.b: Interest on balances due
├── 1.c: Interest on securities
├── 1.d: Interest on fed funds sold
├── 1.e: Interest on trading assets
└── 1.f: Other interest income

INTEREST EXPENSE (Item 2)
├── 2.a: Interest on deposits
├── 2.b: Interest on fed funds purchased
├── 2.c: Interest on trading liabilities
├── 2.d: Interest on borrowed money
└── 2.e: Interest on subordinated debt

NET INTEREST INCOME (Item 3)
= Item 1 - Item 2

PROVISION FOR LOAN LOSSES (Item 4)

NII AFTER PROVISION (Item 5)
= Item 3 - Item 4

NONINTEREST INCOME (Item 6)
├── 6.a: Service charges on deposits
├── 6.b: Trading revenue
├── 6.c: Fiduciary fees
├── 6.d: Investment banking fees
├── 6.e: Venture capital revenue
├── 6.f: Servicing fees
├── 6.g: Securitization income
├── 6.h: Insurance commissions
└── 6.i: Other noninterest income

NONINTEREST EXPENSE (Item 7)
├── 7.a: Salaries and benefits
├── 7.b: Occupancy expense
├── 7.c: Premises and equipment
├── 7.d: Amortization of intangibles
├── 7.e: OREO expense
├── 7.f: FDIC assessment
└── 7.g: Other noninterest expense

INCOME BEFORE TAXES (Item 8)
= Item 5 + Item 6 - Item 7

INCOME TAX EXPENSE (Item 9)

INCOME CONT. OPS (Item 10)
= Item 8 - Item 9

EXTRAORDINARY ITEMS (Item 11)

NET INCOME (Item 12)
= Item 10 + Item 11
```

---

## Detailed Line Items

### Item 1: Interest Income

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 1 (Total) | BHCT4107 | RIAD4107 | Total interest income |
| 1.a | BHCK4010 | RIAD4010 | Interest/fees on loans |
| 1.b | BHCK4115 | RIAD4115 | Interest on balances due |
| 1.c | BHCK4107 | RIAD4107 | Interest on securities |
| 1.c.(1) | BHCKB488 | RIADB488 | Treasury/Agency |
| 1.c.(2) | BHCKB489 | RIADB489 | MBS |
| 1.c.(3) | BHCK4060 | RIAD4060 | Other securities |
| 1.d | BHCK4020 | RIAD4020 | Fed funds sold/reverse repos |
| 1.e | BHCK4069 | RIAD4069 | Trading assets |
| 1.f | BHCKB570 | RIADB570 | Other interest income |

### Item 2: Interest Expense

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 2 (Total) | BHCT4073 | RIAD4073 | Total interest expense |
| 2.a | BHCK4170 | RIAD4170 | Deposits |
| 2.b | BHCK4180 | RIAD4180 | Fed funds purchased/repos |
| 2.c | BHCK4185 | RIAD4185 | Trading liabilities |
| 2.d | BHCK4200 | RIAD4200 | Borrowed money |
| 2.e | BHCK4190 | RIAD4190 | Subordinated debt |

### Item 3: Net Interest Income

| MDRM | Formula |
|------|---------|
| BHCT4074 | Item 1 - Item 2 |

**Key Metric**: Net Interest Margin (NIM) = Item 3 / Average Earning Assets (HC-K)

### Item 4: Provision for Loan and Lease Losses

| MDRM | Description |
|------|-------------|
| BHCT4230 | Provision expense for credit losses |

**CECL Note**: Under CECL, this represents the change in lifetime expected credit loss reserves.

### Item 6: Noninterest Income

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 6 (Total) | BHCT4079 | RIAD4079 | Total noninterest income |
| 6.a | BHCK4080 | RIAD4080 | Service charges on deposits |
| 6.b | BHCKA220 | RIADA220 | Trading revenue |
| 6.c | BHCK4070 | RIAD4070 | Fiduciary activities |
| 6.d | BHCKC886 | RIADC886 | Investment banking fees |
| 6.e | BHCKB491 | RIADB491 | Venture capital revenue |
| 6.f | BHCKB492 | RIADB492 | Net servicing fees |
| 6.g | BHCKB493 | RIADB493 | Securitization income |
| 6.h | BHCK4840 | RIAD4840 | Insurance commissions |
| 6.i | BHCK4076 | RIAD4076 | Other noninterest income |

### Item 7: Noninterest Expense

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 7 (Total) | BHCT4093 | RIAD4093 | Total noninterest expense |
| 7.a | BHCK4135 | RIAD4135 | Salaries and benefits |
| 7.b | BHCK4217 | RIAD4217 | Occupancy |
| 7.c | BHCKF556 | RIADF556 | Premises and equipment |
| 7.d | BHCKC232 | RIADC232 | Amortization of intangibles |
| 7.e | BHCK4230 | RIAD4230 | OREO expense |
| 7.f | BHCK4146 | RIAD4146 | FDIC assessment |
| 7.g | BHCK4092 | RIAD4092 | Other noninterest expense |

### Item 12: Net Income

| MDRM | Formula |
|------|---------|
| BHCT4340 | Item 10 + Item 11 |

---

## Key Profitability Metrics

### Net Interest Margin (NIM)

```
NIM = Net Interest Income (Item 3) / Average Earning Assets (HC-K Item 7)

Typical ranges:
- Regional banks: 3.0% - 4.0%
- Large diversified banks: 2.0% - 3.0%
- Trading-focused banks: 1.0% - 2.0%
```

### Efficiency Ratio

```
Efficiency = Noninterest Expense (Item 7) / (NII + Noninterest Income)
           = Item 7 / (Item 3 + Item 6)

Lower is better:
- Best-in-class: < 55%
- Average: 60-65%
- Weak: > 70%
```

### Return on Assets (ROA)

```
ROA = Net Income (Item 12) / Average Total Assets (HC-K Item 9)

Typical targets: 1.0% - 1.3%
```

### Return on Equity (ROE)

```
ROE = Net Income (Item 12) / Average Total Equity (HC-K Item 15)

Typical targets: 10% - 15%
```

### Pre-Provision Net Revenue (PPNR)

```
PPNR = NII + Noninterest Income - Noninterest Expense
     = Item 3 + Item 6 - Item 7

Key stress test metric - measures earnings power before credit costs
```

---

## Trading Revenue Detail (HI-M)

Schedule HI Memoranda provides trading revenue breakdown:

| Product | MDRM | Description |
|---------|------|-------------|
| Interest rate | BHCKA221 | IR trading gains/losses |
| Foreign exchange | BHCKA222 | FX trading gains/losses |
| Equity | BHCKA223 | Equity trading gains/losses |
| Commodity | BHCKA224 | Commodity trading gains/losses |
| Credit | BHCKHT79 | Credit trading gains/losses |

**Ties To**: Item 6.b total trading revenue

---

## Year-to-Date Considerations

Schedule HI reports cumulative year-to-date figures:

```
Q1: January - March
Q2: January - June
Q3: January - September
Q4: January - December (full year)

Quarterly amounts = Current YTD - Prior YTD
Example: Q2 NII = June YTD NII - March YTD NII
```

---

## Reconciliation to Other Schedules

### To Balance Sheet (HC)

```
Net Income flows to Retained Earnings:
HC Item 26 (Retained Earnings) change ≈
  HI Item 12 (Net Income) - Dividends Declared
```

### To Capital (HC-R)

```
Net Income supports CET1 through retained earnings
```

### To Averages (HC-K)

```
Yield calculations use:
- HI interest income items / HC-K average earning asset items
- HI interest expense items / HC-K average IB liability items
```

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCT4107 | Interest income |
| 1.a | BHCK4010 | Interest on loans |
| 2 | BHCT4073 | Interest expense |
| 2.a | BHCK4170 | Interest on deposits |
| **3** | **BHCT4074** | **Net interest income** |
| 4 | BHCT4230 | Provision for loan losses |
| 5 | BHCT4433 | NII after provision |
| 6 | BHCT4079 | Noninterest income |
| 6.b | BHCKA220 | Trading revenue |
| 7 | BHCT4093 | Noninterest expense |
| 7.a | BHCK4135 | Salaries and benefits |
| 8 | BHCT4301 | Pre-tax income |
| 9 | BHCT4302 | Income tax expense |
| **12** | **BHCT4340** | **Net income** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
