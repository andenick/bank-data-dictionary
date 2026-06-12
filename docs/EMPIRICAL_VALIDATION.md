# Empirical Validation

> **Version 10.0 | 2026-06-11** — every machine-testable official edit on the FR Y-9C **and** the
> Call Report, validated against **208 million + 1.9 billion rows** of real filings; plus the
> **UBPR** derivation formulas validated against real published UBPR values, and a
> **conditional/compound testing engine** that drives every registry row to an explained verdict.

Most data dictionaries assert that "assets equal liabilities plus equity" and stop there. This
one tests it. Every reconciliation identity, bound, and official edit check we publish is checked,
as an actual aggregate query, against the full history of real bank filings — and we publish the
pass rate, the observation count, and an honest verdict for each.

In **v8.0** that meant the FR Y-9C, tested against 208 million rows of bank-holding-company
filings. **v9.0 adds the Call Report**: we acquired the official FFIEC Call Report edit checks and
calculation linkbases (machine-readable, current cycle), structured them into the registry, and
evaluated every machine-testable one against **1.917 billion rows** of Call Report filings
(2001 Q1 – 2026 Q1). We also ran a **cross-source concordance** that checks 16 core concepts
between the Call Reports and the FDIC's independently-collected Summary of Deposits / Statistics on
Depository Institutions (SDI), and corrected two definitional mappings in the process.

The combined [Relationship Registry](data/relationship_registry.md) now holds **7,539
relationships**, every one carrying a status and — where machine-testable — its empirical
observation count and pass rate. **Zero rows are left pending or unexplained.**

**v10.0 adds two things on top of v9.** First, a **conditional/compound testing engine** (IF/THEN
rewritten to SQL `CASE`, AND-conjunction splitting, and constant coefficients) made **448** of the
2,606 previously documented-but-untested conditional/compound rows machine-testable, and every one
of them was adjudicated to an explained verdict; the rest stay honestly documented (2,158
`GRAMMAR_DOC`: null-logic and ratio-division families). Second, the **UBPR** — the FFIEC's analytical
report of derived ratios — was acquired from the official taxonomy v181 and User's Guide, its 4,207
derivation formulas parsed with zero silent drops, and its 31 headline ratios recomputed and
**empirically validated at 99.77–100%** against real published UBPR values. The full v10 status
distribution is in the Results section below.

---

## Where the official edits come from

The v9.0 Call Report layer is built on the **official FFIEC Call Report edit checks and
calculation linkbases, distributed in the CDR XBRL taxonomy (cdr.ffiec.gov)**. These are the same
machine-readable formula linkbases the regulators use to validate filings: **3,615 edits per form**
plus **243 calculation-linkbase identities**, for all three Call Report forms (FFIEC **031 / 041 /
051**) at the current cycle (taxonomy v294, 2026-03-31). We additionally archived **30 historical
cycles** (year-ends 2001–2024 plus every 2025–2026 quarter) so the edit set can be aligned to the
vintage of any filing we test.

This is the authoritative source: rather than re-deriving edits from the human-readable
instructions, v9.0 parses the regulators' own formula linkbases directly, so every tested Call
Report relationship traces to an official edit id or calculation-linkbase parent.

---

## What was done

The methodology is the same on both sides: **acquire the official edits → parse the formula
linkbases → structure into the registry → test every machine-testable relationship against bulk
filings → adjudicate every non-passing result, never silently dropping one.**

1. **Acquire and parse the official edits.** For the Call Report, the formula linkbases were taken
   from the CDR XBRL taxonomy and parsed into linear MDRM expressions (sums, differences, bounds).
   For the FR Y-9C, the official edit checklist was parsed the same way in v8.0. Together with the
   dictionary's curated identities and component hierarchies, this produced the single
   **7,539-relationship** [Relationship Registry](data/relationship_registry.md) (v10.0 added the
   31 UBPR derivation rows and the conditional/compound rows promoted to testable).

2. **Test every testable relationship against real filings.**
   - **FR Y-9C:** every Y-9C relationship that resolves to codes present in the bulk data was
     evaluated as an aggregate query over **Federal Reserve bulk BHCF (FR Y-9C) data**, every
     quarter **1986 Q3 – 2025 Q4**, **13,668 holding companies**, **~208 million reported
     cell-values**.
   - **Call Report:** all **2,464 machine-testable call relationships** were evaluated against
     **1.917 billion rows of Call Report filings (2001 Q1 – 2026 Q1)** — **1,392 sign/bound tests**
     via one bulk scan plus **1,072 identity/bound tests** over a per-code extract.
   - **Y-9C intraseries:** **63** period-over-period (YTD monotonicity) edits were tested with
     `LAG()` over the filing history (62 CONFIRMED + 1 CONFIRMED_CURRENT); a further **221** are
     documented as conditional (they hold only within a reporting sub-population and are not
     cross-sectional identities).

   A relationship "passes" for a filing when the two sides agree within `max($1,000, 0.1%)` of the
   larger side — enough to absorb thousands-rounding without masking real breaks.

3. **Run a cross-source concordance.** For **16 core concepts**, the Call Report value was compared
   against the **FDIC SDI** value for the same bank-quarter — an independent collection — over up to
   **667,551 bank-quarters** each. All 16 concord at **99.5–99.97%**. Two definitional mappings were
   corrected in the process (see below).

4. **Adjudicate every non-passing result.** Each relationship that did not pass cleanly was
   investigated against the official edit text, the field specification, and the MDRM — not silently
   dropped. The Call-side adjudication is documented in full in
   `_rebuild/empirical/ADJUDICATION_V9.md`. As in v8.0, this caught bugs in our own test harness
   (see *Adversarial rigor* below), several sparse-data artifacts, and a small set of genuine
   official-edit violations kept as research findings. The result is a registry in which every
   tested row has a defended verdict and **zero** rows are left in an unexplained state.

**Sources.** Federal Reserve / FFIEC bulk data: the **bulk BHCF (FR Y-9C) data (1986–2025)**, the
**bulk Call Report data (2001–2026)**, and the **FDIC SDI** time series; the **official FFIEC Call
Report edit checks and calculation linkbases (CDR XBRL taxonomy, cdr.ffiec.gov)**; the **FR Y-9C
edit checklist and field specifications**; and the Federal Reserve **MDRM**. No private or derived
data is involved.

---

## The verdict taxonomy

| Verdict | Meaning |
|---------|---------|
| **CONFIRMED** | Holds in ≥99% of all observed filings across the full available window. A structural identity or a robust bound. |
| **CONFIRMED_CURRENT** | Holds in ≥99% of filings in the current reporting regime; older vintages differ because the form line-up was renumbered or split. Correct for today's form. |
| **QUALITY_TOLERANCE** | A regulator "should"-edit or a valid economic bound with a small, explained tail. We publish the actual rate rather than rounding it to "100%". |
| **DATA_GAP** | A genuine identity whose component splits are too sparsely populated in bulk to test as an all-plus sum (banks file the parent total but leave child line-items blank; coalesce-to-zero then breaks the sum). |
| **NOT_IN_BULK** | One side uses a code that is text/confidential/narrative or was discontinued/renumbered, so the two sides never co-occur in the bulk data. Documented, not testable. |
| **CONDITIONAL_DOC** | Applies only to a sub-population or is a conditional/non-arithmetic edit (completeness test, string value-domain, function), so it is not a cross-sectional identity. Verified by documentation. |
| **OFFICIAL_EDIT_UNMET** | An official edit that does **not** hold even on the correct window/population. Kept deliberately as a research finding about edit enforcement, not deleted. |
| **CONDITION_NEVER_MET** | A conditional edit whose triggering condition is never satisfied in any public bulk filing — the codes are confidential supervisory items absent from all bulk data (the RC-O PD-bucket family). Verified absent, not silently dropped. |
| **VINTAGE_CONFIRMED** | A relationship confirmed on the vintage window where its codes are actually collected, distinguished from `CONFIRMED_CURRENT` by an explicit vintage anchor. |
| **LOW_N_PASS** | Passes within tolerance but on a small observation count; flagged so the thin sample is not read as a full-history confirmation. |
| **GRAMMAR_DOC** | A conditional/compound row outside the testable grammar subset (null-logic, ratio-division, multi-branch families). Documented with its parsed form rather than forced into a linear test. |

---

## Results — the full registry

| Status | Count |
|--------|------:|
| **CONFIRMED** | **2,841** |
| **CONFIRMED_CURRENT** | **144** |
| **LOW_N_PASS** | **4** |
| **VINTAGE_CONFIRMED** | **7** |
| **QUALITY_TOLERANCE** | **43** |
| **DATA_GAP** | **122** |
| **OFFICIAL_EDIT_UNMET** | **8** |
| **CONDITION_NEVER_MET** | **48** |
| **NOT_IN_BULK** | **134** |
| **CONDITIONAL_DOC** | **224** |
| **GRAMMAR_DOC** (documented null-logic / ratio-division families) | **2,158** |
| **not_testable** (documented non-arithmetic classes) | **1,806** |
| **Total** | **7,539** |

By scope: **2,330 FR Y-9C**, **5,162 Call Report** (deduplicated across the three forms),
**16 cross-source**, and **31 UBPR**. **Zero rows are pending or unexplained.** The `not_testable`
and `GRAMMAR_DOC` classes are not gaps — they are the documented set of non-arithmetic edits
(completeness / null tests, string value-domain checks, ratio-division and null-logic conditionals,
and function edits) that cannot be expressed as a linear identity over reported values; each is
labelled with its class.

---

## Showcase: confirmed Call Report identities

A selection of the official Call Report edits and calculation-linkbase identities, with their real
pass rates and observation counts against the 1.9-billion-row bulk Call data. Pass rate is the
share of filings in which the relationship held within tolerance.

| Relationship | What it checks | Observations | Pass rate | Verdict |
|---|---|---:|---:|---|
| `RCON2200 = RCON6631 + RCON6636` | Total domestic deposits = noninterest-bearing + interest-bearing | 666,695 | **100.00%** | CONFIRMED |
| `RIAD4074 = RIAD4107 − RIAD4073` | Net interest income = total interest income − total interest expense | 669,296 | **99.99%** | CONFIRMED |
| `RIAD4300 = RIAD4301 − RIAD4302` | Income before taxes ties to the pre-tax/applicable-tax decomposition | 669,338 | **99.99%** | CONFIRMED |
| `RCON2215 = RCON2202 + RCON2203 + RCON2213 + RCON2216 + RCONB549 + RCONB551` | Total transaction-account deposits build up from their components | 667,320 | **99.94%** | CONFIRMED |
| `RCON3548 = RCON3546 + RCON3547 + RCONF624` | Total trading liabilities tie to their reported components | 671,820 | **99.13%** | CONFIRMED |
| `(RCON3493 + RCON3494 + RCON3495) ≤ RCON1420` | Past-due/nonaccrual real-estate loans bounded by total RE loans | 666,695 | **100.00%** | CONFIRMED |
| `(RCONB575 + RCONB576 + RCONB577) ≤ RCONB538` | Past-due credit-card components bounded by their total | 656,623 | **100.00%** | CONFIRMED |
| `RCON3164 ≤ RCONA590 + 25,000` | Premises bound (official edit, with its $25k allowance) | 656,623 | **100.00%** | CONFIRMED |

Each row traces to an official Call edit id (e.g. `R5620.2637` across forms 031/041/051) or a
calculation-linkbase parent (`official_calc:RCON…`), recorded in the registry's `sources` column.

---

## Cross-source concordance (Call Report vs FDIC SDI)

Sixteen core concepts were checked between the Call Reports and the FDIC's independently-collected
SDI, bank-quarter by bank-quarter. **All 16 concord at 99.5–99.97%.** The full table is in
`_rebuild/empirical/RESULTS_cross_source.csv`; a selection:

| Concept | FDIC variable | Call expression | Bank-quarters | Agreement |
|---|---|---|---:|---:|
| Total assets | `ASSET` | `RCFD2170` / `RCON2170` | 667,551 | **99.84%** |
| Total liabilities | `LIAB` | `RCFD2948` / `RCON2948` | 666,523 | **99.55%** |
| Total equity | `EQ` | `RCFD3210` / `RCON3210` | 666,679 | **99.72%** |
| Total deposits | `DEP` | `RCON2200 + RCFN2200` | 659,789 | **99.97%** |
| Net loans & leases | `LNLSNET` | `RCFD2122 − RCFD3123` | 656,563 | **99.89%** |
| Net income | `NETINC` | `RIAD4340` | 666,230 | **99.75%** |
| Interest income | `INTINC` | `RIAD4107` | 666,245 | **99.87%** |
| Noninterest income | `NONII` | `RIAD4079` | 664,271 | **99.85%** |

### Two corrected definitional mappings (findings)

The concordance is not just a pass/fail check — it surfaced two mappings that the naïve crosswalk
gets wrong, and we corrected them:

1. **Total equity → Call item `3210`, not `G105`.** FDIC `EQ` maps to **`RCFD/RCON3210`** (total
   bank equity, *excluding* minority interest). The minority-interest-*inclusive* total `G105`
   scored only **98.6%** against `EQ`; `3210` scores **99.72%**. The correct FDIC↔Call equity
   mapping therefore excludes minority interest.

2. **Net loans → `2122 − 3123`, not `B529`.** FDIC `LNLSNET` maps to **loans net of unearned income
   (`2122`) minus the allowance (`3123`)**, *not* the Schedule RC-C item-12 net total `B529`. The
   `B529` basis scored only **77.8%**; the `2122 − 3123` expression scores **99.89%**. The two
   "net loans" totals are defined differently, and the SDI uses the `2122 − 3123` basis.

Both corrections are recorded in [`json/cross_form_mapping.json`](../json/cross_form_mapping.json)
under the `total_equity` and `total_loans` concepts.

---

## Showcase: confirmed FR Y-9C identities

The v8.0 FR Y-9C results carry forward unchanged. A selection, against the 208-million-row bulk
BHCF data:

| Relationship | What it checks | Observations | Pass rate | Verdict |
|---|---|---:|---:|---|
| `BHCK3300 = BHCK2170` | Total liabilities + equity = total assets (form item 29 = item 12) | 187,845 | **100.00%** | CONFIRMED |
| `BHCK4074 = BHCK4107 − BHCK4073` | Net interest income = total interest income − total interest expense | 187,842 | **100.00%** | CONFIRMED |
| `BHCKB529 = BHCKB528 − BHCK3123` | Net loans = loans held for investment − allowance | 100,102 | **100.00%** | CONFIRMED |
| HI-A equity roll-forward | The full Schedule HI-A changes-in-equity build-up | 55,766 | **99.95%** | CONFIRMED |
| `BHCK2170 = BHCK2948 + BHCK3210` | Assets = liabilities + holding-company equity (textbook A = L + E) | 187,845 | **92.60%** | QUALITY_TOLERANCE |

The last row is instructive: the textbook identity holds exactly only on the **item-29** form
(`BHCK3300`), which ties to total assets at 100.00%. The bare "liabilities + holding-company
equity" form omits noncontrolling interest and so holds in 92.6% of filings — we publish the 92.6%
honestly rather than presenting the textbook form as exact.

---

## Conditional & compound edits (v10.0)

Many official edits are not bare arithmetic identities — they are **conditional** (`IF <cond> THEN
<test>`) or **compound** (`T1 AND T2 AND …`). Through v9 these were carried as documented-but-untested
rows. v10.0 added a **conditional/compound testing engine** that extends the linear evaluator with
three constructs while keeping the linear-only token rule (multiplication/division by a *variable*
still hard-fails rather than being guessed at):

- **IF/THEN → CASE.** `IF <cond> THEN <test>` is evaluated as a SQL `CASE WHEN cond THEN (test)`,
  with the pass rate computed over the sub-population where the condition holds and the population
  size (`n_cond`) reported alongside.
- **AND-conjunction splitting.** A compound `T1 AND T2 AND …` of simple comparisons is evaluated as a
  single all-clauses-hold row predicate; OR-compounds are evaluated as written.
- **Constant coefficients.** Multiplication by a literal constant (e.g. the `× 0` zero-conversion
  edit) is evaluated faithfully — the fix that grew out of the v9 dropped-multiplication catch.

**Coverage.** Of the 2,606 conditional/compound rows, **448 became machine-testable** and were run;
the remaining **2,158 stay `GRAMMAR_DOC`** (null-logic and ratio-division families, documented with
their parsed form — ratio derivations are handled properly in the UBPR work instead rather than
forced through a linear test). Every newly-testable row was adjudicated to an explained verdict:
**246 CONFIRMED + 61 CONFIRMED_CURRENT + 4 LOW_N_PASS**, then to zero unexplained — **81 DATA_GAP**,
**48 CONDITION_NEVER_MET**, **7 QUALITY_TOLERANCE**, **7 VINTAGE_CONFIRMED**, and **1 new
OFFICIAL_EDIT_UNMET** (the 8th overall).

Two stories make the adjudication concrete:

- **CECL transitions are a DATA_GAP, not a broken identity.** The largest block of conditional
  "failures" are ASU 2016-13 (CECL) allowance and provision edits. They hold cleanly once the test is
  restricted to the **post-adoption sub-population** — a bank that has adopted CECL reports the new
  allowance build-up, while pre-adoption filings leave the new line-items blank and the coalesce-to-
  zero sum breaks. The identity is correct; the public data spans the regime change. These are
  classified **DATA_GAP** with the transition fully explained on the post-adoption subset.

- **The RC-O PD-bucket family is CONDITION_NEVER_MET.** A family of conditional edits over Schedule
  RC-O probability-of-default buckets references **280 codes that are verified absent from all public
  bulk data** — they are confidential supervisory items (large-bank PD/LGD inputs) collected but never
  published in bulk. The triggering condition is therefore never satisfied in any public filing. Rather
  than report a meaningless pass rate, these **48** rows are classified **CONDITION_NEVER_MET** with
  the 280-code absence documented.

---

## UBPR derivation validation (v10.0)

The **Uniform Bank Performance Report (UBPR)** is the FFIEC's analytical report: it turns each bank's
raw Call Report into a standardized set of **derived ratios** (`UBPR####` concepts), each defined by
an official formula over Call items and/or other UBPR intermediates. v10.0 acquired the **official CDR
XBRL UBPR taxonomy v181** and the **FFIEC UBPR User's Guide (v181)**, parsed **4,207 derivation
formulas with zero silent drops**, and **empirically validated the 31 headline ratios** by recomputing
each from Call/UBPR inputs and comparing to the **real published UBPR value**, bank-quarter by
bank-quarter, over **2015 Q1 – 2026 Q1** (up to ~44,000 bank-quarters per ratio). **All 31 validated
at 99.77–100%.** The deep companion is [docs/UBPR_GUIDE.md](UBPR_GUIDE.md); the concept catalogue is
[`csv/UBPR_CONCEPTS.csv`](../csv/UBPR_CONCEPTS.csv) (4,099 concepts; 2,186 with derivations).

| UBPR code | ratio | derivation (normalized) | agreement |
|---|---|---|---:|
| `UBPRE013` | Return on assets (ROA) | `100 · RIAD4340 / UBPRD659`, annualized | 99.79% |
| `UBPRE630` | Return on equity (ROE) | `100 · RIAD4340 / UBPRD342`, annualized | 99.77% |
| `UBPRE018` | Net interest margin (TE) | `100 · UBPR4074 / UBPRD362`, annualized | 99.77% |
| `UBPRE088` | Efficiency ratio | `100 · UBPRE037 / UBPRE036` | 100.0% |
| `UBPRE006` | Provision / avg assets | `100 · UBPRD483 / UBPRD659`, annualized | 99.87% |
| `UBPRE019` | Net loss / avg total loans | `100 · UBPR1795 / UBPRE386`, annualized | 99.93% |
| `UBPRE541` | 90+ days past due / gross loans | `100 · UBPRD667 / UBPRE131` | 100.0% |
| `UBPRE542` | Nonaccrual / gross loans | `100 · UBPRD669 / UBPRE131` | 100.0% |
| `UBPR7414` | Noncurrent loans / gross loans | `100 · UBPR1400 / UBPRE131` | 100.0% |
| `UBPRE523` | Loss allowance / total loans | `100 · UBPRD095 / UBPRD146` | 100.0% |
| `UBPRE024` | Net loans & leases / total assets | `100 · UBPRE119 / UBPR2170` | 100.0% |
| `UBPRD486` | Tier 1 leverage ratio | regulator passthrough (±0.5 pp) | 100.0%* |
| `UBPRD487` | Tier 1 risk-based capital ratio | regulator passthrough (±0.5 pp) | 100.0%* |
| `UBPRD488` | Total risk-based capital ratio | regulator passthrough (±0.5 pp) | 100.0%* |

`*` capital ratios are regulator passthroughs stored 2-decimal-rounded as a fraction; they validate
as the documented `×100` relationship within the ±0.5 pp rounding band.

### Three findings from the UBPR work

The validation was not a rubber stamp; calibrating it surfaced conventions and caption errors that a
naïve reading gets wrong (full method in [docs/UBPR_GUIDE.md](UBPR_GUIDE.md)):

1. **Units and annualization.** Call dollar items (`RIAD/RCON/…`) are in **thousands**, while UBPR
   average/level concepts (`UBPRD659`) are in **dollars** — a ratio mixing the two must divide the
   UBPR value by 1,000. Year-to-date flows annualize by **×(4/q)** (Q1 ×4, Q2 ×2, Q3 ×4⁄3, Q4 ×1).
   Both were calibrated empirically on ROA and then held unchanged across every family.

2. **The taxonomy's presentation captions mislabel some concepts — the User's Guide is
   authoritative.** `UBPR7408` is captioned in a way that reads like a capital ratio but the User's
   Guide makes clear it is a **12-month growth rate** ("Tier One Capital 12-month growth rate"), as is
   `UBPRE635`. They validate as parsed but must not be read as adequacy measures.

3. **Capital ratios are regulator passthroughs, stored 2-dp rounded.** `UBPRD486/487/488` are not
   recomputed from RC-R primitives (RWA is a complex regulatory computation outside this scope); they
   are the regulator-reported ratios, and `UBPRD48x = UBPR720x × 100` holds within the ±0.5 pp
   fraction-rounding band.

---

## Intraseries (period-over-period) edits

A class of official edits is not cross-sectional but **temporal**: a year-to-date flow should be
monotone non-decreasing across the quarters of a reporting year (Q1 ≤ Q2 ≤ Q3 ≤ Q4). These cannot
be tested by a single-row aggregate; they require comparing a filing to the same filer's previous
quarter. We tested **63** such FR Y-9C YTD-monotonicity edits with a `LAG()` window over the filing
history: **62 CONFIRMED + 1 CONFIRMED_CURRENT**, all passing ≥99.7% (the small tail is amended
filings, within tolerance). A further **221** intraseries edits are documented as
**CONDITIONAL_DOC** — they apply only within a reporting sub-population and are not unconditional
monotonicity identities.

---

## Adversarial rigor — testing our own tester

The v8.0 adjudication caught a harness parse-bug where `A − (B + C)` was evaluated as `A + B + C`
(a dropped distributed-negation). v9.0 caught a **second silent parser hazard of the same family**:
the side-parser tokenized only `+` and `-`, so a **multiplication was silently dropped** —
`X = Y * 0` was read as `X = Y`. The concrete case was the official 0%-conversion credit-equivalent
edit `RCFDS541 = RCFDS540 * 0`, which the buggy parse evaluated as `S541 = S540` (≈0.35–0.67 pass)
when the official edit simply requires `S541 = 0`. Rewriting the affected registry expressions to
the faithful form re-tested at **1.0000** (`REL_5717`, `REL_5718`). This continues the v8.0 pattern
of adversarially testing our own tester: a failing empirical result is tracked to its true source
before any verdict is recorded.

---

## OFFICIAL_EDIT_UNMET — eight edits kept as findings

Eight official edits do **not** hold even on the correct window, population, and all-components-
reported subset. We keep them deliberately, as research findings about how the official edit set
behaves against real public data rather than deleting them. The eighth was surfaced by the v10.0
conditional engine: a second **RCON-side phantom decomposition** of the same family as the headline
case below — an official decomposition whose child codes have no public observations, so it is
documented and not enforced. The two headline cases:

1. **A phantom decomposition.** The official calculation linkbase decomposes `RCONM288` into
   `RCONL191 + RCONL192` — but `L191` and `L192` have **zero observations warehouse-wide** in the
   public bulk data, while `M288` (51,992 filings) is reported directly. The decomposition is not
   empirically derivable from anything public; we document it and do not enforce it.

2. **A securitization bound that mostly fails among the population it's about.** An RC-R Part II
   securitization bound (`R7020.6507`) holds at a headline 0.983 — but that rate is dominated by
   zero-filers (banks with no securitization, for whom both sides are 0). Among **active
   securitizers** (the population the edit is actually about, n=3,493) it holds at only **0.452**: a
   real, substantial explained-violation population.

The remaining five are soft "should-be" quality edits (an RC-O brokered-deposit bound at 0.71 and
four RI-C/RC-C CECL loan-category bounds at 0.66–0.94) whose violation rates are themselves the
finding.

---

## Limitations (read these)

This validation is rigorous **within its scope**, and that scope has edges worth stating plainly.

- **The `not_testable` class is honest, not hidden.** 4,412 registry rows are non-arithmetic
  official edits — completeness/null tests, string value-domain checks, conditional edits, and
  function edits — that cannot be expressed as a linear identity over reported values. They are
  labelled by class, not asserted as confirmed.

- **"Should" edits are not "must" edits.** The 36 **QUALITY_TOLERANCE** relationships are valid
  economic bounds or regulator "should"-class edits — flagged for review but not filing-rejecting.
  Their published pass rates (≈0.94–0.985) are real and the small tails are explained (minority
  interest, netting, securitization tail, allowance-vs-balance timing), not data errors.

- **DATA_GAP is sparse data, not a broken identity.** The 48 **DATA_GAP** rows are official
  calculation-linkbase identities that hold perfectly where the full component breakdown is
  reported (`allcomp ≈ 1.0000`) but "fail" in bulk because filers report the parent total and leave
  many child line-items blank, and coalesce-to-zero then makes parent ≠ partial-sum. The
  calculation is correct; the public data is sparse.

- **NOT_IN_BULK is documented, not "tested away".** The 134 **NOT_IN_BULK** rows reference codes
  that are text/confidential/narrative items never published in bulk, or that were renumbered/retired
  across the window, so the two sides never co-occur.

- **Vintage matters.** The 83 **CONFIRMED_CURRENT** relationships hold for today's forms but not
  uniformly back to the start of the window, because both forms have been re-laid-out many times.
  Each is confirmed for the regime in which its codes are actually collected; the 30 archived
  historical taxonomy cycles let us align edits to filing vintage.

---

## Reproducing this

Everything needed to reproduce the verdicts is public:

- The **[Relationship Registry](data/relationship_registry.md)** — every relationship, its
  expression, source (official edit id and/or calculation-linkbase parent), status, observation
  count (`empirical_n`), pass rate (`empirical_pass_rate`), and test window — is in
  [`csv/RELATIONSHIP_REGISTRY.csv`](https://raw.githubusercontent.com/andenick/bank-data-dictionary/main/csv/RELATIONSHIP_REGISTRY.csv).
- The bulk **FR Y-9C (BHCF)** and **Call Report** filings are published by the Federal Reserve /
  FFIEC and are downloadable and queryable via the companion
  **[FreeNIC](https://github.com/andenick/FreeNIC)** package.
- The official edits are the **FFIEC Call Report edit checks and calculation linkbases, distributed
  in the CDR XBRL taxonomy (cdr.ffiec.gov)** and the FR Y-9C edit checklist.
- `scripts/validate_reconciliation.py` evaluates the registry against any supplied filing; use
  `--scope {y9c,call,all,ubpr}` to select the filing universe. Token validity is additionally
  CI-enforced by `scripts/ci_audit.py`, which fails the build on any invalid token.

Take any `CONFIRMED` row, evaluate its expression against the bulk filings with a
`max($1,000, 0.1%)` tolerance, and you will recover its published pass rate.
