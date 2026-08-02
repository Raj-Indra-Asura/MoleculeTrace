# Week 01 — Checkpoint

A week counts as complete only when every item below is true. Later weeks assume
this checkpoint has passed: week 02 models the entities named in your problem
statement, and weeks 09, 13, 17 and 21 are verified against your requirement
IDs. Run every command from the repository root.

## Automated

```bash
make test-week WEEK=week-01-requirements-and-architecture
```

- [ ] All tests pass.

```bash
make lint
```

- [ ] `make lint` reports no errors on files you changed.

## Manual

Each command with its exact expected result:

```bash
grep -c 'TODO:' docs/01_problem_statement.md docs/02_requirements.md docs/03_architecture.md
```
- [ ] Every file reports `0` — no skeleton markers left.

```bash
grep -c '^| FR-' docs/02_requirements.md
```
- [ ] Prints 12 or more.

```bash
grep -c '^| NFR-' docs/02_requirements.md
```
- [ ] Prints 8 or more.

```bash
grep -c '^| RISK-' docs/02_requirements.md
```
- [ ] Prints 6 or more.

```bash
grep -c '```mermaid' docs/03_architecture.md
```
- [ ] Prints 1 or more, and the diagram shows presentation → application → data
      with the protocol on each arrow.

```bash
git log --oneline -1
```
- [ ] Shows your week-01 commit, message formatted `docs(week-01): ...`.

## Requirement-quality review (self-assessed, all must be true)

Take any five requirements at random and check each against the checklist in
README section 5.6:

- [ ] **Atomic** — none of the five states two obligations.
- [ ] **Testable** — each names a check, a threshold or an observable state.
- [ ] **Unambiguous** — each has exactly one reading; no "fast", "easy",
      "appropriate", "as needed", "etc.".
- [ ] **Necessary** — each traces to an actor in `docs/01_problem_statement.md`.
- [ ] **Implementation-free** — none names a library, data type or index.
- [ ] **Traceable** — each has a stable ID cited in the traceability table.
- [ ] Every actor listed in the problem statement is referenced by at least one
      requirement.
- [ ] Every non-goal in the problem statement is contradicted by no requirement.

## Artefacts

- [ ] Required exercises 1–4 committed.
- [ ] `docs/01_problem_statement.md`, `docs/02_requirements.md` and
      `docs/03_architecture.md` committed.
- [ ] `LEARNING_NOTES.md` and `REFLECTION.md` filled in.
- [ ] Portfolio evidence saved to `docs/portfolio/week-01/`.
- [ ] Progress table in the root `README.md` updated with status, rubric score
      and commit hash.
- [ ] Week 1 badge criteria in [`BADGE.md`](BADGE.md) all met.

## Self-assessed rubric score

| Criterion | Weight | Score (0–2) |
|-----------|--------|-------------|
| Correctness of required exercises | 3 | |
| Depth of conceptual understanding | 2 | |
| Quality of the project improvement | 2 | |
| Validation and evidence | 2 | |
| Git hygiene and documentation | 1 | |

**Total: __ / 10** (pass mark 7)
