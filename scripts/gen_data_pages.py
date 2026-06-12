#!/usr/bin/env python3
"""Generate interactive DataTables pages from the key CSV catalogues.

For each source CSV this writes one Markdown page into ``docs/data/<slug>.md``
containing an HTML table (DataTables-initialised) plus a raw-CSV download link.
It also writes ``docs/data/index.md`` linking every generated page with its row
count. The pages are regenerated in CI before ``mkdocs build`` so they always
match the CSVs. Stdlib only.
"""

import csv
import html
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
CSV_DIR = REPO_ROOT / "csv"
OUT_DIR = REPO_ROOT / "docs" / "data"
RAW_BASE = "https://raw.githubusercontent.com/andenick/bank-data-dictionary/main/csv"

# (csv filename, human title, one-line description)
SOURCES = [
    ("COLLECTIONS_CATALOG.csv", "Collections Catalog",
     "Every regulatory collection (form family) in the dictionary, with regulator, filer, frequency and primary identifier."),
    ("SCHEDULES_CATALOG.csv", "Schedules Catalog",
     "All documented subschedules across every form, down to schedule id, title and form applicability."),
    ("MDRM_CROSSWALK_EXPANDED.csv", "MDRM Crosswalk (Expanded)",
     "Field-level MDRM crosswalk mapping codes and mnemonics across reporting forms and schedules."),
    ("MDRM_NAMESPACES.csv", "MDRM Namespaces",
     "MDRM namespaces describing form family, scope, consolidation and period for each code space."),
    ("MDRM_PREFIX_DEFINITIONS.csv", "MDRM Prefix Definitions",
     "Definitions of the MDRM code prefixes (mnemonics), their form, scope and typical use."),
    ("NIC_CODE_LISTS.csv", "NIC Code Lists",
     "National Information Center code lists describing bank corporate-structure attributes and relationships."),
    ("IDENTIFIERS.csv", "Entity Identifiers",
     "The entity-identifier crosswalk reconciling RSSD, FDIC Cert, LEI and other keys across sources."),
    ("CODE_VALIDATION_AUDIT.csv", "Code Validation Audit",
     "Per-code validation audit recording the status and source files for every MDRM code."),
    ("RELATIONSHIP_REGISTRY.csv", "Relationship Registry (empirically tested)",
     "Every reconciliation identity and bound in the dictionary — official FR Y-9C and Call "
     "Report edit checks plus curated identities — with its expression, source, and (where "
     "machine-testable) the empirical verdict, observation count and pass rate against 208 "
     "million FR Y-9C rows and 1.9 billion Call Report rows of real filings."),
    ("EDIT_HISTORY.csv", "Official Edit History (2001-2026)",
     "Lifetime of every official Call Report edit label across 30 CDR taxonomy cycles: rule "
     "type, forms, first/last cycle observed, and the number of expression revisions."),
]


def slug_for(filename: str) -> str:
    return filename[:-4].lower() if filename.lower().endswith(".csv") else filename.lower()


def table_id_for(slug: str) -> str:
    return "dt-" + slug.replace("_", "-")


def read_csv(path: Path):
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.reader(fh)
        rows = list(reader)
    if not rows:
        return [], []
    return rows[0], rows[1:]


def build_table_html(table_id: str, header, data_rows) -> str:
    parts = [f'<table id="{table_id}" class="data-table display" style="width:100%">']
    parts.append("<thead><tr>")
    for col in header:
        parts.append(f"<th>{html.escape(col)}</th>")
    parts.append("</tr></thead>")
    parts.append("<tbody>")
    for row in data_rows:
        parts.append("<tr>")
        # Normalise ragged rows to header width.
        cells = list(row) + [""] * (len(header) - len(row))
        for cell in cells[: len(header)]:
            parts.append(f"<td>{html.escape(cell)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "".join(parts)


def write_page(filename, title, description):
    src = CSV_DIR / filename
    header, data_rows = read_csv(src)
    slug = slug_for(filename)
    table_id = table_id_for(slug)
    raw_url = f"{RAW_BASE}/{filename}"

    table_html = build_table_html(table_id, header, data_rows)
    init_js = (
        "<script>\n"
        "  document.addEventListener('DOMContentLoaded', function () {\n"
        f"    if (window.jQuery && jQuery.fn.dataTable && !jQuery.fn.dataTable.isDataTable('#{table_id}')) {{\n"
        f"      jQuery('#{table_id}').DataTable({{\n"
        "        paging: true,\n"
        "        searching: true,\n"
        "        ordering: true,\n"
        "        pageLength: 25,\n"
        "        lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, 'All']]\n"
        "      });\n"
        "    }\n"
        "  });\n"
        "</script>"
    )

    md = (
        f"# {title}\n\n"
        f"{description}\n\n"
        f"**{len(data_rows):,} rows.** "
        f"[Download the raw CSV]({raw_url}) from the repository.\n\n"
        f"{table_html}\n\n"
        f"{init_js}\n"
    )
    out_path = OUT_DIR / f"{slug}.md"
    out_path.write_text(md, encoding="utf-8")
    return slug, len(data_rows)


def write_index(entries):
    lines = [
        "# Data tables",
        "",
        "Browse the dictionary's key catalogues as interactive, searchable and sortable",
        "tables. Each table is generated directly from the source CSV in the repository,",
        "so it always matches the published data. Use the search box to filter, click a",
        "column header to sort, and the download link on each page for the raw CSV.",
        "",
        "| Catalogue | Rows |",
        "| --- | ---: |",
    ]
    for slug, title, rows in entries:
        lines.append(f"| [{title}]({slug}.md) | {rows:,} |")
    lines.append("")
    (OUT_DIR / "index.md").write_text("\n".join(lines), encoding="utf-8")


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    for filename, title, description in SOURCES:
        src = CSV_DIR / filename
        if not src.exists():
            print(f"  skip (missing): {filename}")
            continue
        slug, rows = write_page(filename, title, description)
        entries.append((slug, title, rows))
        print(f"  wrote docs/data/{slug}.md ({rows} rows)")
    write_index(entries)
    print(f"  wrote docs/data/index.md ({len(entries)} tables)")


if __name__ == "__main__":
    main()
