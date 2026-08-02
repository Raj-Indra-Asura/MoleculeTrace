# Syllabus Mapping

How a standard university Database Management Systems syllabus maps onto the
24 weeks of MoleculeTrace. Use this table when you need to justify coverage to
an instructor, or to revise a specific examinable topic.

## Unit 1 — Introduction and the relational model

| Syllabus topic | Week |
|----------------|------|
| Database systems vs. file systems; DBMS architecture; three-schema architecture | week-00, week-01 |
| Data models; instances and schemas; data independence | week-01 |
| Relational model: relations, tuples, attributes, domains | week-01 |
| Keys: super, candidate, primary, foreign | week-01, week-03 |
| Integrity constraints: entity and referential integrity | week-03, week-09 |

## Unit 2 — Conceptual and logical design

| Syllabus topic | Week |
|----------------|------|
| ER model: entities, attributes, relationships, cardinality, participation | week-02 |
| Weak entities, specialisation and generalisation (EER) | week-02 |
| ER-to-relational mapping | week-03 |
| DDL: `CREATE`, `ALTER`, `DROP`; data types | week-03 |
| Functional dependencies; closure; canonical cover | week-04 |
| 1NF, 2NF, 3NF, BCNF; lossless join and dependency preservation | week-04 |
| Denormalization trade-offs | week-04, week-22 |

## Unit 3 — Query languages

| Syllabus topic | Week |
|----------------|------|
| SQL DML: `INSERT`, `SELECT`, `UPDATE`, `DELETE`; `NULL` semantics | week-05 |
| Relational algebra: σ, π, ×, ⋈, ∪, −, ρ, division | week-06 |
| Relational calculus (tuple/domain) — conceptual treatment | week-06 |
| Query equivalence and algebraic rewriting | week-06, week-22 |
| Joins: inner, outer, semi, anti, self | week-07 |
| Aggregation, `GROUP BY`, `HAVING` | week-07 |
| Nested subqueries, correlated subqueries, `EXISTS` | week-08 |
| CTEs, recursive queries, window functions | week-08 |
| Views, materialised views, updatable views | week-10 |
| Stored functions, procedures and triggers | week-10 |
| Assertions, `CHECK`, domain constraints | week-09 |

## Unit 4 — Transactions, concurrency and recovery

| Syllabus topic | Week |
|----------------|------|
| Transaction concept; ACID properties; transaction states | week-11 |
| Schedules, serialisability (conflict and view) | week-11, week-20 |
| Isolation levels; anomalies (dirty/non-repeatable/phantom) | week-11, week-20 |
| Lock-based protocols; two-phase locking; deadlock detection | week-20 |
| Timestamp ordering; MVCC as implemented by PostgreSQL | week-20 |
| Failure classification; log-based recovery; WAL; checkpoints | week-21 |
| Backup, restore and point-in-time recovery | week-21 |

## Unit 5 — Storage, file structure and indexing

| Syllabus topic | Week |
|----------------|------|
| Access paths, selectivity, index selection | week-17 |
| Index types: B-tree, hash, GIN, partial, covering, composite | week-17, week-18, week-19 |
| Physical storage: pages, tuples, heap files, TOAST, fill factor | week-18 |
| Ordered indices; B-tree and B+ tree structure and operations | week-18 |
| Static and dynamic (extendible/linear) hashing; collisions | week-19 |
| Hash joins, hash aggregation | week-19, week-22 |

## Unit 6 — Query processing and optimization

| Syllabus topic | Week |
|----------------|------|
| Query processing pipeline; parse, rewrite, plan, execute | week-22 |
| Cost estimation, statistics, cardinality estimation | week-17, week-22 |
| Join algorithms: nested loop, merge, hash | week-19, week-22 |
| Heuristic and cost-based optimization; `EXPLAIN (ANALYZE, BUFFERS)` | week-22 |

## Unit 7 — Application and data engineering

| Syllabus topic | Week |
|----------------|------|
| Embedded/dynamic SQL, connection handling, cursors | week-12 |
| Parameterised queries and SQL-injection prevention | week-12, week-13 |
| Connection pooling; transaction boundaries in applications | week-12, week-13 |
| REST API over a relational store; schema validation | week-13 |
| ETL and derived attributes | week-14 |
| Data versioning, provenance and reproducibility | week-15, week-16 |
| Auditing, metadata and reporting | week-16, week-22 |
| Documentation, packaging and release | week-23 |

## Cross-cutting practice

| Practice | Weeks |
|----------|-------|
| Retrieval practice of earlier material | every week |
| Automated validation with `pytest` | week-05 onward |
| Portfolio evidence capture | every week |
