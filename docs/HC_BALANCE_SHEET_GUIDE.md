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

EQUITY (Items 23-28)
├── Items 23-26: Preferred, common, surplus, retained, AOCI, other
├── Item 27.a: Total holding company equity
├── Item 27.b: Noncontrolling (minority) interest
└── Item 28: TOTAL EQUITY (incl. noncontrolling interest)

BALANCING (Item 29)
└── Total Liabilities + Total Equity = Total Assets
```

---

## Detailed Line Item Analysis

### ASSETS

#### Item 1: Cash and Balances Due from Depository Institutions

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| 1 (Total) | - | Caption only; no consolidated BHC total code (former BHCK0010 ended 2014-12-31) |
| 1.a | BHCK0081 | Noninterest-bearing balances and currency/coin |
| 1.b.(1) | BHCK0395 | Interest-bearing balances in U.S. offices |
| 1.b.(2) | BHCK0397 | Interest-bearing balances in foreign offices, Edge/Agreement subsidiaries, and IBFs |

**Components**:
- Currency and coin on hand
- Cash items in process of collection
- Balances due from Federal Reserve Banks
- Balances due from other depository institutions

**Reconciliation**:
```
Item 1 = Item 1.a + Item 1.b.(1) + Item 1.b.(2)
```

---

#### Item 2: Securities

| Sub-Item | MDRM | Description | Ties To |
|----------|------|-------------|---------|
| 2 (Total) | - | Total securities (caption; no consolidated code; = 2.a + 2.b + 2.c; Call total = RCFD8641) | HC-B |
| 2.a | BHCKJJ34 | HTM securities (amortized cost) | HC-B Item 8 Col A |
| 2.b | BHCK1773 | AFS debt securities (fair value) | HC-B Item 8 Col D |
| 2.c | BHCKJA22 | Equity securities with determinable FV | HC-B M5 |

**Key Distinctions**:
- **HTM**: Carried at amortized cost; positive intent and ability to hold to maturity
- **AFS**: Carried at fair value; unrealized gains/losses flow to AOCI (Item 27)
- **Equity**: Carried at fair value; changes flow through income statement

**Reconciliation**:
```
Item 2 = Item 2.a + Item 2.b + Item 2.c
Item 2.a = HC-B Item 8, Column A (Total HTM amortized cost)
Item 2.b = HC-B Item 8, Column D (Total AFS fair value)
```

**Note**: The fair value amounts differ from book value for HTM securities. HC-B provides both amortized cost and fair value for all securities.

---

#### Item 3: Federal Funds Sold and Securities Purchased Under Resale Agreements

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| 3 (Total) | - | Caption only; no consolidated BHC total code (former BHCKC225 ended 2014-12-31) |
| 3.a | BHDMB987 | Federal funds sold in domestic offices |
| 3.b | BHCKB989 | Securities purchased under agreements to resell |

**Nature**:
- Short-term lending to other financial institutions
- Reverse repos = collateralized lending
- Important component of liquidity management

---

#### Item 4: Loans and Lease Financing Receivables

| Sub-Item | MDRM | Description | Ties To |
|----------|------|-------------|---------|
| 4.a | BHCK5369 | Loans and leases held for sale | HC-C Item 10 |
| 4.b | BHCKB528 | Loans and leases held for investment (net of unearned income) | HC-C Items 1-9 minus Item 10 |
| 4.c | BHCK3123 | LESS: Allowance for credit losses on loans and leases | HC-C Item 11 |
| 4.d | BHCKB529 | Loans and leases held for investment, net of allowance | Item 4.b - Item 4.c |

**Reconciliation to HC-C**:
```
Gross Loans (HC-C) = Sum(Items 1-9) = Real estate + Ag + C&I + Consumer + Other + Leases
Net of Unearned = Gross - Unearned income fees
Net Loans = Net of Unearned - Allowance for credit losses

HC Item 4.b = HC-C Items 1-9 - HC-C Item 10
HC Item 4.c = HC-C Item 11
HC Item 4.d = HC Item 4.b - HC Item 4.c
```

---

#### Item 5: Trading Assets

| Sub-Item | MDRM | Description | Ties To |
|----------|------|-------------|---------|
| 5 (Total) | BHCK3545 | Total trading assets | HC-D Item 12 |

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
| 6 | BHCK2145 | Premises and fixed assets (incl. right-of-use assets) | HC-F Item 6 |
| 7 | BHCK2150 | Other real estate owned | HC-M Item 7 |
| 8 | BHCK2130 | Investments in unconsolidated subs | HC-F Item 8 |
| 9 | BHCK3656 | Direct/indirect RE venture investments | HC-F Item 9 |
| 10 (Total) | BHCK2143 | Intangible assets (= 10.a + 10.b) | HC-M |
| 10.a | BHCK3163 | Goodwill | HC-M Item 10.a |
| 10.b | BHCK0426 | All other intangible assets | HC-M Item 10.b |

---

#### Item 11: Other Assets

| MDRM | Description | Ties To |
|------|-------------|---------|
| BHCK2160 | Other assets | HC-F Item 12 |

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
| BHCK2170 | Sum(Items 1 through 11) |

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
| 13 (Total) | - | Total deposits (caption; no consolidated code; = 13.a + 13.b; Call total = RCFD2200) |
| 13.a | - | Domestic office deposits (no consolidated code; = BHDM6631 + BHDM6636; Call = RCON2200) |
| 13.a.(1) | BHDM6631 | Domestic noninterest-bearing |
| 13.a.(2) | BHDM6636 | Domestic interest-bearing |
| 13.b | - | Foreign office deposits (caption; no consolidated code; = 13.b.(1) + 13.b.(2); Call = RCFNB536) |
| 13.b.(1) | BHFN6631 | Foreign noninterest-bearing |
| 13.b.(2) | BHFN6636 | Foreign interest-bearing (BHFN series, NOT consumer-loan BHCKB538) |

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
| 14 (Total) | - | Caption only; no consolidated BHC total code (former BHCK2800 ended 2001-12-31) |
| 14.a | BHDMB993 | Federal funds purchased in domestic offices |
| 14.b | BHCKB995 | Securities sold under agreements to repurchase |
| 15 | BHCK3548 | Trading liabilities (ties to HC-D Item 15) |
| 16 | BHCK3190 | Other borrowed money (from HC-M) |

---

#### Item 19: Subordinated Notes and Debentures

| Sub-Item | MDRM | Description |
|----------|------|-------------|
| 19.a | BHCK4062 | Subordinated notes and debentures |
| 19.b | BHCKC699 | Subordinated notes payable to unconsolidated trusts issuing trust preferred securities, and trust preferred securities issued by consolidated special purpose entities |

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

#### Items 23-27: Equity Components

On the current form, item 22 is reserved (NOT APPLICABLE). Noncontrolling (minority)
interest is reported within equity at item 27.b, not as a separate pre-equity line.

| Item | MDRM | Description |
|------|------|-------------|
| 22 | - | NOT APPLICABLE (reserved); minority interest now at 27.b |
| 23 | BHCK3283 | Perpetual preferred stock and related surplus |
| 24 | BHCK3230 | Common stock (par value) |
| 25 | BHCK3240 | Surplus (excl. surplus related to preferred stock) |
| 26.a | BHCK3247 | Retained earnings |
| 26.b | BHCKB530 | Accumulated other comprehensive income (AOCI) |
| 26.c | BHCKA130 | Other equity capital components |
| 27.a | BHCK3210 | Total holding company equity capital (sum of items 23 through 26.c) |
| 27.b | BHCK3000 | Noncontrolling (minority) interests in consolidated subsidiaries |

**AOCI Components (item 26.b)**:
- Unrealized gains/losses on AFS securities
- Foreign currency translation adjustments
- Pension liability adjustments
- Cash flow hedge adjustments

**Other equity capital components (item 26.c)**: treasury stock, unearned ESOP shares, etc.

---

#### Item 28: Total Equity Capital

| MDRM | Formula |
|------|---------|
| BHCKG105 | Item 27.a + Item 27.b (= total holding company equity + noncontrolling interest) |

**Note**: BHCKG105 is the total equity capital INCLUDING noncontrolling interest. BHCK3210
(item 27.a) is the parent-only total holding company equity capital.

**Ties to HC-R**: Schedule HC-R uses equity components as starting point for regulatory capital calculations.

---

#### Item 29: Total Liabilities and Equity

| MDRM | Formula | Validation |
|------|---------|------------|
| BHCK3300 | Item 21 + Item 28 | Must equal Item 12 |

**Balance Check**:
```
Total Assets (Item 12) = Total Liabilities (Item 21) + Total Equity (Item 28)
BHCK2170 = BHCK2948 + BHCKG105 (= BHCK3300)
```
(Verified against warehouse: for every filer BHCK2170 = BHCK2948 + BHCKG105, and
BHCKG105 = BHCK3210 + BHCK3000.)

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
Total Assets = Total Liabilities + Total Equity
BHCK2170 = BHCK2948 + BHCKG105 (= BHCK3300)
where BHCKG105 = BHCK3210 (HC equity) + BHCK3000 (noncontrolling interest)
```

### Sub-Total Validations
```
Item 1 = Item 1.a + Item 1.b.(1) + Item 1.b.(2)
Item 2 = Item 2.a + Item 2.b + Item 2.c
Item 3 = Item 3.a + Item 3.b
Item 4.d = Item 4.b - Item 4.c
Item 10 = Item 10.a + Item 10.b
Item 13 = Item 13.a + Item 13.b
Item 13.a = Item 13.a.(1) + Item 13.a.(2)
Item 13.b = Item 13.b.(1) + Item 13.b.(2)
Item 14 = Item 14.a + Item 14.b
Item 28 = Item 27.a + Item 27.b
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
| 1 | - | Cash (caption; Call = RCFD0081) |
| 1.b.(1) | BHCK0395 | Interest-bearing balances, U.S. offices |
| 1.b.(2) | BHCK0397 | Interest-bearing balances, foreign offices |
| 2 | - | Total securities (caption; Call = RCFD8641) |
| 2.a | BHCKJJ34 | HTM securities |
| 2.b | BHCK1773 | AFS securities |
| 3 | - | Fed funds sold/reverse repos (caption) |
| 3.a | BHDMB987 | Federal funds sold in domestic offices |
| 4.b | BHCKB528 | Loans held for investment |
| 4.c | BHCK3123 | Allowance for credit losses |
| 5 | BHCK3545 | Trading assets |
| 10 | BHCK2143 | Intangible assets |
| 10.a | BHCK3163 | Goodwill |
| 11 | BHCK2160 | Other assets |
| 12 | BHCK2170 | **TOTAL ASSETS** |
| 13 | - | Total deposits (caption; Call = RCFD2200) |
| 13.b.(2) | BHFN6636 | Foreign interest-bearing deposits |
| 14 | - | Fed funds purchased/repos (caption) |
| 14.a | BHDMB993 | Federal funds purchased in domestic offices |
| 15 | BHCK3548 | Trading liabilities |
| 16 | BHCK3190 | Other borrowed money |
| 19.a | BHCK4062 | Subordinated debt |
| 19.b | BHCKC699 | Sub. notes payable to trusts |
| 20 | BHCK2750 | Other liabilities |
| 21 | BHCK2948 | **TOTAL LIABILITIES** |
| 26.b | BHCKB530 | AOCI |
| 26.c | BHCKA130 | Other equity components |
| 27.a | BHCK3210 | Total holding company equity |
| 27.b | BHCK3000 | Noncontrolling interest |
| 28 | BHCKG105 | **TOTAL EQUITY** (incl. NCI) |

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C Instructions (March 2026)*
