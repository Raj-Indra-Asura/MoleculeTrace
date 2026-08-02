# Exercise 5 — Specialisation alternatives (Optional, stretch)

Not assumed by any later week. Do it if the user/role decision in
`docs/data-model.md` section 8 still feels arbitrary.

## Part A — Three designs, one domain

Model the user side of MoleculeTrace three ways. For each, give a Mermaid
fragment and fill in the table.

### D1 — `UserAccount` with a `role` attribute

TODO: Mermaid fragment.

### D2 — `UserAccount` M:N `Role`, with a `holds` relationship carrying
`granted_at` and `granted_by`

TODO: Mermaid fragment.

### D3 — Specialisation: `UserAccount` generalises `HumanAccount` and
`ServiceAccount`, plus roles as in D2

TODO: Mermaid fragment.

| Question | D1 | D2 | D3 |
|----------|----|----|----|
| Can one person hold two roles? | TODO | TODO | TODO |
| Can a role exist before anyone holds it? | TODO | TODO | TODO |
| Where does "who granted this permission, and when" live? | TODO | TODO | TODO |
| What does adding a new role cost? | TODO | TODO | TODO |
| How is a program account, which has no email, represented? | TODO | TODO | TODO |
| What does week 09 have to enforce? | TODO | TODO | TODO |
| What does the dashboard in week 22 have to query? | TODO | TODO | TODO |

## Part B — Constraints

For the specialisation in D3, state and justify:

| Constraint | Choice | Justification |
|------------|--------|---------------|
| Disjoint or overlapping | TODO | TODO |
| Total or partial | TODO | TODO |
| Attribute-defined or user-defined | TODO | TODO |

Then answer: what would have to be true of the domain for the specialisation to
become *overlapping*, and what would break?

## Part C — Generalisation in the other direction

`Prediction` and `ActivityObservation` both record "a number about a molecule,
with a unit, produced at a time, by some process".

1. Write the generalisation that would merge them into a superclass.
2. Give three reasons not to do it.
3. Give one circumstance in which you would.
4. Say which week would suffer most if you did it wrongly.

## Part D — The specialisation that is not worth it

Invent a specialisation of one of the sixteen concepts whose subclasses would
have identical attributes and identical relationships. Explain what should be
used instead, and why "we might need it later" is not a reason to specialise now.
