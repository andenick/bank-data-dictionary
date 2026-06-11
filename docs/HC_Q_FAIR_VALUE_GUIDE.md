# Schedule HC-Q: Fair Value Measurements Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-Q - Financial Assets and Liabilities Measured at Fair Value on a Recurring Basis
**Frequency**: Quarterly
**Purpose**: Disclose the fair value of assets and liabilities measured at fair value, split across the fair value hierarchy (Levels 1, 2, 3)

---

## Overview

Schedule HC-Q discloses, for assets and liabilities measured at fair value on a recurring basis, the total fair value reported on the balance sheet (Schedule HC) and its decomposition across the fair value hierarchy. The disclosure implements ASC 820 (Fair Value Measurement). The current five-column layout has been in effect since the **June 30, 2009** report date (the "G-series" codes), with several lines carrying older 2007-2008 "F-series" codes and a few 2018 "HT-series" codes for items added later.

### Fair Value Hierarchy

| Level | Inputs | Examples |
|-------|--------|----------|
| **Level 1** | Quoted prices in active markets for identical assets/liabilities | Exchange-traded equities and listed derivatives |
| **Level 2** | Observable inputs other than Level 1 quoted prices | OTC derivatives, structured products with observable inputs |
| **Level 3** | Significant unobservable (model-based) inputs | Illiquid securities, complex/distressed positions |

---

## Who Files

Schedule HC-Q is reported by holding companies with **total assets of $5 billion or more**, and by holding companies of any size that have elected the fair value option (FVO) or have trading activity that puts assets or liabilities into recurring fair value measurement. Holding companies not required to report Schedule HC-D or Schedule HC-Q may leave these schedules blank.

---

## Column Structure

HC-Q uses a **five-column grid** for the main asset and liability rows (items 1-14):

| Column | Label | Meaning |
|--------|-------|---------|
| A | Total fair value | Total fair value **as reported on Schedule HC** for the item |
| B | Netting | Amounts netted in determining total fair value (FIN 39 / FIN 41 counterparty and collateral netting) |
| C | Level 1 | Level 1 fair value measurements |
| D | Level 2 | Level 2 fair value measurements |
| E | Level 3 | Level 3 fair value measurements |

**Column reconciliation (per row):**
```
Column A = Column C + Column D + Column E − Column B
(Total FV reported on HC = Level 1 + Level 2 + Level 3 − netting)
```

The fair-value-option loan memoranda (M.3 and M.4) are single-column (total fair value / unpaid principal balance only).

---

## Asset Line Items (Items 1-7)

| Item | Description | Col A (Total FV) | Col B (Netting) | Col C (L1) | Col D (L2) | Col E (L3) |
|------|-------------|------------------|-----------------|------------|------------|------------|
| 1 | Available-for-sale debt and equity securities with readily determinable FV not held for trading | **BHCYJA36** | BHCKG474 | BHCKG475 | BHCKG476 | BHCKG477 |
| 2 | Federal funds sold and securities purchased under agreements to resell | BHCKG478 | BHCKG479 | BHCKG480 | BHCKG481 | BHCKG482 |
| 3 | Loans and leases held for sale | BHCKG483 | BHCKG484 | BHCKG485 | BHCKG486 | BHCKG487 |
| 4 | Loans and leases held for investment | BHCKG488 | BHCKG489 | BHCKG490 | BHCKG491 | BHCKG492 |
| 5.a | Trading assets: Derivative assets | **BHCT3543** | BHCKG493 | BHCKG494 | BHCKG495 | BHCKG496 |
| 5.b | Trading assets: Other trading assets | BHCKG497 | BHCKG498 | BHCKG499 | BHCKG500 | BHCKG501 |
| 5.b.(1) | Nontrading securities at fair value with changes in FV reported in current earnings | BHCKF240 | BHCKF684 | BHCKF692 | BHCKF241 | BHCKF242 |
| 6 | All other assets | BHCKG391 | BHCKG392 | BHCKG395 | BHCKG396 | BHCKG804 |
| 7 | **Total assets measured at fair value on a recurring basis** | BHCKG502 | BHCKG503 | BHCKG504 | BHCKG505 | BHCKG506 |

**Item 1 column A — special code (BHCYJA36).** The column-A total for AFS securities uses the `BHCY`-prefix code **BHCYJA36**, effective **2018-03-31** with the ASU 2016-01 revision (which moved certain equity securities to fair value through earnings). Columns B-E remain on the 2009 G-series codes. A series spanning the 2018 break therefore changes column-A code at that date even though the line item is continuous.

**Item 5.b.(1)** is a memorandum-style sub-item of 5.b that carries 2007-2008 F-series codes.

**Item 7 is a per-column total:** for each of columns A-E, item 7 = sum of items 1 through 6.

---

## Liability Line Items (Items 8-14)

| Item | Description | Col A (Total FV) | Col B (Netting) | Col C (L1) | Col D (L2) | Col E (L3) |
|------|-------------|------------------|-----------------|------------|------------|------------|
| 8 | Deposits | **BHCKF252** | BHCKF686 | BHCKF694 | BHCKF253 | BHCKF254 |
| 9 | Federal funds purchased and securities sold under agreements to repurchase | BHCKG507 | BHCKG508 | BHCKG509 | BHCKG510 | BHCKG511 |
| 10.a | Trading liabilities: Derivative liabilities | **BHCT3547** | BHCKG512 | BHCKG513 | BHCKG514 | BHCKG515 |
| 10.b | Trading liabilities: Other trading liabilities | BHCKG516 | BHCKG517 | BHCKG518 | BHCKG519 | BHCKG520 |
| 11 | Other borrowed money | BHCKG521 | BHCKG522 | BHCKG523 | BHCKG524 | BHCKG525 |
| 12 | Subordinated notes and debentures | BHCKG526 | BHCKG527 | BHCKG528 | BHCKG529 | BHCKG530 |
| 13 | All other liabilities | BHCKG805 | BHCKG806 | BHCKG807 | BHCKG808 | BHCKG809 |
| 14 | **Total liabilities measured at fair value on a recurring basis** | BHCKG531 | BHCKG532 | BHCKG533 | BHCKG534 | BHCKG535 |

**Item 8 (Deposits)** uses 2007-vintage F-series codes (column A BHCKF252 effective 2007-03-31; netting/Level 1 effective 2008).

**Item 14 is a per-column total:** for each of columns A-E, item 14 = sum of items 8 through 13.

---

## Code-Reuse Note: BHCT3543 and BHCT3547 (explicit, by design)

Items **5.a** (column A, derivative assets) and **10.a** (column A, derivative liabilities) reuse two codes whose MDRM **item names** read as Schedule HC-D revaluation lines:

| Code | MDRM item name (as registered) | HC-Q use |
|------|--------------------------------|----------|
| BHCT3543 | "Revaluation gains on interest rate, foreign exchange rate, and other commodity and equity contracts" | Total fair value of **trading derivative assets** (HC-Q item 5.a, column A) |
| BHCT3547 | "Revaluation losses on interest rate, foreign exchange rate, and other commodity and equity contracts" | Total fair value of **trading derivative liabilities** (HC-Q item 10.a, column A) |

This is intentional reuse, not an error. The trading-derivative total fair value reported in HC-Q column A is the same quantity the Federal Reserve collects for the HC-D revaluation-gains/losses line, so HC-Q points at the existing `BHCT3543` / `BHCT3547` codes rather than minting new column-A codes for these two rows. The corresponding netting and Level 1/2/3 columns (B-E) use HC-Q's own G-series codes (BHCKG493-G496 for 5.a; BHCKG512-G515 for 10.a). **An automated MDRM-name audit will appear to flag these two cells as "HC-D" descriptions — this is expected and correct.**

---

## Memoranda Items

### M.1 — "All other assets" detail (item 6 itemization, 5-column)

Itemize and describe amounts in item 6 that exceed $100,000 and exceed 25% of item 6.

| Item | Description | Col A | Col B | Col C | Col D | Col E |
|------|-------------|-------|-------|-------|-------|-------|
| M.1.a | Mortgage servicing assets | BHCKG536 | BHCKG537 | BHCKG538 | BHCKG539 | BHCKG540 |
| M.1.b | Nontrading derivative assets | BHCKG541 | BHCKG542 | BHCKG543 | BHCKG544 | BHCKG545 |
| M.1.c | Itemized component (text code BHTXG546) | BHCKG546 | BHCKG547 | BHCKG548 | BHCKG549 | BHCKG550 |
| M.1.d | Itemized component (text code BHTXG551) | BHCKG551 | BHCKG552 | BHCKG553 | BHCKG554 | BHCKG555 |
| M.1.e | Itemized component (text code BHTXG556) | BHCKG556 | BHCKG557 | BHCKG558 | BHCKG559 | BHCKG560 |
| M.1.f | Itemized component (text code BHTXG561) | BHCKG561 | BHCKG562 | BHCKG563 | BHCKG564 | BHCKG565 |

### M.2 — "All other liabilities" detail (item 13 itemization, 5-column)

Itemize and describe amounts in item 13 that exceed $100,000 and exceed 25% of item 13.

| Item | Description | Col A | Col B | Col C | Col D | Col E |
|------|-------------|-------|-------|-------|-------|-------|
| M.2.a | Loan commitments (not accounted for as derivatives) | BHCKF261 | BHCKF689 | BHCKF697 | BHCKF262 | BHCKF263 |
| M.2.b | Nontrading derivative liabilities | BHCKG566 | BHCKG567 | BHCKG568 | BHCKG569 | BHCKG570 |
| M.2.c | Itemized component (text code BHTXG571) | BHCKG571 | BHCKG572 | BHCKG573 | BHCKG574 | BHCKG575 |
| M.2.d | Itemized component (text code BHTXG576) | BHCKG576 | BHCKG577 | BHCKG578 | BHCKG579 | BHCKG580 |
| M.2.e | Itemized component (text code BHTXG581) | BHCKG581 | BHCKG582 | BHCKG583 | BHCKG584 | BHCKG585 |
| M.2.f | Itemized component (text code BHTXG586) | BHCKG586 | BHCKG587 | BHCKG588 | BHCKG589 | BHCKG590 |

M.2.a (loan commitments) carries 2007-2008 F-series codes.

### M.3 — Loans measured at fair value (single column, total fair value)

| Item | Description | MDRM | Start |
|------|-------------|------|-------|
| M.3.a.(1) | Secured by 1-4 family residential properties | BHCKHT87 | 2018-03-31 |
| M.3.a.(2) | All other loans secured by real estate | BHCKHT88 | 2018-03-31 |
| M.3.b | Commercial and industrial loans | BHCKF585 | 2008-03-31 |
| M.3.c | Consumer loans (includes purchased paper) | BHCKHT89 | 2018-03-31 |
| M.3.d | Other loans | BHCKF589 | 2008-03-31 |

### M.4 — Unpaid principal balance of loans at fair value (single column)

| Item | Description | MDRM | Start |
|------|-------------|------|-------|
| M.4.a.(1) | UPB: Secured by 1-4 family residential properties | BHCKHT91 | 2018-03-31 |
| M.4.a.(2) | UPB: All other loans secured by real estate | BHCKHT92 | 2018-03-31 |
| M.4.b | UPB: Commercial and industrial loans | BHCKF597 | 2008-03-31 |
| M.4.c | UPB: Consumer loans | BHCKHT93 | 2018-03-31 |
| M.4.d | UPB: Other loans | BHCKF601 | 2008-03-31 |

**Vintage-mix note.** M.3 and M.4 mix **2008 F-series** codes (C&I and "other" loans: BHCKF585/F589/F597/F601) with **2018 HT-series** codes (the real-estate and consumer breakouts added in 2018: BHCKHT87/88/89/91/92/93). The two real-estate sub-rows and the consumer row were added to the form in 2018; the C&I and "other" rows are the older 2008 lines.

---

## Relationships and Tie-Outs

```
Per-row hierarchy:   A = C + D + E − B           (each item, columns A-E)
Asset total:         Item 7  = Σ items 1-6        (each column)
Liability total:     Item 14 = Σ items 8-13       (each column)
```

Cross-schedule ties (column A, total fair value reported on Schedule HC):

```
HC-Q item 1  (BHCYJA36)  ←→  HC items 2.b / 2.c   (AFS securities)
HC-Q item 2  (BHCKG478)  ←→  HC item 3            (fed funds sold / reverse repos)
HC-Q item 3  (BHCKG483)  ←→  HC item 4.a          (loans held for sale)
HC-Q item 4  (BHCKG488)  ←→  HC item 4.b          (FVO loans held for investment)
HC-Q item 5  (5.a + 5.b) ←→  HC item 5 / HC-D     (trading assets)
HC-Q item 8  (BHCKF252)  ←→  HC item 13           (deposits)
HC-Q item 9  (BHCKG507)  ←→  HC item 14           (fed funds purchased / repos)
HC-Q item 10 (10.a+10.b) ←→  HC item 15 / HC-D    (trading liabilities)
HC-Q item 11 (BHCKG521)  ←→  HC item 16           (other borrowed money)
HC-Q item 12 (BHCKG526)  ←→  HC item 19.a         (subordinated notes and debentures)
```

The derivative-assets total (item 5.a, BHCT3543) and derivative-liabilities total (item 10.a, BHCT3547) also reconcile to the HC-D derivative revaluation lines, consistent with the code-reuse note above. For HC-D filers, the trading-liability fair value (HC-D item 15, column carried into HC-Q item 5/10) is subject to the Fed cross-schedule edit requiring agreement with HC-Q item 5/10 column A.

---

## Level 3 Analysis

```
Level 3 share = Column E / Column A
- Low (< 5%): liquid, transparent portfolio
- Moderate (5-15%): some illiquid holdings
- High (> 15%): significant model-dependent valuations
```

Level 3 positions rely on significant unobservable inputs and internal models, draw enhanced disclosure, and are the focus of regulatory scrutiny — especially growth trends and transfers from Level 2 into Level 3 during market stress.

---

## Historical Notes

| Date | Change |
|------|--------|
| 2007-03-31 | Earliest F-series fair-value codes appear (deposits, FVO loans, loan commitments) |
| 2008-03-31 | Additional F-series netting / Level-1 codes; C&I and "other" FVO-loan memoranda |
| 2009-06-30 | Current five-column HC-Q layout effective; G-series codes for items 1-14 (columns B-E and most column A) |
| 2018-03-31 | ASU 2016-01: item 1 column A becomes BHCYJA36; HT-series real-estate/consumer FVO-loan memoranda (M.3/M.4) added |

---

## Common Pitfalls

- **Mis-stating the column reconciliation.** Column A (total FV on HC) = C + D + E **minus** B (netting). The netting column is subtracted, not added.
- **Flagging BHCT3543 / BHCT3547 as wrong-schedule codes.** Their MDRM names read as HC-D revaluation lines, but HC-Q reuses them by design for the derivative-asset (5.a) and derivative-liability (10.a) column-A totals.
- **Assuming one code era for item 1 column A.** It switches to BHCYJA36 at 2018-03-31 (ASU 2016-01); earlier periods use the original 2009 layout.
- **Treating M.3/M.4 as a single code vintage.** They mix 2008 F-series (C&I, other) and 2018 HT-series (real estate, consumer) codes.
- **Forgetting the totals are per-column.** Item 7 sums items 1-6 and item 14 sums items 8-13, separately for each of columns A-E.

> **Revision note (v7.0).** Earlier editions of this dictionary carried an unverifiable HC-Q code grid built on a four-column layout (total / L1 / L2 / L3) and a long block of `BHCL` F-series codes that do not appear in the MDRM or in reported FR Y-9C data. Version 7.0 replaces that grid with the MDRM-verified five-column layout (total FV / netting / Level 1 / Level 2 / Level 3) and the G/F/HT-series codes the form actually uses.

---

## Verification and Provenance

Every MDRM code in this guide was verified against the Federal Reserve Micro Data Reference Manual (MDRM) snapshot downloaded 2026-06-11 and was observed as a reported column in actual FR Y-9C data. The HC-Q codes appear in Federal Reserve bulk BHCF data over their respective reporting windows (2009-2021 for the G-series five-column layout; 2007-2021 for the F-series deposit/FVO lines; 2018-2021 for the BHCYJA36 and HT-series additions).

**Sources:**
- MDRM (Federal Reserve Micro Data Reference Manual)
- FR Y-9C form and instructions

---

*Last Updated: 2026-06-11 (v7.0 — MDRM-verified rebuild)*
*Reference: FR Y-9C form and instructions; MDRM*
