# FR Y-14 Capital Assessments and Stress Testing Guide

## Overview

The FR Y-14 is the Federal Reserve's primary data collection for stress testing and capital planning under CCAR (Comprehensive Capital Analysis and Review) and DFAST (Dodd-Frank Act Stress Testing). It has three components:

- **Y-14A (Annual)**: Forward-looking 9-quarter projections under stress scenarios
- **Y-14Q (Quarterly)**: Current positions, risk metrics, and financial data
- **Y-14M (Monthly)**: Loan-level portfolio data

## Reporters

Bank Holding Companies (BHCs), Intermediate Holding Companies (IHCs), and covered Savings and Loan Holding Companies (SLHCs) with $100 billion or more in total consolidated assets.

## Y-14A Annual Schedules

### A.1 - Income Statement Projections
Projects income statement items over 9 quarters under baseline and stress scenarios:
- Net Interest Income (cross-ref: HI, BHCT4074)
- Trading Revenue (cross-ref: HI, BHCKA220)
- Provision for Credit Losses (cross-ref: HI, BHCT4230)
- Net Income (cross-ref: HI, BHCT4340)

### A.2 - Balance Sheet Projections
Projects balance sheet under stress:
- Total Assets (cross-ref: HC, BHCT2170)
- Loans by type (cross-ref: HC-C)
- Securities (cross-ref: HC-B)
- Trading Assets (cross-ref: HC-D, BHCT3545)

### A.3 - Capital Projections
Projected capital ratios - the core output of stress testing:
- CET1 Ratio (cross-ref: HC-R, BHCAP859 / BHCAA223)
- Tier 1 Ratio
- Total Capital Ratio
- Leverage Ratio

### A.4 - RWA Projections
Risk-weighted assets by category under stress.

### A.5 - Operational Risk
Operational loss projections including scenario analysis.

### F.2 - Counterparty Default
Impact of the default of the firm's largest counterparty.

## Y-14Q Quarterly Schedules

### Schedule B - Securities Risk
CUSIP-level data on the securities portfolio, enabling position-level stress loss estimation. Links to HC-B.

### Schedule E - Counterparty Credit Risk
- **E.1**: Top 20 counterparty exposures by EAD (links to HC-L)
- **E.2**: CVA and wrong-way risk detail (links to Pillar 3 CCR2)

### Schedule G - Trading Risk (Volcker-Critical)
- **G.1**: Global trading revenue by desk and product. Primary source for trading P&L attribution.
- **G.2**: VaR and stressed VaR by risk factor. Links to FFIEC 102 and Pillar 3 MR3.

### Schedule H - PPNR
Pre-Provision Net Revenue: detailed revenue and expense components for stress projections. Links to HI.

## Y-14M Monthly Schedules

Loan-level data for credit-sensitive portfolios:
1. First Lien Residential Mortgage (FICO, LTV, delinquency)
2. Home Equity (HELOC/HEL draw rates, utilization)
3. Credit Card (balances, limits, payment behavior)
4. Auto Loans (vintage, LTV, performance)

## Cross-Form Relationships

| Y-14 Schedule | FR Y-9C | Call Report | FFIEC 102 | Pillar 3 |
|---------------|---------|-------------|-----------|----------|
| A.1 Income | HI | RI | - | - |
| A.2 Balance Sheet | HC | RC | - | KM1 |
| A.3 Capital | HC-R | RC-R | - | KM1 |
| B Securities | HC-B | RC-B | - | - |
| E Counterparty | HC-L | RC-L | - | CCR1-CCR8 |
| G.1 Trading Revenue | HI | RI | - | MR1 |
| G.2 VaR | - | - | VaR/sVaR | MR3, MR4 |
| H PPNR | HI | RI | - | - |

## Key Use Cases

1. **Stress Testing**: Primary input for Fed's annual stress test results
2. **Capital Planning**: Firms project minimum capital ratios under stress
3. **Trading Risk Analysis**: G.1/G.2 provide granular trading revenue and risk data
4. **Counterparty Risk**: E.1/E.2 reveal concentrated counterparty exposures
5. **Credit Portfolio Analysis**: Y-14M provides loan-level data unavailable elsewhere

## Data Availability

Y-14 data is **confidential** - only aggregate stress test results are published. The instructions and form templates are public and available in the Knowledge Base.

## Repository Files

- `csv/FR_Y14A_SCHEDULES.csv` - Y-14A schedule items
- `csv/FR_Y14Q_SCHEDULES.csv` - Y-14Q schedule items
- `csv/Y14_SCHEDULE_MAP.csv` - Schedule reference mapping

---

*Part of the Bank Regulatory Data Dictionary*
