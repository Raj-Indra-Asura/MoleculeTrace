# Week 00 — Orientation and Project Setup

<!--
  SCAFFOLD. This week was created from curriculum/_TEMPLATE/ and the lesson
  content has not been authored yet. Replace every <angle-bracket placeholder>
  and TODO. Do not delete sections: every week must contain all of them.
-->

**Phase:** 0. Foundations · **Required effort:** 5 hours ·
**Depends on:** none — this is the first week

**Topic scope:** Set up the toolchain, understand the MoleculeTrace domain end to end, and agree the working rhythm for the next 24 weeks.

## 1. Learning objectives

By the end of this week you can:

1. <verb + observable outcome>
2. <verb + observable outcome>
3. <verb + observable outcome>
4. <verb + observable outcome>

## 2. Connection to MoleculeTrace

<What part of the molecules → targets → assays → activities → datasets →
experiments → model versions → predictions → validation chain this week builds,
and the visible improvement the project gains by Friday.>

**Visible improvement this week:** <one sentence>

## 3. Prerequisites

- Completed checkpoints for weeks <list>.
- <Tools or data that must already exist.>

### Retrieval practice (15 minutes, required)

Answer from memory before opening any notes:

1. <question drawn from an earlier week>
2. <question drawn from an earlier week>
3. <question drawn from an earlier week>

Check your answers against `curriculum/week-<earlier>/LEARNING_NOTES.md`.

## 4. Five-hour study plan

| Block | Time | Activity | Output |
|-------|------|----------|--------|
| 1 | 0:00–0:15 | Retrieval practice | Three written answers |
| 2 | 0:15–1:15 | Conceptual notes (section 5) | Notes in `LEARNING_NOTES.md` |
| 3 | 1:15–2:45 | Guided work (section 6) | <artefact> |
| 4 | 2:45–4:15 | Independent work and exercises (sections 7–8) | <artefact> |
| 5 | 4:15–4:45 | Validation (section 9) | Passing checks |
| 6 | 4:45–5:00 | Reflection and commit (sections 11–15) | Commit pushed |

## 5. Conceptual notes

<Concise explanation of the week's theory, written to be read in one hour.
Define every term used later in the exercises. Link to official documentation in
RESOURCES.md rather than restating it.>

## 6. Guided work (required)

Step-by-step, with expected output stated for each step.

1. <step>
2. <step>
3. <step>

## 7. Independent work (required)

<A task with a stated goal but no step list. This is the part that goes in the
portfolio.>

## 8. Exercises

Files live in `exercises/`. Starter files with `TODO:` markers live in
`starter/`.

| # | File | Type | Required? |
|---|------|------|-----------|
| 1 | `exercises/01-<name>.sql` | SQL | Required |
| 2 | `exercises/02-<name>.py` | Python | Required |
| 3 | `exercises/03-<name>.md` | Design | Required |
| 4 | `exercises/04-<name>.md` | <type> | **Optional (stretch)** |

Optional exercises are never assumed by a later week.

## 9. Validation

```bash
make test-week WEEK=week-00-orientation
```

Compare your outputs against `expected-outputs/`. <Any additional manual check,
with the exact command and the exact expected result.>

## 10. Common mistakes

- <mistake> → <how to recognise it> → <fix>
- <mistake> → <how to recognise it> → <fix>
- <mistake> → <how to recognise it> → <fix>

## 11. Reflection questions

Answer in `REFLECTION.md`:

1. <question about the concept>
2. <question about the design decision made this week>
3. <question connecting this week to an earlier week>

## 12. Completion checklist

- [ ] Retrieval practice answered before consulting notes.
- [ ] Conceptual notes summarised in `LEARNING_NOTES.md`.
- [ ] Guided work completed.
- [ ] Independent work completed.
- [ ] All required exercises done.
- [ ] `make test-week WEEK=week-00-orientation` passes.
- [ ] Outputs match `expected-outputs/`.
- [ ] `REFLECTION.md` completed.
- [ ] Portfolio evidence saved (section 14).
- [ ] Work committed and the progress table in the root `README.md` updated.

## 13. Syllabus mapping

| Syllabus topic | Covered by |
|----------------|-----------|
| <topic> | sections <n> |

See [`SYLLABUS_MAPPING.md`](../../SYLLABUS_MAPPING.md).

## 14. Portfolio evidence

Save to `docs/portfolio/week-00/`:

- <artefact, e.g. ER diagram, EXPLAIN plan, metric table, screenshot>
- <one-paragraph write-up suitable for a README or interview>

## 15. Suggested Git commit

```bash
git add -A
git commit -m "<type>(week-00): <imperative summary>"
```

## 16. Rubric (out of 10)

| Criterion | Weight | 0 | 1 | 2 |
|-----------|--------|---|---|---|
| Correctness of required exercises | 3 | Not attempted | Partly correct | Fully correct and validated |
| Depth of conceptual understanding (notes + reflection) | 2 | Absent | Restates the text | Explains in own words with a project example |
| Quality of the project improvement | 2 | None | Works but rough | Clean, documented, tested |
| Validation and evidence | 2 | None | Partial | All checks pass, evidence saved |
| Git hygiene and documentation | 1 | Absent | Inconsistent | Clear commits, progress table updated |

Scoring: multiply each criterion's score (0–2) by its weight, divide by 2,
round to the nearest whole number. **Pass mark: 7/10.** The detailed rubric
lives in [`instructor/rubrics/`](../../instructor/rubrics/).
