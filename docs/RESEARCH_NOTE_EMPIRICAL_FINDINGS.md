# What 2.1 Billion Filings Reveal About the Bank Regulatory Rulebook: Empirical Findings from a Verified Data Dictionary

> A researcher-facing summary of the empirical findings from the v8–v10 validation campaigns.
> Every number below traces to [Empirical Validation](EMPIRICAL_VALIDATION.md), the
> [Relationship Registry](data/relationship_registry.md), and the official edit sources cited there.

---

## 1. Setting — what was tested

A data dictionary usually *asserts* that "assets equal liabilities plus equity" and stops. This
project tests every such assertion as an aggregate query against the full history of real bank
filings, then publishes the pass rate, the observation count, and an honest verdict for each.

What was tested:

- **The official rules.** The FFIEC Call Report edit checks and calculation-linkbase identities,
  taken directly from the regulators' own machine-readable formula linkbases (the CDR XBRL
  taxonomy, `cdr.ffiec.gov`) — **3,615 edits per form** plus **243 calculation-linkbase identities**
  across forms FFIEC 031 / 041 / 051 — and the FR Y-9C edit checklist, parsed the same way. To these
  were added the dictionary's curated reconciliation identities and component hierarchies, and (in
  v10) the UBPR derivation formulas.
- **The corpus.** These rules were evaluated against the full bulk filing record: **208 million**
  reported cell-values of **FR Y-9C** (bulk BHCF) data, every quarter 1986 Q3 – 2025 Q4, 13,668
  holding companies; and **1.917 billion rows** of **Call Report** filings, 2001 Q1 – 2026 Q1.
- **The registry.** The result is a single **7,539-relationship** registry, every row carrying a
  status and — where machine-testable — its empirical observation count and pass rate. **Zero rows
  are left pending or unexplained.** Of these, 2,464 Call relationships and the FR Y-9C set were
  machine-evaluated; a 16-concept cross-source concordance and 31 UBPR ratios were validated
  independently.

A relationship "passes" for a filing when both sides agree within `max($1,000, 0.1%)` of the larger
side — enough to absorb thousands-rounding without masking a real break. Every non-passing row was
adjudicated against the official edit text, the field specification, and the MDRM — never silently
dropped.

---

## 2. Finding I — official rules that don't hold in the filed data

Eight official edits do **not** hold even on the correct window, population, and
all-components-reported subset. They are kept deliberately as research findings about how the
official edit set behaves against real public data, classified `OFFICIAL_EDIT_UNMET`. The two
headline cases:

**(I-a) A phantom decomposition.** The official calculation linkbase decomposes the
representation-and-warranty reserve `RCONM288` into `RCONL191 + RCONL192`. But `L191` and `L192`
have **zero observations warehouse-wide** in the public bulk data, while `M288` is reported directly
in **51,992 filings**. The decomposition is not empirically derivable from anything public; the
edit fails at **0.828** and is documented, not enforced (registry `REL_7424`). A second,
RCON-side variant of the same family (`REL_5161`, the same `M288 = L191 + L192` reserve, edit
`R6230.5551`) was surfaced by the v10 conditional engine and is the 8th finding — pass **0.937**,
same root cause.
*Reproduce:* over all Call filings, compare `RCONM288` against `RCONL191 + RCONL192`; note that
`L191`/`L192` are never populated, so the sum collapses to zero while the parent is reported.

**(I-b) A securitization bound that mostly fails among the population it's about.** An RC-R Part II
securitization bound (`REL_5882`, edit `R7020.6507`) holds at a headline **0.983** — but that rate
is dominated by zero-filers (banks with no securitization, for whom both sides are 0). Among
**active securitizers** — the population the edit is actually about, **n = 3,493** — it holds at only
**0.452**. That is a real, substantial explained-violation population, not a rounding tail.
*Reproduce:* restrict to bank-quarters where the securitization components are non-zero, then test
the bound; the pass rate falls from 0.983 to 0.452.

The remaining six are soft "should-be" quality edits whose violation rates are themselves the
finding: an RC-O brokered-deposit bound at **0.714** (`REL_5399`, `R6770.5451`) and a family of
RI-C / RC-C CECL loan-category bounds at **0.657 – 0.937** (`REL_3757/3759/3760/3763`, edits
`R2006.7256/7258/7259/7262`). All eight rows, with full expressions and per-row `empirical_n` /
`empirical_pass_rate`, are in the [Relationship Registry](data/relationship_registry.md) filtered
to `OFFICIAL_EDIT_UNMET`.

---

## 3. Finding II — corrected cross-source definitional mappings

For 16 core concepts the Call Report value was compared against the FDIC's independently-collected
Statistics on Depository Institutions (SDI), bank-quarter by bank-quarter, over up to **667,551**
bank-quarters. All 16 concord at **99.5 – 99.97%**. More usefully, the concordance surfaced two
mappings that the naïve crosswalk gets wrong:

**(II-a) Total equity → Call item `3210`, not `G105`.** FDIC `EQ` maps to **`RCFD/RCON3210`** (total
bank equity, *excluding* minority interest). The minority-interest-*inclusive* total `G105` scored
only **98.6%** against `EQ`; `3210` scores **99.72%** (n = 666,679). The correct FDIC↔Call equity
mapping therefore excludes minority interest.

**(II-b) Net loans → `2122 − 3123`, not `B529`.** FDIC `LNLSNET` maps to loans net of unearned
income (`2122`) minus the allowance (`3123`), *not* the Schedule RC-C item-12 net total `B529`. The
`B529` basis scored only **77.8%**; the `2122 − 3123` expression scores **99.89%** (n = 656,563).
The two "net loans" totals are defined differently, and the SDI uses the `2122 − 3123` basis.

Why it matters: anyone joining FDIC SDI to Call Report data on "equity" or "net loans" with the
obvious code will inherit a 1.4- or 22-point definitional mismatch that looks like noise but is
structural. Both corrections are recorded in
[`json/cross_form_mapping.json`](../json/cross_form_mapping.json) under `total_equity` and
`total_loans`; the full 16-concept table is in `_rebuild/empirical/RESULTS_cross_source.csv`.

---

## 4. Finding III — the rulebook's 25-year growth

The official Call Report edit set was parsed from **30 reporting cycles** (every year-end 2001–2024
plus all 2025–2026 quarters, forms 031/041/051), one machine-readable lifetime per edit label.
Headline numbers ([Edit History](EDIT_HISTORY.md), `csv/EDIT_HISTORY.csv`):

- **15,622** distinct edit labels observed, 2001–2026.
- **4,759** retired before the current (2026 Q1) cycle.
- **1,212** introduced in 2020 or later.
- Edit count grew from ~2,450 (2001 year-end) to ~11,000 (2025 Q1) — the rulebook roughly
  **quintupled in 25 years**, with quality ("should"-hold) edits outnumbering validity
  ("must"-hold) edits about 2.5 : 1 throughout.

The eras are visible in the data: a steady state (2001–2007), a crisis buildout in past-due /
securitization / fair-value reporting (2008–2013), the **Basel III spike** (2014–2019 — the single
largest event, validity edits jumping from ~2,100 to ~3,300 while hundreds of pre-Basel capital
edits retire simultaneously), the **CECL and pandemic** turnover (2020–2022 — ASU 2016-13 allowance
edits replace incurred-loss edits; short-lived PPP items appear and depart), and a refinement
plateau (2023–2026, where change shifts to expression revisions within continuing labels).

---

## 5. Finding IV — UBPR construction conventions, pinned empirically

The Uniform Bank Performance Report (UBPR) turns each bank's raw Call Report into derived ratios.
The official CDR XBRL UBPR taxonomy v181 and User's Guide were acquired, **4,207 derivation formulas
parsed with zero silent drops**, and the **31 headline ratios** recomputed from Call/UBPR inputs and
compared to the **real published UBPR value** over 2015 Q1 – 2026 Q1 (~44,000 bank-quarters per
ratio). **All 31 validated at 99.77 – 100%** (e.g. ROA `UBPRE013` at 99.79%, ROE `UBPRE630` at
99.77%, net interest margin `UBPRE018` at 99.77%, efficiency `UBPRE088` at 100.0%). Calibrating the
validation pinned three construction conventions that a naïve reading gets wrong
([UBPR Guide](UBPR_GUIDE.md)):

1. **Units.** Call dollar items (`RIAD/RCON/…`) are in **thousands**; UBPR average/level concepts
   (e.g. `UBPRD659`) are in **dollars**. A ratio mixing the two must divide the UBPR value by 1,000.
2. **Annualization.** Year-to-date flows annualize by **×(4/q)** — Q1 ×4, Q2 ×2, Q3 ×4⁄3, Q4 ×1.
3. **Averages as published.** Denominators like `UBPRD659` (average total assets) are taken as
   published year-to-date averages of the Schedule RC-K quarterly balances, not re-derived.

**Caption-mislabel warning.** The taxonomy's presentation captions mislabel some concepts; the
User's Guide is authoritative. `UBPR7408` and `UBPRE635` read like capital-adequacy measures but are
**12-month growth rates** ("Tier One Capital 12-month growth rate"). They validate as parsed but must
not be read as adequacy ratios. Relatedly, the capital ratios `UBPRD486/487/488` are **regulator
passthroughs** stored 2-decimal-rounded as a fraction — validated as the documented `×100`
relationship within a ±0.5 pp band, not recomputed from RC-R primitives.

---

## 6. Methods in brief

- **Tolerance.** A relationship passes a filing when the two sides agree within `max($1,000, 0.1%)`
  of the larger side — absorbing thousands-rounding without masking real breaks.
- **Windows and populations.** Each edit is tested on the window and sub-population where its codes
  are actually collected. Where a headline rate is dominated by trivial zero-filers (e.g. the
  securitization bound), the rate among the active population is reported alongside it.
- **Adjudication to zero unexplained.** Every non-passing row was investigated against the official
  edit text, field spec, and MDRM and assigned a defended verdict — `CONFIRMED`, `CONFIRMED_CURRENT`,
  `QUALITY_TOLERANCE`, `DATA_GAP` (sparse child line-items, identity correct), `NOT_IN_BULK`,
  `CONDITION_NEVER_MET`, or `OFFICIAL_EDIT_UNMET` — never dropped. Notably, the RC-O probability-of-
  default-bucket family (`CONDITION_NEVER_MET`, 48 rows) references **280 codes that are confidential
  supervisory items, verified absent from all public bulk data**, so its triggering condition is
  never met in any public filing.
- **Independent verification, including of our own tester.** Adjudication repeatedly caught harness
  defects rather than data errors — a dropped distributed-negation (`A − (B + C)` read as `A + B +
  C`), a silently dropped multiplication (`X = Y × 0` read as `X = Y`), and a registry expression
  truncated at ~588 characters. Each was traced to its source and repaired against the official edit
  text before any verdict was recorded.

Full method, verdict taxonomy, and the complete results distribution:
[Empirical Validation](EMPIRICAL_VALIDATION.md) and the
[Relationship Registry data page](data/relationship_registry.md).

---

## 7. How to reproduce, and how to cite

Everything needed to reproduce the verdicts is public:

- The **Relationship Registry** — every relationship, its expression, source (official edit id
  and/or calculation-linkbase parent), status, observation count (`empirical_n`), pass rate
  (`empirical_pass_rate`), and test window — is in
  [`csv/RELATIONSHIP_REGISTRY.csv`](https://raw.githubusercontent.com/andenick/bank-data-dictionary/main/csv/RELATIONSHIP_REGISTRY.csv).
- The bulk **FR Y-9C (BHCF)** and **Call Report** filings are published by the Federal
  Reserve / FFIEC and are downloadable and queryable via the companion data package,
  **[FreeNIC](https://github.com/andenick/FreeNIC)**.
- The official edits are the **FFIEC Call Report edit checks and calculation linkbases** in the CDR
  XBRL taxonomy (`cdr.ffiec.gov`) and the FR Y-9C edit checklist.
- `scripts/validate_reconciliation.py --scope {y9c,call,all,ubpr}` evaluates the registry against
  any supplied filing. Take any `CONFIRMED` row, evaluate its expression against the bulk filings
  with the `max($1,000, 0.1%)` tolerance, and you will recover its published pass rate.

**Citation.**

> *Bank Regulatory Data Dictionary — Empirical Validation (v10.0).* The validated relationship
> registry and edit-history dataset. https://github.com/andenick/bank-data-dictionary
>
> Data companion: *FreeNIC* — bulk FR Y-9C and Call Report filings.
> https://github.com/andenick/FreeNIC
