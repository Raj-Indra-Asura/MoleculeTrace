# Hashing — reference pointer

Hashing gives constant-time equality lookup: static hashing, collisions and overflow, extendible and linear hashing, and PostgreSQL's hash index. It also powers hash joins and hash aggregation, which is how large joins between activity observations and datasets are usually executed.

The topic is taught and exercised in week 19, where hash and B-tree access paths are compared on the same equality predicates and hash-join plans are read from EXPLAIN output.

## Where this topic is taught

- [`curriculum/week-19-hashing/`](../curriculum/week-19-hashing/)

> **Pointer file.** `labs/` holds reference pointers only. All starter code,
> exercises, tests and expected outputs for this topic live in the week folder(s)
> linked above. If you find a copy of an exercise here, the week folder is the
> authoritative version and this file must be corrected to point at it.
