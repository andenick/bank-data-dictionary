# What Adds Up to What

> **Complete Reconciliation Hierarchy for FR Y-9C and Related Forms**
>
> Version 1.0 | Created: 2026-01-29

This document provides a comprehensive visual representation of how all regulatory data elements relate to each other hierarchically. Use this to understand the cascade from summary totals down to detailed components.

---

## Table of Contents

1. [Balance Sheet Cascade](#balance-sheet-cascade)
2. [Asset Detail Hierarchy](#asset-detail-hierarchy)
3. [Liability Detail Hierarchy](#liability-detail-hierarchy)
4. [Capital Hierarchy](#capital-hierarchy)
5. [Income Statement Hierarchy](#income-statement-hierarchy)
6. [Derivatives Hierarchy](#derivatives-hierarchy)
7. [Cross-Schedule Tie-Outs](#cross-schedule-tie-outs)

---

## Balance Sheet Cascade

### The Fundamental Balance Sheet Identity

```
ASSETS (BHCK2170) = TOTAL LIABILITIES & MINORITY INTEREST (BHCK2948) + TOTAL EQUITY CAPITAL (BHCK3210) = BHCK3300
  (BHCK2948 already INCLUDES minority interest per its MDRM title; do NOT add BHCK3000 separately - it double-counts)
         |                    |                                                  |
   Schedule HC           Schedule HC              Schedule HC              Schedule HC
    Item 12               Item 21                  Item 22                  Item 28
```

### Complete Asset Breakdown

```
HC Total Assets (BHCT2170) - Schedule HC Item 12
|
+-- 1. Cash (BHCK0010)
|   +-- 1.a Noninterest-bearing (BHCK0081)
|   +-- 1.b Interest-bearing (BHCK0395)
|
+-- 2. Securities (= 2.a + 2.b + 2.c) ---------> [Detail: Schedule HC-B]
|   +-- 2.a HTM at amortized cost (BHCKJJ34) --> HC-B Item 8 Col C
|   +-- 2.b AFS at fair value (BHCT1773) -----> HC-B Item 8 Col B
|   +-- 2.c Equity securities (BHCKJA22) -----> HC-B M5
|
+-- 3. Fed Funds & Resale (BHCKC225)
|   +-- 3.a Fed funds sold (BHCKB987)
|   +-- 3.b Securities purchased under resale (BHCKB989)
|
+-- 4. Loans (BHCT2122) -----------------------> [Detail: Schedule HC-C]
|   +-- 4.a Held for sale (BHCT5369) ---------> HC-C Item 10
|   +-- 4.b Gross loans (BHCTB528) -----------> HC-C Sum(1-9) - Item 10
|   +-- 4.c LESS: Allowance (BHCT3123) -------> HC-C Item 11
|   +-- 4.d Net loans (BHCKB529) -------------> HC-C Item 12
|
+-- 5. Trading Assets (BHCT3545) --------------> [Detail: Schedule HC-D]
|   +-- (See Trading Assets Hierarchy below)
|
+-- 6. Premises and Fixed Assets (BHCK2145) --> HC-F Item 6
|
+-- 7. Other Real Estate Owned (BHCT2150) ----> HC-F Item 7
|
+-- 8. Investments in Unconsolidated (BHCK2130) -> HC-F Item 8
|
+-- 9. RE Ventures (BHCK3656) ----------------> HC-F Item 9
|
+-- 10. Intangible Assets (BHCT2143)
|    +-- 10.a Goodwill (BHCK3163) ------------> HC-F Item 10.a
|    +-- 10.b Other intangibles (BHCK0426) --> HC-F Item 10.b
|
+-- 11. Other Assets (BHCT2160) --------------> [Detail: Schedule HC-F]
     +-- (See Other Assets Hierarchy below)
```

### Complete Liability Breakdown

```
HC Total Liabilities (BHCK2948) - Schedule HC Item 21
|
+-- 13. Deposits [no single consolidated Y-9C MDRM; = domestic + foreign]
|    +-- 13.a Domestic (= BHDM6631 + BHDM6636)
|    |    +-- 13.a.(1) Noninterest-bearing (BHDM6631)
|    |    +-- 13.a.(2) Interest-bearing (BHDM6636)
|    +-- 13.b Foreign (= BHFN6631 + BHFN6636)
|         +-- 13.b.(1) Noninterest-bearing (BHFN6631)
|         +-- 13.b.(2) Interest-bearing (BHFN6636)
|
+-- 14. Fed Funds Purchased & Repos (BHCK2800)
|    +-- 14.a Fed funds purchased (BHCKB993)
|    +-- 14.b Securities sold under repo (BHCKB995)
|
+-- 15. Trading Liabilities (BHCT3548) --------> [Detail: Schedule HC-D]
|    +-- (See Trading Liabilities Hierarchy below)
|
+-- 16. Other Borrowed Money (BHCT3190)
|
+-- 19. Subordinated Debt (BHCK4062)
|
+-- 20. Other Liabilities (BHCK2750) ----------> [Detail: Schedule HC-G]
     +-- (See Other Liabilities Hierarchy below)
```

### Complete Equity Breakdown

```
HC Total Equity Capital (BHCT3210) - Schedule HC Item 28
|
+-- 22. Minority Interest (BHCK3000)
|
+-- 23. Perpetual Preferred Stock (BHCK3283)
|
+-- 24. Common Stock (BHCK3230)
|
+-- 25. Surplus (BHCK3240)
|
+-- 26. Retained Earnings (BHCK3247)
|
+-- 27. AOCI (BHCKB530)
     +-- 27.a AOCI on AFS securities (BHCK8434)
```

---

## Asset Detail Hierarchy

### Securities (HC-B)

```
HC-B Total Securities
|
+-- AFS Fair Value (BHCT1773) - Column B
|   +-- 1. U.S. Treasury (BHCK1287)
|   +-- 2. Agency Obligations (BHCKJF78)
|   +-- 3. MBS
|   |   +-- 3.a GNMA (BHCKG301)
|   |   +-- 3.b FNMA/FHLMC (BHCKG309)
|   |   +-- 3.c Non-agency RMBS (BHCKG317)
|   +-- 4. CMBS
|   |   +-- 4.a Agency CMBS (BHCKK143)
|   |   +-- 4.b Non-agency CMBS (BHCKK151)
|   +-- 5. Asset-backed Securities (BHCKC027)
|   |   +-- 5.a Credit card (BHCKB839)
|   |   +-- 5.b HELOC (BHCKB843)
|   |   +-- 5.c Auto (BHCKB847)
|   |   +-- 5.d Other consumer (BHCKB851)
|   |   +-- 5.e C&I / CLO (BHCKB855)
|   |   +-- 5.f Other (BHCKB859)
|   +-- 6.a Domestic corp bonds (BHCK1741)
|   +-- 6.b Foreign corp bonds (BHCK1746)
|   +-- 7. Munis (BHCK8497)
|
+-- HTM Amortized Cost (BHCT1754) - Column C
|   +-- [Same structure as AFS, different MDRM codes]
|
+-- Equity Securities with readily determinable fair values not held for trading (BHCKJA22) - M5
    +-- (reported as a single line on HC-B Memorandum 5; not split into mutual-funds/other components on the FR Y-9C)
```

### Loans (HC-C)

```
HC-C Net Loans (BHCKB529) = Sum(Items 1-9) - Item 10 - Item 11
|
+-- 1. Real Estate Loans (BHCK1410)
|   +-- 1.a Construction & Land (BHCK1415)
|   |   +-- 1.a.(1) 1-4 Family ADC (BHCKF158)
|   |   +-- 1.a.(2) Other ADC (BHCKF159)
|   +-- 1.b Farmland (BHCK1420)
|   +-- 1.c HELOCs (BHCK1797)
|   +-- 1.d 1-4 Family Closed End (= 1.d.(1) + 1.d.(2); no atomic code)
|   |   +-- 1.d.(1) First liens (BHCK5367)
|   |   +-- 1.d.(2) Junior liens (BHCK5368)
|   +-- 1.e Multifamily (BHCK1460)
|   |   +-- 1.e.(1) With govt guarantees (BHCKKX57)
|   |   +-- 1.e.(2) Other (BHCKKX58)
|   +-- 1.f CRE Nonfarm Nonres (BHCK1480)
|       +-- 1.f.(1) Owner-occupied (BHCKF160)
|       +-- 1.f.(2) Non-owner-occupied (BHCKF161)
|
+-- 2. Loans to Depository Institutions (BHCK1288)
|   +-- 2.a US banks/thrifts (BHCK1292)
|   +-- 2.b Foreign banks (BHCK1296)
|   +-- 2.c Acceptances (BHCK1755)
|
+-- 3. Agricultural Production (BHCK1590)
|
+-- 4. C&I Loans (BHCK1766)
|   +-- 4.a Domestic addressees (BHCK1763)
|   +-- 4.b Foreign addressees (BHCK1763)
|
+-- 5. Consumer Loans (BHCK1975)
|   +-- 5.a Credit Cards (BHCKB538)
|   |   +-- 5.a.(1) Consumer CC (BHDMB561)
|   |   +-- 5.a.(2) Corporate CC (BHCKK137)
|   +-- 5.b Other revolving (BHCKB539)
|   +-- 5.c Auto loans (BHCKK137)
|   |   +-- 5.c.(1) New vehicles (BHCKK138)
|   |   +-- 5.c.(2) Used vehicles (BHCKK139)
|   +-- 5.d Other consumer (BHCKK207)
|
+-- 6. Foreign Governments (BHCK1296)
|
+-- 7. Obligations of states & political subdivisions (no consolidated BHCK code; Call basis RCFD/RCON2107)
|
+-- 8. Other Loans (BHCK1563)
|   +-- 8.a Securities loans (BHCK1545)
|   +-- 8.b All other (BHCK1564)
|
+-- 9. Lease Financing (BHCK2165)
|   +-- 9.a Individual leases (BHCKF164)
|   +-- 9.b Other leases (BHCKF163)
|
+-- 10. LESS: Unearned Income (BHCK2123)
|
+-- 11. LESS: Allowance (BHCT3123)
```

### Trading Assets (HC-D)

```
HC-D Total Trading Assets (BHCT3545) - Item 12
|
+-- 1. U.S. Treasury (BHCM3531)
|
+-- 2. U.S. Agency (BHCM3532)
|
+-- 3. Securities by States/Munis (BHCM3533)
|
+-- 4. Other Debt Securities (BHCKHT59)
|
+-- 5. Mortgage-Backed Securities
|   +-- 5.a RMBS GNMA (BHCKK197)
|   +-- 5.b RMBS FNMA/FHLMC (BHCKK198)
|   +-- 5.c RMBS Non-agency (BHCKK199)
|   +-- 5.d CMBS Agency (BHCKK200)
|   +-- 5.e CMBS Non-agency (BHCKK201)
|
+-- 6. Trading Loans
|   +-- 6.a Domestic loans (BHCKHT63)
|   +-- 6.b Foreign loans (BHCKHT64)
|   +-- 6.c High-yield bonds (BHCKF614)
|   +-- 6.d Leveraged loans (BHCKHT65)
|   +-- 6.e Other loans (BHCKF618)
|
+-- 9. Other Trading Assets (BHCM3541)
|
+-- 11. Derivative Contracts Positive FV (BHCT3543) --> [Detail: Schedule HC-L]
```

### Trading Liabilities (HC-D)

```
HC-D Total Trading Liabilities (BHCT3548) - Item 15
|
+-- 13. Short Positions
|   +-- 13.a.(1) U.S. Treasury shorts (BHCKG209)
|   +-- 13.a.(2) U.S. Agency shorts (BHCKG210)
|   +-- 13.a.(3) Other shorts (BHCKG211)
|   +-- 13.b Other trading liabilities (BHCKF624)
|
+-- 14. Derivative Contracts Negative FV (BHCT3547) --> [Detail: Schedule HC-L]
```

---

## Capital Hierarchy

### Basel III Capital Cascade

```
Total Capital (BHCA3792) = Tier 1 (BHCA8274) + Tier 2 (BHCA5311)
                                |                    |
                                |                    |
                                v                    v
+---------------------------+  +---------------------------+
|    TIER 1 CAPITAL         |  |    TIER 2 CAPITAL         |
|    (BHCA8274)             |  |    (BHCA5311)             |
+---------------------------+  +---------------------------+
|                           |  |                           |
| CET1 (BHCAP859)           |  | T2 Instruments (BHCAP866) |
|   |                       |  | T2 Phase-out  (BHCAP867)  |
|   +-- CET1 Before Adj     |  | T2 Before Ded (BHCAP870)  |
|   |   (BHCAP840)          |  | LESS: T2 Ded  (BHCAP872)  |
|   |   +-- Common Stock    |  | = Total T2    (BHCA5311)  |
|   |   |   (BHCAP742)      |  +---------------------------+
|   |   +-- Retained Earn   |
|   |   |   (BHCAKW00)      |
|   |   +-- AOCI opt-out    |
|   |   |   (BHCAP838)      |
|   |   +-- CET1 Minority   |
|   |       (BHCAP839)      |
|   |                       |
|   +-- LESS: CET1 Deduct   |
|       (BHCAP852)          |
|       +-- Goodwill (841)  |
|       +-- Intangibles(842)|
|       +-- DTA NOL (843)   |
|       +-- Gain on Sale    |
|       +-- Pension Assets  |
|       +-- Own Shares (846)|
|       +-- Reciprocal (847)|
|       +-- FI Invest (848) |
|       +-- MSA (849)       |
|       +-- DTA Temp (850)  |
|       +-- Other (851)     |
|                           |
| Additional T1 (BHCAP865)  |
|   +-- AT1 Instruments     |
|       (BHCAP860)          |
|   +-- T1 Minority Int     |
|       (BHCAP862)          |
|   +-- AT1 Before Deduct   |
|       (BHCAP863)          |
|   +-- LESS: AT1 Deduct    |
|       (BHCAP864)          |
+---------------------------+
```

> **Capital-code notes (all `BHCA` mnemonic, FR Y-9C Schedule HC-R, MDRM-verified):**
> Tier 1 = `BHCA8274`, Tier 2 = `BHCA5311`, Total = `BHCA3792`, CET1 = `BHCAP859`,
> **AT1 = `BHCAP865`** (AT1 buildup: instruments `BHCAP860`, Tier-1 minority `BHCAP862`,
> before deductions `BHCAP863`, deductions `BHCAP864`). Tier 2 buildup: instruments `BHCAP866`,
> phase-out `BHCAP867`, before deductions `BHCAP870`, deductions `BHCAP872`.
> The CET1 adjustment/deduction items shown as `(841)…(851)` are `BHCAP841`–`BHCAP851`
> (subtotal `BHCAP852`; total CET1 adjustments & deductions `BHCAP858`). Note `BHCAP856`
> is **not** AT1 — it is "significant investments in unconsolidated financial institutions
> exceeding the 15% CET1 threshold"; `BHCAP838` is the **AOCI opt-out election flag** (1/0),
> not an AOCI dollar amount.

### Capital Ratio Calculations

```
CET1 Ratio (BHCAP793)  = CET1 Capital (BHCAP859) / Total RWA (BHCAA223)
                         Minimum: 4.5%

Tier 1 Ratio (BHCA7206) = Tier 1 Capital (BHCA8274) / Total RWA (BHCAA223)
                          Minimum: 6.0%

Total Capital Ratio (BHCA7205) = Total Capital (BHCA3792) / Total RWA (BHCAA223)
                                 Minimum: 8.0%

Leverage Ratio (BHCA7204) = Tier 1 Capital (BHCA8274) / Average Total Assets
                            Minimum: 4.0%
```

### Risk-Weighted Assets Composition

```
Total RWA (BHCAA223) - Schedule HC-R Part II
|
+-- 0% Risk Weight (BHCKA221)
|   +-- Cash, Treasuries
|
+-- 20% Risk Weight (BHCKS396)
|   +-- GSE, Munis, Interbank
|
+-- 50% Risk Weight (BHCKS397)
|   +-- Prudent residential mortgages
|
+-- 100% Risk Weight (BHCKS398)
|   +-- C&I, CRE, most loans
|
+-- 150% Risk Weight (BHCKS399)
|   +-- HVCRE, non-IG exposures
|
+-- Securitization RWA (BHCKS400)
|
+-- Equity Exposures RWA (computed across HC-R Part II equity risk-weight bands; no single atomic BHCK code)
|
+-- Derivatives RWA (BHCKS402)
|
+-- Off-Balance Sheet RWA (BHCKS403)
|
+-- Market Risk RWA (BHCKA222)
```

---

## Income Statement Hierarchy

```
HI Net Income (BHCT4340) - Schedule HI Item 12
|
+-- Net Interest Income (BHCK4074) = Interest Income - Interest Expense
|   |
|   +-- Interest Income (BHCK4107)
|   |   +-- 1.a Loans (BHCK4010)
|   |   +-- 1.b Securities (BHCK4065)
|   |   +-- 1.c Fed funds/resale (BHCK4115)
|   |   +-- 1.d Deposits in banks (BHCK4060)
|   |   +-- 1.e Trading assets (BHCK4069)
|   |   +-- 1.f Other interest income (BHCK4518)
|   |
|   +-- LESS: Interest Expense (BHCK4073)
|       +-- 2.a Deposits [caption; = domestic + foreign office interest, no single BHCK code]
|       +-- 2.b Fed funds/repos (BHCK4180)
|       +-- 2.c Trading liabilities (BHCK4180)
|       +-- 2.d Other borrowed (BHCK4185)
|
+-- LESS: Provision for Credit Losses (BHCT4230)
|
+-- Noninterest Income (BHCK4079)
|   +-- 6.a Service charges (BHCK4070)
|   +-- 6.b Trading revenue (BHCKB492)
|   +-- 6.c Fiduciary income (BHCKA220)
|   +-- 6.d Investment banking (BHCKB497)
|   +-- 6.e Insurance underwriting income (BHCKC386)
|   +-- 6.f Other noninterest income (BHCKB497)
|
+-- LESS: Noninterest Expense (BHCK4093)
|   +-- 7.a Salaries & benefits (BHCK4135)
|   +-- 7.b Premises (BHCK4217)
|   +-- 7.c Other (BHCK4092)
|
+-- Income Before Taxes (BHCK4301)
|
+-- LESS: Taxes (BHCK4302)
|
+-- Net Income (BHCT4340)
```

---

## Derivatives Hierarchy

### HC-L Fair Value Reconciliation to HC-D

```
HC-D Item 11 - Derivatives Positive FV (BHCT3543)
|
= Sum of:
|
+-- Trading Positive FV
|   +-- Interest Rate (BHCK8733)
|   +-- Foreign Exchange (BHCK8734)
|   +-- Equity (BHCK8735)
|   +-- Commodity/Other (BHCK8736)
|
+-- Non-Trading Positive FV
    +-- Interest Rate (BHCK8741)
    +-- Foreign Exchange (BHCK8742)
    +-- Equity (BHCK8743)
    +-- Commodity/Other (BHCK8744)


HC-D Item 14 - Derivatives Negative FV (BHCT3547)
|
= Sum of:
|
+-- Trading Negative FV
|   +-- Interest Rate (BHCK8737)
|   +-- Foreign Exchange (BHCK8738)
|   +-- Equity (BHCK8739)
|   +-- Commodity/Other (BHCK8740)
|
+-- Non-Trading Negative FV
    +-- Interest Rate (BHCK8745)
    +-- Foreign Exchange (BHCK8746)
    +-- Equity (BHCK8747)
    +-- Commodity/Other (BHCK8748)
```

### Credit Derivatives Structure

```
Credit Derivatives - Schedule HC-L
|
+-- Protection SOLD (Notional)
|   +-- CDS Sold (BHCKC968)
|   +-- TRS Sold (BHCKC970)
|   +-- Other Credit Sold (BHCKC974)
|
+-- Protection BOUGHT (Notional)
    +-- CDS Bought (BHCKC969)
    +-- TRS Bought (BHCKC971)
    +-- Other Credit Bought (BHCKC975)

Net Exposure = Bought - Sold
```

---

## Cross-Schedule Tie-Outs

### Master Tie-Out Table

| HC Item | MDRM | Must Equal | Detail Schedule | MDRM |
|---------|------|------------|-----------------|------|
| 2.a HTM | BHCKJJ34 | = | HC-B Item 8 Col C | BHCT1754 |
| 2.b AFS | BHCT1773 | = | HC-B Item 8 Col B | BHCT1773 |
| 4.b Loans | BHCTB528 | = | HC-C Item 12 | BHCTB528 |
| 4.c ALLL | BHCT3123 | = | HC-C Item 11 | BHCT3123 |
| 5 Trading Assets | BHCT3545 | = | HC-D Item 12 | BHCT3545 |
| 11 Other Assets | BHCT2160 | = | HC-F Item 12 | BHCT2160 |
| 15 Trading Liab | BHCT3548 | = | HC-D Item 15 | BHCT3548 |
| 20 Other Liab | BHCK2750 | = | HC-G Item 5 | BHCK2750 |

### Derivatives Cross-Schedule Tie-Outs

| HC-D Item | MDRM | Must Equal | HC-L | Calculation |
|-----------|------|------------|------|-------------|
| 11 Pos FV | BHCT3543 | = | Sum Positive FV | 8733+8734+8735+8736+8741+8742+8743+8744 |
| 14 Neg FV | BHCT3547 | = | Sum Negative FV | 8737+8738+8739+8740+8745+8746+8747+8748 |

---

## Validation Checklist

Use this checklist when validating regulatory data:

- [ ] Balance Sheet: BHCK2170 = BHCK2948 + BHCK3210 (= BHCK3300)
- [ ] Total Assets: BHCT2170 = Sum(Items 1-11)
- [ ] Total Liabilities: BHCK2948 = Sum(Items 13-20)
- [ ] Total Equity: BHCT3210 = Sum(Items 23-27)
- [ ] Trading Assets: BHCT3545 (HC.5) = BHCT3545 (HC-D.12)
- [ ] Trading Liabilities: BHCT3548 (HC.15) = BHCT3548 (HC-D.15)
- [ ] Net Loans: BHCTB528 (HC.4.b) = BHCKB529 (HC-C.12)
- [ ] Allowance: BHCT3123 (HC.4.c) = BHCT3123 (HC-C.11)
- [ ] Other Assets: BHCT2160 (HC.11) = BHCT2160 (HC-F.12)
- [ ] Other Liabilities: BHCK2750 (HC.20) = BHCK2750 (HC-G.5)
- [ ] Derivatives Pos FV: BHCT3543 = Sum(HC-L Positive FV)
- [ ] Derivatives Neg FV: BHCT3547 = Sum(HC-L Negative FV)
- [ ] Tier 1 Capital: BHCA8274 = BHCAP859 + BHCAP865
- [ ] Total Capital: BHCA3792 = BHCA8274 + BHCA5311
- [ ] CET1 Ratio: BHCAP793 = BHCAP859 / BHCAA223

---

*See also: [RECONCILIATION_FORMULAS_COMPLETE.csv](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) for 60+ reconciliation formulas*

*Last updated: 2026-01-29 | Version 1.0*
