# Schedule HC-Q: Financial Assets and Liabilities Measured at Fair Value Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-Q - Financial Assets and Liabilities Measured at Fair Value on a Recurring Basis
**Frequency**: Quarterly
**Purpose**: Provide fair value hierarchy breakdown (Level 1/2/3) for assets and liabilities

---

## Overview

Schedule HC-Q discloses the fair value measurement hierarchy for financial assets and liabilities. This is required under ASC 820 (Fair Value Measurement) and provides transparency into valuation approaches.

### Fair Value Hierarchy

| Level | Inputs | Examples |
|-------|--------|----------|
| **Level 1** | Quoted prices in active markets | Exchange-traded securities, listed derivatives |
| **Level 2** | Observable inputs (not quoted prices) | OTC derivatives, structured products with observable inputs |
| **Level 3** | Unobservable inputs (model-based) | Illiquid securities, complex derivatives, distressed assets |

---

## Schedule Structure

```
FINANCIAL ASSETS AT FAIR VALUE
├── Item 1: Trading assets
│   ├── 1.a: Debt securities
│   ├── 1.b: Equity securities
│   ├── 1.c: Derivative assets (trading)
│   └── 1.d: Loans
├── Item 2: AFS debt securities
├── Item 3: Loans held for sale
├── Item 4: Loans held for investment at FV
├── Item 5: Derivative assets (non-trading)
└── Item 6: Other financial assets at FV

FINANCIAL LIABILITIES AT FAIR VALUE
├── Item 7: Trading liabilities
│   ├── 7.a: Short positions
│   └── 7.b: Derivative liabilities (trading)
├── Item 8: Derivative liabilities (non-trading)
└── Item 9: Other financial liabilities at FV

MEMORANDA
├── M1: Intangible assets at FV
├── M2: MSAs
├── M3-M4: Level 3 transfers
└── M5: Unpaid principal balance of loans at FV
```

---

## Column Structure

| Column | Description | MDRM Suffix |
|--------|-------------|-------------|
| A | Total Fair Value | Various |
| B | Level 1 | Various |
| C | Level 2 | Various |
| D | Level 3 | Various |

**Reconciliation**: Column A = Column B + Column C + Column D

---

## Key Items

### Trading Assets (Item 1)

| Category | Total FV | Level 1 | Level 2 | Level 3 |
|----------|----------|---------|---------|---------|
| Total | BHCLF688 | BHCLF689 | BHCLF690 | BHCLF691 |
| Debt securities | BHCLF692 | BHCLF693 | BHCLF694 | BHCLF695 |
| Equity securities | BHCLF696 | BHCLF697 | BHCLF698 | BHCLF699 |
| Derivative assets | BHCLF700 | BHCLF701 | BHCLF702 | BHCLF703 |
| Loans | BHCLF704 | BHCLF705 | BHCLF706 | BHCLF707 |

**Ties To**: HC-D Item 12 (Total trading assets)

### AFS Debt Securities (Item 2)

| Metric | MDRM |
|--------|------|
| Total FV | BHCL1773 |
| Level 1 | BHCLF709 |
| Level 2 | BHCLF710 |
| Level 3 | BHCLF711 |

**Ties To**: HC Item 2.b and HC-B Item 8, Column B

### Trading Liabilities (Item 7)

| Category | Total FV | Level 1 | Level 2 | Level 3 |
|----------|----------|---------|---------|---------|
| Total | BHCLF728 | BHCLF729 | BHCLF730 | BHCLF731 |
| Short positions | BHCLF732 | BHCLF733 | BHCLF734 | BHCLF735 |
| Derivative liabilities | BHCLF736 | BHCLF737 | BHCLF738 | BHCLF739 |

**Ties To**: HC-D Item 15 (Total trading liabilities)

---

## Level 3 Analysis

Level 3 assets and liabilities require:
- Significant unobservable inputs
- Internal models for valuation
- Enhanced disclosure requirements

### Level 3 Indicators to Watch

```
Level 3 % = Level 3 Assets / Total Fair Value Assets
- Low (< 5%): Liquid, transparent portfolio
- Moderate (5-15%): Some illiquid holdings
- High (> 15%): Significant model-dependent valuations
```

### Level 3 Reconciliation Roll-Forward

The memoranda items track transfers into/out of Level 3:
- M3: Transfers INTO Level 3 (increased uncertainty)
- M4: Transfers OUT OF Level 3 (improved observability)

---

## Reconciliation to Other Schedules

### Trading Assets

```
HC-Q Item 1, Total FV ≈ HC-D Item 12 ≈ HC Item 5
```

### Trading Liabilities

```
HC-Q Item 7, Total FV ≈ HC-D Item 15 ≈ HC Item 15
```

### AFS Securities

```
HC-Q Item 2, Total FV = HC-B Item 8, Column B = HC Item 2.b
```

### Derivatives

```
HC-Q Items 1.c + 5 = HC-D Item 11 (derivative assets)
HC-Q Items 7.b + 8 = HC-D Item 14 (derivative liabilities)
```

---

## Analytical Applications

### Valuation Quality Assessment

```
Higher Level 1 = More reliable valuations
Higher Level 3 = More model risk, potential for surprise

L3/Total Ratio monitors model reliance over time
```

### Stress Testing Considerations

Level 3 assets are particularly vulnerable in stress:
- Market dislocation → fewer observable inputs
- Assets may migrate L2 → L3
- Larger valuation adjustments possible

### Regulatory Scrutiny

Regulators focus on:
- Level 3 growth trends
- Transfer activity (especially L2 → L3)
- Valuation methodology documentation
- Independent price verification

---

## MDRM Quick Reference

| Item | Total FV | Level 1 | Level 2 | Level 3 |
|------|----------|---------|---------|---------|
| Trading assets | BHCLF688 | BHCLF689 | BHCLF690 | BHCLF691 |
| - Derivatives | BHCLF700 | BHCLF701 | BHCLF702 | BHCLF703 |
| AFS securities | BHCL1773 | BHCLF709 | BHCLF710 | BHCLF711 |
| Trading liabilities | BHCLF728 | BHCLF729 | BHCLF730 | BHCLF731 |
| - Derivatives | BHCLF736 | BHCLF737 | BHCLF738 | BHCLF739 |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
