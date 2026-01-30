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

### Real Estate Loans

| Item | Description | 30-89 DPD | 90+ DPD | Nonaccrual |
|------|-------------|-----------|---------|------------|
| 1.a | Construction/land | RCFD5377 | RCFD5378 | RCFDC229 |
| 1.b | Farmland | RCFD5379 | RCFD5380 | RCFDC230 |
| 1.c | 1-4 family (all) | RCFD5381 | RCFD5382 | RCFDC231 |
| 1.c.(1) | First liens residential | RCON5383 | RCON5384 | RCONC234 |
| 1.c.(2) | Junior liens residential | RCON5385 | RCON5386 | RCONC235 |
| 1.c.(3) | HELOCs | RCONC233 | RCONC234 | RCONC235 |
| 1.d | Multifamily | RCFD5389 | RCFD5390 | RCFDC239 |
| 1.e | CRE nonfarm nonres | RCFD5391 | RCFD5392 | RCFDC240 |

### Commercial and Consumer Loans

| Item | Description | 30-89 DPD | 90+ DPD | Nonaccrual |
|------|-------------|-----------|---------|------------|
| 2 | Depository institutions | RCFD5396 | RCFD5397 | RCFDC241 |
| 3 | Agricultural production | RCON5398 | RCON5399 | RCONC242 |
| 4 | C&I loans | RCFD5400 | RCFD5401 | RCFDC244 |
| 5 | Consumer loans (total) | RCON5407 | RCON5408 | RCONC246 |
| 5.a | Credit cards | RCONB575 | RCONB576 | RCONK213 |
| 5.b | Other revolving | RCONK215 | RCONK216 | RCONK217 |
| 5.c | Auto loans | RCONK218 | RCONK219 | RCONK220 |
| 5.d | Other consumer | RCONK221 | RCONK222 | RCONK223 |
| 6 | Foreign governments | RCFN5411 | RCFN5412 | RCFNC248 |
| 7 | Loans to states/munis | RCFD5414 | RCFD5415 | RCFDC249 |
| 8 | Other loans | RCFD1226 | RCFD1227 | RCFD1228 |
| 9 | Lease financing | RCFD5420 | RCFD5421 | RCFDC251 |
| **10** | **Total loans and leases** | **RCFD5524** | **RCFD5525** | **RCFD1403** |

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
| M.1 | Restructured loans (TDRs) | Various | Problem debt restructurings |
| M.1.a | TDRs 30-89 DPD | RCFDK103 | Performing TDRs |
| M.1.b | TDRs 90+ DPD | RCFDK104 | Seriously delinquent TDRs |
| M.1.c | TDRs nonaccrual | RCFDK108 | Nonaccrual TDRs |
| M.2 | Loans covered by FDIC loss sharing | RCFDK190 | Failed bank acquisitions |

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
