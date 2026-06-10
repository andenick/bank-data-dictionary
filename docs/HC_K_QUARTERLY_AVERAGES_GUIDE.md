# Schedule HC-K: Quarterly Averages Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-K - Quarterly Averages
**Frequency**: Quarterly
**Purpose**: Report average balances for key assets, liabilities, and equity

---

## Overview

Schedule HC-K provides quarterly average balances for earning assets, interest-bearing liabilities, and equity. These averages are essential for calculating meaningful yields, costs, and profitability ratios.

### Why Averages Matter

- **Point-in-time vs. Average**: Balance sheet shows end-of-period; averages smooth fluctuations
- **Yield Calculations**: Interest income / Average earning assets = Yield on assets
- **Cost Calculations**: Interest expense / Average IB liabilities = Cost of funds
- **NIM**: Net interest income / Average earning assets = Net interest margin

---

## Schedule Structure

```
AVERAGE ASSETS
├── Item 1: Interest-bearing balances
├── Item 2: Securities (AFS + HTM)
│   ├── 2.a: AFS securities
│   └── 2.b: HTM securities
├── Item 3: Fed funds sold and reverse repos
├── Item 4: Loans and leases
│   ├── 4.a: Total loans
│   └── 4.b: Lease financing receivables
├── Item 5: Trading assets
├── Item 6: Other earning assets
├── Item 7: Total earning assets
├── Item 8: Allowance for loan losses
└── Item 9: Total assets

AVERAGE LIABILITIES
├── Item 10: Interest-bearing deposits
│   ├── 10.a: Domestic offices
│   └── 10.b: Foreign offices
├── Item 11: Fed funds purchased and repos
├── Item 12: Other borrowed money
├── Item 13: Total interest-bearing liabilities
└── Item 14: Total liabilities

AVERAGE EQUITY
└── Item 15: Total equity capital

MEMORANDA
├── M1: Net interest-bearing funds
├── M2: Noninterest-bearing deposits
└── M3: Total deposits
```

---

## Key Items and MDRM Codes

### Average Assets

| Item | MDRM | Description | Ties To |
|------|------|-------------|---------|
| 1 | BHCK3381 | Interest-bearing balances | HC Item 1.b |
| 2 | BHCK3365 | Securities (excl. trading) | HC Item 2 |
| 4 | BHCK3516 | Loans and leases | HC Item 4 |
| 5 | BHCK3401 | Trading assets | HC Item 5 |
| 7 | BHCKA517 | Total earning assets | Calculated |
| 9 | BHCK3368 | Total assets | HC Item 12 |

### Average Liabilities

| Item | MDRM | Description | Ties To |
|------|------|-------------|---------|
| 10 | BHCK3387 | Interest-bearing deposits | HC Item 13 |
| 11 | BHCK3353 | Fed funds purchased/repos | HC Item 14 |
| 12 | BHCK2635 | Other borrowed money | HC Item 16 |
| 13 | BHCKA518 | Total IB liabilities | Calculated |
| 14 | BHCK3548 | Total liabilities | HC Item 21 |

### Average Equity

| Item | MDRM | Description | Ties To |
|------|------|-------------|---------|
| 15 | BHCK3519 | Total equity capital | HC Item 28 |

---

## Key Profitability Ratios Using HC-K

### Net Interest Margin (NIM)

```
NIM = Net Interest Income (HI Item 3) / Average Earning Assets (HC-K Item 7)

Example:
  NII = $2.5 billion
  Avg Earning Assets = $100 billion
  NIM = 2.5%
```

### Yield on Earning Assets

```
Yield = Total Interest Income (HI Item 1) / Average Earning Assets (HC-K Item 7)
```

### Cost of Funds

```
Cost = Total Interest Expense (HI Item 2) / Average IB Liabilities (HC-K Item 13)
```

### Return on Average Assets (ROAA)

```
ROAA = Net Income (HI Item 12) / Average Total Assets (HC-K Item 9)
```

### Return on Average Equity (ROAE)

```
ROAE = Net Income (HI Item 12) / Average Total Equity (HC-K Item 15)
```

### Efficiency Ratio

```
Efficiency = Noninterest Expense (HI Item 7) / (NII + Noninterest Income)
```

---

## Validation Checks

### Balance Sheet Consistency

Average balances should be reasonably close to:
```
(Beginning Balance + Ending Balance) / 2
```

Large deviations may indicate:
- Significant intra-period transactions
- Acquisitions/divestitures
- Reclassifications

### Asset = Liability + Equity (Averages)

```
Average Total Assets ≈ Average Total Liabilities + Average Total Equity
HC-K Item 9 ≈ HC-K Item 14 + HC-K Item 15
```

---

## Analytical Applications

### Trend Analysis

```
Period-over-period change in:
- Average earning asset mix
- Average deposit mix
- Funding structure

Rising average trading assets → More trading activity
Rising average deposits / falling average borrowings → Improved funding
```

### Peer Comparison

Using averages enables meaningful peer comparison:
- Normalizes for different period-end dates
- Smooths seasonal fluctuations
- Better represents typical operating position

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCK3381 | Avg interest-bearing balances |
| 2 | BHCK3365 | Avg securities |
| 4 | BHCK3516 | Avg loans and leases |
| 5 | BHCK3401 | Avg trading assets |
| **7** | **BHCKA517** | **Avg earning assets** |
| 8 | BHCK3368 | Avg ALLL |
| **9** | **BHCK3368** | **Avg total assets** |
| 10 | BHCK3387 | Avg IB deposits |
| **13** | **BHCKA518** | **Avg IB liabilities** |
| **15** | **BHCK3519** | **Avg total equity** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
