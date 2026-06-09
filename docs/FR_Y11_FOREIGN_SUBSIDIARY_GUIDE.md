# FR Y-11 - Report on Assets and Liabilities of U.S. Nonbank Subsidiaries Guide

## Overview

The FR Y-11 collects financial data for individual U.S. nonbank subsidiaries of domestic holding companies, including:
- Balance sheet information
- Income statement data
- Off-balance sheet exposures
- Equity capital changes

## Filing Requirements

### FR Y-11 (Quarterly)
**Who Files:** Top-tier holding companies file for each nonbank subsidiary where:
- Total assets >= $1 billion, OR
- Total off-balance sheet activity >= $5 billion, OR
- Equity capital >= 5% of consolidated top-tier equity capital

### FR Y-11S (Annual)
**Who Files:** Subsidiaries with:
- Assets >= $250 million but < $500 million
- Not meeting quarterly filing thresholds

**OMB Control Number:** 7100-0244

> The legacy 7100-0073 cited in older materials is superseded for the FR Y-11; 7100-0073 now covers the FR Y-7N family (US nonbank subsidiaries of foreign banking organizations).

## Key Schedules

| Schedule | Description |
|----------|-------------|
| Schedule BS | Balance Sheet |
| Schedule BS-A | Loans and Lease Financing Receivables |
| Schedule BS-M | Memoranda (off-balance-sheet and other memoranda items) |
| Schedule IS | Income Statement (calendar year-to-date) |
| Schedule IS-A | Changes in Equity Capital |
| Schedule IS-B | Changes in Allowance for Credit Losses (retitled from "Allowance for Loan and Lease Losses" under CECL) |

## Covered Subsidiary Types

The FR Y-11 covers nonbank subsidiaries including:
- Broker-dealers
- Asset managers
- Insurance companies
- Finance companies
- Real estate subsidiaries
- Technology subsidiaries
- Special purpose vehicles

## Key MDRM Codes

| Mnemonic | Item Code | Description |
|----------|-----------|-------------|
| BHCS | 2170 | Total Assets |
| BHCS | 2948 | Total Liabilities |
| BHCS | 3210 | Total Equity Capital |
| BHCS | 4340 | Net Income (Loss) |
| BHCS | 1763 | Goodwill |
| BHCS | 1773 | Other Intangible Assets |

## Relationship to Consolidated Reporting

| Level | Report | Coverage |
|-------|--------|----------|
| Consolidated | FR Y-9C | All subsidiaries combined |
| Bank Subsidiary | Call Report | Individual bank data |
| Nonbank Subsidiary | FR Y-11 | Individual nonbank data |

## Analytical Uses

- **Legal Entity Analysis:** Individual subsidiary financial health
- **Resolution Planning:** Entity-level data for living wills
- **Intercompany Exposures:** Track upstream/downstream transactions
- **Operational Risk:** Identify concentrated nonbank activities

## Relationship to Other Forms

- **FR Y-9C:** Consolidated parent; Y-11 entities should reconcile
- **FR Y-10:** Organizational structure changes
- **FR Y-6:** Annual ownership and control report
- **FR Y-7N:** Foreign nonbank subsidiary equivalent

## Data Sources

- **Instructions:** [FR Y-11 Instructions](https://www.federalreserve.gov/apps/reportingforms/Report/Index/FR_Y-11FR_Y-11S)
- **Data Dictionary:** `csv/FR_Y11_FOREIGN_SUBSIDIARY.csv`
- **Bulk Data:** Available through FFIEC NIC

## Notes

- Not all fields publicly disclosed
- Critical for CCAR/stress testing subsidiary impacts
- Filing thresholds updated periodically
- Intercompany transactions should be clearly identified
