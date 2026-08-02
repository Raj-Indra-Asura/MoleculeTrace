# Week 00 — Resources

Official documentation first. Add a link only after you have used it.

## Required reading

- Docker Compose — how Compose works and the file reference:
  https://docs.docker.com/compose/intro/compose-application-model/ and
  https://docs.docker.com/reference/compose-file/
- Docker Compose — environment variables and `.env` files:
  https://docs.docker.com/compose/how-tos/environment-variables/variable-interpolation/
- PostgreSQL official Docker image (the `POSTGRES_*` variables and the
  `docker-entrypoint-initdb.d` rule): https://hub.docker.com/_/postgres
- PostgreSQL 16 — `psql` reference, including `\conninfo`, `\l`, `\dt`, `\q`:
  https://www.postgresql.org/docs/16/app-psql.html
- psycopg 3 — basic module usage (`connect`, cursors, context managers):
  https://www.psycopg.org/psycopg3/docs/basic/usage.html
- FastAPI — first steps: https://fastapi.tiangolo.com/tutorial/first-steps/
- pytest — how to invoke pytest and read its output:
  https://docs.pytest.org/en/stable/how-to/usage.html

## Reference

- PostgreSQL 16 documentation: https://www.postgresql.org/docs/16/
- PostgreSQL SQL commands: https://www.postgresql.org/docs/16/sql-commands.html
- PostgreSQL connection strings (URI format):
  https://www.postgresql.org/docs/16/libpq-connect.html#LIBPQ-CONNSTRING
- `pg_isready`: https://www.postgresql.org/docs/16/app-pg-isready.html
- psycopg 3 documentation: https://www.psycopg.org/psycopg3/docs/
- FastAPI documentation: https://fastapi.tiangolo.com/
- Uvicorn deployment and CLI options: https://www.uvicorn.org/
- Pydantic documentation: https://docs.pydantic.dev/latest/
- python-dotenv: https://saurabh-kumar.com/python-dotenv/
- pytest documentation: https://docs.pytest.org/en/stable/
- Docker Compose CLI reference: https://docs.docker.com/reference/cli/docker/compose/
- Git reference: https://git-scm.com/docs
- Conventional Commits: https://www.conventionalcommits.org/en/v1.0.0/
- Ruff rules: https://docs.astral.sh/ruff/rules/

## In this repository

- [`README.md`](../../README.md) — layout and progress table.
- [`ROADMAP.md`](../../ROADMAP.md) — the 24-week contract and dependency rule.
- [`CONTRIBUTING.md`](../../CONTRIBUTING.md) — branch, commit and PR conventions.
- [`SYLLABUS_MAPPING.md`](../../SYLLABUS_MAPPING.md) — syllabus topic → week.

## Optional depth

- Docker Compose profiles:
  https://docs.docker.com/compose/how-tos/profiles/
- PostgreSQL server configuration:
  https://www.postgresql.org/docs/16/runtime-config.html
