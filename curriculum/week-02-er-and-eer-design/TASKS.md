# Week 02 — Tasks

ER and EER design. Required work must fit in five focused hours. Optional work
is a stretch and is never assumed by a later week. Tick a task only when its
stated proof produces the stated result.

## Required

- [ ] **R1 — Retrieval practice** (15 min)
      Answer the three questions in README section 3 in `LEARNING_NOTES.md`
      before opening week 01.

- [ ] **R2 — Conceptual notes** (60 min)
      Read README section 5, then write sections 2–4 of `LEARNING_NOTES.md` in
      your own words.
      *Proof:* the attribute-kind table and the weak-entity test list are filled
      in with a MoleculeTrace example each.

- [ ] **R3 — Initial ER model** (60 min)
      Follow README section 6 using `starter/er-initial.mmd`,
      `starter/attribute-classification.md` and
      `starter/relationship-narratives.md`; write sections 1–3 of
      `docs/data-model.md`.
      *Proof:* `grep -c '```mermaid' docs/data-model.md` prints 1 or more and
      all sixteen concept names appear in the document.

- [ ] **R4 — Improved EER model** (45 min)
      Write section 4 of `docs/data-model.md` from
      `starter/eer-improved.mmd`: multivalued attributes extracted, redundancy
      removed, specialisation applied, plus a before/after list of at least six
      differences.
      *Proof:* `grep -c '```mermaid' docs/data-model.md` prints 2 or more.

- [ ] **R5 — Cardinality and participation tables** (30 min)
      Write sections 5 and 6 of `docs/data-model.md` from
      `starter/cardinality-table.md` and `starter/participation-table.md`.
      *Proof:* every relationship appears in both tables; no cell is blank; at
      least one `1:1`, six `1:N` and two `M:N` rows.

- [ ] **R6 — Weak entity and specialisation arguments** (25 min)
      Write sections 7 and 8 of `docs/data-model.md`.
      *Proof:* section 7 names owner, identifying relationship and partial key;
      section 8 states disjoint/overlapping and total/partial.

- [ ] **R7 — Relationship narratives and decision log** (25 min)
      Write sections 9 and 10 of `docs/data-model.md` using
      `starter/design-decision-log.md`.
      *Proof:* `grep -c '^| DD-' docs/data-model.md` prints 8 or more, and every
      relationship in the cardinality table has a narrative.

- [ ] **R8 — Exercise 1, repair five broken ER fragments** (25 min)
      `exercises/01-broken-er-fragments.md` — all five diagnosed and repaired.

- [ ] **R9 — Exercise 2, cardinality and participation drill** (15 min)
      `exercises/02-cardinality-and-participation.md`.

- [ ] **R10 — Exercise 3, weak entities** (10 min)
      `exercises/03-weak-entities.md`.

- [ ] **R11 — Exercise 4, attributes and redundancy** (10 min)
      `exercises/04-attributes-and-redundancy.md`.

- [ ] **R12 — Validate** (15 min)
      `make test-week WEEK=week-02-er-and-eer-design` until it passes, then
      `make lint`.

- [ ] **R13 — Reflect, record and commit** (15 min)
      Fill in `REFLECTION.md`, save evidence to `docs/portfolio/week-02/`,
      update the progress table in the root `README.md`, commit with the message
      in README section 15 and claim the badge in `BADGE.md`.

## Optional (stretch)

- [ ] **O1 — Specialisation alternatives** —
      `exercises/05-specialisation-alternatives.md`.
- [ ] **O2 — Decision record** — write
      `docs/decisions/002-datasetversion-as-weak-entity.md` in the format
      described in `docs/decisions/README.md`, citing the requirement IDs that
      force immutable dataset versions.
- [ ] **O3 — Adversarial review** — ask someone else (or your future self after
      a break) to read only your relationship narratives, redraw the diagram
      from them, and compare. Every difference is an ambiguous sentence.

## Deliverables

| Deliverable | Path |
|-------------|------|
| Initial ER model, improved EER model, cardinality and participation tables, weak-entity and specialisation arguments, narratives, decision log | `docs/data-model.md` |
| Completed exercises | `curriculum/week-02-er-and-eer-design/exercises/` |
| Notes and reflection | `curriculum/week-02-er-and-eer-design/LEARNING_NOTES.md`, `REFLECTION.md` |
| Evidence | `docs/portfolio/week-02/er-model-summary.md` |
