# 02 — Requirements

> **Status:** skeleton. Completed in
> [week 01](../curriculum/week-01-requirements-and-architecture/README.md),
> section 7A. Replace every `TODO:` marker and add rows until the minimum counts
> are met: **12 functional**, **8 non-functional**, **6 risks**.

Identifiers are permanent. Later weeks cite `FR-07` and `NFR-03` by number, so
requirements are repaired in place and new ones are appended — never renumbered,
never reused.

Every requirement must survive the six-test checklist in
[`../curriculum/week-01-requirements-and-architecture/starter/requirement-quality-checklist.md`](../curriculum/week-01-requirements-and-architecture/starter/requirement-quality-checklist.md):
atomic, testable, unambiguous, necessary, implementation-free, traceable.

## 1. Functional requirements

Pattern: *The system shall `<observable behaviour>` when `<trigger>`, so that
`<actor>` can `<goal>`.*
Priority is `MUST`, `SHOULD` or `COULD`. `Verified by` names the week, test or
command that will prove it.

| ID | Requirement | Actor | Priority | Verified by |
|----|-------------|-------|----------|-------------|
| FR-01 | The system shall store one row per distinct molecule, identified by its canonical SMILES, so that a compound is never registered twice. | Data curator | MUST | week-09 unique-constraint test |
| FR-02 | TODO: | TODO: | TODO: | TODO: |
| FR-03 | TODO: | TODO: | TODO: | TODO: |

TODO: continue to at least `FR-12`. Cover, at minimum: registering molecules,
targets, assays and activity observations; rejecting orphan references;
constructing and freezing a dataset version; recording an experiment, a model
version and its metrics; storing predictions with the model version that made
them; recording validation outcomes; querying activity by target; and exposing
the registry through the service layer.

## 2. Non-functional requirements

Pattern: *The system shall `<quality>`, measured as `<metric>`, reaching
`<threshold>` under `<workload>`, verified by `<method>`.*
Every row needs a number and a unit.

| ID | Category | Requirement | Metric and threshold | Verified by |
|----|----------|-------------|----------------------|-------------|
| NFR-01 | Performance | A lookup of one molecule by canonical SMILES shall stay interactive as the registry grows. | p95 under 200 ms over 100 sequential lookups with 100 000 molecules loaded | week-17 timing and `EXPLAIN` |
| NFR-02 | TODO: | TODO: | TODO: | TODO: |

TODO: continue to at least `NFR-08`, covering performance, integrity,
reliability/recoverability, security, usability, maintainability,
reproducibility and portability.

## 3. Traceability

Every requirement appears exactly once here. A requirement with no implementing
week is either premature or out of scope.

| Requirement ID | Actor | Implemented in week | Evidence |
|----------------|-------|---------------------|----------|
| FR-01 | Data curator | week-03, week-09 | `CREATE UNIQUE INDEX` in the schema, plus the week-09 test |
| TODO: | TODO: | TODO: | TODO: |

## 4. Risk register

| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|----|------|-----------|--------|------------|-------|
| RISK-01 | Source activity data holds duplicate measurements recorded in different units. | High | High | Normalise units on ingest; constrain (assay, molecule, unit) to be unique. | Data curator |
| RISK-02 | TODO: | TODO: | TODO: | TODO: | TODO: |

TODO: continue to at least `RISK-06`, including at least one data-quality risk,
one performance risk and one scope risk. Likelihood and impact are `Low`,
`Medium` or `High`.

## 5. Assumptions and constraints

- TODO: assumption about the data available.
- TODO: assumption about the users.
- Constraint: about five hours of work per week, twenty-four weeks.
- Constraint: PostgreSQL 16 in Docker Compose; no managed cloud services.
- TODO:

## 6. Definition of done

### A week is done when

- [ ] Its `CHECKPOINT.md` items are all true.
- [ ] `make test-week WEEK=<week>` passes and `make lint` is clean.
- [ ] TODO: your criterion about documentation.
- [ ] TODO: your criterion about evidence in `docs/portfolio/`.
- [ ] TODO: your criterion about the commit and the progress table.

### The project is done when

- [ ] Every requirement marked `MUST` has passed its stated verification.
- [ ] TODO:
- [ ] TODO:
- [ ] TODO:

## Related documents

- [`01_problem_statement.md`](01_problem_statement.md) — problem, scope, actors.
- [`03_architecture.md`](03_architecture.md) — where each requirement is
  enforced.
- [`../SYLLABUS_MAPPING.md`](../SYLLABUS_MAPPING.md) — syllabus topic → week.
