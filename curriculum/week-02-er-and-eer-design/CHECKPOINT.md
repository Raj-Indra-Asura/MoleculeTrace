# Week 02 — Checkpoint

A week counts as complete only when every item below is true. Later weeks assume
this checkpoint has passed: week 03 generates DDL from your entity sets and
cardinalities, week 04 normalises the result, week 09 turns your participation
constraints into database constraints, and week 15 depends on `DatasetVersion`
being weak and immutable. Run every command from the repository root.

## Automated

```bash
make test-week WEEK=week-02-er-and-eer-design
```

- [ ] All tests pass.

```bash
make lint
```

- [ ] `make lint` reports no errors on files you changed.

## Manual

Each command with its exact expected result:

```bash
grep -c 'TODO:' docs/data-model.md
```
- [ ] Prints `0` — no skeleton markers left.

```bash
grep -c '```mermaid' docs/data-model.md
```
- [ ] Prints 2 or more: the initial ER diagram (§2) and the improved EER
      diagram (§4).

```bash
grep -c '^| DD-' docs/data-model.md
```
- [ ] Prints 8 or more design decisions.

```bash
grep -Eo '\| (1:1|1:N|M:N) \|' docs/data-model.md | sort | uniq -c
```
- [ ] Shows at least one `1:1`, at least six `1:N` and at least two `M:N` rows.

```bash
grep -c 'TODO' curriculum/week-02-er-and-eer-design/exercises/01-broken-er-fragments.md
```
- [ ] Prints `0` — all five fragments diagnosed and repaired.

```bash
git log --oneline -1
```
- [ ] Shows your week-02 commit, message formatted `docs(week-02): ...`.

## Model review (self-assessed, all must be true)

- [ ] All sixteen domain concepts from README section 5.1 appear in
      `docs/data-model.md`, each classified as entity set, associative entity,
      relationship set or attribute.
- [ ] Every relationship in the improved model appears in **both** the
      cardinality table and the participation table.
- [ ] Participation is stated for **both** sides of every relationship; no cell
      is blank and no cell says "n/a".
- [ ] Every cardinality row names a **domain rule**, not a property of today's
      sample data.
- [ ] Every relationship has a plain-language sentence in each direction, and
      none of them uses the words "foreign key", "join" or "table".
- [ ] No multivalued attribute survives in the improved EER model.
- [ ] Every derived attribute is labelled derived and names who would recompute
      it.
- [ ] No attribute appears in two entity sets with the same meaning.
- [ ] No relationship can be removed without losing a fact (no redundant
      shortcut edges).
- [ ] `DatasetVersion` is presented as weak, with owner, identifying
      relationship, partial key and the resulting full identifier.
- [ ] The specialisation in §8 states disjoint-or-overlapping and
      total-or-partial, and explains the multi-role case.
- [ ] Each `DD-` entry names an alternative that was rejected and its cost.

## Artefacts

- [ ] Required exercises 1–4 committed.
- [ ] `docs/data-model.md` committed.
- [ ] `LEARNING_NOTES.md` and `REFLECTION.md` filled in.
- [ ] Portfolio evidence saved to `docs/portfolio/week-02/`.
- [ ] Progress table in the root `README.md` updated with status, rubric score
      and commit hash.
- [ ] Week 2 badge criteria in [`BADGE.md`](BADGE.md) all met.

## Self-assessed rubric score

| Criterion | Weight | Score (0–2) |
|-----------|--------|-------------|
| Correctness of required exercises | 3 | |
| Depth of conceptual understanding | 2 | |
| Quality of the project improvement | 2 | |
| Validation and evidence | 2 | |
| Git hygiene and documentation | 1 | |

**Total: __ / 10** (pass mark 7)
