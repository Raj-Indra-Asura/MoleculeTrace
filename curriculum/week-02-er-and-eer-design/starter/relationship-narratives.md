# Starter — Relationship narratives

Copy this into `docs/data-model.md` section 9. **Every** relationship in the
improved EER model needs an entry. A diagram nobody can read aloud is not a
design; this section is where you prove you understand your own model.

## Rules

1. Plain language only. Banned words: *foreign key*, *join*, *table*, *column*,
   *many-to-many*, *cardinality*, *nullable*.
2. One sentence per direction, both in the present tense.
3. One sentence saying **why the relationship exists** — the question it lets
   someone answer.
4. One sentence saying **what is forbidden** by its participation constraints.
5. No hedges: *maybe*, *usually*, *typically*, *some*, *should normally*.

## Template, repeated per relationship

### R-NN — <verb phrase> (<left entity> ↔ <right entity>)

- **Left to right:** TODO: "One assay produces many activity observations."
- **Right to left:** TODO: "Each activity observation was produced by exactly
  one assay."
- **Why it exists:** TODO: the question this lets a scientist answer.
- **What it forbids:** TODO: the situation the participation constraints make
  impossible.
- **Serves requirement:** TODO: an `FR-`/`NFR-` ID from
  `docs/02_requirements.md`, or `none` with a reason.

## Self-test

Give someone only this section — no diagram — and ask them to draw the model.
Every entity set they invent, merge or miss is an ambiguous sentence you must
repair. Record what they got wrong in `REFLECTION.md`.
