# Exercise 04 — Adminer and volume reset (Optional, stretch)

Never assumed by a later week.

## Part A — a browser client

```bash
docker compose --profile tools up -d adminer
```

Open http://localhost:8080 and log in with system *PostgreSQL*, server `db`,
and the user, password and database from your `.env`.

1. Why is the server `db` and not `localhost` here?

2. Stop it again with `docker compose --profile tools down`. What happened to
   the database container?

## Part B — the destructive command

With the database running:

```bash
docker compose exec db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" \
  -c "CREATE TABLE scratch_note (id int);"
make down && make up
docker compose exec db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "\dt"
```

3. Is `scratch_note` still there? Why?

```bash
make reset && make up
docker compose exec db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "\dt"
```

4. Is it there now? Which command destroyed it, and what else did it destroy?

5. Write the one-sentence rule you will follow before ever running `make reset`
   again after week 03.
