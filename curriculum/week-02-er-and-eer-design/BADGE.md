# Week 2 Badge — Domain Modeller

A badge is a public, verifiable claim: award it to yourself only when every
criterion below is objectively true.

| Field | Value |
|-------|-------|
| Badge ID | `week-02-domain-modeller` |
| Name | Domain Modeller |
| Phase | 0. Foundations |
| Icon | 🧬 |
| Issued by | MoleculeTrace Learning System (self-issued, evidence-backed) |
| Evidence | `docs/portfolio/week-02/er-model-summary.md` + the week-02 commit hash |

## Criteria

All five must be true:

1. **Model drawn twice** — `docs/data-model.md` contains an initial ER diagram
   and an improved EER diagram, both as Mermaid source, with a before/after list
   of at least six defects removed.
2. **Constraints stated** — the cardinality table covers every relationship with
   a domain rule for each, and the participation table states both sides of
   every relationship with no blank cells.
3. **EER reasoning shown** — `DatasetVersion` is argued as a weak entity with
   owner, identifying relationship and partial key; the user–role section states
   disjointness and totality and handles the multi-role case.
4. **Model explained and justified** — every relationship has a plain-language
   sentence in both directions, and the design-decision log holds at least eight
   `DD-` entries, each naming a rejected alternative.
5. **Validated and committed** — `make test-week WEEK=week-02-er-and-eer-design`
   passes, all five broken ER fragments in exercise 1 are repaired, and a
   Conventional Commits message is pushed with the root `README.md` progress
   table updated.

Minimum rubric score: **7/10** (`CHECKPOINT.md`).

## Claiming it

Add this line to `docs/portfolio/week-02/er-model-summary.md`:

```markdown
🧬 **Week 2 badge — Domain Modeller** · earned <YYYY-MM-DD> · commit `<hash>`
```

and set week 02 to `✅ Complete` in the progress table in the root `README.md`.

## Revoking it

The badge lapses if week 03 has to invent an entity set or a key that the
conceptual model never named, or if week 04 finds a normalisation defect that a
redundant attribute in your EER model caused. Repair `docs/data-model.md`, then
re-claim it with a new date.
