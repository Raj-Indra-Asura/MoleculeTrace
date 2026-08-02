# project/tests/

pytest suites for the project code (schema, backend, ML pipeline), as opposed to
the per-week validation in `curriculum/week-XX/tests/`.

```bash
make test
```

Database tests read `TEST_DATABASE_URL` from `.env` and must skip with a clear
message when it is unset. Tests never write to the development database.
