# Schedule HC-C: Loans and Lease Financing Receivables Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-C - Loans and Lease Financing Receivables
**Frequency**: Quarterly
**Purpose**: Detail the loan and lease portfolio by collateral type, borrower type, and geography

---

## Overview

Schedule HC-C is the primary schedule for loan portfolio analysis. It provides:
- **Granular loan breakdowns** by collateral and purpose
- **Two-column reporting**: Column A vs. Column B (see below)
- **Basis for asset quality analysis** (ties to HC-N)
- **Risk-weighted asset inputs** for capital calculations (HC-R)

### The Two Columns (critical)

| Column | Meaning | MDRM prefix |
|--------|---------|-------------|
| **Column A** | Consolidated / total (the whole holding company) | **BHCK** |
| **Column B** | "In domestic offices" only | **BHDM** |

Not every line is reported in both columns. Some lines are Column A only (e.g., construction 1.a.(1)/1.a.(2)), some are Column B only (e.g., farmland 1.b, HELOC 1.c.(1)), and a few are reported in both (e.g., item 3 agricultural, item 7 foreign governments, item 11 unearned income, item 12 total). The CSV maps **Column A -> `mdrm_total`** and **Column B -> `mdrm_domestic`**. The `mdrm_foreign` column is "-" throughout because the current FR Y-9C HC-C has no separate foreign-office (BHFN) loan codes; the only geographic split on this schedule is the domestic-offices Column B.

---

## Schedule Structure (current / March 2026 form)

```
LOAN AND LEASE PORTFOLIO
├── Item 1: Loans secured by real estate (BHCK1410, Col A total)
│   ├── 1.a.(1): 1-4 family residential construction   (A: BHCKF158)
│   ├── 1.a.(2): Other construction / land development   (A: BHCKF159)
│   ├── 1.b:     Secured by farmland                     (B: BHDM1420)
│   ├── 1.c.(1): Revolving open-end 1-4 family (HELOCs)  (B: BHDM1797)
│   ├── 1.c.(2)(a): Closed-end 1-4 family, first liens   (B: BHDM5367)
│   ├── 1.c.(2)(b): Closed-end 1-4 family, junior liens  (B: BHDM5368)
│   ├── 1.d:     Multifamily (5+ units)                  (B: BHDM1460)
│   ├── 1.e.(1): Owner-occupied nonfarm nonresidential   (A: BHCKF160)
│   └── 1.e.(2): Other nonfarm nonresidential            (A: BHCKF161)
├── Item 2: Loans to depository institutions & acceptances (B: BHDM1288)
│   ├── 2.a: To U.S. banks / U.S. depository institutions (A: BHCK1292)
│   └── 2.b: To foreign banks                             (A: BHCK1296)
├── Item 3: Ag production & other loans to farmers (A: BHCK1590 / B: BHDM1590)
├── Item 4: Commercial and industrial loans (B total: BHDM1766)
│   ├── 4.a: To U.S. addressees (domicile)               (A: BHCK1763)
│   ├── 4.b: To non-U.S. addressees (domicile)           (A: BHCK1764)
│   └── 4.c: Combined U.S. + non-U.S. (single-column)    (A: BHCKKX56)
│   [Item 5: not used in the current form — the spec jumps 4 -> 6]
├── Item 6: Loans to individuals / consumer loans (B total: BHDM1975)
│   ├── 6.a: Credit cards                                (A: BHCKB538)
│   ├── 6.b: Other revolving credit plans                (A: BHCKB539)
│   ├── 6.c: Automobile loans                            (A: BHCKK137)
│   └── 6.d: Other consumer loans                        (A: BHCKK207)
├── Item 7: Loans to foreign governments (A: BHCK2081 / B: BHDM2081)
│   [Item 8: not used as a body line in the current form]
├── Item 9: Nondepository financial institutions & other loans
│   ├── 9.a:     Loans to nondepository financial inst.  (A: BHCKJ454 / B: BHDMJ454)
│   ├── 9.b.(1): Purchasing/carrying securities (margin) (A: BHCK1545 / B: BHDM1545)
│   ├── 9.b.(2): All other loans                         (A: BHCKJ451 / B: BHDMJ451)
│   └── 9.b.(3): Combined 9.b (single-column)            (A: BHCKKX57 / B: BHDMKX57)
├── Item 10: Lease financing receivables (B total: BHDM2165)
│   ├── 10.a: Leases to individuals (consumer leases)    (A: BHCKF162)
│   ├── 10.b: All other leases                           (A: BHCKF163)
│   └── 10.c: Lease finance receivables (combined)       (A: BHCKKX58)
├── Item 11: LESS: Any unearned income on loans (A: BHCK2123 / B: BHDM2123)
└── Item 12: TOTAL loans and leases (A: BHCK2122 / B: BHDM2122)
```

> **Numbering note.** The current form skips a numbered item 5 (the schedule goes 4 -> 6) and has no separate body item 8. Consumer loans are item 6, foreign governments are item 7, and nondepository-financial / other loans are item 9. Real-estate sub-lettering uses 1.c for 1-4 family residential and 1.e for nonfarm nonresidential.

---

## Detailed Line Item Analysis

### Item 1: Loans Secured by Real Estate

| Line | Column | MDRM | Description |
|------|--------|------|-------------|
| 1 (total) | A | BHCK1410 | Total real estate loans (consolidated) |
| 1.a.(1) | A | BHCKF158 | 1-4 family residential construction |
| 1.a.(2) | A | BHCKF159 | Other construction and all land development |
| 1.b | B | BHDM1420 | Secured by farmland (in domestic offices) |
| 1.c.(1) | B | BHDM1797 | Revolving open-end 1-4 family (HELOCs) |
| 1.c.(2)(a) | B | BHDM5367 | Closed-end 1-4 family, first liens |
| 1.c.(2)(b) | B | BHDM5368 | Closed-end 1-4 family, junior liens |
| 1.d | B | BHDM1460 | Multifamily (5+ units) |
| 1.e.(1) | A | BHCKF160 | Owner-occupied nonfarm nonresidential |
| 1.e.(2) | A | BHCKF161 | Other nonfarm nonresidential |

**Risk Characteristics**:
- Construction (1.a.(2)) is the highest-risk RE category; may include HVCRE at 150%.
- Closed-end 1-4 family first liens receive 35-50% risk weight under Basel III by LTV; junior liens 100%.
- Owner-occupied CRE repayment depends on business operations; other (non-owner) CRE on rental income.

> Lettering changed from earlier versions of this dictionary: the current form uses **1.c** for 1-4 family residential (revolving + closed-end first/junior liens) and **1.e** for nonfarm nonresidential. There is no separate 1.a construction subtotal or 1.f CRE subtotal line in the current form.

---

### Item 2: Loans to Depository Institutions and Acceptances of Other Banks

| Line | Column | MDRM | Description | Risk Weight |
|------|--------|------|-------------|-------------|
| 2 (total) | B | BHDM1288 | In domestic offices | 20-100% |
| 2.a | A | BHCK1292 | To U.S. banks / U.S. depository institutions | 20% |
| 2.b | A | BHCK1296 | To foreign banks | 20-150% |

Acceptances of other banks are folded into the item-2 caption in the current form; there is no separate body line for them.

---

### Item 3: Agricultural Production Loans

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCK1590 | Loans to finance agricultural production (consolidated) |
| B | BHDM1590 | Same, in domestic offices |

Operating loans for farming/ranching; seasonal working capital.

---

### Item 4: Commercial and Industrial (C&I) Loans

| Line | Column | MDRM | Description |
|------|--------|------|-------------|
| 4 (total) | B | BHDM1766 | C&I in domestic offices |
| 4.a | A | BHCK1763 | To U.S. addressees (domicile) |
| 4.b | A | BHCK1764 | To non-U.S. addressees (domicile) |
| 4.c | A | BHCKKX56 | Combined U.S. + non-U.S. (single-column reporters) |

> **Correction vs. older dictionaries**: 4.b (non-U.S. addressees) is **BHCK1764**, not a duplicate of 4.a's BHCK1763. The item-4 domestic total is **BHDM1766** (Column B). C&I loans are a leading indicator of economic activity.

---

### Item 6: Consumer Loans (Loans to Individuals)

| Line | Column | MDRM | Description | Risk Weight |
|------|--------|------|-------------|-------------|
| 6 (total) | B | BHDM1975 | In domestic offices | 75-100% |
| 6.a | A | BHCKB538 | Credit cards | 100% |
| 6.b | A | BHCKB539 | Other revolving credit plans | 100% |
| 6.c | A | BHCKK137 | Automobile loans | 75% |
| 6.d | A | BHCKK207 | Other consumer (single payment, installment, all student loans) | 100% |

> Consumer loans are **item 6** in the current form (not item 5). Auto loans receive a preferential 75% risk weight under Basel III.

---

### Item 7: Loans to Foreign Governments and Official Institutions

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCK2081 | Loans to foreign governments and official institutions (incl. foreign central banks) |
| B | BHDM2081 | Same, in domestic offices |

> **Correction vs. older dictionaries**: foreign governments is **item 7** and uses **BHCK2081 / BHDM2081**, not BHCK1296 (which is interbank-foreign, item 2.b). Risk weight is country-risk based (0% to 150%).

> **No states/political-subdivisions body line.** The current HC-C has **no** numbered body line for obligations of states and political subdivisions (the old "municipals" item). That concept survives only on the Call Report (RCON2107), not on FR Y-9C HC-C.

---

### Item 9: Nondepository Financial Institutions and Other Loans

| Line | Column | MDRM | Description |
|------|--------|------|-------------|
| 9.a | A / B | BHCKJ454 / BHDMJ454 | Loans to nondepository financial institutions |
| 9.b.(1) | A / B | BHCK1545 / BHDM1545 | Purchasing or carrying securities (incl. margin loans) |
| 9.b.(2) | A / B | BHCKJ451 / BHDMJ451 | All other loans (exclude consumer loans) |
| 9.b.(3) | A / B | BHCKKX57 / BHDMKX57 | Combined 9.b (single-column reporters) |

> This replaces the older "item 8 Other loans / 8.a margin / 8.b all other" structure. There is no standalone item 8 in the current form. New-style memo detail of 9.a appears in Memorandum 10 (below).

---

### Item 10: Lease Financing Receivables

| Line | Column | MDRM | Description |
|------|--------|------|-------------|
| 10 (total) | B | BHDM2165 | Lease financing receivables (net of unearned income), in domestic offices |
| 10.a | A | BHCKF162 | Leases to individuals (consumer leases) |
| 10.b | A | BHCKF163 | All other leases |
| 10.c | A | BHCKKX58 | Lease finance receivables (combined / single-column) |

> **Correction vs. older dictionaries**: leases are **item 10** with **F162 / F163 / KX58**, not the old item-9 F164/F165/B541 mix. Lease types include direct financing leases and leveraged leases.

---

### Item 11: LESS: Any Unearned Income on Loans

| Column | MDRM | Description |
|--------|------|-------------|
| A | BHCK2123 | Unearned income on loans (consolidated) |
| B | BHDM2123 | Same, in domestic offices |

> **Correction vs. older dictionaries**: current HC-C item 11 is **unearned income** (BHCK2123 / BHDM2123). It is **not** the allowance for loan and lease losses. The allowance (BHCT3123) is **not** an HC-C body line — it lives on **Schedule HC, item 4.c**. Unearned income is deferred loan fees/discounts recognized over loan life.

---

### Item 12: Total Loans and Leases

| Column | MDRM | Formula | Ties To |
|--------|------|---------|---------|
| A | BHCK2122 | Items 1 through 10 minus item 11 | HC items 4.a + 4.b |
| B | BHDM2122 | Same, in domestic offices | — |

> **Correction vs. older dictionaries**: item 12 is **BHCK2122 / BHDM2122** ("total loans and leases held for investment and held for sale, net of unearned income"). It is **not** BHCKB529, which is the HC item 4.d figure (loans/leases net of unearned income **and** allowance) — a different concept. Column A of item 12 must equal Schedule HC items 4.a + 4.b.

---

## Memoranda

The current HC-C memoranda are dominated by the loan-modification family (M.1, formerly "troubled debt restructurings"/TDR), plus several carve-out and disclosure memos. Each memo's column (A consolidated or B domestic-offices) is recorded in the CSV.

| Memo | Column | MDRM | Description |
|------|--------|------|-------------|
| M.1.a.(1) | B | BHDMK158 | Loan mods: 1-4 family residential construction |
| M.1.a.(2) | B | BHDMK159 | Loan mods: all other construction / land |
| M.1.b | B | BHDMF576 | Loan mods: 1-4 family residential (domestic offices) |
| M.1.c | B | BHDMK160 | Loan mods: multifamily |
| M.1.d.(1) | B | BHDMK161 | Loan mods: owner-occupied nonfarm nonresidential |
| M.1.d.(2) | B | BHDMK162 | Loan mods: other nonfarm nonresidential |
| M.1.e.(1) | A | BHCKK163 | Loan mods (C&I): U.S. addressees |
| M.1.e.(2) | A | BHCKK164 | Loan mods (C&I): non-U.S. addressees |
| M.1.e.(3) | A | BHCKKX59 | Loan mods (C&I): combined |
| M.1.f | A | BHCKK165 | Loan mods: all other loans |
| M.1.f.(1) | B | BHDMK166 | Loan mods: farmland (domestic offices) |
| M.1.f.(2) | A | BHCKK168 | Loan mods: agricultural production |
| M.1.f.(3)(a) | A | BHCKK098 | Loan mods (consumer): credit cards |
| M.1.f.(3)(b) | A | BHCKK203 | Loan mods (consumer): automobile |
| M.1.f.(3)(c) | A | BHCKK204 | Loan mods (consumer): other consumer |
| M.1.g | A | BHCKHK25 | **Total** loan modifications in compliance with modified terms |
| M.2 | A | BHCK2746 | CRE / construction / land-dev loans NOT secured by RE (in items 4 & 9) |
| M.3 | A | BHCKB837 | RE loans to non-U.S. addressees (in item 1) |
| M.4 | A | BHCKC391 | Outstanding credit-card fees and finance charges (in item 6.a) |
| M.6.a | A | BHCKF230 | Carrying amount of closed-end 1-4 family neg-am loans |
| M.6.b | A | BHCKF231 | Max remaining neg-am contractually permitted |
| M.6.c | A | BHCKF232 | Amount of neg-am included in M.6.a |
| M.9 | B | BHDMF577 | 1-4 family (domestic offices) in process of foreclosure |
| M.10.a | A / B | BHCKPV05 / BHDMPV05 | NDFI: loans to mortgage credit intermediaries |
| M.10.b | A / B | BHCKPV06 / BHDMPV06 | NDFI: loans to business credit intermediaries |
| M.10.c | A / B | BHCKPV07 / BHDMPV07 | NDFI: loans to private equity funds |
| M.10.d | A / B | BHCKPV08 / BHDMPV08 | NDFI: loans to consumer credit intermediaries |
| M.10.e | A / B | BHCKPV09 / BHDMPV09 | NDFI: other loans to nondepository financial institutions |
| M.12.a | A | BHCKG091 (+G092/G093) | PCD-acquired loans/leases secured by real estate |
| M.12.b | A | BHCKG094 (+G095/G096) | PCD-acquired C&I loans |
| M.12.c | A | BHCKG097 (+G098/G099) | PCD-acquired consumer loans |
| M.12.d | A | BHCKG100 (+G101/G102) | PCD-acquired all other loans and all leases |
| M.12.e | A | BHCKKX60 (+KX61/KX62) | PCD-acquired loans and leases (combined) |
| M.14 | A | BHCKG378 | Pledged loans and leases |
| M.15 | A | BHCKLE75 | Revolving 1-4 family HELOCs converted to closed-end status (in item 1.c.(1)) |

> **Memorandum 10 (NDFI breakout) is NEW in the March 2026 form** (codes PV05-PV09, both BHCK and BHDM). It is not yet populated in historical warehouse data (which ends 2025-12-31).
>
> **Memorandum 12** reports purchased-credit-deteriorated (PCD) / acquired loans across **three measures per row** — fair value at acquisition, gross contractual amounts receivable, and the best estimate of contractual cash flows not expected to be collected. The CSV lists each memo line (M.12.a..e) once and names all three codes in the notes (e.g., M.12.a = G091/G092/G093).

---

## Reconciliation to Schedule HC

```
SCHEDULE HC-C                                  SCHEDULE HC
═══════════════════════════════════════════════════════════════════════

Item 12, Column A (Total loans & leases) ────► HC items 4.a + 4.b
BHCK2122                                        (held for sale + held for investment)

Allowance for loan & lease losses        ────► HC item 4.c
BHCT3123 (reported on HC, NOT on HC-C)          BHCT3123

Net loans and leases                     ────► HC item 4.d
(HC-C item 12 minus the HC-4.c allowance)       BHCKB529
```

> The allowance (BHCT3123) and the net-of-allowance figure (BHCKB529) belong to **Schedule HC item 4**, not to HC-C. HC-C stops at item 12 (total net of unearned income).

---

## Ties to Other Schedules

### HC-N (Past Due and Nonaccrual)
HC-N breaks the same loan categories down by delinquency status (30-89 days past due, 90+ days and still accruing, nonaccrual). The HC-C loan-modification memoranda (M.1 family) tie to the loan-modification disclosures in HC-N.

### HC-H (Interest Sensitivity)
HC-H reports loans by repricing/maturity bucket (3 months or less, 3-12 months, 1-3 years, 3-5 years, 5-15 years, over 15 years).

### HC-R (Regulatory Capital)
HC-C loan categories map to HC-R Part II risk-weighted asset calculations; each category carries an assigned risk weight and Total RWA = Sum of (Loan Balance × Risk Weight).

---

## Risk Weight Summary

| Loan Category | Standard Risk Weight |
|---------------|---------------------|
| 1-4 family first lien (prudent) | 35-50% |
| 1-4 family junior lien | 100% |
| Multifamily | 50-100% |
| CRE (owner-occupied / other) | 100% |
| Construction (HVCRE) | 150% |
| Construction (other) | 100% |
| C&I | 100% |
| Consumer - automobile | 75% |
| Consumer - other / credit cards | 100% |
| Interbank (U.S. banks) | 20% |
| Foreign government | 0-150% (country risk) |

---

## Key Analytical Metrics

### Portfolio Composition
```
RE Concentration = Item 1 (BHCK1410) / Item 12 Column A (BHCK2122)
C&I share        = (BHCK1763 + BHCK1764) / BHCK2122
Consumer share   = Item 6 detail / BHCK2122
```

### Credit Quality
```
Coverage Ratio       = Allowance (HC 4.c, BHCT3123) / Nonperforming loans (HC-N)
Net Charge-Off Rate  = (Charge-offs - Recoveries) / Average Loans [from HI]
```

### Growth
```
Loan Growth = (Current Period - Prior Period) / Prior Period
```

---

## Historical Changes

| Date | Change |
|------|--------|
| 1981-06-30 | Core HC-C totals (BHCK1410, BHDM1766, BHCK2122, etc.) |
| 1990-09-30 | Domestic-offices (Column B) farmland/HELOC/multifamily detail |
| 1991-03-31 | Closed-end 1-4 family first/junior lien split (BHDM5367/5368) |
| 2007-03-31 | Construction sub-categories (F158/F159); nonfarm-nonres owner/other (F160/F161); consumer & other leases (F162/F163) |
| 2010-03-31 | Nondepository financial institutions & other loans (J451/J454) |
| 2018-03-31 | Total loan-modification memo (HK25) |
| 2019-12-31 | Single-column combined codes (KX56/KX57/KX58/KX59/KX60-62) |
| 2020-03-31 | CECL implementation |
| 2021-03-31 | HELOC-converted-to-closed-end memo (LE75) |
| 2026-03-31 | **NDFI breakout Memorandum 10 (PV05-PV09)** |

---

## MDRM Quick Reference

| Item | Col | MDRM | Description |
|------|-----|------|-------------|
| 1 | A | BHCK1410 | Real estate loans (total) |
| 1.b | B | BHDM1420 | Farmland |
| 1.c.(1) | B | BHDM1797 | HELOCs |
| 1.c.(2)(a) | B | BHDM5367 | 1-4 family first liens |
| 1.c.(2)(b) | B | BHDM5368 | 1-4 family junior liens |
| 1.d | B | BHDM1460 | Multifamily |
| 1.e.(1)/(2) | A | BHCKF160 / BHCKF161 | Owner-occ / other nonfarm nonresidential |
| 2 | B | BHDM1288 | Depository institutions (total) |
| 3 | A/B | BHCK1590 / BHDM1590 | Agricultural |
| 4 | B | BHDM1766 | C&I (domestic total) |
| 4.a / 4.b | A | BHCK1763 / BHCK1764 | C&I U.S. / non-U.S. addressees |
| 6 | B | BHDM1975 | Consumer (domestic total) |
| 6.a / 6.c | A | BHCKB538 / BHCKK137 | Credit cards / auto |
| 7 | A/B | BHCK2081 / BHDM2081 | Foreign governments |
| 9.a | A/B | BHCKJ454 / BHDMJ454 | Nondepository financial institutions |
| 10 | B | BHDM2165 | Leases (domestic total) |
| 10.a / 10.b | A | BHCKF162 / BHCKF163 | Consumer / other leases |
| 11 | A/B | BHCK2123 / BHDM2123 | **LESS: unearned income** |
| 12 | A/B | BHCK2122 / BHDM2122 | **TOTAL loans and leases (net of unearned income)** |

---

*Last Updated: March 2026*
*Reference: FR Y-9C Instructions and MDRM (current as of the March 2026 form)*
