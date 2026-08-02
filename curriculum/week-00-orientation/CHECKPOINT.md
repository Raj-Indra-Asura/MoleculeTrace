# Week 00 — Checkpoint

A week counts as complete only when every item below is true. Later weeks assume
this checkpoint has passed. Run every command from the repository root with the
virtual environment activated.

## Automated

```bash
make test-week WEEK=week-00-orientation
```

Expected tail of the output: `1 passed`.

```bash
make lint
```

Expected: `All checks passed!` (or no errors on the files you changed).

- [ ] The week test passes.
- [ ] `make lint` reports no errors on files you changed.

## Manual

Each command with its exact expected result:

```bash
docker compose config --quiet && echo OK
```
- [ ] Prints `OK` — the Compose file and your `.env` substitute cleanly.

```bash
docker compose -f curriculum/week-00-orientation/starter/docker-compose.check.yml config --quiet && echo OK
```
- [ ] Prints `OK` — your Compose validation exercise is syntactically valid.

```bash
docker compose ps --format '{{.Name}} {{.State}}'
```
- [ ] Prints `moleculetrace-db running`.

```bash
docker compose exec db pg_isready -U "$POSTGRES_USER" -d "$POSTGRES_DB"
```
- [ ] Ends with `accepting connections`.

```bash
docker compose exec db psql -U "$POSTGRES_USER" -d "$POSTGRES_DB" -Atc "SELECT current_database();"
```
- [ ] Prints `moleculetrace`.

```bash
python scripts/check_db_connection.py; echo "exit=$?"
```
- [ ] First line starts with `OK` and the last line is `exit=0`.

```bash
curl -s -o /tmp/health.json -w '%{http_code}\n' http://127.0.0.1:8000/health; cat /tmp/health.json
```
(with `make api` running in another terminal)
- [ ] Prints `200` then `{"status":"ok","database":"up"}`.

```bash
git check-ignore -v .env
```
- [ ] Prints a `.gitignore` rule — `.env` is not tracked.

```bash
git log --oneline -1
```
- [ ] Shows your week-00 commit, message formatted `chore(week-00): ...`.

- [ ] Outputs match the files in `expected-outputs/`.

## Artefacts

- [ ] Required exercises committed (`exercises/01`–`03`).
- [ ] `scripts/check_db_connection.py` and `project/backend/app/main.py`
      committed, with no credentials in either file.
- [ ] `LEARNING_NOTES.md` and `REFLECTION.md` filled in.
- [ ] Portfolio evidence saved to `docs/portfolio/week-00/`.
- [ ] Progress table in the root `README.md` updated with status, rubric score
      and commit hash.
- [ ] Week 0 badge criteria in [`BADGE.md`](BADGE.md) all met.

## Self-assessed rubric score

| Criterion | Weight | Score (0–2) |
|-----------|--------|-------------|
| Correctness of required exercises | 3 | |
| Depth of conceptual understanding | 2 | |
| Quality of the project improvement | 2 | |
| Validation and evidence | 2 | |
| Git hygiene and documentation | 1 | |

**Total: __ / 10** (pass mark 7)
