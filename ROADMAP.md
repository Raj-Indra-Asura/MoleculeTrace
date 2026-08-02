# MoleculeTrace Roadmap

A 24-week, project-based path through a university Database Management Systems
course. Every week produces a visible improvement to the MoleculeTrace registry
and depends only on weeks that came before it.

Required workload: **~5 focused hours per week**. Optional work is always marked
as optional and never assumed by later weeks.

## Phases

| Phase | Weeks | Theme | Project outcome |
|-------|-------|-------|-----------------|
| 0. Foundations | 00–03 | Environment, requirements and architecture, ER design, DDL | A documented design and a running PostgreSQL schema for molecules, targets and assays |
| 1. Design quality | 04–06 | Normalization, SQL basics, relational algebra | A normalised, query-ready schema with a documented algebra layer |
| 2. Query depth | 07–10 | Joins, aggregation, subqueries, CTEs, windows, views, server-side logic | Analytical queries and reusable views over activity data |
| 3. Application layer | 11–13 | Transactions, psycopg, FastAPI | A transactional Python/FastAPI service over the database |
| 4. ML registry | 14–16 | RDKit ETL, dataset versioning, experiment + model registry | Versioned datasets, experiments, model versions and predictions |
| 5. Internals | 17–19 | Indexing, storage and B+ trees, hashing | Measured, documented performance work |
| 6. Reliability | 20–21 | Concurrency control, recovery and backup | Documented isolation behaviour and a tested restore procedure |
| 7. Delivery | 22–23 | Query optimization, Streamlit dashboard, portfolio release | A demo-ready, documented, tagged release |

## Week index

| Week | Folder | Title |
|------|--------|-------|
| 00 | `curriculum/week-00-orientation/` | Orientation and Project Setup |
| 01 | `curriculum/week-01-requirements-and-architecture/` | Requirements and Architecture |
| 02 | `curriculum/week-02-er-and-eer-design/` | ER and EER Design |
| 03 | `curriculum/week-03-logical-design-and-ddl/` | Logical Design and DDL |
| 04 | `curriculum/week-04-normalization/` | Functional Dependencies and Normalization |
| 05 | `curriculum/week-05-sql-fundamentals/` | SQL Fundamentals and Data Loading |
| 06 | `curriculum/week-06-relational-algebra/` | Relational Algebra and Query Equivalence |
| 07 | `curriculum/week-07-joins-and-aggregation/` | Joins and Aggregation over Assay Data |
| 08 | `curriculum/week-08-subqueries-ctes-and-windows/` | Subqueries, CTEs and Window Functions |
| 09 | `curriculum/week-09-constraints-and-integrity/` | Constraints and Data Integrity |
| 10 | `curriculum/week-10-views-and-server-side-logic/` | Views, Functions and Server-Side Logic |
| 11 | `curriculum/week-11-transactions-and-acid/` | Transactions and ACID |
| 12 | `curriculum/week-12-python-integration-psycopg/` | Python Integration with psycopg |
| 13 | `curriculum/week-13-fastapi-service-layer/` | A FastAPI Service Layer |
| 14 | `curriculum/week-14-rdkit-descriptors-and-etl/` | RDKit Descriptors and ETL |
| 15 | `curriculum/week-15-dataset-versioning/` | Versioned Datasets |
| 16 | `curriculum/week-16-ml-experiments-and-model-registry/` | ML Experiments and the Model Registry |
| 17 | `curriculum/week-17-indexing/` | Indexing and Access Paths |
| 18 | `curriculum/week-18-storage-and-bplus-trees/` | Storage Layout and B+ Trees |
| 19 | `curriculum/week-19-hashing/` | Hashing and Hash-Based Access |
| 20 | `curriculum/week-20-concurrency-control/` | Concurrency Control and Isolation |
| 21 | `curriculum/week-21-recovery-and-backup/` | Recovery, Backup and Restore |
| 22 | `curriculum/week-22-query-optimization-and-dashboard/` | Query Optimization and the Streamlit Dashboard |
| 23 | `curriculum/week-23-portfolio-release/` | Portfolio Release |

## Dependency rule

Week *N* may only assume the completion checklists of weeks `00 … N-1`.
Each week begins with a short retrieval-practice section drawn from earlier
weeks, so skipped weeks become visible immediately.

## Out of scope

Molecular docking, protein-structure prediction, graph neural networks,
molecular generation, clinical information, drug recommendations and complex
cloud infrastructure are deliberately excluded. The molecular machine learning
stays simple so the database can be explored deeply.
