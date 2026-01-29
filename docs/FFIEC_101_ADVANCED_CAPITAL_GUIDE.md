# FFIEC 101 - Advanced Capital Adequacy Framework Guide

## Overview

The FFIEC 101 (Regulatory Capital Reporting for Institutions Subject to the Advanced Capital Adequacy Framework) collects detailed information about:
- Components of regulatory capital
- Risk-weighted assets by type of credit risk exposure under the Advanced Internal Ratings-Based (AIRB) Approach
- Risk-weighted assets and operational losses under the Advanced Measurement Approach (AMA)

## Filing Requirements

**Who Files:** Large, internationally active banks and bank holding companies that:
- Have consolidated total assets >= $250 billion, OR
- Have consolidated total on-balance sheet foreign exposure >= $10 billion

**Frequency:** Quarterly

**OMB Control Number:** 7100-0319

## Key Schedules

| Schedule | Description |
|----------|-------------|
| Schedule A | Regulatory Capital Components and Ratios |
| Schedule B | Credit Risk: Wholesale Exposures |
| Schedule C | Credit Risk: Retail Exposures |
| Schedule D | Credit Risk: Counterparty |
| Schedule E | Credit Risk: Securitization |
| Schedule F | Credit Risk: Equity |
| Schedule G | Credit Risk: Cleared Transactions |
| Schedule H | Operational Risk |
| Schedule I | Market Risk |
| Schedule J | Summary |
| Schedule K | Supplementary Leverage Ratio |
| Schedule L | Total Loss-Absorbing Capacity |
| Schedule M-S | Additional Detailed Schedules |

## Key MDRM Codes

| Mnemonic | Item Code | Description |
|----------|-----------|-------------|
| AAAA | 2170 | Total Assets |
| AAAA | 7205 | Total Risk-Based Capital Ratio |
| AAAA | 7206 | Tier 1 Risk-Based Capital Ratio |
| AAAA | P793 | Common Equity Tier 1 Capital Ratio |
| AAAA | 8274 | Tier 1 Capital Allowable |
| AAAA | H015 | Total Leverage Exposure |
| AAAA | H036 | Supplementary Leverage Ratio |

## Relationship to Other Forms

- **FR Y-9C:** FFIEC 101 is filed by the same institutions that file FR Y-9C, providing more granular capital data
- **FFIEC 102:** Market risk data from FFIEC 102 feeds into Schedule I
- **Basel III:** Implements Advanced Approaches under Basel III framework

## Data Sources

- **Instructions:** [FFIEC 101 Instructions](https://www.ffiec.gov/resources/reporting-forms/ffiec101)
- **Data Dictionary:** `csv/FFIEC_101_ADVANCED_CAPITAL.csv`
- **MDRM Reference:** Federal Reserve MDRM Database

## Notes

- Confidentiality flags apply to certain items during parallel run periods
- Dollar values typically reported in thousands
- Effective dates vary by schedule and item
