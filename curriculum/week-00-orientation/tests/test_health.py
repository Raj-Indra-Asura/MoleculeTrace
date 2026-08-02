"""Week 00 validation: the FastAPI health endpoint answers correctly.

Run with:  make test-week WEEK=week-00-orientation

The test loads project/backend/app/main.py the same way uvicorn does and calls
GET /health through FastAPI's test client, so it needs no running server. It
does not need a running database: the endpoint must report the database as
"down" instead of raising.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[3]
APP_PATH = REPO_ROOT / "project" / "backend" / "app" / "main.py"


def load_app():
    """Import project/backend/app/main.py and return its FastAPI instance."""
    if not APP_PATH.exists():
        pytest.fail(
            f"{APP_PATH.relative_to(REPO_ROOT)} does not exist. "
            "Copy curriculum/week-00-orientation/starter/health_app.py there "
            "and complete the TODOs (README section 7)."
        )

    spec = importlib.util.spec_from_file_location("week00_main", APP_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)

    app = getattr(module, "app", None)
    if app is None:
        pytest.fail("project/backend/app/main.py must define a FastAPI app named 'app'.")
    return app


def test_health_endpoint_reports_ok():
    fastapi_testclient = pytest.importorskip(
        "fastapi.testclient",
        reason="Install the development extras first: make install",
    )

    client = fastapi_testclient.TestClient(load_app())
    response = client.get("/health")

    assert response.status_code == 200, (
        f"GET /health returned {response.status_code}, expected 200."
    )

    payload = response.json()
    assert payload.get("status") == "ok", (
        f'GET /health returned {payload!r}; expected "status": "ok".'
    )
    assert payload.get("database") in {"up", "down"}, (
        f'GET /health returned {payload!r}; expected "database" to be "up" or "down". '
        "The endpoint must report the database state instead of raising."
    )
