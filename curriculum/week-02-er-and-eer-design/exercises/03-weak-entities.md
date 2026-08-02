# Exercise 3 — Weak entities (Required)

## Part A — Apply the three tests

For each candidate, answer the three weak-entity tests with yes or no, then give
the verdict. A weak entity must pass all three.

Tests:

- **T1 Existence dependency** — does deleting the owner destroy the meaning of
  this thing?
- **T2 Identifying relationship** — is it many-to-one towards exactly one owner,
  with total participation on this side?
- **T3 Partial key** — does it have an attribute unique only *within* that
  owner, and not globally?

| Candidate | Owner (if any) | T1 | T2 | T3 | Verdict | Reason |
|-----------|----------------|----|----|----|---------|--------|
| DatasetVersion | TODO | TODO | TODO | TODO | TODO | TODO |
| MoleculeSynonym | TODO | TODO | TODO | TODO | TODO | TODO |
| MoleculeDescriptor | TODO | TODO | TODO | TODO | TODO | TODO |
| ModelVersion | TODO | TODO | TODO | TODO | TODO | TODO |
| ActivityObservation | TODO | TODO | TODO | TODO | TODO | TODO |
| PredictionValidation | TODO | TODO | TODO | TODO | TODO | TODO |

## Part B — DatasetVersion in detail

Answer each in one or two sentences. These answers feed section 7 of
`docs/data-model.md`.

| Question | Your answer |
|----------|-------------|
| Which entity set owns it? | TODO |
| What is the identifying relationship called, in plain language? | TODO |
| What is the partial key? | TODO |
| What is the full identifier that results? | TODO |
| Why is the partial key not globally unique? | TODO |
| What must happen to versions when their dataset is deleted, and why? | TODO |
| Which requirement ID depends on versions being immutable? | TODO |

Then answer the alternative-design question:

> Suppose `DatasetVersion` were given a globally unique identifier of its own and
> modelled as a strong entity.

| Question | Your answer |
|----------|-------------|
| What would still work? | TODO |
| What would become possible that should not be? | TODO |
| What would week 15 have to check that it otherwise gets for free? | TODO |

## Part C — The near-misses

Two candidates in Part A are *nearly* weak and fail exactly one test.

1. Name them and name the failing test.
2. For each, describe the smallest change to the domain that would make it
   genuinely weak.
3. Explain why "it cannot exist without its parent" is not, by itself, enough to
   make something a weak entity.

## Part D — Reflection (three sentences maximum)

Which candidate did you first classify wrongly, and which test corrected you?
