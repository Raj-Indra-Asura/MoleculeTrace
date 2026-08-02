# Week 00 — Orientation and Project Setup

**Phase:** 0. Foundations · **Required effort:** 5 hours ·
**Depends on:** none — this is the first week

**Topic scope:** Set up the toolchain, learn the repository's workflow, prove
that PostgreSQL, psql, Python, FastAPI and pytest all work on your machine, and
agree the working rhythm for the next 24 weeks.

> This week does **not** teach Python or Git from scratch. It assumes you can
> already write a small script and use `git add` / `git commit`. What it gives
> you is the project-specific commands, paths and workflow you will repeat every
> week.

## 1. Learning objectives

By the end of this week you can:

1. Navigate the repository and say what belongs in `curriculum/`, `project/`,
   `labs/`, `docs/`, `instructor/` and `scripts/`.
2. Start and stop the MoleculeTrace PostgreSQL container with Docker Compose and
   connect to it with `psql`.
3. Read configuration from `.env` in a Python script and open a database
   connection with psycopg without hard-coding credentials.
4. Run a FastAPI health endpoint locally and prove it works with one pytest
   test, then commit the week with the project's branch and commit conventions.

## 2. Connection to MoleculeTrace

MoleculeTrace models this chain:

```
molecules → biological targets → assays → activity observations
          → versioned datasets → ML experiments → model versions
          → predictions → validation
```

This week builds none of that chain yet. It builds the *rails* the chain runs
on: a reproducible database container, a configuration file, a service process
and a test command. Every later week starts by assuming these four things work.

**Visible improvement this week:** the repository gains a running database, a
`GET /health` endpoint that reports whether the database is reachable, and a
passing test that proves it.

## 3. Prerequisites

- Completed checkpoints for weeks: none.
- Installed and on your `PATH`: Git, Docker Desktop or Docker Engine with the
  Compose v2 plugin (`docker compose version`), and Python 3.11 or newer
  (`python --version`).
- A terminal you are comfortable in, and a text editor.

### Retrieval practice (15 minutes, required)

There is no earlier week to recall from, so this slot is a **baseline check**.
Answer from memory in `LEARNING_NOTES.md`, then verify with the commands given:

1. What does `docker compose up -d` do that `docker run` does not?
   (Verify: `docker compose --help`.)
2. What is the difference between an environment variable and a command-line
   argument? (Verify: `printenv | head`.)
3. What does `git status` show that `git log` does not?
   (Verify: run both in this repository.)

Anything you could not answer becomes a note in section "Open questions" of
`LEARNING_NOTES.md`.

## 4. Five-hour study plan

| Block | Time | Activity | Output |
|-------|------|----------|--------|
| 1 | 0:00–0:15 | Baseline retrieval practice (section 3) | Three written answers |
| 2 | 0:15–1:15 | Conceptual notes (section 5) and repository tour | Notes in `LEARNING_NOTES.md` |
| 3 | 1:15–2:45 | Guided work (section 6): `.env`, Compose, psql, connection script | Running database, `scripts/check_db_connection.py` |
| 4 | 2:45–4:15 | Independent work and exercises (sections 7–8) | `GET /health` endpoint, exercises 1–3 |
| 5 | 4:15–4:45 | Validation (section 9) | `make test-week WEEK=week-00-orientation` passes |
| 6 | 4:45–5:00 | Reflection and commit (sections 11–15) | Commit pushed, badge claimed |

## 5. Conceptual notes

### 5.1 Repository navigation

| Path | What you do there |
|------|-------------------|
| `curriculum/week-XX-*/` | Read the lesson, do the exercises, run the week's tests. |
| `project/` | The product you are building: `database/`, `backend/`, `frontend/`, `ml/`, `data/`, `tests/`. Work you want to keep lands here. |
| `scripts/` | Small helper scripts invoked by hand or by the `Makefile`. |
| `labs/` | Pointer files only — one markdown file per cross-cutting topic linking to the week that teaches it. |
| `docs/` | Design notes, decision records and `docs/portfolio/week-XX/` evidence. |
| `instructor/` | Rubrics and solution notes. Open **after** you have attempted the work. |

Two rules that matter from day one: a week's folder holds the *lesson*, and
`project/` holds the *artefact*. When a week tells you to copy a starter file
into `project/`, the copy in `project/` is the one that must keep working in
later weeks.

### 5.2 Git workflow for this course

One branch per week, one pull request per week:

```bash
git switch -c week-00-orientation
# ...do the work...
git add -A
git commit -m "chore(week-00): verify development environment"
git push -u origin week-00-orientation
```

Commit messages follow Conventional Commits — `<type>(week-XX): <imperative
summary>` — with types `feat`, `fix`, `docs`, `test`, `refactor`, `chore`,
`perf`. Full conventions live in [`CONTRIBUTING.md`](../../CONTRIBUTING.md).

Never commit `.env`. It is already listed in `.gitignore`; confirm with
`git check-ignore -v .env`.

### 5.3 Environment variables and `.env`

`.env.example` is the committed template; `.env` is your private copy. Both
Docker Compose and the Python code read the same variables, which is why the
database URL never appears in source:

| Variable | Used by | Meaning |
|----------|---------|---------|
| `POSTGRES_USER` / `POSTGRES_PASSWORD` / `POSTGRES_DB` | Compose, psycopg | Credentials and database name created inside the container |
| `POSTGRES_HOST` / `POSTGRES_PORT` | your machine | Where the container's port 5432 is published |
| `DATABASE_URL` | application code | One connection string assembled from the above |
| `TEST_DATABASE_URL` | pytest | A separate database so tests never touch working data |
| `API_HOST` / `API_PORT` | FastAPI / uvicorn | Where the service listens |

Compose substitutes `${VAR}` from `.env` automatically. Python does not: use
`python-dotenv` (`load_dotenv()`) or export the variables in your shell.

### 5.4 Docker Compose concepts

`docker-compose.yml` in the repository root describes the stack declaratively:

- **service** — one container definition (`db`, and an optional `adminer`).
- **image** — `postgres:16`, pulled from Docker Hub; you never install
  PostgreSQL on the host.
- **environment** — variables injected into the container; PostgreSQL's official
  image uses `POSTGRES_USER`, `POSTGRES_PASSWORD` and `POSTGRES_DB` to
  initialise itself the first time it starts.
- **ports** — `"${POSTGRES_PORT:-5432}:5432"` maps *host port : container port*.
  Only the left-hand number is yours to change.
- **volumes** — `pgdata` keeps the data files when the container is recreated.
  `./project/database/init` is mounted read-only and its SQL runs **only when
  the volume is empty**.
- **healthcheck** — `pg_isready` tells Compose when the database is actually
  accepting connections, not merely started.
- **profiles** — `adminer` sits behind the `tools` profile, so it starts only
  with `docker compose --profile tools up -d adminer`.

Lifecycle you will use all course:

| Command | Effect |
|---------|--------|
| `make up` | Start the database in the background |
| `make logs` | Follow the database logs (`Ctrl-C` to stop following) |
| `make psql` | Open a psql shell inside the container |
| `make down` | Stop the containers, **keep** the data volume |
| `make reset` | Stop the containers and **delete** the data volume |

### 5.5 The 24-week learning contract

- Five focused hours per week. Anything marked **Optional (stretch)** is never
  assumed by a later week.
- Week *N* may only assume weeks `00 … N-1`. Each week opens with retrieval
  practice, so a skipped week becomes visible immediately.
- A week is finished when its `CHECKPOINT.md` passes — not when you have read
  the material.
- Every week produces a visible improvement to the project and portfolio
  evidence in `docs/portfolio/week-XX/`.
- You self-assess against the rubric in section 16 and record the score, status
  and commit hash in the progress table in the root [`README.md`](../../README.md).
- Everything the project produces about molecules is a teaching artefact, not a
  scientific or medical claim; generated data is labelled synthetic.

## 6. Guided work (required)

Expected output is stated for every step. Run everything from the repository
root.

**1. Create your environment file.**

```bash
cp .env.example .env
```

Edit `POSTGRES_PASSWORD` to a value of your own. Then confirm Git ignores it:

```bash
git check-ignore -v .env
```

*Expected:* a line naming `.gitignore` and the `.env` rule. If the command
prints nothing, stop — your `.env` would be committed.

**2. Validate the Compose file before starting anything.**

```bash
docker compose config --quiet && echo "compose file OK"
```

*Expected:* `compose file OK`. This also proves your `.env` values substitute
correctly; unset variables show up here first.

**3. Start PostgreSQL.**

```bash
make up
docker compose ps
```

*Expected:* a `moleculetrace-db` row with state `running` and status
`healthy` (wait a few seconds and re-run if it still says `starting`).

**4. Connect with psql.**

```bash
make psql
```

*Expected:* a `moleculetrace=#` prompt. Inside it run:

```sql
SELECT version();
\conninfo
\l
\q
```

*Expected:* a `PostgreSQL 16.x ...` string, a line naming database
`moleculetrace` on port `5432`, a database list containing `moleculetrace`, then
you are back in your shell. Save the `SELECT version();` output — it is
portfolio evidence.

**5. Install the Python project.**

```bash
python -m venv .venv
source .venv/bin/activate        # Windows PowerShell: .venv\Scripts\Activate.ps1
make install
```

*Expected:* `Successfully installed moleculetrace-0.1.0` (plus dependencies).

**6. Write the connection-check script.**

Copy `starter/check_db_connection.py` to `scripts/check_db_connection.py` and
replace every `TODO:`. It must load `.env`, connect with psycopg using
`DATABASE_URL`, run `SELECT version();` and print one line starting with `OK`.

```bash
python scripts/check_db_connection.py
```

*Expected:* a single line, e.g.
`OK connected to moleculetrace on localhost:5432 — PostgreSQL 16.4 ...`.
On failure it must print a line starting with `FAIL` and exit with status 1 —
check with `echo $?`.

**7. Stop and restart to prove reproducibility.**

```bash
make down && make up && python scripts/check_db_connection.py
```

*Expected:* the same `OK` line. Data survives `make down`; it does not survive
`make reset`.

## 7. Independent work (required)

Give the project a health endpoint.

**Goal:** running `make api` serves `GET /health` on
`http://127.0.0.1:8000/health`, returning HTTP 200 and a JSON body with a
`status` field equal to `"ok"` and a `database` field equal to `"up"` when the
database answers and `"down"` when it does not. The endpoint must never raise an
unhandled exception when the database is stopped, and it must not contain any
credentials — read `DATABASE_URL` from the environment.

Start from `starter/health_app.py` and create `project/backend/app/main.py`.
`make api` runs `uvicorn app.main:app --app-dir project/backend`, so the module
path must be exactly that.

Prove it manually before you write the test:

```bash
make api            # in one terminal
curl -s http://127.0.0.1:8000/health   # in another
```

*Expected:* `{"status":"ok","database":"up"}` — compare with
`expected-outputs/health-response.json`.

## 8. Exercises

Files live in `exercises/`. Starter files with `TODO:` markers live in
`starter/`.

| # | File | Type | Required? |
|---|------|------|-----------|
| 1 | `exercises/01-compose-validation.md` | Docker Compose | Required |
| 2 | `exercises/02-psql-tour.sql` | SQL | Required |
| 3 | `exercises/03-repository-map.md` | Design | Required |
| 4 | `exercises/04-adminer-and-reset.md` | Docker | **Optional (stretch)** |

Optional exercises are never assumed by a later week.

## 9. Validation

```bash
make test-week WEEK=week-00-orientation
```

*Expected:* one test passes —
`tests/test_health.py::test_health_endpoint_reports_ok`. It fails with an
explicit message if `project/backend/app/main.py` is missing or if `/health`
does not return `status: "ok"`.

Additional manual checks, with exact expected results:

```bash
docker compose ps --format '{{.Name}} {{.State}}'   # moleculetrace-db running
python scripts/check_db_connection.py               # line starts with OK
curl -s -o /dev/null -w '%{http_code}\n' http://127.0.0.1:8000/health   # 200
make lint                                           # no errors on your files
```

Compare your outputs against `expected-outputs/`.

## 10. Common mistakes and troubleshooting

### 10.1 Ports

- **`bind: address already in use` on 5432** → another PostgreSQL (a system
  install or an older container) already owns the port. Find it with
  `sudo lsof -i :5432` (macOS/Linux) or
  `netstat -ano | findstr :5432` (Windows), then either stop it, or set
  `POSTGRES_PORT=5433` in `.env`, run `make down && make up`, and reconnect on
  the new port. `make psql` still works, because it runs *inside* the container.
- **`Address already in use` on 8000** → a previous `make api` is still running.
  Stop it with `Ctrl-C` in its terminal, or change `API_PORT` in `.env`.
- **Changed `POSTGRES_PORT` but the script still fails** → `DATABASE_URL` in
  `.env` is a literal string; update it too, and restart your shell or rerun the
  script so `load_dotenv()` picks it up.
- **Port 8080 clash** → only affects the optional `adminer` service; skip it.

### 10.2 Docker

- **`Cannot connect to the Docker daemon`** → Docker Desktop is not running, or
  on Linux your user is not in the `docker` group.
- **`docker compose` reported as unknown** → you have the old `docker-compose`
  v1 binary; install the Compose v2 plugin and verify with
  `docker compose version`.
- **Container status `unhealthy` or restarting** → read `make logs`. The usual
  cause is a leftover volume initialised with different credentials: run
  `make reset` (this deletes the data — safe in week 00) and `make up` again.
- **SQL in `project/database/init/` did not run** → it runs only when the volume
  is empty. Use `make reset` to force re-initialisation.
- **Connecting from another container** → the host is the service name `db`, not
  `localhost`. From your machine it is `localhost`.

### 10.3 Environment variables

- **`WARN[0000] The "POSTGRES_USER" variable is not set`** → you are not in the
  repository root, or `.env` does not exist. `cp .env.example .env`.
- **Python sees no variables while Compose does** → Compose reads `.env`
  automatically, Python does not. Call `load_dotenv()` before reading
  `os.environ`, or export the variables.
- **Password changed in `.env` but authentication still fails** → the password
  was baked into the volume on first start. `make reset && make up`.
- **`psycopg.OperationalError: connection failed` immediately after `make up`**
  → the container is still initialising. Wait for `healthy` in
  `docker compose ps`.
- **`.env` appears in `git status`** → do not commit it. Confirm the
  `.gitignore` rule with `git check-ignore -v .env`.

## 11. Reflection questions

Answer in `REFLECTION.md`:

1. Why does the project keep credentials in `.env` and read them at runtime
   instead of writing the connection string in `main.py`?
2. What is the practical difference between `make down` and `make reset`, and
   when would choosing wrongly cost you work?
3. Which single step of this week's setup is most likely to break on a different
   machine, and what would you document to prevent it?

## 12. Completion checklist

- [ ] Baseline retrieval practice answered before consulting notes.
- [ ] Conceptual notes summarised in `LEARNING_NOTES.md`.
- [ ] Guided work completed: `.env`, Compose validated, database running, psql
      connection made, `scripts/check_db_connection.py` prints `OK`.
- [ ] Independent work completed: `GET /health` served by
      `project/backend/app/main.py`.
- [ ] All required exercises done.
- [ ] `make test-week WEEK=week-00-orientation` passes.
- [ ] Outputs match `expected-outputs/`.
- [ ] `REFLECTION.md` completed.
- [ ] Portfolio evidence saved (section 14).
- [ ] Work committed and the progress table in the root `README.md` updated.
- [ ] Week 0 badge claimed — see [`BADGE.md`](BADGE.md).

## 13. Syllabus mapping

| Syllabus topic | Covered by |
|----------------|-----------|
| Database systems vs. file systems; DBMS architecture | sections 5.4, 6 |
| Client/server architecture and connection handling | sections 5.4, 6, 7 |
| Course tooling and reproducible environments | sections 5.1–5.3, 6 |

See [`SYLLABUS_MAPPING.md`](../../SYLLABUS_MAPPING.md).

## 14. Portfolio evidence

Save to `docs/portfolio/week-00/`:

- `environment-check.md` — the output of `docker compose ps`,
  `SELECT version();`, `python scripts/check_db_connection.py` and
  `curl http://127.0.0.1:8000/health`.
- A one-paragraph write-up describing the local stack (database container,
  configuration, API process, test command) in terms a reader unfamiliar with
  the repository would understand.

## 15. Suggested Git commit

```bash
git add -A
git commit -m "chore(week-00): verify development environment and add health endpoint"
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
