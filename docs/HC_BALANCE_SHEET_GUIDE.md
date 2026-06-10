# Schedule HC: Consolidated Balance Sheet Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC - Consolidated Balance Sheet
**Frequency**: Quarterly
**Filers**: All bank holding companies with total consolidated assets of $3 billion or more

---

## Overview

Schedule HC is the master consolidated balance sheet for bank holding companies. It provides a high-level view of the institution's financial position and serves as the reconciliation point for all detailed sub-schedules.

### Key Characteristics

- **Consolidation Level**: Full consolidation of all subsidiaries
- **Reporting Basis**: Generally Accepted Accounting Principles (GAAP)
- **Valuation**: Mix of fair value and amortized cost depending on asset class
- **Primary Equation**: Total Assets = Total Liabilities + Total Equity

---

## Balance Sheet Structure

```
ASSETS (Items 1-12)
├── Item 1: Cash and balances due
├── Item 2: Securities → ties to HC-B
├── Item 3: Federal funds sold / reverse repos
├── Item 4: Loans and leases → ties to HC-C
├── Item 5: Trading assets → ties to HC-D
├── Items 6-9: Premises, OREO, investments
├── Item 10: Intangible assets
├── Item 11: Other assets → ties to HC-F
└── Item 12: TOTAL ASSETS

LIABILITIES (Items 13-21)
├── Item 13: Deposits
├── Items 14-16: Fed funds, trading liabs, borrowings
├── Item 19: Subordinated debt
├── Item 20: Other liabilities → ties to HC-G
└── Item 21: TOTAL LIABILITIES

EQUITY (Items 22-28)
├── Items 23-27: Preferred, common, surplus, retained, AOCI
└── Item 28: TOTAL EQUITY

BALANCING (Item 29)
└── Total Liabilities + Minority Interest + Equity = Total Assets
```

---

## Detailed Line Item Analysis

### ASSETS

#### Item 1: Cash and Balances Due from Depository Institutions

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| 1 (Total) | BHCK0010 | Total cash and due from |
| 1.a | BHCK0081 | Noninterest-bearing balances and currency/coin |
| 1.b | BHCK0395 | Interest-bearing balances |

**Components**:
- Currency and coin on hand
- Cash items in process of collection
- Balances due from Federal Reserve Banks
- Balances due from other depository institutions

**Reconciliation**:
```
Item 1 = Item 1.a + Item 1.b
```

---

#### Item 2: Securities

| Sub-Item | MDRM | Description | Ties To |
|----------|------|-------------|---------|
| 2 (Total) | BHCT8641 | Total securities | HC-B |
| 2.a | BHCKJJ34 | HTM securities (amortized cost) | HC-B Item 8 Col C |
| 2.b | BHCT1773 | AFS debt securities (fair value) | HC-B Item 8 Col B |
| 2.c | BHCKJA22 | Equity securities with determinable FV | HC-B M5 |

**Key Distinctions**:
- **HTM**: Carried at amortized cost; positive intent and ability to hold to maturity
- **AFS**: Carried at fair value; unrealized gains/losses flow to AOCI (Item 27)
- **Equity**: Carried at fair value; changes flow through income statement

**Reconciliation**:
```
Item 2 = Item 2.a + Item 2.b + Item 2.c
Item 2.a = HC-B Item 8, Column C (Total HTM amortized cost)
Item 2.b = HC-B Item 8, Column B (Total AFS fair value)
```

**Note**: The fair value amounts differ from book value for HTM securities. HC-B provides both amortized cost and fair value for all securities.

---

#### Item 3: Federal Funds Sold and Securities Purchased Under Resale Agreements

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| 3 (Total) | BHCKC225 | Total fed funds sold and reverse repos |
| 3.a | BHCKB987 | Federal funds sold |
| 3.b | BHCKB989 | Securities purchased under resale agreements |

**Nature**:
- Short-term lending to other financial institutions
- Reverse repos = collateralized lending
- Important component of liquidity management

---

#### Item 4: Loans and Lease Financing Receivables

| Sub-Item | MDRM | Description | Ties To |
|----------|------|-------------|---------|
| 4.a | BHCT5369 | Loans and leases held for sale | HC-C Item 10 |
| 4.b | BHCTB528 | Loans and leases, net of unearned income | HC-C Items 1-9 minus Item 10 |
| 4.c | BHCT3123 | LESS: Allowance for loan losses | HC-C Item 11 |
| 4.d | BHCKB529 | Net loans and leases | Item 4.a + Item 4.b - Item 4.c |

**Reconciliation to HC-C**:
```
Gross Loans (HC-C) = Sum(Items 1-9) = Real estate + Ag + C&I + Consumer + Other + Leases
Net of Unearned = Gross - Unearned income fees
Net Loans = Net of Unearned - Allowance

HC Item 4.b = HC-C Items 1-9 - HC-C Item 10
HC Item 4.c = HC-C Item 11
HC Item 4.d = HC Item 4.a + HC Item 4.b - HC Item 4.c
```

---

#### Item 5: Trading Assets

| Sub-Item | MDRM | Description | Ties To |
|----------|------|-------------|---------|
| 5 (Total) | BHCT3545 | Total trading assets | HC-D Item 12 |
| 5.a | BHDM3545 | Trading assets in domestic offices | - |

**Reconciliation to HC-D**:
```
Item 5 = HC-D Item 12
      = HC-D Items 1-11 (Securities + Loans + Derivatives + Other)
```

**Components (from HC-D)**:
- U.S. Treasury, agency, municipal securities
- MBS (residential and commercial)
- Structured products, other debt
- Loans held for trading
- Derivative contracts with positive fair value

---

#### Items 6-10: Other Asset Categories

| Item | MDRM | Description | Ties To |
|------|------|-------------|---------|
| 6 | BHCK2145 | Premises and fixed assets | HC-F Item 6 |
| 7 | BHCT2150 | Other real estate owned | HC-F Item 7 |
| 8 | BHCK2130 | Investments in unconsolidated subs | HC-F Item 8 |
| 9 | BHCK3656 | Direct/indirect RE venture investments | HC-F Item 9 |
| 10.a | BHCK3163 | Goodwill | HC-F Item 10.a |
| 10.b | BHCK0426 | Other intangible assets | HC-F Item 10.b |

---

#### Item 11: Other Assets

| MDRM | Description | Ties To |
|------|-------------|---------|
| BHCT2160 | Other assets | HC-F Item 12 |

**Reconciliation to HC-F**:
```
Item 11 = HC-F Item 12
       = HC-F Sum(Items 1-11)
```

**Major Components (from HC-F)**:
- Accrued interest receivable
- Net deferred tax assets
- Bank-owned life insurance (BOLI)
- Other miscellaneous assets

---

#### Item 12: Total Assets

| MDRM | Formula |
|------|---------|
| BHCT2170 | Sum(Items 1 through 11) |

**Validation**:
```
Total Assets = Cash + Securities + Fed Funds + Net Loans + Trading Assets
             + Premises + OREO + Investments + RE Ventures + Intangibles + Other
```

---

### LIABILITIES

#### Item 13: Deposits

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| 13 (Total) | BHCT2200 | Total deposits |
| 13.a | BHCM2200 | Domestic office deposits |
| 13.a.(1) | BHDM6631 | Domestic noninterest-bearing |
| 13.a.(2) | BHDM6636 | Domestic interest-bearing |
| 13.b | BHCKB536 | Foreign office deposits |
| 13.b.(1) | BHFN6631 | Foreign noninterest-bearing |
| 13.b.(2) | BHCKB538 | Foreign interest-bearing |

**Reconciliation**:
```
Item 13 = Item 13.a + Item 13.b
Item 13.a = Item 13.a.(1) + Item 13.a.(2)
Item 13.b = Item 13.b.(1) + Item 13.b.(2)
```

---

#### Items 14-16: Other Funding

| Item | MDRM | Description |
|------|------|-------------|
| 14 | BHCK2800 | Fed funds purchased and repos |
| 14.a | BHCKB993 | Federal funds purchased |
| 14.b | BHCKB995 | Securities sold under repo |
| 15 | BHCT3548 | Trading liabilities (ties to HC-D Item 15) |
| 16 | BHCT3190 | Other borrowed money |

---

#### Item 19: Subordinated Notes and Debentures

| MDRM | Description |
|------|-------------|
| BHCK4062 | Subordinated notes and debentures |

**Regulatory Significance**: May qualify as Tier 2 capital if meeting specified criteria (maturity, subordination, etc.)

---

#### Item 20: Other Liabilities

| MDRM | Description | Ties To |
|------|-------------|---------|
| BHCK2750 | Other liabilities | HC-G Item 5 |

**Reconciliation to HC-G**:
```
Item 20 = HC-G Item 5
       = HC-G Sum(Items 1-4)
```

---

#### Item 21: Total Liabilities

| MDRM | Formula |
|------|---------|
| BHCK2948 | Sum(Items 13 through 20) |

---

### EQUITY CAPITAL

#### Items 22-27: Equity Components

| Item | MDRM | Description |
|------|------|-------------|
| 22 | BHCK3000 | Minority interest / noncontrolling interest |
| 23 | BHCK3283 | Perpetual preferred stock |
| 24 | BHCK3230 | Common stock |
| 25 | BHCK3240 | Surplus (APIC) |
| 26 | BHCK3247 | Retained earnings |
| 27 | BHCKB530 | Accumulated other comprehensive income (AOCI) |
| 27.a | BHCK8434 | AOCI - unrealized gains/losses on AFS securities |

**AOCI Components**:
- Unrealized gains/losses on AFS securities
- Foreign currency translation adjustments
- Pension liability adjustments
- Cash flow hedge adjustments

---

#### Item 28: Total Equity Capital

| MDRM | Formula |
|------|---------|
| BHCT3210 | Sum(Items 23 through 27) |

**Ties to HC-R**: Schedule HC-R uses equity components as starting point for regulatory capital calculations.

---

#### Item 29: Total Liabilities and Equity

| MDRM | Formula | Validation |
|------|---------|------------|
| BHCK3300 | Item 21 + Item 22 + Item 28 | Must equal Item 12 |

**Balance Check**:
```
Total Assets (Item 12) = Total Liabilities (Item 21) + Minority Interest (Item 22) + Total Equity (Item 28)
BHCK2170 = BHCK2948 + BHCK3210 (= BHCK3300; BHCK2948 already includes minority interest, so BHCK3000 is NOT added separately)
```

---

## Cross-Schedule Reconciliation Map

```
Schedule HC                          Detailed Schedules
═══════════════════════════════════════════════════════════════════════════

Item 2 (Securities)           ──────► HC-B (Securities Portfolio)
  │                                    ├── AFS by security type
  │                                    ├── HTM by security type
  │                                    └── Unrealized gains/losses

Item 4 (Loans)                ──────► HC-C (Loan Portfolio)
  │                                    ├── Real estate loans (1.a-1.f)
  │                                    ├── C&I loans
  │                                    ├── Consumer loans
  │                                    └── Leases

Item 5 (Trading Assets)       ──────► HC-D (Trading Assets)
  │                                    ├── Securities
  │                                    ├── Loans
  │                                    └── Derivatives (→ HC-L)

Item 11 (Other Assets)        ──────► HC-F (Other Assets)
  │                                    ├── Deferred taxes
  │                                    ├── BOLI
  │                                    └── Miscellaneous

Item 15 (Trading Liabs)       ──────► HC-D (Trading Liabilities)
  │                                    ├── Short positions
  │                                    └── Derivatives (→ HC-L)

Item 20 (Other Liabs)         ──────► HC-G (Other Liabilities)
  │                                    ├── Accrued expenses
  │                                    └── Deferred taxes

Item 28 (Equity)              ──────► HC-R (Regulatory Capital)
                                       ├── CET1 calculation
                                       ├── Tier 1 calculation
                                       └── Total capital
```

---

## Key Validation Rules

### Primary Balance Equation
```
Total Assets = Total Liabilities + Minority Interest + Total Equity
BHCK2170 = BHCK2948 + BHCK3210 (= BHCK3300; BHCK2948 already includes minority interest, so BHCK3000 is NOT added separately)
```

### Sub-Total Validations
```
Item 1 = Item 1.a + Item 1.b
Item 2 = Item 2.a + Item 2.b + Item 2.c
Item 3 = Item 3.a + Item 3.b
Item 4.d = Item 4.a + Item 4.b - Item 4.c
Item 10 = Item 10.a + Item 10.b
Item 13 = Item 13.a + Item 13.b
Item 14 = Item 14.a + Item 14.b
```

### Cross-Schedule Validations
```
HC Item 5 = HC-D Item 12
HC Item 11 = HC-F Item 12
HC Item 15 = HC-D Item 15
HC Item 20 = HC-G Item 5
```

---

## Analytical Considerations

### Size Metrics
- **Total Assets (Item 12)**: Primary size metric for regulatory thresholds
- **$250B+**: Enhanced prudential standards (Category I-III)
- **$100B+**: Category IV standards
- **$10B+**: DFAST stress testing requirements

### Liquidity Analysis
- Cash (Item 1) + Trading assets (Item 5) = Liquid assets
- Fed funds and repos (Items 3, 14) indicate wholesale funding reliance

### Asset Quality Indicators
- Allowance ratio: Item 4.c / Item 4.b
- OREO (Item 7): Foreclosed property indicator
- Intangibles (Item 10): Deduction from regulatory capital

### Funding Structure
- Deposit funding: Item 13 / Item 21
- Wholesale funding: (Items 14+16+19) / Item 21

---

## Historical Notes

| Date | Change |
|------|--------|
| 1976-03-31 | Original FR Y-9C implementation |
| 1994-03-31 | AFS/HTM securities classification (FAS 115) |
| 1998-03-31 | AOCI introduced (FAS 130) |
| 2014-03-31 | Basel III implementation - capital items restructured |
| 2018-03-31 | Equity securities fair value accounting (ASU 2016-01) |
| 2020-03-31 | CECL implementation for larger institutions |

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCK0010 | Cash and balances |
| 2 | BHCT8641 | Total securities |
| 2.a | BHCKJJ34 | HTM securities |
| 2.b | BHCT1773 | AFS securities |
| 3 | BHCKC225 | Fed funds sold/reverse repos |
| 4.b | BHCTB528 | Loans net of unearned |
| 4.c | BHCT3123 | Allowance |
| 5 | BHCT3545 | Trading assets |
| 10.a | BHCK3163 | Goodwill |
| 11 | BHCT2160 | Other assets |
| 12 | BHCT2170 | **TOTAL ASSETS** |
| 13 | BHCT2200 | Total deposits |
| 15 | BHCT3548 | Trading liabilities |
| 16 | BHCT3190 | Other borrowed money |
| 19 | BHCK4062 | Subordinated debt |
| 20 | BHCK2750 | Other liabilities |
| 21 | BHCK2948 | **TOTAL LIABILITIES** |
| 28 | BHCT3210 | **TOTAL EQUITY** |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
