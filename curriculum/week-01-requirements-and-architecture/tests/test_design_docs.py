"""Week 01 validation: the design documents have the structure later weeks need.

Run with:  make test-week WEEK=week-01-requirements-and-architecture

These tests check structure, not prose: the required sections exist, the
requirement identifiers are well formed and numerous enough, the risk register
is populated, the architecture document carries a three-tier Mermaid diagram,
and no skeleton ``TODO:`` marker is left behind. A human grades the writing with
the rubric in README section 16.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
DOCS = REPO_ROOT / "docs"
PROBLEM_STATEMENT = DOCS / "01_problem_statement.md"
REQUIREMENTS = DOCS / "02_requirements.md"
ARCHITECTURE = DOCS / "03_architecture.md"

WEEK = "week-01-requirements-and-architecture"

MIN_FUNCTIONAL = 12
MIN_NON_FUNCTIONAL = 8
MIN_RISKS = 6
MIN_ACTORS = 5
MIN_RESPONSIBILITIES = 8

PRIORITIES = {"MUST", "SHOULD", "COULD"}
LIKELIHOODS = {"LOW", "MEDIUM", "HIGH"}


def read(path: Path) -> str:
    """Return the text of a required document, failing with a usable message."""
    if not path.exists():
        pytest.fail(
            f"{path.relative_to(REPO_ROOT)} does not exist. "
            f"It is a deliverable of curriculum/{WEEK}/ (README sections 6-7)."
        )
    return path.read_text(encoding="utf-8")


def section(text: str, *keywords: str) -> str:
    """Return the body of the first ``##`` section whose heading holds every keyword."""
    parts = re.split(r"^## ", text, flags=re.MULTILINE)
    for part in parts[1:]:
        heading = part.splitlines()[0].lower()
        if all(keyword in heading for keyword in keywords):
            return part
    return ""


def table_rows(text: str, prefix: str) -> list[list[str]]:
    """Return markdown table rows whose first cell is an ID like ``FR-07``."""
    rows = []
    pattern = re.compile(rf"^\|\s*{prefix}-\d+\s*\|", re.MULTILINE)
    for line in text.splitlines():
        if pattern.match(line):
            cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows


def identifiers(rows: list[list[str]]) -> list[str]:
    return [row[0] for row in rows]


def assert_ids_are_consecutive(ids: list[str], prefix: str) -> None:
    numbers = [int(identifier.split("-")[1]) for identifier in ids]
    duplicates = {n for n in numbers if numbers.count(n) > 1}
    assert not duplicates, f"Duplicate {prefix} identifiers: {sorted(duplicates)}."
    assert numbers == sorted(numbers), f"{prefix} identifiers are out of order: {ids}."
    expected = list(range(1, len(numbers) + 1))
    assert numbers == expected, (
        f"{prefix} identifiers must run consecutively from {prefix}-01 with no gaps; found {ids}."
    )


def headings(text: str) -> list[str]:
    return [line.lstrip("#").strip().lower() for line in text.splitlines() if line.startswith("#")]


def has_heading(text: str, *keywords: str) -> bool:
    return any(all(keyword in heading for keyword in keywords) for heading in headings(text))


# --------------------------------------------------------------------------- #
# docs/01_problem_statement.md
# --------------------------------------------------------------------------- #


def test_problem_statement_has_required_sections():
    text = read(PROBLEM_STATEMENT)
    for keywords in (("problem",), ("scope",), ("actors",), ("objectives",), ("success",)):
        assert has_heading(text, *keywords), (
            f"docs/01_problem_statement.md is missing a heading about {keywords[0]!r} "
            "(README section 6)."
        )


def test_problem_statement_lists_actors():
    text = read(PROBLEM_STATEMENT)
    section = text.split("## 5. Actors", 1)
    assert len(section) == 2, "docs/01_problem_statement.md must keep the '## 5. Actors' heading."
    body = section[1].split("\n## ", 1)[0]
    rows = [line for line in body.splitlines() if line.startswith("|")]
    data_rows = [row for row in rows[2:] if row.strip("| ")]
    assert len(data_rows) >= MIN_ACTORS, (
        f"docs/01_problem_statement.md lists {len(data_rows)} actors; "
        f"at least {MIN_ACTORS} are required (README section 5.5)."
    )


def test_problem_statement_keeps_the_educational_use_statement():
    text = read(PROBLEM_STATEMENT).lower()
    assert "educational use only" in text, (
        "docs/01_problem_statement.md must repeat the educational-use statement from README.md."
    )


def test_problem_statement_has_no_todo_markers():
    text = read(PROBLEM_STATEMENT)
    assert "TODO:" not in text, (
        "docs/01_problem_statement.md still contains TODO: markers; "
        "every marker must be replaced (README section 6)."
    )


# --------------------------------------------------------------------------- #
# docs/02_requirements.md
# --------------------------------------------------------------------------- #


def functional_rows() -> list[list[str]]:
    return table_rows(section(read(REQUIREMENTS), "functional requirements"), "FR")


def non_functional_rows() -> list[list[str]]:
    return table_rows(section(read(REQUIREMENTS), "non-functional requirements"), "NFR")


def risk_rows() -> list[list[str]]:
    return table_rows(section(read(REQUIREMENTS), "risk register"), "RISK")


def test_functional_requirements_present():
    rows = functional_rows()
    assert len(rows) >= MIN_FUNCTIONAL, (
        f"docs/02_requirements.md defines {len(rows)} functional requirements; "
        f"at least {MIN_FUNCTIONAL} are required (README section 7A)."
    )
    assert_ids_are_consecutive(identifiers(rows), "FR")


def test_functional_requirements_are_complete_rows():
    for row in functional_rows():
        identifier = row[0]
        assert len(row) >= 5, (
            f"{identifier} must have the columns: ID, requirement, actor, priority, verified by."
        )
        requirement, actor, priority, verified = row[1], row[2], row[3], row[4]
        assert len(requirement.split()) >= 8, f"{identifier} is too short to be a requirement."
        assert actor and "TODO" not in actor, f"{identifier} does not name an actor."
        assert priority.upper() in PRIORITIES, (
            f"{identifier} has priority {priority!r}; expected one of {sorted(PRIORITIES)}."
        )
        assert verified and "TODO" not in verified, (
            f"{identifier} does not state how it will be verified."
        )


def test_non_functional_requirements_present():
    rows = non_functional_rows()
    assert len(rows) >= MIN_NON_FUNCTIONAL, (
        f"docs/02_requirements.md defines {len(rows)} non-functional requirements; "
        f"at least {MIN_NON_FUNCTIONAL} are required (README section 7A)."
    )
    assert_ids_are_consecutive(identifiers(rows), "NFR")


def test_non_functional_requirements_are_measurable():
    for row in non_functional_rows():
        identifier = row[0]
        assert len(row) >= 5, (
            f"{identifier} must have the columns: ID, category, requirement, "
            "metric and threshold, verified by."
        )
        metric, verified = row[3], row[4]
        assert re.search(r"\d", metric), (
            f"{identifier} has no number in its metric column: {metric!r}. "
            "A non-functional requirement without a threshold is not testable "
            "(README section 5.6, test 2)."
        )
        assert verified and "TODO" not in verified, (
            f"{identifier} does not state how it will be measured."
        )


def test_non_functional_requirements_cover_the_required_categories():
    rows = non_functional_rows()
    categories = " ".join(row[1].lower() for row in rows if len(row) > 1)
    for required in (
        "performance",
        "integrity",
        "security",
        "maintainability",
        "reproducibility",
    ):
        assert required in categories, (
            f"No non-functional requirement is categorised {required!r} (README section 7A)."
        )


def test_risk_register_present():
    rows = risk_rows()
    assert len(rows) >= MIN_RISKS, (
        f"docs/02_requirements.md records {len(rows)} risks; "
        f"at least {MIN_RISKS} are required (README section 7A)."
    )
    assert_ids_are_consecutive(identifiers(rows), "RISK")
    for row in rows:
        assert len(row) >= 6, (
            f"{row[0]} must have the columns: ID, risk, likelihood, impact, mitigation, owner."
        )
        assert row[2].upper() in LIKELIHOODS, (
            f"{row[0]} has likelihood {row[2]!r}; expected one of {sorted(LIKELIHOODS)}."
        )
        assert row[3].upper() in LIKELIHOODS, (
            f"{row[0]} has impact {row[3]!r}; expected one of {sorted(LIKELIHOODS)}."
        )


def test_requirements_document_has_traceability_and_definition_of_done():
    text = read(REQUIREMENTS)
    assert has_heading(text, "traceability"), (
        "docs/02_requirements.md must keep the traceability section (README section 7A)."
    )
    assert has_heading(text, "definition", "done"), (
        "docs/02_requirements.md must end with a definition of done (README section 7A)."
    )


def test_requirements_document_has_no_todo_markers():
    text = read(REQUIREMENTS)
    assert "TODO:" not in text, (
        "docs/02_requirements.md still contains TODO: markers; "
        "every marker must be replaced (README section 7A)."
    )


# --------------------------------------------------------------------------- #
# docs/03_architecture.md
# --------------------------------------------------------------------------- #


def test_architecture_has_a_three_tier_mermaid_diagram():
    text = read(ARCHITECTURE)
    blocks = re.findall(r"```mermaid\n(.*?)```", text, flags=re.DOTALL)
    assert blocks, (
        "docs/03_architecture.md must contain a ```mermaid``` diagram of the three tiers "
        "(README section 7B)."
    )
    diagram = "\n".join(blocks).lower()
    for tier in ("presentation", "application", "data"):
        assert tier in diagram, f"The Mermaid diagram does not name the {tier} tier."
    assert "-->" in diagram, "The Mermaid diagram has no arrows between the tiers."


def test_architecture_has_required_sections():
    text = read(ARCHITECTURE)
    for label, keywords in (
        ("two-tier versus three-tier", ("two-tier",)),
        ("responsibilities by tier", ("responsibilit",)),
        ("file system versus DBMS", ("dbms",)),
        ("data-flow narrative", ("data-flow",)),
        ("levels of abstraction", ("abstraction",)),
    ):
        assert has_heading(text, *keywords), (
            f"docs/03_architecture.md is missing the {label} section (README section 7B)."
        )


def test_architecture_compares_all_six_file_versus_dbms_dimensions():
    text = read(ARCHITECTURE).lower()
    for dimension in (
        "redundancy",
        "isolation",
        "integrity",
        "atomicity",
        "concurrent access",
    ):
        assert dimension in text, (
            f"docs/03_architecture.md does not discuss {dimension!r} in the "
            "file-system versus DBMS comparison (README section 5.1)."
        )


def test_architecture_assigns_enough_responsibilities():
    text = read(ARCHITECTURE)
    owners = re.findall(r"^\|[^|\n]+\|\s*(Data|Application|ML|Presentation)\s*\|", text, re.M)
    assert len(owners) >= MIN_RESPONSIBILITIES, (
        f"docs/03_architecture.md assigns {len(owners)} responsibilities to a tier; "
        f"at least {MIN_RESPONSIBILITIES} are required, each owned by one of "
        "Data, Application, ML or Presentation (README section 7B)."
    )


def test_architecture_covers_data_independence():
    text = read(ARCHITECTURE).lower()
    assert "physical data independence" in text and "logical data independence" in text, (
        "docs/03_architecture.md must give one example each of physical and logical "
        "data independence (README section 5.2)."
    )


def test_architecture_has_no_todo_markers():
    text = read(ARCHITECTURE)
    assert "TODO:" not in text, (
        "docs/03_architecture.md still contains TODO: markers; "
        "every marker must be replaced (README section 7B)."
    )
