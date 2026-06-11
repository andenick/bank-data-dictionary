# Empirical Validation

> **Version 8.0 | 2026-06-11** — every machine-testable relationship in this dictionary was
> tested against **208 million rows of real FR Y-9C filings**.

Most data dictionaries assert that "assets equal liabilities plus equity" and stop there. This
one tests it. Every reconciliation identity and bound we publish for the FR Y-9C is checked, as
an actual SQL aggregate, against the full history of bank holding company filings — and we
publish the pass rate, the observation count, and an honest verdict for each.

---

## What was done

1. **Build a complete relationship registry.** The official Federal Reserve FR Y-9C **edit
   checklist** (2,195 current edit checks from the published reporting instructions) was parsed
   and structured, then merged with the dictionary's own curated identities and component
   hierarchies into a single [Relationship Registry](data/relationship_registry.md) of
   **2,330 relationships**. Each row carries its machine-readable expression, its source
   (official edit id and/or curated rule), a severity, and a testability flag.

2. **Test every testable relationship against real filings.** Every relationship that resolves
   to FR Y-9C codes present in the bulk data — **332 relationships after adjudication** — was
   evaluated as an aggregate query over **Federal Reserve bulk BHCF (FR Y-9C) data**: every
   quarterly filing from **1986 Q3 through 2025 Q4**, **13,668 distinct holding companies**,
   **~208 million reported cell-values**. A relationship "passes" for a filing when the two
   sides agree within a tolerance of **max($1,000, 0.1%)** of the larger side — enough to absorb
   thousands-rounding in the filings without masking real breaks.

3. **Adjudicate every non-passing result.** Each relationship that did not pass cleanly was
   investigated against the official edit text, the FR Y-9C field specification, and the MDRM —
   not silently dropped. That review caught a systematic bug in our own test harness (it
   mis-parsed `A − (B + C)` as `A + B + C`), several mis-stated curated edges, and a handful of
   genuinely invalid bounds, all documented and corrected. The result is a registry in which
   every tested row has a defended verdict and **zero** rows are left in an unexplained
   "rejected" state.

**Sources.** All testing uses the **Federal Reserve bulk BHCF data (1986–2025)**, the
**FR Y-9C Reporting Central field specifications (March 2026)**, and the **official FR Y-9C edit
checklist (current reporting instructions)**. No private or derived data is involved.

---

## The verdict taxonomy

| Verdict | Meaning |
|---------|---------|
| **CONFIRMED** | Holds in ≥99% of all observed filings across the full 1986–2025 window. A structural identity of the form. |
| **CONFIRMED_CURRENT** | Holds in ≥99% of filings in the current reporting regime (2021+); older vintages differ because the form line-up was renumbered or split. The identity is correct for today's form. |
| **QUALITY_TOLERANCE** | A Fed "should"-edit or a valid economic bound with a small, explained tail (e.g. minority-interest or netting nuance). We publish the actual rate rather than rounding it to "100%". |
| **NOT_IN_BULK** | One side uses a code that was discontinued or renumbered, so the two sides never co-occur in the bulk data. Documented, not testable. |
| **CONDITIONAL_DOC** | Applies only to a sub-population (e.g. advanced-approaches banks exiting parallel run), so it is not a cross-sectional identity. Verified by documentation. |
| **DATA_GAP** | A genuine identity whose component splits are too sparsely populated in the bulk data to test as an all-plus sum. |

---

## Results

| Verdict | Count |
|---------|------:|
| **CONFIRMED** (≥99%, full history) | **264** |
| **CONFIRMED_CURRENT** (≥99%, 2021+) | **34** |
| **QUALITY_TOLERANCE** (documented rate) | **13** |
| **NOT_IN_BULK** (discontinued/renumbered code) | **17** |
| **CONDITIONAL_DOC** (sub-population only) | **3** |
| **DATA_GAP** (component splits too sparse) | **1** |
| **Total tested** | **332** |

**298 of the 332 machine-testable relationships are confirmed at ≥99%** (264 across the full
38-year history, plus 34 more for the current form). The remaining 34 are each individually
explained: 13 are valid bounds with a small documented tail, 20 reference discontinued codes or
sub-populations, and 1 is a real identity the bulk data is too sparse to test.

---

## Showcase: confirmed identities

A selection of the tested relationships, with their real pass rates and observation counts.
Pass rate is the share of filings in which the identity held within tolerance.

| Relationship | What it checks | Observations | Pass rate | Verdict |
|---|---|---:|---:|---|
| `BHCK3300 = BHCK2170` | Total liabilities + equity equals total assets (the balance-sheet identity, stated as the form's own item 29 = item 12) | 187,845 | **100.00%** | CONFIRMED |
| `BHCK4107 − BHCK4073 = BHCK4074` | Net interest income = total interest income − total interest expense | 187,842 | **100.00%** | CONFIRMED |
| `BHCKB528 − BHCK3123 = BHCKB529` | Net loans = loans held for investment − allowance for credit losses | 100,102 | **100.00%** | CONFIRMED |
| `BHCK3049 + BHCKB557 + BHCKB984 = BHCT2750` | Schedule HC-G other liabilities tie out to the balance-sheet total | 55,737 | **100.00%** | CONFIRMED |
| `BHCT2750 = BHCK2750` | Consolidated/total mnemonic tie for other liabilities (HC-G ↔ HC) | 55,737 | **100.00%** | CONFIRMED |
| `BHCT4340 = BHCK4340` | Net income ties across the two consolidated mnemonics | 55,737 | **100.00%** | CONFIRMED |
| `BHCT1773 = BHCK1773` | Available-for-sale securities tie (HC-B ↔ HC) | 55,766 | **100.00%** | CONFIRMED |
| HI-A equity roll-forward `(prior equity + net income + … ) = end-of-period equity` | The full Schedule HI-A changes-in-equity build-up | 55,766 | **99.95%** | CONFIRMED |
| `BHCK2170 = BHCK2948 + BHCK3210` | Assets = liabilities + holding-company equity (the textbook A = L + E) | 187,845 | **92.60%** | QUALITY_TOLERANCE |

The last row is instructive. The textbook accounting identity *Assets = Liabilities + Equity*
holds exactly only when minority (noncontrolling) interest is handled correctly: on the FR Y-9C,
**item 29** (`BHCK3300`, total liabilities **and** equity) is the line that ties to total assets
at **100.00%**, while the bare "liabilities + holding-company equity" form
(`BHCK2948 + BHCK3210`) omits the noncontrolling-interest component and therefore holds in 92.6%
of filings. We publish the 92.6% honestly rather than presenting the textbook form as exact.

---

## Limitations (read these)

This validation is rigorous **within its scope**, and that scope has edges worth stating plainly.

- **FR Y-9C only.** The empirical tests run against the bulk **FR Y-9C** filings. The dictionary
  documents Call Report (FFIEC 031/041/051) identities too, but those are validated by the
  data provider's own **cross-form code concordance** (Y-9C `BHCK`/`BHCT` ↔ Call `RCFD`), not by
  a second independent test against bulk Call data. A Y-9C identity that is confirmed implies its
  Call Report twin under that concordance; it is not separately re-measured here.

- **"Should" edits are not "must" edits.** The 13 **QUALITY_TOLERANCE** relationships are valid
  economic bounds or Federal Reserve "should"-class edits — relationships the Fed flags for
  review but does not reject a filing over. Their published pass rates (0.85–0.98) are real and
  the small tails are explained (minority interest, derivative netting, foreign-office residual,
  timing of allowance vs. balance), not data errors.

- **One documented DATA_GAP.** A single genuine identity (an HC-P mortgage-banking split) cannot
  be tested as an all-plus sum because its sub-components are reported too sparsely — missing
  values read as zero and break the sum. It is flagged, not asserted as confirmed.

- **Discontinued and sub-population relationships are not "tested away".** The 17 **NOT_IN_BULK**
  rows reference codes that were renumbered or retired across the 38-year window, so the two
  sides never co-occur; the 3 **CONDITIONAL_DOC** rows apply only to advanced-approaches banks.
  Both are documented as such rather than dropped or force-fit.

- **Vintage matters.** The 34 **CONFIRMED_CURRENT** relationships hold for today's form but not
  uniformly back to 1986, because the FR Y-9C has been re-laid-out many times (e.g. the CECL
  provision line, the post-2018 trading-detail breakout). Each is confirmed for the regime in
  which its codes are actually collected.

---

## Reproducing this

Everything needed to reproduce the verdicts is public:

- The **[Relationship Registry](data/relationship_registry.md)** — every relationship, its
  expression, source, verdict, observation count (`empirical_n`), pass rate
  (`empirical_pass_rate`), and test window — is in
  [`csv/RELATIONSHIP_REGISTRY.csv`](https://raw.githubusercontent.com/andenick/bank-data-dictionary/main/csv/RELATIONSHIP_REGISTRY.csv).
- The bulk **FR Y-9C (BHCF)** filings are published by the Federal Reserve and are downloadable
  and queryable via the companion **[FreeNIC](https://github.com/andenick/FreeNIC)** package.
- The field specifications and edit checklist are part of the official FR Y-9C reporting
  instructions (Reporting Central).

Take any `CONFIRMED` row, evaluate its expression against the bulk filings with a
`max($1,000, 0.1%)` tolerance, and you will recover its published pass rate.
