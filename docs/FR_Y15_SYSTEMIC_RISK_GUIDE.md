# FR Y-15 - Systemic Risk Report Guide

## Overview

The FR Y-15 (Banking Organization Systemic Risk Report) collects systemic risk data used to:
- Identify Global Systemically Important Banks (G-SIBs)
- Calculate G-SIB capital surcharges
- Monitor systemic risk indicators across the financial system

## Filing Requirements

**Who Files:**
- U.S. bank holding companies (BHCs) with consolidated total assets >= $100 billion
- U.S. intermediate holding companies (IHCs) of foreign banking organizations with U.S. assets >= $100 billion
- Any U.S.-based organization designated as a G-SIB

**Frequency:** Quarterly (as of 2018; previously annual)

**OMB Control Number:** 7100-0352

## G-SIB Indicator Categories

The FR Y-15 measures five categories of systemic importance:

| Category | Weight | Key Metrics |
|----------|--------|-------------|
| Size | 20% | Total Exposures |
| Interconnectedness | 20% | Intra-financial assets/liabilities |
| Substitutability | 20% | Payment activity, custody assets, underwriting |
| Complexity | 20% | Derivatives, Level 3 assets, trading/AFS |
| Cross-jurisdictional Activity | 20% | Cross-border claims/liabilities |

## Key Schedules

| Schedule | Description |
|----------|-------------|
| Schedule A | Size Indicator |
| Schedule B | Interconnectedness Indicators |
| Schedule C | Substitutability Indicators |
| Schedule D | Complexity Indicators |
| Schedule E | Cross-Jurisdictional Activity |
| Schedule F | Ancillary Indicators |
| Schedule G | Short-Term Wholesale Funding (Method 2) |

## G-SIB Surcharge Calculation

### Method 1 (Basel Committee)
Based on equally-weighted indicator scores across 5 categories

### Method 2 (U.S. Enhanced)
Replaces substitutability with short-term wholesale funding:
- Weighted short-term wholesale funding
- Average risk-weighted assets

**Current U.S. G-SIBs (2024):**
| Bank | RSSD ID | Method 2 Surcharge |
|------|---------|-------------------|
| JPMorgan Chase | 1039502 | 4.5% |
| Bank of America | 1073757 | 3.0% |
| Citigroup | 1951350 | 3.0% |
| Goldman Sachs | 2380443 | 3.0% |
| Morgan Stanley | 2162966 | 3.0% |
| Wells Fargo | 1120754 | 2.0% |
| BNY Mellon | 3587146 | 1.5% |
| State Street | 1111435 | 1.0% |

## Relationship to Other Forms

- **FR Y-9C:** Many items pulled directly from Y-9C schedules
- **FFIEC 101:** Total exposure measure aligns with SLR denominator
- **Basel GSIB Assessment:** U.S. indicators submitted to BIS

## Data Sources

- **Instructions:** [FR Y-15 Instructions](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-15)
- **Data Dictionary:** `csv/FR_Y15_SYSTEMIC_RISK.csv`
- **FR Y-15 Snapshots:** [FFIEC FR Y-15 Data](https://www.ffiec.gov/npw/FinancialReport/FRY15Reports)

## Notes

- Data used in annual G-SIB surcharge calculations
- December 31 filing is critical for surcharge determination
- Method 2 surcharge typically higher for U.S. G-SIBs due to STWF
