# How the Official Call Report Rules Changed, 2001–2026

**Source**: the official FFIEC Call Report edit checks, as distributed in the CDR XBRL taxonomy
(cdr.ffiec.gov), parsed from **30 reporting cycles** — every year-end 2001–2024 plus all
2025–2026 quarters, forms 031/041/051. Machine-readable lifetimes:
[`csv/EDIT_HISTORY.csv`](../csv/EDIT_HISTORY.csv) (one row per edit label: rule type, forms,
first/last cycle observed, number of expression revisions).

## Headline numbers

| Metric | Value |
|---|---|
| Distinct edit labels observed, 2001–2026 | **15,622** |
| Retired before the current (2026 Q1) cycle | **4,759** |
| Introduced 2020 or later | **1,212** |
| Edit count, 2001 year-end (validity + quality, all forms) | ~2,450 |
| Edit count, 2025 Q1 (validity + quality, all forms) | ~11,000 |

The official rulebook roughly **quintupled in 25 years**. Growth is concentrated in
quality ("should"-hold) edits, which outnumber validity ("must"-hold) edits about 2.5:1
throughout.

## Eras visible in the data

- **2001–2007 — steady state.** A compact rulebook (~2,400–4,400 edits) with incremental
  growth as schedules gained detail.
- **2008–2013 — crisis buildout.** Past-due/nonaccrual, securitization, and fair-value
  reporting drove sustained additions (~4,400 → ~6,600).
- **2014–2019 — Basel III spike.** The regulatory-capital rewrite (RC-R Parts I/II) is the
  single largest event in the series: validity edits jump from ~2,100 to ~3,300 and the
  total passes 11,000 by 2019. Hundreds of pre-Basel capital edits retire simultaneously.
- **2020–2022 — CECL and pandemic.** ASU 2016-13 allowance edits replace incurred-loss
  edits; temporary PPP-related items arrive and depart within a few cycles (visible as
  short edit lifetimes).
- **2023–2026 — refinement.** Net edit count plateaus; revisions shift to expression
  changes within continuing labels rather than new labels.

## How to use this with the relationship registry

Every Call-scope row in [`csv/RELATIONSHIP_REGISTRY.csv`](../csv/RELATIONSHIP_REGISTRY.csv)
that derives from an official edit carries a `first_official_cycle` column joined from this
history. A registry row whose empirical verdict is `CONFIRMED_CURRENT` (holds ≥99% in recent
data but not across full history) can now be read against the cycle in which its rule first
appeared — in the cases sampled, the empirical window aligns with the rule's official
lifetime, i.e. the data "fails" the rule only in quarters before the rule existed.

## Caveats

- Lifetimes are observed at the sampled cycles (every year-end 2001–2024, plus all
  2025–2026 quarters). An edit introduced and retired between two year-ends would carry
  slightly conservative first/last dates.
- Edit labels are the taxonomy's stable identifiers; a relabeled rule appears as one
  retirement plus one introduction.
- Counts aggregate the three forms; an edit shared by all forms counts once per label but
  its per-cycle totals reflect each form's edit file.
