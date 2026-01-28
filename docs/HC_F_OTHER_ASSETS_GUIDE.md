# Schedule HC-F: Other Assets Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-F - Other Assets
**Frequency**: Quarterly
**Purpose**: Detail other assets not reported elsewhere on the balance sheet

---

## Overview

Schedule HC-F provides the breakdown of assets that flow into Schedule HC Item 11 (Other Assets). Many items in this schedule also appear as separate line items on Schedule HC (Items 6-10).

### Relationship to Schedule HC

| HC-F Item | HC Item | Description |
|-----------|---------|-------------|
| 6 | 6 | Premises and fixed assets |
| 7 | 7 | Other real estate owned |
| 8 | 8 | Investments in unconsolidated subs |
| 9 | 9 | Direct/indirect RE investments |
| 10.a | 10.a | Goodwill |
| 10.b | 10.b | Other intangible assets |
| 12 | 11 | Total other assets |

---

## Schedule Structure

```
OTHER ASSETS
├── Item 1: Accrued interest receivable
├── Item 2: Net deferred tax assets
├── Item 3: Interest-only strips (non-mortgage)
├── Item 4: Equity investments without determinable FV
├── Item 5: Bank-owned life insurance (BOLI)
├── Item 6: Premises and fixed assets (= HC Item 6)
├── Item 7: Other real estate owned (= HC Item 7)
├── Item 8: Investments in unconsolidated subs (= HC Item 8)
├── Item 9: RE venture investments (= HC Item 9)
├── Item 10: Intangible assets
│   ├── 10.a: Goodwill (= HC Item 10.a)
│   └── 10.b: Other intangibles (= HC Item 10.b)
├── Item 11: All other assets
└── Item 12: TOTAL OTHER ASSETS (= HC Item 11)
```

---

## Detailed Line Items

### Item 1: Accrued Interest Receivable

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCTB556 | RCFDB556 | Interest earned but not collected |

**Components**:
- Interest accrued on loans
- Interest accrued on securities
- Interest accrued on other earning assets

### Item 2: Net Deferred Tax Assets

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCT2148 | RCFD2148 | Net deferred tax assets |

**Nature**: Represents future tax benefits from:
- Deductible temporary differences
- Tax loss carryforwards
- Tax credit carryforwards

**Regulatory Significance**: Subject to deduction from CET1 capital if exceeds threshold

### Item 3: Interest-Only Strips (Non-Mortgage)

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCKC976 | RCFDC976 | IO strips from non-mortgage securitizations |

**Note**: Mortgage-related IO strips reported elsewhere

### Item 4: Equity Investments Without Readily Determinable Fair Value

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCK1752 | RCFD1752 | Equity securities at cost |

**Includes**:
- FHLB stock (required holding)
- Federal Reserve Bank stock
- Bankers' bank stock
- Community development investments
- Other equity without quoted prices

**Accounting**: Measured at cost less impairment, plus/minus observable price changes (ASU 2016-01)

### Item 5: Bank-Owned Life Insurance (BOLI)

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCK4659 | RCFD4659 | Cash surrender value of BOLI |

**Nature**: Life insurance policies owned by the bank on lives of key employees

**Accounting**: Carried at cash surrender value; income tax-advantaged

### Items 6-9: Cross-Referenced to HC

These items appear as separate line items on Schedule HC:

| Item | MDRM | HC Item | Description |
|------|------|---------|-------------|
| 6 | BHCT2145 | HC Item 6 | Premises and fixed assets |
| 7 | BHCT2150 | HC Item 7 | Other real estate owned (OREO) |
| 8 | BHCT2130 | HC Item 8 | Investments in unconsolidated subs |
| 9 | BHCK5372 | HC Item 9 | Direct/indirect RE investments |

### Item 10: Intangible Assets

#### Item 10.a: Goodwill

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCT3163 | RCFD3163 | Goodwill |

**Nature**: Excess of purchase price over fair value of net assets in acquisitions

**Regulatory**: Deducted from CET1 capital

#### Item 10.b: Other Intangible Assets

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCTC752 | RCFDC752 | Other intangible assets |

**Components**:
- Mortgage servicing assets (MSAs)
- Core deposit intangibles
- Credit card relationships
- Customer lists
- Non-compete agreements

**Regulatory**: Generally deducted from CET1 capital (except MSAs up to threshold)

### Item 11: All Other Assets

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCTB557 | RCFDB557 | Residual other assets |

**May Include**:
- Prepaid expenses
- Accounts receivable
- Derivatives not reported elsewhere
- Miscellaneous assets

### Item 12: Total Other Assets

| MDRM | Call MDRM | Description | Ties To |
|------|-----------|-------------|---------|
| BHCT2160 | RCFD2160 | Total other assets | HC Item 11 |

**Reconciliation**:
```
Item 12 = Sum(Items 1-11)
Schedule HC Item 11 = HC-F Item 12
```

---

## Memoranda Items

### Mortgage Servicing Assets (MSAs)

| Item | MDRM | Description |
|------|------|-------------|
| M1 | BHCK1651 | MSAs from mortgages purchased |
| M2 | BHCK1652 | MSAs from mortgages sold with servicing retained |
| M3 | BHCKB027 | Total MSAs |

**Relationship**: Total MSAs (M3) is a component of Item 10.b

### Other Memoranda (2022+)

| Item | MDRM | Description |
|------|------|-------------|
| M4 | BHCKJF85 | Prepaid expenses |
| M5 | BHCKJF86 | Accounts receivable |
| M6 | BHCKJF87 | Servicing assets (non-mortgage) |

---

## Regulatory Capital Treatment

### Items Deducted from CET1

| Item | Treatment |
|------|-----------|
| Goodwill (10.a) | Full deduction from CET1 |
| Other intangibles (10.b) | Generally deducted |
| MSAs (portion of 10.b) | Subject to 10%/15% threshold tests |
| Net DTA (Item 2) | Subject to 10%/15% threshold tests |

### Threshold Test Items

Under Basel III, certain assets are subject to threshold deductions:
- MSAs
- Net DTAs arising from temporary differences
- Significant investments in unconsolidated FIs

If individually >10% of CET1 or collectively >15% of CET1, excess is deducted.

---

## Reconciliation Hierarchy

```
SCHEDULE HC-F                           SCHEDULE HC
═══════════════════════════════════════════════════════════════════════

Item 6 (Premises)              ────────► HC Item 6
BHCT2145                                 BHCT2145

Item 7 (OREO)                  ────────► HC Item 7
BHCT2150                                 BHCT2150

Item 8 (Unconsolidated subs)   ────────► HC Item 8
BHCT2130                                 BHCT2130

Item 9 (RE investments)        ────────► HC Item 9
BHCK5372                                 BHCK5372

Item 10.a (Goodwill)           ────────► HC Item 10.a
BHCT3163                                 BHCT3163

Item 10.b (Other intangibles)  ────────► HC Item 10.b
BHCTC752                                 BHCTC752

Item 12 (Total)                ────────► HC Item 11
BHCT2160                                 BHCT2160
```

---

## Key Analytical Metrics

### Intangible Asset Ratio
```
Intangible Ratio = (Item 10.a + Item 10.b) / Total Equity
- Higher ratio = more acquisition-driven growth
- Regulatory concern if intangibles large relative to capital
```

### BOLI as % of Tier 1
```
BOLI Ratio = Item 5 / Tier 1 Capital
- OCC guidance suggests cap at 25% of Tier 1
```

### OREO Ratio
```
OREO Ratio = Item 7 / Total Loans
- Higher ratio indicates asset quality issues
- Elevated during credit stress
```

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCTB556 | Accrued interest receivable |
| 2 | BHCT2148 | Net deferred tax assets |
| 3 | BHCKC976 | IO strips (non-mortgage) |
| 4 | BHCK1752 | Equity without determinable FV |
| 5 | BHCK4659 | BOLI |
| 6 | BHCT2145 | Premises and fixed assets |
| 7 | BHCT2150 | OREO |
| 8 | BHCT2130 | Unconsolidated sub investments |
| 9 | BHCK5372 | RE venture investments |
| 10.a | BHCT3163 | Goodwill |
| 10.b | BHCTC752 | Other intangibles |
| 11 | BHCTB557 | All other assets |
| **12** | **BHCT2160** | **TOTAL OTHER ASSETS** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
