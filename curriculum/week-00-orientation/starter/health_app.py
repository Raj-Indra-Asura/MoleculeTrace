# Starter: minimal FastAPI application for MoleculeTrace.
#
# Copy this file to project/backend/app/main.py and replace every TODO.
# "make api" runs: uvicorn app.main:app --app-dir project/backend
# so the module path and the variable name "app" must not change.
#
# Required behaviour of GET /health:
#   200 {"status": "ok", "database": "up"}    when the database answers
#   200 {"status": "ok", "database": "down"}  when it does not
# It must never raise, and must never contain credentials.

from __future__ import annotations

import os

from fastapi import FastAPI

app = FastAPI(title="MoleculeTrace API", version="0.1.0")


def database_is_reachable() -> bool:
    """Return True when a trivial query succeeds against DATABASE_URL."""
    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        return False
    try:
        # TODO: connect with psycopg using database_url and execute "SELECT 1;".
        #       Return True only when the query returns 1.
        return False
    except Exception:  # noqa: BLE001 - health must never raise
        return False


@app.get("/health")
def health() -> dict[str, str]:
    # TODO: return the status payload described above, using
    #       database_is_reachable() to fill the "database" field.
    return {"status": "TODO", "database": "TODO"}
