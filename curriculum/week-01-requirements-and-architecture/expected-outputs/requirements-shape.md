# Expected shape — `docs/02_requirements.md`

A target for *structure*, not wording. Your requirements will differ; the
columns, the ID format and the row shape must not.

## Functional requirements

```markdown
| ID | Requirement | Actor | Priority | Verified by |
|----|-------------|-------|----------|-------------|
| FR-01 | The system shall store one row per distinct molecule, identified by its canonical SMILES, so that a compound is never registered twice. | Data curator | MUST | week-09 unique constraint test |
| FR-02 | The system shall reject an activity observation whose molecule is not present in the registry. | ML pipeline | MUST | week-09 referential-integrity test |
```

Checks the week test applies:

- IDs match `FR-NN`, start at `FR-01`, are consecutive and unique.
- At least 12 rows.
- Priority is one of `MUST`, `SHOULD`, `COULD`.
- The `Verified by` cell is non-empty.

## Non-functional requirements

```markdown
| ID | Category | Requirement | Metric and threshold | Verified by |
|----|----------|-------------|----------------------|-------------|
| NFR-01 | Performance | A lookup of one molecule by canonical SMILES shall stay interactive with 100 000 molecules loaded. | p95 latency < 200 ms over 100 sequential lookups | week-17 EXPLAIN + timing |
| NFR-02 | Recoverability | A full restore from the latest backup shall reproduce the registry without manual repair. | restore completes in < 15 min, row counts identical | week-21 restore drill |
```

Checks the week test applies:

- IDs match `NFR-NN`, start at `NFR-01`, are consecutive and unique.
- At least 8 rows.
- Each requirement row contains at least one digit — a number with a unit.

## Risk register

```markdown
| ID | Risk | Likelihood | Impact | Mitigation | Owner |
|----|------|-----------|--------|------------|-------|
| RISK-01 | Source activity data contains duplicate measurements under different units. | High | High | Normalise units on ingest; unique constraint on (assay, molecule, unit). | Data curator |
```

At least 6 rows, IDs `RISK-NN`, likelihood and impact each one of `Low`,
`Medium`, `High`.
