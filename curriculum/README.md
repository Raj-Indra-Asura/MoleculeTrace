# curriculum/

The course. Twenty-four week folders plus the template they are made from.

## Using a week

1. Read `README.md` top to bottom before starting.
2. Work through `TASKS.md`, keeping to the five-hour plan.
3. Fill in `LEARNING_NOTES.md` as you go, not afterwards.
4. Validate with `make test-week WEEK=week-XX-<slug>`.
5. Complete `CHECKPOINT.md` and `REFLECTION.md`.
6. Commit using the suggested message and update the progress table in the root
   `README.md`.

## Standard week folder

| Item | Purpose |
|------|---------|
| `README.md` | The lesson: objectives, plan, concepts, guided and independent work, validation, rubric |
| `LEARNING_NOTES.md` | Your own summary of the theory |
| `TASKS.md` | Required and optional task list with time estimates |
| `CHECKPOINT.md` | Pass/fail criteria that later weeks depend on |
| `REFLECTION.md` | Reflection answers and a confidence check |
| `RESOURCES.md` | Official documentation used this week |
| `starter/` | Skeleton files with `TODO:` markers — never solutions |
| `exercises/` | Numbered exercises, marked required or optional |
| `tests/` | Automated validation for the week |
| `expected-outputs/` | Reference outputs to compare against |

## Adding or editing a week

Copy `_TEMPLATE/` to `week-XX-<slug>/` and replace every placeholder. Keep all
sixteen `README.md` sections: a week is not complete without a title, learning
objectives, the MoleculeTrace connection, prerequisites, a five-hour plan,
conceptual notes, guided work, independent work, exercises, validation
instructions, common mistakes, reflection questions, a completion checklist,
syllabus mapping, portfolio evidence, a suggested commit and a rubric out of 10.

Week *N* may only assume weeks `00 … N-1`, must include retrieval practice from
earlier weeks, and must deliver a visible project improvement.
