# Bank Regulatory Filings Master Guide

**Version**: 6.0 | 2026-06-09
**Scope**: Comprehensive reference for U.S. bank regulatory reporting

---

## Table of Contents

1. [Introduction & Purpose](#1-introduction--purpose)
2. [Regulatory Form Hierarchy](#2-regulatory-form-hierarchy)
3. [MDRM Code System](#3-mdrm-code-system)
4. [Schedule-by-Schedule Reference](#4-schedule-by-schedule-reference)
5. [Reconciliation & Validation](#5-reconciliation--validation)
6. [Data Sources & Access](#6-data-sources--access)
7. [G-SIB Entity Identifiers](#7-g-sib-entity-identifiers)
8. [Known Data Quality Issues](#8-known-data-quality-issues)
9. [Appendix: Complete Variable Lists](#9-appendix-complete-variable-lists)

---

## 1. Introduction & Purpose

### 1.1 What This Guide Covers

This guide provides a comprehensive reference for understanding U.S. bank regulatory filings, with particular focus on:

- **FR Y-9C**: Consolidated Financial Statements for Bank Holding Companies (BHCs)
- **FFIEC Call Reports**: Report of Condition and Income for individual banks
- **FR Y-14**: Capital Assessment and Stress Testing data
- **FR 2052a**: Liquidity Monitoring Report
- **Pillar 3**: Basel III public disclosure requirements

### 1.2 Target Audience

- Quantitative researchers analyzing bank data
- Financial analysts evaluating bank performance
- Risk managers assessing trading and derivatives exposure
- Academics studying financial institutions
- Regulators and compliance professionals

### 1.3 How to Use This Guide

This guide is structured from general concepts to specific details:

1. Start with **Section 2** to understand how different forms relate to each other
2. **Section 3** explains the MDRM code system essential for data extraction
3. **Section 4** provides schedule-by-schedule detail
4. **Section 5** covers validation and reconciliation
5. **Section 6** lists data access points

---

## 2. Regulatory Form Hierarchy

### 2.1 Overview of U.S. Bank Regulatory Reporting

U.S. bank regulatory reporting operates at multiple levels:

```
                    ┌─────────────────────────────────────┐
                    │          FEDERAL RESERVE            │
                    │     (Consolidated BHC Level)        │
                    └─────────────────────────────────────┘
                                     │
         ┌───────────────────────────┼───────────────────────────┐
         ▼                           ▼                           ▼
    ┌─────────┐               ┌─────────────┐             ┌──────────┐
    │ FR Y-9C │               │  FR Y-14    │             │ FR 2052a │
    │Quarterly│               │A/Q/M Stress │             │ Liquidity│
    │ $5B+   │               │   $100B+    │             │  Large   │
    └─────────┘               └─────────────┘             └──────────┘
         │
         ▼ (Consolidates)
    ┌─────────────────────────────────────────────────────────────┐
    │                    FFIEC (Bank Level)                       │
    │                    FFIEC Call Reports                       │
    │                    All FDIC-insured banks                   │
    └─────────────────────────────────────────────────────────────┘
```

### 2.2 FR Y-9C: Consolidated Financial Statements for Holding Companies

**Regulator**: Federal Reserve Board
**Frequency**: Quarterly (filed within 40-45 days of quarter end)
**Reporters**: All BHCs/SLHCs with $5 billion or more in total consolidated assets

#### Key Schedules

| Schedule | Name | Content |
|----------|------|---------|
| HC | Balance Sheet | Consolidated balance sheet |
| HC-B | Securities | Available-for-sale and held-to-maturity |
| HC-C | Loans and Leases | Loan portfolio detail |
| HC-D | Trading Assets and Liabilities | Trading book positions |
| HC-L | Derivatives and Off-Balance Sheet | Derivatives notional and fair value |
| HC-N | Past Due and Nonaccrual | Asset quality |
| HC-Q | Assets at Fair Value | Fair value hierarchy (Level 1/2/3) |
| HC-R | Regulatory Capital | Basel III capital ratios |
| HI | Income Statement | Consolidated income statement |

#### Data Availability

- **Historical coverage**: 1986 to present (FR Y-9C panel)
- **Public access**: Federal Reserve NIC database, FFIEC CDR
- **Machine-readable**: Available via bulk download

### 2.3 FFIEC Call Reports: Report of Condition and Income

**Regulator**: FFIEC (Federal Reserve, OCC, FDIC jointly)
**Frequency**: Quarterly
**Reporters**: All FDIC-insured depository institutions

#### Call Report Variants

| Form | Asset Threshold | Filing |
|------|-----------------|--------|
| FFIEC 031 | Banks with foreign offices | More detailed |
| FFIEC 041 | Domestic banks $5B+ | Standard |
| FFIEC 051 | Domestic banks <$5B | Simplified |

#### Relationship to FR Y-9C

The FR Y-9C **consolidates** the Call Reports of all subsidiary banks, plus:
- Nonbank subsidiaries
- Parent company items
- Intercompany eliminations

**Important**: BHC data (Y-9C) ≠ Sum of bank data (Call Reports) due to:
- Nonbank activities
- Different consolidation levels
- Intercompany transactions

### 2.4 FR Y-14: Capital Assessment and Stress Testing

**Regulator**: Federal Reserve Board
**Reporters**: BHCs with $100 billion or more in total consolidated assets

#### Components

| Form | Frequency | Content |
|------|-----------|---------|
| FR Y-14A | Annual | Comprehensive capital planning (CCAR) |
| FR Y-14Q | Quarterly | Ongoing positions and risk metrics |
| FR Y-14M | Monthly | Loan-level portfolio data |

#### Key Y-14Q Schedules for Trading Analysis

- **Schedule G.1**: Trading revenue by product type
- **Schedule G.2**: VaR and Stressed VaR
- **Schedule E.1**: Top counterparty exposures
- **Schedule E.2**: Credit valuation adjustment (CVA)
- **Schedule H**: Pre-Provision Net Revenue (PPNR)

### 2.5 FR 2052a: Complex Institution Liquidity Monitoring Report

**Regulator**: Federal Reserve Board
**Frequency**: Daily (largest firms) or Monthly
**Reporters**: Large BHCs, IHCs, covered savings/loan HCs

#### Purpose

Supports calculation and monitoring of:
- Liquidity Coverage Ratio (LCR)
- Net Stable Funding Ratio (NSFR)
- Internal liquidity stress testing

### 2.6 Pillar 3: Basel III Public Disclosures

**Framework**: Basel Committee on Banking Supervision
**Implementation**: Federal Reserve Regulation Q
**Reporters**: G-SIBs and large internationally active banks

#### Key Templates

| Template | Content |
|----------|---------|
| KM1 | Key regulatory metrics |
| OV1 | Overview of RWA |
| CR1-CR5 | Credit risk |
| MR1-MR4 | Market risk |
| LIQ1-LIQ2 | Liquidity |
| CCR1-CCR8 | Counterparty credit risk |

---

## 3. MDRM Code System

### 3.1 What is MDRM?

**MDRM** = **Micro Data Reference Manual**

The MDRM is the Federal Reserve and FFIEC's system for uniquely identifying every data element in regulatory reports. Understanding MDRM codes is essential for:

- Extracting data from regulatory databases
- Mapping variables across forms
- Tracking historical changes
- Building time series

### 3.2 MDRM Code Structure

An MDRM code consists of:

```
[PREFIX][ITEM_NUMBER]
  4-5       4-5
 chars     chars

Example: BHCK3545
         ├──┤├──┤
         │   │
         │   └── Item Number (3545 = Trading Assets)
         │
         └────── Prefix (BHCK = BHC domestic)
```

### 3.3 Prefix Definitions

#### FR Y-9C Prefixes (Bank Holding Company)

| Prefix | Scope | Description |
|--------|-------|-------------|
| **BHCK** | Domestic only | BHC domestic operations; pre-2018 for items later split |
| **BHCM** | Domestic only (post-2018) | BHC domestic office; introduced for domestic/foreign split |
| **BHCT** | Total consolidated | BHC domestic + foreign; primary prefix for totals |
| **BHCFA** | Regulatory capital | HC-R schedule capital items |
| **BHCA** | Risk-weighted assets | HC-R Part II items |
| **BHCAP** | Advanced approaches | Basel III advanced capital |

#### Call Report Prefixes (Bank Level)

| Prefix | Scope | Description |
|--------|-------|-------------|
| **RCFD** | Full domestic | Bank domestic + foreign branches; most comprehensive |
| **RCON** | Domestic offices only | Excludes foreign branches/agencies |
| **RIAD** | Income/dividends | Income statement items (flow data) |
| **RCFA** | Regulatory capital | RC-R schedule capital items |
| **RCFN** | Foreign only | Foreign office items |

### 3.4 Prefix Conversion Rules

To convert between FR Y-9C and Call Report codes:

| Y-9C Prefix | Call Report Equivalent |
|-------------|------------------------|
| BHCK → | RCFD |
| BHCM → | RCFD (or RCON for domestic-only) |
| BHCT → | RCFD |
| BHCFA → | RCFAA |
| BHCA → | RCFDA |

**Example**:
- Y-9C Total Trading Assets: **BHCT3545**
- Call Report Total Trading Assets: **RCFD3545**

### 3.5 Item Number Ranges

MDRM item numbers follow general patterns:

| Range | General Category |
|-------|------------------|
| 0001-0999 | Assets |
| 1000-1999 | Liabilities |
| 2000-2999 | Capital and equity |
| 3000-3999 | Trading and derivatives |
| 4000-4999 | Income statement |
| 5000+ | Various specialized items |
| A000-Z999 | Extended codes (newer items) |

### 3.6 Historical Code Changes

MDRM codes evolve over time. Major transition periods:

#### 2018 Domestic/Foreign Split
- Many BHCK codes split into BHCM (domestic) + BHCT (total)
- Example: BHCK3531 → BHCM3531 (domestic) + BHCT3531 (total)

#### 2014 Basel III Implementation
- New capital codes introduced (BHCAP, BHCFA prefixes)
- Legacy Basel I/II codes discontinued

#### 2011 MBS Granular Breakout
- Combined MBS codes (BHCK3534, BHCK3536) replaced
- New granular MBS codes (BHCKK197-K201)

#### 2009 Post-Crisis Additions
- Short position codes added (BHCKG209-G211)
- Derivatives fair value detail enhanced

#### 2006 Credit Derivatives
- CDS codes added (BHCKC968-C975)
- TRS and other credit derivatives

---

## 4. Schedule-by-Schedule Reference

### 4.1 Schedule HC / RC: Consolidated Balance Sheet

The main balance sheet schedule provides high-level asset and liability totals.

#### Key Asset Items

| Line | Description | Y-9C MDRM | Call MDRM |
|------|-------------|-----------|-----------|
| 1 | Cash and balances due | BHCK0010 | RCFD0081 |
| 2 | Securities | BHCT1754 | RCFD1754 |
| 3 | Fed funds sold/reverse repos | BHCKC225 | RCFDB987 |
| 4 | Loans and leases, net | BHCKB529 | RCFDB529 |
| **5** | **Trading assets** | **BHCT3545** | **RCFD3545** |
| 10 | Goodwill and intangibles | BHCT2143 | RCFD2143 |
| 11 | Other assets | BHCT2160 | RCFD2160 |
| **12** | **Total assets** | **BHCT2170** | **RCFD2170** |

#### Key Liability Items

| Line | Description | Y-9C MDRM | Call MDRM |
|------|-------------|-----------|-----------|
| 13 | Total deposits | BHCM2200 | RCON2200 |
| 14 | Fed funds purchased/repos | BHCK2800 | RCFDB993 |
| **15** | **Trading liabilities** | **BHCT3548** | **RCFD3548** |
| 16 | Other borrowed money | BHCT3190 | RCFD3190 |
| 19 | Subordinated debt | BHCK4062 | RCFD3200 |
| **21** | **Total liabilities** | **BHCK2948** | **RCFD2948** |

#### Equity Items

| Line | Description | Y-9C MDRM | Call MDRM |
|------|-------------|-----------|-----------|
| 28 | Total equity capital | BHCT3210 | RCFD3210 |
| 29 | Total liabilities and equity | BHCK3300 | RCFD3300 |

### 4.2 Schedule HC-B / RC-B: Securities

Reports securities held in the investment portfolio (not trading).

#### Classification

| Category | Description |
|----------|-------------|
| **Held-to-Maturity (HTM)** | Securities held with intent and ability to hold to maturity |
| **Available-for-Sale (AFS)** | Securities not classified as HTM or trading |

#### Key Items

| Description | HTM MDRM | AFS MDRM |
|-------------|----------|----------|
| U.S. Treasury | BHCK0211 | BHCT1286 |
| U.S. Government agency | BHCK0213 | BHCT1287 |
| MBS - residential | Various | Various |
| MBS - commercial | Various | Various |
| **Total HTM** | **BHCKJJ34** | - |
| **Total AFS** | - | **BHCT1773** |

### 4.3 Schedule HC-D / RC-D: Trading Assets and Liabilities

**Critical Schedule for Trading Analysis**

This schedule breaks down trading book positions reported on Schedule HC lines 5 and 15.

#### Trading Assets (Items 1-12)

| Line | Description | Current MDRM | Legacy MDRM | Start Date |
|------|-------------|--------------|-------------|------------|
| 1 | U.S. Treasury securities | BHCM3531 | BHCK3531 | 2008-03-31 |
| 2 | U.S. Government agency | BHCM3532 | BHCK3532 | 2008-03-31 |
| 3 | Municipal securities | BHCM3533 | BHCK3533 | 2008-03-31 |
| 4.a.(1) | Residential MBS - GNMA | BHCKK197 | - | 2011-03-31 |
| 4.a.(2) | Residential MBS - FNMA/FHLMC | BHCKK198 | - | 2011-03-31 |
| 4.b | Other residential MBS | BHCKK199 | - | 2011-03-31 |
| 4.c.(1) | Commercial MBS - agency | BHCKK200 | - | 2011-03-31 |
| 4.c.(2) | Commercial MBS - other | BHCKK201 | - | 2011-03-31 |
| 5.a | Structured financial products | BHCKHT62 | - | 2018-06-30 |
| 5.b | Other debt securities (incl ABS) | BHCKK202 | - | 2011-03-31 |
| 6.a | Loans - 1-4 family residential | BHCKHT63 | - | 2018-06-30 |
| 6.b | Loans - other real estate | BHCKHT64 | - | 2018-06-30 |
| 6.c | Loans - C&I | BHCKF614 | - | 2008-03-31 |
| 6.d | Loans - consumer | BHCKHT65 | - | 2018-06-30 |
| 6.e | Loans - other | BHCKF618 | - | 2008-03-31 |
| 9 | Other trading assets | BHCM3541 | BHCK3541 | 2008-03-31 |
| **11** | **Derivatives positive fair value** | **BHCT3543** | BHCK3543 | 2009-06-30 |
| **12** | **TOTAL TRADING ASSETS** | **BHCT3545** | BHCK3545 | 1995-12-31 |

#### Trading Liabilities (Items 13-15)

| Line | Description | MDRM | Start Date |
|------|-------------|------|------------|
| 13.a.(1) | Short positions - Equity | BHCKG209 | 2009-03-31 |
| 13.a.(2) | Short positions - Debt | BHCKG210 | 2009-03-31 |
| 13.a.(3) | Short positions - Other | BHCKG211 | 2009-03-31 |
| 13.b | Other trading liabilities | BHCKF624 | 2008-03-31 |
| **14** | **Derivatives negative fair value** | **BHCT3547** | 2009-06-30 |
| **15** | **TOTAL TRADING LIABILITIES** | **BHCT3548** | 1989-09-30 |

### 4.4 Schedule HC-L / RC-L: Derivatives and Off-Balance Sheet Items

**Critical Schedule for Derivatives Analysis**

Schedule HC-L reports:
1. **Notional amounts** by product type
2. **Fair values** by asset class and trading/non-trading purpose

#### Notional Amounts by Product Type

##### Futures (Exchange-Traded)

| Asset Class | MDRM |
|-------------|------|
| Interest Rate | BHCK8693 |
| Foreign Exchange | BHCK8694 |
| Equity | BHCK8695 |
| Commodity/Other | BHCK8696 |

##### Forwards (OTC)

| Asset Class | MDRM |
|-------------|------|
| Interest Rate | BHCK8697 |
| Foreign Exchange | BHCK8698 |
| Equity | BHCK8699 |
| Commodity/Other | BHCK8700 |

##### Swaps

| Asset Class | MDRM |
|-------------|------|
| Interest Rate | BHCK3450 |
| Cross-Currency | BHCK3826 |
| Equity | BHCK8719 |
| Commodity/Other | BHCK8720 |

##### Options (Exchange-Traded)

| Asset Class | Written | Purchased |
|-------------|---------|-----------|
| Interest Rate | BHCK8701 | BHCK8705 |
| Foreign Exchange | BHCK8702 | BHCK8706 |
| Equity | BHCK8703 | BHCK8707 |
| Commodity/Other | BHCK8704 | BHCK8708 |

##### Options (OTC)

| Asset Class | Written | Purchased |
|-------------|---------|-----------|
| Interest Rate | BHCK8709 | BHCK8713 |
| Foreign Exchange | BHCK8710 | BHCK8714 |
| Equity | BHCK8711 | BHCK8715 |
| Commodity/Other | BHCK8712 | BHCK8716 |

##### Credit Derivatives

| Type | Protection Sold | Protection Bought |
|------|-----------------|-------------------|
| Credit Default Swaps | BHCKC968 | BHCKC969 |
| Total Return Swaps | BHCKC970 | BHCKC971 |
| Other Credit Derivatives | BHCKC974 | BHCKC975 |

#### Fair Values by Asset Class

##### Trading Derivatives

| Asset Class | Positive FV | Negative FV |
|-------------|-------------|-------------|
| Interest Rate | BHCK8733 | BHCK8737 |
| Foreign Exchange | BHCK8734 | BHCK8738 |
| Equity | BHCK8735 | BHCK8739 |
| Commodity/Other | BHCK8736 | BHCK8740 |

##### Non-Trading Hedges

| Asset Class | Positive FV | Negative FV |
|-------------|-------------|-------------|
| Interest Rate | BHCK8741 | BHCK8745 |
| Foreign Exchange | BHCK8742 | BHCK8746 |
| Equity | BHCK8743 | BHCK8747 |
| Commodity/Other | BHCK8744 | BHCK8748 |

### 4.5 Schedule HC-Q / RC-Q: Assets and Liabilities at Fair Value

Reports assets and liabilities measured at fair value by valuation hierarchy.

#### Fair Value Hierarchy

| Level | Description | Observability |
|-------|-------------|---------------|
| **Level 1** | Quoted prices in active markets | Directly observable |
| **Level 2** | Observable inputs other than Level 1 | Indirectly observable |
| **Level 3** | Unobservable inputs | Model-based |

#### Trading Assets by Level

| Level | MDRM |
|-------|------|
| Level 1 | BHCKF527 |
| Level 2 | BHCKF528 |
| Level 3 | BHCKF529 |

### 4.6 Schedule HC-R / RC-R: Regulatory Capital

Reports Basel III regulatory capital components and ratios.

#### Capital Components

| Item | Description | MDRM |
|------|-------------|------|
| CET1 | Common Equity Tier 1 Capital | BHCAP859 |
| AT1 | Additional Tier 1 Capital | BHCAP865 |
| T1 | Tier 1 Capital (CET1 + AT1) | BHCA8274 |
| T2 | Tier 2 Capital | BHCA5311 |
| TC | Total Capital (T1 + T2) | BHCA3792 |
| RWA | Total Risk-Weighted Assets | BHCAA223 |

#### Key Ratios

| Ratio | Formula | Minimum |
|-------|---------|---------|
| CET1 Ratio | CET1 / RWA | 4.5% |
| Tier 1 Ratio | T1 / RWA | 6.0% |
| Total Capital Ratio | TC / RWA | 8.0% |
| Leverage Ratio | T1 / Total Exposure | 3.0% |

---

## 5. Reconciliation & Validation

### 5.1 Balance Sheet Crosswalks

#### Trading Assets Reconciliation

**Rule**: Schedule HC Item 5 = Schedule HC-D Item 12

```
BHCT3545 (HC Item 5) = BHCT3545 (HC-D Item 12)
                     = Sum of HC-D Items 1-11
```

Components:
- Securities (Items 1-5): Treasuries, agencies, munis, MBS, debt
- Loans (Items 6): Various loan types
- Other (Item 9): Residual trading assets
- Derivatives (Item 11): Positive fair value derivatives

#### Trading Liabilities Reconciliation

**Rule**: Schedule HC Item 15 = Schedule HC-D Item 15

```
BHCT3548 (HC Item 15) = BHCT3548 (HC-D Item 15)
                      = Sum of HC-D Items 13-14
```

Components:
- Short positions (Items 13.a): Equity, debt, other
- Other liabilities (Item 13.b)
- Derivatives (Item 14): Negative fair value derivatives

### 5.2 Derivatives Fair Value Reconciliation

**Rule**: HC-D derivatives = Sum of HC-L fair values

#### Positive Fair Value

```
BHCT3543 (HC-D Item 11) = Trading positive FV + Non-trading positive FV

Trading Positive FV = BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736
                    = IR + FX + Equity + Commodity trading positive

Non-Trading Positive FV = BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744
                        = IR + FX + Equity + Commodity non-trading positive
```

#### Negative Fair Value

```
BHCT3547 (HC-D Item 14) = Trading negative FV + Non-trading negative FV

Trading Negative FV = BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740
                    = IR + FX + Equity + Commodity trading negative

Non-Trading Negative FV = BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748
                        = IR + FX + Equity + Commodity non-trading negative
```

### 5.3 Capital Reconciliation

```
Total Capital (BHCA3792) = Tier 1 (BHCA8274) + Tier 2 (BHCA5311)
Tier 1 (BHCA8274) = CET1 (BHCAP859) + AT1 (BHCAP865)
```

### 5.4 Common Validation Checks

| Check | Formula | Expected |
|-------|---------|----------|
| Balance sheet balance | Total Assets = Total Liabilities + Equity | Must equal |
| Trading assets detail | HC-D Item 12 = HC Item 5 | Must equal |
| Trading liabilities detail | HC-D Item 15 = HC Item 15 | Must equal |
| Capital components | T1 + T2 = Total Capital | Must equal |
| RWA consistency | Credit RWA + Market RWA + Op RWA = Total RWA | Must equal |

---

## 6. Data Sources & Access

### 6.1 FFIEC Central Data Repository (CDR)

**URL**: https://cdr.ffiec.gov/

**Content**: Call Report and FR Y-9C data

**Access Methods**:
- Online interface for individual filers
- Bulk download for all filers
- XBRL taxonomy files

### 6.2 Federal Reserve NIC Database

**URL**: https://www.ffiec.gov/NPW/

**Content**: National Information Center - organization data

**Key Features**:
- RSSD ID lookups
- Corporate structure
- Historical name changes

### 6.3 Federal Reserve Bank of Chicago

**URL**: https://www.chicagofed.org/banking/financial-institution-reports/

**Content**: Historical FR Y-9C data

**Coverage**: 1986-present

### 6.4 FDIC BankFind Suite

**URL**: https://banks.data.fdic.gov/

**Content**: Bank financial data and failure information

**Key Features**:
- Summary of Deposits
- Historical data
- Failure information

### 6.5 Chicago Fed Bank Holding Company Database

**URL**: https://www.chicagofed.org/banking/financial-institution-reports/bhc-data

**Description**: Public historical FR Y-9C holding-company panel

**Coverage**: 1986 to present

**Content**: All Y-9C variables in downloadable bulk files

### 6.6 Wharton Research Data Services (WRDS)

**URL**: https://wrds-www.wharton.upenn.edu/

**Content**: Bank Regulatory suite

**Access**: Academic subscription required

---

## 7. G-SIB Entity Identifiers

### 7.1 Identifier Types

| Identifier | Source | Used In |
|------------|--------|---------|
| **RSSD ID** | Federal Reserve | FR Y-9C, NIC database |
| **FDIC Certificate** | FDIC | Call Reports, FDIC databases |
| **LEI** | GLEIF | Pillar 3, international reporting |
| **OCC Charter** | OCC | National bank identification |

### 7.2 Major Trading BHCs

| Entity | RSSD ID | G-SIB Bucket | Assets (2024) |
|--------|---------|--------------|---------------|
| JPMorgan Chase & Co. | 1039502 | 4 (3.5%) | $3.9T |
| Bank of America Corp | 1073757 | 3 (2.5%) | $3.3T |
| Citigroup Inc. | 1951350 | 3 (2.5%) | $2.4T |
| Wells Fargo & Co. | 1120754 | 2 (1.5%) | $1.9T |
| Goldman Sachs Group | 2380443 | 2 (1.5%) | $1.7T |
| Morgan Stanley | 2162966 | 2 (1.5%) | $1.2T |
| Bank of New York Mellon | 3587146 | 1 (1.0%) | $0.4T |
| State Street Corp | 1111435 | 1 (1.0%) | $0.3T |

---

## 8. Known Data Quality Issues

### 8.1 Historical Discontinuities

#### MDRM Code Changes

When MDRM codes change, time series have breaks:
- **2018 prefix changes**: BHCK → BHCM/BHCT splits
- **2011 MBS breakout**: Combined MBS → granular items
- **2014 Basel III**: New capital codes

**Solution**: Create crosswalk tables mapping old to new codes

#### Reporting Threshold Changes

Asset thresholds for filing have changed:
- FR Y-9C: Increased from $150M to $5B over time
- FR Y-14: $100B threshold since inception

### 8.2 Consolidation Issues

#### BHC vs Bank Data

BHC data includes nonbank subsidiaries and may differ from sum of bank subsidiaries due to:
- Nonbank trading operations
- Intercompany eliminations
- Different accounting treatments

#### Foreign Operations

- BHCK/RCON = Domestic only
- BHCT/RCFD = Including foreign

Ensure consistent scope when comparing.

### 8.3 Timing Issues

#### Quarter-End vs Average

Some items are reported as:
- Quarter-end balances (point-in-time)
- Quarterly averages
- Year-to-date cumulative (income items)

### 8.4 Restatements

Banks may file amendments that restate prior data. The CDR tracks amendments with:
- Amendment flags
- Submission dates
- Version numbers

---

## 9. Appendix: Complete Variable Lists

### 9.1 Core Balance Sheet Variables

See `MDRM_MASTER_COMPLETE.csv` for full list.

### 9.2 Trading and Derivatives Variables

See `HC_D_TRADING_ASSETS.csv` and `HC_L_DERIVATIVES.csv`.

### 9.3 Capital Variables

Key capital variables:

| Variable | Description | MDRM |
|----------|-------------|------|
| CET1 Capital | Common Equity Tier 1 | BHCAP859 |
| Tier 1 Capital | Total Tier 1 | BHCA8274 |
| Tier 2 Capital | Tier 2 | BHCA5311 |
| Total Capital | Total Risk-Based | BHCA3792 |
| RWA | Risk-Weighted Assets | BHCAA223 |

### 9.4 CAMELS Categories

Variables are classified by CAMELS category:

| Code | Category | Focus |
|------|----------|-------|
| C | Capital Adequacy | Regulatory capital ratios |
| A | Asset Quality | NPLs, charge-offs, allowances |
| M | Management | Size, structure, efficiency |
| E | Earnings | ROA, ROE, NIM, revenue |
| L | Liquidity | Funding, deposits, LCR |
| S | Sensitivity to Market Risk | Trading, derivatives, VaR |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-28 | N. Anderson | Initial comprehensive guide |
| 6.0 | 2026-06-09 | N. Anderson | Aligned to v6.0 rebuild (NIC entity layer, full collection/sub-schedule catalogue, identifier semantics, coverage/provenance, expanded MDRM/namespace catalogue) |

---

**End of Master Regulatory Guide**
