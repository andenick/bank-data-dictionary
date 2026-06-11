# Schedule HC-B: Securities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-B - Securities
**Frequency**: Quarterly
**Purpose**: Detail all debt securities (and selected equity disclosures) held by the BHC

---

## Overview

Schedule HC-B provides a comprehensive breakdown of the institution's securities portfolio by:
- **Security Type**: Treasury, U.S. agency, munis, MBS, ABS, structured products, other debt
- **Accounting Classification**: Held-to-Maturity (HTM) vs. Available-for-Sale (AFS)
- **Valuation Basis**: Amortized cost and fair value for each classification

### Accounting Classifications

| Classification | Carrying Value | Unrealized G/L Treatment |
|----------------|----------------|--------------------------|
| **HTM** | Amortized cost | Not recognized until sale (FV disclosed) |
| **AFS** | Fair value | AOCI (equity) |
| **Equity (M.5)** | Fair value | Income statement (ASU 2016-01) |

---

## Column Scheme (CURRENT FORM)

The current FR Y-9C HC-B reports **four columns** for each line item, in this order:

```
COLUMN A: Held-to-maturity  — AMORTIZED COST   (carrying value of HTM)
COLUMN B: Held-to-maturity  — FAIR VALUE       (disclosure only)
COLUMN C: Available-for-sale — AMORTIZED COST   (cost basis of AFS)
COLUMN D: Available-for-sale — FAIR VALUE       (carrying value of AFS)
```

Verified against item 1 (A=BHCK0211 HTM amortized cost, B=BHCK0213 HTM fair value, C=BHCK1286 AFS amortized cost, D=BHCK1287 AFS fair value) and item 8 totals (A=BHCK1754 HTM total, B=BHCK1771 HTM FV total, C=BHCK1772 AFS amortized-cost total, D=BHCT1773 AFS FV total).

> **CSV layout note**: the companion `csv/HC_B_SECURITIES.csv` carries four MDRM columns named `mdrm_afs_amortized_cost`, `mdrm_afs_fair_value`, `mdrm_htm_amortized_cost`, `mdrm_htm_fair_value`. These are mapped **by meaning**, not by form column position:
> - `mdrm_htm_amortized_cost` ← Column A
> - `mdrm_htm_fair_value` ← Column B
> - `mdrm_afs_amortized_cost` ← Column C
> - `mdrm_afs_fair_value` ← Column D

---

## Schedule Structure

```
COLUMN A: HTM Amortized Cost  → item 8 col A (BHCK1754) ties to HC item 2.a
COLUMN B: HTM Fair Value      (disclosure only)
COLUMN C: AFS Amortized Cost
COLUMN D: AFS Fair Value      → item 8 col D (BHCT1773) ties to HC item 2.b

ROW ITEMS:
├── Item 1: U.S. Treasury securities
├── Item 2: U.S. government agency obligations (exclude MBS)
├── Item 3: Securities issued by states and political subdivisions in the U.S. (munis)
├── Item 4: Mortgage-backed securities (MBS)
│   ├── 4.a: Residential MBS pass-through securities
│   │   ├── 4.a.(1): Guaranteed by GNMA
│   │   ├── 4.a.(2): Issued by FNMA and FHLMC
│   │   ├── 4.a.(3): Other pass-through securities
│   │   └── 4.a.(4): Guaranteed by GNMA, issued by FNMA/FHLMC, and other pass-through
│   ├── 4.b: Other residential MBS (CMOs, REMICs, stripped MBS)
│   │   ├── 4.b.(1): Issued or guaranteed by U.S. Gov agencies or sponsored agencies
│   │   ├── 4.b.(2): Collateralized by agency/GSE MBS
│   │   └── 4.b.(3): All other residential MBS
│   └── 4.c: Commercial MBS
│       ├── 4.c.(1): Pass-through
│       │   ├── (a): Issued or guaranteed by FNMA, FHLMC, or GNMA
│       │   └── (b): Other pass-through securities
│       └── 4.c.(2): Other commercial MBS
│           ├── (a): Issued or guaranteed by U.S. Gov agencies or sponsored agencies
│           └── (b): All other commercial MBS
├── Item 5: Asset-backed securities and structured financial products
│   ├── 5.a: Asset-backed securities (ABS)
│   └── 5.b: Structured financial products
├── Item 6: Other debt securities
│   ├── 6.a: Other domestic debt securities
│   └── 6.b: Other foreign debt securities
├── Item 7: Unallocated portfolio layer fair value hedge basis adjustments
└── Item 8: TOTAL (sum of items 1 through 7)
```

---

## Detailed Line Item Analysis

(Tables list MDRM codes by form column: A = HTM amortized cost, B = HTM fair value, C = AFS amortized cost, D = AFS fair value.)

### Item 1: U.S. Treasury Securities

| Column | MDRM | Description |
|--------|------|-------------|
| A (HTM Cost) | BHCK0211 | HTM Treasuries at amortized cost |
| B (HTM FV)   | BHCK0213 | HTM Treasuries at fair value |
| C (AFS Cost) | BHCK1286 | AFS Treasuries at amortized cost |
| D (AFS FV)   | BHCK1287 | AFS Treasuries at fair value |

**Characteristics**: Zero credit risk (U.S. government backing); highly liquid; LCR Level 1 HQLA.

---

### Item 2: U.S. Government Agency Obligations (Excluding MBS)

| Column | MDRM | Description |
|--------|------|-------------|
| A (HTM Cost) | BHCKHT50 | HTM agency obligations at amortized cost |
| B (HTM FV)   | BHCKHT51 | HTM agency obligations at fair value |
| C (AFS Cost) | BHCKHT52 | AFS agency obligations at amortized cost |
| D (AFS FV)   | BHCKHT53 | AFS agency obligations at fair value |

**Includes**: FHLB debentures, SBA securities, TVA bonds, and other non-MBS agency obligations.
**Excludes**: All MBS (reported in item 4).

> **Code history**: the current form uses **BHCKHT50–HT53** (open since 2018-06-30). These replaced the retired pairs BHCK1289/1290 (HTM, closed 2018-03-31). The old repo build used BHCKJF77/JF78 for AFS agency — those codes actually mean *"Total assets/liabilities of ABCP conduit VIEs"* and were a concept error, now corrected.

---

### Item 3: Securities Issued by States and Political Subdivisions in the U.S.

| Column | MDRM | Description |
|--------|------|-------------|
| A (HTM Cost) | BHCK8496 | HTM munis at amortized cost |
| B (HTM FV)   | BHCK8497 | HTM munis at fair value |
| C (AFS Cost) | BHCK8498 | AFS munis at amortized cost |
| D (AFS FV)   | BHCK8499 | AFS munis at fair value |

**Tax Treatment**: Generally tax-exempt for federal income tax purposes.
**Placement note**: On the current form, municipals are **item 3**. (The old repo layout incorrectly placed munis at item 7.)

---

### Item 4: Mortgage-Backed Securities

#### Item 4.a: Residential MBS Pass-Through Securities

| Line | Description | A (HTM Cost) | B (HTM FV) | C (AFS Cost) | D (AFS FV) |
|------|-------------|--------------|-----------|--------------|-----------|
| 4.a.(1) | Guaranteed by GNMA | BHCKG300 | BHCKG301 | BHCKG302 | BHCKG303 |
| 4.a.(2) | Issued by FNMA and FHLMC | BHCKG304 | BHCKG305 | BHCKG306 | BHCKG307 |
| 4.a.(3) | Other pass-through securities | BHCKG308 | BHCKG309 | BHCKG310 | BHCKG311 |
| 4.a.(4) | Guaranteed by GNMA, issued by FNMA/FHLMC, and other pass-through | BHCKKX52 | BHCKKX53 | BHCKKX54 | BHCKKX55 |

#### Item 4.b: Other Residential MBS (CMOs, REMICs, Stripped MBS)

| Line | Description | A (HTM Cost) | B (HTM FV) | C (AFS Cost) | D (AFS FV) |
|------|-------------|--------------|-----------|--------------|-----------|
| 4.b.(1) | Issued or guaranteed by U.S. Gov agencies/sponsored agencies | BHCKG312 | BHCKG313 | BHCKG314 | BHCKG315 |
| 4.b.(2) | Collateralized by agency/GSE MBS | BHCKG316 | BHCKG317 | BHCKG318 | BHCKG319 |
| 4.b.(3) | All other residential MBS | BHCKG320 | BHCKG321 | BHCKG322 | BHCKG323 |

#### Item 4.c: Commercial MBS

| Line | Description | A (HTM Cost) | B (HTM FV) | C (AFS Cost) | D (AFS FV) |
|------|-------------|--------------|-----------|--------------|-----------|
| 4.c.(1)(a) | Pass-through: Issued/guaranteed by FNMA, FHLMC, or GNMA | BHCKK142 | BHCKK143 | BHCKK144 | BHCKK145 |
| 4.c.(1)(b) | Pass-through: Other | BHCKK146 | BHCKK147 | BHCKK148 | BHCKK149 |
| 4.c.(2)(a) | Other CMBS: Issued/guaranteed by U.S. Gov agencies/sponsored agencies | BHCKK150 | BHCKK151 | BHCKK152 | BHCKK153 |
| 4.c.(2)(b) | Other CMBS: All other | BHCKK154 | BHCKK155 | BHCKK156 | BHCKK157 |

---

### Item 5: Asset-Backed Securities and Structured Financial Products

| Line | Description | A (HTM Cost) | B (HTM FV) | C (AFS Cost) | D (AFS FV) |
|------|-------------|--------------|-----------|--------------|-----------|
| 5.a | Asset-backed securities (ABS) | BHCKC026 | BHCKC988 | BHCKC989 | BHCKC027 |
| 5.b | Structured financial products | BHCKHT58 | BHCKHT59 | BHCKHT60 | BHCKHT61 |

ABS sub-detail by underlying asset is reported in Memorandum 5; SFP sub-detail by collateral in Memorandum 6.

---

### Item 6: Other Debt Securities

| Line | Description | A (HTM Cost) | B (HTM FV) | C (AFS Cost) | D (AFS FV) |
|------|-------------|--------------|-----------|--------------|-----------|
| 6.a | Other domestic debt securities | BHCK1737 | BHCK1738 | BHCK1739 | BHCK1741 |
| 6.b | Other foreign debt securities | BHCK1742 | BHCK1743 | BHCK1744 | BHCK1746 |

**Includes**: Corporate bonds, sovereign/foreign government debt, and other non-government debt.

---

### Item 7: Unallocated Portfolio Layer Fair Value Hedge Basis Adjustments

| Column | MDRM | Description |
|--------|------|-------------|
| (single cell) | BHCKMG95 | Unallocated portfolio layer fair value hedge basis adjustments |

Item 7 has only **one** reported cell (BHCKMG95, open since 2022-09-30). It captures basis adjustments from portfolio-layer fair-value hedges (ASU 2022-01) not allocated to individual securities. Columns B/C/D are not applicable.

---

### Item 8: Total Securities (Sum of Items 1 through 7)

| Column | MDRM | Description | Ties To |
|--------|------|-------------|---------|
| A (HTM Cost) | BHCK1754 | Total HTM amortized cost | **HC item 2.a** |
| B (HTM FV)   | BHCK1771 | Total HTM fair value | - |
| C (AFS Cost) | BHCK1772 | Total AFS amortized cost | - |
| D (AFS FV)   | BHCT1773 | Total AFS fair value | **HC item 2.b** |

**Reconciliation**:
```
Item 8 = Sum(Items 1-7) for each column.

Schedule HC ties:
HC item 2.a (Held-to-maturity securities) = HC-B item 8, Column A (BHCK1754)
HC item 2.b (Available-for-sale securities) = HC-B item 8, Column D (BHCT1773)
```

---

## Memoranda Items

### M.1: Pledged Securities

| MDRM | Description |
|------|-------------|
| BHCK0416 | Pledged securities (single cell) |

Securities encumbered as collateral for public deposits, repo agreements, FHLB advances, derivative margin, etc.

### M.2: Maturity / Repricing Distribution

| Line | MDRM | Description |
|------|------|-------------|
| M.2.a | BHCK0383 | Remaining maturity (or repricing) of one year or less |
| M.2.b | BHCK0384 | Over one year through five years |
| M.2.c | BHCK0387 | Over five years |

Each is a single cell. (The PDF parse garbled the M.2.a caption — reconstructed from MDRM item_name "Securities maturing in one year or less".)

### M.3: HTM Sold/Transferred to AFS or Trading (YTD)

| MDRM | Description |
|------|-------------|
| BHCK1778 | Amortized cost (at date of sale/transfer) of HTM securities sold or transferred to AFS or trading during the calendar year-to-date (single cell) |

### M.4: Structured Notes

| Line | MDRM | Description |
|------|------|-------------|
| M.4.a | BHCK8782 | Structured notes — amortized cost |
| M.4.b | BHCK8783 | Structured notes — fair value |

### M.5: Asset-Backed Securities by Underlying Assets

| Line | Description | A (HTM Cost) | B (HTM FV) | C (AFS Cost) | D (AFS FV) |
|------|-------------|--------------|-----------|--------------|-----------|
| M.5.a | Credit card receivables | BHCKB838 | BHCKB839 | BHCKB840 | BHCKB841 |
| M.5.b | Home equity lines | BHCKB842 | BHCKB843 | BHCKB844 | BHCKB845 |
| M.5.c | Automobile loans | BHCKB846 | BHCKB847 | BHCKB848 | BHCKB849 |
| M.5.d | Other consumer loans | BHCKB850 | BHCKB851 | BHCKB852 | BHCKB853 |
| M.5.e | Commercial and industrial loans | BHCKB854 | BHCKB855 | BHCKB856 | BHCKB857 |
| M.5.f | Other | BHCKB858 | BHCKB859 | BHCKB860 | BHCKB861 |

These memoranda decompose the item 5.a ABS aggregate by collateral type.

### M.6: Structured Financial Products by Underlying Collateral or Reference Assets

| Line | Description | A (HTM Cost) | B (HTM FV) | C (AFS Cost) | D (AFS FV) |
|------|-------------|--------------|-----------|--------------|-----------|
| M.6.a | Trust preferred securities issued by financial institutions | BHCKG348 | BHCKG349 | BHCKG350 | BHCKG351 |
| M.6.b | Trust preferred securities issued by REITs | BHCKG352 | BHCKG353 | BHCKG354 | BHCKG355 |
| M.6.c | Corporate and similar loans | BHCKG356 | BHCKG357 | BHCKG358 | BHCKG359 |
| M.6.d | 1-4 family residential MBS issued/guaranteed by GSEs | BHCKG360 | BHCKG361 | BHCKG362 | BHCKG363 |
| M.6.e | 1-4 family residential MBS not issued/guaranteed by GSEs | BHCKG364 | BHCKG365 | BHCKG366 | BHCKG367 |
| M.6.f | Diversified (mixed) pools of structured financial products | BHCKG368 | BHCKG369 | BHCKG370 | BHCKG371 |
| M.6.g | Other collateral or reference assets | BHCKG372 | BHCKG373 | BHCKG374 | BHCKG375 |

These memoranda decompose the item 5.b structured financial products by collateral.

### M.7: Structured Financial Products Guaranteed by U.S. Government Agencies/Sponsored Agencies (in item 5.b)

| Column | MDRM | Description |
|--------|------|-------------|
| A (HTM Cost) | BHCKPU98 | HTM amortized cost |
| B (HTM FV)   | BHCKPU99 | HTM fair value |
| C (AFS Cost) | BHCKPV00 | AFS amortized cost |
| D (AFS FV)   | BHCKPV01 | AFS fair value |

**New current-form item** effective **2026-03-31** (BHCKPU98–PV01 open 3/31/2026). It carves out the agency-guaranteed portion already included in item 5.b. Not yet present in the warehouse (data ends 2025Q4).

### Equity Securities (related HC reconciliation)

Equity securities with readily determinable fair values are reported on Schedule HC line 2.c via **BHCKJA22** (open since 2018-03-31, ASU 2016-01: fair value through income). They are not a numbered HC-B item but tie the securities portfolio to HC item 2.c.

---

## Reconciliation Hierarchy

```
SCHEDULE HC-B                              SCHEDULE HC
═══════════════════════════════════════════════════════════════════════

Item 8, Column A (HTM amort cost)  ──────► HC item 2.a (Held-to-maturity securities)
BHCK1754                                    BHCK1754

Item 8, Column D (AFS fair value)  ──────► HC item 2.b (Available-for-sale securities)
BHCT1773                                    BHCT1773

Equity securities (BHCKJA22)       ──────► HC item 2.c (Equity securities with
                                            readily determinable fair values)


SCHEDULE HC-B                              SCHEDULE HC-R (Capital)
═══════════════════════════════════════════════════════════════════════

Total Securities                   ──────► Part II: Risk-Weighted Assets
                                            (by risk-weight category)
```

---

## Risk Weight Mapping (Basel III)

| Security Type | Risk Weight | HQLA Category |
|---------------|-------------|---------------|
| U.S. Treasury | 0% | Level 1 |
| GNMA MBS | 0% | Level 1 |
| GSE Debt & MBS | 20% | Level 2A |
| Munis (General Obligation) | 20% | Level 2B (if liquid) |
| Investment Grade Corporate | 100% | Level 2B (if liquid) |
| Non-Agency MBS | 100% | Not HQLA |
| Below IG Corporate | 150% | Not HQLA |

---

## Key Analytical Ratios

### Portfolio Composition
```
Treasury % = Item 1 / Item 8
Agency % = (Item 2 + 4.a + 4.b.(1) + 4.b.(2) + 4.c agency lines) / Item 8
Non-Agency % = (4.b.(3) + 4.c.(2)(b)) / Item 8
ABS+SFP % = Item 5 / Item 8
```

### HTM vs. AFS Mix
```
HTM % = Item 8 Col A (BHCK1754) / (Col A + Col C cost totals)
- Higher HTM % = more locked-in positions, less AOCI volatility
- Lower HTM % = more mark-to-market exposure flowing through AOCI
```

### Unrealized Gain/Loss
```
AFS Unrealized = AFS Fair Value - AFS Amortized Cost = BHCT1773 - BHCK1772 (flows to AOCI)
HTM Unrealized = HTM Fair Value - HTM Amortized Cost = BHCK1771 - BHCK1754 (disclosed, not recognized)
```

---

## Historical Changes

| Date | Change |
|------|--------|
| 1994-03-31 | FAS 115 - AFS/HTM classification; Treasury, totals (0211/0213/1286/1287/1754) introduced |
| 2001-03-31 | ABS, munis, other domestic/foreign debt granular codes (8496-8499, 1737-1746, B838-B861) |
| 2006-03-31 | ABS aggregate cost/FV codes (C026/C027/C988/C989) |
| 2009-06-30 | MBS and SFP-by-collateral granular breakdown (G300+ residential MBS, G348-G375 SFP) |
| 2011-03-31 | Commercial MBS pass-through / other breakdown (K142-K157) |
| 2018-03-31 | ASU 2016-01 - equity securities at fair value through income (BHCKJA22) |
| 2018-06-30 | Agency obligations re-coded to BHCKHT50-53; structured financial products HT58-61 |
| 2019-12-31 | Combined residential pass-through line BHCKKX52-55 (item 4.a.(4)) |
| 2022-09-30 | Item 7 added: unallocated portfolio layer FV hedge basis adjustments (BHCKMG95) |
| 2026-03-31 | M.7 added: agency-guaranteed SFP within item 5.b (BHCKPU98-PV01) |

---

## MDRM Quick Reference — Column D (AFS Fair Value, carrying value of AFS)

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCK1287 | U.S. Treasury |
| 2 | BHCKHT53 | U.S. agency obligations (non-MBS) |
| 3 | BHCK8499 | Munis |
| 4.a.(1) | BHCKG303 | Residential pass-through - GNMA |
| 4.a.(2) | BHCKG307 | Residential pass-through - FNMA/FHLMC |
| 4.a.(3) | BHCKG311 | Residential pass-through - Other |
| 4.a.(4) | BHCKKX55 | Residential pass-through - combined |
| 4.b.(1) | BHCKG315 | Other residential - agency/GSE |
| 4.b.(2) | BHCKG319 | Other residential - agency-collateralized |
| 4.b.(3) | BHCKG323 | Other residential - non-agency |
| 4.c.(1)(a) | BHCKK145 | Commercial pass-through - agency |
| 4.c.(1)(b) | BHCKK149 | Commercial pass-through - other |
| 4.c.(2)(a) | BHCKK153 | Other CMBS - agency/GSE |
| 4.c.(2)(b) | BHCKK157 | Other CMBS - non-agency |
| 5.a | BHCKC027 | ABS |
| 5.b | BHCKHT61 | Structured financial products |
| 6.a | BHCK1741 | Other domestic debt |
| 6.b | BHCK1746 | Other foreign debt |
| 7 | (n/a) | Hedge basis adj. (single cell BHCKMG95) |
| 8 | BHCT1773 | **TOTAL AFS FAIR VALUE** → HC 2.b |

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C Instructions (March 2026)*
