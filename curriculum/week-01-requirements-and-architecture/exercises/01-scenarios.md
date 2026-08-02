# Exercise 1 — Scenarios (Required)

Eight situations. For each, answer the three questions in the table underneath
it. Keep answers to one or two sentences; cite requirement IDs from
`docs/02_requirements.md` where they apply. Add the requirement if it does not
exist yet — that is the point of the exercise.

Answer format for every scenario:

| Question | Your answer |
|----------|-------------|
| Which layer must enforce this (data / application / ML / presentation)? | |
| Which requirement ID covers it, and does it exist yet? | |
| What breaks if the file-based approach is used instead? | |

---

## S1 — The duplicate molecule

A collaborator submits 5 000 compounds. Six hundred of them are already in the
registry under a different supplier code, and eleven of them appear twice inside
the submission itself with slightly different SMILES strings for the same
structure.

## S2 — The half-finished dataset

A data scientist builds dataset version 7: one row in `datasets`, then 40 000
membership rows. The laptop running the loader loses power after 12 000 rows.
The next morning someone trains a model on dataset version 7.

## S3 — The two loaders

Two ETL jobs start within a second of each other, both computing RDKit
descriptors for the same batch of molecules, both writing results.

## S4 — The disappearing target

A curator deletes a biological target that turned out to be a typo. Three
thousand activity observations referenced it, and two published datasets were
filtered on it.

## S5 — The impatient scientist

The dashboard's "compounds active against target X" panel takes 40 seconds once
the registry passes 100 000 molecules. The scientist starts keeping a private
spreadsheet copy instead.

## S6 — The unreproducible model

A model version reports an AUC of 0.91. Two months later nobody can reproduce
it: the dataset it used has been "updated", and the train/test split was
randomised at run time.

## S7 — The curious analyst

A new analyst is given the production `DATABASE_URL` "just to look at the data"
and runs an `UPDATE` without a `WHERE` clause in a session they thought was a
copy.

## S8 — The clinical question

A stakeholder asks whether the dashboard can rank compounds for a patient
population and export the ranking as a treatment recommendation.

For S8 also answer: which non-goal does this violate, and what exactly do you
say in reply?

---

## Wrap-up

1. Which scenario forced a requirement you had not written? Add it now and note
   its ID here.
2. Which two scenarios are solved by the *same* mechanism? Name the mechanism.
3. Which scenario is not solvable by the database alone? Explain who else must
   act.
