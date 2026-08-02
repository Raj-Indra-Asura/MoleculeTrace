"""Week 02 validation: the conceptual model has the structure later weeks need.

Run with:  make test-week WEEK=week-02-er-and-eer-design

These tests check structure, not design taste: both diagrams exist as Mermaid
source, all sixteen domain concepts are accounted for, the cardinality table
uses legal values and covers enough relationships, participation is stated on
both sides of every relationship, the weak-entity and specialisation arguments
are arguments rather than assertions, every relationship has a plain-language
narrative, and the design-decision log is populated. A human grades the model
itself with the rubric in README section 16 and the reference description in
``instructor/solution-notes/week-02.md``.
"""

from __future__ import annotations

import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
DATA_MODEL = REPO_ROOT / "docs" / "data-model.md"

WEEK = "week-02-er-and-eer-design"

CONCEPTS = (
    "UserAccount",
    "Role",
    "Molecule",
    "MoleculeSynonym",
    "DescriptorType",
    "MoleculeDescriptor",
    "BiologicalTarget",
    "Assay",
    "ActivityObservation",
    "Dataset",
    "DatasetVersion",
    "Experiment",
    "ModelVersion",
    "Prediction",
    "PredictionValidation",
    "AuditLog",
)

CARDINALITIES = {"1:1", "1:N", "M:N"}
PARTICIPATIONS = {"total", "partial"}

MIN_ONE_TO_ONE = 1
MIN_ONE_TO_MANY = 6
MIN_MANY_TO_MANY = 2
MIN_DECISIONS = 8
MIN_BEFORE_AFTER = 6
MIN_ATTRIBUTES = 20
MIN_WEAK_ENTITY_WORDS = 200

JARGON = ("foreign key", "many-to-many", "join", "table")


def read() -> str:
    """Return the text of the week's deliverable, failing with a usable message."""
    if not DATA_MODEL.exists():
        pytest.fail(
            f"{DATA_MODEL.relative_to(REPO_ROOT)} does not exist. "
            f"It is the deliverable of curriculum/{WEEK}/ (README sections 6-7)."
        )
    return DATA_MODEL.read_text(encoding="utf-8")


def section(text: str, *keywords: str) -> str:
    """Return the body of the first ``##`` section whose heading holds every keyword."""
    parts = re.split(r"^## ", text, flags=re.MULTILINE)
    for part in parts[1:]:
        heading = part.splitlines()[0].lower()
        if all(keyword in heading for keyword in keywords):
            return part
    return ""


def rows(text: str) -> list[list[str]]:
    """Return the data rows of every markdown table in ``text``."""
    parsed = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|"):
            continue
        cells = [cell.strip() for cell in stripped.strip("|").split("|")]
        if all(set(cell) <= {"-", ":"} and cell for cell in cells):
            continue
        parsed.append(cells)
    return parsed


def cardinality_rows(text: str) -> list[list[str]]:
    """Return rows of the cardinality table, recognised by their cardinality cell."""
    return [row for row in rows(section(text, "cardinality")) if set(row) & CARDINALITIES]


def participation_rows(text: str) -> list[list[str]]:
    """Return rows of the participation table, recognised by two participation cells."""
    found = []
    for row in rows(section(text, "participation")):
        cells = [cell.lower() for cell in row]
        if sum(cell in PARTICIPATIONS for cell in cells) >= 1:
            found.append(row)
    return found


def decision_rows(text: str) -> list[list[str]]:
    return [row for row in rows(text) if re.fullmatch(r"DD-\d+", row[0])]


def relationship_names(text: str) -> list[str]:
    return [row[0] for row in cardinality_rows(text)]


def headings(text: str) -> list[str]:
    return [line.lstrip("#").strip().lower() for line in text.splitlines() if line.startswith("#")]


def has_heading(text: str, *keywords: str) -> bool:
    return any(all(keyword in heading for keyword in keywords) for heading in headings(text))


# --------------------------------------------------------------------------- #
# Document structure
# --------------------------------------------------------------------------- #


def test_data_model_has_required_sections():
    text = read()
    for label, keywords in (
        ("concept inventory", ("concept",)),
        ("initial ER model", ("initial",)),
        ("attribute classification", ("attribute",)),
        ("improved EER model", ("improved",)),
        ("cardinality table", ("cardinality",)),
        ("participation constraints", ("participation",)),
        ("DatasetVersion weak entity", ("weak",)),
        ("user and role specialisation", ("specialis",)),
        ("relationship narratives", ("narrative",)),
        ("design-decision log", ("decision",)),
    ):
        assert has_heading(text, *keywords), (
            f"docs/data-model.md is missing the {label} section (README sections 6-7)."
        )


def test_all_sixteen_concepts_are_accounted_for():
    text = read()
    missing = [concept for concept in CONCEPTS if concept not in text]
    assert not missing, (
        f"docs/data-model.md never mentions {missing}. Every one of the sixteen "
        "concepts in README section 5.1 must be classified in section 1."
    )


def test_both_diagrams_are_present_as_mermaid_source():
    blocks = re.findall(r"```mermaid\n(.*?)```", read(), flags=re.DOTALL)
    assert len(blocks) >= 2, (
        f"docs/data-model.md contains {len(blocks)} Mermaid diagrams; the initial ER model "
        "(section 2) and the improved EER model (section 4) are both required."
    )
    for index, block in enumerate(blocks[:2], start=1):
        assert "erDiagram" in block, f"Mermaid diagram {index} is not an erDiagram."
        assert "--" in block, (
            f"Mermaid diagram {index} draws no relationships; a model without "
            "relationships is a list, not an ER diagram."
        )


def test_before_and_after_list_is_populated():
    body = section(read(), "improved")
    differences = [
        row
        for row in rows(body)
        if len(row) >= 4 and re.fullmatch(r"\d+", row[0]) and all(row[1:4])
    ]
    assert len(differences) >= MIN_BEFORE_AFTER, (
        f"docs/data-model.md lists {len(differences)} differences between the initial ER "
        f"model and the improved EER model; at least {MIN_BEFORE_AFTER} are required "
        "(README section 7A)."
    )


def test_attribute_classification_covers_every_attribute_kind():
    body = section(read(), "attribute").lower()
    for kind in ("composite", "multivalued", "derived", "key"):
        assert body.count(kind) >= 2, (
            f"The attribute-classification section labels fewer than two attributes "
            f"{kind!r} (README section 6, step 3)."
        )
    assert len(rows(body)) >= MIN_ATTRIBUTES, (
        f"The attribute-classification section has {len(rows(body))} rows; "
        f"at least {MIN_ATTRIBUTES} attributes are required."
    )


# --------------------------------------------------------------------------- #
# Cardinality
# --------------------------------------------------------------------------- #


def test_cardinality_table_covers_enough_relationships():
    found = cardinality_rows(read())
    assert found, (
        "docs/data-model.md declares no relationship with a cardinality of 1:1, 1:N or M:N "
        "(README section 7B)."
    )
    counts = {value: 0 for value in CARDINALITIES}
    for row in found:
        for cell in row:
            if cell in CARDINALITIES:
                counts[cell] += 1
                break
    for value, minimum in (
        ("1:1", MIN_ONE_TO_ONE),
        ("1:N", MIN_ONE_TO_MANY),
        ("M:N", MIN_MANY_TO_MANY),
    ):
        assert counts[value] >= minimum, (
            f"docs/data-model.md declares {counts[value]} relationships with a cardinality "
            f"of {value}; at least {minimum} are required (README section 7B)."
        )


def test_cardinality_rows_are_complete():
    for row in cardinality_rows(read()):
        name = row[0]
        assert len(row) >= 7, (
            f"Cardinality row {name!r} must have the columns: relationship, left entity, "
            "right entity, cardinality, domain rule, reading left to right, "
            "reading right to left."
        )
        assert all(cell for cell in row[:7]), f"Cardinality row {name!r} has an empty cell."
        assert len(row[4].split()) >= 5, (
            f"Cardinality row {name!r} states no domain rule. Cardinality follows from a "
            "fact about the world, not from convenience (README section 5.4)."
        )
        for reading in (row[5], row[6]):
            assert len(reading.split()) >= 5, (
                f"Cardinality row {name!r} is missing a plain-language reading in one "
                "direction (README section 5.3)."
            )


# --------------------------------------------------------------------------- #
# Participation
# --------------------------------------------------------------------------- #


def test_participation_is_stated_on_both_sides():
    found = participation_rows(read())
    assert found, (
        "docs/data-model.md states no participation constraints; each relationship needs a "
        "row with 'total' or 'partial' on both sides (README section 7C)."
    )
    for row in found:
        name = row[0]
        stated = [cell.lower() for cell in row if cell.lower() in PARTICIPATIONS]
        assert len(stated) >= 2, (
            f"Relationship {name!r} does not state participation for both sides; "
            "each cell must be 'total' or 'partial' (README section 7C)."
        )
        assert all(cell for cell in row), f"Participation row {name!r} has an empty cell."
        assert len(row[-1].split()) >= 5, (
            f"Participation row {name!r} does not say what the constraint forbids or "
            "deliberately allows (README section 5.5)."
        )


def test_every_relationship_has_a_participation_row():
    text = read()
    participation = section(text, "participation")
    missing = [name for name in relationship_names(text) if name not in participation]
    assert not missing, (
        f"These relationships appear in the cardinality table but not in the participation "
        f"table: {missing}. Both tables must cover the same relationships (CHECKPOINT.md)."
    )


# --------------------------------------------------------------------------- #
# Weak entities and specialisation
# --------------------------------------------------------------------------- #


def test_weak_entity_argument_is_complete():
    body = section(read(), "weak")
    words = len(body.split())
    assert words >= MIN_WEAK_ENTITY_WORDS, (
        f"The DatasetVersion weak-entity section is {words} words; at least "
        f"{MIN_WEAK_ENTITY_WORDS} are required (README section 7D)."
    )
    lowered = body.lower()
    for term in ("owner", "identifying relationship", "partial key"):
        assert term in lowered, (
            f"The weak-entity argument never mentions the {term}; a weak entity is defined "
            "by its owner, its identifying relationship and its partial key "
            "(README section 5.6)."
        )
    assert "datasetversion" in lowered.replace(" ", ""), (
        "The weak-entity section must argue about DatasetVersion by name."
    )


def test_specialisation_section_states_its_constraints():
    lowered = section(read(), "specialis").lower()
    assert lowered, "docs/data-model.md is missing the user and role specialisation section."
    assert "disjoint" in lowered or "overlapping" in lowered, (
        "The specialisation section must state whether the subclasses are disjoint or "
        "overlapping (README section 5.7)."
    )
    assert "total" in lowered or "partial" in lowered, (
        "The specialisation section must state whether the specialisation is total or "
        "partial (README section 5.7)."
    )
    assert "role" in lowered and "useraccount" in lowered.replace(" ", ""), (
        "The specialisation section must discuss UserAccount and Role by name "
        "(README section 7E)."
    )


# --------------------------------------------------------------------------- #
# Narratives and decisions
# --------------------------------------------------------------------------- #


def test_every_relationship_has_a_plain_language_narrative():
    text = read()
    narratives = section(text, "narrative")
    assert narratives, "docs/data-model.md is missing the relationship-narratives section."
    missing = [name for name in relationship_names(text) if name not in narratives]
    assert not missing, (
        f"These relationships have no plain-language narrative: {missing}. "
        "Every relationship must be explained in both directions (README section 7F)."
    )


def test_narratives_avoid_implementation_jargon():
    lowered = section(read(), "narrative").lower()
    used = [word for word in JARGON if word in lowered]
    assert not used, (
        f"The relationship narratives use implementation jargon: {used}. "
        "They must be readable by a bench scientist (README section 7F)."
    )


def test_design_decision_log_is_populated():
    found = decision_rows(read())
    assert len(found) >= MIN_DECISIONS, (
        f"docs/data-model.md records {len(found)} design decisions; at least "
        f"{MIN_DECISIONS} are required (README section 7G)."
    )
    numbers = [int(row[0].split("-")[1]) for row in found]
    assert numbers == list(range(1, len(numbers) + 1)), (
        f"Design-decision identifiers must run consecutively from DD-01 with no gaps; "
        f"found {[row[0] for row in found]}."
    )
    for row in found:
        assert len(row) >= 6, (
            f"{row[0]} must have the columns: ID, decision, alternatives, reason, "
            "consequence, requirement."
        )
        assert all(cell for cell in row[:5]), f"{row[0]} has an empty cell."
        assert len(row[2].split()) >= 2, (
            f"{row[0]} names no alternative. A decision without a rejected alternative "
            "is an assumption (README section 7G)."
        )


def test_data_model_has_no_todo_markers():
    text = read()
    assert "TODO:" not in text, (
        "docs/data-model.md still contains TODO: markers; every marker must be replaced "
        "(README sections 6-7)."
    )
