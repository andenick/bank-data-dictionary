# Pillar 3 Basel III Public Disclosure Guide

## Overview

Pillar 3 is the market discipline component of the Basel III framework, requiring banks to publicly disclose risk and capital information in standardized templates. This enables investors, analysts, and counterparties to assess bank risk profiles.

## Reporters

G-SIBs and large internationally active banking organizations. In the U.S., this includes the 8 U.S. G-SIBs plus other large banks subject to advanced approaches.

## Template Categories

### Overview & Key Metrics
- **KM1**: Key capital and liquidity ratios (CET1, Tier 1, Total Capital, Leverage, LCR, NSFR)
- **KM2**: TLAC metrics for G-SIBs
- **OV1**: RWA overview by risk category (credit, market, operational)

### Credit Risk (CR1-CR5)
- **CR1**: Asset quality - performing vs. defaulted, provisions, write-offs (links to HC-N)
- **CR2**: Changes in defaulted loan stock (flow statement)
- **CR3**: Credit risk mitigation techniques (collateral, guarantees)
- **CR4**: Standardized approach credit RWA by exposure class
- **CR5**: IRB approach credit RWA with PD/LGD detail (links to FFIEC 101)

### Counterparty Credit Risk (CCR1-CCR8)
- **CCR1**: CCR exposure by approach (SA-CCR, IMM)
- **CCR2**: CVA capital charge (links to Y-14Q Schedule E.2)
- **CCR5**: Collateral for OTC derivatives (IM, VM)
- **CCR6**: Credit derivatives in CCR hedging (links to HC-L BHCKC968-C975)
- **CCR8**: CCP exposures (links to HC-L)

### Market Risk (MR1-MR4)
- **MR1**: Market risk capital charges under IMA (links to FFIEC 102)
- **MR2**: RWA flow statement for market risk
- **MR3**: VaR and stressed VaR levels by risk factor
- **MR4**: Backtesting - VaR vs. actual P&L (links to Y-14Q Schedule G.2)

### Securitization (SEC1-SEC4)
- Banking book and trading book securitization exposures
- Originator/sponsor and investor perspectives

### Liquidity (LIQ1-LIQ2)
- **LIQ1**: LCR components (HQLA, outflows, inflows) - derived from FR 2052a
- **LIQ2**: NSFR components (ASF, RSF) - derived from FR 2052a

### Operational Risk (OR1-OR3)
- Historical losses, business indicators, capital charge

### Leverage (LR1-LR2)
- Supplementary leverage ratio detail (links to FFIEC 101 Schedule F)

### Remuneration (REM1-REM3)
- Senior management and material risk-taker compensation

## Cross-Form Reference Matrix

| Pillar 3 | Primary Source | Key MDRM Codes |
|----------|---------------|-----------------|
| KM1 | HC-R | BHCAP859, BHCFA223, BHCFA225, BHCAA223 |
| CR1-CR2 | HC-N | BHCK1403, BHCK5524, BHCK5525 |
| CCR1-CCR8 | HC-L | BHCK8693-8740, BHCKC968-C975 |
| MR1-MR4 | FFIEC 102 | VaR, sVaR, IRC, CRM components |
| LIQ1-LIQ2 | FR 2052a | LCR, NSFR calculations |
| OV1 | HC-R Part II | BHCAA223 (total RWA) |

## Banks Covered in Knowledge Base

| Bank | RSSD ID | Quarters Available |
|------|---------|-------------------|
| Bank of America | 1073757 | 2024Q4, 2025Q3 |
| Citigroup | 1951350 | 2024Q2, 2024Q3 |
| JPMorgan Chase | 1039502 | 2024Q1, 2024Q4 |
| Morgan Stanley | 2162966 | 2024Q4, 2025Q3 |
| Wells Fargo | 1120754 | 2024Q2, 2025Q1 |

## Key Analytical Uses

1. **Cross-Bank Comparison**: Standardized templates enable direct comparison
2. **VaR Analysis**: MR3/MR4 provide VaR levels and backtesting across banks
3. **Credit Quality Trends**: CR1/CR2 track NPL migration over time
4. **Capital Adequacy**: KM1 provides comparable capital ratios
5. **Derivatives Risk**: CCR templates reveal concentrated counterparty exposures
6. **Liquidity**: LIQ1/LIQ2 show LCR/NSFR compliance margins

## Repository Files

- `csv/PILLAR3_TEMPLATES.csv` - Template reference (26 items)
- `csv/PILLAR3_GSIB_DISCLOSURE.csv` - Cross-bank disclosure items
- `csv/GSIB_ENTITY_IDENTIFIERS.csv` - Bank identifiers

---

*Part of the Bank Regulatory Data Dictionary*
