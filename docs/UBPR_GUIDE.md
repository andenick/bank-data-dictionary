# UBPR — Construction, Derivation Formulas & Empirical Validation

The **Uniform Bank Performance Report (UBPR)** is the FFIEC's analytical report that
turns each bank's raw Call Report (FFIEC 031/041/051) into a standardized set of
**derived ratios, percentages, and dollar figures** — every value compared against a
peer-group average and a percentile rank for examiner and analyst use. UBPR items are
**computed/derived, not directly filed**: each `UBPR####` concept is defined by an
official formula over Call Report items and/or other (intermediate) UBPR concepts.

This guide documents how those derivations actually work — parsed from the official
taxonomy, cross-checked against the User's Guide, and **empirically validated against
real published UBPR values**. It is the deep companion to the catalogue entry in
[`FDIC_NCUA_OCC_UBPR_GUIDE.md`](./FDIC_NCUA_OCC_UBPR_GUIDE.md#6-ubpr--uniform-bank-performance-report-ffiec).

**Official sources** (cited; no other dependencies):

- **CDR XBRL UBPR taxonomy v181** — the machine-readable formula, label, reference,
  and presentation linkbases.
- **FFIEC UBPR User's Guide (v181, March 2026)** — authoritative per-concept
  descriptions, narratives, and formulas.

---

## 1. What a UBPR concept is

Each UBPR concept has its own 8-character code, `UBPR####`, where the first letters
after `UBPR` denote a topic group:

| prefix | topic group (examples) |
|---|---|
| `UBPRE…` | Earnings & summary ratios (`UBPRE013` ROA, `UBPRE018` net interest margin) |
| `UBPRD…` | Derived levels / averages (`UBPRD659` average total assets) |
| `UBPRB…`, `UBPRA…`, `UBPRC…`, `UBPRF…`, `UBPRK…`, `UBPRM…` | balance-sheet, asset-quality, liquidity, memoranda |
| `UBPR####` (digits) | items carried directly from the Call Report (e.g. `UBPR2170` total assets) |

Two sibling namespaces hold the **peer statistics** of each base concept:
`UBPS####` (peer-group statistic / average) and `UBPK####` (peer percentile rank).
In `csv/UBPR_CONCEPTS.csv` these carry the base concept's caption suffixed with the
peer kind.

---

## 2. Report page structure

The UBPR is organized into report pages; the taxonomy's presentation linkbase assigns
every concept to one. This repo maps those pages to the following **categories** (the
`category` column in `csv/UBPR_CONCEPTS.csv`):

| category | UBPR pages |
|---|---|
| **Summary Ratios** | Summary Ratios (page 1) |
| **Earnings** | Income Statement $, QTR Income Statement, Noninterest Income & Expenses, Asset Yields & Funding Costs, One-Quarter Annualized Income |
| **Balance Sheet** | Balance Sheet $, Balance Sheet Percentage Composition |
| **Asset Quality** | Concentrations of Credit; Loan Allowance & Loan Mix; Past Due, Nonaccrual & Restructured |
| **Liquidity & Funding** | Liquidity & Funding; Liquidity & Investment Portfolio |
| **Capital** | Capital Analysis |
| **Off-Balance-Sheet / Derivatives / Securitization / Interest Rate Risk / Fiduciary** | the remaining specialty pages |

---

## 3. How derivations work

The taxonomy expresses each derivation as a `select` expression in the CDR formula
dialect. The parser (`_rebuild/officials/taxonomy/parse_ubpr_linkbase.py`) normalizes
it into readable tokens. The vocabulary:

| construct | meaning |
|---|---|
| `UBPRE001`, `RIAD4340`, `RCON2170` | a concept value, current period. `RIAD…` = Call income items (Schedule RI); `RCON…/RCFA…/RCFD…` = Call balance items (Schedule RC). UBPR codes are intermediates. |
| `PCTOF(num, den)` | `100 × num / den` — the core ratio constructor (a percent). |
| `PCTOFANN(num, den)` | the same, **annualized** for a year-to-date flow (see below). |
| `CHANGEYI/QI/YA/QA(…)` | year- or quarter-over change of a flow / average. |
| `IF(condition, then, else)` | almost always a **date or form-version guard** — e.g. `IF(UBPR9999 ≤ '2009-03-31', …, …)` switches the input set for older reporting regimes. |
| `ExistingOf(x, false)` | a COALESCE-like "value if present". |

### 3.1 The three conventions you must get right

These were **calibrated empirically on ROA** and then held unchanged across every
family (full derivation in `_rebuild/empirical/attestations/UBPR_NOTES.md`):

1. **Units.** Call dollar items (`RIAD/RCON/…`) are in **thousands of dollars**.
   UBPR average/level concepts (e.g. `UBPRD659`) are published in **dollars**. In a
   ratio mixing the two, divide the UBPR dollar value by 1,000 to align. (When both
   sides are the same kind, the factor cancels.)

2. **Annualization.** `PCTOFANN` annualizes a year-to-date income flow by **4/q**,
   where q is the quarter index: **Q1 ×4, Q2 ×2, Q3 ×4⁄3, Q4 ×1**.

3. **Averaging.** Denominators like `UBPRD659` (average total assets) are
   *year-to-date averages of the quarterly Schedule RC-K average balances* — taken
   here as published intermediates rather than re-derived. The User's Guide confirms:
   "A year-to-date average of the average assets reported in the Call Report Schedule
   RC-K." Tax-equivalent (TE) income figures (`UBPR4107`, `UBPR4074`) include the
   municipal-income gross-up and are likewise used as published intermediates.

### 3.2 Worked example — Return on Assets (`UBPRE013`)

Taxonomy formula: `IF(UBPRD659 ≠ 0, PCTOFANN(RIAD4340, UBPRD659), NULL)`
→ **ROA = 100 × (net income, annualized) / (average total assets)**.

Real bank, 2023-Q4 (q=4, factor 1): net income `RIAD4340` = −644,000 (thousands),
average assets `UBPRD659` = 557,077,500,000 (dollars):

```
100 × (−644,000) / (557,077,500,000 / 1000) = −0.1156
```

Published `UBPRE013` for that bank-quarter: **−0.12**. Agreement is within the
2-decimal rounding boundary.

---

## 4. Empirically validated headline ratios

**31 headline ratios** were recomputed from Call/UBPR inputs and compared to the
published values over **2015-Q1 → 2026-Q1** (recent window where conventions are
stable), up to 1,200 banks per ratio (~44,000 bank-quarters each). **All 31
VALIDATED** (agreement 99.77%–100.0%); the full table is `RESULTS_ubpr.csv`.

| UBPR code | ratio | derivation (normalized) | agreement |
|---|---|---|---|
| `UBPRE013` | Return on assets (ROA) | `100 · RIAD4340 / UBPRD659`, annualized | 99.79% |
| `UBPRE630` | Return on equity (ROE) | `100 · RIAD4340 / UBPRD342`, annualized | 99.77% |
| `UBPRE018` | Net interest margin (TE) | `100 · UBPR4074 / UBPRD362`, annualized | 99.77% |
| `UBPRE088` | Efficiency ratio | `100 · UBPRE037 / UBPRE036` | 100.0% |
| `UBPRE006` | Provision / avg assets | `100 · UBPRD483 / UBPRD659`, annualized | 99.87% |
| `UBPR7402` | Cash dividends / net income | `100 · UBPRE625 / RIAD4340` | 100.0% |
| `UBPRE019` | Net loss / avg total loans | `100 · UBPR1795 / UBPRE386`, annualized | 99.93% |
| `UBPRE541` | 90+ days past due / gross loans | `100 · UBPRD667 / UBPRE131` | 100.0% |
| `UBPRE542` | Nonaccrual / gross loans | `100 · UBPRD669 / UBPRE131` | 100.0% |
| `UBPR7414` | Noncurrent loans / gross loans | `100 · UBPR1400 / UBPRE131` | 100.0% |
| `UBPRE523` | Loss allowance / total loans | `100 · UBPRD095 / UBPRD146` | 100.0% |
| `UBPRE024` | Net loans & leases / total assets | `100 · UBPRE119 / UBPR2170` | 100.0% |
| `UBPRE600` | Net loans & leases / deposits | `100 · UBPRE119 / UBPRD663` | 100.0% |
| `UBPRD486` | Tier 1 leverage ratio | regulator-reported (see §6) | 100.0%* |
| `UBPRD487` | Tier 1 risk-based capital ratio | regulator-reported (see §6) | 100.0%* |
| `UBPRD488` | Total risk-based capital ratio | regulator-reported (see §6) | 100.0%* |

`*` capital ratios are validated as the documented `×100` relationship to their
rounded-fraction series, **within ±0.5 pp** — see §6.

### Six more worked derivations

- **Net interest margin (`UBPRE018`)** = `PCTOFANN(UBPR4074, UBPRD362)` = tax-equivalent
  net interest income / average earning assets, annualized. (`UBPR4074` = TE total
  interest income `UBPR4107` − total interest expense `RIAD4073`.)
- **Efficiency ratio (`UBPRE088`)** = `PCTOF(UBPRE037, UBPRE036)` = total overhead
  expense / (net interest income + noninterest income). Not annualized — both sides
  are flows over the same window, so the ratio is period-neutral. 100% agreement.
- **Net charge-off rate (`UBPRE019`)** = `PCTOFANN(UBPR1795, UBPRE386)` = net credit
  losses (gross charge-offs − recoveries) / average total loans & leases, annualized.
- **Noncurrent loans (`UBPR7414`)** = `PCTOF(UBPR1400, UBPRE131)` = (loans 90+ days
  past due **plus** nonaccrual) / gross loans & leases — the standard asset-quality
  headline. 100% agreement.
- **Loan-mix concentration (`UBPRE424`)** = `PCTOF(UBPRD172, UBPRD242)` = loans to
  individuals / gross loans & leases. The mix ratios `UBPRE423/424/432/890` all
  validated at ≈100%.
- **Net loans / assets (`UBPRE024`)** = `PCTOF(UBPRE119, UBPR2170)` = net loans &
  leases / total assets — a liquidity/balance-sheet headline. 100% agreement.

---

## 5. The concept catalogue (`csv/UBPR_CONCEPTS.csv`)

One row per UBPR concept that appears in the published data or the formula set —
**4,099 concepts**. Columns:

| column | meaning |
|---|---|
| `ubpr_code` | the `UBPR####` / `UBPK####` / `UBPS####` code |
| `caption` | authoritative caption (User's Guide preferred) |
| `category` | report-page family (§2) |
| `derivation` | human-readable formula over Call codes / UBPR intermediates, where cleanly parseable; otherwise `-` |
| `inputs` | the regulatory codes the formula consumes |
| `validated` | `yes` for the 31 empirically tested ratios, else `no` |
| `empirical_agreement_rate` | agreement rate for validated concepts |
| `notes` | provenance (in published data; taxonomy formula kind; validation n/verdict) |

The full machine-readable formula parse (all 4,207 taxonomy formulas, including the
raw multi-branch conditionals) lives in
`_rebuild/officials/taxonomy/OFFICIAL_UBPR_FORMULAS.csv`.

---

## 6. Honest limitations

- **Which families are validated vs cataloged.** Earnings, Asset Quality, and
  Liquidity & Funding headline ratios are **recomputed and validated**. The whole
  concept universe (all categories, 4,099 codes) is **cataloged** with its parsed
  derivation, but only the 31 headline ratios are independently re-derived.
- **Capital adequacy ratios are regulator-reported, not UBPR-recomputed.**
  `UBPRD486/487/488` (Tier 1 leverage, Tier 1 RBC, total RBC) are the precise percent
  series; `UBPR7204/7205/7206` are the **same ratios stored rounded to 2 decimals as a
  fraction**. The `UBPRD48x = UBPR720x × 100` identity holds **within ±0.5 pp** (the
  fraction-rounding band). Risk-weighted assets and the CET1 ratio are **not**
  recomputed from RC-R primitives (RWA is a complex regulatory computation outside
  this scope) — they are cataloged as Call passthroughs.
- **`UBPR7408` and `UBPRE635` are growth rates**, not capital-adequacy measures
  (their Guide captions: "Tier One Capital 12-month growth rate", "Annual Growth Rate
  in Total Bank Equity Capital"). They validate as parsed but should not be read as
  adequacy ratios.
- **Intermediate averages are taken as published.** Where a denominator is itself a
  UBPR average (e.g. `UBPRD659`), validation uses its published value; the test
  confirms the **ratio construction and conventions**, while the intermediate's own
  multi-quarter average derivation is cataloged, not independently re-validated.
- **Unparseable derivations are honest `-` / `UNTESTED`.** 361 of 4,207 formulas are
  deeply nested conditionals that resist a single-expression reading; they are
  preserved raw in the formula CSV and shown as `-` in the catalogue rather than
  guessed at.
- **Window.** Validation is 2015+ only; pre-2015 form-version branches are cataloged
  but not validated.

---

## 7. Reproduce

```powershell
$env:PYTHONIOENCODING = 'utf-8'
python _rebuild/officials/taxonomy/extract_ubpr_guide.py
python _rebuild/officials/taxonomy/parse_ubpr_linkbase.py
python _rebuild/officials/taxonomy/build_ubpr_concepts.py
python _rebuild/empirical/validate_ubpr.py
```

All database access is read-only and aggregate. Full method and calibration:
`_rebuild/empirical/attestations/UBPR_NOTES.md`.
