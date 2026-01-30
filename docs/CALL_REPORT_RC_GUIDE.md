# Call Report Schedule RC - Consolidated Report of Condition

> **Master Balance Sheet for FDIC-Insured Banks**
>
> Form: FFIEC 031/041/051 | Frequency: Quarterly

---

## Overview

Schedule RC is the master balance sheet for Call Reports filed by FDIC-insured banks. It parallels Schedule HC from the FR Y-9C but at the individual bank level rather than consolidated holding company level.

### Key Differences from FR Y-9C Schedule HC

| Aspect | FR Y-9C (HC) | Call Report (RC) |
|--------|--------------|------------------|
| Reporter | Bank Holding Company | Individual Bank |
| Prefix | BHCT, BHCK, BHCM | RCFD, RCON |
| Consolidation | All subsidiary banks | Single bank entity |
| Threshold | $5B+ BHC assets | All FDIC-insured banks |

---

## MDRM Prefix Guide

| Prefix | Scope | Description |
|--------|-------|-------------|
| RCFD | Total | Domestic + foreign office combined |
| RCON | Domestic | Domestic offices only |
| RCFN | Foreign | Foreign offices only |
| RCFA | Advanced | Advanced approaches capital |
| RIAD | Income | Income statement items |

---

## Schedule RC Line Items

### Assets

| Item | Description | MDRM | Y-9C Equivalent | Notes |
|------|-------------|------|-----------------|-------|
| 1 | Cash and balances due | RCFD0081 | BHCT0081 | Same item number |
| 1.a | Noninterest-bearing | RCON0395 | BHCT0395 | Domestic only in RCON |
| 1.b | Interest-bearing | RCON0397 | BHCT0397 | Domestic only in RCON |
| 2 | Securities | RCFD8641 | BHCT8641 | Total securities |
| 2.a | HTM securities | RCFDJJ34 | BHCTJJ34 | At amortized cost |
| 2.b | AFS securities | RCFD1773 | BHCT1773 | At fair value |
| 3 | Fed funds sold | RCFDB987 | BHCTB987 | + resale agreements |
| 4 | Loans and leases | RCFD2122 | BHCT2122 | Net of allowance |
| 4.a | Loans held for sale | RCFD5369 | BHCT5369 | |
| 4.b | Loans net of unearned | RCFDB528 | BHCTB528 | Ties to RC-C |
| 4.c | LESS: Allowance | RCFD3123 | BHCT3123 | ALLL/ACL |
| 5 | Trading assets | RCFD3545 | BHCT3545 | Ties to RC-D |
| 6 | Premises and fixed | RCFD2145 | BHCT2145 | |
| 7 | Other real estate | RCFD2150 | BHCT2150 | OREO |
| 10 | Intangible assets | RCFD2143 | BHCT2143 | Goodwill + other |
| 11 | Other assets | RCFD2160 | BHCT2160 | Ties to RC-F |
| **12** | **Total assets** | **RCFD2170** | **BHCT2170** | **Primary size metric** |

### Liabilities

| Item | Description | MDRM | Y-9C Equivalent | Notes |
|------|-------------|------|-----------------|-------|
| 13 | Deposits | RCFD2200 | BHCT2200 | Total deposits |
| 13.a | Domestic deposits | RCON2200 | BHCM2200 | |
| 13.b | Foreign deposits | RCFNB536 | BHCKB536 | If applicable |
| 14 | Fed funds purchased | RCFDB993 | BHCTB993 | + repos |
| 15 | Trading liabilities | RCFD3548 | BHCT3548 | Ties to RC-D |
| 16 | Other borrowed money | RCFD3190 | BHCT3190 | |
| 19 | Subordinated debt | RCFD3200 | BHCT3200 | |
| 20 | Other liabilities | RCFD2930 | BHCT2930 | Ties to RC-G |
| **21** | **Total liabilities** | **RCFD2948** | **BHCT2948** | |

### Equity Capital

| Item | Description | MDRM | Y-9C Equivalent | Notes |
|------|-------------|------|-----------------|-------|
| 23 | Perpetual preferred | RCFD3838 | BHCT3838 | |
| 24 | Common stock | RCFD3230 | BHCT3230 | |
| 25 | Surplus | RCFD3839 | BHCT3839 | APIC |
| 26 | Retained earnings | RCFD3632 | BHCT3632 | |
| 27 | AOCI | RCFDB530 | BHCTB530 | |
| **28** | **Total equity capital** | **RCFD3210** | **BHCT3210** | |
| **29** | **Total L + E** | **RCFD3300** | **BHCT3300** | Must = Item 12 |

---

## Key Reconciliations

### Balance Sheet Identity
```
RCFD2170 (Total Assets) = RCFD2948 (Total Liabilities) + RCFD3210 (Total Equity)
```

### Cross-Schedule Tie-Outs

| RC Item | MDRM | Must Equal | Detail Schedule |
|---------|------|------------|-----------------|
| 2 | RCFD8641 | RC-B Total | Schedule RC-B |
| 4.b | RCFDB528 | RC-C Item 12 | Schedule RC-C |
| 5 | RCFD3545 | RC-D Item 12 | Schedule RC-D |
| 11 | RCFD2160 | RC-F Item 12 | Schedule RC-F |
| 15 | RCFD3548 | RC-D Item 15 | Schedule RC-D |
| 20 | RCFD2930 | RC-G Item 5 | Schedule RC-G |

---

## Form Variants

| Form | Who Files | Requirements |
|------|-----------|--------------|
| FFIEC 031 | Banks with foreign offices | Full form |
| FFIEC 041 | Banks domestic only | Simplified |
| FFIEC 051 | Small banks <$5B | Further simplified |

---

## Mapping to FR Y-9C

To convert Call Report MDRM to Y-9C MDRM:
- RCFD → BHCT (total)
- RCON → BHCM (domestic)
- RCFN → BHCK (foreign)
- RIAD → BHCT (income items)

---

## Data Sources

- FFIEC CDR: https://cdr.ffiec.gov/
- FDIC BankFind: https://banks.data.fdic.gov/

---

*See also: [HC_BALANCE_SHEET_GUIDE.md](HC_BALANCE_SHEET_GUIDE.md) for FR Y-9C equivalent*

*Last updated: 2026-01-29*
