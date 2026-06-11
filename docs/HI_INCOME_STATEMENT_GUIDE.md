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

NONINTEREST INCOME (Item 5)
├── 5.a: Fiduciary activities
├── 5.b: Service charges on deposits
├── 5.c: Trading revenue
├── 5.d: Securities/IB/insurance fees (5.d.1-7)
├── 5.e: Venture capital revenue
├── 5.f: Net servicing fees
├── 5.g: Net securitization income
├── 5.i-5.k: Net gains on sales of loans/OREO/other assets
└── 5.l: Other noninterest income
(5.m = total)

REALIZED SECURITIES GAINS (Item 6.a HTM, 6.b AFS)

NONINTEREST EXPENSE (Item 7)
├── 7.a: Salaries and benefits
├── 7.b: Premises and fixed assets
├── 7.c: Goodwill impairment (7.c.1) + intangible amortization (7.c.2)
└── 7.d: Other noninterest expense
(7.e = total)

INCOME BEFORE TAXES (Item 8.c)
= Items 3 + 5.m + 6.a + 6.b - 4 - 7.e (+ equity-securities gains 8.b)

INCOME TAX EXPENSE (Item 9)

INCOME BEFORE DISCONTINUED OPS (Item 10)
= Item 8 - Item 9

DISCONTINUED OPERATIONS (Item 11, net of tax)

NET INCOME incl. minority (Item 12) = Item 10 + Item 11
LESS minority interest (Item 13)
NET INCOME attributable to HC (Item 14) = Item 12 - Item 13
```

---

## Detailed Line Items

### Item 1: Interest Income

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 1.a.(1)(a) | BHCK4435 | RIAD4435 | Interest/fees on loans secured by 1-4 family residential |
| 1.a.(1)(b) | BHCK4436 | RIAD4436 | All other loans secured by real estate |
| 1.a.(1)(c) | BHCKF821 | RIAD4058 | All other loans |
| 1.a.(2) | BHCK4059 | RIAD4059 | Loans in foreign offices/Edge/IBFs |
| 1.b | BHCK4065 | RIAD4065 | Income from lease financing receivables |
| 1.c | BHCK4115 | RIAD4115 | Interest on balances due from depository institutions |
| 1.d.(1) | BHCKB488 | RIADB488 | U.S. Treasury/agency (excl MBS) |
| 1.d.(2) | BHCKB489 | RIADB489 | MBS |
| 1.d.(3) | BHCK4060 | RIAD4060 | Other securities |
| 1.e | BHCK4069 | RIAD4069 | Trading assets |
| 1.f | BHCK4020 | RIAD4020 | Fed funds sold/reverse repos |
| 1.g | BHCK4518 | RIAD4518 | Other interest income |
| 1.h (Total) | BHCK4107 | RIAD4107 | Total interest income |

### Item 2: Interest Expense

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 2.a.(1)(a) | BHCKHK03 | RIADHK03 | Time deposits of $250,000 or less |
| 2.a.(1)(b) | BHCKHK04 | RIADHK04 | Time deposits of more than $250,000 |
| 2.a.(1)(c) | BHCK6761 | - | Other deposits |
| 2.a.(2) | BHCK4172 | RIAD4172 | Deposits in foreign offices/Edge/IBFs |
| 2.b | BHCK4180 | RIAD4180 | Fed funds purchased/repos |
| 2.c | BHCK4185 | RIAD4185 | Trading liabilities and other borrowed money |
| 2.d | BHCK4397 | RIAD4200 | Subordinated notes/debentures and mandatory convertibles |
| 2.e | BHCK4398 | - | Other interest expense |
| 2.f (Total) | BHCK4073 | RIAD4073 | Total interest expense |

### Item 3: Net Interest Income

| MDRM | Formula |
|------|---------|
| BHCK4074 | Item 1 - Item 2 |

**Key Metric**: Net Interest Margin (NIM) = Item 3 / Average Earning Assets (HC-K)

### Item 4: Provision for Credit Losses

| MDRM | Description |
|------|-------------|
| BHCKJJ33 | Provisions for credit losses on financial assets (CECL) |

**CECL Note**: Under CECL (effective 2019-03-31, code BHCKJJ33), this represents the change in lifetime expected credit loss reserves. The pre-CECL code BHCT4230 (provision for loan and lease losses) was discontinued 2018-12-31.

### Item 5: Noninterest Income

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 5.a | BHCK4070 | RIAD4070 | Income from fiduciary activities |
| 5.b | BHCK4483 | RIAD4483 | Service charges on deposit accounts (domestic) |
| 5.c | BHCKA220 | RIADA220 | Trading revenue |
| 5.d.(1) | BHCKC886 | RIADC886 | Fees/commissions from securities brokerage |
| 5.d.(2) | BHCKC888 | RIADC888 | Investment banking, advisory, underwriting fees |
| 5.d.(3) | BHCKC887 | RIADC887 | Fees/commissions from annuity sales |
| 5.d.(4) | BHCKC386 | RIADC386 | Insurance/reinsurance underwriting income |
| 5.d.(5) | BHCKC387 | RIADC387 | Income from other insurance activities |
| 5.e | BHCKB491 | RIADB491 | Venture capital revenue |
| 5.f | BHCKB492 | RIADB492 | Net servicing fees |
| 5.g | BHCKB493 | RIADB493 | Net securitization income |
| 5.i | BHCK8560 | RIAD5416 | Net gains (losses) on sales of loans and leases |
| 5.j | BHCK8561 | RIAD5415 | Net gains (losses) on sales of OREO |
| 5.k | BHCKB496 | RIADB496 | Net gains (losses) on sales of other assets |
| 5.l | BHCKB497 | RIADB497 | Other noninterest income |
| 5.m (Total) | BHCK4079 | RIAD4079 | Total noninterest income |

### Item 7: Noninterest Expense

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 7.a | BHCK4135 | RIAD4135 | Salaries and employee benefits |
| 7.b | BHCK4217 | RIAD4217 | Premises and fixed assets (net of rental income) |
| 7.c.(1) | BHCKC216 | RIADC216 | Goodwill impairment losses |
| 7.c.(2) | BHCKC232 | RIADC232 | Amortization/impairment of other intangibles |
| 7.d | BHCK4092 | RIAD4092 | Other noninterest expense |
| 7.e (Total) | BHCK4093 | RIAD4093 | Total noninterest expense |

OREO expense, FDIC assessment, data processing, etc. are reported in the memoranda (Schedule HI Memorandum item 7.a-7.p), not in items 7.a-7.d.

### Item 14: Net Income (attributable to holding company)

| Item | MDRM | Formula |
|------|------|---------|
| 12 | BHCKG104 | Net income incl. minority interests (items 10 + 11) |
| 13 | BHCKG103 | LESS: net income attributable to minority interests |
| 14 | BHCK4340 | Net income attributable to HC (item 12 - item 13) |

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

Schedule HI Memoranda item 9 provides the trading revenue breakdown:

| Product | MDRM | Description |
|---------|------|-------------|
| Interest rate | BHCK8757 | IR trading gains/losses |
| Foreign exchange | BHCK8758 | FX trading gains/losses |
| Equity | BHCK8759 | Equity security/index trading gains/losses |
| Commodity/other | BHCK8760 | Commodity and other trading gains/losses |
| Credit | BHCKF186 | Credit-exposure trading gains/losses |

**Ties To**: Item 5.c total trading revenue. (The earlier draft listing BHCKA221-A224 was incorrect — those are HC-R risk-weighted-asset codes.)

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
| 1.h | BHCK4107 | Total interest income |
| 2.f | BHCK4073 | Total interest expense |
| **3** | **BHCK4074** | **Net interest income** |
| 4 | BHCKJJ33 | Provision for credit losses (CECL) |
| 5.m | BHCK4079 | Total noninterest income |
| 5.c | BHCKA220 | Trading revenue |
| 7.e | BHCK4093 | Total noninterest expense |
| 7.a | BHCK4135 | Salaries and benefits |
| 8.c | BHCK4301 | Income before taxes |
| 9 | BHCK4302 | Income tax expense |
| 11 | BHCKFT28 | Discontinued operations, net of tax |
| **14** | **BHCK4340** | **Net income attributable to holding company** |

Note: The current FR Y-9C Schedule HI has no "NII after provision" subtotal line and no "extraordinary items" line (replaced by discontinued operations, item 11). Net income runs items 12 (incl. minority) → 13 (less minority) → 14 (attributable to HC).

---

*Last Updated: 2026-06-11 (v8 conceptual-accuracy sweep; codes verified against FRY9C_FIELDSPEC_202603 + MDRM + warehouse)*
*Reference: FR Y-9C Instructions (current form, March 2026 field spec)*
