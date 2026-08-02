# Expected shape — cardinality and participation tables

A target for *structure*, not content. Your model will differ; the columns, the
allowed values and the row shape must not.

**There is no reference ER or EER diagram in this folder, by design.** The
instructor reference lives in `instructor/solution-notes/week-02.md` and is to be
read only after you submit.

## Cardinality table (`docs/data-model.md` section 5)

```markdown
| Relationship | Left entity | Right entity | Cardinality | Domain rule that forces it | Reading (left → right) | Reading (right → left) |
|--------------|-------------|--------------|-------------|----------------------------|------------------------|------------------------|
| produces | Assay | ActivityObservation | 1:N | The protocol determines what the measured number means, so a measurement belongs to exactly one assay. | One assay produces many activity observations. | Each activity observation was produced by exactly one assay. |
```

Checks the week test applies:

- The cardinality cell is exactly `1:1`, `1:N` or `M:N`.
- At least one `1:1`, at least six `1:N` and at least two `M:N` rows.
- No cell is empty and no cell contains `TODO`.
- Both reading cells contain a sentence of at least five words.

## Participation table (`docs/data-model.md` section 6)

```markdown
| Relationship | Left entity | Left participation | Right entity | Right participation | What this forbids (or deliberately allows) |
|--------------|-------------|--------------------|--------------|---------------------|--------------------------------------------|
| produces | Assay | partial | ActivityObservation | total | Total participation of ActivityObservation forbids a measurement that names no assay; the assay side is partial because a newly defined assay has produced nothing yet. |
```

Checks the week test applies:

- Participation cells contain exactly `total` or `partial`, in lower case.
- Both sides are present for every relationship.
- The final column is a sentence, not a word.
- The set of relationship names matches the cardinality table exactly.

## Design-decision log (`docs/data-model.md` section 10)

```markdown
| ID | Decision | Alternatives considered | Reason | Consequence for a later week | Requirement |
|----|----------|-------------------------|--------|------------------------------|-------------|
| DD-01 | Record a descriptor value on an associative entity between Molecule and DescriptorType. | Store one column per descriptor on Molecule; store a JSON blob. | New descriptor types arrive without a schema change, and the value belongs to the pairing rather than to either side. | Week 14 inserts descriptors without a migration; week 17 indexes the pairing. | FR-08 |
```

Checks the week test applies:

- IDs match `DD-NN`, start at `DD-01`, are consecutive and unique.
- At least 8 rows.
- The alternatives cell is non-empty and does not say `none` on more than one
  row.

## Relationship narratives (section 9)

Shape only:

```markdown
### R-04 — belongs to (DatasetVersion ↔ Dataset)

- **Left to right:** Each dataset version belongs to exactly one dataset.
- **Right to left:** One dataset accumulates many numbered versions over time.
- **Why it exists:** So that a result can name the exact snapshot it was
  produced from, months later.
- **What it forbids:** A version that names no dataset, and two versions of the
  same dataset sharing a number.
- **Serves requirement:** FR-11.
```

Checks the week test applies: the narrative section names every relationship
from the cardinality table, and contains none of the words `foreign key`,
`join`, `table` or `many-to-many`.
