# Week 0 Badge — Environment Ready

The first of 24 completion badges. A badge is a public, verifiable claim: award
it to yourself only when every criterion below is objectively true.

| Field | Value |
|-------|-------|
| Badge ID | `week-00-environment-ready` |
| Name | Environment Ready |
| Phase | 0. Foundations |
| Icon | 🧪 |
| Issued by | MoleculeTrace Learning System (self-issued, evidence-backed) |
| Evidence | `docs/portfolio/week-00/environment-check.md` + the week-00 commit hash |

## Criteria

All five must be true:

1. **Database runs** — `docker compose ps` shows `moleculetrace-db` running and
   healthy, started from the repository's `docker-compose.yml`.
2. **Database reachable** — `make psql` opens a session and `SELECT version();`
   returns PostgreSQL 16.x.
3. **Code connects** — `python scripts/check_db_connection.py` prints a line
   starting with `OK` and exits 0, reading credentials from `.env` only.
4. **Service and test pass** — `GET /health` returns HTTP 200 with
   `{"status":"ok","database":"up"}` and
   `make test-week WEEK=week-00-orientation` reports `1 passed`.
5. **Work committed** — a commit on branch `week-00-orientation` following the
   Conventional Commits format, with `.env` untracked, and the root `README.md`
   progress table updated with status, rubric score and commit hash.

Minimum rubric score: **7/10** (`CHECKPOINT.md`).

## Claiming it

Add this line to `docs/portfolio/week-00/environment-check.md`:

```markdown
🧪 **Week 0 badge — Environment Ready** · earned <YYYY-MM-DD> · commit `<hash>`
```

and set week 00 to `✅ Complete` in the progress table in the root `README.md`.

## Revoking it

The badge lapses if a later week finds the environment broken — for example the
health test fails on a clean checkout after `make reset && make up`. Fix the
environment, then re-claim it with a new date.
