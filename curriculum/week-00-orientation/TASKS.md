# Week 00 — Tasks

Environment verification. Required work must fit in five focused hours. Optional
work is a stretch and is never assumed by a later week. Tick a task only when
its stated proof produces the stated result.

## Required

- [ ] **R1 — Baseline retrieval practice** (15 min)
      Answer the three questions in README section 3 in `LEARNING_NOTES.md`.

- [ ] **R2 — Tool versions** (10 min)
      `git --version`, `docker --version`, `docker compose version`,
      `python --version`.
      *Proof:* Compose v2 is present and Python is 3.11 or newer.

- [ ] **R3 — Repository tour and notes** (50 min)
      Read README section 5, `ROADMAP.md` and `CONTRIBUTING.md`; fill in
      `LEARNING_NOTES.md` sections 2–3.

- [ ] **R4 — Environment file** (10 min)
      `cp .env.example .env`, set your own `POSTGRES_PASSWORD`.
      *Proof:* `git check-ignore -v .env` prints a `.gitignore` rule.

- [ ] **R5 — Compose validation exercise** (20 min)
      Complete `exercises/01-compose-validation.md` using
      `starter/docker-compose.check.yml`.
      *Proof:* `docker compose config --quiet` succeeds for the root file and
      `docker compose -f curriculum/week-00-orientation/starter/docker-compose.check.yml config --quiet`
      succeeds for yours.

- [ ] **R6 — Start PostgreSQL** (15 min)
      `make up`.
      *Proof:* `docker compose ps` shows `moleculetrace-db` running and healthy.

- [ ] **R7 — Connect with psql** (25 min)
      `make psql`, then complete `exercises/02-psql-tour.sql`.
      *Proof:* `SELECT version();` returns PostgreSQL 16.x; `\conninfo` names
      database `moleculetrace`.

- [ ] **R8 — Python environment** (15 min)
      Create a virtual environment and run `make install`.
      *Proof:* `python -c "import fastapi, psycopg; print('ok')"` prints `ok`.

- [ ] **R9 — Connection-check script** (30 min)
      Copy `starter/check_db_connection.py` to `scripts/check_db_connection.py`
      and replace every `TODO:`.
      *Proof:* `python scripts/check_db_connection.py` prints a line starting
      with `OK` and exits 0; with the database stopped it prints `FAIL` and
      exits 1.

- [ ] **R10 — FastAPI health endpoint** (45 min)
      Create `project/backend/app/main.py` from `starter/health_app.py`.
      *Proof:* `make api` then
      `curl -s http://127.0.0.1:8000/health` returns
      `{"status":"ok","database":"up"}`.

- [ ] **R11 — Run the test** (20 min)
      `make test-week WEEK=week-00-orientation` until it passes, then
      `make lint`.

- [ ] **R12 — Repository map exercise** (15 min)
      Complete `exercises/03-repository-map.md`.

- [ ] **R13 — Reflect, record and commit** (20 min)
      Fill in `REFLECTION.md`, save portfolio evidence to
      `docs/portfolio/week-00/`, update the progress table in the root
      `README.md`, then commit on branch `week-00-orientation` using the message
      in README section 15 and claim the badge in `BADGE.md`.

## Optional (stretch)

- [ ] **O1 — Adminer and volume reset** — `exercises/04-adminer-and-reset.md`.
- [ ] **O2 — Break it on purpose** — change `POSTGRES_PORT` to `5433`, make the
      whole stack work again, then change it back. Record what you had to edit.

## Deliverables

| Deliverable | Path |
|-------------|------|
| Connection-check script | `scripts/check_db_connection.py` |
| Health endpoint | `project/backend/app/main.py` |
| Completed exercises | `curriculum/week-00-orientation/exercises/` |
| Notes and reflection | `curriculum/week-00-orientation/LEARNING_NOTES.md`, `REFLECTION.md` |
| Evidence | `docs/portfolio/week-00/environment-check.md` |
