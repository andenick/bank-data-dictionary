# Call Report Schedule RC-E - Deposit Liabilities

> **Deposit Detail for FDIC-Insured Banks**
>
> Form: FFIEC 031/041/051 | Frequency: Quarterly

---

## Overview

Schedule RC-E provides detailed breakdowns of a bank's deposit liabilities by account type, ownership category, and interest-bearing status. This information is critical for:
- Deposit insurance assessment calculations
- Liquidity coverage ratio (LCR) analysis
- Interest rate sensitivity analysis
- Core deposits vs. volatile funding analysis

---

## MDRM Prefix Guide for Deposits

| Prefix | Scope | Typical Use |
|--------|-------|-------------|
| RCON | Domestic offices | Most deposit items |
| RCFN | Foreign offices | Foreign branch deposits |
| RCFD | Total | Combined total |

---

## Part I: Deposits in Domestic Offices

### Transaction Accounts

| Item | Description | MDRM | Notes |
|------|-------------|------|-------|
| 1 | Transaction accounts | RCONB549 | Total transaction |
| 1.a | Individuals, partnerships, corps | RCONB550 | IPC accounts |
| 1.b | US Government | RCON2203 | Federal deposits |
| 1.c | States and political subdivisions | RCON2206 | Municipal deposits |
| 1.d | Commercial banks in US | RCON2207 | Correspondent banks |
| 1.e | Other depository institutions | RCON2209 | Credit unions, etc. |
| 1.f | Banks in foreign countries | RCON2213 | Foreign correspondents |
| 1.g | Certified and official checks | RCON2330 | Bank-issued checks |

### Nontransaction Accounts

| Item | Description | MDRM | Notes |
|------|-------------|------|-------|
| 2 | Nontransaction accounts | RCONB551 | Total nontransaction |
| 2.a | Savings deposits | Various | Multiple categories |
| 2.a.(1) | MMDAs | RCONHK17 | Money market deposits |
| 2.a.(2) | Other savings | RCONHK18 | Passbook, etc. |
| 2.b | Time deposits | Various | By size and maturity |
| 2.b.(1) | Time <= $250K | RCONHK16 | Retail CDs |
| 2.b.(2) | Time > $250K | RCONHK17 | Jumbo CDs |

---

## Part II: Deposits in Foreign Offices (FFIEC 031 only)

| Item | Description | MDRM | Notes |
|------|-------------|------|-------|
| 1 | IPC transaction accounts (foreign offices) | RCFN2241 | Individuals, partnerships, corporations |
| 2 | IPC nontransaction accounts (foreign offices) | RCFN2242 | Individuals, partnerships, corporations |
| — | Noninterest-bearing (foreign offices) | RCFN6631 | By interest status |
| — | Interest-bearing (foreign offices) | RCFN6636 | By interest status |
| **Total** | Total deposits in foreign offices | RCFN2200 | Ties to RC Item 13.b |

---

## Deposit Categories Summary

### By Interest Status

| Category | MDRM | Description |
|----------|------|-------------|
| Noninterest-bearing (domestic) | RCON6631 | DDA, zero-rate accounts |
| Interest-bearing (domestic) | RCON6636 | NOW, MMDA, time deposits |
| Noninterest-bearing (foreign) | RCFNB537 | Foreign office NI |
| Interest-bearing (foreign) | RCFNB538 | Foreign office IB |

### By Insurance Status

| Category | Description | MDRM |
|----------|-------------|------|
| Insured deposits | Under $250K FDIC limit | RCONF049 |
| Uninsured deposits | Over FDIC limit | RCONF051 |
| Preferred deposits | Collateralized public | Various |

---

## Key Totals and Reconciliations

### Total Deposits
```
RC Item 13 (RCFD2200) = RC Item 13.a (RCON2200) + RC Item 13.b (RCFNB536)
                       = Domestic deposits + Foreign deposits
```

### Domestic Deposits
```
RCON2200 = RCON6631 (Noninterest) + RCON6636 (Interest-bearing)
```

---

## Deposit Stability Analysis

### Core vs. Non-Core Deposits

| Category | Typical Treatment | LCR Runoff |
|----------|-------------------|------------|
| Retail transaction | Core, stable | 3-10% |
| Retail savings | Core, stable | 3-10% |
| Retail time <$250K | Core | 3-10% |
| Jumbo CDs >$250K | Less stable | 10-40% |
| Brokered deposits | Volatile | 10-40% |
| Public funds | Volatile | 25-40% |

---

## Memoranda Items

| Item | Description | MDRM | Purpose |
|------|-------------|------|---------|
| M.1 | Selected components | Various | Detail breakouts |
| M.2 | Brokered deposits (total) | RCON2365 | Volatile funding |
| M.3 | Maturity/repricing | Various | IRR analysis |
| M.4 | Reciprocal deposits (total) | RCONJH83 | Network deposits |
| M.5 | Estimated insured | RCONF049 | FDIC coverage |
| M.6 | Estimated uninsured | RCONF051 | Concentration risk |

---

## Cross-Schedule Relationships

| RC-E Ties To | Relationship |
|--------------|--------------|
| RC Item 13 | Total deposits on balance sheet |
| RC-K | Average deposits |
| RC-O | Fiduciary deposits |
| FR 2052a | LCR deposit runoff calculations |

---

## LCR/NSFR Implications

### LCR Deposit Runoff Rates

| Deposit Type | Runoff Rate | Category |
|--------------|-------------|----------|
| Stable retail | 3% | Insured, relationship |
| Less stable retail | 10% | Higher rate, other |
| Small business | 5-10% | Covered, not covered |
| Operational wholesale | 25% | Clearing, custody |
| Non-operational wholesale | 40% | Other wholesale |
| Unsecured wholesale funding | 100% | Short-term |

### NSFR Treatment

| Deposit Type | ASF Factor | Rationale |
|--------------|------------|-----------|
| Stable retail <1yr | 95% | Highly stable |
| Less stable retail <1yr | 90% | Mostly stable |
| Wholesale operational <1yr | 50% | Moderate stability |
| Other wholesale <1yr | 0-50% | Depends on type |

---

## Mapping to FR Y-9C

The FR Y-9C consolidates bank deposits at the holding company level. Note that on Schedule HC, total deposits (line 13) is a caption with no single atomic MDRM code; it is the sum of its domestic and foreign components, each split by interest status:
- Schedule HC Item 13 (total deposits) = Item 13.a (domestic) + Item 13.b (foreign)
- Schedule HC Item 13.a (deposits in domestic offices) = BHDM6631 (noninterest-bearing) + BHDM6636 (interest-bearing)
- Schedule HC Item 13.b (deposits in foreign offices) = BHFN6631 (noninterest-bearing) + BHFN6636 (interest-bearing)

---

*Last updated: 2026-01-29*
