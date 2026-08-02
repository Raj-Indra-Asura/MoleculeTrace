# B+ Trees — reference pointer

A B+ tree is the ordered index structure that PostgreSQL's default B-tree index implements: internal nodes route searches, leaves hold all keys in sorted order and are linked for range scans, and inserts split nodes to keep the tree balanced. This is why range predicates on assay values and ORDER BY ... LIMIT queries in MoleculeTrace can avoid a full scan.

The topic is taught and exercised in week 18, alongside page layout, tuple headers and fill factor, including a small pen-and-paper insertion and split exercise plus measurements on the real schema.

## Where this topic is taught

- [`curriculum/week-18-storage-and-bplus-trees/`](../curriculum/week-18-storage-and-bplus-trees/)

> **Pointer file.** `labs/` holds reference pointers only. All starter code,
> exercises, tests and expected outputs for this topic live in the week folder(s)
> linked above. If you find a copy of an exercise here, the week folder is the
> authoritative version and this file must be corrected to point at it.
