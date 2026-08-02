# Starter — Cardinality table

Copy this table into `docs/data-model.md` section 5 and fill it in. One row per
relationship in your **improved EER model** — no more, no fewer.

Rules the validation applies:

- The cardinality cell is exactly one of `1:1`, `1:N`, `M:N`.
- At least one `1:1`, at least six `1:N` and at least two `M:N` rows.
- The *domain rule* cell states a fact about the world, not about your data
  files, and not "for simplicity".
- Both reading sentences are present, in plain language.
- No cell is blank.

| Relationship | Left entity | Right entity | Cardinality | Domain rule that forces it | Reading (left → right) | Reading (right → left) |
|--------------|-------------|--------------|-------------|----------------------------|------------------------|------------------------|
| TODO: verb phrase | TODO | TODO | TODO: 1:1 / 1:N / M:N | TODO: why the world works this way | TODO: "One X …" | TODO: "Each Y …" |

Relationships you must account for somewhere in the table (name them as you
like, and add any others your model needs):

- a molecule and its synonyms;
- a molecule, a descriptor type and the descriptor value;
- a biological target and its assays;
- an assay and its activity observations;
- a molecule and its activity observations;
- a dataset and its versions;
- a dataset version and the molecules (or observations) it contains;
- a dataset version and the experiments that use it;
- an experiment and the model versions it produces;
- a model version and its predictions;
- a molecule and the predictions made about it;
- a prediction and its validation;
- a user account and the roles it holds;
- a user account and the audit-log entries it caused.

## Checks before you commit

1. Read each row's two sentences aloud. If either needs a hedge word, fix the
   model, not the sentence.
2. For every `1:1` row, answer in one line: why are these two entity sets rather
   than one?
3. For every `M:N` row, answer in one line: does the pairing carry facts of its
   own? If yes, it must appear as an associative entity in the diagram.
4. For every `1:N` row, answer in one line: what stops it becoming `M:N` next
   year?
