# Schedule HC-G: Other Liabilities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-G - Other Liabilities
**Frequency**: Quarterly
**Purpose**: Detail other liabilities not reported elsewhere on the balance sheet

---

## Overview

Schedule HC-G provides the breakdown of liabilities that flow into Schedule HC Item 20 (Other Liabilities). This includes accrued interest, accrued expenses, deferred taxes, and reserves for off-balance sheet exposures.

### Relationship to Schedule HC

```
Schedule HC-G Item 6 (Total) = Schedule HC Item 20 (Other Liabilities)
```

---

## Schedule Structure

```
OTHER LIABILITIES
├── Item 1: Interest accrued and unpaid on deposits
│   ├── 1.a: Domestic offices
│   └── 1.b: Foreign offices
├── Item 2: Other expenses accrued and unpaid
├── Item 3: Net deferred tax liabilities
├── Item 4: Allowance for credit losses on off-balance sheet exposures
├── Item 5: All other liabilities
└── Item 6: TOTAL OTHER LIABILITIES (= HC Item 20)
```

---

## Detailed Line Items

### Item 1: Interest Accrued and Unpaid on Deposits

| Sub-Item | MDRM | Call MDRM | Description |
|----------|------|-----------|-------------|
| 1 (Total) | - | - | Sum of 1.a and 1.b |
| 1.a | BHCK4172 | RCON3645 | Domestic office deposits |
| 1.b | BHCKB557 | RCFNB557 | Foreign office deposits |

**Nature**: Interest expense incurred but not yet paid to depositors

### Item 2: Other Expenses Accrued and Unpaid

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCTB558 | RCFDB558 | Accrued expenses payable |

**Components**:
- Accrued salaries and benefits
- Accrued taxes (other than income)
- Accrued professional fees
- Other accrued operating expenses

### Item 3: Net Deferred Tax Liabilities

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCK3049 | RCFD3049 | Net deferred tax liabilities |

**Nature**: Tax liabilities arising from taxable temporary differences (when book income exceeds taxable income temporarily)

**Note**: Only reported if net DTL position; net DTA reported in HC-F

### Item 4: Allowance for Credit Losses on Off-Balance Sheet Exposures

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCKB559 | RCFDB559 | ACL for unfunded commitments |

**Applicable To**:
- Unfunded loan commitments
- Letters of credit
- Financial guarantees
- Other off-balance sheet credit exposures

**CECL Impact**: Under ASC 326, this reserve reflects lifetime expected credit losses on these commitments

### Item 5: All Other Liabilities

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCTB560 | RCFDB560 | Residual other liabilities |

**May Include**:
- Accounts payable
- Operating lease liabilities (ASC 842)
- Deferred compensation
- Dividends declared but not paid
- Derivatives not reported elsewhere
- Miscellaneous liabilities

### Item 6: Total Other Liabilities

| MDRM | Call MDRM | Description | Ties To |
|------|-----------|-------------|---------|
| BHCK2750 | RCFD2930 | Total other liabilities | HC Item 20 |

**Reconciliation**:
```
Item 6 = Items 1 + 2 + 3 + 4 + 5
Schedule HC Item 20 = HC-G Item 6
```

---

## Memoranda Items (2022+)

| Item | MDRM | Description |
|------|------|-------------|
| M1 | BHCKJF88 | Accounts payable |
| M2 | BHCKHW60 | Operating lease liabilities |
| M3 | BHCKJF89 | Deferred compensation liabilities |
| M4 | BHCKJF90 | Dividends declared but not yet payable |

---

## Key Considerations

### CECL Impact on Item 4

Under Current Expected Credit Loss (CECL) accounting:
- Reserve reflects lifetime expected losses
- Applies to off-balance sheet credit exposures
- Typically larger than pre-CECL reserves
- Significant for banks with large unfunded commitment portfolios

### Operating Lease Liabilities

Under ASC 842 (effective 2019):
- Operating leases now on balance sheet
- Lease liability in Item 5 (or M2)
- Corresponding right-of-use asset in HC-F

### Relationship to Capital

Items in HC-G generally do not receive special capital treatment, but:
- ACL for OBS (Item 4) supports credit quality of commitments
- May be considered in stress testing

---

## Reconciliation Hierarchy

```
SCHEDULE HC-G                           SCHEDULE HC
═══════════════════════════════════════════════════════════════════════

Item 6 (Total)                 ────────► HC Item 20 (Other Liabilities)
BHCK2750                                 BHCK2750
```

---

## Key Analytical Metrics

### Accrued Interest Ratio
```
Accrued Interest % = Item 1 / Total Deposits
- Higher ratio may indicate higher-rate deposit mix
```

### OBS Reserve Adequacy
```
OBS ACL Ratio = Item 4 / Total Unfunded Commitments (from HC-L)
- Should be compared to historical loss experience on commitments
```

### Other Liabilities to Assets
```
Other Liab % = Item 6 / Total Assets
- Typically 1-3% of assets
```

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1.a | BHCK4172 | Accrued interest - domestic deposits |
| 1.b | BHCKB557 | Accrued interest - foreign deposits |
| 2 | BHCTB558 | Other accrued expenses |
| 3 | BHCK3049 | Net deferred tax liabilities |
| 4 | BHCKB559 | ACL for off-balance sheet |
| 5 | BHCTB560 | All other liabilities |
| **6** | **BHCK2750** | **TOTAL OTHER LIABILITIES** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
