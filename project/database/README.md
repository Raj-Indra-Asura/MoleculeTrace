# project/database/

| Folder | Purpose |
|--------|---------|
| `init/` | SQL executed once by the PostgreSQL container on first start (mounted read-only by `docker-compose.yml`). Keep it to extensions, roles and schemas. |
| `migrations/` | Numbered, forward-only schema changes: `NNN_description.sql`. One migration per curriculum week that changes the schema. |
| `seeds/` | Reference data and clearly labelled synthetic sample data. |
| `queries/` | Saved analytical queries, one file per named query, with a header comment stating its purpose and the week it came from. |

Conventions: `snake_case` identifiers, singular column names, surrogate keys
named `<table>_id`, and a `COMMENT ON` for every table and column.
