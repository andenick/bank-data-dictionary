# Bank Regulatory Data Dictionary

A comprehensive, downloadable reference for U.S. bank regulatory filings data, including MDRM codes, form mappings, reconciliation formulas, and detailed guides for trading and derivatives analysis.

## Quick Start

1. **Need MDRM codes?** Start with `csv/MDRM_MASTER_COMPLETE.csv`
2. **Analyzing trading activities?** Read `docs/TRADING_ACTIVITIES_GUIDE.md`
3. **Understanding form relationships?** See `docs/MASTER_REGULATORY_GUIDE.md`
4. **Building automated pipelines?** Use the JSON files in `json/`

## Repository Structure

```
bank-regulatory-data-dictionary/
|
+-- csv/                                 # All CSV data tables
|   +-- MDRM_MASTER_COMPLETE.csv         # Master variable crosswalk (100+ vars)
|   +-- HC_D_TRADING_ASSETS.csv          # HC-D schedule breakdown
|   +-- HC_L_DERIVATIVES.csv             # HC-L derivatives detail
|   +-- CALL_REPORT_RC_SCHEDULES.csv     # RC-D, RC-L, RC-B, RC-Q mappings
|   +-- Y14_SCHEDULE_MAP.csv             # FR Y-14 schedule reference
|   +-- PILLAR3_TEMPLATES.csv            # Basel III disclosure templates
|   +-- MDRM_PREFIX_DEFINITIONS.csv      # BHCK, RCFD, etc. explained
|   +-- RECONCILIATION_FORMULAS.csv      # What adds up to what
|   +-- FORM_HIERARCHY.csv               # Form relationships
|   +-- GSIB_ENTITY_IDENTIFIERS.csv      # Bank identifiers (RSSD, LEI)
|   +-- HISTORICAL_CODE_TRANSITIONS.csv  # Legacy vs current codes
|
+-- docs/                                # Detailed documentation
|   +-- MASTER_REGULATORY_GUIDE.md       # Comprehensive 50+ page guide
|   +-- TRADING_ACTIVITIES_GUIDE.md      # HC-D/HC-L deep dive
|
+-- json/                                # Machine-readable data
|   +-- data_taxonomy.json               # Full regulatory taxonomy
|   +-- schedule_correspondence.json     # Cross-schedule linkages
|
+-- README.md                            # This file
+-- LICENSE                              # MIT License
```

## Key Files Explained

### CSV Tables

| File | Description | Use Case |
|------|-------------|----------|
| `MDRM_MASTER_COMPLETE.csv` | All key variables with Y-9C, Call Report, Y-14, Pillar 3 mappings | Primary reference for variable lookups |
| `HC_D_TRADING_ASSETS.csv` | Complete HC-D schedule with current and legacy codes | Trading book analysis |
| `HC_L_DERIVATIVES.csv` | Complete HC-L schedule with notional and fair value items | Derivatives analysis |
| `RECONCILIATION_FORMULAS.csv` | Formulas showing what adds to what | Data validation |
| `HISTORICAL_CODE_TRANSITIONS.csv` | Track code changes over time | Time series construction |

### Documentation

| File | Pages | Content |
|------|-------|---------|
| `MASTER_REGULATORY_GUIDE.md` | ~50 | Full reference covering all forms, schedules, MDRM system |
| `TRADING_ACTIVITIES_GUIDE.md` | ~30 | Deep dive on trading assets, liabilities, and derivatives |

### JSON Files

| File | Description |
|------|-------------|
| `data_taxonomy.json` | Machine-readable regulatory taxonomy and hierarchy |
| `schedule_correspondence.json` | Programmatic access to cross-schedule mappings |

## Core Concepts

### MDRM Codes

MDRM (Micro Data Reference Manual) codes uniquely identify every data element:

```
BHCK3545
|  | |__|
|  |   |
|  |   +-- Item number (3545 = Trading Assets)
|  |
|  +------ Form/Scope code
|
+--------- Prefix (BHC = Bank Holding Company, K = domestic)
```

**Common Prefixes:**
- `BHCK` / `BHCT` / `BHCM` - FR Y-9C (BHC data)
- `RCFD` / `RCON` - Call Reports (Bank data)
- `RIAD` - Income statement items

### Form Hierarchy

```
FR Y-9C (BHC Level, $5B+)
    |
    +-- Consolidates --> FFIEC Call Reports (Bank Level)
    |
    +-- Supplements --> FR Y-14 (Stress Testing, $100B+)
    |
    +-- Supplements --> FR 2052a (Liquidity)
    |
    +-- Requires --> Pillar 3 (Basel III Disclosures)
```

### Key Reconciliations

1. **Trading Assets**: `HC Item 5 = HC-D Item 12 (BHCT3545)`
2. **Trading Liabilities**: `HC Item 15 = HC-D Item 15 (BHCT3548)`
3. **Derivatives FV**: `HC-D Item 11 = Sum of HC-L positive fair values`

## Common Use Cases

### 1. Build a Trading Activity Time Series

```python
# Key variables for trading analysis
trading_vars = [
    'BHCT3545',  # Total trading assets
    'BHCT3548',  # Total trading liabilities
    'BHCT3543',  # Derivatives positive FV
    'BHCT3547',  # Derivatives negative FV
    'BHCK3450',  # IR swaps notional
]
```

### 2. Map Y-9C to Call Report Codes

| Y-9C | Call Report | Description |
|------|-------------|-------------|
| BHCT3545 | RCFD3545 | Total Trading Assets |
| BHCK3450 | RCFD3450 | IR Swaps Notional |
| BHCKC968 | RCFDC968 | CDS Protection Sold |

### 3. Track Historical Code Changes

For time series spanning 2018, check `HISTORICAL_CODE_TRANSITIONS.csv`:
- BHCK3531 (pre-2018) -> BHCM3531 (post-2018 domestic)

## Data Sources

| Source | URL | Content |
|--------|-----|---------|
| FFIEC CDR | https://cdr.ffiec.gov/ | Call Reports, Y-9C |
| Fed NIC | https://www.ffiec.gov/NPW/ | Organization data |
| Chicago Fed | https://www.chicagofed.org/ | Historical Y-9C |
| FDIC BankFind | https://banks.data.fdic.gov/ | Bank financial data |

## Major Trading BHCs

| Entity | RSSD ID | Trading Focus |
|--------|---------|---------------|
| JPMorgan Chase | 1039502 | Universal bank, largest derivatives |
| Goldman Sachs | 2380443 | Investment bank focused |
| Morgan Stanley | 2162966 | Investment bank focused |
| Bank of America | 1073757 | Universal bank |
| Citigroup | 1951350 | Universal bank |

## Contributing

This repository is maintained as a reference resource. Issues and suggestions are welcome.

## License

MIT License - See LICENSE file for details.

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-01-28 | Initial comprehensive release |

---

*Created as part of the Arcanum knowledge base for bank regulatory data analysis.*
