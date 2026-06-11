# Call Report Schedule RC-C - Loans and Lease Financing Receivables

> **Loan Portfolio Detail for FDIC-Insured Banks**
>
> Form: FFIEC 031/041/051 | Frequency: Quarterly

---

## Overview

Schedule RC-C provides detailed breakdowns of a bank's loan portfolio by loan type. This schedule is the Call Report equivalent of FR Y-9C Schedule HC-C.

---

## MDRM Prefix Guide for Loans

| Prefix | Scope | Example Use |
|--------|-------|-------------|
| RCFD | Total (domestic + foreign) | Total loans by category |
| RCON | Domestic offices only | RE loans in domestic offices |
| RCFN | Foreign offices only | Foreign office loans |

---

## Part I: Loans and Leases

### Real Estate Loans (Item 1)

| Item | Description | MDRM Total | MDRM Domestic | Y-9C Equiv |
|------|-------------|------------|---------------|------------|
| 1 | Loans secured by real estate | RCFD1410 | RCON1410 | BHCK1410 |
| 1.a | Construction & land development | RCFD1415 | RCON1415 | BHCK1415 |
| 1.a.(1) | 1-4 family residential ADC | RCFDF158 | - | BHCKF158 |
| 1.a.(2) | Other construction/land | RCFDF159 | - | BHCKF159 |
| 1.b | Secured by farmland | RCFD1420 | RCON1420 | BHCK1420 |
| 1.c | HELOCs | RCON1797 | RCON1797 | BHCK1797 |
| 1.d | 1-4 family closed-end | (subtotal) | (subtotal) | (subtotal) |
| 1.d.(1) | First liens | RCFD5367 | RCON5367 | BHCK5367 |
| 1.d.(2) | Junior liens | RCFD5368 | RCON5368 | BHCK5368 |
| 1.e | Multifamily (5+ units) | RCFD1460 | RCON1460 | BHCK1460 |
| 1.f | Nonfarm nonresidential | RCFD1480 | RCON1480 | BHCK1480 |
| 1.f.(1) | Owner-occupied | RCFDF160 | RCONF160 | BHCKF160 |
| 1.f.(2) | Non-owner-occupied | RCFDF162 | RCONF162 | BHCKF161 |

> Note: Item 1.d (closed-end 1-4 family) is a subtotal equal to 1.d.(1) first liens + 1.d.(2) junior liens; it has no separate atomic MDRM code. Item 7 (obligations of states and political subdivisions) is reported on the Call Report only (RCFD/RCON 2107); there is no consolidated FR Y-9C BHCK counterpart.

### Commercial and Other Loans

| Item | Description | MDRM Total | Y-9C Equiv | Notes |
|------|-------------|------------|------------|-------|
| 2 | Loans to depository institutions | RCFD1288 | BHCK1288 | Interbank |
| 3 | Loans to finance agricultural | RCON1590 | BHCK1590 | Farm operating |
| 4 | Commercial and industrial | RCFD1766 | BHCK1766 | C&I loans |
| 4.a | To US addressees | RCONB531 | BHCK1763 | Domestic |
| 4.b | To non-US addressees | RCFN1763 | BHCK1763 | Foreign |
| 5 | Loans to individuals | RCON1975 | BHCK1975 | Consumer |
| 5.a | Credit cards | RCONB538 | BHCKB538 | |
| 5.b | Other revolving | RCONB539 | BHCKB539 | |
| 5.c | Automobile loans | RCONK137 | BHCKK137 | |
| 5.d | Other consumer | RCONK207 | BHCKK207 | |
| 6 | Loans to foreign governments | RCFD2081 | BHCK2081 | Sovereign |
| 7 | Obligations of states/political subdivisions | RCFD2107 | - | No consolidated BHCK code; domestic basis RCON2107 |
| 8 | Other loans | RCFD1563 | BHCK1563 | |
| 9 | Lease financing receivables | RCFDB541 | BHCK2165 | |

### Totals and Adjustments

| Item | Description | MDRM | Y-9C Equiv | Notes |
|------|-------------|------|------------|-------|
| 10 | LESS: Unearned income | RCFD2123 | BHCK2123 | Contra |
| 11 | LESS: Allowance | RCFD3123 | BHCT3123 | ALLL/ACL |
| **12** | **Total loans net** | **RCFDB529** | **BHCKB529** | Ties to RC Item 4 |

---

## Key Formulas

### Net Loans Calculation
```
RC-C Item 12 = Sum(Items 1-9) - Item 10 - Item 11
RCFDB529 = [Sum of loan categories] - RCFD2123 - RCFD3123
```

### Real Estate Loans
```
Item 1 = 1.a + 1.b + 1.c + 1.d + 1.e + 1.f
RCFD1410 = RCFD1415 + RCFD1420 + RCON1797 + RCFD5367 + RCFD1460 + RCFD1480
```

---

## Risk Weights by Category

| Loan Category | Typical RW | Notes |
|---------------|------------|-------|
| 1-4 Family First Lien | 35-50% | Prudent underwriting |
| 1-4 Family Junior Lien | 100% | Higher risk |
| Multifamily | 50-100% | Depends on criteria |
| CRE Non-owner | 100% | Standard |
| CRE HVCRE | 150% | High volatility |
| C&I | 100% | Standard |
| Consumer | 75-100% | Retail |

---

## Memoranda Items

| Item | Description | MDRM | Purpose |
|------|-------------|------|---------|
| M.1 | Restructured loans | RCFD1616 | TDRs in compliance |
| M.2 | Loans to non-US addressees | Various | Foreign concentration |
| M.3 | Maturity/repricing | Various | Interest rate risk |
| M.5/M.6 | Small business loans (number and amount by original size) | Various | Reported as count + amount across "$100K or less / $100K-$250K / $250K-$1MM" size bands; no single atomic code |

---

## Cross-Schedule Relationships

| RC-C Ties To | Relationship |
|--------------|--------------|
| RC Item 4.b | RC-C Item 12 = RC Item 4.b (before allowance) |
| RC Item 4.c | RC-C Item 11 = RC Item 4.c (allowance) |
| RC-N | Past due detail by loan type |
| RC-H | Repricing schedule |

---

## Mapping to FR Y-9C HC-C

For each RC-C MDRM code, the Y-9C equivalent is:
- Replace RCFD with BHCT (total)
- Replace RCON with BHCK (domestic bank) or BHCM (BHC domestic)
- Replace RCFN with BHCK (foreign)

Example: RCFDB529 (Call) = BHCKB529 (Y-9C)

---

*See also: [HC_C_LOANS_GUIDE.md](HC_C_LOANS_GUIDE.md) for FR Y-9C equivalent*

*Last updated: 2026-01-29*
