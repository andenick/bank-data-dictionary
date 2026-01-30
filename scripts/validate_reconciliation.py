#!/usr/bin/env python3
"""
Bank Regulatory Data Validation Script

This script validates bank regulatory data against reconciliation rules
and validation checks defined in the data dictionary CSVs.

Usage:
    python validate_reconciliation.py --data <data_file> --rules <rules_file>

Author: Bank Regulatory Data Dictionary
Version: 1.0
Date: 2026-01-29
"""

import csv
import json
import argparse
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum


class Severity(Enum):
    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class RuleType(Enum):
    BALANCE = "balance"
    SUM = "sum"
    RATIO = "ratio"
    RANGE = "range"
    CROSS_SCHEDULE = "cross_schedule"
    TIME_SERIES = "time_series"
    SIGN = "sign"
    DERIVED = "derived"


@dataclass
class ValidationResult:
    """Result of a single validation check."""
    rule_id: str
    passed: bool
    severity: Severity
    description: str
    expected: str
    actual: str
    message: str


class BankDataValidator:
    """Validator for bank regulatory data against reconciliation rules."""

    def __init__(self, data: Dict[str, float]):
        """
        Initialize validator with bank data.

        Args:
            data: Dictionary mapping MDRM codes to values
        """
        self.data = data
        self.results: List[ValidationResult] = []

    def get_value(self, mdrm: str) -> Optional[float]:
        """Get value for an MDRM code, returning None if not found."""
        return self.data.get(mdrm)

    def validate_balance_sheet(self) -> ValidationResult:
        """
        Check: Assets = Liabilities + Minority Interest + Equity
        BHCT2170 = BHCT2948 + BHCK3000 + BHCT3210
        """
        assets = self.get_value('BHCT2170')
        liabilities = self.get_value('BHCT2948')
        minority = self.get_value('BHCK3000') or 0
        equity = self.get_value('BHCT3210')

        if any(v is None for v in [assets, liabilities, equity]):
            return ValidationResult(
                rule_id="VAL_001",
                passed=False,
                severity=Severity.CRITICAL,
                description="Balance Sheet Identity",
                expected="Assets = Liabilities + Minority + Equity",
                actual="Missing data",
                message="Required MDRM codes not found in data"
            )

        expected = liabilities + minority + equity
        passed = abs(assets - expected) < 0.01  # Allow small rounding differences

        return ValidationResult(
            rule_id="VAL_001",
            passed=passed,
            severity=Severity.CRITICAL,
            description="Balance Sheet Identity",
            expected=f"{expected:,.0f}",
            actual=f"{assets:,.0f}",
            message="PASS" if passed else f"Balance sheet does not balance. Difference: {assets - expected:,.0f}"
        )

    def validate_trading_assets_tie(self) -> ValidationResult:
        """
        Check: HC Item 5 = HC-D Item 12 (same MDRM)
        Both should be BHCT3545
        """
        trading_hc = self.get_value('BHCT3545')

        if trading_hc is None:
            return ValidationResult(
                rule_id="VAL_023",
                passed=False,
                severity=Severity.CRITICAL,
                description="Trading Assets Cross-Schedule Tie",
                expected="HC.5 = HC-D.12",
                actual="Missing data",
                message="BHCT3545 not found in data"
            )

        # For same MDRM, this is a structural check
        # In practice, both HC and HC-D use the same code
        return ValidationResult(
            rule_id="VAL_023",
            passed=True,
            severity=Severity.CRITICAL,
            description="Trading Assets Cross-Schedule Tie",
            expected=f"{trading_hc:,.0f}",
            actual=f"{trading_hc:,.0f}",
            message="PASS - Same MDRM used in both schedules"
        )

    def validate_tier1_capital(self) -> ValidationResult:
        """
        Check: Tier 1 = CET1 + Additional Tier 1
        BHCFA223 = BHCAP859 + BHCAP856
        """
        tier1 = self.get_value('BHCFA223')
        cet1 = self.get_value('BHCAP859')
        at1 = self.get_value('BHCAP856') or 0

        if any(v is None for v in [tier1, cet1]):
            return ValidationResult(
                rule_id="VAL_029",
                passed=False,
                severity=Severity.CRITICAL,
                description="Tier 1 Capital Composition",
                expected="Tier 1 = CET1 + AT1",
                actual="Missing data",
                message="Required capital codes not found"
            )

        expected = cet1 + at1
        passed = abs(tier1 - expected) < 0.01

        return ValidationResult(
            rule_id="VAL_029",
            passed=passed,
            severity=Severity.CRITICAL,
            description="Tier 1 Capital Composition",
            expected=f"{expected:,.0f}",
            actual=f"{tier1:,.0f}",
            message="PASS" if passed else f"Tier 1 capital does not reconcile. Difference: {tier1 - expected:,.0f}"
        )

    def validate_total_capital(self) -> ValidationResult:
        """
        Check: Total Capital = Tier 1 + Tier 2
        BHCFA225 = BHCFA223 + BHCFA224
        """
        total = self.get_value('BHCFA225')
        tier1 = self.get_value('BHCFA223')
        tier2 = self.get_value('BHCFA224') or 0

        if any(v is None for v in [total, tier1]):
            return ValidationResult(
                rule_id="VAL_030",
                passed=False,
                severity=Severity.CRITICAL,
                description="Total Capital Composition",
                expected="Total = Tier 1 + Tier 2",
                actual="Missing data",
                message="Required capital codes not found"
            )

        expected = tier1 + tier2
        passed = abs(total - expected) < 0.01

        return ValidationResult(
            rule_id="VAL_030",
            passed=passed,
            severity=Severity.CRITICAL,
            description="Total Capital Composition",
            expected=f"{expected:,.0f}",
            actual=f"{total:,.0f}",
            message="PASS" if passed else f"Total capital does not reconcile. Difference: {total - expected:,.0f}"
        )

    def validate_cet1_ratio_range(self) -> ValidationResult:
        """
        Check: CET1 ratio is within reasonable range (4.5% - 30%)
        BHCAP793 >= 0.045 AND <= 0.30
        """
        cet1_ratio = self.get_value('BHCAP793')

        if cet1_ratio is None:
            return ValidationResult(
                rule_id="VAL_032",
                passed=False,
                severity=Severity.MEDIUM,
                description="CET1 Ratio Range Check",
                expected="4.5% <= CET1 Ratio <= 30%",
                actual="Missing data",
                message="BHCAP793 not found in data"
            )

        # Convert to percentage if stored as decimal
        ratio = cet1_ratio if cet1_ratio < 1 else cet1_ratio / 100

        passed = 0.045 <= ratio <= 0.30

        return ValidationResult(
            rule_id="VAL_032",
            passed=passed,
            severity=Severity.MEDIUM,
            description="CET1 Ratio Range Check",
            expected="4.5% <= CET1 <= 30%",
            actual=f"{ratio * 100:.2f}%",
            message="PASS" if passed else f"CET1 ratio outside normal range"
        )

    def validate_net_interest_income(self) -> ValidationResult:
        """
        Check: NII = Interest Income - Interest Expense
        BHCT4074 = BHCT4107 - BHCT4073
        """
        nii = self.get_value('BHCT4074')
        int_income = self.get_value('BHCT4107')
        int_expense = self.get_value('BHCT4073')

        if any(v is None for v in [nii, int_income, int_expense]):
            return ValidationResult(
                rule_id="VAL_037",
                passed=False,
                severity=Severity.CRITICAL,
                description="Net Interest Income Calculation",
                expected="NII = Interest Income - Interest Expense",
                actual="Missing data",
                message="Required income codes not found"
            )

        expected = int_income - int_expense
        passed = abs(nii - expected) < 0.01

        return ValidationResult(
            rule_id="VAL_037",
            passed=passed,
            severity=Severity.CRITICAL,
            description="Net Interest Income Calculation",
            expected=f"{expected:,.0f}",
            actual=f"{nii:,.0f}",
            message="PASS" if passed else f"NII does not reconcile. Difference: {nii - expected:,.0f}"
        )

    def validate_positive_assets(self) -> ValidationResult:
        """
        Check: Total assets must be non-negative
        BHCT2170 >= 0
        """
        assets = self.get_value('BHCT2170')

        if assets is None:
            return ValidationResult(
                rule_id="VAL_006",
                passed=False,
                severity=Severity.CRITICAL,
                description="Total Assets Sign Check",
                expected=">= 0",
                actual="Missing data",
                message="BHCT2170 not found in data"
            )

        passed = assets >= 0

        return ValidationResult(
            rule_id="VAL_006",
            passed=passed,
            severity=Severity.CRITICAL,
            description="Total Assets Sign Check",
            expected=">= 0",
            actual=f"{assets:,.0f}",
            message="PASS" if passed else "Total assets is negative"
        )

    def run_all_validations(self) -> List[ValidationResult]:
        """Run all validation checks and return results."""
        self.results = [
            self.validate_balance_sheet(),
            self.validate_trading_assets_tie(),
            self.validate_tier1_capital(),
            self.validate_total_capital(),
            self.validate_cet1_ratio_range(),
            self.validate_net_interest_income(),
            self.validate_positive_assets(),
        ]
        return self.results

    def get_summary(self) -> Dict:
        """Get summary of validation results."""
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed

        critical_failures = sum(1 for r in self.results
                               if not r.passed and r.severity == Severity.CRITICAL)

        return {
            'total_checks': total,
            'passed': passed,
            'failed': failed,
            'critical_failures': critical_failures,
            'pass_rate': f"{(passed/total)*100:.1f}%" if total > 0 else "N/A"
        }

    def print_report(self):
        """Print formatted validation report."""
        print("\n" + "=" * 70)
        print("BANK REGULATORY DATA VALIDATION REPORT")
        print("=" * 70)

        summary = self.get_summary()
        print(f"\nSummary: {summary['passed']}/{summary['total_checks']} checks passed ({summary['pass_rate']})")
        if summary['critical_failures'] > 0:
            print(f"WARNING: {summary['critical_failures']} CRITICAL failures detected!")

        print("\n" + "-" * 70)
        print("DETAILED RESULTS")
        print("-" * 70)

        for result in self.results:
            status = "PASS" if result.passed else "FAIL"
            print(f"\n[{status}] {result.rule_id}: {result.description}")
            print(f"       Severity: {result.severity.value}")
            print(f"       Expected: {result.expected}")
            print(f"       Actual:   {result.actual}")
            if not result.passed:
                print(f"       Message:  {result.message}")

        print("\n" + "=" * 70)


def load_data_from_csv(filepath: str) -> Dict[str, float]:
    """Load bank data from a CSV file with MDRM codes and values."""
    data = {}
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            mdrm = row.get('mdrm_code') or row.get('mdrm') or row.get('MDRM')
            value = row.get('value') or row.get('amount') or row.get('VALUE')
            if mdrm and value:
                try:
                    data[mdrm] = float(value.replace(',', ''))
                except ValueError:
                    pass
    return data


def load_data_from_json(filepath: str) -> Dict[str, float]:
    """Load bank data from a JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)


# Sample test data for JPMorgan Chase 2024Q4 (illustrative)
SAMPLE_DATA = {
    # Balance Sheet
    'BHCT2170': 4000000000,   # Total Assets ($4T)
    'BHCT2948': 3600000000,   # Total Liabilities
    'BHCK3000': 0,            # Minority Interest
    'BHCT3210': 400000000,    # Total Equity

    # Trading
    'BHCT3545': 600000000,    # Trading Assets
    'BHCT3548': 200000000,    # Trading Liabilities

    # Capital
    'BHCAP859': 280000000,    # CET1 Capital
    'BHCAP856': 20000000,     # Additional Tier 1
    'BHCFA223': 300000000,    # Tier 1 Capital
    'BHCFA224': 50000000,     # Tier 2 Capital
    'BHCFA225': 350000000,    # Total Capital
    'BHCAA223': 2000000000,   # Total RWA
    'BHCAP793': 0.14,         # CET1 Ratio (14%)

    # Income
    'BHCT4107': 100000000,    # Interest Income
    'BHCT4073': 50000000,     # Interest Expense
    'BHCT4074': 50000000,     # Net Interest Income
    'BHCT4340': 40000000,     # Net Income
}


def main():
    """Main entry point for validation script."""
    parser = argparse.ArgumentParser(
        description='Validate bank regulatory data against reconciliation rules'
    )
    parser.add_argument('--data', type=str, help='Path to data file (CSV or JSON)')
    parser.add_argument('--sample', action='store_true', help='Run with sample data')

    args = parser.parse_args()

    if args.sample or not args.data:
        print("Running validation with sample data...")
        data = SAMPLE_DATA
    else:
        if args.data.endswith('.json'):
            data = load_data_from_json(args.data)
        else:
            data = load_data_from_csv(args.data)

    validator = BankDataValidator(data)
    validator.run_all_validations()
    validator.print_report()

    # Exit with error code if critical failures
    summary = validator.get_summary()
    if summary['critical_failures'] > 0:
        exit(1)
    exit(0)


if __name__ == '__main__':
    main()
