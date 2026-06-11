# Schedule HC-K: Quarterly Averages Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-K - Quarterly Averages
**Frequency**: Quarterly
**Purpose**: Report quarterly average balances for selected assets, liabilities, and equity

---

## Overview

Schedule HC-K reports **quarterly averages** for selected assets, liabilities, and equity capital. Averages smooth intra-quarter fluctuations and are the proper denominators for yield, cost, and profitability ratios, where point-in-time balance-sheet figures would distort the result.

### How Averages Are Computed

Report, for each item, the average of the balances as of the close of business **either**:
- for **each day** of the calendar quarter, **or**
- as of the close of business **on each Wednesday** during the calendar quarter.

For days the company (or a consolidated subsidiary or branch) is closed (weekends, holidays), use the amount outstanding from the previous business day. Business combinations, common-control transactions, and newly formed holding companies have specific numerator/denominator conventions (see the FR Y-9C instructions for HC-K).

### Why Averages Matter

- **Yield on earning assets** = interest income ÷ average earning assets
- **Cost of funds** = interest expense ÷ average interest-bearing liabilities
- **Net interest margin (NIM)** = net interest income ÷ average earning assets
- **Return on average assets / equity** = net income ÷ average total assets / equity

---

## Who Files

All holding companies that file the FR Y-9C complete Schedule HC-K. Insurance SLHCs that do not calculate averages as prescribed may use an industry convention or best-efforts estimates, disclosing the method used in the "Notes to the Balance Sheet — Other" section.

**ASU 2016-13 (CECL) treatment.** Companies that have adopted ASU 2016-13 do **not** deduct allowances for credit losses from amortized cost when computing averages for items 1 through 4, but **do** deduct allowances when computing the average for total consolidated assets (item 5).

---

## Line Items and MDRM Codes

### Assets

| Item | Description | MDRM | Ties To | Start |
|------|-------------|------|---------|-------|
| 1.a | Securities: U.S. Treasury and U.S. Government agency obligations (excluding MBS) | BHCKB558 | HC-B items 1-2 (cols A, C) | 2011-03-31 |
| 1.b | Securities: Mortgage-backed securities | BHCKB559 | HC-B item 4 (cols A, C) | 2011-03-31 |
| 1.c | Securities: All other debt and equity securities with readily determinable fair values not held for trading | BHCKB560 | HC-B items 3, 5-7 | 2011-03-31 |
| 2 | Federal funds sold and securities purchased under agreements to resell | BHCK3365 | HC item 3 | 1990-09-30 |
| 3.a | Total loans and leases in domestic offices (held for investment) | BHDM3516 | HC-C items 1-11 col B | 2010-03-31 |
| 3.a.(1) | Loans secured by 1-4 family residential properties | BHDM3465 | HC-C item 1.c col B | 2008-03-31 |
| 3.a.(2) | All other loans secured by real estate | BHDM3466 | HC-C items 1.a, 1.b, 1.d, 1.e col B | 2008-03-31 |
| 3.a.(3) | Loans to finance agricultural production and other loans to farmers | BHDM3386 | HC-C item 3 col B | 2011-03-31 |
| 3.a.(4) | Commercial and industrial loans | BHDM3387 | HC-C item 4 col B | 2011-03-31 |
| 3.a.(5)(a) | Loans to individuals: Credit cards | BHDMB561 | HC-C item 6.a | 2011-03-31 |
| 3.a.(5)(b) | Loans to individuals: Other | BHDMB562 | HC-C items 6.b-6.d | 2011-03-31 |
| 3.b | Total loans and leases in foreign offices, Edge and Agreement subsidiaries, and IBFs | BHFN3360 | HC-C items 1-10 less 11 | 2010-03-31 |
| 4.a | Trading assets *(conditional — see below)* | BHCK3401 | HC item 5 | 2001-03-31 |
| 4.b | Other earning assets | BHCKB985 | — | 2001-03-31 |
| 5 | Total consolidated assets *(not a sum — see below)* | BHCK3368 | HC item 12 | 1981-06-30 |

**Item 4.a is conditional.** Trading assets (BHCK3401) is completed only by holding companies that reported total trading assets of **$10 million or more in any of the four preceding calendar quarters**. Trading assets include derivatives with positive fair values.

**Item 5 is not the sum of items 1-4.b.** Total consolidated assets (BHCK3368) is defined as Schedule HC, item 12 "Total assets," with prescribed valuation exceptions (debt securities not held for trading at amortized cost; AFS/other equity securities at the values specified in the instructions). The FR Y-9C instructions state explicitly that **item 5 is NOT the sum of items 1 through 4.b.** Fed validity edit **2770** requires item 5 to be greater than zero.

### Liabilities and Equity

| Item | Description | MDRM | Ties To | Start |
|------|-------------|------|---------|-------|
| 6 | Interest-bearing deposits (domestic) | BHCK3517 | HC-E items 1.b-1.e, 2.b-2.e | 1981-06-30 |
| 7 | Interest-bearing deposits (foreign) | BHCK3404 | HC item 13.b.(2) | 1981-06-30 |
| 8 | Federal funds purchased and securities sold under agreements to repurchase | BHCK3353 | HC item 14 | 1990-09-30 |
| 9 | All other borrowed money | BHCK2635 | HC item 16 | 1981-06-30 |
| 10 | **Not applicable** | — | — | — |
| 11 | Total equity capital | BHCK3519 | HC item 27.a | 1981-06-30 |

**Item 9** includes commercial paper and all other borrowed money regardless of maturity.

**Item 10 is "Not applicable"** on the current FR Y-9C form. It is intentionally blank — there is no MDRM code and no amount to report.

**Item 11** (total equity capital) is reported as defined for Schedule HC, item 27.a and excludes limited-life preferred stock. Net unrealized gains/losses on AFS securities and accumulated net gains/losses on cash-flow hedges are included when computing average equity.

---

## Historical (End-Dated) Items

Several earlier HC-K lines are genuine predecessors that were reported on the form in prior years and then end-dated. They are valuable for constructing long quarterly-average time series that span the form's evolution.

| Hist. item | Description | MDRM | Reported on form | Notes |
|------------|-------------|------|-------------------|-------|
| H.1 | Securities (combined quarterly average) | BHCK3515 | 1981-2010 | Superseded by items 1.a-1.c (granular securities split) from 2011 |
| H.2 | Loans and leases, consolidated | BHCK3516 | 1981-2009 | Superseded on the form by items 3.a / 3.b; **from 2010-03-31 BHCK3516 continues as an MDRM-derived consolidated series (domestic + foreign)** for time-series continuity |
| H.3 | Total earning assets | BHCK3402 | 1981-2000 | Dropped from the form after 2000 |
| H.4 | Limited-life preferred stock | BHCK3518 | 1981-1996 | Dropped from the form after 1996 |

When building a continuous loans-and-leases average across the 2010 form change, BHCK3516 (H.2) bridges the older combined series to the newer domestic/foreign split (BHDM3516 + BHFN3360).

---

## Relationships and Tie-Outs

HC-K averages correspond to point-in-time Schedule HC and detail-schedule items:

```
HC-K item 1 (1.a + 1.b + 1.c)  ←→  HC-B securities (amortized cost / FV per instructions)
HC-K item 2 (BHCK3365)         ←→  HC item 3   (fed funds sold / reverse repos)
HC-K item 3 (3.a + 3.b)        ←→  HC-C loans and leases
HC-K item 4.a (BHCK3401)       ←→  HC item 5   (trading assets, if $10M threshold met)
HC-K item 5 (BHCK3368)         ←→  HC item 12  (total assets) — NOT a sum of items 1-4.b
HC-K item 6 (BHCK3517)         ←→  HC-E domestic interest-bearing deposits
HC-K item 7 (BHCK3404)         ←→  HC item 13.b.(2)  (foreign interest-bearing deposits)
HC-K item 8 (BHCK3353)         ←→  HC item 14  (fed funds purchased / repos)
HC-K item 9 (BHCK2635)         ←→  HC item 16  (other borrowed money)
HC-K item 11 (BHCK3519)        ←→  HC item 27.a (total equity capital)
```

### Reasonableness Checks

```
Average balance ≈ (Beginning balance + Ending balance) / 2
```
Large deviations may indicate significant intra-period transactions, acquisitions/divestitures, or reclassifications.

---

## Key Profitability Ratios Using HC-K

```
NIM            = Net interest income (HI item 3) / Average earning assets
Yield          = Total interest income (HI item 1) / Average earning assets
Cost of funds  = Total interest expense (HI item 2) / Average interest-bearing liabilities
ROAA           = Net income (HI item 12) / Average total assets (HC-K item 5)
ROAE           = Net income (HI item 12) / Average total equity (HC-K item 11)
```

Because HC-K does not report a single "total earning assets" or "total interest-bearing liabilities" average line, those aggregates are built from the relevant component averages (securities + fed funds sold + loans + trading + other earning assets for earning assets; interest-bearing deposits + repos + other borrowed money for interest-bearing liabilities).

---

## Common Pitfalls

- **Computing item 5 as the sum of items 1-4.b.** It is not. Total consolidated assets (BHCK3368) is HC item 12 with valuation exceptions, and Fed edit 2770 requires it to be > 0.
- **Expecting an amount in item 10.** Item 10 is "Not applicable" on the current form.
- **Completing item 4.a below the threshold.** Trading assets (BHCK3401) is conditional on $10M+ trading assets in any of the four preceding quarters.
- **Confusing the loan series across the 2010 form change.** Use BHCK3516 (H.2) to bridge the pre-2010 combined loans-and-leases average to the post-2010 domestic (BHDM3516) plus foreign (BHFN3360) split.
- **Forgetting the CECL averaging rule.** Allowances are deducted for item 5 but not for items 1-4 under ASU 2016-13.

---

## Verification and Provenance

Every MDRM code in this guide was verified against the Federal Reserve Micro Data Reference Manual (MDRM) snapshot downloaded 2026-06-11 and was observed as a reported column in actual FR Y-9C data. The current and historical HC-K codes appear in Federal Reserve bulk BHCF data over their respective reporting windows (1986-2021 for the long-running items; granular securities and loan splits from their 2008-2011 start dates).

**Sources:**
- MDRM (Federal Reserve Micro Data Reference Manual)
- FR Y-9C form and instructions

---

*Last Updated: 2026-06-11 (v7.0 — MDRM-verified rebuild)*
*Reference: FR Y-9C form and instructions; MDRM*
