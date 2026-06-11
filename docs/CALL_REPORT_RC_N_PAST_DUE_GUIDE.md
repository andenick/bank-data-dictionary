# Call Report Schedule RC-N - Past Due and Nonaccrual Loans

> **Asset Quality Detail for FDIC-Insured Banks**
>
> Form: FFIEC 031/041/051 | Frequency: Quarterly

---

## Overview

Schedule RC-N reports loans and leases that are past due or on nonaccrual status. This schedule is critical for assessing asset quality and credit risk. It provides a matrix view of delinquency by loan type and aging bucket.

---

## Delinquency Buckets

| Column | Description | Days Past Due |
|--------|-------------|---------------|
| A | 30-89 days past due, still accruing | 30-89 DPD |
| B | 90+ days past due, still accruing | 90+ DPD |
| C | Nonaccrual | N/A - interest stopped |

---

## Part I: Loans and Leases

### Real Estate Loans (reported domestic-office, RCON, on FFIEC 031/041)

| Item | Description | 30-89 DPD | 90+ DPD | Nonaccrual |
|------|-------------|-----------|---------|------------|
| 1.a.(1) | 1-4 family residential construction | RCONF172 | RCONF174 | RCONF176 |
| 1.a.(2) | Other construction & land development | RCONF173 | RCONF175 | RCONF177 |
| 1.b | Farmland | RCON3493 | RCON3494 | RCON3495 |
| 1.c.(1) | 1-4 family revolving (HELOCs) | RCON5398 | RCON5399 | RCON5400 |
| 1.c.(2)(a) | Closed-end 1-4 family, first liens | RCONC236 | RCONC237 | RCONC229 |
| 1.c.(2)(b) | Closed-end 1-4 family, junior liens | RCONC238 | RCONC239 | RCONC230 |
| 1.d | Multifamily (5+) residential | RCON3499 | RCON3500 | RCON3501 |
| 1.e.(1) | Owner-occupied nonfarm nonresidential | RCONF178 | RCONF180 | RCONF182 |
| 1.e.(2) | Other nonfarm nonresidential | RCONF179 | RCONF181 | RCONF183 |

> Note: Real-estate-secured RC-N items are reported on the RCON (domestic-office) basis. Use the matching RCFD code only where a consolidated counterpart is published in MDRM.

### Commercial and Consumer Loans

| Item | Description | 30-89 DPD | 90+ DPD | Nonaccrual |
|------|-------------|-----------|---------|------------|
| 2 | Depository institutions | RCFDB834 | RCFDB835 | RCFDB836 |
| 3 | Agricultural production | RCFD1594 | RCFD1597 | RCFD1583 |
| 4 | C&I loans | RCFD1606 | RCFD1607 | RCFD1608 |
| 5 | Consumer loans (total to individuals) | RCFD1978 | RCFD1979 | RCFD1981 |
| 5.a | Credit cards | RCFDB575 | RCFDB576 | RCFDB577 |
| 6 | Foreign governments | RCFD5389 | RCFD5390 | RCFD5391 |
| 8 | All other loans (incl. leases) | RCFD3183 | RCFD3184 | RCFD3185 |
| 9 | Lease financing receivables | RCFD1226 | RCFD1227 | RCFD1228 |
| **Total** | **Total loans and lease financing receivables** | **RCFD1406** | **RCFD1407** | **RCFD1403** |

---

## Key MDRM Codes

### Primary Totals

| Metric | MDRM | Description |
|--------|------|-------------|
| Total 30-89 DPD | RCFD5524 | Sum of all 30-89 DPD loans |
| Total 90+ DPD | RCFD5525 | Sum of all 90+ DPD accruing |
| Total Nonaccrual | RCFD1403 | Sum of all nonaccrual loans |
| Total NPLs | RCFD5525 + RCFD1403 | 90+ DPD + Nonaccrual |

### Key Asset Quality Ratios

| Ratio | Formula | Benchmark |
|-------|---------|-----------|
| NPL Ratio | (RCFD5525 + RCFD1403) / RCFDB528 | < 2% |
| Nonaccrual Ratio | RCFD1403 / RCFDB528 | < 1% |
| 30-89 DPD Ratio | RCFD5524 / RCFDB528 | < 1% |
| Coverage Ratio | RCFD3123 / (RCFD5525 + RCFD1403) | > 100% |

---

## Memoranda Items

| Item | Description | MDRM | Purpose |
|------|-------------|------|---------|
| M.1 | Loan modifications to borrowers experiencing financial difficulty (total) | RCFDHK28 | Modified/restructured loans (post-ASU 2022-02; formerly TDRs) |
| M.7 | Loans/leases covered by FDIC loss-sharing agreements (total nonaccrual) | RCFDK089 | Failed-bank acquisitions, all-other-loans component |

> Note: The pre-2023 "TDR" memoranda were reported by aging bucket per loan category (e.g., RCFD/RCON K-series). After ASU 2022-02 eliminated TDR accounting, RC-N Memorandum 1 reports total loan modifications to borrowers experiencing financial difficulty (RCFDHK28 / RCONHK28). The modification memoranda are itemized per loan category rather than carried as a single legacy code.

---

## Relationship to CECL/ACL

Under CECL (Current Expected Credit Losses):
- Schedule RC-N delinquency data feeds ACL models
- Historical loss rates by bucket inform expected losses
- Nonaccrual status indicates elevated credit risk

### ACL Segmentation by RC-N

| Segment | RC-N Category | Typical ACL Treatment |
|---------|---------------|----------------------|
| Performing (current) | Not in RC-N | General pool ACL |
| Early delinquency | 30-89 DPD | Elevated ACL |
| Serious delinquency | 90+ DPD | Individual evaluation |
| Nonaccrual | Nonaccrual | Individual evaluation |

---

## Cross-Schedule Relationships

| RC-N Ties To | Relationship |
|--------------|--------------|
| RC-C | Total loans by category should match |
| RC Item 4.b | Total loans = RC-C Item 12 |
| RC-R | Credit risk RWA calculations |
| RI-B | Charge-off and recovery activity |

---

## Asset Quality Trends

### Warning Signs

| Indicator | Concern Level | Action |
|-----------|---------------|--------|
| Rising 30-89 DPD | Early warning | Monitor closely |
| Rising 90+ DPD | Elevated | Review underwriting |
| Rising nonaccrual | Serious | Provision increase |
| Coverage ratio declining | Critical | ACL adequacy review |

---

## Mapping to FR Y-9C HC-N

| Call Report | FR Y-9C |
|-------------|---------|
| RCFD5524 (30-89 DPD) | BHCK5524 |
| RCFD5525 (90+ DPD) | BHCK5525 |
| RCFD1403 (Nonaccrual) | BHCK1403 |

Replace RCFD with BHCK to get Y-9C equivalents.

---

*See also: [HC_N_PAST_DUE_GUIDE.md](HC_N_PAST_DUE_GUIDE.md) for FR Y-9C equivalent*

*Last updated: 2026-01-29*
