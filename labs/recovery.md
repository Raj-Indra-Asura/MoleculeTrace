# Recovery — reference pointer

Recovery is how a database survives failure: failure classification, the write-ahead log, checkpoints, redo and undo, and the practical backup and restore procedures built on them. For MoleculeTrace the question is whether a dataset version and its experiment history can be rebuilt after the container is destroyed.

The topic is taught and exercised in week 21, which includes a full dump, a deliberate loss of the data volume and a verified restore. Its prerequisites are weeks 11 and 20.

## Where this topic is taught

- [`curriculum/week-21-recovery-and-backup/`](../curriculum/week-21-recovery-and-backup/)

> **Pointer file.** `labs/` holds reference pointers only. All starter code,
> exercises, tests and expected outputs for this topic live in the week folder(s)
> linked above. If you find a copy of an exercise here, the week folder is the
> authoritative version and this file must be corrected to point at it.
