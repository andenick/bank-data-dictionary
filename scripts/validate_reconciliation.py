#!/usr/bin/env python3
"""Registry-driven bank regulatory data validator (FR Y-9C).

This script evaluates the empirically-tested reconciliation identities in
``csv/RELATIONSHIP_REGISTRY.csv`` against a supplied set of MDRM-coded values.
Unlike earlier versions, it hardcodes NO rules: every check is read from the
registry at runtime, so the validation logic stays in lock-step with the
empirically-confirmed relationships (and the disproven BHCFA223/224/225 and
"BHCAP856-as-AT1" rules are simply absent from the registry, hence gone).

Each registry row carries an ``expression`` (a linear combination of MDRM codes
with a single comparator), a ``severity``, ``sources``, and the empirical
context (n filings, pass rate, test window) that backs it. Rows flagged
``testable=yes`` are evaluated; the rest are informational.

Expression grammar
------------------
    <linear side> <comparator> <linear side>

where each side is a sum/difference of MDRM codes (``[A-Z]{4}[A-Z0-9]{4}``)
and/or numeric literals, optionally grouped with parentheses, and the
comparator is one of ``=  <=  >=  <  >``. Negation distributes over a
parenthesised group, e.g. ``A - (B + C)`` parses as ``A - B - C`` (the
``parse_side`` routine is ported verbatim from the proven empirical tester in
``_rebuild/empirical/test_identities.py``).

Usage
-----
    python validate_reconciliation.py --sample
    python validate_reconciliation.py --data bank.csv
    python validate_reconciliation.py --data bank.json --severity CRITICAL
    python validate_reconciliation.py --data bank.csv --all
    python validate_reconciliation.py --data bank.csv --scope call

Exit code is non-zero if any CRITICAL rule FAILs.

Author: Bank Regulatory Data Dictionary (v8, Phase 6)
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

# An MDRM code: four letters followed by four alphanumerics (e.g. BHCK2170).
CODE = re.compile(r"\b[A-Z]{4}[A-Z0-9]{4}\b")
# A single expression token: an MDRM code or a numeric literal.
_TOKEN = re.compile(r"[A-Z]{4}[A-Z0-9]{4}|\d+(?:\.\d+)?")

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, ".."))
REGISTRY = os.path.join(REPO, "csv", "RELATIONSHIP_REGISTRY.csv")

# Comparators in match-priority order: two-character operators first so that
# "<=" is not mis-split on "<".
_COMPARATORS = ("<=", ">=", "=", "<", ">")


# ---------------------------------------------------------------------------
# Expression parsing (ported from _rebuild/empirical/test_identities.py)
# ---------------------------------------------------------------------------
def parse_side(side: str) -> List[Tuple[str, str]]:
    """Parse one side of an expression into signed tokens.

    Returns a list of ``(sign, token)`` pairs where ``sign`` is ``"+"`` or
    ``"-"`` and ``token`` is an MDRM code or numeric literal. Negation is
    distributed over parenthesised groups, so ``A - (B + C)`` yields
    ``[("+", "A"), ("-", "B"), ("-", "C")]`` (a naive parser would have
    silently dropped the group negation).

    Args:
        side: One side of a comparison expression.

    Returns:
        List of signed-token tuples in left-to-right order.
    """
    side = side.strip()
    terms: List[Tuple[str, str]] = []
    sign_ctx = 1  # +1 inside a positive group, -1 inside a negated group
    pending = 1   # sign for the next token
    i = 0
    group_stack: List[int] = []
    while i < len(side):
        ch = side[i]
        if ch == "+":
            pending = 1
            i += 1
        elif ch == "-":
            pending = -1
            i += 1
        elif ch == "(":
            group_stack.append(sign_ctx)
            sign_ctx *= pending
            pending = 1
            i += 1
        elif ch == ")":
            if group_stack:
                sign_ctx = group_stack.pop()
            pending = 1
            i += 1
        elif ch.isspace():
            i += 1
        else:
            m = _TOKEN.match(side, i)
            if m:
                s = sign_ctx * pending
                terms.append(("-" if s < 0 else "+", m.group(0)))
                pending = 1
                i = m.end()
            else:
                i += 1
    return terms


def split_expression(expression: str) -> Optional[Tuple[str, str, str]]:
    """Split an expression into (lhs_raw, comparator, rhs_raw).

    Args:
        expression: The full expression string from the registry.

    Returns:
        ``(lhs, op, rhs)`` on success, or ``None`` if no single comparator is
        found (e.g. conditional/intraseries rules that are not simple linear
        identities).
    """
    for op in _COMPARATORS:
        if op not in expression:
            continue
        # Reject "=" matches that are really part of "<=" / ">=".
        if op == "=" and ("<=" in expression or ">=" in expression):
            continue
        lhs_raw, rhs_raw = expression.split(op, 1)
        return lhs_raw, op, rhs_raw
    return None


def eval_side(terms: List[Tuple[str, str]],
              data: Dict[str, float]) -> Tuple[float, List[str]]:
    """Evaluate a parsed side against the data dictionary.

    Missing MDRM codes contribute 0 but are collected and returned so callers
    can report them.

    Args:
        terms: Signed tokens from :func:`parse_side`.
        data: MDRM-code -> value mapping.

    Returns:
        ``(value, missing_codes)`` where ``value`` is the signed sum and
        ``missing_codes`` lists referenced codes absent from ``data``.
    """
    total = 0.0
    missing: List[str] = []
    for sign, tok in terms:
        if CODE.fullmatch(tok):
            if tok in data:
                v = data[tok]
            else:
                v = 0.0
                missing.append(tok)
        else:
            v = float(tok)
        total += v if sign == "+" else -v
    return total, missing


# ---------------------------------------------------------------------------
# Registry model & evaluation
# ---------------------------------------------------------------------------
SEVERITY_ORDER = {"CRITICAL": 0, "HIGH": 1, "MEDIUM": 2, "LOW": 3, "INFO": 4}


@dataclass
class Rule:
    """A single reconciliation rule loaded from the registry."""

    rel_id: str
    scope: str
    kind: str
    expression: str
    severity: str
    sources: str
    status: str
    condition_text: str
    empirical_n: str
    empirical_pass_rate: str
    test_window: str

    def empirical_context(self) -> str:
        """Human-readable empirical-backing string for this rule."""
        status = self.status or "UNKNOWN"
        try:
            n = int(self.empirical_n) if self.empirical_n else None
        except ValueError:
            n = None
        try:
            rate = float(self.empirical_pass_rate) if self.empirical_pass_rate else None
        except ValueError:
            rate = None
        verb = "CONFIRMED" if status.startswith("CONFIRMED") else status
        parts = [f"empirically {verb}"]
        if rate is not None:
            parts.append(f"at {rate * 100:.1f}%")
        if n is not None:
            parts.append(f"across {n:,} filings")
        if self.test_window:
            parts.append(self.test_window.replace("..", " to "))
        return " ".join(parts)


@dataclass
class RuleResult:
    """Outcome of evaluating one rule against supplied data."""

    rule: Rule
    status: str  # "PASS" | "FAIL" | "SKIPPED"
    lhs: Optional[float] = None
    rhs: Optional[float] = None
    tolerance: Optional[float] = None
    codes_missing: List[str] = field(default_factory=list)
    message: str = ""

    @property
    def is_critical_fail(self) -> bool:
        return self.status == "FAIL" and self.rule.severity == "CRITICAL"


def load_registry(path: str = REGISTRY) -> List[Rule]:
    """Load all rules from the relationship registry CSV.

    Args:
        path: Path to RELATIONSHIP_REGISTRY.csv.

    Returns:
        List of :class:`Rule` for every ``testable=yes`` row.
    """
    rules: List[Rule] = []
    with open(path, encoding="utf-8", newline="") as fh:
        for row in csv.DictReader(fh):
            if row.get("testable", "").strip() != "yes":
                continue
            rules.append(Rule(
                rel_id=row["rel_id"],
                scope=row.get("scope", ""),
                kind=row.get("kind", ""),
                expression=row["expression"],
                severity=(row.get("severity") or "MEDIUM").strip().upper(),
                sources=row.get("sources", ""),
                status=(row.get("status") or "").strip(),
                condition_text=row.get("condition_text", ""),
                empirical_n=row.get("empirical_n", ""),
                empirical_pass_rate=row.get("empirical_pass_rate", ""),
                test_window=row.get("test_window", ""),
            ))
    return rules


def evaluate_rule(rule: Rule, data: Dict[str, float]) -> RuleResult:
    """Evaluate one rule against the supplied data.

    Skips (rather than fails) a rule when the *target* side -- the side with the
    fewer codes, conventionally the reported total -- is entirely missing from
    the data, since the rule then cannot be meaningfully tested.

    Tolerance is ``max(1.0, 0.001 * |rhs|)`` (FreeNIC's proven tolerance), in
    the same units as the data (thousands of USD for FR Y-9C).

    Args:
        rule: The rule to evaluate.
        data: MDRM-code -> value mapping.

    Returns:
        A :class:`RuleResult`.
    """
    split = split_expression(rule.expression)
    if split is None:
        return RuleResult(rule, "SKIPPED",
                          message="not a simple linear comparison (conditional/intraseries)")
    lhs_raw, op, rhs_raw = split
    lhs_terms = parse_side(lhs_raw)
    rhs_terms = parse_side(rhs_raw)

    lhs_codes = [t for s, t in lhs_terms if CODE.fullmatch(t)]
    rhs_codes = [t for s, t in rhs_terms if CODE.fullmatch(t)]

    # Target side = side with fewer codes (usually the single-code total).
    if len(lhs_codes) <= len(rhs_codes):
        tgt_codes = lhs_codes
    else:
        tgt_codes = rhs_codes

    # Skip (don't fail) when a code-bearing side has none of its codes present:
    # evaluating it as 0 would spuriously fail the identity. This covers both
    # the target-total-absent case and the (more common, for partial data)
    # component-side-absent case. A side is "present enough" if at least one of
    # its codes is in the data.
    lhs_present = any(c in data for c in lhs_codes)
    rhs_present = any(c in data for c in rhs_codes)
    side_missing = (lhs_codes and not lhs_present) or (rhs_codes and not rhs_present)
    if side_missing:
        absent = sorted(set(c for c in lhs_codes + rhs_codes if c not in data))
        which = "target side" if (tgt_codes and not any(c in data for c in tgt_codes)) \
            else "a code-bearing side"
        return RuleResult(rule, "SKIPPED", codes_missing=absent,
                          message=f"{which} absent from data")

    lhs_val, miss_l = eval_side(lhs_terms, data)
    rhs_val, miss_r = eval_side(rhs_terms, data)
    missing = sorted(set(miss_l + miss_r))

    tol = max(1.0, 0.001 * abs(rhs_val))
    if op == "=":
        passed = abs(lhs_val - rhs_val) <= tol
    elif op == "<=":
        passed = lhs_val <= rhs_val + tol
    elif op == ">=":
        passed = lhs_val >= rhs_val - tol
    elif op == "<":
        passed = lhs_val < rhs_val + tol
    elif op == ">":
        passed = lhs_val > rhs_val - tol
    else:  # pragma: no cover - split_expression guarantees a known op
        return RuleResult(rule, "SKIPPED", message=f"unknown comparator {op!r}")

    msg = "PASS" if passed else f"diff = {lhs_val - rhs_val:,.0f} (tol {tol:,.0f})"
    return RuleResult(rule, "PASS" if passed else "FAIL",
                      lhs=lhs_val, rhs=rhs_val, tolerance=tol,
                      codes_missing=missing, message=msg)


# ---------------------------------------------------------------------------
# Data loading
# ---------------------------------------------------------------------------
def load_data_from_csv(filepath: str) -> Dict[str, float]:
    """Load MDRM values from a CSV with code/value columns.

    Accepts ``mdrm_code``/``mdrm``/``MDRM`` for the code column and
    ``value``/``amount``/``VALUE`` for the value column.

    Args:
        filepath: Path to the CSV file.

    Returns:
        MDRM-code -> float value mapping.
    """
    data: Dict[str, float] = {}
    with open(filepath, "r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mdrm = row.get("mdrm_code") or row.get("mdrm") or row.get("MDRM")
            value = row.get("value") or row.get("amount") or row.get("VALUE")
            if mdrm and value not in (None, ""):
                try:
                    data[mdrm.strip()] = float(str(value).replace(",", ""))
                except ValueError:
                    pass
    return data


def load_data_from_json(filepath: str) -> Dict[str, float]:
    """Load MDRM values from a JSON object ``{code: value}``.

    Args:
        filepath: Path to the JSON file.

    Returns:
        MDRM-code -> float value mapping.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        raw = json.load(f)
    return {str(k): float(v) for k, v in raw.items()}


# Real JPMorgan Chase (RSSD 1039502) FR Y-9C values, period 2025-09-30 (the
# latest filed quarter; 2025-12-31 not yet available), in thousands of USD
# (public regulatory filing). These are the same values written to
# _rebuild/empirical/sample_filings/1039502_20250930.csv in Job 2, so --sample
# demonstrably passes the confirmed registry identities.
SAMPLE_DATA: Dict[str, float] = {
    "BHCK2170": 4560205000,   # HC-12 Total assets
    "BHCK2948": 4199836000,   # HC-21 Total liabilities (incl. minority interest)
    "BHCK3210": 360212000,    # HC-28 Total equity capital
    "BHCK3300": 4560205000,   # HC-29 Total liabilities and equity (= HC-12)
    "BHCKG105": 360369000,    # HC-G total equity capital incl. minority interest
    "BHCK4107": 144891000,    # HI-1h Total interest income
    "BHCK4073": 74085000,     # HI-2f Total interest expense
    "BHCK4074": 70806000,     # HI-3 Net interest income
    "BHCT2750": 317157000,    # HC-G5 Total equity capital (HC-G col)
    "BHCK2750": 317157000,    # HC-20 Total equity capital
    "BHCK3049": 0,            # HC-G2
    "BHCKB557": 2965000,      # HC-G3
    "BHCKB984": 314192000,    # HC-G4
}


# ---------------------------------------------------------------------------
# Reporting
# ---------------------------------------------------------------------------
def filter_rules(rules: List[Rule], severity: Optional[str],
                 only_confirmed: bool, scope: str = "all") -> List[Rule]:
    """Apply scope, severity, and confirmation filters to the rule set.

    Args:
        rules: All loaded rules.
        severity: If set, keep only rules of this severity.
        only_confirmed: If True, keep only rules whose status starts with
            ``CONFIRMED`` (i.e. CONFIRMED or CONFIRMED_CURRENT).
        scope: ``"y9c"``, ``"call"``, or ``"all"`` (default). Selects the
            filing universe a rule belongs to (``Rule.scope``); ``"all"``
            applies no scope filter.

    Returns:
        The filtered rule list.
    """
    out = rules
    if scope and scope != "all":
        out = [r for r in out if r.scope == scope]
    if only_confirmed:
        out = [r for r in out if r.status.startswith("CONFIRMED")]
    if severity:
        sev = severity.upper()
        out = [r for r in out if r.severity == sev]
    return out


def print_report(results: List[RuleResult]) -> Dict[str, int]:
    """Print the validation report and return summary counts.

    Args:
        results: Evaluated rule results.

    Returns:
        Summary dict with passed/failed/skipped/critical_failures counts.
    """
    print("\n" + "=" * 74)
    print("BANK REGULATORY DATA VALIDATION REPORT (registry-driven)")
    print("=" * 74)

    passed = sum(1 for r in results if r.status == "PASS")
    failed = sum(1 for r in results if r.status == "FAIL")
    skipped = sum(1 for r in results if r.status == "SKIPPED")
    critical_failures = sum(1 for r in results if r.is_critical_fail)
    tested = passed + failed

    print(f"\nRules evaluated: {len(results)}  "
          f"(PASS {passed} / FAIL {failed} / SKIPPED {skipped})")
    if tested:
        print(f"Pass rate (of tested): {passed / tested * 100:.1f}%")
    if critical_failures:
        print(f"WARNING: {critical_failures} CRITICAL failure(s) detected!")

    print("\n" + "-" * 74)
    for r in results:
        rule = r.rule
        print(f"\n[{r.status}] {rule.rel_id}  ({rule.severity}, {rule.kind})")
        print(f"       expr: {rule.expression}")
        if r.lhs is not None and r.rhs is not None:
            print(f"       lhs = {r.lhs:,.0f}   rhs = {r.rhs:,.0f}   "
                  f"tol = {r.tolerance:,.0f}")
        if r.codes_missing:
            print(f"       codes_missing: {', '.join(r.codes_missing)}")
        if r.status != "PASS":
            print(f"       note: {r.message}")
        print(f"       context: {rule.empirical_context()}")
        if rule.sources:
            print(f"       sources: {rule.sources}")

    print("\n" + "=" * 74)
    return {
        "evaluated": len(results),
        "passed": passed,
        "failed": failed,
        "skipped": skipped,
        "critical_failures": critical_failures,
    }


def main() -> None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Validate bank regulatory data against the empirically-"
                    "confirmed relationship registry.")
    parser.add_argument("--data", type=str,
                        help="Path to data file (CSV with mdrm_code,value or JSON {code: value})")
    parser.add_argument("--sample", action="store_true",
                        help="Run against the built-in real-bank sample (JPMorgan 2025Q4)")
    parser.add_argument("--scope", type=str, default="all",
                        choices=["y9c", "call", "all"],
                        help="Only evaluate rules from this filing universe "
                             "(y9c = FR Y-9C, call = Call Report; default all)")
    parser.add_argument("--severity", type=str, default=None,
                        choices=["CRITICAL", "HIGH", "MEDIUM", "LOW", "INFO"],
                        help="Only evaluate rules of this severity")
    parser.add_argument("--only-confirmed", dest="only_confirmed",
                        action="store_true", default=True,
                        help="Only rules whose status starts with CONFIRMED (default)")
    parser.add_argument("--all", dest="only_confirmed", action="store_false",
                        help="Include non-CONFIRMED testable rules (QUALITY_TOLERANCE, etc.)")
    parser.add_argument("--registry", type=str, default=REGISTRY,
                        help="Path to RELATIONSHIP_REGISTRY.csv")
    args = parser.parse_args()

    if args.sample or not args.data:
        print("Running validation with built-in sample (JPMorgan Chase, 2025-09-30)...")
        data = dict(SAMPLE_DATA)
    elif args.data.endswith(".json"):
        data = load_data_from_json(args.data)
    else:
        data = load_data_from_csv(args.data)

    rules = load_registry(args.registry)
    rules = filter_rules(rules, args.severity, args.only_confirmed, args.scope)
    results = [evaluate_rule(r, data) for r in rules]

    # Sort: failures first, then by severity, then rel_id -- so problems surface.
    status_rank = {"FAIL": 0, "SKIPPED": 1, "PASS": 2}
    results.sort(key=lambda r: (status_rank[r.status],
                                SEVERITY_ORDER.get(r.rule.severity, 9),
                                r.rule.rel_id))

    summary = print_report(results)
    raise SystemExit(1 if summary["critical_failures"] > 0 else 0)


if __name__ == "__main__":
    main()
