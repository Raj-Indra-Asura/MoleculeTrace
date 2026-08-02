# Starter — Participation-constraint table

Copy this table into `docs/data-model.md` section 6 and fill it in. One row per
relationship, matching the rows of the cardinality table exactly.

Rules the validation applies:

- Participation cells contain exactly `total` or `partial` — never blank, never
  "n/a", never "depends".
- **Both** sides are stated for every relationship.
- The *forbids* cell states, in one sentence, what a total participation makes
  impossible. Where both sides are partial, write what the model therefore
  allows, and confirm that you meant to allow it.

| Relationship | Left entity | Left participation | Right entity | Right participation | What this forbids (or deliberately allows) |
|--------------|-------------|--------------------|--------------|---------------------|--------------------------------------------|
| TODO: verb phrase | TODO | TODO: total / partial | TODO | TODO: total / partial | TODO: one sentence |

## How to decide a cell

Ask the question in this exact form, for each side separately:

> *Can a `<entity>` exist that takes part in no `<relationship>` at all?*

- **Yes** → partial.
- **No** → total.

Then write the consequence:

- Total on the many side of an identifying relationship means the weak entity
  cannot exist without its owner. Say it that way.
- Partial on the one side usually means "not yet" — a molecule with no
  observations, a dataset with no versions, a prediction with no validation.
  Confirm that "not yet" is genuinely acceptable rather than an oversight.

## Traps this table exists to catch

1. Marking a side total because it is *usually* true. Usually is partial.
2. Marking both sides total on an optional relationship, which makes the data
   impossible to load in any order.
3. Forgetting that participation is separate from cardinality: `1:N` says how
   many, participation says whether zero is allowed.
4. Stating participation for the interesting side only.

## Checks before you commit

- [ ] Every relationship in the cardinality table has exactly one row here.
- [ ] No blank cells.
- [ ] Each `total` cell names something that becomes a `NOT NULL` or a
      referential action in week 03 or week 09.
- [ ] Each `partial` cell names a real situation in which zero is correct.
