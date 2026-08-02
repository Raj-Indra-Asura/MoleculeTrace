# tests/

Automated validation for this week, run with:

```bash
make test-week WEEK=week-22-query-optimization-and-dashboard
```

Tests check the state your work should produce — tables, constraints, query
results, API responses, artefact files — not the exact text of your SQL. They
are allowed to be strict about correctness and lenient about style.

Tests requiring a database read `TEST_DATABASE_URL` from `.env` and skip with a
clear message when it is unset.
