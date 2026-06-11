# Call Report Schedule RI - Income Statement

> **Consolidated Report of Income for FDIC-Insured Banks**
>
> Form: FFIEC 031/041/051 | Frequency: Quarterly

---

## Overview

Schedule RI is the income statement for Call Reports filed by FDIC-insured banks. It parallels Schedule HI from the FR Y-9C but at the individual bank level. Income items use the RIAD prefix (Report of Income All Domestic).

---

## MDRM Prefix Guide for Income

| Prefix | Scope | Description |
|--------|-------|-------------|
| RIAD | Income | Standard income statement items |
| RIAE | Income | Equity method income |
| RIAJ | Income | Annualized items |

---

## Interest Income (Items 1.a - 1.h)

| Item | Description | MDRM | Y-9C Equiv | Notes |
|------|-------------|------|------------|-------|
| 1.a | Loans secured by real estate | RIAD4011 | Various | By property type |
| 1.a.(1) | 1-4 family residential | RIAD4012 | - | |
| 1.a.(2) | Other real estate | RIAD4013 | - | |
| 1.b | All other loans | RIAD4010 | BHCK4010 | C&I, consumer, other |
| 1.c | Lease financing receivables | RIAD4065 | BHCK4065 | |
| 1.d | Balances due from depository | RIAD4115 | BHCK4115 | |
| 1.e | Securities - taxable | RIADB488 | BHCKB488 | |
| 1.f | Securities - tax-exempt | RIAD4507 | BHCK4507 | Municipal interest |
| 1.g | Trading assets | RIAD4069 | BHCK4069 | Interest income from trading assets |
| 1.h | Fed funds sold | RIAD4020 | BHCK4020 | + resale agreements |
| 1.i | Other interest income | RIAD4518 | BHCK4518 | |
| **1** | **Total interest income** | **RIAD4107** | **BHCK4107** | |

---

## Interest Expense (Items 2.a - 2.d)

| Item | Description | MDRM | Y-9C Equiv | Notes |
|------|-------------|------|------------|-------|
| 2.a | Deposits (total interest) | RIAD4170 | - | All deposit interest |
| 2.a.(1) | Transaction accounts | RIAD4508 | - | NOW/ATS/telephone & preauth transfer accounts |
| 2.a.(2) | MMDA | RIAD4509 | - | Money market deposit accounts |
| 2.a.(3) | Time deposits | RIADA517 + RIADA518 | - | $100k or more + less than $100k |
| 2.b | Fed funds purchased + repos | RIAD4180 | BHCK4180 | |
| 2.c | Trading liabilities & other borrowed money | RIAD4185 | BHCK4185 | |
| 2.e | Subordinated debt | RIAD4200 | BHCK4397 | Notes/debentures subordinated to deposits |
| **2** | **Total interest expense** | **RIAD4073** | **BHCK4073** | |

---

## Net Interest Income

| Item | Description | MDRM | Y-9C Equiv | Formula |
|------|-------------|------|------------|---------|
| **3** | **Net interest income** | **RIAD4074** | **BHCK4074** | Item 1 - Item 2 |
| 4 | Provision for credit losses | RIAD4230 | BHCT4230 | CECL provision |
| 5 | NII after provision | RIAD4079 | - | Item 3 - Item 4 |

---

## Noninterest Income (Items 5.a - 5.p)

| Item | Description | MDRM | Y-9C Equiv | Notes |
|------|-------------|------|------------|-------|
| 5.a | Service charges on deposits | RIAD4080 | BHCK4483 | |
| 5.b | Trading revenue | RIADA220 | BHCKA220 | |
| 5.c | Investment banking fees | RIADC886 | BHCKC886 | Advisory, underwriting |
| 5.d | Fiduciary income | RIAD4070 | BHCK4070 | Trust activities |
| 5.e | Servicing fees | RIADB492 | BHCKB492 | Loan servicing |
| 5.f | Securitization income | RIADB493 | BHCKB493 | |
| 5.g | Insurance income | RIADC386 | BHCKC386 | |
| 5.h | Securities gains (losses) | RIAD3521 | BHCK3521 | Net securities G/L |
| 5.i | Net gains (losses) on sales of loans | RIAD5416 | - | Mortgage banking / loan sales |
| 5.j | Venture capital revenue | RIADB491 | BHCKB491 | |
| 5.k | Bank-owned life insurance | RIAD4042 | BHCK4042 | BOLI income |
| 5.l | Other noninterest income | RIADB497 | BHCKB497 | |
| **5** | **Total noninterest income** | **RIAD4079** | **BHCK4079** | Sum of 5.a-5.l |

---

## Noninterest Expense (Items 7.a - 7.g)

| Item | Description | MDRM | Y-9C Equiv | Notes |
|------|-------------|------|------------|-------|
| 7.a | Salaries and benefits | RIAD4135 | BHCK4135 | Personnel expense |
| 7.b | Premises and fixed assets | RIAD4217 | BHCK4217 | Occupancy |
| 7.c | Amortization of intangibles | RIADC232 | BHCKC232 | |
| 7.d | Goodwill impairment | RIADC216 | BHCKC216 | Goodwill impairment losses |
| 7.e | Other NIE | RIAD4092 | BHCK4092 | Catch-all |
| **7** | **Total noninterest expense** | **RIAD4093** | **BHCK4093** | Sum of 7.a-7.g |

---

## Net Income Calculation

| Item | Description | MDRM | Y-9C Equiv | Formula |
|------|-------------|------|------------|---------|
| 8.c | Income before income taxes & discontinued ops | RIAD4301 | BHCK4301 | Items 3-4+5-7 |
| 9 | Applicable income taxes | RIAD4302 | BHCK4302 | |
| 10 | Income before discontinued operations | RIAD4300 | BHCK4300 | Item 8 - Item 9 |
| 11 | Discontinued operations, net of taxes | RIAD4320 | BHCK4320 | (formerly extraordinary items) |
| **12** | **Net income (loss)** | **RIAD4340** | **BHCK4340** | Bottom line |

---

## Key Performance Ratios

### Calculated from RI Data

| Ratio | Formula | Benchmark |
|-------|---------|-----------|
| **NIM** | RIAD4074 / Avg Earning Assets | 2.5-4.0% |
| **ROA** | RIAD4340 / Avg Total Assets | 0.8-1.2% |
| **ROE** | RIAD4340 / Avg Equity | 8-12% |
| **Efficiency Ratio** | RIAD4093 / (RIAD4074 + RIAD4079) | < 60% |
| **Provision Rate** | RIAD4230 / Avg Loans | Variable |

### Trading Revenue Analysis

| Item | MDRM | Description |
|------|------|-------------|
| Interest rate exposures | RIAD8757 | IR trading revenue |
| Foreign exchange exposures | RIAD8758 | FX trading revenue |
| Equity security/index exposures | RIAD8759 | Equity trading revenue |
| Commodity and other exposures | RIAD8760 | Commodity/other trading revenue |

---

## Memoranda Items

| Item | Description | MDRM | Purpose |
|------|-------------|------|---------|
| M.1 | Interest income from loans | Various | By loan type detail |
| M.2 | Interest expense on deposits | Various | By deposit type |
| M.3 | Int income from MBS | RIADB485 | Securities breakdown |
| M.6 | Net gains (losses) on sales of loans | RIAD5416 | Mortgage banking |
| M.7 | Net servicing fees | RIADB492 | MSR / loan servicing income |

---

## Cross-Schedule Relationships

| RI Ties To | Relationship |
|------------|--------------|
| RC | Balance sheet averages for ratio calculations |
| RI-B | Charge-offs feed provision |
| RI-E | Securities gains/losses detail |
| RC-K | Average balances |

---

## Mapping to FR Y-9C Schedule HI

| Call Report | FR Y-9C | Notes |
|-------------|---------|-------|
| RIAD4107 | BHCK4107 | Total interest income |
| RIAD4073 | BHCK4073 | Total interest expense |
| RIAD4074 | BHCK4074 | Net interest income |
| RIAD4079 | BHCK4079 | Total noninterest income |
| RIAD4093 | BHCK4093 | Total noninterest expense |
| RIAD4340 | BHCT4340 | Net income |

Generally: Replace RIAD with BHCT or BHCK for Y-9C equivalents.

---

*See also: [HI_INCOME_STATEMENT_GUIDE.md](HI_INCOME_STATEMENT_GUIDE.md) for FR Y-9C equivalent*

*Last updated: 2026-01-29*
