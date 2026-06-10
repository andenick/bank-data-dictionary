# Schedule HC-N: Past Due and Nonaccrual Loans Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-N - Past Due and Nonaccrual Loans, Leases, and Other Assets
**Frequency**: Quarterly
**Purpose**: Detail asset quality by delinquency status across all loan categories

---

## Overview

Schedule HC-N provides a matrix of loan quality, breaking down each loan category from HC-C by delinquency bucket:
- **30-89 days past due** (Column A)
- **90 or more days past due and still accruing** (Column B)
- **Nonaccrual** (Column C)

This schedule is essential for credit risk analysis and early warning detection.

---

## Delinquency Classification

### Column A: 30-89 Days Past Due

Loans where payment is 30-89 days late but still accruing interest.

**Regulatory Significance**: Early warning indicator; "criticized" classification

### Column B: 90+ Days Past Due and Still Accruing

Loans 90+ days late but still accruing interest. Generally requires:
- Well-secured and in process of collection, OR
- Consumer loans (auto, credit card) where collection expected

### Column C: Nonaccrual

Loans where interest accrual has stopped due to:
- Full repayment of principal and interest is not expected
- Payment is 90+ days past due (unless well-secured)
- Designated as troubled debt restructuring (TDR)

---

## Schedule Structure

```
LOAN CATEGORIES (rows mirror HC-C)
├── Item 1: Loans secured by real estate
│   ├── 1.a: Construction (1.a.1, 1.a.2)
│   ├── 1.b: Farmland
│   ├── 1.c: HELOCs
│   ├── 1.d: 1-4 family (1.d.1 first lien, 1.d.2 junior)
│   ├── 1.e: Multifamily
│   └── 1.f: CRE (1.f.1 owner-occ, 1.f.2 non-owner)
├── Item 2: Loans to depository institutions
├── Item 3: Agricultural production
├── Item 4: C&I loans (4.a US, 4.b non-US)
├── Item 5: Consumer loans
│   ├── 5.a: Credit cards
│   ├── 5.b: Other revolving
│   ├── 5.c: Automobile
│   └── 5.d: Other consumer
├── Item 6: Loans to foreign governments
├── Item 7: Municipal loans
├── Item 8: Other loans
├── Item 9: Lease financing receivables
└── Item 10: Total loans and leases
```

---

## MDRM Matrix (Key Categories)

### Real Estate Loans

| Category | 30-89 Days | 90+ Days | Nonaccrual |
|----------|------------|----------|------------|
| 1.a Construction | BHCK2759 | BHCK2769 | BHCK3505 |
| 1.b Farmland | BHCK3493 | BHCK3494 | BHCK3495 |
| 1.c HELOCs | BHCK5398 | BHCK5399 | BHCK5400 |
| 1.d 1-4 Family | BHCK5401 | BHCK5402 | BHCK3499 |
| 1.e Multifamily | BHCK3500 | BHCK3501 | BHCK3502 |
| 1.f CRE | BHCK3503 | BHCK3504 | BHCK5378 |

### Commercial and Consumer Loans

| Category | 30-89 Days | 90+ Days | Nonaccrual |
|----------|------------|----------|------------|
| 3 Ag production | BHCK1594 | BHCK1597 | BHCK1583 |
| 4 C&I | BHCK1606 | BHCK1607 | BHCK1608 |
| 5.a Credit cards | BHCKB575 | BHCKB576 | BHCKB577 |
| 5.c Auto loans | BHCKK206 | BHCKK207 | BHCKK208 |

### Total Loans

| Metric | MDRM |
|--------|------|
| 30-89 days total | BHCK5524 |
| 90+ days total | BHCK5525 |
| Nonaccrual total | BHCK1403 |

---

## Key Asset Quality Metrics

### Nonperforming Loans (NPL)

```
NPL = Nonaccrual + 90+ Days Still Accruing
    = BHCK1403 + BHCK5525 (or detailed sum)
```

### NPL Ratio

```
NPL Ratio = NPL / Total Loans (HC-C Item 12)
          = (BHCK1403 + BHCK5525) / BHCTB528

Typical ranges:
- Strong: < 1%
- Average: 1-2%
- Weak: > 3%
- Crisis: > 5%
```

### Delinquency Rate (30+ Days)

```
Delinquency Rate = (30-89 + 90+ + Nonaccrual) / Total Loans
                 = (BHCK5524 + BHCK5525 + BHCK1403) / BHCTB528
```

### Coverage Ratio

```
Coverage = Allowance (HC-C Item 11) / NPL
         = BHCT3123 / (BHCK1403 + BHCK5525)

Higher coverage = more reserved against expected losses
```

### Texas Ratio

```
Texas Ratio = NPL + OREO / (Tangible Equity + Allowance)
            = (BHCK1403 + BHCK5525 + BHCT2150) / (BHCT3210 - BHCK3163 + BHCT3123)

>100% = Potentially troubled
```

---

## Reconciliation to HC-C

The row totals in HC-N (Column A + B + C for each category) should NOT exceed the corresponding HC-C balances, as they represent only the impaired portion.

```
HC-N Item 1 (all columns) ≤ HC-C Item 1 (Real estate loans)
HC-N Item 4 (all columns) ≤ HC-C Item 4 (C&I loans)
etc.
```

---

## Analytical Applications

### Trend Analysis

```
Watch for:
- Rising 30-89 days → future NPL increases
- Migration from 30-89 → 90+ → Nonaccrual
- Concentration in specific loan types
```

### Vintage Analysis

Combined with Call Report Schedule RC-M:
- Track delinquency by origination year
- Identify vintage-specific problems

### Geographic/Industry Concentration

Combined with Call Report Schedule RC-C Part II:
- Identify geographic hotspots
- Industry-specific stress

---

## Historical Context

### 2008-2010 Financial Crisis

Peak delinquency rates:
- 1-4 family: 10%+ NPL ratio
- CRE: 8%+ NPL ratio
- Construction: 15%+ NPL ratio

### COVID-19 (2020)

- Initial spike in early delinquencies
- Forbearance programs masked true delinquency
- TDR modifications increased

### Current Environment

Monitor for:
- CRE (especially office) stress
- Rising consumer delinquencies
- C&I credit deterioration

---

## MDRM Quick Reference

| Category | 30-89 Days | 90+ Days | Nonaccrual |
|----------|------------|----------|------------|
| RE Total | BHCK5526 | BHCK1422 | BHCK3492 |
| Construction | BHCK2759 | BHCK2769 | BHCK3505 |
| 1-4 Family | BHCK5401 | BHCK5402 | BHCK3499 |
| CRE | BHCK3503 | BHCK3504 | BHCK5378 |
| C&I | BHCK1606 | BHCK1607 | BHCK1608 |
| Credit Card | BHCKB575 | BHCKB576 | BHCKB577 |
| Auto | BHCKK206 | BHCKK207 | BHCKK208 |
| **TOTAL** | **BHCK5524** | **BHCK5525** | **BHCK1403** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
