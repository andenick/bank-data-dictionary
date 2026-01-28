# Schedule HC-D: Trading Assets and Liabilities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-D - Trading Assets and Liabilities
**Frequency**: Quarterly
**Purpose**: Detail all trading book positions held at fair value

---

## Overview

Schedule HC-D provides the breakdown of trading positions summarized on the main balance sheet. Trading assets and liabilities are held at fair value with changes recognized in the income statement.

### Key Characteristics

- **Valuation**: Mark-to-market (fair value)
- **Intent**: Held for short-term profit, market-making, or customer facilitation
- **P&L Impact**: All gains/losses flow through income statement
- **Regulatory**: Subject to Volcker Rule limitations on proprietary trading

---

## Schedule Structure

```
TRADING ASSETS (Items 1-12)
├── Securities (Items 1-5)
│   ├── Item 1: U.S. Treasury securities
│   ├── Item 2: U.S. Government agency obligations
│   ├── Item 3: Municipal securities
│   ├── Item 4: Mortgage-backed securities
│   │   ├── 4.a.(1): GNMA residential pass-through
│   │   ├── 4.a.(2): FNMA/FHLMC residential pass-through
│   │   ├── 4.b: Other residential MBS
│   │   ├── 4.c.(1): Agency commercial MBS
│   │   └── 4.c.(2): Non-agency commercial MBS
│   └── Item 5: Other debt securities
│       ├── 5.a: Structured financial products
│       └── 5.b: Other debt (including ABS)
├── Loans (Item 6)
│   ├── 6.a: 1-4 family residential
│   ├── 6.b: Other real estate
│   ├── 6.c: Commercial and industrial
│   ├── 6.d: Consumer loans
│   └── 6.e: Other loans
├── Items 7-8: NOT IN USE
├── Item 9: Other trading assets
├── Item 10: NOT IN USE
├── Item 11: Derivatives positive fair value → Links to HC-L
└── Item 12: TOTAL TRADING ASSETS → Equals HC Item 5

TRADING LIABILITIES (Items 13-15)
├── Item 13: Short positions and other
│   ├── 13.a.(1): Equity short positions
│   ├── 13.a.(2): Debt short positions
│   ├── 13.a.(3): Other short positions
│   └── 13.b: Other trading liabilities
├── Item 14: Derivatives negative fair value → Links to HC-L
└── Item 15: TOTAL TRADING LIABILITIES → Equals HC Item 15
```

---

## Trading Assets Detail

### Item 1: U.S. Treasury Securities

| MDRM | Period | Description |
|------|--------|-------------|
| BHCM3531 | 2018+ | Treasury securities (domestic + foreign consolidated) |
| BHCK3531 | Pre-2018 | Treasury securities (legacy domestic only) |

**Risk**: Zero credit risk; interest rate risk only

### Item 2: U.S. Government Agency Obligations

| MDRM | Period | Description |
|------|--------|-------------|
| BHCM3532 | 2018+ | Agency securities (non-MBS) |
| BHCK3532 | Pre-2018 | Legacy code |

**Includes**: FNMA, FHLMC, FHLB, GNMA debt obligations (not MBS)

### Item 3: Municipal Securities

| MDRM | Period | Description |
|------|--------|-------------|
| BHCM3533 | 2018+ | States and political subdivisions |
| BHCK3533 | Pre-2018 | Legacy code |

### Item 4: Mortgage-Backed Securities

**Structure**:
```
Item 4: MBS Total
├── 4.a: Residential Pass-Through
│   ├── 4.a.(1) GNMA (BHCKK197)
│   └── 4.a.(2) FNMA/FHLMC (BHCKK198)
├── 4.b: Other Residential MBS (BHCKK199)
└── 4.c: Commercial MBS
    ├── 4.c.(1) Agency (BHCKK200)
    └── 4.c.(2) Non-Agency (BHCKK201)
```

| Line | MDRM | Description | Start Date |
|------|------|-------------|------------|
| 4.a.(1) | BHCKK197 | GNMA residential pass-through | 2011-03-31 |
| 4.a.(2) | BHCKK198 | FNMA/FHLMC residential pass-through | 2011-03-31 |
| 4.b | BHCKK199 | Non-agency residential MBS | 2011-03-31 |
| 4.c.(1) | BHCKK200 | Agency commercial MBS | 2011-03-31 |
| 4.c.(2) | BHCKK201 | Non-agency commercial MBS | 2011-03-31 |

### Item 5: Other Debt Securities

| Line | MDRM | Description | Start Date |
|------|------|-------------|------------|
| 5.a | BHCKHT62 | Structured financial products (CDOs, CLOs) | 2018-06-30 |
| 5.b | BHCKK202 | Other debt securities (including ABS) | 2011-03-31 |

### Item 6: Loans Held for Trading

| Line | MDRM | Description | Start Date |
|------|------|-------------|------------|
| 6.a | BHCKHT63 | 1-4 family residential loans | 2018-06-30 |
| 6.b | BHCKHT64 | Other real estate loans | 2018-06-30 |
| 6.c | BHCKF614 | Commercial and industrial loans | 2008-03-31 |
| 6.d | BHCKHT65 | Consumer loans | 2018-06-30 |
| 6.e | BHCKF618 | Other loans | 2008-03-31 |

### Item 9: Other Trading Assets

| MDRM | Period | Description |
|------|--------|-------------|
| BHCM3541 | 2018+ | Other trading assets |
| BHCK3541 | Pre-2018 | Legacy code |

**Includes**: Equity securities, precious metals, physical commodities, other

### Item 11: Derivatives with Positive Fair Value

| MDRM | Description | Links To |
|------|-------------|----------|
| BHCT3543 | Gross positive fair value of derivatives | HC-L Fair Value items |

**Reconciliation to HC-L**:
```
BHCT3543 = Trading Positive FV + Non-Trading Positive FV
         = (BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736)
         + (BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744)
```

### Item 12: Total Trading Assets

| MDRM | Description | Ties To |
|------|-------------|---------|
| BHCT3545 | Total trading assets | HC Item 5 |

**Reconciliation**:
```
Item 12 = Items 1 + 2 + 3 + 4 + 5 + 6 + 9 + 11
Schedule HC Item 5 = HC-D Item 12
```

---

## Trading Liabilities Detail

### Item 13: Short Positions and Other

| Line | MDRM | Description | Start Date |
|------|------|-------------|------------|
| 13.a.(1) | BHCKG209 | Short positions - equity securities | 2009-03-31 |
| 13.a.(2) | BHCKG210 | Short positions - debt securities | 2009-03-31 |
| 13.a.(3) | BHCKG211 | Short positions - other assets | 2009-03-31 |
| 13.b | BHCKF624 | Other trading liabilities | 2008-03-31 |

**Short Positions**: Securities sold short but not yet purchased; obligation to deliver

### Item 14: Derivatives with Negative Fair Value

| MDRM | Description | Links To |
|------|-------------|----------|
| BHCT3547 | Gross negative fair value of derivatives | HC-L Fair Value items |

**Reconciliation to HC-L**:
```
BHCT3547 = Trading Negative FV + Non-Trading Negative FV
         = (BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740)
         + (BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748)
```

### Item 15: Total Trading Liabilities

| MDRM | Description | Ties To |
|------|-------------|---------|
| BHCT3548 | Total trading liabilities | HC Item 15 |

**Reconciliation**:
```
Item 15 = Items 13 + 14
Schedule HC Item 15 = HC-D Item 15
```

---

## Key Reconciliation Rules

### Schedule HC Balance Sheet

```
HC Item 5 (Trading Assets) = HC-D Item 12 (BHCT3545)
HC Item 15 (Trading Liabs) = HC-D Item 15 (BHCT3548)
```

### Schedule HC-L Derivatives

```
HC-D Item 11 (Deriv Pos FV) = Sum of HC-L positive fair value items
HC-D Item 14 (Deriv Neg FV) = Sum of HC-L negative fair value items
```

### Internal Consistency

```
Item 12 = Sum(Items 1,2,3,4,5,6,9,11)
Item 15 = Sum(Items 13,14)
```

---

## Analytical Considerations

### Trading Intensity

```
Trading Intensity = (Trading Assets + Trading Liabilities) / Total Assets
- Investment banks: 30-50%
- Universal banks: 15-25%
- Regional/commercial banks: <5%
```

### Net Trading Position

```
Net Trading Position = Trading Assets - Trading Liabilities
                     = BHCT3545 - BHCT3548
```

### Derivatives as % of Trading

```
Derivatives Share = (Item 11 + Item 14) / (Item 12 + Item 15)
```

---

## Historical Evolution

| Date | Change |
|------|--------|
| 1989-09-30 | Initial trading liability reporting |
| 1995-12-31 | Enhanced trading assets reporting |
| 2008-03-31 | Loan trading detail added (F614, F618) |
| 2009-03-31 | Short position breakout (G209-G211) |
| 2011-03-31 | MBS granular detail (K197-K202) |
| 2018-06-30 | Structured products and loan detail (HT62-HT65) |

---

## MDRM Quick Reference

| Line | MDRM | Description |
|------|------|-------------|
| 1 | BHCM3531 | Treasury securities |
| 2 | BHCM3532 | Agency securities |
| 3 | BHCM3533 | Municipal securities |
| 4.a.(1) | BHCKK197 | GNMA MBS |
| 4.a.(2) | BHCKK198 | FNMA/FHLMC MBS |
| 4.b | BHCKK199 | Other residential MBS |
| 4.c.(1) | BHCKK200 | Agency CMBS |
| 4.c.(2) | BHCKK201 | Non-agency CMBS |
| 5.a | BHCKHT62 | Structured products |
| 5.b | BHCKK202 | Other debt securities |
| 6.c | BHCKF614 | C&I loans (trading) |
| 9 | BHCM3541 | Other trading assets |
| 11 | BHCT3543 | Derivatives positive FV |
| **12** | **BHCT3545** | **TOTAL TRADING ASSETS** |
| 13.a.(1) | BHCKG209 | Short equity |
| 13.a.(2) | BHCKG210 | Short debt |
| 13.b | BHCKF624 | Other trading liabilities |
| 14 | BHCT3547 | Derivatives negative FV |
| **15** | **BHCT3548** | **TOTAL TRADING LIABS** |

---

*See also*: [Trading Activities Deep Dive](TRADING_ACTIVITIES_GUIDE.md) for comprehensive HC-D and HC-L analysis

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
