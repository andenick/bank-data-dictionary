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

```
PART I: DERIVATIVES
├── Notional Amounts
│   ├── Interest Rate Contracts
│   ├── Foreign Exchange Contracts
│   ├── Equity Contracts
│   ├── Commodity Contracts
│   └── Credit Derivatives
└── Fair Values
    ├── Trading Derivatives (positive/negative)
    └── Non-Trading Hedges (positive/negative)

PART II: OFF-BALANCE SHEET ITEMS
├── Unused Commitments
├── Financial Standby Letters of Credit
├── Performance Standby Letters of Credit
├── Commercial Letters of Credit
├── Securities Lent
├── Securities Borrowed
└── Other Off-Balance Sheet
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
BHCT3543 = Trading Positive FV + Non-Trading Positive FV
         = (BHCK8733 + BHCK8734 + BHCK8735 + BHCK8736)
         + (BHCK8741 + BHCK8742 + BHCK8743 + BHCK8744)
```

### HC-D Derivative Liabilities (Item 14)

```
BHCT3547 = Trading Negative FV + Non-Trading Negative FV
         = (BHCK8737 + BHCK8738 + BHCK8739 + BHCK8740)
         + (BHCK8745 + BHCK8746 + BHCK8747 + BHCK8748)
```

---

## Part II: Off-Balance Sheet Items

### Unused Commitments

| Type | MDRM | Description |
|------|------|-------------|
| Revolving credit lines | BHCKJ457 | Legally binding commitments |
| Credit card lines | BHCKJ458 | Unused card limits |
| Home equity lines | BHCK3814 | Unused HELOC amounts |
| Commercial RE | BHCKF164 | Construction/perm commitments |
| Securities underwriting | BHCK3817 | Firm commitment |

### Letters of Credit

| Type | MDRM | Description |
|------|------|-------------|
| Financial standby | BHCK3819 | Guarantee of financial performance |
| Performance standby | BHCK3821 | Guarantee of non-financial performance |
| Commercial LC | BHCK3411 | Trade finance |

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
                   = BHCT3543 - BHCT3547

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

*See also*: [Trading Activities Deep Dive](TRADING_ACTIVITIES_GUIDE.md) for comprehensive HC-D and HC-L analysis

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
