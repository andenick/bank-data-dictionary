# Schedule HC-S: Securitization and Asset Sale Activities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-S - Securitization and Asset Sale Activities
**Frequency**: Quarterly
**Purpose**: Disclose securitization activities as originator, investor, and servicer

---

## Overview

Schedule HC-S provides comprehensive disclosure of securitization activities across three roles:
- **Part I**: Bank as Originator/Seller
- **Part II**: Bank as Investor
- **Part III**: Bank as Servicer

---

## Schedule Structure

```
PART I: ORIGINATOR/SELLER ACTIVITIES
├── Outstanding principal by asset type
├── Credit exposure retained
└── Asset quality of underlying

PART II: INVESTOR ACTIVITIES
├── ABS holdings by underlying asset type
└── Fair value of positions

PART III: SERVICER ACTIVITIES
├── Mortgage servicing by property type
└── Total servicing portfolio
```

---

## Part I: Originator/Seller

### Outstanding Principal Balance Sold and Securitized

| Item | Asset Type | MDRM | Call MDRM |
|------|------------|------|-----------|
| 1.a | 1-4 family residential | BHCKB705 | RCFDB705 |
| 1.b | HELOCs | BHCKB706 | RCFDB706 |
| 1.c | Credit card receivables | BHCKB707 | RCFDB707 |
| 1.d | Auto loans | BHCKB708 | RCFDB708 |
| 1.e | Other consumer | BHCKB709 | RCFDB709 |
| 1.f | C&I loans | BHCKB710 | RCFDB710 |
| 1.g | All other | BHCKB711 | RCFDB711 |

**Nature**: Shows volume of loans originated and sold into securitizations where bank retained some ongoing involvement.

### Maximum Credit Exposure

| Item | MDRM | Description |
|------|------|-------------|
| 2 | BHCKB712 | Maximum exposure from recourse or credit enhancement |

**Includes**:
- Retained subordinate tranches
- Credit enhancement provided
- Representations and warranties exposure

### Asset Quality of Underlying

| Item | Category | MDRM |
|------|----------|------|
| 3.a | Past due 30-89 days (1-4 family) | BHCKB761 |
| 3.b | Past due 90+ days (1-4 family) | BHCKB762 |
| 4 | Charge-offs YTD | BHCKB763 |

---

## Part II: Investor

### ABS Holdings by Underlying Asset Type

| Item | Asset Type | MDRM | Call MDRM |
|------|------------|------|-----------|
| 5.a | 1-4 family residential | BHCKB764 | RCFDB764 |
| 5.b | HELOCs | BHCKB765 | RCFDB765 |
| 5.c | Credit card | BHCKB766 | RCFDB766 |
| 5.d | Auto | BHCKB767 | RCFDB767 |
| 5.e | Other consumer | BHCKB768 | RCFDB768 |
| 5.f | C&I | BHCKB769 | RCFDB769 |
| 5.g | Other | BHCKB770 | RCFDB770 |
| 6 | **Total ABS held** | BHCKB771 | RCFDB771 |

**Reconciliation**: Item 6 should tie to HC-B ABS holdings (Item 5)

---

## Part III: Servicer

### Mortgages Serviced for Others

| Item | Property Type | MDRM | Call MDRM |
|------|---------------|------|-----------|
| 7.a | 1-4 family residential | BHCKB772 | RCFDB772 |
| 7.b | Other residential | BHCKB773 | RCFDB773 |
| 7.c | Commercial | BHCKB774 | RCFDB774 |
| 8 | **Total mortgage servicing** | BHCKB775 | RCFDB775 |

**Nature**: Unpaid principal balance (UPB) of mortgages serviced for third parties.

### Relationship to MSAs

Mortgage Servicing Assets (MSAs) in HC-F Item 10.b are derived from servicing rights on these portfolios.

---

## Memoranda Items

### ABCP Conduit Support

| Item | MDRM | Description |
|------|------|-------------|
| M1 | BHCKB806 | Credit enhancements to ABCP conduits |
| M2 | BHCKB807 | Liquidity facilities to ABCP conduits |

---

## Analytical Applications

### Securitization Activity Level

```
Total Origination Activity = Sum(Items 1.a - 1.g)

High volume indicates:
- Active mortgage banking
- Consumer finance focus
- Capital-efficient business model
```

### Retained Exposure Analysis

```
Retained Risk Ratio = Item 2 / Total Securitized

Higher ratio = more "skin in the game"
Risk retention rules require minimum retention
```

### Servicing Portfolio Analysis

```
Servicing Multiple = UPB Serviced / MSA Book Value

Higher multiple = higher servicing fees per dollar of MSA
Lower multiple = potential MSA impairment risk
```

### Investor Position Quality

```
Watch for concentrations in:
- Non-agency RMBS (1-4 family, HELOC)
- CLO tranches (C&I)
- Vintage exposure
```

---

## Regulatory Considerations

### Risk Retention Rule (Dodd-Frank)

- Originators must retain ≥5% credit risk
- Qualified mortgages exempt
- Various retention options (horizontal, vertical, L-shaped)

### Capital Treatment

Securitization exposures receive capital treatment per:
- Standardized approach (SFA)
- Supervisory formula approach (for advanced banks)
- Simplified supervisory formula approach (SSFA)

### Consolidation Rules

FAS 167 / ASC 810 determine whether securitization vehicles are consolidated:
- Variable Interest Entity (VIE) analysis
- Primary beneficiary determination

---

## Cross-Schedule Reconciliation

### HC-B Connection

```
HC-S Item 6 (Total ABS held) ≈ HC-B Item 5 (ABS securities)
```

### HC-F Connection

```
Servicing rights from HC-S Part III → MSA in HC-F Item 10.b
```

### Off-Balance Sheet

```
Unconsolidated securitization vehicles appear in HC-L:
- Liquidity commitments
- Credit enhancements
```

---

## MDRM Quick Reference

| Category | Item | MDRM |
|----------|------|------|
| Originated - 1-4 Family | 1.a | BHCKB705 |
| Originated - Credit Card | 1.c | BHCKB707 |
| Originated - C&I | 1.f | BHCKB710 |
| Max Credit Exposure | 2 | BHCKB712 |
| Held - Total ABS | 6 | BHCKB771 |
| Serviced - 1-4 Family | 7.a | BHCKB772 |
| Serviced - Total | 8 | BHCKB775 |
| ABCP Credit Enhancement | M1 | BHCKB806 |

---

*Last Updated: 2026-01-28*
*Reference: FR Y-9C Instructions (March 2024)*
