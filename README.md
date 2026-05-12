# Bank Regulatory Data Dictionary

**A comprehensive, downloadable reference for U.S. bank regulatory filings data — MDRM codes, form mappings, reconciliation formulas, and detailed guides for every FR Y-9C schedule.**

**Version 5.0** | Updated: 2026-01-29

---

## Why This Exists

Bank regulatory filings (FR Y-9C, Call Reports, DFAST, Pillar 3) use thousands of MDRM variable codes across dozens of schedules. Analysts spend hours mapping between forms, deciphering code prefixes, and verifying that balance sheet components actually add up. This repository puts all of that reference material in one place — as CSV tables for programmatic use, JSON schemas for AI agents, and Markdown guides for human readers.

---

## Quick Start

```bash
git clone https://github.com/andenick/bank-data-dictionary.git
cd bank-data-dictionary
```

No installation required — all data is in CSV, JSON, and Markdown files ready to use.

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
| 5 | Tier 1 Capital | BHCFA223 = BHCAP859 + BHCAP856 | CRITICAL |
| 6 | Total Capital | BHCFA225 = BHCFA223 + BHCFA224 | CRITICAL |
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
│   ├── MDRM_MASTER_COMPLETE.csv            # Master variable crosswalk (400+ vars)
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
│   └── Reference Files:
│       ├── MDRM_PREFIX_DEFINITIONS.csv     # BHCK, RCFD, etc.
│       ├── FORM_HIERARCHY.csv              # Form relationships
│       ├── GSIB_ENTITY_IDENTIFIERS.csv     # Bank identifiers
│       └── HISTORICAL_CODE_TRANSITIONS.csv # Legacy codes
│
├── docs/                                   # Documentation (33 guides)
│   ├── INDEX.md                            # Master navigation (NEW v5.0)
│   ├── RECONCILIATION_HIERARCHY.md         # What adds up to what (NEW v5.0)
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
│   ├── schedule_schemas.json               # Schedule structures (NEW v5.0)
│   ├── cross_form_mapping.json             # Concept mapping (NEW v5.0)
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
| BHCK | FR Y-9C | Bank-level item |
| BHCM | FR Y-9C | Domestic offices |
| BHCT | FR Y-9C | Total (domestic + foreign) |
| BHCAP | FR Y-9C | Capital items (Part I) |
| BHCFA | FR Y-9C | Capital Tier items |
| RCFD | Call Report | Total |
| RCON | Call Report | Domestic |
| RIAD | Call Report | Income statement |

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
    'tier1': 'BHCFA223',
    'total_capital': 'BHCFA225',
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
| FFIEC CDR | https://cdr.ffiec.gov/ | Call Reports, Y-9C |
| MDRM Dictionary | https://www.federalreserve.gov/apps/mdrm/ | Official definitions |
| Fed NIC | https://www.ffiec.gov/NPW/ | Organization data |
| FDIC BankFind | https://banks.data.fdic.gov/ | Bank financials |

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
| **5.0** | 2026-01-29 | Complete reconciliation system (60+ formulas), validation rules (50), schedule schemas JSON, cross-form mapping JSON, component hierarchies, 5 Call Report guides, INDEX.md, RECONCILIATION_HIERARCHY.md |
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
