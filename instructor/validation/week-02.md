# Week 02 — Validation notes (instructor only)

How to confirm week 02 is genuinely complete. Week 02 produces no database
objects, so every check reads `docs/data-model.md` and the exercise files.

## 1. Commands and expected results

Run from the repository root.

| # | Command | Expected result |
|---|---------|-----------------|
| 1 | `make test-week WEEK=week-02-er-and-eer-design` | All tests pass. |
| 2 | `make lint` | No errors on changed files. |
| 3 | `grep -c 'TODO:' docs/data-model.md` | `0` |
| 4 | `grep -c '```mermaid' docs/data-model.md` | `2` or more |
| 5 | `grep -c '^| DD-' docs/data-model.md` | `8` or more |
| 6 | `grep -Eo '\| (1:1\|1:N\|M:N) \|' docs/data-model.md \| sort \| uniq -c` | at least 1 × `1:1`, 6 × `1:N`, 2 × `M:N` |
| 7 | `grep -c 'TODO' curriculum/week-02-er-and-eer-design/exercises/01-broken-er-fragments.md` | `0` |

A clean clone reproduces all of these without a database: `make install`, then
command 1. No `TEST_DATABASE_URL` is needed this week.

## 2. What the automated tests deliberately do not check

The tests are structural. They cannot tell a good model from a bad one, so the
following must be inspected by hand against
[`../solution-notes/week-02.md`](../solution-notes/week-02.md):

1. **Whether the cardinalities are right.** The test only checks that the cell
   contains a legal value and that a domain rule is stated. Read the rules; a
   rule that describes the current CSV files instead of the world is a fail.
2. **Whether the two diagrams actually differ.** Diff the two Mermaid blocks.
   Identical blocks with a populated before/after table means the improvements
   were written but not made.
3. **Whether the narratives match the diagram.** Pick three relationships at
   random and check that the sentence, the cardinality row and the diagram edge
   agree. Disagreement is usually a diagram that was edited after the tables.
4. **Whether the weak-entity argument is an argument.** The test only counts
   words and looks for three terms. Look for the three tests applied, the partial
   key named and the rejected alternative costed.
5. **Whether redundancy was actually removed.** Search the improved model for
   `_count`, `_name` repeated across entity sets, and any `is_` flag.
6. **Whether all five broken fragments were repaired**, not merely diagnosed. A
   repair without Mermaid source is half an answer.

## 3. Known-good failure modes

| Failure | Usual cause | What to tell the student |
|---------|-------------|--------------------------|
| `test_all_sixteen_concepts_are_accounted_for` | A concept was dropped as "not needed" | Every concept must be *classified* in section 1, even if the verdict is "attribute of X". |
| `test_both_diagrams_are_present_as_mermaid_source` | The placeholder entity was replaced by an image link | Diagrams are committed as source; an export goes in `docs/portfolio/week-02/`. |
| `test_cardinality_rows_are_complete` | The domain-rule cell says "by design" | Restate as a fact about the world. |
| `test_every_relationship_has_a_participation_row` | The relationship was renamed in one table only | Names must match exactly between sections 5, 6 and 9. |
| `test_narratives_avoid_implementation_jargon` | "linked by a foreign key" in a narrative | The narrative is for a bench scientist; the foreign key is week 03's business. |
| `test_design_decision_log_is_populated` | Fewer than eight decisions, or `DD-03` missing | IDs run consecutively from `DD-01` and are never renumbered. |

## 4. Interaction with later weeks

- **Week 03** generates DDL from this model. If a student's entity set has no
  identifying attribute at all, week 03 will invent a surrogate key and the
  conceptual model will drift. Catch it here.
- **Week 04** normalises the result. A redundant attribute left in section 4
  reappears as an update anomaly; it is worth pointing at the week-02 decision
  log when it does.
- **Week 09** turns the participation table into constraints. Any `total` cell
  that the student cannot restate as "this may not be null / this may not be
  orphaned" was guessed.
- **Week 15** depends on `DatasetVersion` being weak and immutable, and on
  experiments training on exactly one dataset version.

## 5. Grading order that saves time

1. Read section 9 (narratives) first. If the sentences are clear and complete,
   the model is usually sound and the rest of the review is quick.
2. Then the participation table, which is where errors cluster.
3. Then the before/after list, diffing the two diagrams as you go.
4. Then exercise 1, which is the sharpest signal of whether the concepts
   transferred.
5. The decision log last — it is the easiest place to award or withhold the
   final mark for depth.
