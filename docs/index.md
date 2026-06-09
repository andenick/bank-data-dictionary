# Bank Regulatory Data Dictionary

A catalogue and field-level mapping of the **U.S. bank regulatory data universe** — the
forms, schedules, codes and identifiers that banks and bank holding companies file with
the Federal Reserve, FFIEC, FDIC, NCUA and OCC. It exists to make these datasets
discoverable, joinable and machine-readable.

## What's inside

- **42 collections** spanning the full regulatory landscape (FR Y-9C, Call Report,
  FFIEC 009/101/102, FR Y-11/Y-14/Y-15/Y-9LP, FR 2052a, Pillar 3, FDIC/NCUA/OCC/UBPR).
- **265 subschedules** documented down to the line-item and MDRM-code level.
- **NIC structure** reference plus **40 code lists** describing bank corporate hierarchy.
- An **identifier crosswalk** reconciling RSSD, FDIC Cert, LEI and other entity keys.
- The **MDRM meta-dictionary** — the Micro Data Reference Manual code system that ties
  every field across every form together.

## Start here

- [Collections Catalog](COLLECTIONS_CATALOG.md) — the whole data universe at a glance.
- [MDRM Guide](MDRM_GUIDE.md) — how the universal code system works.
- [Identifiers](IDENTIFIERS.md) — reconciling entity identifiers across sources.
- [NIC Structure Guide](NIC_STRUCTURE_GUIDE.md) — bank corporate structure and code lists.

Looking for a specific schedule or concept? The [Navigation Index](NAVIGATION.md) maps
every form, schedule, concept and reconciliation check to its guide and data file.

## Machine-readable data

Every guide is backed by structured data. The repository ships the underlying **CSV** and
**JSON** files alongside this documentation:

- [`csv/`](https://github.com/andenick/bank-data-dictionary/tree/main/csv) — schedule
  catalogs, the MDRM master crosswalk, reconciliation formulas and validation rules.
- [`json/`](https://github.com/andenick/bank-data-dictionary/tree/main/json) — schedule
  schemas, cross-form mappings and the full data taxonomy for automated pipelines.

## Companion project

For programmatic **access** to the underlying filings (downloading and assembling the data
this dictionary describes), see the companion package
**[FreeNIC](https://github.com/andenick/FreeNIC)**.
