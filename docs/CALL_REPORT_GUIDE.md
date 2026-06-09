# The Call Report — Consolidated Reports of Condition and Income

> **Master guide to the FFIEC 031 / 041 / 051 "Call Report"**
>
> Forms: FFIEC 031, FFIEC 041, FFIEC 051 | Frequency: Quarterly | Filed by: every FDIC-insured bank and savings association
>
> Vintage: verified against the **March 2025** FFIEC 031/041 instruction book and the **December 2024** FFIEC 051 instruction book. Captured 2026-06-09.

---

## What the Call Report is

The **Consolidated Reports of Condition and Income** — universally called the **Call Report** — is the quarterly regulatory filing that every national bank, state member bank, insured state nonmember bank, and savings association must submit. It is collected under the authority of the **Federal Financial Institutions Examination Council (FFIEC)** and administered jointly by the **FDIC**, the **Federal Reserve**, and the **OCC**.

Each filing is made as of the close of business on the last calendar day of the quarter (the **report date**) and is due roughly 30 days later. The filing has two halves:

- **Report of Condition** — the balance sheet (Schedule **RC**) and its supporting schedules (**RC-A** through **RC-V**).
- **Report of Income** — the income statement (Schedule **RI**) and its supporting schedules (**RI-A** through **RI-E**).

Source: [FFIEC 031/041 General Instructions, p.1](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202503_i.pdf).

### The three current form variants — who files which

Which of the three forms a bank files depends on (a) whether it has any "foreign" offices, (b) its total consolidated assets, and (c) the regulatory-capital standards applicable to it. ([FFIEC 031/041 General Instructions, "Who Must Report on What Forms," p.1](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202503_i.pdf))

| Form | Who files | Notes |
|------|-----------|-------|
| **FFIEC 031** | Banks of **any size** with one or more **foreign offices**; *also* domestic-only banks that are **advanced approaches institutions** (any size) **or** have total consolidated assets **≥ $100 billion**. | Most detailed of the three. Uniquely carries the foreign-office schedules **RC-H, RC-I, RI-D** and the three-column **RCFD/RCON/RCFN** reporting structure. |
| **FFIEC 041** | Banks with **domestic offices only** and total consolidated assets **< $100 billion** that are **not** advanced approaches institutions. | Same schedule set as the 031 except it omits **RC-H, RC-I, RI-D**. Two-column **RCFD/RCON** structure. |
| **FFIEC 051** | Banks with **domestic offices only** and total assets **< $5 billion** (measured at June 30 of the prior year), excluding advanced approaches / Category III institutions and "large"/"highly complex" institutions for deposit-insurance-assessment purposes. Filing the 051 is **optional** — an eligible bank may instead file the 041. | Streamlined: drops several schedules, reduces frequency of others, and adds **Schedule SU – Supplemental Information**. A bank that exceeds the $5 billion threshold must move to the 041 the following year. |

A "foreign" office is (a) an International Banking Facility (IBF); (b) a branch or consolidated subsidiary in a foreign country; or (c) a majority-owned Edge or Agreement subsidiary. For banks chartered in the 50 states + DC, a branch or consolidated subsidiary in Puerto Rico or a U.S. territory/possession is also "foreign"; a branch at a U.S. military facility abroad is "domestic." ([FFIEC 031/041 General Instructions, p.1](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202503_i.pdf))

Form pages: [FFIEC 031](https://www.ffiec.gov/resources/reporting-forms/ffiec031) · [FFIEC 041](https://www.ffiec.gov/resources/reporting-forms/ffiec041) · [FFIEC 051](https://www.ffiec.gov/resources/reporting-forms/ffiec051).

### Where to get the data

- **FFIEC Central Data Repository (CDR)** — the system of record for Call Report submission and the public download facility: https://cdr.ffiec.gov/
- **FDIC BankFind / financial data API** — financials, structure, history: https://banks.data.fdic.gov/
- **Instruction books** — FFIEC 031/041 (Mar 2025): https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202503_i.pdf · FFIEC 051 (Dec 2024): https://www.ffiec.gov/sites/default/files/data/reporting-forms/hv-051/FFIEC051_202412_i.pdf

---

## The column / prefix (MDRM mnemonic) system

Every Call Report data item has an 8-character **MDRM** code: a 4-character mnemonic **prefix** + a 4-character **item number**. The prefix encodes *which population of offices* (the consolidation scope / column) the value covers. ([Federal Reserve — About MDRM](https://www.federalreserve.gov/apps/mdrm/about_mdrm.htm))

| Prefix | Scope / column | Used on | Example |
|--------|----------------|---------|---------|
| **RCFD** | Report of Condition, **consolidated** — domestic **and** foreign offices combined | FFIEC 031 (and 041, where consolidated = domestic because there is no foreign column) | `RCFD2170` = total assets, whole institution |
| **RCON** | Report of Condition, **domestic offices only** | 031 / 041 / 051 | `RCON2170` = total assets, domestic offices |
| **RCFN** | Report of Condition, **foreign offices only** | FFIEC 031 only | `RCFN2170` = total assets, foreign offices |
| **RCOA** | Regulatory-capital (Schedule **RC-R**) reporting on the **domestic-office** forms (041 / 051) — column A | 041 / 051 | RC-R Part I/II capital & RWA items |
| **RCFA** | Regulatory-capital (Schedule **RC-R**) reporting on the **consolidated** form (031) — column A | FFIEC 031 | RC-R Part I/II capital & RWA items |
| **RIAD** | Report of **Income** — all income-statement items, **year-to-date** | 031 / 041 / 051 | `RIAD4340` = net income |

**The core relationship:** on the FFIEC 031, for a given item number, **RCFD = RCON + RCFN** (consolidated = domestic + foreign). ([Federal Reserve MDRM example](https://www.federalreserve.gov/apps/mdrm/about_mdrm.htm))

> **(partially UNVERIFIED — RC-R column-prefix assignment)** RC-R also uses companion "weighted-amount" column prefixes (e.g., RCFW/RCOW) for risk-weighted-asset columns. The **RCOA/RCFA** pair above is the 031-vs-041/051 split for the Schedule RC-R items. The precise 031-vs-041 assignment of RCOA/RCFA is derived from form usage and should be re-confirmed item-by-item against the MDRM download before publication.

Full MDRM catalogue (downloadable): [Federal Reserve — Micro Data Reference Manual](https://www.federalreserve.gov/data/mdrm.htm).

### Relationship to the FR Y-9C

The Call Report is the **bank-level** analogue of the **FR Y-9C**, which is filed at the **bank holding company** level. The schedules and item numbers largely parallel each other; the prefix changes:

| Call Report prefix | FR Y-9C equivalent | Scope |
|--------------------|--------------------|-------|
| RCFD | BHCK (consolidated) / BHCT (total) | Consolidated |
| RCON | BHCM | Domestic |
| RCFN | BHCK | Foreign |
| RIAD | BHCK | Income (YTD) |

So, e.g., RC ↔ HC (balance sheet), RC-C ↔ HC-C (loans), RI ↔ HI (income). When linking the two forms, **BHCK** (the consolidated holding-company series) is the analogue that lines up with **RCFD** (the bank consolidated series).

---

## Master schedule table — every schedule, all three forms

Coverage key: ✅ = on this form · ❌ = not on this form. "(I, II)" = the schedule is split into two parts in the instructions.

| ID | Title | Description | 031 | 041 | 051 | Notes |
|----|-------|-------------|:---:|:---:|:---:|-------|
| **RI** | Income Statement | Interest income/expense, noninterest income/expense, gains/losses, net income — year-to-date. | ✅ | ✅ | ✅ | Report of Income lead schedule. |
| **RI-A** | Changes in (Bank) Equity Capital | Reconciliation of beginning→ending equity capital. | ✅ | ✅ | ✅ | 051 titles it "Changes in Bank Equity Capital." |
| **RI-B** | Charge-offs and Recoveries and Changes in Allowances for Credit Losses | Part I = charge-offs/recoveries on loans & leases; Part II = changes in allowances for credit losses (ACL/CECL). | ✅ (I, II) | ✅ (I, II) | ✅ (I, II) | Both parts on all three forms. |
| **RI-C** | Disaggregated Data on the Allowance for Loan and Lease Losses | Allowance disaggregated by portfolio segment / measurement method. On 031/041: Part I (ALLL) + Part II (allowances for credit losses). | ✅ (I, II) | ✅ (I, II) | ✅ | **051 collapses RI-C** to a single (non-split) schedule. |
| **RI-D** | Income from Foreign Offices | Interest/noninterest income attributable to foreign offices. | ✅ | ❌ | ❌ | **FFIEC 031 only.** |
| **RI-E** | Explanations | Narrative/itemized explanations of amounts reported elsewhere in RI. | ✅ | ✅ | ✅ | |
| **RC** | Balance Sheet | Assets, liabilities, and equity capital — the core balance sheet. | ✅ | ✅ | ✅ | Report of Condition lead schedule. |
| **RC-A** | Cash and Balances Due from Depository Institutions | Currency/coin, balances due from banks (domestic & foreign), Federal Reserve balances. | ✅ | ✅ | ❌ | **Omitted from 051.** |
| **RC-B** | Securities | HTM and AFS securities by type (Treasuries, agency, MBS, ABS, etc.), amortized cost & fair value. | ✅ | ✅ | ✅ | |
| **RC-C** | Loans and Lease Financing Receivables | Part I = loans & leases by category; Part II = loans to small businesses and small farms. | ✅ (I, II) | ✅ (I, II) | ✅ (I, II) | Part II generally reported in the June report (annual). |
| **RC-D** | Trading Assets and Liabilities | Detail of trading-account assets/liabilities at fair value. | ✅ | ✅ | ❌ | **Omitted from 051;** 031/041 filers above trading thresholds. |
| **RC-E** | Deposit Liabilities | Deposits by type/holder (transaction vs nontransaction, retail/brokered, etc.). On 031: Part I (domestic) + Part II (foreign offices). | ✅ (I, II) | ✅ | ✅ | 031 splits into Part I (domestic) + Part II (foreign); 041/051 domestic only. |
| **RC-F** | Other Assets | Accrued interest receivable, deferred tax assets, equity securities w/o readily determinable FV, other. | ✅ | ✅ | ✅ | |
| **RC-G** | Other Liabilities | Accrued expenses, deferred tax liabilities, allowance for off-B/S credit exposures, other. | ✅ | ✅ | ✅ | |
| **RC-H** | Selected Balance Sheet Items for Domestic Offices | Domestic-office balance-sheet detail carved out of the consolidated total. | ✅ | ❌ | ❌ | **FFIEC 031 only.** |
| **RC-I** | Assets and Liabilities of IBFs | Balance-sheet items of International Banking Facilities. | ✅ | ❌ | ❌ | **FFIEC 031 only.** |
| **RC-K** | Quarterly Averages | Quarter-average balances for major asset/liability categories. | ✅ | ✅ | ✅ | |
| **RC-L** | Derivatives and Off-Balance-Sheet Items | Commitments, guarantees, letters of credit, notional derivatives, etc. | ✅ | ✅ | ✅ | 051 titles it "Off-Balance-Sheet Items." |
| **RC-M** | Memoranda | Insider extensions of credit, BOLI, brokered/reciprocal deposits, intangibles, other memoranda. | ✅ | ✅ | ✅ | |
| **RC-N** | Past Due and Nonaccrual Loans, Leases, and Other Assets | Delinquency aging (30–89 days, 90+ days, nonaccrual) by category. | ✅ | ✅ | ✅ | |
| **RC-O** | Other Data for Deposit Insurance Assessments | Deposit-insurance assessment base and components (FDIC). | ✅ | ✅ | ✅ | |
| **RC-P** | 1-4 Family Residential Mortgage Banking Activities | Originations, sales, repurchases, servicing of 1-4 family mortgages. | ✅ | ✅ | ❌ | **Omitted from 051;** 031/041 filers above activity thresholds. |
| **RC-Q** | Assets and Liabilities Measured at Fair Value on a Recurring Basis | Fair-value hierarchy (Level 1/2/3) detail. | ✅ | ✅ | ❌ | **Omitted from 051;** threshold-triggered on 031/041. |
| **RC-R** | Regulatory Capital | Part I = regulatory capital components & ratios (CET1, Tier 1, Total, leverage); Part II = risk-weighted assets. | ✅ (I, II) | ✅ (I, II) | ✅ (I, II) | Both parts on all three forms; uses **RCOA/RCFA** capital prefixes (see above). |
| **RC-S** | Servicing, Securitization, and Asset Sale Activities | Securitization exposures, servicing, recourse/credit enhancement. | ✅ | ✅ | ❌ | **Omitted from 051.** |
| **RC-T** | Fiduciary and Related Services | Trust/fiduciary assets, accounts, income. | ✅ | ✅ | ✅ | Frequency (annual/quarterly) varies with fiduciary-activity size. |
| **RC-V** | Variable Interest Entities | Consolidated VIE assets/liabilities. | ✅ | ✅ | ❌ | **Omitted from 051.** |
| **SU** | Supplemental Information | Streamlined-form supplement: mostly yes/no triggers for complex/specialized activities, with follow-up detail when applicable. | ❌ | ❌ | ✅ | **FFIEC 051 only.** Replaces the detail in the schedules the 051 drops. |
| RC-X | *Optional Narrative Statement Concerning the Amounts Reported* | Optional free-text narrative; **not a data schedule.** | ✅ | ✅ | ✅ | Listed as "RC-X" on 031/041 and as the narrative item "SU-19" on 051; optional. |

Sources: [FFIEC 031/041 instruction book TOC, pp. i–iii](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202503_i.pdf); [FFIEC 051 instruction book TOC, pp. i–ii](https://www.ffiec.gov/sites/default/files/data/reporting-forms/hv-051/FFIEC051_202412_i.pdf).

### Schedule counts per form (excluding the optional RC-X / SU-19 narrative)

| Form | Income schedules | Condition schedules | Supplemental | **Total** |
|------|:---:|:---:|:---:|:---:|
| FFIEC 031 | 6 (RI, RI-A, RI-B, RI-C, RI-D, RI-E) | 21 (RC, RC-A, RC-B, RC-C, RC-D, RC-E, RC-F, RC-G, RC-H, RC-I, RC-K, RC-L, RC-M, RC-N, RC-O, RC-P, RC-Q, RC-R, RC-S, RC-T, RC-V) | — | **27** |
| FFIEC 041 | 5 (no RI-D) | 19 (no RC-H, RC-I) | — | **24** |
| FFIEC 051 | 5 (no RI-D; RI-C unsplit) | 13 (no RC-A, RC-D, RC-H, RC-I, RC-P, RC-Q, RC-S, RC-V) | 1 (Schedule SU) | **19** |

**This guide documents 28 distinct schedule IDs** (RI, RI-A–RI-E, RC, RC-A–RC-V, SU) plus the optional RC-X narrative.

> **Reconciling these counts with the machine-readable catalog.** The per-form totals above (**27 / 24 / 19** for 031 / 041 / 051) count each lettered schedule **once**. The catalog file [`csv/SCHEDULES_CATALOG.csv`](../csv/SCHEDULES_CATALOG.csv) (and the per-form `schedule_count` in [`json/collections.json`](../json/collections.json)) instead counts **schedule *parts* as separate rows**, so its coverage flags total **30 / 27 / 22**. The difference is exactly **+3** on every form: the three schedules that the instructions split into Part I and Part II — **RI-B**, **RC-C**, and **RC-R** — each contribute **two** catalog rows instead of one. No invented or extra schedules are involved; the gap is purely Part I/II granularity. (RI-C and RC-E are also split on some forms but are carried as single catalog rows, so they do not add to the count.)

---

## What differs across 031 / 041 / 051

The three forms share one master schedule set; the differences are subtractions (and one addition for the 051).

**FFIEC 031 — adds (vs 041):**
- The three **foreign-office-only schedules**: **RC-H** (selected domestic-office items), **RC-I** (IBF assets/liabilities), and **RI-D** (income from foreign offices).
- The **three-column RCFD / RCON / RCFN** reporting structure (the 041 uses two columns, RCFD/RCON, because it has no foreign offices).
- Schedule **RC-E is split** into Part I (domestic) and Part II (foreign offices); on the 041/051 RC-E is domestic only.
- RC-R uses the **consolidated** capital prefix **RCFA** (vs **RCOA** on the 041/051).

**FFIEC 051 — drops (vs 041):**
- Condition-side: **RC-A, RC-D, RC-P, RC-Q, RC-S, RC-V** are omitted entirely.
- **Collapses RI-C** from a two-part schedule to a single (non-split) schedule.
- Reduces several remaining items to **semiannual or annual** frequency.
- (RC-H, RC-I, RI-D are already 031-only and therefore also absent.)

**FFIEC 051 — adds (vs 041):**
- **Schedule SU — Supplemental Information**: mostly yes/no triggers for complex/specialized activities, with follow-up detail only when an activity applies. SU substitutes, in compressed form, for the detail in the schedules the 051 drops.

Sources: [FFIEC 031/041 instruction book](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202503_i.pdf); [FFIEC 051 General Instructions, p.1, 3–5](https://www.ffiec.gov/sites/default/files/data/reporting-forms/hv-051/FFIEC051_202412_i.pdf).

---

## Historical form lineage

- **Before March 2001 — four forms.** Banks filed one of four versions by office type and asset size: **FFIEC 031** (domestic + foreign offices); and three domestic-only forms keyed to asset size — **FFIEC 032**, **FFIEC 033**, and **FFIEC 034**. ([FFIEC 031/032/033/034 instruction book, June 2000](https://www.ffiec.gov/sites/default/files/data/reporting-forms/hv-031/FFIEC031_034inst_200006.pdf))
- **Effective March 2001 — consolidated to two.** The three domestic-only forms (032/033/034) were eliminated and replaced by a single domestic-only form, the **FFIEC 041**, leaving two forms: FFIEC 031 (foreign offices) and FFIEC 041 (domestic only). ([FFIEC Reporting Forms](https://www.ffiec.gov/resources/reporting-forms))
- **Effective March 31, 2017 — the FFIEC 051 introduced.** A new streamlined form for eligible small institutions (originally **domestic offices only and total assets < $1 billion**, excluding advanced approaches institutions). It was created from the FFIEC 041 by removing certain schedules/items and reducing the reporting frequency of others — cutting the report from ~85 to ~61 pages and removing ~950 (about 40%) of the ~2,400 FFIEC 041 data items. ([FFIEC 051 Current Information](https://www.ffiec.gov/resources/reporting-forms/ffiec051); [FFIEC 2016 Call Report Federal Register Notice](https://www.ffiec.gov/sites/default/files/media/press-releases/2016/2016-call-report-federal-register-notice.pdf))
- **FFIEC 051 threshold raised to $5 billion.** The eligibility threshold was subsequently raised from < $1 billion to **< $5 billion** in total assets (following EGRRCPA / S.2155 relief); current eligibility is measured as of June 30 of the prior year. ([FDIC FIL-21-2008](https://www.fdic.gov/news/inactive-financial-institution-letters/2021/fil21008.html); [FFIEC 051 General Instructions, p.2](https://www.ffiec.gov/sites/default/files/data/reporting-forms/hv-051/FFIEC051_202412_i.pdf))

> **Related but distinct collection (not a Call Report form):** **FFIEC 002** — Report of Assets and Liabilities of U.S. Branches and Agencies of Foreign Banks. Out of scope here. ([FFIEC 002 Current Information](https://www.ffiec.gov/resources/reporting-forms/ffiec002))

---

## Detailed schedule guides

Per-schedule deep dives in this repository (line items, MDRM codes, FR Y-9C equivalents, and cross-schedule tie-outs):

- **Schedule RC — Balance Sheet:** [CALL_REPORT_RC_GUIDE.md](CALL_REPORT_RC_GUIDE.md)
- **Schedule RC-C — Loans and Lease Financing Receivables:** [CALL_REPORT_RC_C_LOANS_GUIDE.md](CALL_REPORT_RC_C_LOANS_GUIDE.md)
- **Schedule RC-E — Deposit Liabilities:** [CALL_REPORT_RC_E_DEPOSITS_GUIDE.md](CALL_REPORT_RC_E_DEPOSITS_GUIDE.md)
- **Schedule RC-N — Past Due and Nonaccrual Loans, Leases, and Other Assets:** [CALL_REPORT_RC_N_PAST_DUE_GUIDE.md](CALL_REPORT_RC_N_PAST_DUE_GUIDE.md)
- **Schedule RI — Income Statement:** [CALL_REPORT_RI_INCOME_GUIDE.md](CALL_REPORT_RI_INCOME_GUIDE.md)

The remaining schedules in the master table above (RC-A, RC-B, RC-D, RC-F, RC-G, RC-H, RC-I, RC-K, RC-L, RC-M, RC-O, RC-P, RC-Q, RC-R, RC-S, RC-T, RC-V; RI-A, RI-B, RI-C, RI-D, RI-E; SU) are documented at the form level here and are targets for future per-schedule guides.

---

## Data sources

- **FFIEC Central Data Repository (CDR):** https://cdr.ffiec.gov/
- **FDIC BankFind / financial data API:** https://banks.data.fdic.gov/
- **FFIEC 031/041 form & instructions:** https://www.ffiec.gov/resources/reporting-forms/ffiec031 · https://www.ffiec.gov/resources/reporting-forms/ffiec041 · [Instructions, Mar 2025](https://www.ffiec.gov/sites/default/files/data/reporting-forms/FFIEC031_FFIEC041_202503_i.pdf)
- **FFIEC 051 form & instructions:** https://www.ffiec.gov/resources/reporting-forms/ffiec051 · [Instructions, Dec 2024](https://www.ffiec.gov/sites/default/files/data/reporting-forms/hv-051/FFIEC051_202412_i.pdf)
- **Federal Reserve MDRM (data-item dictionary):** https://www.federalreserve.gov/data/mdrm.htm

---

*Part of the `bank-data-dictionary` project (v6.0). See also the FR Y-9C holding-company guides for the consolidated-BHC analogues of these schedules.*

*Last updated: 2026-06-09*
