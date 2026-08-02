# Starter — Requirement-quality checklist

Keep this open while writing `docs/02_requirements.md`. Run every requirement
through all six tests. A requirement that fails any test is rewritten, not
excused.

| # | Test | Ask | Smell words |
|---|------|-----|-------------|
| Q1 | Atomic | Exactly one obligation? | "and", "also", "as well as" |
| Q2 | Testable | Which check makes it pass or fail? | "fast", "reliable", "user-friendly" |
| Q3 | Unambiguous | Can two readers disagree about what passes? | "manage", "handle", "support", "appropriate", "etc." |
| Q4 | Necessary | Which actor or objective needs it? | requirements with no actor |
| Q5 | Implementation-free | Does it name a design instead of a need? | column types, index names, library names |
| Q6 | Traceable | Does it have a stable ID that other documents cite? | unnumbered prose |

## Sentence pattern

> **FR-NN** — The system **shall** `<observable behaviour>` **when**
> `<trigger or precondition>`, **so that** `<actor>` can `<goal>`.

> **NFR-NN** — The system **shall** `<quality>` measured as `<metric>`,
> reaching `<threshold>` under `<workload>`, verified by `<method>`.

## Self-review pass (do this once before validating)

- [ ] Every requirement has an ID, and no ID appears twice.
- [ ] Every actor in `docs/01_problem_statement.md` is named by ≥1 requirement.
- [ ] No requirement contradicts a non-goal.
- [ ] Every `MUST` requirement has a verification method naming a week or a test.
- [ ] Every NFR has a number and a unit.
- [ ] Two requirements chosen at random can be handed to someone else, who can
      say what they would run to check them.

## TODO for you

TODO: after your self-review, record here the three requirements you changed and
which test each failed. This is the evidence for exercise 2, part B.
