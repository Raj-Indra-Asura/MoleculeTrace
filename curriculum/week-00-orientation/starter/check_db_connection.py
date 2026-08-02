# Starter: PostgreSQL connection check for MoleculeTrace.
#
# Copy this file to scripts/check_db_connection.py and replace every TODO.
# It must read credentials from .env only — never hard-code them.
#
# Success: prints one line starting with "OK" and exits 0.
# Failure: prints one line starting with "FAIL" and exits 1.

from __future__ import annotations

import os
import sys


def main() -> int:
    # TODO: load the .env file so os.environ contains the POSTGRES_* values.
    #       Hint: from dotenv import load_dotenv

    database_url = os.environ.get("DATABASE_URL")
    if not database_url:
        print("FAIL DATABASE_URL is not set — copy .env.example to .env")
        return 1

    host = os.environ.get("POSTGRES_HOST", "localhost")
    port = os.environ.get("POSTGRES_PORT", "5432")
    database = os.environ.get("POSTGRES_DB", "moleculetrace")

    try:
        # TODO: open a connection with psycopg using database_url,
        #       run "SELECT version();" and read the single value returned.
        #       Hint: import psycopg; with psycopg.connect(...) as conn: ...
        version = "TODO"
    except Exception as exc:  # noqa: BLE001 - the script reports any failure
        print(f"FAIL cannot connect to {database} on {host}:{port} — {exc}")
        return 1

    print(f"OK connected to {database} on {host}:{port} — {version}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
