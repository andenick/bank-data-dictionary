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
| 1 | BHCAP742 | Common stock plus surplus (net of treasury/ESOP) |
| 2 | BHCAKW00 | Retained earnings |
| 3 | BHCAB530 | Accumulated other comprehensive income (AOCI) |
| 3.a | BHCAP838 | AOCI opt-out election (advanced approaches enter 0) |
| 4 | BHCAP839 | CET1 minority interest includable |
| 5 | BHCAP840 | **CET1 before adjustments and deductions (sum 1-4)** |

(Item 2.a BHCAJJ29 captures the CECL transition election.)

#### CET1 Deductions and AOCI Adjustments (Items 6-18, current numbering)

| Item | MDRM | Description |
|------|------|-------------|
| 6 | BHCAP841 | LESS: Goodwill (net of DTLs) |
| 7 | BHCAP842 | LESS: Other intangibles (not goodwill/MSAs), net of DTLs |
| 8 | BHCAP843 | LESS: DTAs from NOL/tax-credit carryforwards |
| 9.a | BHCAP844 | LESS: Unrealized gains/losses on AFS debt securities (AOCI) |
| 9.c | BHCAP846 | LESS: Net gains/losses on cash flow hedges (AOCI) |
| 9.d | BHCAP847 | LESS: AOCI from defined benefit postretirement plans |
| 9.e | BHCAP848 | LESS: Unrealized gains/losses on HTM securities in AOCI |
| 9.f | BHCAP849 | LESS: Cash flow hedge gain/loss on non-FV items |
| 10.a | BHCAQ258 | LESS: Unrealized gain/loss on liabilities (own credit risk) |
| 10.b | BHCAP850 | LESS: All other deductions before threshold deductions |
| 11 | BHCWP851 | LESS: Non-significant investments > 10% threshold (col B) |
| 12 | BHCAP852 | Subtotal (col A) / BHCWP852 (col B) |
| 13.a/13.b | BHCALB58 / BHCWP853 | LESS: Investments in unconsolidated FIs (>25% of line 12 / >10% threshold) |
| 14.a/14.b | BHCALB59 / BHCWP854 | LESS: MSAs (>25% of line 12 / >10% threshold) |
| 15.a/15.b | BHCALB60 / BHCWP855 | LESS: DTAs temp differences (>25% of line 12 / >10% threshold) |
| 16 | BHCWP856 | LESS: Aggregate > 15% CET1 threshold (col B) |
| 17 | BHCAP857 | LESS: Deductions due to insufficient AT1/Tier2 |
| 18 | BHCAP858 | **Total adjustments and deductions for CET1** |

Note: the Basel-III renumbering split AOCI adjustments into items 9.a-9.f and threshold deductions into items 13-16. An earlier draft mapped P841-P852 sequentially to items 7-18, which is incorrect.

#### CET1 Capital (Item 19)

| MDRM | Formula |
|------|---------|
| BHCAP859 (col A) / BHCWP859 (col B) | Item 12 - Item 18 |

### Additional Tier 1 (AT1) Capital

| Item | MDRM | Description |
|------|------|-------------|
| 20 | BHCAP860 | AT1 instruments plus related surplus |
| 21 | BHCAP861 | Non-qualifying instruments subject to phase-out |
| 22 | BHCAP862 | Tier 1 minority interest not in CET1 |
| 23 | BHCAP863 | AT1 before deductions (sum 20-22) |
| 24 | BHCAP864 | LESS: AT1 deductions |
| 25 | BHCAP865 | **Additional Tier 1 capital** (greater of 23-24, or 0) |

Note: legacy code BHCAP856 (used in an earlier draft as the AT1 total) is a threshold-investment line discontinued 2019-12-31; the correct AT1 total is BHCAP865.

### Tier 1 Capital (Item 26)

| MDRM | Formula |
|------|---------|
| BHCA8274 | CET1 + AT1 = Item 19 + Item 25 |

### Tier 2 Capital

| Item | MDRM | Description |
|------|------|-------------|
| 37 | BHCAP866 | Tier 2 instruments plus related surplus (sub debt) |
| 38 | BHCAP867 | Non-qualifying instruments subject to phase-out |
| 39 | BHCAP868 | Total capital minority interest not in Tier 1 |
| 40.a | BHCA5310 | Adjusted ALLL (AACL) includable (max 1.25% of RWA) |
| 42.a | BHCAP870 | Tier 2 before deductions (sum 37-40) |
| 43 | BHCAP872 | LESS: Tier 2 deductions |
| 44.a | BHCA5311 | **Tier 2 capital** (greater of 42.a-43, or 0) |

### Total Capital (Item 45.a)

| MDRM | Formula |
|------|---------|
| BHCA3792 | Tier 1 + Tier 2 = Item 26 + Item 44.a |

---

## Part II: Risk-Weighted Assets

Part II is a wide risk-weighting **grid**: each balance-sheet/off-balance-sheet line (items 1-22) is spread across many risk-weight-category columns (0%, 20%, 50%, 100%, 150%, 250%, 300%, 400%, 600%, 625%, 937.5%, 1250%, plus SSFA/gross-up columns). There is **no single MDRM code per risk-weight band**; the codes below are illustrative column codes within specific lines.

### On-Balance Sheet Lines (item 1 example: Cash)

| Column (risk weight) | MDRM | Note |
|-------------|------|----------------|
| A — totals/carrying value | BHCKD957 | Item 1 column A |
| 20% category | BHCKS396 | a risk-weight column within item 1 |
| ... | ... | grid continues across all categories |

### Key RWA Subtotals and Components

| Category | MDRM | Description |
|----------|------|-------------|
| Total balance sheet assets | BHCT2170 (col A) | Item 11 |
| Securitization (SSFA) | BHCKS475+ | Items 9.a-10 (HTM/AFS/trading/other + off-BS) |
| OTC / centrally cleared derivatives | items 20-21 grid | risk-weighted in the category columns |
| Off-balance sheet exposures | items 12-19 grid | LCs, recourse, commitments (CCF applied) |
| RWA by category subtotal | BHCKG630 (col C) | Item 23 (sum of items 11-22 per column) |
| RWA by category | BHCKG634 (col C) | Item 25 (item 23 x category risk weight) |
| Standardized market-risk RWA | BHCKS581 | Item 27 (market-risk-rule banks) |

### Total Risk-Weighted Assets (Part II Item 31)

| MDRM | Description |
|------|-------------|
| BHCKG641 | Total RWA = item 28 minus items 29 and 30 |

This Part II total (BHCKG641) is referenced by Part I item 46.a (BHCAA223) and is the denominator for all the capital ratios.

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

### Supplementary Leverage Ratio (advanced approaches)

| MDRM | Formula | Minimum |
|------|---------|---------|
| BHCAH036 | Tier 1 / Total Leverage Exposure (item 63 = BHCALE88) | 3.0% (+2% leverage buffer for G-SIBs) |

(Item 53 SLR = BHCAH036; the total leverage exposure denominator is item 63 = BHCALE88.)

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
| CET1 Capital | BHCAP859 | Common Equity Tier 1 (Part I item 19) |
| Additional Tier 1 | BHCAP865 | AT1 capital (Part I item 25) |
| Tier 1 Capital | BHCA8274 | CET1 + AT1 (item 26) |
| Tier 2 Capital | BHCA5311 | Sub debt + eligible AACL (item 44.a) |
| Total Capital | BHCA3792 | Tier 1 + Tier 2 (item 45.a) |
| Total RWA (Part I ref) | BHCAA223 | Part I item 46.a |
| Total RWA (Part II) | BHCKG641 | Part II item 31 (the computed total) |
| CET1 Ratio | BHCAP793 | CET1 / RWA (item 47) |
| Tier 1 Ratio | BHCA7206 | Tier 1 / RWA (item 48) |
| Total Capital Ratio | BHCA7205 | Total / RWA (item 49) |
| Leverage Ratio | BHCA7204 | Tier 1 / Avg Assets (item 31) |

Column convention: Part I items split by approach use BHCA (col A, non-advanced / standardized) and BHCW (col B, advanced approaches). The Call Report equivalents are RCFA / RCFW.

---

*Last Updated: 2026-06-11 (v8 conceptual-accuracy sweep; CSV rebuilt to current HC-R-I 108-cell + HC-R-II 377-cell spec, verified vs MDRM + warehouse; CET1<=Tier1<=Total confirmed 344/344 in 2024-12-31 filings)*
*Reference: FR Y-9C Instructions (current form, March 2026 field spec)*
