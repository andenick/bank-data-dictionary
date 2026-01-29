# FFIEC 102 - Market Risk Regulatory Report Guide

## Overview

The FFIEC 102 (Market Risk Regulatory Report for Institutions Subject to the Market Risk Capital Rule) collects information on:
- Value-at-Risk (VaR) based measures
- Specific risk add-ons
- Incremental Risk Capital (IRC) requirement
- Comprehensive Risk Measure (CRM)
- De minimis positions

## Filing Requirements

**Who Files:** Banks, savings associations, and holding companies with:
- Aggregate trading assets and trading liabilities >= $1 billion, OR
- Aggregate trading assets and trading liabilities >= 10% of total assets

**Frequency:** Quarterly

**OMB Control Number:** 7100-0365

## Key Schedules

| Schedule | Description |
|----------|-------------|
| Schedule A | Market Risk Capital |
| Schedule B | VaR-Based Measures |
| Schedule C | Specific Risk Add-Ons |
| Schedule D | Incremental Risk Capital |
| Schedule E | Comprehensive Risk Measure |
| Schedule F | De Minimis Exemption |

## Key MDRM Codes

| Mnemonic | Item Code | Description |
|----------|-----------|-------------|
| MRRR | 4086 | Internet E-mail Address |
| MRRR | 9017 | Legal Name |
| MRRR | 9224 | Legal Entity Identifier (LEI) |
| MRRR | F838 | Reporting Entity Code |
| MRRR | F839 | Primary Federal Regulator Code |

## Market Risk Measures

### Value-at-Risk (VaR)
- 10-day, 99% confidence interval
- Used for general market risk

### Stressed VaR (sVaR)
- VaR using historical period of significant market stress
- Typically 2007-2008 financial crisis period

### Incremental Risk Capital (IRC)
- Captures default and migration risk
- 1-year horizon, 99.9% confidence level

### Comprehensive Risk Measure (CRM)
- For correlation trading portfolios
- Includes default, credit migration, and spread risk

## Relationship to Other Forms

- **FFIEC 101:** Advanced approaches capital feeds from FFIEC 102 market risk
- **FR Y-9C Schedule HC-D:** Trading assets/liabilities must reconcile
- **Pillar 3 Disclosures:** Market risk information disclosed publicly

## Data Sources

- **Instructions:** [FFIEC 102 Instructions](https://www.ffiec.gov/resources/reporting-forms/ffiec102)
- **Data Dictionary:** `csv/FFIEC_102_MARKET_RISK.csv`
- **MDRM Reference:** Federal Reserve MDRM Database

## Notes

- Introduced in 2015 to implement Basel 2.5 market risk amendments
- Subject to ongoing revisions under Basel III Fundamental Review of Trading Book (FRTB)
