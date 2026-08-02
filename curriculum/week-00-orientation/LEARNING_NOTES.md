# Week 00 — Learning Notes

A beginner-level tour of how MoleculeTrace fits together, followed by space for
your own summary. Read section 1, then write sections 2–5 in your own words.

## 1. The architecture, explained simply

Four processes, one configuration file:

```
   .env  ──────────────┬───────────────┬──────────────────┐
                       │               │                  │
                       ▼               ▼                  ▼
              docker compose      Python code          pytest
                   │                   │                  │
                   ▼                   ▼                  ▼
        ┌───────────────────┐   ┌────────────┐     ┌────────────┐
        │ PostgreSQL 16     │◀──│  FastAPI   │◀────│ test client│
        │ container "db"    │   │  service   │     │  (httpx)   │
        │ port 5432 → host  │   │ port 8000  │     └────────────┘
        └───────────────────┘   └────────────┘
                   ▲                   ▲
                   │ psql              │ browser / curl / Streamlit
                   └───────────────────┘
```

**The database.** PostgreSQL runs inside a Docker container so that every
machine gets the identical version 16 without installing anything. Its data
lives in a named Docker volume (`pgdata`), which is why stopping the container
does not lose your tables. The container publishes port 5432 to your machine, so
tools on the host connect to `localhost:5432` as if PostgreSQL were installed
locally.

**The configuration.** `.env` (your private copy of `.env.example`) holds the
user, password, database name, host, port and the assembled `DATABASE_URL`.
Docker Compose reads it automatically; Python reads it via `python-dotenv`. One
source of truth means no credential ever appears in source code, and switching
ports or databases is a one-line edit.

**The application.** A FastAPI process (run by uvicorn) will grow over the
course into the service layer over the database, using psycopg to talk to
PostgreSQL. In week 00 it exposes only `GET /health`, which answers "am I
running?" and "can I reach the database?".

**The tests.** pytest is how the course proves work is done. Week tests live in
`curriculum/week-XX/tests/`; project tests live in `project/tests/`. Database
tests read `TEST_DATABASE_URL` and skip with a clear message when it is unset,
so the suite never fails just because the database is off.

**Why this shape?** Each layer can be checked on its own: `docker compose ps`
checks the container, `psql` checks the database, the connection script checks
Python-to-database, `/health` checks the service, and pytest checks all of it
without you typing anything. When something breaks in week 14, you debug in that
same order.

### Key terms

| Term | Meaning here | Where it appears in MoleculeTrace |
|------|--------------|-----------------------------------|
| Image | A read-only template for a container | `postgres:16` in `docker-compose.yml` |
| Container | A running instance of an image | `moleculetrace-db` |
| Volume | Storage that outlives the container | `pgdata` |
| Port mapping | `host:container` port forwarding | `"5432:5432"` |
| Healthcheck | Command Compose runs to test readiness | `pg_isready` |
| Environment variable | Named value read at run time | `DATABASE_URL` |
| Connection string | One URL holding user, password, host, port, database | `DATABASE_URL` in `.env.example` |
| ASGI server | Process that runs the FastAPI app | `uvicorn` |
| Health endpoint | Cheap route reporting service status | `GET /health` |

## 2. My baseline answers (section 3 of the README)

1. `docker compose up -d` vs `docker run`:
2. Environment variable vs command-line argument:
3. `git status` vs `git log`:

## 3. Core ideas in my words

1.
2.
3.

## 4. Worked example from this week

<Paste the command or code snippet that made the setup click — for example the
`SELECT version();` output or your `/health` response — and explain why it
works.>

## 5. Connections to earlier weeks

- None: this is week 00. Note here what you expect week 01 to build on.

## Open questions

-
