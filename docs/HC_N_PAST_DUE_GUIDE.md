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
LOAN CATEGORIES (rows mirror current HC-C)
├── Item 1: Loans secured by real estate
│   ├── 1.a: Construction — 1.a.(1) 1-4 family, 1.a.(2) other/land dev
│   ├── 1.b: Farmland (domestic offices)
│   ├── 1.c.(1): Revolving open-end 1-4 family (HELOCs)
│   ├── 1.c.(2): Closed-end 1-4 family — (a) first liens, (b) junior liens
│   ├── 1.d: Multifamily (5+) residential (domestic offices)
│   ├── 1.e: Nonfarm nonresidential — 1.e.(1) owner-occ, 1.e.(2) other
│   └── 1.f: RE loans in foreign offices
├── Item 2: Loans to depository institutions — 2.a US banks, 2.b foreign banks
├── Item 3: Agricultural production / loans to farmers
├── Item 4: Commercial and industrial loans (single line; no US/non-US split)
├── Item 5: Loans to individuals
│   ├── 5.a: Credit cards
│   ├── 5.b: Automobile loans
│   └── 5.c: Other consumer loans
├── Item 6: Loans to foreign governments
├── Item 7: All other loans
├── Item 8: Leases — 8.a consumer, 8.b other, 8.c lease finance receivables (HCs < $5B)
├── Item 9: Total loans and leases (sum of items 1-8.b)
├── Item 10: Debt securities and other assets
├── Item 11-12: U.S. Government-guaranteed / FDIC loss-share covered portions
└── Memoranda M.1-M.9 (loan modifications, CRE finance, non-US, HFS/FV, etc.)
```
Columns: A = 30-89 days past due; B = 90+ days past due and still accruing; C = nonaccrual.

---

## MDRM Matrix (Key Categories)

### Real Estate Loans (current codes)

| Category | 30-89 Days (A) | 90+ Days (B) | Nonaccrual (C) |
|----------|------------|----------|------------|
| 1.a.(1) 1-4 family construction | BHCKF172 | BHCKF174 | BHCKF176 |
| 1.a.(2) Other construction/land dev | BHCKF173 | BHCKF175 | BHCKF177 |
| 1.b Farmland | BHCK3493 | BHCK3494 | BHCK3495 |
| 1.c.(1) HELOCs | BHCK5398 | BHCK5399 | BHCK5400 |
| 1.c.(2)(a) Closed-end 1-4 first lien | BHCKC236 | BHCKC237 | BHCKC229 |
| 1.c.(2)(b) Closed-end 1-4 junior lien | BHCKC238 | BHCKC239 | BHCKC230 |
| 1.d Multifamily | BHCK3499 | BHCK3500 | BHCK3501 |
| 1.e.(1) Owner-occupied CRE | BHCKF178 | BHCKF180 | BHCKF182 |
| 1.e.(2) Other nonfarm nonres CRE | BHCKF179 | BHCKF181 | BHCKF183 |

### Commercial and Consumer Loans (current codes)

| Category | 30-89 Days (A) | 90+ Days (B) | Nonaccrual (C) |
|----------|------------|----------|------------|
| 2.a US depository institutions | BHCK5377 | BHCK5378 | BHCK5379 |
| 2.b Foreign banks | BHCK5380 | BHCK5381 | BHCK5382 |
| 3 Ag production | BHCK1594 | BHCK1597 | BHCK1583 |
| 4 C&I | BHCK1606 | BHCK1607 | BHCK1608 |
| 5.a Credit cards | BHCKB575 | BHCKB576 | BHCKB577 |
| 5.b Auto loans | BHCKK213 | BHCKK214 | BHCKK215 |
| 5.c Other consumer | BHCKK216 | BHCKK217 | BHCKK218 |
| 8.a Consumer leases | BHCKF166 | BHCKF167 | BHCKF168 |
| 8.b Other leases | BHCKF169 | BHCKF170 | BHCKF171 |

### Total Loans and Leases (item 9 — current codes)

| Metric | MDRM | Note |
|--------|------|------|
| 30-89 days total | BHCK1406 | (legacy BHCK5524 discontinued 2017-12-31) |
| 90+ days total | BHCK1407 | (legacy BHCK5525 discontinued 2017-12-31) |
| Nonaccrual total | BHCK1403 | unchanged |

---

## Key Asset Quality Metrics

### Nonperforming Loans (NPL)

```
NPL = Nonaccrual + 90+ Days Still Accruing
    = BHCK1403 + BHCK1407 (item 9 totals; or detailed sum)
```

### NPL Ratio

```
NPL Ratio = NPL / Total Loans (HC-C Item 7)
          = (BHCK1403 + BHCK1407) / BHCKB528

Typical ranges:
- Strong: < 1%
- Average: 1-2%
- Weak: > 3%
- Crisis: > 5%
```

### Delinquency Rate (30+ Days)

```
Delinquency Rate = (30-89 + 90+ + Nonaccrual) / Total Loans
                 = (BHCK1406 + BHCK1407 + BHCK1403) / BHCKB528
```

### Coverage Ratio

```
Coverage = Allowance for credit losses / NPL
         = BHCT3123 / (BHCK1403 + BHCK1407)

Higher coverage = more reserved against expected losses
```

### Texas Ratio

```
Texas Ratio = (NPL + OREO) / (Tangible Equity + Allowance)
            = (BHCK1403 + BHCK1407 + BHCK2150) / (BHCT3210 - BHCK3163 + BHCT3123)

>100% = Potentially troubled
```

---

## Reconciliation to HC-C

The row totals in HC-N (Column A + B + C for each category) should NOT exceed the corresponding HC-C balances, as they represent only the impaired portion.

```
HC-N RE sub-items (all columns) ≤ HC-C Item 1 (Real estate loans)
HC-N Item 4 (all columns) ≤ HC-C Item 4 (C&I loans)
HC-N Item 9 total (all columns) ≤ HC-C Item 7 (Total loans and leases)
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

| Category | 30-89 Days (A) | 90+ Days (B) | Nonaccrual (C) |
|----------|------------|----------|------------|
| 1.a.(1) 1-4 Family Construction | BHCKF172 | BHCKF174 | BHCKF176 |
| 1.c.(2)(a) Closed-end 1-4 First Lien | BHCKC236 | BHCKC237 | BHCKC229 |
| 1.e.(2) Other Nonfarm Nonres (CRE) | BHCKF179 | BHCKF181 | BHCKF183 |
| 4 C&I | BHCK1606 | BHCK1607 | BHCK1608 |
| 5.a Credit Card | BHCKB575 | BHCKB576 | BHCKB577 |
| 5.b Auto | BHCKK213 | BHCKK214 | BHCKK215 |
| **9 TOTAL loans & leases** | **BHCK1406** | **BHCK1407** | **BHCK1403** |

Legacy aggregate codes BHCK5526/1422/3492 (RE total) and BHCK5524/5525 (total 30-89 / 90+) were discontinued (2017 and earlier) and removed; the current form has no item-1 RE total and reports the total at item 9.

---

*Last Updated: 2026-06-11 (v8 conceptual-accuracy sweep; rebuilt to current 148-cell HC-N spec, verified vs MDRM + warehouse)*
*Reference: FR Y-9C Instructions (current form, March 2026 field spec)*
