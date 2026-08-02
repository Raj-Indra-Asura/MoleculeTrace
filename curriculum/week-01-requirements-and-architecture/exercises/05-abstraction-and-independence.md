# Exercise 5 — Abstraction and data independence (Optional, stretch)

Optional exercises are never assumed by a later week.

## Part A — Classify

Put each item at the physical, logical or view level, and name the week that
touches it.

| Item | Level | Week |
|------|-------|------|
| `CREATE TABLE activities (...)` | | |
| A B-tree index on `activities(molecule_id)` | | |
| The JSON body returned by `GET /molecules/{id}` | | |
| The 8 kB page holding a heap tuple | | |
| `v_active_compounds` | | |
| The `NOT NULL` constraint on `molecules.canonical_smiles` | | |
| The Streamlit "top targets" chart | | |
| The TOAST table for long SMILES strings | | |

## Part B — Schema or instance?

| Statement | Schema or instance? | Why |
|-----------|---------------------|-----|
| "There are 12 431 molecules." | | |
| "Every activity has a non-null assay." | | |
| "Molecule 4471 has logP 3.2." | | |
| "`activities.value` is numeric." | | |
| "The registry grew by 300 rows last night." | | |

## Part C — Independence

1. Describe a change you will genuinely make in week 17 or 18 that exercises
   *physical* data independence, and name what must **not** change as a result.
2. Describe a change to the logical schema that would break the dashboard, then
   describe how a view in week 10 would have preserved *logical* data
   independence instead.
3. Which of the two kinds of independence does PostgreSQL give you almost for
   free, and which one you have to design for? Justify in two sentences.
