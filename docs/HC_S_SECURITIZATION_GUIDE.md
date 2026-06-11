# Schedule HC-S: Servicing, Securitization, and Asset Sale Activities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-S - Servicing, Securitization, and Asset Sale Activities
**Frequency**: Quarterly
**Purpose**: Disclose securitization activities (own and others'), asset sales, and servicing

---

## Overview

The **current** FR Y-9C HC-S is organized as a **seven-column grid** (columns A-G by collateral
type) for the main securitization items, followed by single/partial-column items for facilities
sponsored by others, asset sales, and memoranda. Earlier versions of this guide described a
pre-2009 "Originator / Investor / Servicer" layout (items 5-8 with codes B764-B775) that is **no
longer on the form**; the current investor/servicer disclosures were dropped or moved, and the
schedule is now collateral-type-segmented.

### Column Definitions (A-G)

| Column | Collateral type |
|--------|-----------------|
| A | 1-4 Family Residential Loans |
| B | Home Equity Lines |
| C | Credit Card Receivables |
| D | Auto Loans |
| E | Other Consumer Loans |
| F | Commercial and Industrial Loans |
| G | All Other Loans, All Leases, and All Other Assets |

---

## Schedule Structure (current FR Y-9C)

```
SECURITIZATION ACTIVITIES (own structures) — columns A-G
├── 1. Outstanding principal balance sold and securitized (servicing retained / recourse)
├── 2. Maximum credit exposure from recourse/seller-provided enhancements (item 1)
├── 3. Unused commitments to provide liquidity to item-1 structures   [$100B+ filers]
├── 4. Past due amounts in item 1  (4.a 30-89 days, 4.b 90+ days)
├── 5. Charge-offs (5.a) and recoveries (5.b) on item-1 assets (YTD)
└── 6. Total ownership (seller's) interest carried as securities/loans (cols A-C)  [$10B+ filers]

FACILITIES SPONSORED BY OTHERS — partial columns
├── 9.  Max credit exposure from enhancements to OTHER institutions' structures (cols A-E)
└── 10. Unused liquidity commitments to OTHER institutions' structures (cols A-E)  [$10B+ filers]

ASSET SALES (not securitized) — columns A-B
├── 11. Assets sold with recourse/seller-provided enhancements, not securitized
└── 12. Max credit exposure from enhancements to item-11 assets

MEMORANDA (single column)
├── M.2.a-d. Assets serviced for others (1-4 family w/ & w/o recourse, other, in-foreclosure)
├── M.3.a-b. ABCP conduit credit exposure & liquidity commitments (sponsored by bank / by others)
└── M.4.    Outstanding credit card fees and finance charges (in item 1, column G)
```

> Items 7 and 8 are "Not applicable" on the current form.

---

## Securitization Activities (items 1-6)

### Item 1: Outstanding Principal Balance Sold and Securitized

Servicing retained or with recourse / other seller-provided credit enhancements. Reported across
columns A-G.

| Column | A | B | C | D | E | F | G |
|--------|---|---|---|---|---|---|---|
| MDRM | B705 | B706 | B707 | B708 | B709 | B710 | B711 |

### Item 2: Maximum Credit Exposure (item 1 structures)

| Column | A | B | C | D | E | F | G |
|--------|---|---|---|---|---|---|---|
| MDRM | HU09 | HU10 | HU11 | HU12 | HU13 | HU14 | HU15 |

> Current codes are **HU09-HU15** (effective 2018-06-30). The pre-2018 single code BHCKB712 is
> superseded.

### Item 3: Unused Liquidity Commitments (item 1 structures)

Columns A-G = B726-B732. To be completed by holding companies with $100 billion or more in total assets.

### Item 4: Past Due Amounts (included in item 1)

| Sub-item | Columns A-G |
|----------|-------------|
| 4.a (30-89 days) | B733-B739 |
| 4.b (90+ days) | B740-B746 |

### Item 5: Charge-offs and Recoveries (YTD, item 1 assets)

| Sub-item | Columns A-G |
|----------|-------------|
| 5.a (charge-offs) | B747-B753 |
| 5.b (recoveries) | B754-B760 |

### Item 6: Total Ownership (Seller's) Interest

Carried as securities or loans; columns A-C only = HU16, HU17, HU18 (effective 2018-06-30,
$10B+ filers).

---

## Facilities Sponsored by Others (items 9-10)

### Item 9: Maximum Credit Exposure to Others' Structures

Standby letters of credit, purchased subordinated securities, and other enhancements; columns
A-E = B776, B779, B780, B781, B782.

### Item 10: Unused Liquidity Commitments to Others' Structures

Columns A-E = B783, B786, B787, B788, B789 ($10B+ filers).

---

## Asset Sales (items 11-12)

| Item | Description | Col A | Col B |
|------|-------------|-------|-------|
| 11 | Assets sold with recourse/seller-provided enhancements, NOT securitized | B790 | B796 |
| 12 | Maximum credit exposure for item-11 assets | B797 | B803 |

---

## Memoranda

| Item | MDRM | Description |
|------|------|-------------|
| M.2.a | BHCKB804 | 1-4 family resi mortgages serviced WITH recourse/servicer enhancements |
| M.2.b | BHCKB805 | 1-4 family resi mortgages serviced with NO recourse/servicer enhancements |
| M.2.c | BHCKA591 | Other financial assets serviced for others |
| M.2.d | BHCKF699 | 1-4 family resi mortgages serviced for others in foreclosure at quarter-end |
| M.3.a.(1) | BHCKB806 | ABCP credit exposure - conduits sponsored by bank/affiliate/holding company |
| M.3.a.(2) | BHCKB807 | ABCP credit exposure - conduits sponsored by other unrelated institutions |
| M.3.b.(1) | BHCKB808 | ABCP unused liquidity - conduits sponsored by bank/affiliate/holding company |
| M.3.b.(2) | BHCKB809 | ABCP unused liquidity - conduits sponsored by other unrelated institutions |
| M.4 | BHCKC407 | Outstanding credit card fees and finance charges (in item 1, column G) |

> Note: prior guide listed M1=B806 / M2=B807; on the current form these are **M.3.a.(1)** and
> **M.3.a.(2)**, and B808/B809 (liquidity) and the M.2 servicing block are added.

---

## Analytical Applications

### Securitization Activity Level

```
Total securitized (item 1) = Sum across columns A-G of BHCKB705..B711
```

### Retained Exposure Analysis

```
Retained Risk Ratio = Item 2 (max credit exposure) / Item 1 (outstanding securitized)
Higher ratio = more "skin in the game"; Dodd-Frank requires >=5% retention.
```

### Asset Quality of Securitized Pools

```
Delinquency = (Item 4.a + Item 4.b) / Item 1   (by collateral column)
Net loss     = Item 5.a (charge-offs) - Item 5.b (recoveries)
```

---

## Cross-Schedule Reconciliation

### Off-Balance Sheet (HC-L)

```
Liquidity and credit-enhancement commitments to unconsolidated securitization vehicles also
surface in HC-L off-balance-sheet items.
```

### Variable Interest Entities (HC-V)

```
Consolidated securitization vehicles (VIEs) are reported on Schedule HC-V.
```

---

## MDRM Quick Reference

| Category | Item | MDRM (col A) |
|----------|------|--------------|
| Securitized - outstanding | 1 | BHCKB705 |
| Max credit exposure (own) | 2 | BHCKHU09 |
| Liquidity commitments (own) | 3 | BHCKB726 |
| Ownership interest | 6 | BHCKHU16 |
| Max credit exposure (others) | 9 | BHCKB776 |
| Liquidity commitments (others) | 10 | BHCKB783 |
| Assets sold not securitized | 11 | BHCKB790 |
| Servicing (with recourse) | M.2.a | BHCKB804 |
| ABCP conduit credit exposure | M.3.a.(1) | BHCKB806 |
| Credit card fees | M.4 | BHCKC407 |

---

*Last Updated: 2026-06-11 (v8 conceptual-accuracy sweep)*
*Reference: FR Y-9C field spec (202603), MDRM, and FreeNIC warehouse*
