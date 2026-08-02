# Normalization — reference pointer

Normalization turns an informally designed schema into one with predictable update behaviour: functional dependencies, closures, candidate keys, 1NF through BCNF, lossless join and dependency preservation. MoleculeTrace uses it to separate molecule identity from assay measurements so a single activity value cannot silently contradict another.

The topic is taught and exercised in week 04, which starts from a deliberately denormalised activity table and derives the normalised design that the rest of the project builds on. Denormalization as a conscious performance trade-off returns in week 22.

## Where this topic is taught

- [`curriculum/week-04-normalization/`](../curriculum/week-04-normalization/)

> **Pointer file.** `labs/` holds reference pointers only. All starter code,
> exercises, tests and expected outputs for this topic live in the week folder(s)
> linked above. If you find a copy of an exercise here, the week folder is the
> authoritative version and this file must be corrected to point at it.
