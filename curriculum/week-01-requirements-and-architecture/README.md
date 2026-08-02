# Week 01 — Requirements and Architecture

**Phase:** 0. Foundations · **Required effort:** 5 hours ·
**Depends on:** week 00

**Topic scope:** DBMS foundations (file systems versus a DBMS), levels of
abstraction, schemas and instances, two-tier versus three-tier architecture,
database users and administrators — applied by writing the MoleculeTrace
problem statement, requirements and architecture documents.

Week 00 proved the environment runs. Week 01 decides *what* is going to be
built and *which layer owns each responsibility*, so that week 02 can model
entities without re-arguing scope.

## 1. Learning objectives

By the end of this week you can:

1. State the MoleculeTrace problem precisely: the data, the users, the
   decisions the system supports, and what it will never do.
2. Assign a responsibility to the database, the application or the ML layer and
   defend the assignment against one named alternative.
3. Contrast file-based processing with a DBMS on redundancy, consistency,
   concurrent access, integrity, atomicity and security, using a MoleculeTrace
   example for each.
4. Explain schema versus instance and the physical, logical and view levels of
   abstraction, and give one example each of physical and logical data
   independence in this project.
5. Compare two-tier and three-tier architectures and justify the three-tier
   choice for MoleculeTrace.
6. Identify the system's actors — naive users, application programmers,
   sophisticated users, the database administrator — and list what each may do.
7. Write functional and non-functional requirements that are atomic, testable,
   unambiguous and traceable, and rewrite an ambiguous requirement so that it
   becomes testable.

## 2. Connection to MoleculeTrace

Everything downstream depends on the chain being agreed:

```
molecules → targets → assays → activities → datasets
         → experiments → model versions → predictions → validation
```

This week fixes the boundaries of that chain in writing. Week 02 draws the ER
model from your problem statement; week 03 turns it into DDL; week 09 turns your
non-functional requirements about integrity into constraints; week 13 builds the
service layer your three-tier diagram promises; week 17 and week 22 are measured
against the performance numbers you write down on Wednesday.

**Visible improvement this week:** the repository gains three reviewed design
documents — `docs/01_problem_statement.md`, `docs/02_requirements.md` and
`docs/03_architecture.md` — that later weeks cite instead of re-inventing.

## 3. Prerequisites

- Week 00 checkpoint passed: PostgreSQL runs, `psql` connects,
  `scripts/check_db_connection.py` prints `OK`, `GET /health` returns
  `{"status":"ok","database":"up"}`.
- The repository conventions in `CONTRIBUTING.md` read at least once.

### Retrieval practice (15 minutes, required)

Answer from memory before opening any notes:

1. Which four processes did week 00 start or exercise, and which port does each
   use?
2. Why does the project read credentials from `.env` at run time instead of
   hard-coding a connection string?
3. What does `GET /health` report when the database container is stopped, and
   why must it not raise an exception?

Check your answers against
[`../week-00-orientation/LEARNING_NOTES.md`](../week-00-orientation/LEARNING_NOTES.md).

## 4. Five-hour study plan

| Block | Time | Activity | Output |
|-------|------|----------|--------|
| 1 | 0:00–0:15 | Retrieval practice (section 3) | Three written answers in `LEARNING_NOTES.md` |
| 2 | 0:15–1:15 | Conceptual notes (section 5) | Sections 2–4 of `LEARNING_NOTES.md` |
| 3 | 1:15–2:15 | Guided work (section 6) | `docs/01_problem_statement.md` complete |
| 4 | 2:15–3:45 | Independent work (section 7) | `docs/02_requirements.md` and `docs/03_architecture.md` complete |
| 5 | 3:45–4:30 | Exercises 1–4 (section 8) | Completed exercise files |
| 6 | 4:30–4:45 | Validation (section 9) | `make test-week` passes |
| 7 | 4:45–5:00 | Reflection and commit (sections 11–15) | Commit pushed, evidence saved |

## 5. Conceptual notes

Read once, then write section 3 of `LEARNING_NOTES.md` in your own words.

### 5.1 What a DBMS is for

A **database** is a collection of related data; a **database management system**
(DBMS) is the software that stores it, enforces rules about it and answers
questions about it. The point of the course is that a DBMS gives you six things
that files in a directory do not.

Imagine MoleculeTrace built from CSV files — `molecules.csv`,
`activities_2024.csv`, `activities_2024_final_v3.csv`:

| Problem with file-based processing | What it looks like in MoleculeTrace | What the DBMS gives you |
|-----------------------------------|-------------------------------------|-------------------------|
| Data redundancy and inconsistency | The same molecule's SMILES stored in three CSVs, two of them stale | One `molecules` row, referenced by key |
| Difficulty accessing data | "Which molecules were active against target X in 2024?" needs a new script each time | Ad-hoc SQL, no new program |
| Data isolation | Descriptors in Parquet, assays in CSV, targets in a spreadsheet | One schema, joinable |
| Integrity problems | Nothing stops an activity row pointing at a molecule that was deleted | Referential integrity (week 09) |
| Atomicity problems | A crash halfway through "insert dataset + insert 5 000 members" leaves half a dataset | Transactions (week 11) |
| Concurrent access and security | Two loaders write the same file; everyone has full access to everything | Locking/MVCC (week 20), roles and privileges |

Write these down with *your* examples: exercise 3 asks for exactly this table.

### 5.2 Levels of abstraction, schema and instance

Three levels:

- **Physical level** — how bytes are laid out: heap pages, index files, TOAST.
  MoleculeTrace touches this in weeks 17–19.
- **Logical level** — what data exists and how it relates: tables `molecules`,
  `targets`, `assays`, `activities`, and their keys. This is what weeks 02–04
  design.
- **View level** — what a particular user sees: a Streamlit chart, a
  `v_active_compounds` view, an API response body. Weeks 10, 13 and 22.

Two words that are easy to confuse:

- **Schema** — the *design*: the definition of the tables, their columns, types
  and constraints. Changes rarely, by migration.
- **Instance** — the *contents at a moment in time*: the actual rows now.
  Changes constantly.

Analogy: schema is the class, instance is the object; schema is the form,
instance is a filled-in form.

**Data independence** is the ability to change one level without changing the
one above it:

- *Physical data independence* — adding a B-tree index on
  `activities(molecule_id)` in week 17 changes performance, not one line of SQL
  in the application.
- *Logical data independence* — splitting a column out into a new table while a
  view preserves the old shape means the dashboard keeps working.

### 5.3 Two-tier versus three-tier

**Two-tier**: the client (a desktop app, a notebook, `psql`) speaks SQL directly
to the database.

```
[ client + application logic ]  ──SQL──▶  [ database ]
```

Simple, and fine for an analyst with `psql`. But every client needs database
credentials, business rules get duplicated in each client, and the connection
count grows with users.

**Three-tier**: the client speaks HTTP to an application server, which speaks
SQL to the database.

```
[ presentation ] ──HTTP──▶ [ application ] ──SQL──▶ [ data ]
  Streamlit,                 FastAPI,                 PostgreSQL
  curl, browser              psycopg, Pydantic        tables, views,
                             validation, auth         constraints, indexes
```

MoleculeTrace is three-tier because: credentials stay on the server; validation
and business rules live in one place; the dashboard can be replaced without
touching the database; connection pooling is possible; and the ML pipeline
becomes just another client of the same rules.

Note that the ML layer is *not* a fourth tier. Training and descriptor
calculation are batch jobs that sit beside the application tier and reach the
data tier through the same rules.

### 5.4 Who owns what

A recurring exam question and a recurring design argument. The rule of thumb:

| Responsibility | Owner | Why |
|----------------|-------|-----|
| Uniqueness of a molecule's canonical SMILES | Database | Must hold no matter which client writes |
| Referential integrity of `activities → molecules` | Database | Same |
| Allowed range of a numeric activity value | Database (`CHECK`) + application (early feedback) | Defence in depth |
| Request shape and HTTP status codes | Application | Protocol concern, not data concern |
| Authentication and authorisation of API callers | Application, backed by database roles | Two layers, different granularity |
| Descriptor calculation from SMILES (RDKit) | ML/ETL | Needs a chemistry library; result is stored, not computed on read |
| Train/test split definition | ML, recorded in the database | Reproducibility requires the split be *stored*, not re-randomised |
| Which model version is "current" | Database | It is a fact about the registry, queried by everyone |

The trap: putting a rule *only* in the application. Any rule that must be true
of the data itself belongs in the database, because the database is the only
component every writer goes through.

### 5.5 Database users and administrators

| Actor | In MoleculeTrace | May do | May not do |
|-------|------------------|--------|------------|
| Naive / end user | Bench scientist using the Streamlit dashboard | Read curated views, filter, export a chart | Write SQL, change schema |
| Application programmer | You, building FastAPI endpoints | Write parameterised SQL through the service, run migrations in review | Bypass validation in production |
| Sophisticated user | Data scientist with `psql` or a notebook | Ad-hoc read-only SQL, build datasets | Write to `activities` directly |
| Specialised user | ML pipeline (a program, not a person) | Insert experiments, model versions, predictions | Delete source data |
| Database administrator (DBA) | You, wearing the ops hat | Schema definition, storage and access-method choices, granting authorisation, monitoring, backup and restore | Silently change data to fix a bug |

Each actor becomes a role with privileges later; each also becomes a source of
requirements this week. If an actor has no requirement, either the actor is
imaginary or the requirement is missing.

### 5.6 What makes a requirement good

A **functional requirement** says what the system must do:
*"The system shall reject an activity observation whose molecule does not exist
in the registry."*
A **non-functional requirement** says how well it must do it:
*"A single-molecule lookup by canonical SMILES shall return in under 200 ms at
the 95th percentile with 100 000 molecules loaded."*

Six quality tests — the **requirement-quality checklist**, used again in
exercise 2 and in `CHECKPOINT.md`:

| # | Test | Failing example | Fixed |
|---|------|-----------------|-------|
| 1 | **Atomic** — one requirement, one obligation | "The system shall import and validate and de-duplicate molecules." | Three requirements |
| 2 | **Testable** — a named check can pass or fail | "The system shall be fast." | "…shall return in under 200 ms at p95 over 100 000 rows." |
| 3 | **Unambiguous** — one reading only | "Users can manage datasets." | "A data scientist shall create a dataset version; nobody shall modify a published dataset version." |
| 4 | **Necessary** — traceable to an actor or objective | "The system shall use a graph database." | Delete, or restate as a constraint with a rationale |
| 5 | **Implementation-free** — states the need, not the design | "The system shall store SMILES in a `VARCHAR(255)`." | "The system shall store the canonical SMILES of every molecule." |
| 6 | **Traceable** — has an ID other documents can cite | An unnumbered paragraph | `FR-07`, cited by the ER model and a test |

Identifiers used by this project: `FR-NN` functional, `NFR-NN` non-functional,
`RISK-NN` risks. Later weeks cite them by ID, so the IDs must not be renumbered
once committed.

### 5.7 Scope, non-goals and definition of done

**Non-goals** are as important as goals, and this project has strong ones:
docking, protein-structure prediction, graph neural networks, molecular
generation, clinical information, drug recommendation and cloud infrastructure
are all out. Writing them down stops week 14 from turning into a chemistry
project.

A **definition of done** turns "finished" into a checklist that someone else can
verify — schema migrated, tests passing, documentation updated, evidence saved.
Yours goes at the end of `docs/02_requirements.md`.

## 6. Guided work (required)

Produce `docs/01_problem_statement.md`. The file already exists as a skeleton
with `TODO:` markers; replace every marker. Expected result after each step is
stated.

1. **Copy the working context.** Open `starter/problem-statement-worksheet.md`
   and answer its five framing questions in rough notes: who suffers today, what
   data exists, what decision the system supports, what "better" means, and what
   is explicitly not being solved.
   *Expected:* five short paragraphs, no jargon.
2. **Write section 1, Problem.** Two to four sentences, no solution words
   ("database", "FastAPI") allowed.
   *Expected:* a reader who knows no chemistry can restate the problem.
3. **Write section 2, Context and current practice.** Describe the file-based
   status quo — spreadsheets, ad-hoc scripts, results in notebooks — and name
   three concrete failures it causes.
   *Expected:* each failure maps to a row of the table in section 5.1.
4. **Write section 3, Objectives.** Three to five objectives, each measurable.
   *Expected:* every objective names a number or a verifiable state.
5. **Write section 4, Scope and non-goals.** In-scope list, out-of-scope list.
   Copy the project's non-goals and add at least two of your own.
   *Expected:* nothing in scope contradicts `README.md`'s scope rule.
6. **Write section 5, Actors.** One row per actor from section 5.5, with their
   goal, their main interaction and the harm if their needs are ignored.
   *Expected:* at least five actors, each later cited by a requirement.
7. **Write section 6, Success criteria and educational-use statement.**
   *Expected:* the statement that all molecular results are teaching artefacts,
   not scientific findings, appears verbatim from `README.md`.
8. **Commit the file on its own.**
   *Expected:* `git log --oneline -1` shows a `docs(week-01)` commit.

## 7. Independent work (required)

No step list. Produce two documents, and expect to revise them once.

**A. `docs/02_requirements.md`**

- At least **12 functional requirements**, `FR-01` upward, each with: ID,
  requirement sentence, actor, priority (`MUST` / `SHOULD` / `COULD`), and the
  verification method (which later week or test proves it).
- At least **8 non-functional requirements**, `NFR-01` upward, each naming a
  measurable target and a measurement method. Cover at least: performance,
  integrity, reliability/recoverability, security, usability, maintainability,
  reproducibility and portability.
- A **traceability table** mapping every requirement to the week that
  implements it and to the actor that needs it.
- An **initial risk register**: at least six risks, `RISK-01` upward, each with
  likelihood, impact, mitigation and owner. Include at least one data-quality
  risk, one performance risk and one scope risk.
- A **definition of done** for a week and for the project.

**B. `docs/03_architecture.md`**

- A **three-tier diagram** in Mermaid, committed as source (the repository rule
  is diagrams as source plus an export where an image is needed), showing
  presentation, application and data tiers, the ML/ETL batch component, and the
  protocol on every arrow.
- A **responsibility table**: for each of at least eight responsibilities, the
  owning tier and one sentence of justification.
- A **file-system versus DBMS comparison** across the six dimensions of section
  5.1, each with a MoleculeTrace example.
- A **two-tier versus three-tier comparison** with the decision and its
  rationale.
- A **data-flow narrative**: follow one activity observation from CSV to
  dashboard, and one prediction from model version to stored row, naming every
  component and every place a rule is enforced.
- A **levels-of-abstraction section** naming what lives at the physical, logical
  and view level in this project, plus one example each of physical and logical
  data independence.

Keep both documents in the same numbering scheme; later weeks will append, not
renumber.

## 8. Exercises

Files live in `exercises/`. Worksheets with `TODO:` markers live in `starter/`.

| # | File | Type | Required? |
|---|------|------|-----------|
| 1 | `exercises/01-scenarios.md` | Scenario analysis | Required |
| 2 | `exercises/02-ambiguous-requirements.md` | Requirement rewriting | Required |
| 3 | `exercises/03-file-vs-dbms.md` | Comparison | Required |
| 4 | `exercises/04-architecture-decision.md` | Design argument | Required |
| 5 | `exercises/05-abstraction-and-independence.md` | Concept drill | **Optional (stretch)** |

Optional exercises are never assumed by a later week.

## 9. Validation

```bash
make test-week WEEK=week-01-requirements-and-architecture
```

The tests read your three documents and check the structure the later weeks
depend on: the required sections exist, there are at least 12 `FR-` and at least
8 `NFR-` identifiers with no duplicates or gaps, at least 6 `RISK-` entries, a
Mermaid diagram is present with all three tiers, and no `TODO:` marker is left
behind. They do not grade your prose — a human does that with the rubric.

Then:

```bash
make lint
```

Compare your documents against `expected-outputs/` for shape (headings,
identifier format, table columns), not for wording.

## 10. Common mistakes

- **Solution-first problem statement** → the problem section contains the words
  "PostgreSQL", "table" or "API" → rewrite it describing only the pain and the
  decision to be supported.
- **Untestable non-functional requirements** → "fast", "secure", "easy" with no
  number → attach a metric, a threshold, a workload and a measurement method.
- **Compound requirements** → the sentence contains "and" joining two
  obligations → split into two IDs.
- **Requirements that describe the implementation** → the sentence names a data
  type, an index or a library → restate as the need, and move the design note to
  `docs/03_architecture.md`.
- **Actors invented but never used** → an actor appears in the table but in no
  requirement → delete the actor or add the requirement.
- **Business rules assigned only to the application** → the responsibility table
  gives the application sole ownership of a rule about the data itself → move it
  to the database and keep the application check as early feedback.
- **Two-tier diagram labelled three-tier** → the dashboard has an arrow straight
  to PostgreSQL → route it through the application tier, or state and justify the
  exception explicitly.
- **Renumbering IDs** → a later edit shifts `FR-07` to `FR-08` → append new IDs
  at the end; never reuse or renumber.

## 11. Reflection questions

Answer in `REFLECTION.md`:

1. Which of your requirements was hardest to make testable, and what did you
   have to decide about the system before you could measure it?
2. Name one responsibility you first gave to the application and then moved to
   the database (or the reverse). What convinced you?
3. Week 00 gave you a running database and a health endpoint. Which of this
   week's non-functional requirements is already partly satisfied by that work,
   and which part is still unproven?

## 12. Completion checklist

- [ ] Retrieval practice answered before consulting notes.
- [ ] Conceptual notes summarised in `LEARNING_NOTES.md`.
- [ ] `docs/01_problem_statement.md` complete, no `TODO:` markers left.
- [ ] `docs/02_requirements.md` complete: ≥12 `FR-`, ≥8 `NFR-`, ≥6 `RISK-`,
      traceability table, definition of done.
- [ ] `docs/03_architecture.md` complete: Mermaid three-tier diagram,
      responsibility table, file-versus-DBMS comparison, two-tier versus
      three-tier decision, data-flow narrative, abstraction levels.
- [ ] Required exercises 1–4 done.
- [ ] `make test-week WEEK=week-01-requirements-and-architecture` passes.
- [ ] Shapes match `expected-outputs/`.
- [ ] `REFLECTION.md` completed.
- [ ] Portfolio evidence saved (section 14).
- [ ] Work committed and the progress table in the root `README.md` updated.

## 13. Syllabus mapping

| Syllabus topic | Covered by |
|----------------|-----------|
| Database systems versus file systems | sections 5.1, 8 (exercise 3), `docs/03_architecture.md` |
| Levels of abstraction; schema and instance; data independence | section 5.2, exercise 5, `docs/03_architecture.md` |
| Two-tier and three-tier DBMS architecture | sections 5.3, 7B, exercise 4 |
| Database users and administrators | section 5.5, `docs/01_problem_statement.md` §5 |
| Requirements analysis preceding conceptual design | sections 5.6–5.7, section 7A |

See [`SYLLABUS_MAPPING.md`](../../SYLLABUS_MAPPING.md).

## 14. Portfolio evidence

Save to `docs/portfolio/week-01/`:

- `requirements-summary.md` — your five strongest requirements (mixed FR and
  NFR) with their verification methods, and the top three risks.
- An export or copy of the three-tier diagram.
- A one-paragraph write-up, suitable for a README or an interview, explaining
  why MoleculeTrace is three-tier and what the database owns that the
  application does not.

## 15. Suggested Git commit

```bash
git add -A
git commit -m "docs(week-01): define problem, requirements and three-tier architecture"
```

## 16. Rubric (out of 10)

| Criterion | Weight | 0 | 1 | 2 |
|-----------|--------|---|---|---|
| Correctness of required exercises | 3 | Not attempted | Partly correct | Fully correct and validated |
| Depth of conceptual understanding (notes + reflection) | 2 | Absent | Restates the text | Explains in own words with a project example |
| Quality of the project improvement | 2 | None | Documents exist but are vague or untestable | Atomic, testable, traceable requirements and a defensible architecture |
| Validation and evidence | 2 | None | Partial | All checks pass, evidence saved |
| Git hygiene and documentation | 1 | Absent | Inconsistent | Clear commits, progress table updated |

Scoring: multiply each criterion's score (0–2) by its weight, divide by 2,
round to the nearest whole number. **Pass mark: 7/10.** The detailed rubric
lives in [`instructor/rubrics/`](../../instructor/rubrics/).
