# FR Y-9LP - Parent Company Only Financial Statements Guide

## Overview

The FR Y-9LP (Parent Company Only Financial Statements for Large Holding Companies) collects the unconsolidated balance sheet, income statement, and detailed supporting schedules from the parent holding company.

## Filing Requirements

**Who Files:**
- Bank holding companies (BHCs) with consolidated total assets >= $3 billion
- Savings and loan holding companies (SLHCs) with consolidated total assets >= $3 billion

**Frequency:** Quarterly

**OMB Control Number:** 7100-0244

## Key Schedules

| Schedule | Description |
|----------|-------------|
| Schedule PC | Parent Company Only Balance Sheet |
| Schedule PC-A | Cash and Balances Due |
| Schedule PC-B | Securities and Investments |
| Schedule PI | Parent Company Only Income Statement |
| Schedule PI-A | Interest Income/Expense Detail |

## Key MDRM Codes

| Mnemonic | Item Code | Description |
|----------|-----------|-------------|
| BHCP | 2170 | Total Assets |
| BHCP | 2948 | Total Liabilities |
| BHCP | 3210 | Total Equity Capital |
| BHCP | 4340 | Net Income |
| BHCP | 3283 | Common Stock |
| BHCP | 3230 | Surplus |

## Parent vs Consolidated Comparison

| Aspect | FR Y-9LP (Parent) | FR Y-9C (Consolidated) |
|--------|-------------------|----------------------|
| Scope | Parent company only | Parent + all subsidiaries |
| Subsidiaries | Investment method | Full consolidation |
| Intercompany | Not eliminated | Eliminated |
| Use Case | Liquidity analysis | Capital adequacy |

## Double Leverage Analysis

The FR Y-9LP enables calculation of double leverage:

```
Double Leverage Ratio = Equity Investment in Subsidiaries / Parent Equity Capital
```

A ratio > 100% indicates the parent is financing subsidiary equity with debt.

## Relationship to Other Forms

- **FR Y-9C:** Consolidated counterpart; parent + subsidiary data
- **FR Y-9SP:** Simplified version for smaller holding companies
- **FR Y-6:** Annual report supplement with ownership details

## Data Sources

- **Instructions:** [FR Y-9LP Instructions](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-9LP)
- **Data Dictionary:** `csv/FR_Y9LP_PARENT_ONLY.csv`
- **Bulk Data:** [FFIEC Financial Data Download](https://www.ffiec.gov/npw/FinancialReport/FinancialDataDownload)

## Notes

- Critical for analyzing holding company liquidity
- Parent-only data not publicly disclosed for most items
- Used in stress testing to assess funding vulnerabilities
