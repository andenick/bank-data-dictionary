# FFIEC 009 - Country Exposure Report Guide

## Overview

The FFIEC 009 (Country Exposure Report) collects detailed information on the distribution, by country, of claims on foreign residents held by U.S. banking organizations.

## Filing Requirements

**Who Files:**
- U.S. banks with foreign office assets > $30 million
- Edge corporations and agreement corporations
- Bank holding companies with consolidated claims on foreign residents > certain thresholds

**Frequency:** Quarterly

**OMB Control Number:** 7100-0035

## Key Schedules

Claims are reported on an immediate-counterparty basis (country of the obligor) and redistributed to an ultimate-risk basis (country of the guarantor / collateral). The report comprises Schedule C plus the numbered schedules below.

| Schedule | Description |
|----------|-------------|
| Schedule C — Part I | Claims by country (immediate-counterparty basis) with redistribution to ultimate-risk basis; cross-border and foreign-office claims on foreign residents by counterparty country and sector (bank / public / other) |
| Schedule C — Part II | Additional claims detail / memoranda *(UNVERIFIED exact title — confirm against the live FFIEC 009 form)* |
| Schedule 1 / 1.a | Foreign-Office Liabilities by Country of Foreign Office and by Country of Creditor (with memorandum items) |
| Schedule 2 | Derivatives and foreign-office detail: positive fair value of derivative contracts; claims on related foreign branches with no guarantee from parent; foreign-office claims on local residents and foreign-office liabilities |

## Exposure Categories

### Cross-Border Claims
Claims on foreign residents booked at U.S. offices:
- Bank claims
- Public sector claims
- Private nonbank claims

### Foreign Office Claims
Claims booked at foreign branches/subsidiaries:
- Local currency claims
- Cross-border claims in other currencies

### Derivative Exposures
- Current credit exposure
- Potential future exposure
- Credit equivalent amounts

## Transfer Risk Classification

Claims are reported by country with exposure levels:
- **Immediate Counterparty Basis:** Direct obligor location
- **Ultimate Risk Basis:** Guarantor/collateral location
- **Transfer Risk:** Country of domicile for debt service

## Key MDRM Codes

| Mnemonic | Item Code | Description |
|----------|-----------|-------------|
| Various | Country-specific | Claims by counterparty type |
| Various | C-series | Cross-border claims |
| Various | L-series | Liabilities to foreigners |

## Country Risk Analysis

The FFIEC 009 data enables:
- Concentration risk assessment by country
- Transfer risk provisioning (ATRR)
- Sovereign exposure monitoring
- Emerging market risk analysis

## Relationship to Other Forms

- **FFIEC 009a:** Supplemental country exposure information report
- **FR Y-9C Schedule HC-H:** International exposure summary
- **Call Report RC-K:** Foreign office assets/liabilities

## Data Sources

- **Instructions:** [FFIEC 009 Instructions](https://www.ffiec.gov/resources/reporting-forms/ffiec009)
- **Data Dictionary:** `csv/FFIEC_009_COUNTRY_EXPOSURE.csv`
- **Country Codes:** ISO 3166 and FIPS country codes

## Notes

- Confidential report - data not publicly disclosed
- Critical for monitoring geopolitical and sovereign risk
- Requires quarterly restatement when exposure thresholds crossed
- Country classifications follow Federal Reserve guidelines
