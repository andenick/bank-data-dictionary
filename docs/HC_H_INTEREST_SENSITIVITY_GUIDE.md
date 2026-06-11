# Schedule HC-H: Interest Sensitivity Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-H - Interest Sensitivity
**Frequency**: Quarterly
**Purpose**: Report selected balance-sheet amounts that reprice or mature within one year, to give a partial view of interest-rate sensitivity

---

## Overview

Schedule HC-H collects a small set of **selected** balance-sheet amounts that reprice or mature within one year. It is a deliberately narrow disclosure: the schedule does **not** provide, nor is it intended to provide, a comprehensive view of the holding company's interest-rate sensitivity position. It is a current schedule that has been on the FR Y-9C since the June 30, 1986 report date and is observed continuously in the Federal Reserve bulk BHCF data from 1986 through 2021.

### What the Schedule Reports

Each line item is a **single dollar amount** (one column, "Amount"). There is no maturity-bucket grid: HC-H asks only for the portion of each selected category that reprices or matures **within one year**.

Amounts are reported:
- By **remaining maturity** for fixed or predetermined-rate instruments
- By **repricing frequency** for floating or adjustable-rate instruments

A holding company may, at its option and applied consistently, report floating-rate transactions by earliest repricing opportunity, and multipayment transactions on the basis of scheduled contractual payments.

> **Revision note (v7.0).** Earlier editions of this dictionary described Schedule HC-H as a 14-row by 7-maturity-bucket repricing grid with a large block of `A`- and `C`-series MDRM codes. That grid could not be verified against the Federal Reserve Micro Data Reference Manual (MDRM) or against reported FR Y-9C data and has been removed. Version 7.0 replaces it with the five MDRM-verified single-column items that the FR Y-9C form actually contains. HC-H is a **current** schedule — it is not discontinued.

---

## Who Files

All holding companies that file the FR Y-9C complete Schedule HC-H. The information must be consolidated on the same basis as the rest of the Consolidated Financial Statements for Holding Companies.

**Foreign-office exclusion option.** Holding companies with foreign subsidiaries (or subsidiaries with more than one foreign office) may exclude the smallest of such non-U.S. offices, provided the excluded offices' assets do not exceed 50% of the company's total foreign-country office assets and do not exceed 10% of total consolidated assets as of the report date. "Shell" branches, offices in Puerto Rico and U.S. territories, domestic offices of Edge and Agreement subsidiaries, and IBFs are excluded when making this determination.

---

## Line Items and MDRM Codes

Schedule HC-H has five single-column items. Each reports an "Amount."

| Item | Description | MDRM | Ties To (Schedule HC) |
|------|-------------|------|------------------------|
| 1 | Earning assets that are repriceable within one year or mature within one year | BHCK3197 | — |
| 2 | Interest-bearing deposit liabilities that reprice within one year or mature within one year | BHCK3296 | Items 13.a.(2), 13.b.(2) |
| 3 | Long-term debt that reprices within one year | BHCK3298 | Items 16, 19.a |
| 4 | Variable-rate preferred stock | BHCK3408 | — |
| 5 | Long-term debt scheduled to mature within one year | BHCK3409 | Item 19.a |

### Item Detail

**Item 1 — Earning assets repriceable/maturing within one year (BHCK3197).** All assets the consolidated holding company considers earning assets that have a remaining maturity of less than one year, or a repricing frequency of less than one year. Earning assets generally include interest-bearing balances due from depository institutions, securities, federal funds sold and securities purchased under agreements to resell, and loans and leases. Nonaccrual assets, trading-account assets, and equity securities are excluded.

**Item 2 — Interest-bearing deposit liabilities repricing/maturing within one year (BHCK3296).** Interest-bearing deposit liabilities with a remaining maturity or repricing frequency of less than one year. These amounts are a subset of the interest-bearing deposits reported in Schedule HC, items 13.a.(2) and 13.b.(2).

**Item 3 — Long-term debt repricing within one year (BHCK3298).** The portion of long-term debt (included in Schedule HC, items 16 and 19.a) whose interest rate reprices within one year.

**Item 4 — Variable-rate preferred stock (BHCK3408).** Includes both limited-life and perpetual preferred stock carrying a variable dividend rate.

**Item 5 — Long-term debt scheduled to mature within one year (BHCK3409).** The portion of long-term debt reported in Schedule HC, item 19.a that is scheduled to mature within one year.

---

## Key Definitions

- **Fixed interest rate** — specified at origination, invariable over the term, known to both parties.
- **Predetermined interest rate** — changes on a predetermined schedule, with the exact rate over the life of the instrument known with certainty when acquired.
- **Floating / adjustable interest rate** — varies relative to an index, another rate, or other criterion whose value cannot be known in advance. When such a rate hits a floor or ceiling and can no longer float, the instrument is treated as fixed-rate until it is again free to float.
- **Remaining maturity** — time from the report date to final contractual maturity, without regard to repayment schedule.
- **Repricing frequency** — how often the contract permits the rate to change, without regard to the time from the report date to the next change.

---

## Relationships and Tie-Outs

HC-H items are **selected subsets** of balance-sheet amounts, not totals, so they tie back to Schedule HC line items only as partial components:

```
HC-H Item 2 (BHCK3296)  ⊆  HC Items 13.a.(2) + 13.b.(2)  (interest-bearing deposits)
HC-H Item 3 (BHCK3298)  ⊆  HC Items 16 + 19.a            (long-term / other borrowed + subordinated debt)
HC-H Item 5 (BHCK3409)  ⊆  HC Item 19.a                  (subordinated notes and debentures)
```

Because the schedule reports only the within-one-year portion of each category, an HC-H item should never exceed the corresponding Schedule HC balance.

For analytical repricing-gap work, note that HC-H supports only a coarse one-year gap measure: Item 1 (assets repricing/maturing within one year) versus Items 2 + 3 + 5 (liabilities repricing/maturing within one year). It is not a full bucketed gap report.

---

## Historical Notes

| Date | Note |
|------|------|
| 1981-06-30 | MDRM start date for BHCK3409 (long-term debt maturing within one year) |
| 1986-06-30 | Schedule HC-H added to the FR Y-9C; items 1-4 begin (BHCK3197, 3296, 3298, 3408) |
| 1986-09 → 2021-03 | All five items observed continuously in Federal Reserve bulk BHCF data |

All five codes remain open (no end date) in the MDRM and are still collected on the current form.

---

## Common Pitfalls

- **Treating HC-H as a maturity-bucket grid.** It is not. There are five single-amount items measuring only the within-one-year portion of each category. Any prior reference to 3-month / 3-12-month / 1-3-year / etc. buckets for HC-H is incorrect.
- **Summing HC-H items into a balance-sheet total.** HC-H items are selected subsets, not exhaustive totals; they do not add up to total assets or total liabilities.
- **Including nonaccrual, trading, or equity positions in Item 1.** These are explicitly excluded from earning assets for this schedule.
- **Mixing the optional reporting conventions.** The earliest-repricing-opportunity and scheduled-contractual-payment options must each be applied consistently to every transaction reported on the schedule.

---

## Verification and Provenance

Every MDRM code in this guide was verified against the Federal Reserve Micro Data Reference Manual (MDRM) snapshot downloaded 2026-06-11 and was observed as a reported column in actual FR Y-9C data. The five HC-H codes (BHCK3197, BHCK3296, BHCK3298, BHCK3408, BHCK3409) appear continuously in Federal Reserve bulk BHCF data from 1986 through 2021.

**Sources:**
- MDRM (Federal Reserve Micro Data Reference Manual)
- FR Y-9C form and instructions

---

*Last Updated: 2026-06-11 (v7.0 — MDRM-verified rebuild)*
*Reference: FR Y-9C form and instructions; MDRM*
