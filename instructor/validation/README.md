# Validation notes

How to confirm a week is genuinely complete.

For each week, record:

1. The exact commands run (`make test-week WEEK=week-XX-<slug>`, plus any manual
   check).
2. The expected result of each command.
3. Known-good failure modes and what they usually mean.
4. Anything the automated tests deliberately do not check, and how to inspect it
   by hand.

File naming: `week-XX.md`. Notes are added as each week is authored.

Validation must be reproducible from a clean clone: `make reset && make up`
followed by replaying the migrations for weeks 01…XX.
