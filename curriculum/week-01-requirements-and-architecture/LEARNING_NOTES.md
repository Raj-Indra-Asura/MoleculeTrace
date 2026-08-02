# Week 01 — Learning Notes

Section 1 is given. Write sections 2–5 yourself, as you go, not afterwards.

## 1. The vocabulary, in one page

| Term | Definition | MoleculeTrace example |
|------|------------|-----------------------|
| Database | A collection of related data | The molecule/activity/model registry |
| DBMS | Software that stores, protects and queries a database | PostgreSQL 16 |
| File-based processing | Data kept in per-application files | `activities_2024_final_v3.csv` |
| Physical level | How data is stored | Heap pages, B-tree index files (weeks 17–19) |
| Logical level | What data exists and how it relates | `molecules`, `targets`, `assays`, `activities` |
| View level | What one user sees | `v_active_compounds`, an API response, a chart |
| Schema | The design; changes rarely | `CREATE TABLE molecules (...)` |
| Instance | The contents right now | The 12 431 rows currently in `molecules` |
| Physical data independence | Change storage without changing the logical schema | Adding an index in week 17 |
| Logical data independence | Change the logical schema without changing the views | Splitting a column out behind a view |
| Two-tier | Client talks SQL to the database | An analyst in `psql` |
| Three-tier | Client → application server → database | Streamlit → FastAPI → PostgreSQL |
| Functional requirement | What the system must do | "The system shall reject an activity with an unknown molecule." |
| Non-functional requirement | How well it must do it | "…under 200 ms at p95 over 100 000 molecules." |
| Actor | A person or program that uses the system | Bench scientist, data scientist, ML pipeline, DBA |
| DBA | Owns schema, storage, access, authorisation, backup | You, wearing the ops hat |

### The six failures of file-based processing

Redundancy and inconsistency · difficulty of access · data isolation ·
integrity problems · atomicity problems · concurrent-access and security
problems. Learn them as a list; you will be asked for them with examples.

## 2. My retrieval-practice answers (README section 3)

1. Four processes from week 00 and their ports:
2. Why credentials live in `.env`:
3. What `/health` reports with the database stopped, and why it must not raise:

## 3. Core ideas in my words

1. Schema versus instance:
2. Physical, logical and view levels, with one MoleculeTrace example each:
3. Why MoleculeTrace is three-tier and not two-tier:
4. What the database must own that the application must not:

## 4. Worked example from this week

<Paste one requirement of yours that started ambiguous and ended testable. Show
the before, the after, and name which of the six quality tests it failed.>

Before:

After:

Failed test(s):

## 5. Connections to earlier weeks

- Week 00 gave a running database, a health endpoint and a test harness. Which
  of my non-functional requirements does that already partly satisfy?
- What do I expect week 02 to take directly from `docs/01_problem_statement.md`?

## Open questions

-
