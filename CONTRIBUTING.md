# Contributing to MoleculeTrace

MoleculeTrace is both a course and a project. Contributions come in two forms:
**student work** (progressing through the curriculum) and **maintenance**
(improving the curriculum itself). Both use the same workflow.

## Ground rules

1. Finished solutions never appear in student-facing folders
   (`curriculum/*/starter/`, `curriculum/*/exercises/`, `project/`).
   Instructor guidance belongs in `instructor/solution-notes/`.
2. Starter code uses explicit `TODO:` markers.
3. `labs/` contains pointer files only. Never add code, exercises, tests or
   expected outputs there. If content is duplicated, `curriculum/week-XX/` wins.
4. Synthetic data must be labelled synthetic — in the file name, in a header
   comment, and in the `README.md` of the folder that holds it.
5. Molecular results are educational artefacts, never scientific or medical
   claims.
6. Only document commands you have actually run.
7. Every week must produce a visible project improvement and must depend only on
   earlier, completed weeks.
8. Required work must fit in five focused hours. Anything beyond that is marked
   **Optional**.

## Workflow

```bash
git switch -c week-07-joins-and-aggregation
# do the week's work
make lint
make test
git add -A
git commit -m "feat(week-07): add assay aggregation queries"
git push -u origin week-07-joins-and-aggregation
```

Open a pull request using the template, then tick the week in the progress table
in `README.md` once the checkpoint passes.

## Branch naming

| Kind | Pattern | Example |
|------|---------|---------|
| Weekly work | `week-XX-<slug>` | `week-04-normalization` |
| Curriculum fix | `curriculum/<short-description>` | `curriculum/fix-week-09-rubric` |
| Project change | `project/<area>-<description>` | `project/backend-add-health-route` |
| Docs | `docs/<description>` | `docs/add-er-diagram` |

## Commit messages

Conventional Commits, with the week as the scope where relevant:

```
<type>(<scope>): <imperative summary>
```

Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `perf`.

Examples:

```
feat(week-03): create molecule, target and assay tables
docs(week-06): record relational algebra derivations
perf(week-17): add composite index on activity(target_id, assay_id)
```

Each week's `README.md` suggests a commit message — use it unless your work
diverged.

## Code style

- Python is formatted with `ruff format` and linted with `ruff check`
  (`make lint`, `make format`).
- SQL keywords uppercase, identifiers `snake_case`, one clause per line.
- Every table and column added to `project/database/` gets a `COMMENT ON`.
- Tests live in `project/tests/` for project code and in
  `curriculum/week-XX/tests/` for week validation.

## Reporting a problem with a week

Open an issue using the **Weekly problem** template
(`.github/ISSUE_TEMPLATE/weekly-problem.md`). Include the week folder, the exact
command you ran, the full output and what you expected.

## Security and data hygiene

- Never commit `.env`, credentials, tokens or connection strings.
  `.env.example` holds placeholders only.
- Never commit real proprietary or licence-restricted molecular datasets.
  Use the synthetic generator in `scripts/` or a clearly attributed public
  source documented in the week's `RESOURCES.md`.
