# Indexing — reference pointer

Indexing is the choice of access paths: which columns to index, single-column versus composite, partial and covering indexes, and how selectivity and statistics drive the planner. In MoleculeTrace the activity table grows fastest, so its lookup patterns decide which indexes earn their storage and write cost.

The topic is taught and exercised in week 17, where indexes are added and measured with EXPLAIN (ANALYZE, BUFFERS) before and after. The physical structures behind these indexes are opened up in weeks 18 and 19.

## Where this topic is taught

- [`curriculum/week-17-indexing/`](../curriculum/week-17-indexing/)

> **Pointer file.** `labs/` holds reference pointers only. All starter code,
> exercises, tests and expected outputs for this topic live in the week folder(s)
> linked above. If you find a copy of an exercise here, the week folder is the
> authoritative version and this file must be corrected to point at it.
