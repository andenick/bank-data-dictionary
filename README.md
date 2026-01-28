# Bank Regulatory Data Dictionary

A comprehensive, downloadable reference for U.S. bank regulatory filings data, including MDRM codes, form mappings, reconciliation formulas, and detailed guides for every FR Y-9C schedule.

## Quick Start

1. **Need MDRM codes?** Start with `csv/MDRM_MASTER_COMPLETE.csv`
2. **Analyzing specific schedules?** See schedule-specific guides in `docs/`
3. **Understanding form relationships?** See `docs/MASTER_REGULATORY_GUIDE.md`
4. **Validating data?** Check `docs/RECONCILIATION_MATRIX.md`
5. **Building automated pipelines?** Use the JSON files in `json/`

## Repository Structure

```
bank-regulatory-data-dictionary/
│
├── csv/                                    # All CSV data tables
│   ├── MDRM_MASTER_COMPLETE.csv            # Master variable crosswalk (400+ vars)
│   │
│   ├── Schedule-Specific Files:
│   ├── HC_BALANCE_SHEET.csv                # Schedule HC master balance sheet
│   ├── HC_B_SECURITIES.csv                 # Schedule HC-B securities (~40 items)
│   ├── HC_C_LOANS.csv                      # Schedule HC-C loans (~60 items)
│   ├── HC_D_TRADING_ASSETS.csv             # Schedule HC-D trading assets
│   ├── HC_F_OTHER_ASSETS.csv               # Schedule HC-F other assets (~20 items)
│   ├── HC_G_OTHER_LIABILITIES.csv          # Schedule HC-G other liabilities (~15 items)
│   ├── HC_H_INTEREST_SENSITIVITY.csv       # Schedule HC-H repricing buckets
│   ├── HC_K_QUARTERLY_AVERAGES.csv         # Schedule HC-K averages (~25 items)
│   ├── HC_L_DERIVATIVES.csv                # Schedule HC-L derivatives detail
│   ├── HC_N_PAST_DUE.csv                   # Schedule HC-N past due (~50 items)
│   ├── HC_Q_FAIR_VALUE.csv                 # Schedule HC-Q fair value hierarchy
│   ├── HC_R_CAPITAL.csv                    # Schedule HC-R regulatory capital (~120 items)
│   ├── HC_S_SECURITIZATION.csv             # Schedule HC-S securitization
│   ├── HI_INCOME_STATEMENT.csv             # Schedule HI income statement (~40 items)
│   │
│   ├── Reference Files:
│   ├── CALL_REPORT_RC_SCHEDULES.csv        # RC-D, RC-L, RC-B, RC-Q mappings
│   ├── Y14_SCHEDULE_MAP.csv                # FR Y-14 schedule reference
│   ├── PILLAR3_TEMPLATES.csv               # Basel III disclosure templates
│   ├── MDRM_PREFIX_DEFINITIONS.csv         # BHCK, RCFD, etc. explained
│   ├── RECONCILIATION_FORMULAS.csv         # What adds up to what
│   ├── FORM_HIERARCHY.csv                  # Form relationships
│   ├── GSIB_ENTITY_IDENTIFIERS.csv         # Bank identifiers (RSSD, LEI)
│   └── HISTORICAL_CODE_TRANSITIONS.csv     # Legacy vs current codes
│
├── docs/                                   # Detailed documentation
│   ├── Core Guides:
│   ├── MASTER_REGULATORY_GUIDE.md          # Comprehensive reference guide
│   ├── VERIFICATION_REPORT.md              # MDRM code verification
│   ├── RECONCILIATION_MATRIX.md            # Cross-schedule tie-outs
│   │
│   ├── Schedule-Specific Guides:
│   ├── HC_BALANCE_SHEET_GUIDE.md           # Schedule HC guide
│   ├── HC_B_SECURITIES_GUIDE.md            # Schedule HC-B guide
│   ├── HC_C_LOANS_GUIDE.md                 # Schedule HC-C guide
│   ├── HC_D_TRADING_GUIDE.md               # Schedule HC-D guide
│   ├── HC_F_OTHER_ASSETS_GUIDE.md          # Schedule HC-F guide
│   ├── HC_G_OTHER_LIABILITIES_GUIDE.md     # Schedule HC-G guide
│   ├── HC_H_INTEREST_SENSITIVITY_GUIDE.md  # Schedule HC-H guide
│   ├── HC_K_QUARTERLY_AVERAGES_GUIDE.md    # Schedule HC-K guide
│   ├── HC_L_DERIVATIVES_GUIDE.md           # Schedule HC-L guide
│   ├── HC_N_PAST_DUE_GUIDE.md              # Schedule HC-N guide
│   ├── HC_Q_FAIR_VALUE_GUIDE.md            # Schedule HC-Q guide
│   ├── HC_R_CAPITAL_GUIDE.md               # Schedule HC-R guide
│   ├── HC_S_SECURITIZATION_GUIDE.md        # Schedule HC-S guide
│   ├── HI_INCOME_STATEMENT_GUIDE.md        # Schedule HI guide
│   └── TRADING_ACTIVITIES_GUIDE.md         # Comprehensive trading guide
│
├── json/                                   # Machine-readable data
│   ├── data_taxonomy.json                  # Full regulatory taxonomy
│   └── schedule_correspondence.json        # Cross-schedule linkages
│
├── README.md                               # This file
└── LICENSE                                 # MIT License
```

## Key Files Explained

### Schedule CSV Files

| File | Schedule | Content | Items |
|------|----------|---------|-------|
| `HC_BALANCE_SHEET.csv` | HC | Master balance sheet line items | ~40 |
| `HC_B_SECURITIES.csv` | HC-B | AFS/HTM securities by type | ~40 |
| `HC_C_LOANS.csv` | HC-C | Loan portfolio breakdown | ~60 |
| `HC_D_TRADING_ASSETS.csv` | HC-D | Trading assets and liabilities | ~30 |
| `HC_F_OTHER_ASSETS.csv` | HC-F | Other assets detail | ~20 |
| `HC_G_OTHER_LIABILITIES.csv` | HC-G | Other liabilities detail | ~15 |
| `HC_H_INTEREST_SENSITIVITY.csv` | HC-H | Repricing gap analysis | ~50 |
| `HC_K_QUARTERLY_AVERAGES.csv` | HC-K | Average balances | ~25 |
| `HC_L_DERIVATIVES.csv` | HC-L | Derivatives notional and FV | ~50 |
| `HC_N_PAST_DUE.csv` | HC-N | Delinquency matrix | ~50 |
| `HC_Q_FAIR_VALUE.csv` | HC-Q | Fair value hierarchy | ~40 |
| `HC_R_CAPITAL.csv` | HC-R | Regulatory capital | ~120 |
| `HC_S_SECURITIZATION.csv` | HC-S | Securitization activities | ~30 |
| `HI_INCOME_STATEMENT.csv` | HI | Income statement | ~40 |

### Documentation

| File | Content |
|------|---------|
| `VERIFICATION_REPORT.md` | Verification of all MDRM codes against official sources |
| `RECONCILIATION_MATRIX.md` | How all schedules tie together |
| `[SCHEDULE]_GUIDE.md` | Detailed guide for each schedule with MDRM codes, formulas, and analysis |

## Core Concepts

### MDRM Codes

MDRM (Micro Data Reference Manual) codes uniquely identify every data element:

```
BHCK3545
│  │ │──│
│  │   │
│  │   └── Item number (3545 = Trading Assets)
│  │
│  └────── Form/Scope code (K = domestic)
│
└───────── Prefix (BHC = Bank Holding Company)
```

**Common Prefixes:**
- `BHCK` / `BHCT` / `BHCM` - FR Y-9C (BHC data)
- `RCFD` / `RCON` - Call Reports (Bank data)
- `RIAD` - Income statement items
- `BHCFA` / `BHCAP` - Capital items

### Schedule Hierarchy

```
Schedule HC (Balance Sheet)
├── Item 2 (Securities)      → HC-B detail
├── Item 4 (Loans)           → HC-C detail → HC-N (past due)
├── Item 5 (Trading Assets)  → HC-D detail → HC-L (derivatives)
├── Item 11 (Other Assets)   → HC-F detail
├── Item 15 (Trading Liabs)  → HC-D detail
├── Item 20 (Other Liabs)    → HC-G detail
└── Item 28 (Equity)         → HC-R (capital)

Schedule HI (Income Statement)
├── Item 3 (NII)             → NIM calculation
└── Item 12 (Net Income)     → Profitability metrics
```

### Key Reconciliations

| Check | Formula |
|-------|---------|
| Balance Sheet | Assets = Liabilities + Equity |
| Trading Assets | HC Item 5 = HC-D Item 12 |
| Trading Liabilities | HC Item 15 = HC-D Item 15 |
| Derivatives FV | HC-D Item 11 = Sum(HC-L positive FV) |
| Net Loans | HC-C Item 12 = Items 1-9 - Item 10 - Item 11 |
| Other Assets | HC Item 11 = HC-F Item 12 |
| Capital Ratio | CET1 Ratio = CET1 / RWA |

## Common Use Cases

### 1. Build a Complete Bank Financial Model

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
income_stmt = {
    'interest_income': 'BHCT4107',
    'interest_expense': 'BHCT4073',
    'net_interest_income': 'BHCT4074',
    'provision': 'BHCT4230',
    'noninterest_income': 'BHCT4079',
    'noninterest_expense': 'BHCT4093',
    'net_income': 'BHCT4340',
}
```

### 2. Analyze Asset Quality

```python
# Past due and nonaccrual from HC-N
asset_quality = {
    'npl_total': 'BHCK1403',        # Total nonaccrual
    'past_due_30_89': 'BHCK5524',   # 30-89 days
    'past_due_90_plus': 'BHCK5525', # 90+ days
    'allowance': 'BHCT3123',        # ALLL
}

# NPL Ratio = (BHCK1403 + BHCK5525) / BHCTB528
```

### 3. Calculate Capital Ratios

```python
# From HC-R
capital = {
    'cet1': 'BHCAP859',
    'tier1': 'BHCFA223',
    'total_capital': 'BHCFA225',
    'rwa': 'BHCAA223',
}

# CET1 Ratio = BHCAP859 / BHCAA223
# Tier 1 Ratio = BHCFA223 / BHCAA223
```

## Data Sources

| Source | URL | Content |
|--------|-----|---------|
| FFIEC CDR | https://cdr.ffiec.gov/ | Call Reports, Y-9C |
| MDRM Dictionary | https://www.federalreserve.gov/apps/mdrm/ | Official code definitions |
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
| 2.0 | 2026-01-28 | Added comprehensive schedule coverage (14 schedules) |
| 1.0 | 2026-01-28 | Initial release with trading focus |

---

*Created as part of the Arcanum knowledge base for bank regulatory data analysis.*
