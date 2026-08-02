# project/backend/

FastAPI service over the MoleculeTrace database, built in weeks 12–13.

Planned layout:

```
app/
  main.py        # FastAPI application factory and routes
  db.py          # psycopg connection handling and transaction boundaries
  schemas.py     # Pydantic request/response models
tests/           # API tests (httpx + pytest)
```

Run it with `make api` once week 13 is complete.

Rules: parameterised queries only, transaction boundaries owned by the service
layer, and no credentials in source — read them from `.env`.
