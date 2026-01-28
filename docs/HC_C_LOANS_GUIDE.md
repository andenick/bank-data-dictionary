# Schedule HC-C: Loans and Lease Financing Receivables Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-C - Loans and Lease Financing Receivables
**Frequency**: Quarterly
**Purpose**: Detail the loan portfolio by collateral type, borrower type, and geography

---

## Overview

Schedule HC-C is the primary schedule for loan portfolio analysis. It provides:
- **Granular loan breakdowns** by collateral and purpose
- **Geographic split** between domestic and foreign
- **Basis for asset quality analysis** (ties to HC-N)
- **Risk-weighted asset inputs** for capital calculations (HC-R)

### Key Metrics

| Metric | Formula | Purpose |
|--------|---------|---------|
| Gross Loans | Sum(Items 1-9) | Total loan originations |
| Net Loans | Gross - Unearned - Allowance | Balance sheet carrying value |
| Allowance Ratio | Item 11 / (Items 1-9 - Item 10) | Credit risk reserve adequacy |

---

## Schedule Structure

```
LOAN PORTFOLIO
├── Item 1: Real Estate Loans (largest category)
│   ├── 1.a: Construction and land development
│   │   ├── 1.a.(1): 1-4 family residential construction
│   │   └── 1.a.(2): Other construction (commercial)
│   ├── 1.b: Farmland
│   ├── 1.c: HELOCs (revolving home equity)
│   ├── 1.d: 1-4 family residential (closed-end)
│   │   ├── 1.d.(1): First liens
│   │   └── 1.d.(2): Junior liens
│   ├── 1.e: Multifamily (5+ units)
│   └── 1.f: Nonfarm nonresidential (CRE)
│       ├── 1.f.(1): Owner-occupied
│       └── 1.f.(2): Non-owner occupied
├── Item 2: Loans to depository institutions
├── Item 3: Agricultural production loans
├── Item 4: Commercial and industrial (C&I)
├── Item 5: Consumer loans
│   ├── 5.a: Credit cards
│   ├── 5.b: Other revolving
│   ├── 5.c: Automobile loans
│   └── 5.d: Other consumer
├── Item 6: Loans to foreign governments
├── Item 7: Municipal loans
├── Item 8: Other loans
├── Item 9: Lease financing receivables
├── Item 10: LESS: Unearned income
├── Item 11: LESS: Allowance for loan losses
└── Item 12: NET LOANS AND LEASES
```

---

## Detailed Line Item Analysis

### Item 1: Loans Secured by Real Estate

**Total Real Estate MDRM**:

| Geography | MDRM | Description |
|-----------|------|-------------|
| Domestic | BHCK1410 | RE loans - domestic offices |
| Foreign | BHCK1411 | RE loans - foreign offices |
| Total | BHCT1410 | Total RE loans |

**Reconciliation**:
```
Item 1 = Item 1.a + Item 1.b + Item 1.c + Item 1.d + Item 1.e + Item 1.f
```

---

#### Item 1.a: Construction and Land Development

| Sub-Item | MDRM | Description | Risk Weight |
|----------|------|-------------|-------------|
| 1.a (Total) | BHCT1415 | Total construction | 100-150% |
| 1.a.(1) | BHCKF158 | 1-4 family construction | 50-100% |
| 1.a.(2) | BHCKF159 | Other construction | 100-150% |

**Risk Characteristics**:
- Highest risk real estate category
- No cash flow until completion
- Interest typically capitalized
- Higher default rates in downturns

**HVCRE (High Volatility CRE)**: Item 1.a.(2) may include HVCRE loans subject to 150% risk weight under Basel III standardized approach.

---

#### Item 1.b: Secured by Farmland

| MDRM | Description |
|------|-------------|
| BHCT1420 | Loans secured by farmland |

**Characteristics**:
- Long-term agricultural real estate
- Commodity price sensitivity
- Often tied to USDA programs

---

#### Item 1.c: Home Equity Lines of Credit (HELOCs)

| MDRM | Description |
|------|-------------|
| BHCK1797 | Revolving home equity |

**Characteristics**:
- Open-end revolving credit
- Secured by 1-4 family residence
- Draw period followed by repayment period
- Variable rate, prime-based pricing

**Risk Weight**: 50-100% depending on LTV and documentation

---

#### Item 1.d: 1-4 Family Residential (Closed-End)

| Sub-Item | MDRM | Description | Risk Weight |
|----------|------|-------------|-------------|
| 1.d (Total) | BHCT5367 | Total closed-end 1-4 family | 35-100% |
| 1.d.(1) | BHCTC236 | First liens | 35-50% |
| 1.d.(2) | BHCTC238 | Junior liens | 100% |

**First Lien Risk Weights** (Basel III):
- LTV ≤ 60%: 35%
- 60% < LTV ≤ 80%: 50%
- LTV > 80% (non-prudent): 100%

---

#### Item 1.e: Multifamily (5+ Units)

| MDRM | Description |
|------|-------------|
| BHCT1460 | Multifamily residential |

**Sub-Items (2022+)**:
| MDRM | Description | Risk Weight |
|------|-------------|-------------|
| BHCKKX57 | Government-guaranteed multifamily | 20% |
| BHCKKX58 | Other multifamily | 50-100% |

**Characteristics**:
- Apartment buildings (5+ units)
- Cash flow from rental income
- Generally lower risk than construction

---

#### Item 1.f: Nonfarm Nonresidential (CRE)

| Sub-Item | MDRM | Description | Risk Weight |
|----------|------|-------------|-------------|
| 1.f (Total) | BHCT1480 | Total CRE | 100% |
| 1.f.(1) | BHCTF160 | Owner-occupied | 100% |
| 1.f.(2) | BHCTF162 | Non-owner occupied | 100% |

**Owner-Occupied CRE**: Repayment depends on business operations, not rental income
**Non-Owner Occupied CRE**: Investment property; repayment from rental income

**Property Types**:
- Office
- Retail
- Industrial/Warehouse
- Hotel/Hospitality
- Healthcare facilities

---

### Item 2: Loans to Depository Institutions

| Sub-Item | MDRM | Description | Risk Weight |
|----------|------|-------------|-------------|
| 2 (Total) | BHCK1288 | Total interbank | 20-100% |
| 2.a | BHCKB532 | US banks and thrifts | 20% |
| 2.b | BHCKB533 | Foreign banks | 20-150% |
| 2.c | BHCKB534 | Acceptances of other banks | 20% |

**Nature**: Short-term lending between financial institutions

---

### Item 3: Agricultural Production Loans

| MDRM | Description |
|------|-------------|
| BHCK1590 | Loans to finance agricultural production |

**Characteristics**:
- Operating loans for farming/ranching
- Seasonal working capital
- Commodity-secured in some cases

---

### Item 4: Commercial and Industrial (C&I) Loans

| Sub-Item | MDRM | Description | Risk Weight |
|----------|------|-------------|-------------|
| 4 (Total) | BHCT1766 | Total C&I | 100% |
| 4.a | BHCKB531 | US addressees | 100% |
| 4.b | BHCK1763 | Non-US addressees | 100% |

**C&I Loan Types**:
- Working capital lines
- Term loans
- Asset-based lending
- Leveraged loans
- Small business loans

**Key Metric**: C&I loans are a leading indicator of economic activity

---

### Item 5: Consumer Loans

| Sub-Item | MDRM | Description | Risk Weight |
|----------|------|-------------|-------------|
| 5 (Total) | BHCK1975 | Total consumer | 75-100% |
| 5.a | BHCKB538 | Credit cards | 100% |
| 5.a.(1) | BHCKB561 | Consumer credit cards | 100% |
| 5.a.(2) | BHCKK137 | Commercial credit cards | 100% |
| 5.b | BHCKB539 | Other revolving | 100% |
| 5.c | BHCKK137 | Automobile loans | 75% |
| 5.c.(1) | BHCKK138 | New vehicles | 75% |
| 5.c.(2) | BHCKK139 | Used vehicles | 75% |
| 5.d | BHCKB540 | Other consumer | 100% |

**Credit Card Segmentation**:
- Consumer cards (5.a.1): Personal use
- Commercial cards (5.a.2): Business expense cards

**Auto Loans**: Receive preferential 75% risk weight under Basel III

---

### Item 6: Loans to Foreign Governments

| MDRM | Description |
|------|-------------|
| BHCK1296 | Sovereign exposures |

**Risk Weight**: Based on OECD country risk classification (0% to 150%)

---

### Item 7: Municipal Loans

| MDRM | Description |
|------|-------------|
| BHCT1709 | Direct loans to states/political subdivisions |

**Risk Weight**:
- General obligations: 20%
- Revenue bonds: 50%

---

### Item 8: Other Loans

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| 8 (Total) | BHCT1563 | Total other loans |
| 8.a | BHCK1545 | Loans for purchasing/carrying securities |
| 8.b | BHCK1564 | All other loans |

**Item 8.a**: Margin loans to broker-dealers and individuals

---

### Item 9: Lease Financing Receivables

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| 9 (Total) | BHCTB541 | Total leases |
| 9.a | BHCKF164 | Consumer leases |
| 9.b | BHCTF165 | Commercial leases |

**Lease Types**:
- Direct financing leases
- Leveraged leases
- Operating leases (equipment)

---

### Item 10: LESS: Unearned Income

| MDRM | Description |
|------|-------------|
| BHCT2123 | Unearned income on loans |

**Nature**: Deferred loan fees and discounts that will be recognized over loan life

---

### Item 11: LESS: Allowance for Loan and Lease Losses

| MDRM | Description | Ties To |
|------|-------------|---------|
| BHCT3123 | Allowance for credit losses | HC Item 4.c |

**CECL Note**: Under ASC 326 (CECL), this represents lifetime expected credit losses on loans held at amortized cost.

**Adequacy Analysis**:
```
Allowance Ratio = BHCT3123 / (Sum Items 1-9 - Item 10)
Coverage Ratio = BHCT3123 / Nonperforming Loans (HC-N)
```

---

### Item 12: Net Loans and Leases

| MDRM | Formula | Ties To |
|------|---------|---------|
| BHCTB529 | Items 1-9 - Item 10 - Item 11 | HC Item 4.d |

---

## Reconciliation to Schedule HC

```
SCHEDULE HC-C                           SCHEDULE HC
═══════════════════════════════════════════════════════════════════════

Item 12 (Net Loans)            ────────► HC Item 4.d (Net loans)
BHCTB529                                 BHCTB529

Items 1-9 minus Item 10        ────────► HC Item 4.b (Loans net of unearned)
                                         BHCTB528

Item 11 (Allowance)            ────────► HC Item 4.c (Allowance)
BHCT3123                                 BHCT3123
```

---

## Ties to Other Schedules

### HC-N (Past Due and Nonaccrual)

Schedule HC-N breaks down the same loan categories by delinquency status:
- 30-89 days past due
- 90+ days past due and still accruing
- Nonaccrual

**Reconciliation**: HC-N totals by loan type should equal HC-C line items.

### HC-H (Interest Sensitivity)

Schedule HC-H reports loans by repricing/maturity bucket:
- 3 months or less
- 3-12 months
- 1-3 years
- 3-5 years
- 5-15 years
- Over 15 years

### HC-R (Regulatory Capital)

HC-C loan categories map to HC-R Part II risk-weighted asset calculations:
- Each loan category has an assigned risk weight
- Total RWA = Sum of (Loan Balance × Risk Weight)

---

## Risk Weight Summary

| Loan Category | Standard Risk Weight |
|---------------|---------------------|
| 1-4 Family First Lien (prudent) | 35-50% |
| 1-4 Family Junior Lien | 100% |
| Multifamily (gov't guaranteed) | 20% |
| Multifamily (other) | 50-100% |
| CRE (all) | 100% |
| Construction (HVCRE) | 150% |
| Construction (other) | 100% |
| C&I | 100% |
| Consumer (auto) | 75% |
| Consumer (other) | 100% |
| Credit cards | 100% |

---

## Key Analytical Metrics

### Portfolio Composition
```
RE Concentration = Item 1 / Sum(Items 1-9)
CRE Concentration = (Item 1.a + 1.e + 1.f) / Total Capital
C&I % = Item 4 / Sum(Items 1-9)
Consumer % = Item 5 / Sum(Items 1-9)
```

### Credit Quality
```
Allowance Ratio = Item 11 / Gross Loans
Net Charge-Off Rate = (Charge-offs - Recoveries) / Average Loans [from HI]
```

### Growth Metrics
```
Loan Growth = (Current Period - Prior Period) / Prior Period
```

---

## Historical Changes

| Date | Change |
|------|--------|
| 1976-03-31 | Original FR Y-9C implementation |
| 1991-03-31 | HELOC/closed-end split introduced |
| 2007-03-31 | Construction sub-categories; first/junior lien split |
| 2010-03-31 | Credit card consumer/commercial split |
| 2015-03-31 | Auto loans new/used split |
| 2020-03-31 | CECL implementation |
| 2022-03-31 | Multifamily guaranteed/other split |

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCT1410 | Real estate loans (total) |
| 1.a | BHCT1415 | Construction |
| 1.c | BHCK1797 | HELOCs |
| 1.d | BHCT5367 | 1-4 family closed-end |
| 1.e | BHCT1460 | Multifamily |
| 1.f | BHCT1480 | Nonfarm nonresidential (CRE) |
| 3 | BHCK1590 | Agricultural |
| 4 | BHCT1766 | C&I loans |
| 5 | BHCK1975 | Consumer loans |
| 5.a | BHCKB538 | Credit cards |
| 5.c | BHCKK137 | Auto loans |
| 9 | BHCTB541 | Leases |
| 10 | BHCT2123 | Unearned income |
| 11 | BHCT3123 | **ALLOWANCE** |
| 12 | BHCTB529 | **NET LOANS** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
