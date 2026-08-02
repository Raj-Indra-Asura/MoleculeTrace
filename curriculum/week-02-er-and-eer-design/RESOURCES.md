# Week 02 — Resources

Official documentation first. Add a link only after you have used it.

## Required reading

- Mermaid — entity-relationship diagram syntax, including cardinality markers:
  https://mermaid.js.org/syntax/entityRelationshipDiagram.html
- Mermaid live editor, for checking a diagram renders before committing it:
  https://mermaid.live/
- PostgreSQL 16 — data definition, the shape your entity sets will take in
  week 03: https://www.postgresql.org/docs/16/ddl.html
- PostgreSQL 16 — constraints, where participation and cardinality end up:
  https://www.postgresql.org/docs/16/ddl-constraints.html
- PostgreSQL 16 — inheritance, one implementation of specialisation, and its
  documented caveats: https://www.postgresql.org/docs/16/ddl-inherit.html
- PostgreSQL 16 — generated columns, the supported way to store a derived
  attribute: https://www.postgresql.org/docs/16/ddl-generated-columns.html

## Reference

- PostgreSQL 16 documentation: https://www.postgresql.org/docs/16/
- PostgreSQL 16 — primary and foreign keys, for compound and partial keys:
  https://www.postgresql.org/docs/16/tutorial-fk.html
- PostgreSQL 16 — data types, for judging whether a composite attribute should
  split: https://www.postgresql.org/docs/16/datatype.html
- Graphviz DOT language, if you prefer `.dot` to Mermaid for the conceptual
  diagram: https://graphviz.org/doc/info/lang.html
- ChEMBL data model documentation, a real chemical registry schema to compare
  yours against: https://chembl.gitbook.io/chembl-interface-documentation
- PubChem data specification, for what a molecule identifier looks like in
  practice: https://pubchem.ncbi.nlm.nih.gov/docs/data-specification

## In this repository

- [`docs/01_problem_statement.md`](../../docs/01_problem_statement.md) — the
  nouns this week harvests.
- [`docs/02_requirements.md`](../../docs/02_requirements.md) — requirement IDs
  cited by the design-decision log.
- [`docs/03_architecture.md`](../../docs/03_architecture.md) — which tier will
  enforce each constraint.
- [`docs/README.md`](../../docs/README.md) — where `data-model.md` lives.
- [`docs/decisions/README.md`](../../docs/decisions/README.md) — decision-record
  format for the optional task.
- [`SYLLABUS_MAPPING.md`](../../SYLLABUS_MAPPING.md) — syllabus topic → week.
- [`curriculum/week-01-requirements-and-architecture/LEARNING_NOTES.md`](../week-01-requirements-and-architecture/LEARNING_NOTES.md)
  — schema versus instance, revisited here as design versus diagram.

## Optional depth

- PostgreSQL 16 — arrays, and why a multivalued attribute is still not an
  excuse to use one in a conceptual model:
  https://www.postgresql.org/docs/16/arrays.html
- PostgreSQL 16 — exclusion constraints, useful later for 1:1 relationships:
  https://www.postgresql.org/docs/16/ddl-constraints.html#DDL-CONSTRAINTS-EXCLUSION
- PostgreSQL 16 — role and privilege model, the eventual home of the user/role
  decision: https://www.postgresql.org/docs/16/user-manag.html
