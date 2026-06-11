# Market Risk & Trading Book Complete Guide

This guide provides comprehensive documentation of all market risk and trading book components in the FR Y-9C, including complete hierarchies, MDRM codes, and cross-schedule reconciliations.

## Table of Contents

1. [Trading Revenue Hierarchy](#1-trading-revenue-hierarchy)
2. [Trading Assets Hierarchy](#2-trading-assets-hierarchy)
3. [Trading Liabilities Hierarchy](#3-trading-liabilities-hierarchy)
4. [Derivatives Notional by Asset Class](#4-derivatives-notional-by-asset-class)
5. [Derivatives Fair Value Decomposition](#5-derivatives-fair-value-decomposition)
6. [Credit Derivatives Detail](#6-credit-derivatives-detail)
7. [Market Risk Capital](#7-market-risk-capital)
8. [Cross-Schedule Reconciliation Map](#8-cross-schedule-reconciliation-map)
9. [Risk Type Classification](#9-risk-type-classification)
10. [Analysis Examples](#10-analysis-examples)

---

## 1. Trading Revenue Hierarchy

**Schedule HI Item 6.b / HI-Memoranda Item 7**

Trading revenue captures mark-to-market gains and losses from the trading book, broken down by underlying risk factor.

### Complete Hierarchy

```
BHCKA220 (Total Trading Revenue) = HI Item 6.b
│
├── BHCKA221: Interest Rate Trading Revenue
│   └── P&L from: IR swaps, futures, options, bond trading
│
├── BHCKA222: Foreign Exchange Trading Revenue
│   └── P&L from: Spot, forwards, FX swaps, FX options
│
├── BHCKA223: Equity Trading Revenue
│   └── P&L from: Cash equities, equity derivatives
│
├── BHCKA224: Commodity Trading Revenue
│   └── P&L from: Precious metals, energy, agriculture
│
└── BHCKF186: Credit Trading Revenue (added 2018)
    └── P&L from: CDS, TRS, credit-linked notes
```

### MDRM Code Reference

| Product | MDRM | Call Report | Description |
|---------|------|-------------|-------------|
| **Total** | BHCKA220 | RIADA220 | Sum of all trading revenue |
| Interest Rate | BHCKA221 | RIAD8757 | IR instruments P&L |
| Foreign Exchange | BHCKA222 | RIAD8758 | FX instruments P&L |
| Equity | BHCKA223 | RIAD8759 | Equity instruments P&L |
| Commodity | BHCKA224 | RIAD8760 | Commodity instruments P&L |
| Credit | BHCKF186 | RIADF186 | Credit instruments P&L |

### Reconciliation Formula

```
BHCKA220 = BHCKA221 + BHCKA222 + BHCKA223 + BHCKA224 + BHCKF186
```

### Notes

- Trading revenue is a component of noninterest income (HI Item 6)
- Credit trading revenue (BHCKF186) was added Q2 2018; prior to that, credit trading was embedded in other categories
- Revenue includes both realized and unrealized gains/losses
- Does not include interest income on trading assets (that's in HI Item 1.e: BHCK4069)

---

## 2. Trading Assets Hierarchy

**Schedule HC-D / Schedule HC Item 5**

Trading assets represent instruments held in the trading book, measured at fair value through income.

### Complete Hierarchy

```
BHCT3545 (Total Trading Assets) = HC Item 5 = HC-D Item 12
│
├── SECURITIES (Items 1-5)
│   │
│   ├── BHCM3531: U.S. Treasury Securities
│   │   └── Risk: Duration/IR; RW: 0%
│   │
│   ├── BHCM3532: U.S. Government Agency Obligations
│   │   └── Risk: Duration/IR; RW: 20%
│   │
│   ├── BHCM3533: Municipal Securities
│   │   └── Risk: Duration/IR + Credit spread
│   │
│   ├── MBS BREAKDOWN (Item 4)
│   │   ├── BHCKK197: GNMA RMBS Pass-Through
│   │   ├── BHCKK198: FNMA/FHLMC RMBS Pass-Through
│   │   ├── BHCKK199: Other Residential MBS (non-agency)
│   │   ├── BHCKK200: Agency Commercial MBS
│   │   └── BHCKK201: Other Commercial MBS (non-agency)
│   │
│   └── OTHER DEBT (Item 5)
│       ├── BHCKHT62: Structured Financial Products (CDO/CLO)
│       └── BHCKK202: Other Debt Securities (ABS, corporates)
│
├── TRADING LOANS (Item 6)
│   ├── BHCKHT63: 1-4 Family Residential Loans
│   ├── BHCKHT64: Other Real Estate Loans
│   ├── BHCKF614: Commercial & Industrial Loans
│   ├── BHCKHT65: Consumer Loans
│   └── BHCKF618: Other Loans
│
├── BHCM3541: Other Trading Assets (Item 9)
│   └── Residual category
│
└── BHCT3543: Derivatives with Positive Fair Value (Item 11)
    │
    ├── TRADING DERIVATIVES (from HC-L)
    │   ├── BHCK8733: Interest Rate Positive FV
    │   ├── BHCK8734: Foreign Exchange Positive FV
    │   ├── BHCK8735: Equity Positive FV
    │   └── BHCK8736: Commodity Positive FV
    │
    └── NON-TRADING DERIVATIVES (from HC-L)
        ├── BHCK8741: Interest Rate Positive FV
        ├── BHCK8742: Foreign Exchange Positive FV
        ├── BHCK8743: Equity Positive FV
        └── BHCK8744: Commodity Positive FV
```

### MDRM Code Reference - Securities

| Item | MDRM | Description | Risk Type |
|------|------|-------------|-----------|
| 1 | BHCM3531 | U.S. Treasury securities | IR |
| 2 | BHCM3532 | U.S. Agency obligations | IR |
| 3 | BHCM3533 | Municipal securities | IR/Credit |
| 4.a.(1) | BHCKK197 | GNMA RMBS | IR/Prepay |
| 4.a.(2) | BHCKK198 | FNMA/FHLMC RMBS | IR/Prepay |
| 4.b | BHCKK199 | Other RMBS | Credit/Prepay |
| 4.c.(1) | BHCKK200 | Agency CMBS | IR/Credit |
| 4.c.(2) | BHCKK201 | Other CMBS | Credit |
| 5.a | BHCKHT62 | Structured products | Credit |
| 5.b | BHCKK202 | Other debt/ABS | Credit |

### MDRM Code Reference - Loans

| Item | MDRM | Description | Risk Type |
|------|------|-------------|-----------|
| 6.a | BHCKHT63 | 1-4 Family RE | Credit/Prepay |
| 6.b | BHCKHT64 | Other RE | Credit |
| 6.c | BHCKF614 | C&I Loans | Credit |
| 6.d | BHCKHT65 | Consumer Loans | Credit |
| 6.e | BHCKF618 | Other Loans | Credit |

### Reconciliation Formula

```
BHCT3545 = BHCM3531 + BHCM3532 + BHCM3533
         + BHCKK197 + BHCKK198 + BHCKK199 + BHCKK200 + BHCKK201
         + BHCKHT62 + BHCKK202
         + BHCKHT63 + BHCKHT64 + BHCKF614 + BHCKHT65 + BHCKF618
         + BHCM3541 + BHCT3543
```

---

## 3. Trading Liabilities Hierarchy

**Schedule HC-D / Schedule HC Item 15**

Trading liabilities represent obligations arising from trading activities.

### Complete Hierarchy

```
BHCT3548 (Total Trading Liabilities) = HC Item 15 = HC-D Item 15
│
├── SHORT POSITIONS (Item 13)
│   │
│   ├── BHCKG209: Short Equity Positions
│   │   └── Obligations to deliver equities sold short
│   │
│   ├── BHCKG210: Short Debt Positions
│   │   └── Obligations to deliver bonds sold short
│   │
│   ├── BHCKG211: Short Other Positions
│   │   └── Commodity and other short sales
│   │
│   └── BHCKF624: Other Trading Liabilities
│       └── Residual category
│
└── BHCT3547: Derivatives with Negative Fair Value (Item 14)
    │
    ├── TRADING DERIVATIVES (from HC-L)
    │   ├── BHCK8737: Interest Rate Negative FV
    │   ├── BHCK8738: Foreign Exchange Negative FV
    │   ├── BHCK8739: Equity Negative FV
    │   └── BHCK8740: Commodity Negative FV
    │
    └── NON-TRADING DERIVATIVES (from HC-L)
        ├── BHCK8745: Interest Rate Negative FV
        ├── BHCK8746: Foreign Exchange Negative FV
        ├── BHCK8747: Equity Negative FV
        └── BHCK8748: Commodity Negative FV
```

### MDRM Code Reference

| Item | MDRM | Description |
|------|------|-------------|
| 13.a.(1) | BHCKG209 | Short equity positions |
| 13.a.(2) | BHCKG210 | Short debt positions |
| 13.a.(3) | BHCKG211 | Short other positions |
| 13.b | BHCKF624 | Other trading liabilities |
| 14 | BHCT3547 | Derivatives negative FV |
| **15** | **BHCT3548** | **Total trading liabilities** |

### Reconciliation Formula

```
BHCT3548 = BHCKG209 + BHCKG210 + BHCKG211 + BHCKF624 + BHCT3547
```

---

## 4. Derivatives Notional by Asset Class

**Schedule HC-L**

Notional amounts represent the underlying value upon which derivative payments are calculated.

### Interest Rate Derivatives

| Instrument | Venue | MDRM | Call Report |
|------------|-------|------|-------------|
| Futures | Exchange | BHCK8693 | RCFD8693 |
| Forwards | OTC | BHCK8697 | RCFD8697 |
| Swaps | OTC | BHCK3450 | RCFD3450 |
| Options Written | Exchange | BHCK8701 | RCFD8701 |
| Options Purchased | Exchange | BHCK8705 | RCFD8705 |
| Options Written | OTC | BHCK8709 | RCFD8709 |
| Options Purchased | OTC | BHCK8713 | RCFD8713 |

### Foreign Exchange Derivatives

| Instrument | Venue | MDRM | Call Report |
|------------|-------|------|-------------|
| Futures | Exchange | BHCK8694 | RCFD8694 |
| Forwards | OTC | BHCK8698 | RCFD8698 |
| Swaps | OTC | BHCK3826 | RCFD3826 |
| Options Written | Exchange | BHCK8702 | RCFD8702 |
| Options Purchased | Exchange | BHCK8706 | RCFD8706 |
| Options Written | OTC | BHCK8710 | RCFD8710 |
| Options Purchased | OTC | BHCK8714 | RCFD8714 |

### Equity Derivatives

| Instrument | Venue | MDRM | Call Report |
|------------|-------|------|-------------|
| Futures | Exchange | BHCK8695 | RCFD8695 |
| Forwards | OTC | BHCK8699 | RCFD8699 |
| Swaps | OTC | BHCK8719 | RCFD8719 |
| Options Written | Exchange | BHCK8703 | RCFD8703 |
| Options Purchased | Exchange | BHCK8707 | RCFD8707 |
| Options Written | OTC | BHCK8711 | RCFD8711 |
| Options Purchased | OTC | BHCK8715 | RCFD8715 |

### Commodity Derivatives

| Instrument | Venue | MDRM | Call Report |
|------------|-------|------|-------------|
| Futures | Exchange | BHCK8696 | RCFD8696 |
| Forwards | OTC | BHCK8700 | RCFD8700 |
| Swaps | OTC | BHCK8720 | RCFD8720 |
| Options Written | Exchange | BHCK8704 | RCFD8704 |
| Options Purchased | Exchange | BHCK8708 | RCFD8708 |
| Options Written | OTC | BHCK8712 | RCFD8712 |
| Options Purchased | OTC | BHCK8716 | RCFD8716 |

### Notional Summary by Asset Class

```
IR Total = 8693 + 8697 + 3450 + 8701 + 8705 + 8709 + 8713
FX Total = 8694 + 8698 + 3826 + 8702 + 8706 + 8710 + 8714
EQ Total = 8695 + 8699 + 8719 + 8703 + 8707 + 8711 + 8715
CO Total = 8696 + 8700 + 8720 + 8704 + 8708 + 8712 + 8716
```

---

## 5. Derivatives Fair Value Decomposition

**Schedule HC-L Fair Value Section**

Fair values represent the balance sheet carrying value of derivative positions.

### Trading Derivatives - Positive Fair Value

These sum to HC-D Item 11 (BHCT3543)

| Asset Class | MDRM | Description |
|-------------|------|-------------|
| Interest Rate | BHCK8733 | IR trading positive FV |
| Foreign Exchange | BHCK8734 | FX trading positive FV |
| Equity | BHCK8735 | Equity trading positive FV |
| Commodity | BHCK8736 | Commodity trading positive FV |

```
BHCT3543 (Trading Positive FV) = BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736
                                + BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744
```

### Trading Derivatives - Negative Fair Value

These sum to HC-D Item 14 (BHCT3547)

| Asset Class | MDRM | Description |
|-------------|------|-------------|
| Interest Rate | BHCK8737 | IR trading negative FV |
| Foreign Exchange | BHCK8738 | FX trading negative FV |
| Equity | BHCK8739 | Equity trading negative FV |
| Commodity | BHCK8740 | Commodity trading negative FV |

```
BHCT3547 (Trading Negative FV) = BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740
                                + BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748
```

### Non-Trading (Hedging) Derivatives - Positive Fair Value

Included in HC Item 11 (Other Assets) via HC-F

| Asset Class | MDRM | Description |
|-------------|------|-------------|
| Interest Rate | BHCK8741 | IR hedging positive FV |
| Foreign Exchange | BHCK8742 | FX hedging positive FV |
| Equity | BHCK8743 | Equity hedging positive FV |
| Commodity | BHCK8744 | Commodity hedging positive FV |

### Non-Trading (Hedging) Derivatives - Negative Fair Value

Included in HC Item 20 (Other Liabilities) via HC-G

| Asset Class | MDRM | Description |
|-------------|------|-------------|
| Interest Rate | BHCK8745 | IR hedging negative FV |
| Foreign Exchange | BHCK8746 | FX hedging negative FV |
| Equity | BHCK8747 | Equity hedging negative FV |
| Commodity | BHCK8748 | Commodity hedging negative FV |

---

## 6. Credit Derivatives Detail

**Schedule HC-L Credit Derivatives Section**

Credit derivatives transfer credit risk between counterparties.

### By Position

| Position | Instrument | MDRM | Description |
|----------|------------|------|-------------|
| Guarantor (Sold) | CDS | BHCKC968 | Protection sold - takes credit risk |
| Beneficiary (Bought) | CDS | BHCKC969 | Protection bought - sheds credit risk |
| Guarantor (Sold) | TRS | BHCKC970 | Total return swap - sold |
| Beneficiary (Bought) | TRS | BHCKC971 | Total return swap - bought |
| Guarantor (Sold) | Other | BHCKC974 | Other credit derivatives - sold |
| Beneficiary (Bought) | Other | BHCKC975 | Other credit derivatives - bought |

### Net Credit Protection

```
Net Protection = (C969 + C971 + C975) - (C968 + C970 + C974)
```

- **Positive** = Net buyer of protection (reduced credit exposure)
- **Negative** = Net seller of protection (increased credit exposure)

### Credit Derivatives Considerations

- Protection sellers (guarantors) are similar to writing insurance on credit
- Large net sold positions indicate significant credit risk exposure
- CDS notional typically >> fair value (leverage)
- TRS transfers both credit and market risk

---

## 7. Market Risk Capital

**Schedule HC-R Part II**

Market risk capital requirements apply to trading book positions.

### Risk-Weighted Asset Components

| Component | MDRM | Description | Capital Impact |
|-----------|------|-------------|----------------|
| 0% RW | BHCKA221 | Cash, Treasuries | Minimal |
| 20% RW | BHCKS396 | GSE, munis, interbank | Low |
| 50% RW | BHCKS397 | Residential mortgages | Medium |
| 100% RW | BHCKS398 | C&I, CRE, most loans | Standard |
| 150% RW | BHCKS399 | HVCRE, non-IG | High |
| Securitization | BHCKS400 | ABS, MBS positions | Variable |
| Equity | - | Equity exposures (computed across risk-weight bands; no single MDRM code) | High |
| Derivatives | BHCKS402 | CCR from derivatives | Variable |
| OBS | BHCKS403 | Commitments, guarantees | CCF applied |
| **Market Risk** | **BHCKA222** | **Trading book RWA** | **VaR-based** |
| **Total RWA** | **BHCAA223** | **Sum of all components** | - |

### Market Risk RWA Hierarchy

```
BHCAA223 (Total RWA)
│
├── Credit Risk RWA
│   ├── BHCKA221: 0% risk weight
│   ├── BHCKS396: 20% risk weight
│   ├── BHCKS397: 50% risk weight
│   ├── BHCKS398: 100% risk weight
│   ├── BHCKS399: 150% risk weight
│   ├── BHCKS400: Securitization RWA
│   ├── Equity RWA (computed; no single code)
│   ├── BHCKS402: Derivatives CCR RWA
│   └── BHCKS403: Off-balance sheet RWA
│
└── BHCKA222: Market Risk RWA
    ├── VaR-based capital (10-day, 99%)
    ├── Stressed VaR capital (10-day, 99%, stressed period)
    ├── Incremental Risk Charge (credit migration + default)
    └── Comprehensive Risk Measure (correlation trading)
```

### Capital Ratios

| Ratio | MDRM | Formula |
|-------|------|---------|
| CET1 Ratio | BHCAP793 | BHCAP859 / BHCAA223 |
| Tier 1 Ratio | BHCA7206 | BHCA8274 / BHCAA223 |
| Total Capital Ratio | BHCA7205 | BHCA3792 / BHCAA223 |
| Leverage Ratio | BHCA7204 | BHCA8274 / Avg Assets |

### Regulatory Minimums (Basel III)

| Ratio | Minimum | Well-Capitalized |
|-------|---------|------------------|
| CET1 | 4.5% | 6.5% |
| Tier 1 | 6.0% | 8.0% |
| Total Capital | 8.0% | 10.0% |
| Leverage | 4.0% | 5.0% |

---

## 8. Cross-Schedule Reconciliation Map

### Balance Sheet Tie-Outs

```
SCHEDULE HC (Balance Sheet)
│
├── Item 5: Trading Assets ═══════════════════ HC-D Item 12 (BHCT3545)
│   │                                          │
│   │                                          ├─ Securities: Items 1-5
│   │                                          ├─ Loans: Item 6
│   │                                          ├─ Other: Item 9
│   │                                          └─ Derivatives: Item 11 ═══ HC-L Fair Value (+)
│   │
├── Item 15: Trading Liabilities ═════════════ HC-D Item 15 (BHCT3548)
│   │                                          │
│   │                                          ├─ Short positions: Item 13
│   │                                          └─ Derivatives: Item 14 ═══ HC-L Fair Value (-)
│   │
├── Item 11: Other Assets ════════════════════ HC-F Item 12
│   │                                          └─ Includes non-trading deriv (+)
│   │
├── Item 20: Other Liabilities ═══════════════ HC-G Item 5
│   │                                          └─ Includes non-trading deriv (-)
│   │
└── Item 28: Total Equity ════════════════════ HC-R Part I
                                               └─ Capital adequacy
```

### Income Statement Tie-Outs

```
SCHEDULE HI (Income Statement)
│
├── Item 1.e: Interest on Trading Assets ═════ BHCK4069
│
├── Item 2.c: Interest on Trading Liabilities  BHCK4185
│
├── Item 6.b: Trading Revenue ════════════════ HI-M Items 7.a-7.e
│   │
│   ├── BHCKA221: Interest Rate P&L
│   ├── BHCKA222: Foreign Exchange P&L
│   ├── BHCKA223: Equity P&L
│   ├── BHCKA224: Commodity P&L
│   └── BHCKF186: Credit P&L
│   │
│   └────────────────────────────────────────── Reflects: HC-D & HC-L changes
│
└── Item 12: Net Income ═════════════════════ Retained Earnings flow
```

### Capital Linkage

```
HC-R (Regulatory Capital)
│
├── Part I: Capital Components
│   ├── CET1 (BHCAP859)
│   ├── Tier 1 (BHCA8274)
│   └── Total Capital (BHCA3792)
│
└── Part II: Risk-Weighted Assets
    ├── Credit RWA (by risk weight bucket)
    ├── Market Risk RWA (BHCKA222) ═══════════ Trading book capital
    │   │
    │   └── Captures risk from:
    │       ├── HC-D: Trading asset positions
    │       ├── HC-L: Derivatives notional/FV
    │       └── HI: Trading revenue volatility
    │
    └── Total RWA (BHCAA223)
```

### Verification Checks

| Check | Formula | Expected |
|-------|---------|----------|
| Trading Assets | HC Item 5 = HC-D Item 12 | Equal |
| Trading Liabilities | HC Item 15 = HC-D Item 15 | Equal |
| Deriv Positive FV | HC-D Item 11 = Sum(HC-L positive) | Equal |
| Deriv Negative FV | HC-D Item 14 = Sum(HC-L negative) | Equal |
| Trading Revenue | HI Item 6.b = Sum(HI-M components) | Equal |
| RWA | HC-R Total = Sum(RW buckets + Market) | Equal |

---

## 9. Risk Type Classification

### Market Risk Factors

| Risk Type | Description | Affected Items |
|-----------|-------------|----------------|
| **Interest Rate** | Changes in yield curves | Treasuries, agencies, MBS, IR derivatives |
| **Foreign Exchange** | Currency movements | FX forwards, swaps, options |
| **Equity** | Stock price changes | Equity positions, equity derivatives |
| **Commodity** | Commodity price changes | Commodity derivatives, precious metals |
| **Credit Spread** | Credit spreads widening/tightening | Corporate bonds, CDS, structured products |
| **Prepayment** | Mortgage prepayment speeds | MBS, mortgage loans |
| **Basis** | Imperfect hedge correlations | All hedged positions |
| **Volatility** | Implied vol changes | All options |

### Trading Book vs Banking Book

| Attribute | Trading Book | Banking Book |
|-----------|--------------|--------------|
| Intent | Short-term trading | Hold to maturity/investment |
| Measurement | Fair value through P&L | Amortized cost or FVOCI |
| Capital | Market risk RWA | Credit risk RWA |
| Schedule | HC-D, HC-L | HC-B, HC-C |
| Revenue | Trading revenue (HI 6.b) | Net interest income |

---

## 10. Analysis Examples

### Example 1: Calculate Net Trading Position

```python
# Net trading position = Assets - Liabilities
trading_assets = df['BHCT3545']     # Total trading assets
trading_liabs = df['BHCT3548']       # Total trading liabilities

net_trading = trading_assets - trading_liabs
```

### Example 2: Derivatives Leverage Ratio

```python
# Compare notional to fair value
ir_notional = (df['BHCK8693'] + df['BHCK8697'] + df['BHCK3450'] +
               df['BHCK8701'] + df['BHCK8705'] + df['BHCK8709'] + df['BHCK8713'])

ir_fair_value_net = df['BHCK8733'] - df['BHCK8737']  # Positive - Negative

ir_leverage = ir_notional / abs(ir_fair_value_net)
# Typical leverage: 50x-100x for IR swaps
```

### Example 3: Trading Revenue Breakdown

```python
# Revenue contribution by product
total_trading_rev = df['BHCKA220']

pct_ir = df['BHCKA221'] / total_trading_rev * 100
pct_fx = df['BHCKA222'] / total_trading_rev * 100
pct_eq = df['BHCKA223'] / total_trading_rev * 100
pct_co = df['BHCKA224'] / total_trading_rev * 100
pct_cr = df['BHCKF186'] / total_trading_rev * 100
```

### Example 4: Market Risk Capital Intensity

```python
# Market risk as % of total RWA
market_risk_rwa = df['BHCKA222']
total_rwa = df['BHCAA223']

market_risk_intensity = market_risk_rwa / total_rwa * 100
# Banks with large trading: 5-15%
# Traditional banks: < 2%
```

### Example 5: Credit Derivative Position

```python
# Net CDS position
cds_sold = df['BHCKC968']    # Protection sold = long credit
cds_bought = df['BHCKC969']  # Protection bought = short credit

net_cds = cds_bought - cds_sold
# Positive = Net protection buyer (hedging)
# Negative = Net protection seller (risk taking)
```

---

## Appendix: Complete MDRM Quick Reference

### Trading Revenue
- BHCKA220: Total
- BHCKA221: IR
- BHCKA222: FX
- BHCKA223: Equity
- BHCKA224: Commodity
- BHCKF186: Credit

### Trading Assets (HC-D)
- BHCT3545: Total
- BHCT3543: Derivatives (+)
- BHCM3531-3533: Securities
- BHCKK197-K202: MBS/ABS
- BHCKHT62-65, F614, F618: Loans
- BHCM3541: Other

### Trading Liabilities (HC-D)
- BHCT3548: Total
- BHCT3547: Derivatives (-)
- BHCKG209-211: Short positions
- BHCKF624: Other

### Derivatives Notional (HC-L)
- 8693-8716: By product/venue (28 items)
- C968-C975: Credit derivatives (6 items)
- 3450, 3826: IR/FX swaps

### Derivatives Fair Value (HC-L)
- 8733-8736: Trading positive
- 8737-8740: Trading negative
- 8741-8744: Non-trading positive
- 8745-8748: Non-trading negative

### Capital (HC-R)
- BHCAA223: Total RWA
- BHCKA222: Market Risk RWA
- BHCAP859: CET1
- BHCA8274: Tier 1
- BHCA3792: Total Capital

---

*This guide consolidates all market risk and trading book components from the FR Y-9C for comprehensive trading analysis.*
