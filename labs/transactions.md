# Transactions — reference pointer

A transaction is the unit of atomicity and isolation: BEGIN, COMMIT, ROLLBACK, savepoints and the ACID properties. MoleculeTrace depends on them whenever an ingestion writes a molecule together with its activity rows, or an experiment run records a model version and its predictions together.

The concept is taught and exercised in week 11 (ACID, transaction boundaries, anomalies) and extended in week 20 (serialisability, locking, MVCC and isolation levels in practice).

## Where this topic is taught

- [`curriculum/week-11-transactions-and-acid/`](../curriculum/week-11-transactions-and-acid/)
- [`curriculum/week-20-concurrency-control/`](../curriculum/week-20-concurrency-control/)

> **Pointer file.** `labs/` holds reference pointers only. All starter code,
> exercises, tests and expected outputs for this topic live in the week folder(s)
> linked above. If you find a copy of an exercise here, the week folder is the
> authoritative version and this file must be corrected to point at it.
