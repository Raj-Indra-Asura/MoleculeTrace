# Week 1 Badge — Requirements Architect

A badge is a public, verifiable claim: award it to yourself only when every
criterion below is objectively true.

| Field | Value |
|-------|-------|
| Badge ID | `week-01-requirements-architect` |
| Name | Requirements Architect |
| Phase | 0. Foundations |
| Icon | 📐 |
| Issued by | MoleculeTrace Learning System (self-issued, evidence-backed) |
| Evidence | `docs/portfolio/week-01/requirements-summary.md` + the week-01 commit hash |

## Criteria

All five must be true:

1. **Problem framed** — `docs/01_problem_statement.md` states the problem,
   scope, non-goals, at least five actors and measurable success criteria, with
   no `TODO:` markers left.
2. **Requirements written** — `docs/02_requirements.md` holds at least 12
   functional and 8 non-functional requirements, each with an ID, an actor, a
   priority and a verification method, plus a risk register of at least six
   entries and a definition of done.
3. **Architecture argued** — `docs/03_architecture.md` contains a Mermaid
   three-tier diagram, a responsibility table, the file-system versus DBMS
   comparison, the two-tier versus three-tier decision, a data-flow narrative
   and the three levels of abstraction.
4. **Validated** — `make test-week WEEK=week-01-requirements-and-architecture`
   passes and every requirement sampled in `CHECKPOINT.md` survives the
   requirement-quality checklist.
5. **Work committed** — a commit following the Conventional Commits format, with
   the root `README.md` progress table updated with status, rubric score and
   commit hash.

Minimum rubric score: **7/10** (`CHECKPOINT.md`).

## Claiming it

Add this line to `docs/portfolio/week-01/requirements-summary.md`:

```markdown
📐 **Week 1 badge — Requirements Architect** · earned <YYYY-MM-DD> · commit `<hash>`
```

and set week 01 to `✅ Complete` in the progress table in the root `README.md`.

## Revoking it

The badge lapses if a later week has to rewrite the problem statement because
scope was never really agreed — for example if week 02 models an entity that no
requirement asks for. Repair the documents, then re-claim it with a new date.
