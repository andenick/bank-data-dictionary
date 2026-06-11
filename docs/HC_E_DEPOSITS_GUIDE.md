# Schedule HC-E: Deposit Liabilities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-E - Deposit Liabilities
**Frequency**: Quarterly
**Purpose**: Disaggregate the holding company's domestic-office deposits by depository-subsidiary type and deposit product, and collect brokered-deposit memoranda

---

## Overview

Schedule HC-E breaks down the deposits that flow into Schedule HC item 13.a, "Deposits in domestic offices." The breakdown is two-dimensional:

1. **By type of depository subsidiary** - item 1 covers deposits held in domestic offices of *commercial bank* subsidiaries; item 2 covers deposits held in domestic offices of *other depository institution* (e.g., thrift/savings) subsidiaries.
2. **By deposit product** - within each block, deposits are split into noninterest-bearing, interest-bearing transaction (NOW/ATS), money-market and other savings, time deposits of $250,000 or less, and time deposits of more than $250,000.

A four-item Memoranda section captures brokered-deposit and remaining-maturity detail used in liquidity and resolution analysis.

### Relationship to Schedule HC

```
Sum of HC-E items 1.a-1.e and 2.a-2.e  =  Schedule HC items 13.a.(1) + 13.a.(2)
                                          (interest-bearing + noninterest-bearing
                                           deposits in domestic offices)
```

The official form footnote states: *"The sum of items 1.a through 1.e and items 2.a through 2.e must equal the sum of Schedule HC, items 13.a.(1) and 13.a.(2)."* Foreign-office deposits (HC item 13.b) are not detailed here except in Memoranda item 4.

---

## Who Files

All FR Y-9C reporters complete HC-E. The split between item 1 (commercial bank subsidiaries) and item 2 (other depository institutions) depends on the charter types within the consolidated organization; a holding company with no thrift/other depository subsidiary reports only item 1.

---

## Schedule Structure

```
DEPOSIT LIABILITIES (domestic offices)
├── Item 1: Commercial bank subsidiaries
│   ├── 1.a Noninterest-bearing balances
│   ├── 1.b Interest-bearing demand, NOW, ATS, other transaction accounts
│   ├── 1.c Money market deposit accounts and other savings accounts
│   ├── 1.d Time deposits of $250,000 or less
│   └── 1.e Time deposits of more than $250,000
├── Item 2: Other depository institution subsidiaries
│   ├── 2.a Noninterest-bearing balances
│   ├── 2.b Interest-bearing demand, NOW, ATS, other transaction accounts
│   ├── 2.c Money market deposit accounts and other savings accounts
│   ├── 2.d Time deposits of $250,000 or less
│   └── 2.e Time deposits of more than $250,000
└── Memoranda
    ├── M.1 Brokered deposits $250,000 or less, remaining maturity <= 1 year
    ├── M.2 Brokered deposits $250,000 or less, remaining maturity > 1 year
    ├── M.3 Time deposits > $250,000, remaining maturity <= 1 year
    └── M.4 Foreign-office time deposits, remaining maturity <= 1 year
```

---

## Detailed Line Items

### Item 1 - Commercial bank subsidiaries (codeset `BHCB`)

| Line | MDRM | Description |
|------|------|-------------|
| 1.a | BHCB2210 | Noninterest-bearing balances (includes noninterest-bearing demand, time, and savings deposits) |
| 1.b | BHCB3187 | Interest-bearing demand deposits, NOW, ATS, and other transaction accounts |
| 1.c | BHCB2389 | Money market deposit accounts and other savings accounts |
| 1.d | BHCBHK29 | Time deposits of $250,000 or less |
| 1.e | BHCBJ474 | Time deposits of more than $250,000 |

### Item 2 - Other depository institution subsidiaries (codeset `BHOD`)

| Line | MDRM | Description |
|------|------|-------------|
| 2.a | BHOD3189 | Noninterest-bearing balances |
| 2.b | BHOD3187 | Interest-bearing demand deposits, NOW, ATS, and other transaction accounts |
| 2.c | BHOD2389 | Money market deposit accounts and other savings accounts |
| 2.d | BHODHK29 | Time deposits of $250,000 or less |
| 2.e | BHODJ474 | Time deposits of more than $250,000 |

Note the codeset prefix carries the meaning: `BHCB` = commercial bank subsidiaries (domestic offices), `BHOD` = other depository institution subsidiaries (domestic offices).

### Memoranda

| Line | MDRM | Codeset | Description |
|------|------|---------|-------------|
| M.1 | BHDMHK06 | BHDM | Brokered deposits of $250,000 or less, remaining maturity of one year or less |
| M.2 | BHDMHK31 | BHDM | Brokered deposits of $250,000 or less, remaining maturity of more than one year |
| M.3 | BHDMHK32 | BHDM | Time deposits of more than $250,000, remaining maturity of one year or less |
| M.4 | BHFNA245 | BHFN | Foreign-office time deposits, remaining maturity of one year or less |

The Memoranda are *informational overlays* on the deposit balances; they are not additive to items 1-2 and do not enter the HC item 13.a reconciliation.

---

## Reconciliation / Ties

```
SCHEDULE HC-E                                      SCHEDULE HC
═══════════════════════════════════════════════════════════════════════════
Sum(1.a..1.e) + Sum(2.a..2.e)  ──────────────────► HC item 13.a.(1) + 13.a.(2)
                                                   (deposits in domestic offices)

Memoranda M.4 (foreign-office time deposits)  ────► relates to HC item 13.b
                                                   (deposits in foreign offices)
```

The "$250,000 or less" vs. "more than $250,000" split (items 1.d/1.e, 2.d/2.e) aligns with the FDIC standard maximum deposit insurance amount and is used to estimate insured vs. uninsured deposit shares.

---

## Pitfalls

- **Do not confuse with Call Report RC-E.** The Call Report Schedule RC-E disaggregates deposits *by depositor type* (individuals/partnerships/corporations, U.S. government, states and political subdivisions, etc.), whereas FR Y-9C HC-E disaggregates by *subsidiary charter type and deposit product*. The captions do not map one-to-one, so most HC-E lines have no clean RC-E analogue (`call_mdrm` = "-"). Only the product-level codes that the Federal Reserve shares across forms (e.g., the `2210`/`2389`/`J474` item numbers under RCFD/RCON) carry a Call analogue.
- **Codeset prefix is load-bearing.** Items 1 and 2 reuse identical four-character item numbers (e.g., `3187` appears in both 1.b and 2.b); only the prefix (`BHCB` vs. `BHOD`) distinguishes them. Joining on the item number alone will collapse the two blocks.
- **Memoranda use yet another prefix.** M.1-M.3 use `BHDM` (domestic-office detail) and M.4 uses `BHFN` (foreign-office); they are not in the `BHCB`/`BHOD` families.
- **Time-deposit threshold history.** The `$250,000` threshold codes (`HK29`, `J474`, `HK31`, `HK32`) entered the form in 2017; earlier vintages used a `$100,000` threshold with different codes. This guide reflects the current ($250,000) structure.

---

## Verification & Provenance

- **MDRM:** all 14 line codes were joined to the Federal Reserve MDRM codeset; 14 of 14 verified present, with start/end dates recorded in the provenance file.
- **Warehouse evidence:** every HC-E code is observed in the Federal Reserve bulk BHCF data (1986-2025); the `$250,000`-threshold codes first appear in 2017 Q1, consistent with their MDRM start dates.
- **Provenance file:** `_rebuild/schedules/PROVENANCE_HC_E.csv` (line, column, code, MDRM name, MDRM start/end, BHCF first/last seen, source).
- **Sources:** Federal Reserve MDRM; FR Y-9C form and instructions (March 2026); Federal Reserve bulk BHCF data (1986-2025).

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1.a | BHCB2210 | Commercial bank subs - noninterest-bearing |
| 1.b | BHCB3187 | Commercial bank subs - interest-bearing transaction |
| 1.c | BHCB2389 | Commercial bank subs - MMDA / other savings |
| 1.d | BHCBHK29 | Commercial bank subs - time deposits <= $250k |
| 1.e | BHCBJ474 | Commercial bank subs - time deposits > $250k |
| 2.a | BHOD3189 | Other depository subs - noninterest-bearing |
| 2.b | BHOD3187 | Other depository subs - interest-bearing transaction |
| 2.c | BHOD2389 | Other depository subs - MMDA / other savings |
| 2.d | BHODHK29 | Other depository subs - time deposits <= $250k |
| 2.e | BHODJ474 | Other depository subs - time deposits > $250k |
| M.1 | BHDMHK06 | Brokered deposits <= $250k, maturity <= 1yr |
| M.2 | BHDMHK31 | Brokered deposits <= $250k, maturity > 1yr |
| M.3 | BHDMHK32 | Time deposits > $250k, maturity <= 1yr |
| M.4 | BHFNA245 | Foreign-office time deposits, maturity <= 1yr |

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C form and instructions (March 2026); Federal Reserve MDRM; Federal Reserve bulk BHCF data (1986-2025)*
