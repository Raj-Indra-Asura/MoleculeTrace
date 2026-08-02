---
name: Weekly problem
about: Report a problem with a curriculum week (unclear instructions, failing validation, broken command)
title: "[week-XX] <short summary>"
labels: ["curriculum"]
---

## Week

Folder: `curriculum/week-XX-<slug>/`
Section: (study plan / guided work / independent work / exercise / validation / rubric)

## What I was trying to do

<!-- One or two sentences. -->

## Command I ran

```bash
# exact command
```

## Output I got

```text
# full output, not a screenshot
```

## Output I expected

<!-- Quote the expected output file or the README instruction you were following. -->

## Environment

- OS:
- Python version (`python --version`):
- PostgreSQL version (`make psql` then `SELECT version();`):
- Docker Compose version (`docker compose version`):

## Checks

- [ ] I completed the previous week's `CHECKPOINT.md`.
- [ ] I copied `.env.example` to `.env` and filled it in.
- [ ] The database container is healthy (`docker compose ps`).
- [ ] I searched existing issues.
