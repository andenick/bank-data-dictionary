# FR 2052a Complex Institution Liquidity Monitoring Report Guide

## Overview

The FR 2052a collects granular liquidity data from the largest financial institutions, serving as the primary input for calculating the Liquidity Coverage Ratio (LCR) and Net Stable Funding Ratio (NSFR).

## Reporters

- Large BHCs, IHCs, and covered SLHCs
- Daily reporting for G-SIBs, monthly for others

## Structure

Unlike schedule-based regulatory forms, the FR 2052a uses a **product-based hierarchy** organized by cash flow direction:

### Inflows
Cash expected to come in over various time horizons:
- **Secured Lending**: Reverse repo, securities borrowing, margin lending
- **Unsecured Lending**: Fed funds sold, interbank loans
- **Asset Maturities**: Securities, loan repayments
- **Derivatives**: Net derivative cash inflows, collateral returns

### Outflows
Cash expected to go out:
- **Secured Funding**: Repo, securities lending (run-off by collateral quality)
- **Unsecured Wholesale**: Operational deposits (25% run-off), non-operational FI deposits (100%), CP, MTN
- **Retail Funding**: Stable deposits (3% run-off), less stable (10%), brokered
- **Derivatives**: Margin calls, rating triggers (2-notch downgrade scenario)
- **Commitments**: Credit facilities (5-40% draw), liquidity facilities (100% draw)
- **Operational**: Payroll, debt service, dividends

### Supplemental
- **HQLA**: Level 1 (reserves, UST - no haircut), Level 2A (agency MBS - 15% haircut), Level 2B (IG corporate - 50% haircut)
- **Collateral**: Pledged, received, and rehypothecated collateral
- **Balance Sheet Items**: Selected items for NSFR calculation

## LCR Calculation

```
LCR = HQLA / Net Cash Outflows (30-day stress) >= 100%

Where:
  HQLA = Level 1 + (Level 2A x 0.85) + (Level 2B x 0.50)
  Net Outflows = Total Outflows - min(Inflows, 0.75 x Outflows)
```

## NSFR Calculation

```
NSFR = Available Stable Funding / Required Stable Funding >= 100%

Where:
  ASF = Sum(Liability x ASF_Factor) for all funding sources
  RSF = Sum(Asset x RSF_Factor) for all assets
```

## Maturity Buckets

| Bucket | LCR | NSFR |
|--------|-----|------|
| Overnight | Yes | Yes |
| 2-7 days | Yes | Yes |
| 8-30 days | Yes | Yes |
| 31-90 days | No | Yes |
| 91-180 days | No | Yes |
| 181-365 days | No | Yes |
| > 1 year | No | Yes |

## Cross-Form Relationships

| FR 2052a | FR Y-9C | Call Report | FR Y-15 | Pillar 3 |
|----------|---------|-------------|---------|----------|
| HQLA L1 | HC-B (UST) | RC-B | Sched D | LIQ1 |
| HQLA L2A | HC-B (Agency MBS) | RC-B | Sched D | LIQ1 |
| Repo/Rev Repo | HC, HC-L | RC, RC-L | Sched G | LIQ1 |
| Deposits | - | RC-E | Sched G | LIQ1 |
| Derivatives | HC-L | RC-L | Sched D | LIQ1 |
| Commitments | HC-L | RC-L | - | LIQ1 |
| LCR | - | - | - | LIQ1 |
| NSFR | - | - | - | LIQ2 |
| STWF | - | - | Sched G | - |

## Key Analytical Uses

1. **LCR Compliance Monitoring**: Track HQLA buffer and net outflow projections
2. **Funding Risk Assessment**: Identify concentrated or vulnerable funding sources
3. **Stress Testing**: Liquidity impact under various stress scenarios
4. **G-SIB Assessment**: STWF component feeds FR Y-15 Method 2 score
5. **NSFR Analysis**: Structural funding stability assessment

## Repository Files

- `csv/FR_2052a_PRODUCT_HIERARCHY.csv` - Product hierarchy with LCR/NSFR treatment

---

*Part of the Bank Regulatory Data Dictionary*
