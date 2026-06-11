# Schedule HC-M: Memoranda Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-M - Memoranda
**Frequency**: Quarterly (with several items collected only annually in December)
**Purpose**: Collect a heterogeneous set of memorandum items, indicators, and supporting detail referenced throughout the FR Y-9C - intangibles, other borrowed money, OREO, secured liabilities, broker-dealer balances, FR Y-12 gating questions, and more

---

## Overview

Schedule HC-M is the FR Y-9C's catch-all memoranda schedule. Unlike a balance-sheet schedule, it does not roll up to a single control total; instead it carries:

- **Supporting detail** for HC balance-sheet lines (intangible assets -> HC item 10; other borrowed money -> HC item 16; OREO -> HC item 7).
- **Yes/No indicator items** (business combinations, restatements, FR Y-10 reporting, mutual-fund sales, nonfinancial-equity-investment gating for the FR Y-12).
- **Specialized balances** (captive insurance/reinsurance subsidiaries, broker-dealer intercompany balances, secured liabilities, TARP Capital Purchase Program issuances).
- **Text items** (name/phone of the FR Y-10 verifying official; risk-disclosure URL).

### Who Files

All FR Y-9C reporters complete HC-M, but many items are conditional: item 6 (covered OREO) and several memoranda apply only to filers with $5 billion or more in assets; items 7.a/7.b (captive insurance/reinsurance) are completed annually in December; items 20-21 (broker-dealer / insurance-underwriting subsidiaries) apply only to financial holding companies; item 22 (risk-disclosure URL) applies to filers with $30 billion or more in total assets.

---

## CSV Schema

`HC_M_MEMORANDA.csv` uses the standard single-column schema:

`line_number, item_description, mdrm_code, call_mdrm, category, ties_to_hc_line, start_date, notes`

Text items (the two FR Y-10 verifying-official fields and the risk-disclosure URL) are retained as rows with their `TEXT…` MDRM codes and a `Text Item` category, so the schedule's line inventory is complete; they carry no dollar amount. Indicator items (Yes/No questions) are retained with their `BHCK…` codes and an `Indicator` category.

> **Scope note.** The official March-2026 field specification lists 44 cells for HC-M. One of those (`BHCKG450`, "Over-the-counter derivatives: fair value of collateral: equity securities - hedge funds") is an HC-L code that bleeds into the top of the HC-M block as an OCR page-header artifact; it is **not** an HC-M line item and does not appear on the HC-M form. It is therefore excluded, leaving the 43 genuine HC-M cells. This exclusion is documented in the provenance file and the verification notes below.

---

## Schedule Structure (selected)

```
MEMORANDA
├── 1.  Total number of holding company common shares outstanding (a count, not $)
├── 2-3 Debt maturing <= / > one year issued to third parties by bank subsidiaries
├── 4.  Other assets acquired in satisfaction of debts previously contracted
├── 5.  Reverse repos offset against repos on Schedule HC
├── 6.  Covered OREO protected by FDIC loss-sharing agreements
├── 7.  Captive insurance (7.a) and reinsurance (7.b) subsidiaries - total assets
├── 8-9 Indicators: business combination / restatement during the year
├── 11. Indicator: FR Y-10 reporting (+ text: verifying official name & phone)
├── 12. Intangible assets: 12.a MSAs (+ 12.a.(1) fair value), 12.b goodwill,
│        12.c other intangibles, 12.d Total (= HC item 10)
├── 13. Other real estate owned (= component of HC item 7)
├── 14. Other borrowed money: 14.a commercial paper, 14.b <=1yr, 14.c >1yr,
│        14.d Total (= HC item 16)
├── 15-16 Mutual-fund/annuity sales indicator; assets under management
├── 17-19 Nonfinancial-equity-investment FR Y-12 gating questions
├── 20. Broker-dealer subsidiaries: net assets and intercompany due-from/due-to
├── 21. Insurance/reinsurance underwriting subsidiaries - net assets
├── 22. Risk-disclosure URL (text item)
├── 23. Secured liabilities (23.a secured fed funds; 23.b secured other borrowings)
└── 24. TARP Capital Purchase Program: 24.a senior preferred; 24.b warrants
```

(Item 10 is "Not applicable" on the current form and carries no code.)

---

## Detailed Line Items (highlights)

### Item 12 - Intangible assets (ties to HC item 10)

| Line | MDRM | Description |
|------|------|-------------|
| 12.a | BHCK3164 | Mortgage servicing assets |
| 12.a.(1) | BHCK6438 | Estimated fair value of mortgage servicing assets (memo) |
| 12.b | BHCK3163 | Goodwill |
| 12.c | BHCKJF76 | All other intangible assets |
| 12.d | BHCT2143 | Total intangible assets (= Schedule HC item 10) |

```
HC-M item 12.d (BHCT2143)  =  12.a + 12.b + 12.c  =  Schedule HC item 10
                              (Goodwill 10.a + Other intangible assets 10.b)
```

### Item 14 - Other borrowed money (ties to HC item 16)

| Line | MDRM | Description |
|------|------|-------------|
| 14.a | BHCK2309 | Commercial paper |
| 14.b | BHCK2332 | Other borrowed money, remaining maturity <= 1 year |
| 14.c | BHCK2333 | Other borrowed money, remaining maturity > 1 year |
| 14.d | BHCT3190 | Total other borrowed money (= Schedule HC item 16) |

### Item 13 - Other real estate owned

| Line | MDRM | Description | Ties To |
|------|------|-------------|---------|
| 13 | BHCT2150 | Other real estate owned | Component of HC item 7 |

### Captive insurance/reinsurance (item 7) and broker-dealer (item 20)

| Line | MDRM | Description |
|------|------|-------------|
| 7.a | BHCKK193 | Total assets of captive insurance subsidiaries (December only) |
| 7.b | BHCKK194 | Total assets of captive reinsurance subsidiaries (December only) |
| 20.a | BHCKC252 | Broker-dealer subsidiaries - net assets |
| 20.b.(1)-(3) | BHCK4832/4833/4834 | Due from parent / subsidiary banks / nonbank subsidiaries |
| 20.c.(1)-(3) | BHCK5041/5043/5045 | Due to parent / subsidiary banks / nonbank subsidiaries |
| 20.d | BHCK5047 | Intercompany liabilities qualifying as subordinated |

### Secured liabilities (item 23) and TARP CPP (item 24)

| Line | MDRM | Description | Ties To |
|------|------|-------------|---------|
| 23.a | BHCKF064 | Secured "Federal funds purchased in domestic offices" | Portion of HC item 14.a |
| 23.b | BHCKF065 | Secured "Other borrowings" | Portion of HC-M item 14.d |
| 24.a | BHCKG234 | Senior perpetual preferred stock or similar (CPP) | - |
| 24.b | BHCKG235 | Warrants to purchase common stock or similar (CPP) | - |

See the CSV for the complete 43-line inventory, including indicator and text items.

---

## Reconciliation / Ties

```
HC-M 12.d (BHCT2143)  =  HC item 10  (intangible assets)
HC-M 14.d (BHCT3190)  =  HC item 16  (other borrowed money)
HC-M 13   (BHCT2150)  ⊂  HC item 7   (premises/OREO; OREO component)
HC-M 23.a (BHCKF064)  ⊂  HC item 14.a (secured portion of fed funds purchased)
HC-M 23.b (BHCKF065)  ⊂  HC-M item 14.d (secured portion of other borrowings)
```

The "reciprocal / brokered deposit" style intercompany detail in item 20 (due-from / due-to related institutions) and the FHLB-relevant other-borrowed-money lines in item 14 are the schedule's principal funding-structure disclosures.

---

## Pitfalls

- **`BHCKG450` is not an HC-M item.** It is an HC-L derivatives-collateral code that appears as an OCR header artifact at the top of the HC-M field-spec block; it is excluded here (see Scope note).
- **Mixed item kinds.** HC-M mixes dollar amounts, integer counts (item 1, common shares - reported unrounded, not in thousands), Yes/No indicators (items 8, 9, 11, 15, 17, 18, 19.a, 19.b), and text fields (item 11 official name/phone, item 22 URL). Treating an indicator code as a dollar amount will corrupt any aggregation.
- **Conditional and annual items.** Several items are blank for most filers by design (item 6 and various memoranda for < $5B filers; items 7.a/7.b only in December; items 20-21 only for financial holding companies; item 22 only for $30B+ filers). A blank is a valid filing.
- **Item numbering has gaps.** Item 10 is "Not applicable"; the form jumps from 9 to 11. Do not infer a missing item 10 row.
- **Total cells use the `BHCT` prefix.** Items 12.d, 13, and 14.d use `BHCT…` total codes; the component lines use `BHCK…`. The total prefix signals a Federal Reserve-computed/edited control cell.

---

## Verification & Provenance

- **MDRM:** all 43 HC-M line codes joined to the Federal Reserve MDRM codeset; 43 of 43 verified present (the 44th field-spec cell, `BHCKG450`, is the excluded HC-L artifact).
- **Warehouse evidence:** all 43 codes are observed in the Federal Reserve bulk BHCF data (1986-2025); the `TEXT…` items are non-numeric and (as expected) carry no value series in the bulk numeric data.
- **Provenance file:** `_rebuild/schedules/PROVENANCE_HC_M.csv`.
- **Sources:** Federal Reserve MDRM; FR Y-9C form and instructions (March 2026); Federal Reserve bulk BHCF data (1986-2025).

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C form and instructions (March 2026); Federal Reserve MDRM; Federal Reserve bulk BHCF data (1986-2025)*
