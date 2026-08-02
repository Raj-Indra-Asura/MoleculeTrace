# Week 01 — Tasks

Requirements and architecture. Required work must fit in five focused hours.
Optional work is a stretch and is never assumed by a later week. Tick a task
only when its stated proof produces the stated result.

## Required

- [ ] **R1 — Retrieval practice** (15 min)
      Answer the three questions in README section 3 in `LEARNING_NOTES.md`
      before opening week 00.

- [ ] **R2 — Conceptual notes** (60 min)
      Read README section 5, then write sections 2–4 of `LEARNING_NOTES.md` in
      your own words.
      *Proof:* the schema-versus-instance and two-tier-versus-three-tier
      entries are filled in with a MoleculeTrace example each.

- [ ] **R3 — Problem statement** (60 min)
      Complete `docs/01_problem_statement.md` following README section 6, using
      `starter/problem-statement-worksheet.md`.
      *Proof:* `grep -c 'TODO:' docs/01_problem_statement.md` prints `0`.

- [ ] **R4 — Requirements** (55 min)
      Complete `docs/02_requirements.md`: ≥12 functional, ≥8 non-functional
      requirements, traceability table, risk register (≥6 risks), definition of
      done.
      *Proof:* `grep -c '^| FR-' docs/02_requirements.md` prints 12 or more and
      `grep -c '^| NFR-' docs/02_requirements.md` prints 8 or more.

- [ ] **R5 — Architecture** (35 min)
      Complete `docs/03_architecture.md`: Mermaid three-tier diagram,
      responsibility table, file-system versus DBMS comparison, tier decision,
      data-flow narrative, abstraction levels.
      *Proof:* the file contains a ```mermaid``` block naming all three tiers.

- [ ] **R6 — Exercise 1, scenarios** (15 min)
      `exercises/01-scenarios.md`.

- [ ] **R7 — Exercise 2, ambiguous requirements** (15 min)
      `exercises/02-ambiguous-requirements.md` — rewrite all eight, and add two
      ambiguous requirements found in your *own* `docs/02_requirements.md`.

- [ ] **R8 — Exercise 3, file system versus DBMS** (10 min)
      `exercises/03-file-vs-dbms.md`.

- [ ] **R9 — Exercise 4, architecture decision** (10 min)
      `exercises/04-architecture-decision.md`.

- [ ] **R10 — Validate** (15 min)
      `make test-week WEEK=week-01-requirements-and-architecture` until it
      passes, then `make lint`.

- [ ] **R11 — Reflect, record and commit** (15 min)
      Fill in `REFLECTION.md`, save evidence to `docs/portfolio/week-01/`,
      update the progress table in the root `README.md`, commit with the message
      in README section 15 and claim the badge in `BADGE.md`.

## Optional (stretch)

- [ ] **O1 — Abstraction drill** — `exercises/05-abstraction-and-independence.md`.
- [ ] **O2 — Architecture decision record** — write
      `docs/decisions/001-three-tier-architecture.md` in the format described in
      `docs/decisions/README.md`, citing the requirement IDs that forced the
      decision.
- [ ] **O3 — Adversarial review** — ask someone else (or your future self after
      a break) to find three requirements they can read two ways. Fix them and
      record the before/after.

## Deliverables

| Deliverable | Path |
|-------------|------|
| Problem statement | `docs/01_problem_statement.md` |
| Requirements, risks, definition of done | `docs/02_requirements.md` |
| Architecture | `docs/03_architecture.md` |
| Completed exercises | `curriculum/week-01-requirements-and-architecture/exercises/` |
| Notes and reflection | `curriculum/week-01-requirements-and-architecture/LEARNING_NOTES.md`, `REFLECTION.md` |
| Evidence | `docs/portfolio/week-01/requirements-summary.md` |
