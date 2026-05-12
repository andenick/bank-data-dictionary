# Bank Trading Activities Deep Dive Guide

**Version**: 1.0
**Last Updated**: 2026-01-28
**Focus**: Schedule HC-D (Trading) and Schedule HC-L (Derivatives) Analysis

---

## Table of Contents

1. [Introduction to Bank Trading Activities](#1-introduction-to-bank-trading-activities)
2. [Schedule HC-D: Trading Assets & Liabilities](#2-schedule-hc-d-trading-assets--liabilities)
3. [Schedule HC-L: Derivatives and Off-Balance Sheet](#3-schedule-hc-l-derivatives-and-off-balance-sheet)
4. [The HC → HC-D → HC-L Linkage](#4-the-hc--hc-d--hc-l-linkage)
5. [Call Report Equivalents (RC-D, RC-L)](#5-call-report-equivalents-rc-d-rc-l)
6. [FR Y-14 Trading Schedules](#6-fr-y-14-trading-schedules)
7. [Pillar 3 Market Risk Templates](#7-pillar-3-market-risk-templates)
8. [Reconciliation Checks](#8-reconciliation-checks)
9. [Major Trading BHCs](#9-major-trading-bhcs)
10. [Appendix: Complete Code Tables](#10-appendix-complete-code-tables)

---

## 1. Introduction to Bank Trading Activities

### 1.1 What is Bank Trading?

Bank trading activities involve positions held for:
- **Market making**: Providing liquidity to clients
- **Proprietary trading**: Taking positions for profit (limited post-Volcker)
- **Hedging**: Managing risk from other banking activities
- **Customer facilitation**: Supporting client transactions

### 1.2 Regulatory Framework

Trading activities are governed by multiple regulatory frameworks:

| Regulation | Focus | Key Requirements |
|------------|-------|------------------|
| Volcker Rule | Proprietary trading | Restricts prop trading, requires compliance |
| Basel III | Capital | Market risk capital for trading book |
| Dodd-Frank | Derivatives | Central clearing, margin requirements |
| SEC/CFTC | Derivatives | Swap dealer registration, reporting |

### 1.3 Key Regulatory Filings for Trading

| Form | Schedule | Content |
|------|----------|---------|
| FR Y-9C | HC-D | Trading assets and liabilities |
| FR Y-9C | HC-L | Derivatives notional and fair value |
| FR Y-9C | HC-Q | Fair value hierarchy |
| FR Y-14Q | Schedule G | Trading revenue, VaR |
| Pillar 3 | MR1-MR4 | Market risk disclosures |

### 1.4 Why Trading Data Matters

Understanding bank trading data is essential for:

1. **Risk Assessment**: Evaluating market risk exposure
2. **Capital Analysis**: Understanding trading book capital requirements
3. **Revenue Analysis**: Decomposing bank earnings
4. **Systemic Risk**: Assessing interconnectedness via derivatives
5. **Volcker Compliance**: Monitoring permitted activities

---

## 2. Schedule HC-D: Trading Assets & Liabilities

### 2.1 Overview

Schedule HC-D provides the detailed breakdown of trading book positions summarized on the main balance sheet (Schedule HC Items 5 and 15).

```
Schedule HC (Balance Sheet)
├── Item 5: Trading Assets → Detailed in HC-D Items 1-12
└── Item 15: Trading Liabilities → Detailed in HC-D Items 13-15
```

### 2.2 Trading Assets Breakdown

#### Securities Held for Trading (Items 1-5)

##### Item 1: U.S. Treasury Securities

| MDRM | Period | Scope |
|------|--------|-------|
| BHCM3531 | 2018-03-31 to present | Domestic + Foreign consolidated |
| BHCK3531 | 1995-03-31 to 2018-03-31 | Domestic only (legacy) |

**Content**: U.S. Treasury bills, notes, bonds, TIPS held in trading book.

**Use**: Primary safe-haven trading asset; large positions at major dealers.

##### Item 2: U.S. Government Agency Obligations

| MDRM | Period | Scope |
|------|--------|-------|
| BHCM3532 | 2018-03-31 to present | Domestic + Foreign consolidated |
| BHCK3532 | 1995-03-31 to 2018-03-31 | Domestic only (legacy) |

**Content**: FNMA, FHLMC, FHLB, GNMA debt securities (non-MBS).

##### Item 3: Municipal Securities

| MDRM | Period | Scope |
|------|--------|-------|
| BHCM3533 | 2018-03-31 to present | Domestic + Foreign consolidated |
| BHCK3533 | 1995-03-31 to 2018-03-31 | Domestic only (legacy) |

**Content**: Securities issued by states and political subdivisions.

##### Item 4: Mortgage-Backed Securities (MBS)

The MBS section underwent major restructuring in 2011:

**Current Structure (2011-present)**:

| Line | Description | MDRM | Start |
|------|-------------|------|-------|
| 4.a.(1) | Residential MBS - GNMA pass-through | BHCKK197 | 2011-03-31 |
| 4.a.(2) | Residential MBS - FNMA/FHLMC pass-through | BHCKK198 | 2011-03-31 |
| 4.b | All other residential MBS | BHCKK199 | 2011-03-31 |
| 4.c.(1) | Commercial MBS - agency issued | BHCKK200 | 2011-03-31 |
| 4.c.(2) | Commercial MBS - all other | BHCKK201 | 2011-03-31 |

**Legacy Structure (pre-2011)**:

| Line | Description | MDRM | End |
|------|-------------|------|-----|
| 4 | MBS pass-through (combined) | BHCK3534 | 2009-03-31 |
| 4 | All other MBS (combined) | BHCK3536 | 2009-03-31 |

**Key Distinction**:
- **Agency MBS** (K197, K198, K200): Government-backed, lower risk
- **Non-Agency MBS** (K199, K201): Private-label, higher risk, focus during 2008 crisis

##### Item 5: Other Debt Securities

**Current Structure (2018-present)**:

| Line | Description | MDRM | Start |
|------|-------------|------|-------|
| 5.a | Structured financial products | BHCKHT62 | 2018-06-30 |
| 5.b | Other debt securities (incl ABS) | BHCKK202 | 2011-03-31 |

**Content**:
- **5.a**: CDOs, CLOs, structured notes, complex products
- **5.b**: Corporate bonds, ABS, foreign government debt, other

#### Loans Held for Trading (Item 6)

**Current Structure (2018-present)**:

| Line | Description | MDRM | Start |
|------|-------------|------|-------|
| 6.a | 1-4 family residential loans | BHCKHT63 | 2018-06-30 |
| 6.b | Other real estate loans | BHCKHT64 | 2018-06-30 |
| 6.c | Commercial and industrial loans | BHCKF614 | 2008-03-31 |
| 6.d | Consumer loans | BHCKHT65 | 2018-06-30 |
| 6.e | Other loans | BHCKF618 | 2008-03-31 |

**Use Cases**:
- Mortgage trading desks (Items 6.a, 6.b)
- Leveraged loan trading (Item 6.c)
- Consumer loan securitization flow (Item 6.d)

#### Other Trading Assets (Item 9)

| MDRM | Period | Scope |
|------|--------|-------|
| BHCM3541 | 2018-03-31 to present | Domestic + Foreign |
| BHCK3541 | 1995-03-31 to 2018-03-31 | Domestic only (legacy) |

**Content**: Residual trading assets not elsewhere classified:
- Equity securities held for trading
- Precious metals
- Physical commodities
- Other

#### Derivatives with Positive Fair Value (Item 11)

| MDRM | Period |
|------|--------|
| BHCT3543 | 2009-06-30 to present |
| BHCK3543 | 1995-03-31 to 2018-03-31 (legacy) |

**Critical Linkage**: This item links to Schedule HC-L fair values.

**Formula**:
```
BHCT3543 = Sum of all positive fair value derivatives from HC-L
         = Trading positive FV + Non-trading hedge positive FV
         = (BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736)
         + (BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744)
```

#### Total Trading Assets (Item 12)

| MDRM | Period |
|------|--------|
| BHCT3545 | 1995-12-31 to present |

**Reconciliation Rule**:
```
HC-D Item 12 (BHCT3545) = Schedule HC Item 5 (BHCT3545)
```

### 2.3 Trading Liabilities Breakdown

#### Short Positions (Item 13)

Short positions were added post-crisis (2009) to increase transparency:

| Line | Description | MDRM | Start |
|------|-------------|------|-------|
| 13.a.(1) | Short positions - Equity securities | BHCKG209 | 2009-03-31 |
| 13.a.(2) | Short positions - Debt securities | BHCKG210 | 2009-03-31 |
| 13.a.(3) | Short positions - All other | BHCKG211 | 2009-03-31 |
| 13.b | Other trading liabilities | BHCKF624 | 2008-03-31 |

**Content**:
- Securities sold short pending delivery
- Obligations to return borrowed securities
- Other trading book liabilities

#### Derivatives with Negative Fair Value (Item 14)

| MDRM | Period |
|------|--------|
| BHCT3547 | 2009-06-30 to present |
| BHCK3547 | 1994-03-31 to present (legacy) |

**Formula**:
```
BHCT3547 = Sum of all negative fair value derivatives from HC-L
         = Trading negative FV + Non-trading hedge negative FV
         = (BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740)
         + (BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748)
```

#### Total Trading Liabilities (Item 15)

| MDRM | Period |
|------|--------|
| BHCT3548 | 1989-09-30 to present |

**Reconciliation Rule**:
```
HC-D Item 15 (BHCT3548) = Schedule HC Item 15 (BHCT3548)
```

### 2.4 Historical Evolution of HC-D

| Period | Change | Impact |
|--------|--------|--------|
| 1995 | Initial structure | Basic trading asset/liability reporting |
| 2008 | Post-crisis expansion | Added loan detail, other trading liab |
| 2009 | Short positions added | Items 13.a added for short sales |
| 2011 | MBS granular breakout | K197-K202 codes added |
| 2018 | Further granularity | HT62-HT65 codes; prefix split |

---

## 3. Schedule HC-L: Derivatives and Off-Balance Sheet

### 3.1 Overview

Schedule HC-L reports derivatives in two dimensions:
1. **Notional amounts**: Contract face value by product type
2. **Fair values**: Mark-to-market value by asset class

### 3.2 Understanding Notional vs Fair Value

| Measure | Definition | Use |
|---------|------------|-----|
| **Notional** | Face/principal amount of contract | Activity level, exposure |
| **Fair Value** | Current mark-to-market value | Balance sheet impact |

**Example**: A $100M interest rate swap at inception:
- Notional: $100M
- Fair Value: $0 (at-the-money at inception)

After rates move, same swap might have:
- Notional: $100M (unchanged)
- Fair Value: +$2M (in-the-money) or -$3M (out-of-the-money)

**Key Insight**: Notional >> Fair Value typically

For G-SIBs, notional amounts can exceed $50 trillion while fair values are in the hundreds of billions.

### 3.3 Notional Amounts by Product Type

#### Futures (Exchange-Traded)

| Asset Class | MDRM | Notes |
|-------------|------|-------|
| Interest Rate | BHCK8693 | Treasury futures, Eurodollar futures |
| Foreign Exchange | BHCK8694 | Currency futures |
| Equity | BHCK8695 | Index futures, single stock futures |
| Commodity/Other | BHCK8696 | Oil, gold, agricultural futures |

**Characteristics**:
- Standardized contracts
- Exchange clearing (CCPs)
- Daily mark-to-market
- Lower counterparty risk

#### Forwards (OTC)

| Asset Class | MDRM | Notes |
|-------------|------|-------|
| Interest Rate | BHCK8697 | FRAs |
| Foreign Exchange | BHCK8698 | FX forwards, spots > 2 days |
| Equity | BHCK8699 | Equity forwards |
| Commodity/Other | BHCK8700 | Commodity forwards |

**Characteristics**:
- Customized contracts
- Bilateral counterparty risk
- Settlement at maturity

**Note**: FX forwards (BHCK8698) include spot transactions with settlement > 2 business days.

#### Swaps

| Asset Class | MDRM | Notes |
|-------------|------|-------|
| Interest Rate | BHCK3450 | LARGEST category; fixed-for-floating |
| Cross-Currency | BHCK3826 | Currency swaps |
| Equity | BHCK8719 | Total return swaps on equity |
| Commodity/Other | BHCK8720 | Commodity swaps |

**Interest Rate Swaps (BHCK3450)**:
- Largest derivatives category by notional
- JPMorgan alone: >$40 trillion notional
- Used for ALM hedging, trading, client facilitation

#### Options

Options are reported separately by:
- **Venue**: Exchange vs OTC
- **Direction**: Written (sold) vs Purchased (bought)
- **Asset Class**: IR, FX, Equity, Commodity

| Asset Class | Exch Written | Exch Purch | OTC Written | OTC Purch |
|-------------|--------------|------------|-------------|-----------|
| Interest Rate | BHCK8701 | BHCK8705 | BHCK8709 | BHCK8713 |
| Foreign Exchange | BHCK8702 | BHCK8706 | BHCK8710 | BHCK8714 |
| Equity | BHCK8703 | BHCK8707 | BHCK8711 | BHCK8715 |
| Commodity/Other | BHCK8704 | BHCK8708 | BHCK8712 | BHCK8716 |

**Written vs Purchased**:
- **Written (Sold)**: Bank receives premium, has obligation
- **Purchased (Bought)**: Bank pays premium, has right

#### Credit Derivatives

Credit derivatives were added in 2006 (Q1 2006):

| Type | Protection Sold (Guarantor) | Protection Bought (Beneficiary) |
|------|----------------------------|--------------------------------|
| Credit Default Swaps | BHCKC968 | BHCKC969 |
| Total Return Swaps | BHCKC970 | BHCKC971 |
| Other Credit Deriv | BHCKC974 | BHCKC975 |

**Credit Default Swaps (CDS)**:
- **Protection Sold (C968)**: Bank is guarantor, assumes credit risk
- **Protection Bought (C969)**: Bank is beneficiary, hedges credit risk

**Net CDS Position**:
```
Net CDS Exposure = Protection Bought - Protection Sold
                 = BHCKC969 - BHCKC968
```
- Positive: Net buyer of protection (hedged/bearish)
- Negative: Net seller of protection (risk-taking/bullish)

### 3.4 Fair Values by Asset Class

#### Trading Derivatives

| Asset Class | Positive FV | Negative FV |
|-------------|-------------|-------------|
| Interest Rate | BHCK8733 | BHCK8737 |
| Foreign Exchange | BHCK8734 | BHCK8738 |
| Equity | BHCK8735 | BHCK8739 |
| Commodity/Other | BHCK8736 | BHCK8740 |

**Positive Fair Value**: Derivatives that are in-the-money (assets)
**Negative Fair Value**: Derivatives that are out-of-the-money (liabilities)

#### Non-Trading Hedges

| Asset Class | Positive FV | Negative FV |
|-------------|-------------|-------------|
| Interest Rate | BHCK8741 | BHCK8745 |
| Foreign Exchange | BHCK8742 | BHCK8746 |
| Equity | BHCK8743 | BHCK8747 |
| Commodity/Other | BHCK8744 | BHCK8748 |

**Trading vs Non-Trading**:
- **Trading**: Held for market making, customer facilitation, (limited) prop trading
- **Non-Trading Hedges**: Designated hedges of banking book items (loans, deposits)

### 3.5 Netting and Gross vs Net Fair Value

Reported fair values are **gross** (before netting).

**Netting**: Under ISDA master agreements and CSAs, banks can net:
- Positive and negative fair values with same counterparty
- Collateral received/posted

**Balance Sheet Impact**:
```
Gross Positive FV (HC-L) ≥ Net Derivative Assets (Balance Sheet)
```

Banks apply netting for balance sheet presentation but report gross in HC-L.

---

## 4. The HC → HC-D → HC-L Linkage

### 4.1 Hierarchical Structure

```
Schedule HC (Balance Sheet)
│
├── Item 5: Trading Assets (BHCT3545)
│   │
│   └── Schedule HC-D (Trading Detail)
│       ├── Items 1-5: Securities
│       ├── Item 6: Loans
│       ├── Item 9: Other trading assets
│       ├── Item 11: Derivatives positive FV ─────────┐
│       └── Item 12: TOTAL (= HC Item 5)              │
│                                                      │
├── Item 15: Trading Liabilities (BHCT3548)           │
│   │                                                  │
│   └── Schedule HC-D (Trading Detail)                │
│       ├── Item 13: Short positions & other          │
│       ├── Item 14: Derivatives negative FV ─────────┤
│       └── Item 15: TOTAL (= HC Item 15)             │
│                                                      │
└───────────────────────────────────────────────────┐ │
                                                    │ │
Schedule HC-L (Derivatives Detail) ◄────────────────┴─┘
├── Notional Amounts (by product type)
│   ├── Futures
│   ├── Forwards
│   ├── Swaps
│   ├── Options
│   └── Credit Derivatives
│
└── Fair Values (by asset class)
    ├── Trading Positive FV ──► Sums to HC-D Item 11
    ├── Trading Negative FV ──► Sums to HC-D Item 14
    ├── Non-Trading Positive FV ──► Sums to HC-D Item 11
    └── Non-Trading Negative FV ──► Sums to HC-D Item 14
```

### 4.2 Key Reconciliation Formulas

#### Trading Assets Derivatives

```
HC-D Item 11 (BHCT3543) = HC-L Trading Pos FV + HC-L Non-Trading Pos FV

Where:
  HC-L Trading Pos FV = BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736
  HC-L Non-Trading Pos FV = BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744
```

#### Trading Liabilities Derivatives

```
HC-D Item 14 (BHCT3547) = HC-L Trading Neg FV + HC-L Non-Trading Neg FV

Where:
  HC-L Trading Neg FV = BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740
  HC-L Non-Trading Neg FV = BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748
```

### 4.3 Notional to Fair Value Relationship

**Important**: Notional amounts do NOT link directly to balance sheet.

The relationship between notional and fair value:
- Notional represents contract size (activity level)
- Fair value represents economic value (balance sheet)
- Fair value is typically << 5% of notional
- Fair value can be positive or negative

**Example** (Illustrative G-SIB):
```
Interest Rate Swaps:
  Notional: $40 trillion
  Positive FV: $200 billion (0.5% of notional)
  Negative FV: $195 billion
  Net FV: $5 billion
```

---

## 5. Call Report Equivalents (RC-D, RC-L)

### 5.1 Parallel Structure

Call Report schedules RC-D and RC-L mirror FR Y-9C schedules HC-D and HC-L.

| FR Y-9C | Call Report | Level |
|---------|-------------|-------|
| HC-D | RC-D | BHC consolidated → Bank level |
| HC-L | RC-L | BHC consolidated → Bank level |

### 5.2 MDRM Prefix Conversion

| Y-9C Prefix | Call Report Prefix |
|-------------|-------------------|
| BHCK | RCFD |
| BHCM | RCFD (or RCON) |
| BHCT | RCFD |

**Example**:
- Y-9C Total Trading Assets: **BHCT3545**
- Call Report Total Trading Assets: **RCFD3545**

### 5.3 Key Differences

| Aspect | FR Y-9C (HC-D/HC-L) | Call Report (RC-D/RC-L) |
|--------|---------------------|-------------------------|
| Entity Level | Consolidated BHC | Individual bank |
| Includes | All subsidiaries | Bank only |
| Nonbank Trading | Included | Excluded |
| Foreign Offices | Consolidated | Depends on prefix |

### 5.4 BHC vs Sum of Banks

**Warning**: BHC trading data ≠ Sum of subsidiary bank data

Reasons:
1. **Nonbank trading**: Broker-dealer subs trade but aren't banks
2. **Eliminations**: Intercompany positions eliminated at BHC level
3. **Different reporting**: Some items differ between forms

---

## 6. FR Y-14 Trading Schedules

### 6.1 Overview

FR Y-14 provides granular trading data not available in FR Y-9C.

| Form | Schedule | Content | Frequency |
|------|----------|---------|-----------|
| Y-14Q | G.1 | Trading Revenue | Quarterly |
| Y-14Q | G.2 | VaR/Stressed VaR | Quarterly |
| Y-14Q | E.1 | Top Counterparties | Quarterly |
| Y-14Q | E.2 | CVA | Quarterly |

### 6.2 Schedule G.1: Trading Revenue

Breaks down trading revenue by:
- Product type (IR, FX, Equity, Commodity, Credit)
- Revenue component (Bid-ask, Position change, CVA)

**Links to FR Y-9C**:
- Total trading revenue should reconcile to HI trading revenue items

### 6.3 Schedule G.2: VaR and Stressed VaR

Reports:
- Daily VaR at 99% confidence
- Stressed VaR (crisis period calibration)
- VaR breaches/backtesting

**Regulatory Use**: Determines market risk capital under IMA

### 6.4 Schedule E.1: Top Counterparties

Reports:
- Top 50 counterparties by exposure
- Gross and net exposure
- Collateral

**Links to HC-L**: Derivatives counterparty exposure detail

### 6.5 Schedule E.2: CVA

Reports:
- Credit Valuation Adjustment by counterparty
- CVA reserves
- CVA capital

---

## 7. Pillar 3 Market Risk Templates

### 7.1 Overview

Basel III Pillar 3 requires public disclosure of market risk.

| Template | Content |
|----------|---------|
| MR1 | Market risk under IMA |
| MR2 | RWA flow statement |
| MR3 | IMA VaR values |
| MR4 | VaR comparison to P&L |

### 7.2 MR1: Market Risk Under Internal Models Approach

Reports:
- VaR-based capital
- Stressed VaR capital
- Incremental Risk Charge (IRC)
- Comprehensive Risk Measure (CRM)
- Total market risk capital

**Links to FR Y-9C**: Market risk capital in HC-R

### 7.3 MR3: IMA Values for Trading Portfolios

Reports daily VaR at 99%:
- Maximum, minimum, average
- Period-end value

**Links to FR Y-14Q**: Schedule G.2 VaR data

### 7.4 MR4: Comparison of VaR Estimates with Actual P&L

Backtesting disclosure:
- VaR vs actual P&L chart
- Number of exceptions
- Model performance assessment

---

## 8. Reconciliation Checks

### 8.1 Balance Sheet to Schedule HC-D

| Check | Formula | Must Equal |
|-------|---------|------------|
| Trading Assets | HC Item 5 = HC-D Item 12 | Exact match |
| Trading Liabilities | HC Item 15 = HC-D Item 15 | Exact match |

### 8.2 HC-D to HC-L (Derivatives)

| Check | Formula |
|-------|---------|
| Deriv Pos FV | HC-D Item 11 = Sum(HC-L Trading Pos FV) + Sum(HC-L Non-Trading Pos FV) |
| Deriv Neg FV | HC-D Item 14 = Sum(HC-L Trading Neg FV) + Sum(HC-L Non-Trading Neg FV) |

**Detailed**:
```
BHCT3543 = (BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736) +
           (BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744)

BHCT3547 = (BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740) +
           (BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748)
```

### 8.3 HC-D Internal Sums

| Check | Formula |
|-------|---------|
| Trading Assets | HC-D Item 12 = Items 1+2+3+4+5+6+9+11 |
| Trading Liabilities | HC-D Item 15 = Items 13+14 |

### 8.4 Common Discrepancies

| Issue | Cause | Resolution |
|-------|-------|------------|
| Small differences | Rounding | Accept if < $1M |
| Large differences | Reporting error | Flag for review |
| Missing data | Threshold | Bank may not report if below threshold |
| Historical breaks | Code changes | Check HISTORICAL_CODE_TRANSITIONS.csv |

---

## 9. Major Trading BHCs

### 9.1 Overview of G-SIB Trading Activity

The largest trading operations are concentrated in a few G-SIBs:

| BHC | Trading Assets ($B) | Derivatives Notional ($T) | Primary Focus |
|-----|---------------------|---------------------------|---------------|
| JPMorgan Chase | ~600 | ~55 | Universal |
| Goldman Sachs | ~450 | ~45 | Investment bank |
| Morgan Stanley | ~350 | ~35 | Investment bank |
| Bank of America | ~250 | ~40 | Universal |
| Citigroup | ~300 | ~45 | Universal |
| Wells Fargo | ~50 | ~10 | Commercial bank |

### 9.2 Trading Profile Differences

#### Investment Bank Focused (Goldman, Morgan Stanley)

- Trading assets ~30-40% of total assets
- Large equity and commodity trading
- Prime brokerage
- Lower deposit funding

#### Universal Bank (JPM, BAC, Citi)

- Trading assets ~15-20% of total assets
- Large interest rate derivatives (ALM)
- Significant FX operations
- Deposit-funded

#### Commercial Bank Focused (Wells Fargo)

- Trading assets ~3-5% of total assets
- Primarily interest rate hedging
- Limited market-making
- Deposit-funded

### 9.3 Key RSSD Identifiers

| BHC | RSSD ID | Lead Bank RSSD |
|-----|---------|----------------|
| JPMorgan Chase & Co. | 1039502 | 852218 (JPM Bank NA) |
| Goldman Sachs Group | 2380443 | 2182786 (GS Bank USA) |
| Morgan Stanley | 2162966 | 1456501 (MS Bank NA) |
| Bank of America Corp | 1073757 | 480228 (Bank of America NA) |
| Citigroup Inc. | 1951350 | 476810 (Citibank NA) |
| Wells Fargo & Co. | 1120754 | 451965 (Wells Fargo Bank NA) |

---

## 10. Appendix: Complete Code Tables

### 10.1 HC-D Complete Code Reference

See `HC_D_TRADING_ASSETS.csv` for complete listing.

### 10.2 HC-L Complete Code Reference

See `HC_L_DERIVATIVES.csv` for complete listing.

### 10.3 Cross-Reference Summary

| Concept | Y-9C MDRM | Call MDRM | HC-D Link | HC-L Link |
|---------|-----------|-----------|-----------|-----------|
| Total Trading Assets | BHCT3545 | RCFD3545 | Item 12 | - |
| Total Trading Liabilities | BHCT3548 | RCFD3548 | Item 15 | - |
| Derivatives Pos FV | BHCT3543 | RCFD3543 | Item 11 | Fair Value Section |
| Derivatives Neg FV | BHCT3547 | RCFD3547 | Item 14 | Fair Value Section |
| IR Swaps Notional | BHCK3450 | RCFD3450 | - | Notional Section |
| CDS Sold | BHCKC968 | RCFDC968 | - | Credit Deriv Section |
| CDS Bought | BHCKC969 | RCFDC969 | - | Credit Deriv Section |

### 10.4 Data Quality Checklist

Before using trading data, verify:

- [ ] Correct MDRM codes for time period
- [ ] Prefix matches desired scope (domestic vs consolidated)
- [ ] HC-D totals match HC balance sheet
- [ ] HC-L fair values sum to HC-D derivatives
- [ ] No unexpected zeros or missing values
- [ ] Historical code transitions handled

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-28 | N. Anderson | Initial trading activities guide |

---

**End of Trading Activities Guide**
