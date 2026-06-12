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

## Machine-readable line items

The full, triple-attested per-line-item code set ships as
[`csv/CALL_RC_N_PAST_DUE.csv`](../csv/CALL_RC_N_PAST_DUE.csv) (93 rows; provenance in
`_rebuild/schedules/PROVENANCE_CALL_RC_N.csv`). Each row gives the three past-due-grid codes
(`mdrm_30_89`, `mdrm_90_plus`, `mdrm_nonaccrual`), a `prefix`, the `forms` that use that code
triple, `start_date`, `notes`, and `mdrm_single` (for the single-column nonaccrual-flow
memoranda). The tables below digest that CSV.

### CSV schema

| Column | Meaning |
|--------|---------|
| line_number | Form item number (031 and 041/051 use different numbering; the CSV keeps both) |
| loan_category | Official caption |
| mdrm_30_89 | Column A code (past due 30-89 days, still accruing), or `-` |
| mdrm_90_plus | Column B code (past due 90+ days, still accruing), or `-` |
| mdrm_nonaccrual | Column C code (nonaccrual), or `-` |
| prefix | MDRM prefix for the triple (RCFD/RCFN consolidated, RCON domestic) |
| forms | Which forms report that code triple (031/041/051) |
| start_date | MDRM start date for the primary code |
| mdrm_single | Single-column code for nonaccrual-flow memoranda (M.4/M.7/M.8), else `-` |

> **Form structure matters.** FFIEC **031** filers report many categories on the consolidated
> **RCFD/RCFN** basis and split a few items (e.g. C&I into 4.a U.S. / 4.b non-U.S. addressees;
> depository institutions into 2.a U.S. / 2.b foreign). FFIEC **041/051** filers report the
> domestic-office **RCON** basis with those items aggregated, and **051** uses its own condensed
> item numbering (1.a-1.h). The CSV carries every form's codes; the tables below show the 031
> consolidated layout, then the 041/051 aggregated items.

---

## Part I: Loans and Leases (FFIEC 031 consolidated, RCFD/RCFN)

### Real Estate Loans (item 1)

| Item | Description | 30-89 DPD | 90+ DPD | Nonaccrual |
|------|-------------|-----------|---------|------------|
| 1.a.(1) | 1-4 family residential construction | RCONF172 | RCONF174 | RCONF176 |
| 1.a.(2) | Other construction & land development | RCONF173 | RCONF175 | RCONF177 |
| 1.b | Farmland (domestic offices) | RCON3493 | RCON3494 | RCON3495 |
| 1.c.(1) | 1-4 family revolving (HELOCs) | RCON5398 | RCON5399 | RCON5400 |
| 1.c.(2)(a) | Closed-end 1-4 family, first liens | RCONC236 | RCONC237 | RCONC229 |
| 1.c.(2)(b) | Closed-end 1-4 family, junior liens | RCONC238 | RCONC239 | RCONC230 |
| 1.d | Multifamily (5+) residential (domestic offices) | RCON3499 | RCON3500 | RCON3501 |
| 1.e.(1) | Owner-occupied nonfarm nonresidential | RCONF178 | RCONF180 | RCONF182 |
| 1.e.(2) | Other nonfarm nonresidential | RCONF179 | RCONF181 | RCONF183 |
| 1.f | Real estate in foreign offices (031 only) | RCFNB572 | RCFNB573 | RCFNB574 |

> Item 1 real-estate sub-items in domestic offices are reported on the RCON basis on all forms.

### Commercial, Consumer, and Other Loans (031 consolidated)

| Item | Description | 30-89 DPD | 90+ DPD | Nonaccrual |
|------|-------------|-----------|---------|------------|
| 2.a | To U.S. depository institutions | RCFD5377 | RCFD5378 | RCFD5379 |
| 2.b | To foreign banks | RCFD5380 | RCFD5381 | RCFD5382 |
| 3 | Agricultural production | RCFD1594 | RCFD1597 | RCFD1583 |
| 4.a | C&I loans to U.S. addressees | RCFD1251 | RCFD1252 | RCFD1253 |
| 4.b | C&I loans to non-U.S. addressees | RCFD1254 | RCFD1255 | RCFD1256 |
| 5.a | Credit cards | RCFDB575 | RCFDB576 | RCFDB577 |
| 5.b | Automobile loans | RCFDK213 | RCFDK214 | RCFDK215 |
| 5.c | Other consumer (revolving + other) | RCFDK216 | RCFDK217 | RCFDK218 |
| 6 | Loans to foreign governments | RCFD5389 | RCFD5390 | RCFD5391 |
| 7 | All other loans | RCFD5459 | RCFD5460 | RCFD5461 |
| 8.a | Lease financing: to individuals (household) | RCFDF166 | RCFDF167 | RCFDF168 |
| 8.b | Lease financing: all other leases | RCFDF169 | RCFDF170 | RCFDF171 |
| **9** | **Total loans and leases (sum of items 1-8)** | **RCFD1406** | **RCFD1407** | **RCFD1403** |
| 10 | Debt securities and other assets | RCFD3505 | RCFD3506 | RCFD3507 |

### FFIEC 041 / 051 aggregated items (RCON, domestic basis)

On 041/051 the interbank and C&I categories are reported in aggregate rather than split:

| Item | Description | 30-89 DPD | 90+ DPD | Nonaccrual | Forms |
|------|-------------|-----------|---------|------------|-------|
| 2 | Loans to depository institutions and acceptances | RCONB834 | RCONB835 | RCONB836 | 041/051 |
| 4 | Commercial and industrial loans | RCON1606 | RCON1607 | RCON1608 | 041/051 |
| 8 | Lease financing receivables (041) | RCON1226 | RCON1227 | RCON1228 | 041 |
| 9 | Total loans and leases (041) | RCON1406 | RCON1407 | RCON1403 | 041 |

> 051 condenses real estate into items 1.a-1.h (construction; farmland; HELOCs; closed-end
> first/junior liens; multifamily; nonfarm owner-occupied/other) on the RCON basis. See the CSV
> for the complete 051 mapping.

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

---

## Sources and attestation

Line items reconciled to the **FFIEC Call Report forms and instructions (December 2025)**,
cross-checked against the **CDR XBRL taxonomy** (v294 presentation linkbase, per-form concept
inventory) and the **Federal Reserve MDRM**, with empirical presence verified in **FFIEC bulk
Call Report data (2001-2026)**. Per-code provenance is in
`_rebuild/schedules/PROVENANCE_CALL_RC_N.csv`; the attestation ledger is in
`_rebuild/empirical/attestations/CALL_ATTESTATION_RCE_RCN_RCR.csv` (all 263 RC-N code rows
verdict OK: present in taxonomy and in the warehouse).

*Last updated: 2026-06-11*
