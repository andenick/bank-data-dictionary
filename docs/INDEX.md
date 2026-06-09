# Bank Regulatory Data Dictionary - Navigation Index

> **Master index for navigating the complete regulatory data dictionary**
>
> Version 6.0 | Updated: 2026-06-09

---

## Quick Navigation

| I Need To... | Go To |
|--------------|-------|
| See the whole data universe (42 collections) | [COLLECTIONS_CATALOG.md](COLLECTIONS_CATALOG.md) · [csv](../csv/COLLECTIONS_CATALOG.csv) |
| Find a specific schedule across all forms | [csv/SCHEDULES_CATALOG.csv](../csv/SCHEDULES_CATALOG.csv) |
| Understand bank corporate structure (NIC) | [NIC_STRUCTURE_GUIDE.md](NIC_STRUCTURE_GUIDE.md) |
| Reconcile entity identifiers (RSSD/Cert/LEI…) | [IDENTIFIERS.md](IDENTIFIERS.md) |
| Understand the MDRM code system | [MDRM_GUIDE.md](MDRM_GUIDE.md) · [namespaces](../csv/MDRM_NAMESPACES.csv) |
| Look up an MDRM concept crosswalk | [csv/MDRM_MASTER_COMPLETE.csv](../csv/MDRM_MASTER_COMPLETE.csv) |
| Understand the Call Report (031/041/051) | [CALL_REPORT_GUIDE.md](CALL_REPORT_GUIDE.md) |
| Work with foreign/structure forms | [FOREIGN_AND_STRUCTURE_GUIDE.md](FOREIGN_AND_STRUCTURE_GUIDE.md) |
| Work with FDIC/NCUA/OCC/UBPR data | [FDIC_NCUA_OCC_UBPR_GUIDE.md](FDIC_NCUA_OCC_UBPR_GUIDE.md) |
| Understand a specific FR Y-9C schedule | [Schedule Guides](#by-form) below |
| Validate data reconciliation | [Reconciliation Section](#reconciliation-quick-reference) |
| Build automated pipelines | [JSON Schemas](#json-schemas-for-ai-agents) |
| Map Y-9C to Call Report | [json/cross_form_mapping.json](../json/cross_form_mapping.json) |
| See what adds up to what | [RECONCILIATION_HIERARCHY.md](RECONCILIATION_HIERARCHY.md) |
| Check temporal coverage & vintages | [COVERAGE_PROVENANCE.md](COVERAGE_PROVENANCE.md) |

> **New in v6.0:** the dictionary now spans the full U.S. bank-data universe (Federal Reserve, FFIEC-joint, FDIC, NCUA, OCC, SEC, CFPB), not just FR Y-9C. Start at [COLLECTIONS_CATALOG.md](COLLECTIONS_CATALOG.md). Companion data-access package: **[FreeNIC](https://github.com/andenick/FreeNIC)**.

---

## By Form

### FR Y-9C Schedules (Primary BHC Filing)

| Schedule | CSV Data | Documentation Guide | JSON Schema | Key MDRM |
|----------|----------|---------------------|-------------|----------|
| **HC** - Balance Sheet | [HC_BALANCE_SHEET.csv](../csv/HC_BALANCE_SHEET.csv) | [HC_BALANCE_SHEET_GUIDE.md](HC_BALANCE_SHEET_GUIDE.md) | [schedule_schemas.json#HC](../json/schedule_schemas.json) | BHCT2170 |
| **HC-B** - Securities | [HC_B_SECURITIES.csv](../csv/HC_B_SECURITIES.csv) | [HC_B_SECURITIES_GUIDE.md](HC_B_SECURITIES_GUIDE.md) | [schedule_schemas.json#HC-B](../json/schedule_schemas.json) | BHCT1773 |
| **HC-C** - Loans | [HC_C_LOANS.csv](../csv/HC_C_LOANS.csv) | [HC_C_LOANS_GUIDE.md](HC_C_LOANS_GUIDE.md) | [schedule_schemas.json#HC-C](../json/schedule_schemas.json) | BHCTB529 |
| **HC-D** - Trading | [HC_D_TRADING_ASSETS.csv](../csv/HC_D_TRADING_ASSETS.csv) | [HC_D_TRADING_GUIDE.md](HC_D_TRADING_GUIDE.md) | [schedule_schemas.json#HC-D](../json/schedule_schemas.json) | BHCT3545 |
| **HC-F** - Other Assets | [HC_F_OTHER_ASSETS.csv](../csv/HC_F_OTHER_ASSETS.csv) | [HC_F_OTHER_ASSETS_GUIDE.md](HC_F_OTHER_ASSETS_GUIDE.md) | - | BHCT2160 |
| **HC-G** - Other Liabilities | [HC_G_OTHER_LIABILITIES.csv](../csv/HC_G_OTHER_LIABILITIES.csv) | [HC_G_OTHER_LIABILITIES_GUIDE.md](HC_G_OTHER_LIABILITIES_GUIDE.md) | - | BHCT2930 |
| **HC-H** - Interest Sensitivity | [HC_H_INTEREST_SENSITIVITY.csv](../csv/HC_H_INTEREST_SENSITIVITY.csv) | [HC_H_INTEREST_SENSITIVITY_GUIDE.md](HC_H_INTEREST_SENSITIVITY_GUIDE.md) | - | Various |
| **HC-K** - Quarterly Averages | [HC_K_QUARTERLY_AVERAGES.csv](../csv/HC_K_QUARTERLY_AVERAGES.csv) | [HC_K_QUARTERLY_AVERAGES_GUIDE.md](HC_K_QUARTERLY_AVERAGES_GUIDE.md) | - | Various |
| **HC-L** - Derivatives | [HC_L_DERIVATIVES.csv](../csv/HC_L_DERIVATIVES.csv) | [HC_L_DERIVATIVES_GUIDE.md](HC_L_DERIVATIVES_GUIDE.md) | [schedule_schemas.json#HC-L](../json/schedule_schemas.json) | BHCK3450 |
| **HC-N** - Past Due | [HC_N_PAST_DUE.csv](../csv/HC_N_PAST_DUE.csv) | [HC_N_PAST_DUE_GUIDE.md](HC_N_PAST_DUE_GUIDE.md) | - | BHCK1403 |
| **HC-Q** - Fair Value | [HC_Q_FAIR_VALUE.csv](../csv/HC_Q_FAIR_VALUE.csv) | [HC_Q_FAIR_VALUE_GUIDE.md](HC_Q_FAIR_VALUE_GUIDE.md) | - | Various |
| **HC-R** - Capital | [HC_R_CAPITAL.csv](../csv/HC_R_CAPITAL.csv) | [HC_R_CAPITAL_GUIDE.md](HC_R_CAPITAL_GUIDE.md) | [schedule_schemas.json#HC-R](../json/schedule_schemas.json) | BHCAP859 |
| **HC-S** - Securitization | [HC_S_SECURITIZATION.csv](../csv/HC_S_SECURITIZATION.csv) | [HC_S_SECURITIZATION_GUIDE.md](HC_S_SECURITIZATION_GUIDE.md) | - | Various |
| **HI** - Income Statement | [HI_INCOME_STATEMENT.csv](../csv/HI_INCOME_STATEMENT.csv) | [HI_INCOME_STATEMENT_GUIDE.md](HI_INCOME_STATEMENT_GUIDE.md) | [schedule_schemas.json#HI](../json/schedule_schemas.json) | BHCT4340 |

### Call Report Schedules

| Schedule | CSV Data | Documentation Guide | Key MDRM |
|----------|----------|---------------------|----------|
| **RC** - Balance Sheet | [CALL_REPORT_RC_SCHEDULES.csv](../csv/CALL_REPORT_RC_SCHEDULES.csv) | [CALL_REPORT_RC_GUIDE.md](CALL_REPORT_RC_GUIDE.md) | RCFD2170 |
| **RC-C** - Loans | [CALL_REPORT_RC_SCHEDULES.csv](../csv/CALL_REPORT_RC_SCHEDULES.csv) | [CALL_REPORT_RC_C_LOANS_GUIDE.md](CALL_REPORT_RC_C_LOANS_GUIDE.md) | RCFDB529 |
| **RC-E** - Deposits | [CALL_REPORT_RC_SCHEDULES.csv](../csv/CALL_REPORT_RC_SCHEDULES.csv) | [CALL_REPORT_RC_E_DEPOSITS_GUIDE.md](CALL_REPORT_RC_E_DEPOSITS_GUIDE.md) | RCFD2200 |
| **RC-N** - Past Due | [CALL_REPORT_RC_SCHEDULES.csv](../csv/CALL_REPORT_RC_SCHEDULES.csv) | [CALL_REPORT_RC_N_PAST_DUE_GUIDE.md](CALL_REPORT_RC_N_PAST_DUE_GUIDE.md) | RCFD1403 |
| **RI** - Income Statement | [CALL_REPORT_RC_SCHEDULES.csv](../csv/CALL_REPORT_RC_SCHEDULES.csv) | [CALL_REPORT_RI_INCOME_GUIDE.md](CALL_REPORT_RI_INCOME_GUIDE.md) | RIAD4340 |

### Advanced Capital & Regulatory Forms

| Form | CSV Data | Documentation Guide | Purpose |
|------|----------|---------------------|---------|
| FFIEC 101 | [FFIEC_101_ADVANCED_CAPITAL.csv](../csv/FFIEC_101_ADVANCED_CAPITAL.csv) | [FFIEC_101_ADVANCED_CAPITAL_GUIDE.md](FFIEC_101_ADVANCED_CAPITAL_GUIDE.md) | Advanced capital approaches |
| FFIEC 102 | [FFIEC_102_MARKET_RISK.csv](../csv/FFIEC_102_MARKET_RISK.csv) | [FFIEC_102_MARKET_RISK_GUIDE.md](FFIEC_102_MARKET_RISK_GUIDE.md) | Market risk VaR/sVaR |
| FR Y-15 | [FR_Y15_SYSTEMIC_RISK.csv](../csv/FR_Y15_SYSTEMIC_RISK.csv) | [FR_Y15_SYSTEMIC_RISK_GUIDE.md](FR_Y15_SYSTEMIC_RISK_GUIDE.md) | G-SIB systemic risk |
| FR Y-9LP | [FR_Y9LP_PARENT_ONLY.csv](../csv/FR_Y9LP_PARENT_ONLY.csv) | [FR_Y9LP_PARENT_ONLY_GUIDE.md](FR_Y9LP_PARENT_ONLY_GUIDE.md) | Parent company only |
| FFIEC 009 | [FFIEC_009_COUNTRY_EXPOSURE.csv](../csv/FFIEC_009_COUNTRY_EXPOSURE.csv) | [FFIEC_009_COUNTRY_EXPOSURE_GUIDE.md](FFIEC_009_COUNTRY_EXPOSURE_GUIDE.md) | Country exposure |
| FR Y-11 | [FR_Y11_FOREIGN_SUBSIDIARY.csv](../csv/FR_Y11_FOREIGN_SUBSIDIARY.csv) | [FR_Y11_FOREIGN_SUBSIDIARY_GUIDE.md](FR_Y11_FOREIGN_SUBSIDIARY_GUIDE.md) | Foreign subsidiaries |
| FR Y-14A/Q | [FR_Y14A_SCHEDULES.csv](../csv/FR_Y14A_SCHEDULES.csv) | [FR_Y14_CAPITAL_ASSESSMENT_GUIDE.md](FR_Y14_CAPITAL_ASSESSMENT_GUIDE.md) | Stress testing (CCAR) |
| FR 2052a | [FR_2052a_PRODUCT_HIERARCHY.csv](../csv/FR_2052a_PRODUCT_HIERARCHY.csv) | [FR_2052a_LIQUIDITY_GUIDE.md](FR_2052a_LIQUIDITY_GUIDE.md) | Liquidity monitoring |
| Pillar 3 | [PILLAR3_GSIB_DISCLOSURE.csv](../csv/PILLAR3_GSIB_DISCLOSURE.csv) | [PILLAR3_DISCLOSURE_GUIDE.md](PILLAR3_DISCLOSURE_GUIDE.md) | Public disclosure |

---

## By Concept

| Concept | CAMELS | Y-9C MDRM | Call MDRM | Y-14 | Pillar 3 |
|---------|--------|-----------|-----------|------|----------|
| **Total Assets** | M | BHCT2170 | RCFD2170 | A.2 | KM1 |
| **Total Liabilities** | M | BHCT2948 | RCFD2948 | A.2 | - |
| **Total Equity** | C | BHCT3210 | RCFD3210 | A.3 | KM1 |
| **CET1 Capital** | C | BHCAP859 | RCFAP859 | A.3 | KM1 |
| **Tier 1 Capital** | C | BHCFA223 | RCFAA223 | A.3 | KM1 |
| **Total Capital** | C | BHCFA225 | RCFAA225 | A.3 | KM1 |
| **Total RWA** | C | BHCAA223 | RCFDA223 | A.4 | KM1 |
| **CET1 Ratio** | C | BHCAP793 | RCFAP793 | - | KM1 |
| **Total Loans Net** | A | BHCTB529 | RCFDB529 | - | CR1 |
| **Allowance (ALLL)** | A | BHCT3123 | RCFD3123 | - | CR2 |
| **NPLs** | A | BHCK1403 | RCFD1403 | - | CR1 |
| **Total Securities** | L | BHCT8641 | RCFD8641 | F | - |
| **Trading Assets** | S | BHCT3545 | RCFD3545 | G | MR1 |
| **Derivatives PF FV** | S | BHCT3543 | RCFD3543 | E | CCR1 |
| **IR Swaps Notional** | S | BHCK3450 | RCFD3450 | - | CCR5 |
| **Net Income** | E | BHCT4340 | RIAD4340 | A.1 | - |
| **Net Interest Income** | E | BHCT4074 | RIAD4074 | H | - |
| **Deposits** | L | BHCT2200 | RCFD2200 | - | LIQ1 |

---

## Reconciliation Quick Reference

### Critical Balance Sheet Checks

| Check | Formula | Priority | Schedules | See Also |
|-------|---------|----------|-----------|----------|
| Balance Sheet Identity | Assets = Liabilities + Equity | CRITICAL | HC | [RECON_BS_005](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Total Assets Sum | HC.12 = Sum(Items 1-11) | CRITICAL | HC | [RECON_BS_001](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Trading Assets Tie | HC.5 = HC-D.12 | CRITICAL | HC, HC-D | [RECON_TRD_001](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Trading Liabilities Tie | HC.15 = HC-D.15 | CRITICAL | HC, HC-D | [RECON_TRD_002](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Loans Net Tie | HC.4.b = HC-C.12 | CRITICAL | HC, HC-C | [RECON_LOAN_001](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Other Assets Tie | HC.11 = HC-F.12 | CRITICAL | HC, HC-F | [RECON_OTH_001](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Securities Tie | HC.2 = HC-B Total | CRITICAL | HC, HC-B | [RECON_SEC_001](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |

### Critical Capital Checks

| Check | Formula | Priority | Schedules | See Also |
|-------|---------|----------|-----------|----------|
| Tier 1 = CET1 + AT1 | HC-R.24 = HC-R.19 + HC-R.23 | CRITICAL | HC-R | [RECON_CAP_004](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Total = Tier 1 + Tier 2 | HC-R.30 = HC-R.24 + HC-R.29 | CRITICAL | HC-R | [RECON_CAP_006](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| CET1 Ratio | CET1/RWA >= 4.5% | CRITICAL | HC-R | [RECON_CAP_009](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Total Capital Ratio | Total/RWA >= 8.0% | CRITICAL | HC-R | [RECON_CAP_011](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |

### Critical Derivatives Checks

| Check | Formula | Priority | Schedules | See Also |
|-------|---------|----------|-----------|----------|
| Positive FV Reconciliation | HC-D.11 = Sum(HC-L Positive FV) | CRITICAL | HC-D, HC-L | [RECON_TRD_005](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Negative FV Reconciliation | HC-D.14 = Sum(HC-L Negative FV) | CRITICAL | HC-D, HC-L | [RECON_TRD_006](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |

---

## JSON Schemas for AI Agents

| File | Purpose | Use Case |
|------|---------|----------|
| [schedule_schemas.json](../json/schedule_schemas.json) | Complete structure for each schedule | Programmatic access to schedule line items, MDRMs, and reconciliations |
| [cross_form_mapping.json](../json/cross_form_mapping.json) | Same concept across forms | Mapping Y-9C to Call Report to Pillar 3 |
| [data_taxonomy.json](../json/data_taxonomy.json) | Full regulatory taxonomy | Understanding form hierarchy and MDRM prefixes |
| [schedule_correspondence.json](../json/schedule_correspondence.json) | Cross-schedule linkages | Detailed reconciliation mappings |

### Example: Programmatic Schedule Access

```python
import json

with open('json/schedule_schemas.json') as f:
    schemas = json.load(f)

# Get all HC balance sheet items
for item in schemas['HC']['line_items']:
    print(f"{item['item']}: {item['name']} - {item['mdrm']}")

# Get capital cascade
capital = schemas['HC-R']['capital_cascade']
print(f"CET1 minimum: {capital['cet1']['minimum']}")
```

---

## Validation Resources

| Resource | Purpose | File |
|----------|---------|------|
| Complete Reconciliation Formulas | 60+ reconciliation checks | [RECONCILIATION_FORMULAS_COMPLETE.csv](../csv/RECONCILIATION_FORMULAS_COMPLETE.csv) |
| Validation Rules | 50 automated validation rules | [VALIDATION_RULES.csv](../csv/VALIDATION_RULES.csv) |
| Schedule Component Hierarchy | Parent-child relationships | [SCHEDULE_COMPONENT_HIERARCHY.csv](../csv/SCHEDULE_COMPONENT_HIERARCHY.csv) |
| Form Reporting Hierarchy | Which forms feed into which | [FORM_REPORTING_HIERARCHY.csv](../csv/FORM_REPORTING_HIERARCHY.csv) |
| Validation Test Cases | Sample test data | [VALIDATION_TEST_CASES.csv](../csv/VALIDATION_TEST_CASES.csv) |

---

## Reference Data

| Resource | Purpose | File |
|----------|---------|------|
| MDRM Master | Complete MDRM crosswalk | [MDRM_MASTER_COMPLETE.csv](../csv/MDRM_MASTER_COMPLETE.csv) |
| MDRM Prefixes | Prefix definitions | [MDRM_PREFIX_DEFINITIONS.csv](../csv/MDRM_PREFIX_DEFINITIONS.csv) |
| G-SIB Entities | Bank identifiers | [GSIB_ENTITY_IDENTIFIERS.csv](../csv/GSIB_ENTITY_IDENTIFIERS.csv) |
| Historical Transitions | Legacy code mappings | [HISTORICAL_CODE_TRANSITIONS.csv](../csv/HISTORICAL_CODE_TRANSITIONS.csv) |

---

## External Resources

| Source | URL | Content |
|--------|-----|---------|
| FFIEC CDR | https://cdr.ffiec.gov/ | Call Reports, Y-9C filings |
| MDRM Dictionary | https://www.federalreserve.gov/apps/mdrm/ | Official MDRM definitions |
| Fed NIC | https://www.ffiec.gov/NPW/ | Organization structure data |
| Chicago Fed | https://www.chicagofed.org/ | Historical Y-9C data |
| FDIC BankFind | https://banks.data.fdic.gov/ | Bank financial data |

---

*Last updated: 2026-06-09 | Version 6.0*
