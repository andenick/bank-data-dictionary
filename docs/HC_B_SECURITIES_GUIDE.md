# Schedule HC-B: Securities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-B - Securities
**Frequency**: Quarterly
**Purpose**: Detail all debt and equity securities held by the BHC

---

## Overview

Schedule HC-B provides a comprehensive breakdown of the institution's securities portfolio by:
- **Security Type**: Treasury, agency, MBS, ABS, munis, corporate, equity
- **Accounting Classification**: Available-for-Sale (AFS) vs. Held-to-Maturity (HTM)
- **Valuation Basis**: Amortized cost and fair value for each category

### Accounting Classifications

| Classification | Valuation | Unrealized G/L Treatment |
|----------------|-----------|--------------------------|
| **AFS** | Fair value | AOCI (equity) |
| **HTM** | Amortized cost | Not recognized until sale |
| **Equity** | Fair value | Income statement |

---

## Schedule Structure

```
COLUMN A: AFS Amortized Cost
COLUMN B: AFS Fair Value → ties to HC Item 2.b
COLUMN C: HTM Amortized Cost → ties to HC Item 2.a
COLUMN D: HTM Fair Value (disclosure only)

ROW ITEMS:
├── Item 1: U.S. Treasury securities
├── Item 2: U.S. Government agency obligations (non-MBS)
├── Item 3: Residential MBS
│   ├── 3.a: GNMA pass-through
│   ├── 3.b: FNMA/FHLMC pass-through
│   └── 3.c: Other residential MBS (non-agency)
├── Item 4: Commercial MBS
│   ├── 4.a: Agency issued
│   └── 4.b: Non-agency
├── Item 5: Asset-backed securities
│   ├── 5.a: Credit card receivables
│   ├── 5.b: Home equity lines
│   ├── 5.c: Automobile loans
│   ├── 5.d: Other consumer loans
│   ├── 5.e: C&I loans (CLOs)
│   └── 5.f: Other
├── Item 6: Other debt securities
│   ├── 6.a: Domestic issuers
│   └── 6.b: Foreign issuers
├── Item 7: Municipal securities
└── Item 8: TOTAL
```

---

## Detailed Line Item Analysis

### Item 1: U.S. Treasury Securities

| Column | MDRM | Description |
|--------|------|-------------|
| A (AFS Cost) | BHCK1286 | AFS Treasuries at amortized cost |
| B (AFS FV) | BHCK1287 | AFS Treasuries at fair value |
| C (HTM Cost) | BHCK0211 | HTM Treasuries at amortized cost |
| D (HTM FV) | BHCK0213 | HTM Treasuries at fair value |

**Characteristics**:
- Zero credit risk (US government backing)
- Highly liquid
- Key component of HQLA (High Quality Liquid Assets)
- LCR Level 1 assets

---

### Item 2: U.S. Government Agency Obligations (Excluding MBS)

| Column | MDRM | Description |
|--------|------|-------------|
| A (AFS Cost) | BHCKJF77 | AFS agency debt at amortized cost |
| B (AFS FV) | BHCKJF78 | AFS agency debt at fair value |
| C (HTM Cost) | BHCK1289 | HTM agency debt at amortized cost |
| D (HTM FV) | BHCK1290 | HTM agency debt at fair value |

**Includes**:
- GNMA, FNMA, FHLMC non-MBS obligations
- FHLB debentures
- TVA bonds
- Small Business Administration securities

**Excludes**: All MBS (reported in Items 3-4)

---

### Item 3: Residential Mortgage-Backed Securities

#### Item 3.a: GNMA Pass-Through Securities

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCKG300 | AFS GNMA MBS amortized cost |
| B | BHCKG301 | AFS GNMA MBS fair value |
| C | BHCKG303 | HTM GNMA MBS amortized cost |
| D | BHCKG304 | HTM GNMA MBS fair value |

**Characteristics**:
- Full faith and credit US government guarantee
- Zero credit risk, prepayment risk only
- LCR Level 1 HQLA

#### Item 3.b: FNMA/FHLMC Pass-Through Securities

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCKG308 | AFS FNMA/FHLMC MBS amortized cost |
| B | BHCKG309 | AFS FNMA/FHLMC MBS fair value |
| C | BHCKG311 | HTM FNMA/FHLMC MBS amortized cost |
| D | BHCKG312 | HTM FNMA/FHLMC MBS fair value |

**Characteristics**:
- GSE guarantee (implicit government support)
- LCR Level 2A HQLA (85% haircut)

#### Item 3.c: Other Residential MBS (Non-Agency)

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCKG316 | AFS non-agency RMBS amortized cost |
| B | BHCKG317 | AFS non-agency RMBS fair value |
| C | BHCKG319 | HTM non-agency RMBS amortized cost |
| D | BHCKG320 | HTM non-agency RMBS fair value |

**Characteristics**:
- Private label / non-agency
- Credit risk based on underlying loans
- NOT HQLA eligible
- Higher yield, higher risk

---

### Item 4: Commercial Mortgage-Backed Securities

#### Item 4.a: Agency CMBS

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCKK142 | AFS agency CMBS amortized cost |
| B | BHCKK143 | AFS agency CMBS fair value |
| C | BHCKK145 | HTM agency CMBS amortized cost |
| D | BHCKK146 | HTM agency CMBS fair value |

**Issuers**: GNMA, FNMA, FHLMC multifamily programs

#### Item 4.b: Non-Agency CMBS

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCKK150 | AFS non-agency CMBS amortized cost |
| B | BHCKK151 | AFS non-agency CMBS fair value |
| C | BHCKK153 | HTM non-agency CMBS amortized cost |
| D | BHCKK154 | HTM non-agency CMBS fair value |

**Risk Factors**:
- Commercial real estate credit risk
- Property type concentration
- Geographic concentration

---

### Item 5: Asset-Backed Securities

**Total ABS MDRM Codes**:

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCKC026 | AFS total ABS amortized cost |
| B | BHCKC027 | AFS total ABS fair value |
| C | BHCK1737 | HTM total ABS amortized cost |
| D | BHCK1738 | HTM total ABS fair value |

**Sub-Categories**:

| Sub-Item | Description | AFS Cost | AFS FV | HTM Cost | HTM FV |
|----------|-------------|----------|--------|----------|--------|
| 5.a | Credit card receivables | BHCKB838 | BHCKB839 | BHCKB840 | BHCKB841 |
| 5.b | Home equity lines | BHCKB842 | BHCKB843 | BHCKB844 | BHCKB845 |
| 5.c | Automobile loans | BHCKB846 | BHCKB847 | BHCKB848 | BHCKB849 |
| 5.d | Other consumer loans | BHCKB850 | BHCKB851 | BHCKB852 | BHCKB853 |
| 5.e | C&I loans (CLOs) | BHCKB854 | BHCKB855 | BHCKB856 | BHCKB857 |
| 5.f | Other | BHCKB858 | BHCKB859 | BHCKB860 | BHCKB861 |

**Item 5 Reconciliation**:
```
Item 5 = Item 5.a + 5.b + 5.c + 5.d + 5.e + 5.f
```

---

### Item 6: Other Debt Securities

#### Item 6.a: Domestic Issuers

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCK1739 | AFS domestic corporate amortized cost |
| B | BHCK1741 | AFS domestic corporate fair value |
| C | BHCK1742 | HTM domestic corporate amortized cost |
| D | BHCK1743 | HTM domestic corporate fair value |

**Includes**: Corporate bonds, bank debt, other domestic non-government debt

#### Item 6.b: Foreign Issuers

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCK1744 | AFS foreign corporate amortized cost |
| B | BHCK1746 | AFS foreign corporate fair value |
| C | BHCK1747 | HTM foreign corporate amortized cost |
| D | BHCK1748 | HTM foreign corporate fair value |

**Includes**: Foreign government bonds, foreign corporate debt, sovereign debt

---

### Item 7: Securities Issued by States and Political Subdivisions

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCK8496 | AFS munis amortized cost |
| B | BHCK8497 | AFS munis fair value |
| C | BHCK8498 | HTM munis amortized cost |
| D | BHCK8499 | HTM munis fair value |

**Tax Treatment**: Generally tax-exempt for federal income tax purposes

---

### Item 8: Total Securities

| Column | MDRM | Description | Ties To |
|--------|------|-------------|---------|
| A | BHCT1772 | Total AFS amortized cost | - |
| B | BHCT1773 | Total AFS fair value | HC Item 2.b |
| C | BHCT1754 | Total HTM amortized cost | HC Item 2.a |
| D | BHCTJJ34 | Total HTM fair value | - |

**Reconciliation**:
```
Item 8 = Sum(Items 1-7) for each column

Schedule HC Ties:
HC Item 2.a (HTM securities) = HC-B Item 8, Column C (BHCTJJ34)
HC Item 2.b (AFS securities) = HC-B Item 8, Column B (BHCT1773)
```

---

## Memoranda Items

### M1: Pledged Securities

| MDRM | Description |
|------|-------------|
| BHCT0416 | AFS securities pledged |
| BHCT0417 | HTM securities pledged |

**Purpose**: Identifies securities encumbered as collateral for:
- Public deposits
- Repo agreements
- FHLB advances
- Derivative margin

---

### M2: Structured Financial Products

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| M2.a | BHCKC989 | SFPs - Investment grade |
| M2.b | BHCKC990 | SFPs - Below investment grade |

**Includes**: CDOs, CLOs, CDO-squared, and similar structures

**Regulatory Concern**: Post-2008 heightened scrutiny of complex structured products

---

### M3: AOCI on AFS Securities

| MDRM | Description |
|------|-------------|
| BHCK8434 | AOCI - Unrealized gains/losses on AFS (pre-tax) |

**Calculation**:
```
AOCI = AFS Fair Value (Col B) - AFS Amortized Cost (Col A)
     = BHCT1773 - BHCT1772
```

**Impact**: Flows through to equity (HC Item 27.a) but excluded from regulatory capital for most banks under AOCI opt-out

---

### M5: Equity Securities

| MDRM | Description | Ties To |
|------|-------------|---------|
| BHCTJJ32 | Total equity securities with determinable FV | HC Item 2.c |
| BHCKJJ33 | Mutual funds and ETFs | - |
| BHCKJJ35 | Other equity securities | - |

**Note**: Per ASU 2016-01 (effective 2018), equity securities are carried at fair value with changes recognized in income (not AOCI).

---

### M6: Equity Securities Without Readily Determinable Fair Value

| MDRM | Description |
|------|-------------|
| BHCK1752 | Equity securities without determinable FV |

**Includes**:
- FHLB stock
- Federal Reserve Bank stock
- Bankers' bank stock
- Community development investments

**Accounting**: Measured at cost less impairment, plus/minus observable price changes

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

## Reconciliation Hierarchy

```
SCHEDULE HC-B                           SCHEDULE HC
═══════════════════════════════════════════════════════════════════════

Item 8, Column B (AFS FV)      ────────► HC Item 2.b (AFS securities)
BHCT1773                                 BHCT1773

Item 8, Column C (HTM Cost)    ────────► HC Item 2.a (HTM securities)
BHCTJJ34                                 BHCTJJ34

M5 (Equity with FV)            ────────► HC Item 2.c (Equity securities)
BHCTJJ32                                 BHCTJJ32


SCHEDULE HC-B                           SCHEDULE HC-R (Capital)
═══════════════════════════════════════════════════════════════════════

Total Securities               ────────► Part II: Risk-Weighted Assets
                                         (by risk weight category)
```

---

## Key Analytical Ratios

### Portfolio Composition
```
Treasury % = Item 1 / Item 8
Agency % = (Item 2 + Item 3.a + 3.b + 4.a) / Item 8
Non-Agency % = (Item 3.c + 4.b) / Item 8
ABS % = Item 5 / Item 8
```

### Duration/Interest Rate Risk Indicators
```
HTM % = Column C Total / (Column B + Column C Totals)
- Higher HTM % = more locked-in positions, less flexibility
- Lower HTM % = more mark-to-market exposure in AOCI
```

### Unrealized Gain/Loss
```
Unrealized G/L = Fair Value - Amortized Cost
AFS Unrealized = BHCT1773 - BHCT1772
HTM Unrealized = BHCTJJ34 - BHCT1754 (disclosed but not recognized)
```

---

## Historical Changes

| Date | Change |
|------|--------|
| 1994-03-31 | FAS 115 - AFS/HTM classification introduced |
| 2011-03-31 | MBS granular breakdown (GNMA, FNMA/FHLMC, Other) |
| 2011-03-31 | ABS sub-categories added |
| 2018-03-31 | ASU 2016-01 - Equity securities FV through income |
| 2020-03-31 | CECL implementation - PCD securities (M7) |

---

## MDRM Quick Reference - Column B (AFS Fair Value)

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCK1287 | Treasury |
| 2 | BHCKJF78 | Agency (non-MBS) |
| 3.a | BHCKG301 | GNMA MBS |
| 3.b | BHCKG309 | FNMA/FHLMC MBS |
| 3.c | BHCKG317 | Non-agency RMBS |
| 4.a | BHCKK143 | Agency CMBS |
| 4.b | BHCKK151 | Non-agency CMBS |
| 5 | BHCKC027 | ABS total |
| 6.a | BHCK1741 | Domestic corporate |
| 6.b | BHCK1746 | Foreign corporate |
| 7 | BHCK8497 | Munis |
| 8 | BHCT1773 | **TOTAL AFS FV** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
