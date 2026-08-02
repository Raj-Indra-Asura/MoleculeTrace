# Concurrency Control — reference pointer

Concurrency control keeps interleaved transactions correct: schedules and serialisability, two-phase locking, deadlock detection, timestamp ordering and PostgreSQL's MVCC. In MoleculeTrace it matters when two ingestion jobs touch the same molecule or two experiment runs append to the same dataset version.

The topic is taught and exercised in week 20 using two concurrent psql sessions to reproduce lost updates, non-repeatable reads, phantoms, serialisation failures and deadlocks. Its prerequisite is week 11.

## Where this topic is taught

- [`curriculum/week-20-concurrency-control/`](../curriculum/week-20-concurrency-control/)

> **Pointer file.** `labs/` holds reference pointers only. All starter code,
> exercises, tests and expected outputs for this topic live in the week folder(s)
> linked above. If you find a copy of an exercise here, the week folder is the
> authoritative version and this file must be corrected to point at it.
