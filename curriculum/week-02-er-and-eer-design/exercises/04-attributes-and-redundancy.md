# Exercise 4 — Attributes and redundancy (Required)

## Part A — Classify

Label each attribute `simple`, `composite`, `multivalued`, `derived` or `key`,
and say how it must be treated in the improved EER model.

| # | Attribute | Kind | Treatment |
|---|-----------|------|-----------|
| 1 | `UserAccount.full_name` (given name, family name) | TODO | TODO |
| 2 | `UserAccount.roles_held` | TODO | TODO |
| 3 | `Molecule.canonical_smiles` | TODO | TODO |
| 4 | `Molecule.synonyms` | TODO | TODO |
| 5 | `Molecule.activity_count` | TODO | TODO |
| 6 | `Assay.protocol` (method, readout, temperature) | TODO | TODO |
| 7 | `Assay.target_name` | TODO | TODO |
| 8 | `ActivityObservation.value` | TODO | TODO |
| 9 | `Dataset.version_count` | TODO | TODO |
| 10 | `DatasetVersion.version_number` | TODO | TODO |
| 11 | `DatasetVersion.row_count` | TODO | TODO |
| 12 | `ModelVersion.is_current` | TODO | TODO |
| 13 | `Prediction.generated_at` | TODO | TODO |
| 14 | `AuditLog.actor_email` | TODO | TODO |
| 15 | `DescriptorType.unit` | TODO | TODO |

## Part B — The redundancy hunt

Four of the attributes in Part A are redundant or derived. For each, complete the
row:

| Attribute | Why it is redundant or derived | Where the fact really lives | Cost of keeping it | Decision |
|-----------|--------------------------------|-----------------------------|--------------------|----------|
| TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |

`DatasetVersion.row_count` is deliberately harder than the others. Argue both
sides: it is derivable from the membership, *and* it is a checksum-like fact
about an immutable snapshot. State your decision and the condition under which
you would reverse it.

## Part C — Redundant relationships

For each pair of paths, say whether the shortcut is redundant, and give the test
you applied.

| # | Path A | Path B (shortcut) | Redundant? | Test applied |
|---|--------|-------------------|------------|--------------|
| 1 | Observation → Assay → Target | Observation → Target | TODO | TODO |
| 2 | Prediction → ModelVersion → Experiment → DatasetVersion | Prediction → DatasetVersion | TODO | TODO |
| 3 | Prediction → ModelVersion → Experiment → DatasetVersion → Molecule | Prediction → Molecule | TODO | TODO |

Row 3 is the interesting one: a model version can predict for a molecule that
was never in its training dataset version. Say what that means for whether the
shortcut is redundant, and write the plain-language sentence that distinguishes
the two facts.

## Part D — Composite attributes

`Assay.protocol` and `UserAccount.full_name` are both composite. For each,
answer:

1. Are the parts ever queried, sorted or constrained separately?
2. Does the answer differ between the conceptual model (this week) and the
   logical model (week 03)?
3. What breaks if you guess wrong in each direction?

## Part E — Reflection (three sentences maximum)

Which redundant attribute were you most tempted to keep, and what argument did
you use on yourself before deleting it?
