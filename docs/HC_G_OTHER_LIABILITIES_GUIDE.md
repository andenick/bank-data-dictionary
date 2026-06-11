# Schedule HC-G: Other Liabilities Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-G - Other Liabilities
**Frequency**: Quarterly
**Purpose**: Detail other liabilities not reported elsewhere on the balance sheet

---

## Overview

Schedule HC-G provides the breakdown of liabilities that flow into Schedule HC Item 20 (Other Liabilities): net deferred tax liabilities, the allowance for credit losses on off-balance sheet credit exposures, and a residual "other" line. It is a short, four-line schedule (item 1 is not applicable on the current form).

### Relationship to Schedule HC

```
Schedule HC-G Item 5 (Total) = Schedule HC Item 20 (Other Liabilities)
```

---

## Schedule Structure

```
OTHER LIABILITIES
├── Item 1: Not applicable
├── Item 2: Net deferred tax liabilities
├── Item 3: Allowance for credit losses on off-balance sheet credit exposures
├── Item 4: Other (all other liabilities)
└── Item 5: TOTAL OTHER LIABILITIES (= HC Item 20)
```

---

## Detailed Line Items

### Item 1: Not Applicable

Line item 1 is "Not applicable" on the current FR Y-9C Schedule HC-G.

### Item 2: Net Deferred Tax Liabilities

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCK3049 | RCFD3049 | Net deferred tax liabilities |

**Nature**: Tax liabilities arising from taxable temporary differences (when book income exceeds taxable income temporarily).

**Note**: Reported per tax jurisdiction when the net result is a credit balance; a net debit (asset) balance is reported in Schedule HC-F, item 2, "Net deferred tax assets." A company can report a net DTA for one jurisdiction and a net DTL for another at the same time.

### Item 3: Allowance for Credit Losses on Off-Balance Sheet Credit Exposures

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCKB557 | RCFDB557 | ACL for unfunded commitments and other off-balance sheet credit exposures |

**Applicable To**:
- Unfunded loan commitments
- Letters of credit
- Financial guarantees
- Other off-balance sheet credit exposures

**CECL Impact**: Under ASC 326 this reserve reflects lifetime expected credit losses; holding companies that have adopted ASU 2016-13 exclude exposures that are unconditionally cancellable.

### Item 4: Other (All Other Liabilities)

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCKB984 | RCFD2938 | All other liabilities not reported in items 2-3 and not reportable in HC items 13-19 |

**Includes** (no separate MDRM codes — these are components of item 4):
- Accrued interest on deposits and nondeposit liabilities
- Accrued income taxes and other accrued expenses
- Accounts payable
- Deferred compensation liabilities
- Dividends declared but not yet payable
- Operating lease liabilities (ASC 842)
- Miscellaneous liabilities

### Item 5: Total Other Liabilities

| MDRM | Call MDRM | Description | Ties To |
|------|-----------|-------------|---------|
| BHCK2750 | RCFD2930 | Total other liabilities | HC Item 20 |

**Reconciliation**:
```
Item 5 = Items 2 + 3 + 4
Schedule HC Item 20 = HC-G Item 5
```

---

## Key Considerations

### CECL Impact on Item 3

Under Current Expected Credit Loss (CECL) accounting:
- Reserve reflects lifetime expected losses
- Applies to off-balance sheet credit exposures
- Typically larger than pre-CECL reserves
- Significant for banks with large unfunded commitment portfolios

### Operating Lease Liabilities

Under ASC 842 (effective 2019):
- Operating leases now on balance sheet
- Lease liability is a component of Item 4 (no separate HC-G code)
- Corresponding right-of-use asset in HC-F

### Relationship to Capital

Items in HC-G generally do not receive special capital treatment, but:
- ACL for OBS (Item 3) supports credit quality of commitments
- May be considered in stress testing

---

## Reconciliation Hierarchy

```
SCHEDULE HC-G                           SCHEDULE HC
═══════════════════════════════════════════════════════════════════════

Item 5 (Total)                 ────────► HC Item 20 (Other Liabilities)
BHCK2750                                 BHCK2750
```

---

## Key Analytical Metrics

### OBS Reserve Adequacy
```
OBS ACL Ratio = Item 3 / Total Unfunded Commitments (from HC-L)
- Should be compared to historical loss experience on commitments
```

### Other Liabilities to Assets
```
Other Liab % = Item 5 / Total Assets
- Typically 1-3% of assets
```

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | - | Not applicable |
| 2 | BHCK3049 | Net deferred tax liabilities |
| 3 | BHCKB557 | ACL for off-balance sheet credit exposures |
| 4 | BHCKB984 | Other (all other liabilities) |
| **5** | **BHCK2750** | **TOTAL OTHER LIABILITIES** |

> **Revision note (v7.0).** Earlier editions of this guide described a six-item HC-G with accrued-interest sub-items and a "Memoranda (2022+)" block; that structure does not exist on the FR Y-9C (it loosely mirrored the Call Report RC-G), and several of its codes were misassigned (the ACL line cited an MBS code; the memoranda cited consolidated-VIE asset codes). Version 7.0 rebuilds the schedule to the official four-line layout with MDRM-verified codes.

---

*Last Updated: 2026-06-11*
*Reference: FR Y-9C Instructions (September 2018 HC-G vintage); Federal Reserve MDRM*
