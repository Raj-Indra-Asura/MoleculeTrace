# Exercise 01 — Compose file validation (Required)

**Goal:** be able to read a Compose file and prove it is valid before starting
anything.

## Part A — read the real file

Open the root `docker-compose.yml` and answer here:

1. Which host port reaches the database, and which variable controls it?

2. What exactly does the `pgdata` volume protect you from losing?

3. When does the SQL in `project/database/init/` run, and what command forces it
   to run again?

4. Why is `adminer` not started by `make up`?

## Part B — validate

Run and paste the output:

```bash
docker compose config --quiet && echo "compose file OK"
```

```
<paste here>
```

Now temporarily rename your `.env` (`mv .env .env.bak`), re-run the command,
paste what changes, then restore it (`mv .env.bak .env`).

```
<paste here>
```

5. What did the change in output tell you about where the values come from?

## Part C — complete the minimal file

Replace every `TODO:` in `starter/docker-compose.check.yml`, then validate:

```bash
docker compose -f curriculum/week-00-orientation/starter/docker-compose.check.yml config --quiet && echo OK
```

Paste your finished `services:` block here:

```yaml
<paste here>
```

Compare the rendered output with
`expected-outputs/compose-config.txt`.

**Required output:** answers to questions 1–5, both validation commands printing
`OK`, and the completed YAML.
