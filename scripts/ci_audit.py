#!/usr/bin/env python3
"""CI freshness guard: fail the build if any shipped MDRM-code-shaped token is invalid.

Validates every code-shaped token in csv/, json/, docs/ (excluding the audit artifacts,
which record bad codes by design) against the committed slim code set
``ci/mdrm_codes.txt.gz`` (mnemonic+item pairs from the Federal Reserve MDRM).

Exit codes: 0 = all valid; 1 = invalid tokens found (listed on stdout).

The IGNORE whitelist below mirrors the maintainers' audit tooling: tokens that match the
8-character pattern but are NOT MDRM codes (form names and attribute names appearing
inside verbatim official text, plus quoted form-number literals).
"""
import glob
import gzip
import os
import re
import sys

REPO = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
TOKEN = re.compile(r"\b[A-Z]{4}[A-Z0-9]{4}\b")
HASDIGIT = re.compile(r"[0-9]")

IGNORE = {
    # NIC / external attribute names and form names inside verbatim official text
    "ARID2017", "CHCLASS1", "RESTYPE1", "SVRR3491",
    "BONB6798", "BONB6799", "BONB6800", "RSSD9204", "TEXT9005",
    "FFIEC009", "FFIEC101", "FFIEC031", "FFIEC041", "FFIEC051",
    "BHCK0364",
}

SKIP_SUFFIXES = (
    "CODE_VALIDATION_AUDIT.csv", "CODE_REMEDIATION_LOG.csv",
    os.path.join("docs", "data", "code_validation_audit.md"),
)


def main() -> int:
    with gzip.open(os.path.join(REPO, "ci", "mdrm_codes.txt.gz"), "rt", encoding="utf-8") as fh:
        codes = set(fh.read().split())
    # UBPR concepts are defined by the official CDR UBPR taxonomy (not all appear in
    # MDRM's UBPR section); UBPR/UBPK/UBPS tokens validate against this set instead.
    with gzip.open(os.path.join(REPO, "ci", "ubpr_concepts.txt.gz"), "rt", encoding="utf-8") as fh:
        codes |= set(fh.read().split())
    mnems = {c[:4] for c in codes}
    bad = {}
    for pattern in ("csv/*.csv", "json/*.json", "docs/**/*.md", "README.md"):
        for path in glob.glob(os.path.join(REPO, pattern), recursive=True):
            norm = path.replace("\\", "/")
            if any(norm.endswith(s.replace("\\", "/")) for s in SKIP_SUFFIXES):
                continue
            try:
                text = open(path, encoding="utf-8", errors="replace").read()
            except OSError:
                continue
            rel = os.path.relpath(path, REPO)
            for m in TOKEN.finditer(text):
                t = m.group(0)
                if t in IGNORE or t in codes:
                    continue
                if t[:4] in mnems and HASDIGIT.search(t[4:]):
                    bad.setdefault(t, set()).add(rel)
    if bad:
        print(f"CI AUDIT FAIL: {len(bad)} invalid MDRM token(s):")
        for t in sorted(bad):
            print(f"  {t} -> {', '.join(sorted(bad[t])[:4])}")
        return 1
    print(f"CI audit OK: all code tokens valid against {len(codes):,} MDRM codes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
