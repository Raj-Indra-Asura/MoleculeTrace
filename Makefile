# MoleculeTrace developer tasks.
# Every target here has been run against the stack described in README.md.

SHELL := /bin/bash
COMPOSE ?= docker compose
PYTHON ?= python

-include .env
export

.DEFAULT_GOAL := help

.PHONY: help
help: ## Show this help
	@grep -hE '^[a-zA-Z_-]+:.*?## ' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-14s\033[0m %s\n", $$1, $$2}'

.PHONY: up
up: ## Start PostgreSQL with Docker Compose
	$(COMPOSE) up -d db

.PHONY: down
down: ## Stop the containers (keeps the volume)
	$(COMPOSE) down

.PHONY: reset
reset: ## Stop the containers and delete the database volume
	$(COMPOSE) down -v

.PHONY: logs
logs: ## Follow database logs
	$(COMPOSE) logs -f db

.PHONY: psql
psql: ## Open a psql shell inside the database container
	$(COMPOSE) exec db psql -U $(POSTGRES_USER) -d $(POSTGRES_DB)

.PHONY: install
install: ## Install the Python project with development extras
	$(PYTHON) -m pip install -e ".[dev]"

.PHONY: test
test: ## Run the project test suite
	$(PYTHON) -m pytest project/tests

.PHONY: test-week
test-week: ## Run one week's validation: make test-week WEEK=week-05-sql-fundamentals
	@test -n "$(WEEK)" || { echo "Set WEEK=week-XX-slug"; exit 1; }
	$(PYTHON) -m pytest curriculum/$(WEEK)/tests

.PHONY: lint
lint: ## Lint Python sources
	$(PYTHON) -m ruff check .

.PHONY: format
format: ## Format Python sources
	$(PYTHON) -m ruff format .

.PHONY: api
api: ## Run the FastAPI service with reload
	$(PYTHON) -m uvicorn app.main:app --reload --app-dir project/backend --host $(API_HOST) --port $(API_PORT)

.PHONY: dashboard
dashboard: ## Run the Streamlit dashboard
	$(PYTHON) -m streamlit run project/frontend/app.py --server.port $(STREAMLIT_PORT)
