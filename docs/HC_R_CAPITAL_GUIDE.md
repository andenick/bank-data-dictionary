# Schedule HC-R: Regulatory Capital Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-R - Regulatory Capital
**Frequency**: Quarterly
**Purpose**: Calculate and disclose regulatory capital components, ratios, and risk-weighted assets

---

## Overview

Schedule HC-R is the cornerstone of regulatory capital reporting under Basel III. It contains:
- **Part I**: Regulatory capital components and ratios
- **Part II**: Risk-weighted assets (RWA) calculation

### Basel III Capital Framework

```
                   CET1 Capital
                        ↓
         + Additional Tier 1 Capital
                        ↓
              = Tier 1 Capital
                        ↓
           + Tier 2 Capital
                        ↓
             = Total Capital
```

---

## Part I: Regulatory Capital Components

### Common Equity Tier 1 (CET1) Capital

#### Starting Point (Items 1-6)

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCAP742 | Common stock plus surplus |
| 2 | BHCAKW00 | Retained earnings |
| 3 | BHCAB530 | AOCI (if opt-out elected) |
| 4 | BHCAP838 | AOCI included in CET1 |
| 5 | BHCAP839 | CET1 minority interest |
| 6 | BHCAP840 | **CET1 before adjustments** |

#### CET1 Deductions (Items 7-18)

| Item | MDRM | Description |
|------|------|-------------|
| 7 | BHCAP841 | Goodwill (net of DTL) |
| 8 | BHCAP842 | Other intangible assets |
| 9 | BHCAP843 | DTA from operating losses |
| 10 | BHCAP844 | Gain on sale securitization |
| 11 | BHCAP845 | Defined benefit pension net assets |
| 12 | BHCAP846 | Investments in own shares |
| 13 | BHCAP847 | Reciprocal cross-holdings |
| 14 | BHCAP848 | Investments in unconsolidated FIs |
| 15 | BHCAP849 | MSA (threshold deduction) |
| 16 | BHCAP850 | DTA from temp differences |
| 17 | BHCAP851 | Other CET1 deductions |
| 18 | BHCAP852 | **Total CET1 deductions** |

#### CET1 Capital (Item 19)

| MDRM | Formula |
|------|---------|
| BHCAP859 | Item 6 - Item 18 |

### Additional Tier 1 (AT1) Capital

| Item | MDRM | Description |
|------|------|-------------|
| 20 | BHCAP853 | AT1 instruments (non-cumulative preferred) |
| 21 | BHCAP854 | Tier 1 minority interest |
| 22 | BHCAP855 | AT1 deductions |
| 23 | BHCAP856 | **Additional Tier 1 capital** |

### Tier 1 Capital (Item 24)

| MDRM | Formula |
|------|---------|
| BHCA8274 | CET1 + AT1 = Item 19 + Item 23 |

### Tier 2 Capital

| Item | MDRM | Description |
|------|------|-------------|
| 25 | BHCAP857 | Tier 2 instruments (sub debt) |
| 26 | BHCAP858 | Tier 2 minority interest |
| 27 | BHCA5311 | Eligible ALLL (max 1.25% of RWA) |
| 28 | BHCKP856 | Tier 2 deductions |
| 29 | BHCA5311 | **Tier 2 capital** |

### Total Capital (Item 30)

| MDRM | Formula |
|------|---------|
| BHCA3792 | Tier 1 + Tier 2 = Item 24 + Item 29 |

---

## Part II: Risk-Weighted Assets

### On-Balance Sheet Assets by Risk Weight

| Risk Weight | MDRM | Typical Assets |
|-------------|------|----------------|
| 0% | BHCKA221 | Cash, Treasuries, GNMA MBS |
| 20% | BHCKS396 | GSE debt, munis, interbank |
| 50% | BHCKS397 | Prudent 1-4 family mortgages |
| 100% | BHCKS398 | C&I, CRE, most loans |
| 150% | BHCKS399 | HVCRE, past due, below IG |

### Other RWA Components

| Category | MDRM | Description |
|----------|------|-------------|
| Securitization | BHCKS400 | Securitization exposures |
| Equity | BHCKS401 | Equity investments |
| Derivatives | BHCKS402 | Derivative exposures |
| Off-Balance Sheet | BHCKS403 | Commitments, LCs, guarantees |
| Market Risk | BHCKA222 | Trading book capital |

### Total Risk-Weighted Assets (Item 31)

| MDRM | Description |
|------|-------------|
| BHCAA223 | Sum of all risk-weighted exposures |

---

## Capital Ratios

### CET1 Capital Ratio

| MDRM | Formula | Minimum |
|------|---------|---------|
| BHCAP793 | CET1 / RWA | 4.5% |

### Tier 1 Capital Ratio

| MDRM | Formula | Minimum |
|------|---------|---------|
| BHCA7206 | Tier 1 / RWA | 6.0% |

### Total Capital Ratio

| MDRM | Formula | Minimum |
|------|---------|---------|
| BHCA7205 | Total Capital / RWA | 8.0% |

### Leverage Ratio

| MDRM | Formula | Minimum |
|------|---------|---------|
| BHCA7204 | Tier 1 / Avg Total Assets | 4.0% |

### Supplementary Leverage Ratio (G-SIBs)

| MDRM | Formula | Minimum |
|------|---------|---------|
| BHCKA224 | Tier 1 / Total Leverage Exposure | 3.0% (5.0% for G-SIBs) |

---

## Capital Buffers

### Conservation Buffer: 2.5%

All banks must maintain CET1 buffer above minimums.

### G-SIB Surcharge: 1.0% - 3.5%

Based on systemic importance score.

### Countercyclical Buffer: 0% - 2.5%

Activated by regulators during credit expansion.

### Well-Capitalized Requirements

| Ratio | Well-Capitalized | Adequately Capitalized |
|-------|------------------|------------------------|
| CET1 | ≥ 6.5% | ≥ 4.5% |
| Tier 1 | ≥ 8.0% | ≥ 6.0% |
| Total | ≥ 10.0% | ≥ 8.0% |
| Leverage | ≥ 5.0% | ≥ 4.0% |

---

## Threshold Deduction Items

Certain items are subject to threshold-based deductions rather than full deduction:

### 10% Individual Threshold

| Item | Treatment |
|------|-----------|
| MSAs | Deduct amount > 10% of CET1 |
| DTA (temp differences) | Deduct amount > 10% of CET1 |
| Significant investments in FIs | Deduct amount > 10% of CET1 |

### 15% Aggregate Threshold

Combined threshold items cannot exceed 15% of CET1.

### Below-Threshold Treatment

Amounts below thresholds receive 250% risk weight instead of deduction.

---

## Reconciliation to Balance Sheet

### Equity to CET1 Reconciliation

```
Total Equity (HC Item 28)
  - Preferred stock (not qualifying as AT1)
  - AOCI adjustments (if opt-out)
  - Goodwill and intangibles
  - DTA and other deductions
  + Minority interest adjustments
= CET1 Capital (HC-R Part I)
```

### RWA to Assets Reconciliation

```
Total Assets (HC Item 12) × Average Risk Weight ≈ RWA

Where Average Risk Weight typically 60-80% for traditional banks
(Lower for investment banks with more low-risk trading assets)
```

---

## Key Analytical Metrics

### CET1 Ratio Trend

```
Monitor for:
- Declining trend → potential capital stress
- Below buffers → distribution restrictions
- Peer comparison → relative strength
```

### RWA Density

```
RWA Density = RWA / Total Assets
- Lower = more low-risk assets (Treasuries, agency MBS)
- Higher = more commercial lending, trading
```

### Capital Efficiency

```
Return on RWA = Net Income / RWA
Measures profitability relative to regulatory capital consumption
```

---

## MDRM Quick Reference

| Concept | MDRM | Description |
|---------|------|-------------|
| CET1 Capital | BHCAP859 | Common Equity Tier 1 |
| Tier 1 Capital | BHCA8274 | CET1 + AT1 |
| Tier 2 Capital | BHCA5311 | Sub debt + eligible ALLL |
| Total Capital | BHCA3792 | Tier 1 + Tier 2 |
| Total RWA | BHCAA223 | Risk-weighted assets |
| CET1 Ratio | BHCAP793 | CET1 / RWA |
| Tier 1 Ratio | BHCA7206 | Tier 1 / RWA |
| Total Capital Ratio | BHCA7205 | Total / RWA |
| Leverage Ratio | BHCA7204 | Tier 1 / Avg Assets |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
