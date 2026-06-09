# Bank Regulatory Data Dictionary

**The most detailed open catalogue of U.S. bank regulatory data — every major information collection and its subschedules, the MDRM code system, the FFIEC NIC institutional-structure data, the identifier crosswalk, cross-form mappings, and reconciliation formulas.**

**Version 6.1** | Updated: 2026-06-09

> This repository is a **catalogue / mapping reference** — it documents *what the datasets are, how they are structured, and how they relate to each other*. For a data-*access* package (download and query the actual filings), see the companion project **[FreeNIC](https://github.com/andenick/FreeNIC)**.

---

## Why This Exists

U.S. bank regulators run dozens of overlapping data collections — FR Y-9C, the Call Report (FFIEC 031/041/051), FFIEC 101/102/002/009, the FR Y-7/Y-10/Y-11/Y-12/Y-14/Y-15 family, FR 2052a, Pillar 3, plus FDIC (SDI/SOD/failures), NCUA 5300, OCC historical returns, and the NIC/NPW structure files — together using **tens of thousands of MDRM variable codes across hundreds of schedules**. Analysts spend hours mapping between forms, deciphering code prefixes, tracing corporate hierarchies, reconciling identifiers, and verifying that balance-sheet components actually add up. This repository puts all of that reference material in one place — as CSV tables for programmatic use, JSON for AI agents, and Markdown guides for human readers.

**What v6.0 adds over the original FR Y-9C/trading focus:** a master [collections catalogue](docs/COLLECTIONS_CATALOG.md) of **42 collections** with a [schedule catalogue](csv/SCHEDULES_CATALOG.csv) of every subschedule; the full [FFIEC NIC institutional-structure layer](docs/NIC_STRUCTURE_GUIDE.md) (entities, relationships, transformations, 40+ code lists); an [identifier crosswalk](docs/IDENTIFIERS.md) (RSSD / FDIC Cert / OCC / NCUA / LEI / ABA / EIN / CIK); the complete [Call Report](docs/CALL_REPORT_GUIDE.md), [foreign/structure](docs/FOREIGN_AND_STRUCTURE_GUIDE.md), and [FDIC/NCUA/OCC/UBPR](docs/FDIC_NCUA_OCC_UBPR_GUIDE.md) guides; and an [MDRM meta-dictionary](docs/MDRM_GUIDE.md) + namespace catalogue.

---

## Get the Repo

```bash
git clone https://github.com/andenick/bank-data-dictionary.git
cd bank-data-dictionary
```

No installation required — all data is in CSV, JSON, and Markdown files ready to use. Start with [`docs/NAVIGATION.md`](docs/NAVIGATION.md) for navigation or [`docs/COLLECTIONS_CATALOG.md`](docs/COLLECTIONS_CATALOG.md) for the full data universe.

---

## What Adds Up to What

```
                    TOTAL ASSETS (BHCT2170)
                           |
    +----------+-----------+-----------+-----------+----------+
    |          |           |           |           |          |
  Cash      Securities    Loans     Trading    Other Assets
 (0081)     (8641)       (B528)     (3545)      (2160)
              |            |           |           |
           HC-B         HC-C        HC-D        HC-F
              |            |           |
         AFS + HTM    Net Loans   Assets + Deriv
           1773+        B529      Pos FV 3543
           JJ34                       |
                                    HC-L
                               (FV by Asset Class)

                    TOTAL LIABILITIES (BHCT2948)
                           |
    +----------+-----------+-----------+-----------+
    |          |           |           |           |
 Deposits   Fed Funds   Trading    Other      Borrowings
  (2200)    Purchased    Liab      Liab       (3190)
              (B993)    (3548)    (2930)
                          |         |
                        HC-D      HC-G
                          |
                    Shorts + Deriv
                     Neg FV 3547

                    TOTAL EQUITY (BHCT3210)
                           |
         +--------+--------+--------+--------+
         |        |        |        |        |
      Preferred Common  Surplus  Retained  AOCI
       (3838)   (3230)  (3839)   (3632)   (B530)

                REGULATORY CAPITAL
                    (HC-R)
         +----------+----------+
         |                     |
    TIER 1 (FA223)      TIER 2 (FA224)
         |
    +----+----+
    |         |
  CET1      AT1
 (P859)    (P856)
```

---

## Quick Start

### For Analysts

1. **Need MDRM codes?** Start with `csv/MDRM_MASTER_COMPLETE.csv`
2. **Analyzing specific schedules?** See schedule-specific guides in `docs/`
3. **Understanding form relationships?** See `docs/MASTER_REGULATORY_GUIDE.md`
4. **Validating data?** Check `docs/RECONCILIATION_HIERARCHY.md`

### For AI Agents

1. **Programmatic access to schedules** → `json/schedule_schemas.json`
2. **Cross-form concept mapping** → `json/cross_form_mapping.json`
3. **Validation rules for data quality** → `csv/VALIDATION_RULES.csv`
4. **Full regulatory taxonomy** → `json/data_taxonomy.json`

### For Data Engineers

1. **Reconciliation formulas** → `csv/RECONCILIATION_FORMULAS_COMPLETE.csv`
2. **Component hierarchies** → `csv/SCHEDULE_COMPONENT_HIERARCHY.csv`
3. **Form data flow** → `csv/FORM_REPORTING_HIERARCHY.csv`
4. **Validation test cases** → `csv/VALIDATION_TEST_CASES.csv`

---

## Reconciliation Quick Reference

### Top 10 Critical Checks

| # | Check | Formula | Priority |
|---|-------|---------|----------|
| 1 | Balance Sheet | BHCT2170 = BHCT2948 + BHCK3000 + BHCT3210 | CRITICAL |
| 2 | Trading Assets | BHCT3545 (HC) = BHCT3545 (HC-D) | CRITICAL |
| 3 | Trading Liabilities | BHCT3548 (HC) = BHCT3548 (HC-D) | CRITICAL |
| 4 | Loans Net | BHCTB528 (HC) = BHCTB529 (HC-C) | CRITICAL |
| 5 | Tier 1 Capital | BHCA8274 = BHCAP859 + BHCAP856 | CRITICAL |
| 6 | Total Capital | BHCA3792 = BHCA8274 + BHCA5311 | CRITICAL |
| 7 | Derivatives +FV | BHCT3543 = Sum(HC-L Positive FV) | CRITICAL |
| 8 | Derivatives -FV | BHCT3547 = Sum(HC-L Negative FV) | CRITICAL |
| 9 | Securities | BHCT8641 = BHCT1773 + BHCTJJ34 | HIGH |
| 10 | NII | BHCT4074 = BHCT4107 - BHCT4073 | HIGH |

---

## Repository Structure

```
bank-regulatory-data-dictionary/
│
├── csv/                                    # All CSV data tables
│   ├── MDRM_MASTER_COMPLETE.csv            # Curated cross-form concept spine (~100 concepts)
│   ├── MDRM_CROSSWALK_EXPANDED.csv         # 677 MDRM-verified codes w/ cross-scope mapping (NEW v6.1)
│   │
│   ├── Schedule-Specific Files (14 Y-9C schedules):
│   │   ├── HC_BALANCE_SHEET.csv            # Schedule HC master balance sheet
│   │   ├── HC_B_SECURITIES.csv             # Schedule HC-B securities
│   │   ├── HC_C_LOANS.csv                  # Schedule HC-C loans
│   │   ├── HC_D_TRADING_ASSETS.csv         # Schedule HC-D trading
│   │   ├── HC_F_OTHER_ASSETS.csv           # Schedule HC-F other assets
│   │   ├── HC_G_OTHER_LIABILITIES.csv      # Schedule HC-G other liabilities
│   │   ├── HC_H_INTEREST_SENSITIVITY.csv   # Schedule HC-H repricing
│   │   ├── HC_K_QUARTERLY_AVERAGES.csv     # Schedule HC-K averages
│   │   ├── HC_L_DERIVATIVES.csv            # Schedule HC-L derivatives
│   │   ├── HC_N_PAST_DUE.csv               # Schedule HC-N past due
│   │   ├── HC_Q_FAIR_VALUE.csv             # Schedule HC-Q fair value
│   │   ├── HC_R_CAPITAL.csv                # Schedule HC-R capital
│   │   ├── HC_S_SECURITIZATION.csv         # Schedule HC-S securitization
│   │   └── HI_INCOME_STATEMENT.csv         # Schedule HI income
│   │
│   ├── Advanced Forms (~5,000 items):
│   │   ├── FFIEC_101_ADVANCED_CAPITAL.csv  # Advanced approaches capital
│   │   ├── FFIEC_102_MARKET_RISK.csv       # Market risk VaR/sVaR
│   │   ├── FR_Y15_SYSTEMIC_RISK.csv        # G-SIB systemic risk
│   │   ├── FR_Y9LP_PARENT_ONLY.csv         # Parent company only
│   │   ├── FFIEC_009_COUNTRY_EXPOSURE.csv  # Country exposure
│   │   └── FR_Y11_FOREIGN_SUBSIDIARY.csv   # Foreign subsidiary
│   │
│   ├── New Files (v4.0-5.0):
│   │   ├── FR_Y14A_SCHEDULES.csv           # Y-14A stress testing
│   │   ├── FR_Y14Q_SCHEDULES.csv           # Y-14Q quarterly
│   │   ├── FR_2052a_PRODUCT_HIERARCHY.csv  # Liquidity monitoring
│   │   ├── PILLAR3_GSIB_DISCLOSURE.csv     # Pillar 3 disclosure
│   │   ├── RECONCILIATION_FORMULAS_COMPLETE.csv  # 60+ reconciliations (NEW v5.0)
│   │   ├── VALIDATION_RULES.csv            # 50 validation rules (NEW v5.0)
│   │   ├── SCHEDULE_COMPONENT_HIERARCHY.csv # Component hierarchies (NEW v5.0)
│   │   └── FORM_REPORTING_HIERARCHY.csv    # Form data flow (NEW v5.0)
│   │
│   ├── Catalogue & Structure (NEW v6.0):
│   │   ├── COLLECTIONS_CATALOG.csv         # All 42 collections
│   │   ├── SCHEDULES_CATALOG.csv           # Every subschedule (265 rows)
│   │   ├── NIC_ATTRIBUTES_SCHEMA.csv       # NIC entity attributes (74 fields)
│   │   ├── NIC_RELATIONSHIPS_SCHEMA.csv    # NIC relationships (22 fields)
│   │   ├── NIC_TRANSFORMATIONS_SCHEMA.csv  # NIC mergers/failures (6 fields)
│   │   ├── NIC_CODE_LISTS.csv              # 40 NIC code lists (274 codes)
│   │   ├── IDENTIFIERS.csv                 # Identifier systems crosswalk
│   │   └── MDRM_NAMESPACES.csv             # Full mnemonic namespace catalogue
│   │
│   └── Reference Files:
│       ├── MDRM_PREFIX_DEFINITIONS.csv     # BHCK (consolidated), RCFD, etc.
│       ├── FORM_HIERARCHY.csv              # Form relationships
│       ├── GSIB_ENTITY_IDENTIFIERS.csv     # Bank identifiers
│       └── HISTORICAL_CODE_TRANSITIONS.csv # Legacy codes
│
├── docs/                                   # Documentation (43 guides)
│   ├── index.md                            # Site landing page (GitHub Pages home)
│   ├── NAVIGATION.md                       # Master navigation
│   ├── COLLECTIONS_CATALOG.md              # The full data universe — 42 collections (NEW v6.0)
│   ├── NIC_STRUCTURE_GUIDE.md              # FFIEC NIC entities/relationships/transformations (NEW v6.0)
│   ├── IDENTIFIERS.md                      # RSSD/FDIC/OCC/NCUA/LEI/ABA/EIN/CIK crosswalk (NEW v6.0)
│   ├── CALL_REPORT_GUIDE.md                # Complete FFIEC 031/041/051 (NEW v6.0)
│   ├── FOREIGN_AND_STRUCTURE_GUIDE.md      # FFIEC 002/009, FR Y-7/10/11/12/6/8 (NEW v6.0)
│   ├── FDIC_NCUA_OCC_UBPR_GUIDE.md         # Non-Fed collections + UBPR (NEW v6.0)
│   ├── MDRM_GUIDE.md                       # MDRM meta-dictionary + namespaces (NEW v6.0)
│   ├── COVERAGE_PROVENANCE.md              # Temporal coverage & vintages (NEW v6.0)
│   ├── RECONCILIATION_HIERARCHY.md         # What adds up to what
│   ├── MASTER_REGULATORY_GUIDE.md          # Comprehensive reference
│   ├── RECONCILIATION_MATRIX.md            # Cross-schedule tie-outs
│   │
│   ├── Schedule Guides (14 Y-9C + 5 Call Report):
│   │   ├── HC_BALANCE_SHEET_GUIDE.md       # Through HC_S and HI
│   │   ├── CALL_REPORT_RC_GUIDE.md         # (NEW v5.0)
│   │   ├── CALL_REPORT_RC_C_LOANS_GUIDE.md # (NEW v5.0)
│   │   ├── CALL_REPORT_RC_E_DEPOSITS_GUIDE.md # (NEW v5.0)
│   │   ├── CALL_REPORT_RC_N_PAST_DUE_GUIDE.md # (NEW v5.0)
│   │   └── CALL_REPORT_RI_INCOME_GUIDE.md  # (NEW v5.0)
│   │
│   └── Advanced Form Guides:
│       ├── FR_Y14_CAPITAL_ASSESSMENT_GUIDE.md
│       ├── FR_2052a_LIQUIDITY_GUIDE.md
│       └── PILLAR3_DISCLOSURE_GUIDE.md
│
├── json/                                   # Machine-readable data
│   ├── collections.json                    # All 42 collections (NEW v6.0)
│   ├── identifiers.json                     # Identifier systems (NEW v6.0)
│   ├── schedule_schemas.json               # Schedule structures
│   ├── cross_form_mapping.json             # Concept mapping
│   ├── data_taxonomy.json                  # Full regulatory taxonomy
│   └── schedule_correspondence.json        # Cross-schedule linkages
│
├── scripts/                                # Validation scripts (NEW v5.0)
│   └── validate_reconciliation.py          # Python validation template
│
├── README.md                               # This file
└── LICENSE                                 # MIT License
```

---

## Key Concepts

### MDRM Codes Explained

```
BHCT3545
│  │ │──│
│  │   │
│  │   └── Item number (3545 = Trading Assets)
│  │
│  └────── Form/Scope code (T = total consolidated)
│
└───────── Prefix (BHC = Bank Holding Company)
```

**Common Prefixes:**

| Prefix | Form | Scope |
|--------|------|-------|
| BHCK | FR Y-9C | **Consolidated** (domestic + foreign) — the primary Y-9C series |
| BHDM | FR Y-9C | Domestic offices only |
| BHFN | FR Y-9C | Foreign offices only |
| BHCP | FR Y-9LP | Parent company only (large) |
| BHSP | FR Y-9SP | Parent company only (small) |
| BHCA | FR Y-9C | Consolidated regulatory capital (HC-R) |
| RCFD | Call Report | Consolidated (domestic + foreign) |
| RCON | Call Report | Domestic offices only |
| RCFN | Call Report | Foreign offices only |
| RIAD | Call Report / FR Y-9C | Income statement (year-to-date) |

> **Correction (v6.0):** earlier releases mislabeled `BHCK` as "domestic only." `BHCK` is the **consolidated** series; domestic-only is `BHDM` and foreign-only is `BHFN` (confirmed against the Federal Reserve MDRM). See [`docs/MDRM_GUIDE.md`](docs/MDRM_GUIDE.md) and [`csv/MDRM_NAMESPACES.csv`](csv/MDRM_NAMESPACES.csv) for the full namespace catalogue.

---

## For AI Agents

### JSON Schema Structure

```python
import json

# Load schedule schemas
with open('json/schedule_schemas.json') as f:
    schemas = json.load(f)

# Access HC balance sheet structure
for item in schemas['HC']['line_items']:
    print(f"{item['item']}: {item['mdrm']} - {item['name']}")
    if item.get('reconciliation'):
        print(f"  Reconciliation: {item['reconciliation']}")
```

### Cross-Form Mapping

```python
# Load cross-form mapping
with open('json/cross_form_mapping.json') as f:
    mapping = json.load(f)

# Find same concept across forms
total_assets = mapping['concepts']['total_assets']
print(f"Y-9C: {total_assets['forms']['FR_Y9C']['mdrm']}")  # BHCT2170
print(f"Call: {total_assets['forms']['Call_Report_031']['mdrm']}")  # RCFD2170
```

### Validation Rules

```python
import pandas as pd

# Load validation rules
rules = pd.read_csv('csv/VALIDATION_RULES.csv', comment='#')

# Get critical balance sheet rules
critical_rules = rules[rules['severity'] == 'CRITICAL']
for _, rule in critical_rules.iterrows():
    print(f"{rule['rule_id']}: {rule['description']}")
```

---

## Common Use Cases

### 1. Bank Financial Model

```python
# Core balance sheet items
balance_sheet = {
    'total_assets': 'BHCT2170',
    'total_loans': 'BHCTB528',
    'securities': 'BHCT8641',
    'trading_assets': 'BHCT3545',
    'deposits': 'BHCT2200',
    'total_equity': 'BHCT3210',
}

# Income statement items
income = {
    'interest_income': 'BHCT4107',
    'interest_expense': 'BHCT4073',
    'net_interest_income': 'BHCT4074',
    'provision': 'BHCT4230',
    'net_income': 'BHCT4340',
}
```

### 2. Capital Analysis

```python
# Regulatory capital
capital = {
    'cet1': 'BHCAP859',
    'tier1': 'BHCA8274',
    'total_capital': 'BHCA3792',
    'rwa': 'BHCAA223',
}

# Ratios
cet1_ratio = capital['cet1'] / capital['rwa']  # Min 4.5%
tier1_ratio = capital['tier1'] / capital['rwa']  # Min 6.0%
total_ratio = capital['total_capital'] / capital['rwa']  # Min 8.0%
```

### 3. Asset Quality

```python
asset_quality = {
    'npl_total': 'BHCK1403',        # Nonaccrual
    'past_due_30_89': 'BHCK5524',   # 30-89 days
    'past_due_90_plus': 'BHCK5525', # 90+ days
    'allowance': 'BHCT3123',        # ALLL
}

# NPL Ratio = (Nonaccrual + 90+ DPD) / Total Loans
```

---

## Data Sources

| Source | URL | Content |
|--------|-----|---------|
| FFIEC CDR | https://cdr.ffiec.gov/ | Call Reports, FR Y-9C, FFIEC 101/102/002/009 |
| MDRM Dictionary | https://www.federalreserve.gov/apps/mdrm/ | Official variable definitions (~87,000+ codes) |
| Fed Reporting Forms | https://www.federalreserve.gov/apps/reportingforms/ | FR Y-series forms + instructions |
| Fed NIC / NPW | https://www.ffiec.gov/NPW/ | Institutional structure, relationships, transformations |
| FDIC BankFind | https://banks.data.fdic.gov/ | SDI financials, SOD, failures, locations |
| NCUA | https://ncua.gov/analysis/credit-union-corporate-call-report-data | 5300 credit-union Call Reports (FS220) |
| FRASER (OCC) | https://fraser.stlouisfed.org/ | Historical OCC national-bank reports (1863–1941) |

---

## Companion Project: FreeNIC

This repository is the **catalogue / mapping** product. Its sibling, **[FreeNIC](https://github.com/andenick/FreeNIC)**, is the **data-access** package — it lets you download and query ~2.3 billion rows of the actual filings (1863–2026) via Python/SQL. Use this repo to understand *what the data is and how it fits together*; use FreeNIC to *get and query it*.

---

## Major Trading BHCs

| Entity | RSSD ID | 2024Q4 Assets |
|--------|---------|---------------|
| JPMorgan Chase | 1039502 | $3.9T |
| Bank of America | 1073757 | $3.3T |
| Citigroup | 1951350 | $2.4T |
| Wells Fargo | 1120754 | $1.9T |
| Goldman Sachs | 2380443 | $1.7T |
| Morgan Stanley | 2162966 | $1.2T |

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| **6.1** | 2026-06-09 | **Capital-code correction + crosswalk expansion + docs site.** Fixed the non-existent `BHCFA223/224/225` codes repo-wide → verified `BHCA8274` (Tier 1) / `BHCA5311` (Tier 2) / `BHCA3792` (Total). Resolved prefix scopes against the full Fed MDRM (BHCT/BHCM/BHCB verified; BHCAP/BHCFA shown to be non-mnemonics = `BHCA`+item). Added `MDRM_CROSSWALK_EXPANDED.csv` (677 MDRM-verified codes with cross-scope mapping). Resolved FFIEC 002/009 Schedule C Part II titles + CIK↔RSSD note. Added a MkDocs Material GitHub Pages site. |
| **6.0** | 2026-06-09 | **Major expansion from FR Y-9C focus to the full U.S. bank-data universe.** Added: master Collections Catalogue (42 collections) + Schedules Catalogue (every subschedule); FFIEC NIC institutional-structure layer (entity/relationship/transformation schemas + 40 code lists, 274 codes); identifier crosswalk (RSSD/FDIC/OCC/NCUA/LEI/ABA/EIN/CIK); complete Call Report (031/041/051) guide; foreign/structure guide (FFIEC 002/009, FR Y-7/10/11/12/6/8); FDIC/NCUA/OCC/UBPR guide; MDRM meta-dictionary + namespace catalogue; coverage/provenance guide. **Fixed:** BHCK mislabel (it is consolidated, not domestic); FR Y-11 and FFIEC 009 schedule lists; cross-form line-item references. |
| 5.0 | 2026-01-29 | Complete reconciliation system (60+ formulas), validation rules (50), schedule schemas JSON, cross-form mapping JSON, component hierarchies, 5 Call Report guides, INDEX.md, RECONCILIATION_HIERARCHY.md |
| 4.0 | 2026-01-29 | Added Y-14A/Q, 2052a hierarchy, Pillar 3 G-SIB disclosure |
| 3.0 | 2026-01-29 | Added FFIEC 101/102, FR Y-15/Y-9LP/Y-11, FFIEC 009 |
| 2.1 | 2026-01-28 | Market risk/trading analysis |
| 2.0 | 2026-01-28 | Comprehensive schedule coverage (14 schedules) |
| 1.0 | 2026-01-28 | Initial release with trading focus |

---

## Contributing

This repository is maintained as a reference resource. Issues and suggestions are welcome.

## Citation

```bibtex
@software{bank_data_dictionary2026,
  title = {Bank Regulatory Data Dictionary},
  author = {Anderson, Nicholas},
  year = {2026},
  url = {https://github.com/andenick/bank-data-dictionary}
}
```

## License

MIT License — See [LICENSE](LICENSE) file for details.
