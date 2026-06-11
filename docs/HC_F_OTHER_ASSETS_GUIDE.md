# Schedule HC-F: Other Assets Guide

**Form**: FR Y-9C (Consolidated Financial Statements for Holding Companies)
**Schedule**: HC-F - Other Assets
**Frequency**: Quarterly
**Purpose**: Detail the components of "Other assets" reported on Schedule HC, item 11

---

## Overview

Schedule HC-F itemizes the assets that aggregate into Schedule HC item 11 ("Other assets").
The **current** FR Y-9C HC-F is a compact 7-line schedule (no memoranda). Earlier versions of
this guide described the **pre-2009** layout, which embedded Premises, OREO, unconsolidated
subsidiaries, real-estate ventures, goodwill, and other intangibles as HC-F items 6-10. Those
concepts are reported elsewhere (Schedule HC items 6-10) and are **not** part of the current HC-F.

### Relationship to Schedule HC

| HC-F Item | HC Item | Description |
|-----------|---------|-------------|
| 7 (Total) | 11 | Total other assets (must equal Schedule HC item 11) |

All HC-F detail lines (items 1-6) are sub-components of HC item 11; they do not individually
cross-reference other HC lines on the current form.

---

## Schedule Structure (current FR Y-9C)

```
OTHER ASSETS
├── Item 1: Accrued interest receivable
├── Item 2: Net deferred tax assets
├── Item 3: Interest-only strips receivable (not in the form of a security)
├── Item 4: Equity investments without readily determinable fair values
├── Item 5: Life insurance assets
│   ├── 5.a: General account
│   ├── 5.b: Separate account
│   └── 5.c: Hybrid account
├── Item 6: Other
└── Item 7: TOTAL (sum of items 1-6) = Schedule HC item 11
```

---

## Detailed Line Items

### Item 1: Accrued Interest Receivable

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCKB556 | RCFDB556 | Interest earned but not yet collected |

**Components**: interest accrued on loans, securities, and other earning assets.

### Item 2: Net Deferred Tax Assets

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCK2148 | RCFD2148 | Net deferred tax assets |

**Regulatory significance**: DTAs arising from temporary differences are subject to CET1
threshold-deduction tests under Basel III.

### Item 3: Interest-Only Strips Receivable (Not in the Form of a Security)

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCKHT80 | RCFDHT80 | IO strips not carried as a security |

**Note**: current code is **BHCKHT80** (effective 2018-06-30). The earlier code BHCKA520
("interest-only strips receivable") was end-dated 2018-03-31 and should not be used for the
current form.

### Item 4: Equity Investments Without Readily Determinable Fair Values

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCK1752 | RCFD1752 | Equity investments measured under the cost-method exception |

**Includes**: FHLB stock, Federal Reserve Bank stock, bankers' bank stock, and other equity
without quoted prices. **Accounting**: cost less impairment, plus/minus observable price changes
(ASU 2016-01).

### Item 5: Life Insurance Assets

| Line | MDRM | Call MDRM | Description |
|------|------|-----------|-------------|
| 5.a | BHCKK201 | RCFDK201 | General account life insurance assets |
| 5.b | BHCKK202 | RCFDK202 | Separate account life insurance assets |
| 5.c | BHCKK270 | RCFDK270 | Hybrid account life insurance assets |

**Note**: BOLI is now reported in this three-way split (effective 2011-03-31). The legacy single
code BHCK4659 (cash surrender value) was end-dated 2006-12-31.

### Item 6: Other

| MDRM | Call MDRM | Description |
|------|-----------|-------------|
| BHCK2168 | RCFD2168 | Residual other assets |

**May include**: prepaid expenses, accounts receivable, and miscellaneous assets not captured in
items 1-5.

### Item 7: Total (= Schedule HC Item 11)

| MDRM | Call MDRM | Description | Ties To |
|------|-----------|-------------|---------|
| BHCT2160 | RCFD2160 | Total other assets | HC Item 11 |

**Reconciliation**:
```
Item 7 = Sum(Items 1 through 6)
Schedule HC Item 11 = HC-F Item 7
```

---

## MDRM Quick Reference

| Item | MDRM | Description |
|------|------|-------------|
| 1 | BHCKB556 | Accrued interest receivable |
| 2 | BHCK2148 | Net deferred tax assets |
| 3 | BHCKHT80 | IO strips (not a security) |
| 4 | BHCK1752 | Equity without determinable FV |
| 5.a | BHCKK201 | Life insurance - general account |
| 5.b | BHCKK202 | Life insurance - separate account |
| 5.c | BHCKK270 | Life insurance - hybrid account |
| 6 | BHCK2168 | Other |
| **7** | **BHCT2160** | **TOTAL OTHER ASSETS (= HC item 11)** |

---

*Last Updated: 2026-06-11 (v8 conceptual-accuracy sweep)*
*Reference: FR Y-9C field spec (202603), MDRM, and FreeNIC warehouse*
