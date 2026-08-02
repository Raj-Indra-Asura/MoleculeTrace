# Starter — Design-decision log

Copy this into `docs/data-model.md` section 10. At least eight decisions,
`DD-01` upward, numbered consecutively and never renumbered once committed —
later weeks cite them by ID exactly as they cite `FR-` identifiers.

| ID | Decision | Alternatives considered | Reason | Consequence for a later week | Requirement |
|----|----------|-------------------------|--------|------------------------------|-------------|
| DD-01 | TODO: what you decided | TODO: what you rejected | TODO: why | TODO: which week is affected and how | TODO: `FR-`/`NFR-` ID or `none` |

## Decisions you must record (at minimum)

1. Which of the sixteen concepts are entity sets, and which are relationship
   sets, associative entities or attributes.
2. How the molecule/descriptor-type pairing is modelled, and where the value
   lives.
3. Whether `ActivityObservation` is a strong entity with a compound key or a
   weak entity, and why.
4. Why `DatasetVersion` is weak, and what a global version identifier would
   cost.
5. How dataset membership is recorded, and whether it is molecules or activity
   observations that belong to a version.
6. The user/role decision: specialisation, an M:N `holds` relationship, or both.
7. Every redundant attribute or relationship you removed, and the fact you
   checked could not be lost.
8. Every derived attribute you kept as derived, and who recomputes it.
9. One decision you reversed between the initial ER model and the improved EER
   model — with the reason it changed.

## What a weak entry looks like

> DD-03 — Made `MoleculeSynonym` an entity. Alternatives: none. Reason: it is
> better. Consequence: none.

No alternative, no reason, no consequence. It scores zero.

## What a strong entry looks like

Name a real alternative that a competent designer would have chosen, state the
fact that decided against it, and name the week that will feel the effect. If
you cannot name a rejected alternative, you have not made a decision — you have
made an assumption, and it belongs in the assumptions list instead.
