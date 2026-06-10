# Schedule HC-H: Interest Sensitivity Analysis Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-H - Selected Balance Sheet Items for Changes in Interest Rates
**Frequency**: Quarterly
**Purpose**: Analyze interest rate risk through repricing gap analysis

---

## Overview

Schedule HC-H breaks down interest-bearing assets and liabilities by repricing or maturity time buckets. This enables analysis of interest rate risk exposure through gap analysis.

### Key Concept: Repricing Gap

The repricing gap measures the difference between interest-sensitive assets and liabilities in each time bucket:

```
Gap = Interest-Bearing Assets - Interest-Bearing Liabilities

Positive Gap: Assets reprice before liabilities
  → Benefits from rising rates
  → Hurt by falling rates

Negative Gap: Liabilities reprice before assets
  → Benefits from falling rates
  → Hurt by rising rates
```

---

## Time Bucket Structure

| Column | Time Period | Description |
|--------|-------------|-------------|
| A | 3 months or less | Very short-term exposure |
| B | Over 3 months through 12 months | Near-term exposure |
| C | Over 1 year through 3 years | Medium-term |
| D | Over 3 years through 5 years | Medium-long term |
| E | Over 5 years through 15 years | Long-term |
| F | Over 15 years | Very long-term |
| G | Total | Sum across all buckets |

---

## Schedule Structure

```
INTEREST-BEARING ASSETS (Items 1-4)
├── Item 1: Debt securities (AFS and HTM)
├── Item 2: Loans and leases
│   ├── 2.a: Fixed rate
│   └── 2.b: Floating rate
├── Item 3: Other interest-bearing assets
└── Item 4: Total interest-bearing assets

INTEREST-BEARING LIABILITIES (Items 5-7)
├── Item 5: Deposits
│   ├── 5.a: Time deposits
│   └── 5.b: Other deposits
├── Item 6: Other interest-bearing liabilities
└── Item 7: Total interest-bearing liabilities

GAP ANALYSIS (Item 8)
└── Item 8: Net interest-bearing position (repricing gap)

MEMORANDA
└── M1: Cumulative gap
```

---

## Detailed Line Items

### Item 1: Debt Securities

| Bucket | MDRM | Description |
|--------|------|-------------|
| 3 months or less | BHCKA526 | Securities maturing/repricing ≤3mo |
| 3-12 months | BHCKA527 | Securities maturing 3-12mo |
| 1-3 years | BHCKA528 | Securities maturing 1-3yr |
| 3-5 years | BHCKA529 | Securities maturing 3-5yr |
| 5-15 years | BHCKA530 | Securities maturing 5-15yr |
| Over 15 years | BHCKA531 | Securities maturing >15yr |
| Total | BHCKA549 | Total securities |

**Note**: For floating-rate securities, classified by next repricing date

### Item 2: Loans and Leases

**Total Loans by Bucket**:

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKB556 |
| 3-12 months | BHCKB557 |
| 1-3 years | BHCKB558 |
| 3-5 years | BHCKB559 |
| 5-15 years | BHCKB560 |
| Over 15 years | BHDMB561 |
| Total | BHCKB562 |

**Fixed Rate Loans (2.a)**:

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKC400 |
| 3-12 months | BHCKC401 |
| ... | ... |
| Total | BHCKC406 |

**Floating Rate Loans (2.b)**:

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKC408 |
| 3-12 months | BHCKC409 |
| ... | ... |
| Total | BHCKC414 |

### Item 3: Other Interest-Bearing Assets

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKA544 |
| 3-12 months | BHCKA545 |
| ... | ... |

**Includes**: Fed funds sold, securities purchased under resale, interest-bearing deposits in banks

### Item 4: Total Interest-Bearing Assets

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKA550 |
| 3-12 months | BHCKA551 |
| ... | ... |
| Total | BHCKA556 |

**Reconciliation**:
```
Item 4 = Item 1 + Item 2 + Item 3
```

### Item 5: Deposits

**Total Deposits by Bucket**:

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKA557 |
| ... | ... |
| Total | BHCKA563 |

**Time Deposits (5.a)**:

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKC416 |
| ... | ... |
| Total | BHCKC422 |

**Other Deposits (5.b)**: Transaction accounts, savings accounts - typically short-term repricing

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKC424 |
| ... | ... |
| Total | BHCKC430 |

### Item 6: Other Interest-Bearing Liabilities

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKA564 |
| ... | ... |
| Total | BHCKA570 |

**Includes**: Fed funds purchased, repos, FHLB advances, subordinated debt

### Item 7: Total Interest-Bearing Liabilities

| Bucket | MDRM |
|--------|------|
| 3 months or less | BHCKA571 |
| ... | ... |
| Total | BHCKA577 |

### Item 8: Net Interest-Bearing Position (Repricing Gap)

| Bucket | MDRM | Formula |
|--------|------|---------|
| 3 months or less | BHCKA578 | Item 4, Col A - Item 7, Col A |
| ... | ... | ... |
| Total | BHCKA584 | Total assets - Total liabilities |

---

## Gap Analysis Interpretation

### Simple Gap Analysis

```
Period Gap = Rate-Sensitive Assets - Rate-Sensitive Liabilities

Example (3-month bucket):
  Assets repricing: $50B
  Liabilities repricing: $70B
  Gap: -$20B (liability sensitive)

Impact of 100bp rate increase:
  NII change ≈ Gap × Rate change × Time
           ≈ -$20B × 1% × (3/12)
           ≈ -$50M annual NII impact
```

### Cumulative Gap

The cumulative gap shows total exposure through each time horizon:

```
Cumulative Gap (1 year) = Sum of gaps through 12 months
                        = 3mo gap + 3-12mo gap
```

### Gap Ratio

```
Gap Ratio = Gap / Total Earning Assets

| Ratio | Interpretation |
|-------|----------------|
| > 0% | Asset sensitive |
| < 0% | Liability sensitive |
| ±10% | Moderate sensitivity |
| > ±20% | Significant sensitivity |
```

---

## Cross-Schedule Validation

### Asset Totals

```
HC-H Item 4, Total (Total IB Assets) ≈
  HC Item 2 (Securities) + HC Item 4.b (Loans) + HC Item 3 (Fed Funds/Repos)
  + Other earning assets
```

### Liability Totals

```
HC-H Item 7, Total (Total IB Liabilities) ≈
  HC Item 13 (Deposits) + HC Item 14 (Fed Funds/Repos)
  + HC Item 16 (Other Borrowed) + HC Item 19 (Sub Debt)
```

---

## Analytical Considerations

### Embedded Options

Gap analysis doesn't fully capture:
- **Prepayment risk**: Mortgage loans may prepay early in falling rate environment
- **Deposit decay**: Core deposits may be repriced or withdrawn
- **Rate floors/caps**: Floating-rate instruments with embedded options

### Behavioral Assumptions

For non-maturity deposits (transaction, savings):
- Banks make assumptions about repricing behavior
- "Core deposits" may be assigned longer repricing horizons
- Regulators scrutinize these assumptions

### Duration vs Gap

Duration analysis is more sophisticated:
- Gap measures $ mismatch
- Duration measures price sensitivity
- Both are useful for different purposes

---

## MDRM Quick Reference (3-Month Bucket)

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCKA526 | Securities |
| 2 | BHCKB556 | Loans |
| 2.a | BHCKC400 | Fixed-rate loans |
| 2.b | BHCKC408 | Floating-rate loans |
| 3 | BHCKA544 | Other IB assets |
| 4 | BHCKA550 | Total IB assets |
| 5 | BHCKA557 | Deposits |
| 5.a | BHCKC416 | Time deposits |
| 5.b | BHCKC424 | Other deposits |
| 6 | BHCKA564 | Other IB liabilities |
| 7 | BHCKA571 | Total IB liabilities |
| **8** | **BHCKA578** | **Gap (3mo)** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
