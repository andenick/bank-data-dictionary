# Schedule HC-L: Derivatives and Off-Balance Sheet Items Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-L - Derivatives and Off-Balance Sheet Items
**Frequency**: Quarterly
**Purpose**: Detail derivative positions (notional and fair value) and off-balance sheet exposures

---

## Overview

Schedule HC-L is the primary schedule for derivatives reporting, providing:
- **Notional amounts** by product type and asset class
- **Fair values** (positive and negative) by asset class
- **Off-balance sheet commitments** (unfunded commitments, letters of credit, etc.)

### Key Distinction: Notional vs. Fair Value

| Measure | Definition | Balance Sheet Impact |
|---------|------------|---------------------|
| **Notional** | Face/principal amount of contract | None (off-balance sheet) |
| **Fair Value** | Current mark-to-market value | On balance sheet (HC-D Items 11/14) |

Typical relationship: Fair Value << 5% of Notional

---

## Schedule Structure

The current FR Y-9C HC-L is a single numbered schedule (items 1-15, plus memoranda). The CSV
is keyed by `line_number` and `column` to reflect the official grid. Off-balance-sheet items come
first (1-9); derivatives notional, totals, fair values, and credit exposure follow (7, 11-15).

```
OFF-BALANCE-SHEET (items 1-9)
├── 1. Unused commitments (1.a HELOC, 1.b credit cards, 1.c CRE/construction,
│        1.d underwriting, 1.e other incl. new 2026Q1 nondepository-FI breakout PV10-PV16)
├── 2. Financial standby letters of credit (+ 2.a conveyed)
├── 3. Performance standby letters of credit (+ 3.a conveyed)
├── 4. Commercial and similar letters of credit
├── 6. Securities lent (6.a) / borrowed (6.b)
├── 7. Credit derivatives (notional sold/bought, gross FV, by maturity & rating)
├── 8. Spot foreign exchange contracts
└── 9. All other off-balance-sheet items (+ itemized 9.a-9.f)

DERIVATIVES (items 11-15), columns A=Interest Rate, B=Foreign Exchange, C=Equity, D=Commodity/Other
├── 11. Notional by instrument (futures, forwards, options, swaps)
├── 12. Total gross notional held for trading
├── 13. Total gross notional held for purposes other than trading
├── 14. Gross positive/negative fair value (a = trading, b = non-trading) -> HC-D items 11/14
└── 15. OTC derivatives net current credit exposure (15.a) and fair value of collateral (15.b),
        columns A-E by counterparty type (banks/securities firms, monoline guarantors,
        hedge funds, sovereign governments, corporations and all other)
```

---

## Part I: Derivatives - Notional Amounts

### Interest Rate Derivatives

| Product | MDRM | Call MDRM | Description |
|---------|------|-----------|-------------|
| Futures | BHCK8693 | RCFD8693 | Exchange-traded IR futures |
| Forwards | BHCK8697 | RCFD8697 | OTC IR forwards (FRAs) |
| Swaps | BHCK3450 | RCFD3450 | Interest rate swaps |
| Options Written (Exchange) | BHCK8701 | RCFD8701 | Sold IR options |
| Options Purchased (Exchange) | BHCK8705 | RCFD8705 | Bought IR options |
| Options Written (OTC) | BHCK8709 | RCFD8709 | Sold IR swaptions/caps |
| Options Purchased (OTC) | BHCK8713 | RCFD8713 | Bought IR swaptions/caps |

**Interest Rate Swaps (BHCK3450)**: Largest category by notional; G-SIBs have $40-50 trillion each.

### Foreign Exchange Derivatives

| Product | MDRM | Call MDRM | Description |
|---------|------|-----------|-------------|
| Futures | BHCK8694 | RCFD8694 | Exchange-traded FX futures |
| Forwards | BHCK8698 | RCFD8698 | FX forwards (spots > 2 days) |
| Swaps | BHCK3826 | RCFD3826 | Cross-currency swaps |
| Options Written (Exchange) | BHCK8702 | RCFD8702 | |
| Options Purchased (Exchange) | BHCK8706 | RCFD8706 | |
| Options Written (OTC) | BHCK8710 | RCFD8710 | |
| Options Purchased (OTC) | BHCK8714 | RCFD8714 | |

### Equity Derivatives

| Product | MDRM | Call MDRM | Description |
|---------|------|-----------|-------------|
| Futures | BHCK8695 | RCFD8695 | Index futures, single stock |
| Forwards | BHCK8699 | RCFD8699 | Equity forwards |
| Swaps | BHCK8719 | RCFD8719 | Total return swaps on equity |
| Options Written (Exchange) | BHCK8703 | RCFD8703 | |
| Options Purchased (Exchange) | BHCK8707 | RCFD8707 | |
| Options Written (OTC) | BHCK8711 | RCFD8711 | |
| Options Purchased (OTC) | BHCK8715 | RCFD8715 | |

### Commodity Derivatives

| Product | MDRM | Call MDRM | Description |
|---------|------|-----------|-------------|
| Futures | BHCK8696 | RCFD8696 | Oil, gold, agricultural |
| Forwards | BHCK8700 | RCFD8700 | Commodity forwards |
| Swaps | BHCK8720 | RCFD8720 | Commodity swaps |
| Options Written (Exchange) | BHCK8704 | RCFD8704 | |
| Options Purchased (Exchange) | BHCK8708 | RCFD8708 | |
| Options Written (OTC) | BHCK8712 | RCFD8712 | |
| Options Purchased (OTC) | BHCK8716 | RCFD8716 | |

### Credit Derivatives

| Product | Position | MDRM | Call MDRM |
|---------|----------|------|-----------|
| CDS | Protection Sold (Guarantor) | BHCKC968 | RCFDC968 |
| CDS | Protection Bought (Beneficiary) | BHCKC969 | RCFDC969 |
| TRS | Protection Sold | BHCKC970 | RCFDC970 |
| TRS | Protection Bought | BHCKC971 | RCFDC971 |
| Other | Protection Sold | BHCKC974 | RCFDC974 |
| Other | Protection Bought | BHCKC975 | RCFDC975 |

**Net CDS Position**:
```
Net CDS Exposure = Protection Bought - Protection Sold
                 = BHCKC969 - BHCKC968
Positive = Net buyer of protection (hedged/risk-off)
Negative = Net seller of protection (risk-on)
```

---

## Part I: Derivatives - Fair Values

### Trading Derivatives - Positive Fair Value

| Asset Class | MDRM | Call MDRM | Links To |
|-------------|------|-----------|----------|
| Interest Rate | BHCK8733 | RCFD8733 | HC-D Item 11 |
| Foreign Exchange | BHCK8734 | RCFD8734 | HC-D Item 11 |
| Equity | BHCK8735 | RCFD8735 | HC-D Item 11 |
| Commodity | BHCK8736 | RCFD8736 | HC-D Item 11 |

### Trading Derivatives - Negative Fair Value

| Asset Class | MDRM | Call MDRM | Links To |
|-------------|------|-----------|----------|
| Interest Rate | BHCK8737 | RCFD8737 | HC-D Item 14 |
| Foreign Exchange | BHCK8738 | RCFD8738 | HC-D Item 14 |
| Equity | BHCK8739 | RCFD8739 | HC-D Item 14 |
| Commodity | BHCK8740 | RCFD8740 | HC-D Item 14 |

### Non-Trading Hedges - Positive Fair Value

| Asset Class | MDRM | Call MDRM | Links To |
|-------------|------|-----------|----------|
| Interest Rate | BHCK8741 | RCFD8741 | HC-D Item 11 |
| Foreign Exchange | BHCK8742 | RCFD8742 | HC-D Item 11 |
| Equity | BHCK8743 | RCFD8743 | HC-D Item 11 |
| Commodity | BHCK8744 | RCFD8744 | HC-D Item 11 |

### Non-Trading Hedges - Negative Fair Value

| Asset Class | MDRM | Call MDRM | Links To |
|-------------|------|-----------|----------|
| Interest Rate | BHCK8745 | RCFD8745 | HC-D Item 14 |
| Foreign Exchange | BHCK8746 | RCFD8746 | HC-D Item 14 |
| Equity | BHCK8747 | RCFD8747 | HC-D Item 14 |
| Commodity | BHCK8748 | RCFD8748 | HC-D Item 14 |

---

## Key Reconciliation Formulas

### HC-D Derivative Assets (Item 11)

```
BHCM3543 (HC-D item 11) = Trading Positive FV + Non-Trading Positive FV
         = (BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736)   [HC-L item 14.a.(1)]
         + (BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744)   [HC-L item 14.b.(1)]
```

### HC-D Derivative Liabilities (Item 14)

```
BHCK3547 (HC-D item 14) = Trading Negative FV + Non-Trading Negative FV
         = (BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740)   [HC-L item 14.a.(2)]
         + (BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748)   [HC-L item 14.b.(2)]
```

---

## Part II: Off-Balance Sheet Items

### Unused Commitments (item 1)

| Line | MDRM | Description |
|------|------|-------------|
| 1.a | BHCK3814 | Revolving open-end loans secured by 1-4 family residential (HELOCs) |
| 1.b.(1) | BHCKJ455 | Unused consumer credit card lines |
| 1.b.(2) | BHCKJ456 | Other unused credit card lines |
| 1.c.(1) | BHCK3816 | Commitments to fund CRE/construction/land dev. secured by RE |
| 1.c.(2) | BHCK6550 | Same, NOT secured by real estate |
| 1.d | BHCK3817 | Securities underwriting |
| 1.e.(1) | BHCKJ457 | Other unused commitments - C&I loans |
| 1.e.(2) | BHCKPV10 | Loans to depository financial institutions (new 2026Q1) |
| 1.e.(3) | BHCKPV11 | Loans to nondepository financial institutions (new 2026Q1; PV12-PV16 detail) |
| 1.e.(4) | BHCKJ459 | All other unused commitments |

### Letters of Credit (items 2-4)

| Line | MDRM | Description |
|------|------|-------------|
| 2 | BHCK6566 | Financial standby letters of credit and foreign office guarantees |
| 2.a | BHCK3820 | Amount conveyed to others |
| 3 | BHCK6570 | Performance standby letters of credit and foreign office guarantees |
| 3.a | BHCK3822 | Amount conveyed to others |
| 4 | BHCK3411 | Commercial and similar letters of credit |

---

## Analytical Considerations

### Notional to Fair Value Ratio

```
FV/Notional Ratio = Gross FV / Notional
Typical range: 0.5% - 3%

Higher ratio indicates:
- More market movement
- More seasoned portfolio
- Potential credit deterioration
```

### Net Fair Value Position

```
Net Derivatives FV = Positive FV - Negative FV
                   = BHCM3543 - BHCK3547   (HC-D items 11 and 14)

Positive = Net derivative asset
Negative = Net derivative liability
```

### Credit Derivative Position

```
Net CDS = Bought - Sold
Positive = Net protection buyer (risk-off)
Negative = Net protection seller (risk-on)
```

---

## MDRM Quick Reference - Fair Values

| Category | Positive FV | Negative FV |
|----------|-------------|-------------|
| IR Trading | BHCK8733 | BHCK8737 |
| FX Trading | BHCK8734 | BHCK8738 |
| Equity Trading | BHCK8735 | BHCK8739 |
| Commodity Trading | BHCK8736 | BHCK8740 |
| IR Non-Trading | BHCK8741 | BHCK8745 |
| FX Non-Trading | BHCK8742 | BHCK8746 |
| Equity Non-Trading | BHCK8743 | BHCK8747 |
| Commodity Non-Trading | BHCK8744 | BHCK8748 |

---

---

## Item 15: OTC Derivatives Credit Exposure and Collateral

Item 15 is a counterparty-segmented grid. Columns A-E are: A = Banks and securities firms,
B = Monoline financial guarantors, C = Hedge funds, D = Sovereign governments, E = Corporations
and all other counterparties.

| Line | Description | Code base (cols A-E) |
|------|-------------|----------------------|
| 15.a | Net current credit exposure | BHCKG418-G422 |
| 15.b.(1) | Collateral - Cash (U.S. dollar) | BHCKG423-G427 |
| 15.b.(2) | Collateral - Cash (Other currencies) | BHCKG428-G432 |
| 15.b.(3) | Collateral - U.S. Treasury securities | BHCKG433-G437 |
| 15.b.(4) | Collateral - U.S. govt agency & GSE debt | BHCKG438-G442 |
| 15.b.(5) | Collateral - Corporate bonds | BHCKG443-G447 |
| 15.b.(6) | Collateral - Equity securities | BHCKG448-G452 |
| 15.b.(7) | Collateral - All other | BHCKG453-G457 |
| 15.b.(8) | Total fair value of collateral | BHCKG458-G462 |

Codes are perfectly sequential (G418..G462); the monoline/sovereign columns (G419, G424, ...,
G460) are absent from the field-spec PDF parse but were confirmed via MDRM captions and warehouse
presence (2009-06-30 onward) per the FIELDSPEC_KNOWN_GAPS adjudication rule.

---

*See also*: [Trading Activities Deep Dive](TRADING_ACTIVITIES_GUIDE.md) for comprehensive HC-D and HC-L analysis

*Last Updated: 2026-06-11 (v8 conceptual-accuracy sweep)*
*Reference: FR Y-9C field spec (202603), MDRM, and FreeNIC warehouse*
