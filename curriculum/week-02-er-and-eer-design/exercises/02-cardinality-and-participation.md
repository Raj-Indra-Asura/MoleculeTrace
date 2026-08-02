# Exercise 2 — Cardinality and participation (Required)

Ten statements about the MoleculeTrace domain. For each: give the cardinality,
give the participation of both sides, and name the rule in the world that forces
your answer. Then say what changes if the statement is relaxed.

Cardinality is one of `1:1`, `1:N`, `M:N`. Participation is `total` or
`partial` — never blank.

| # | Statement | Cardinality | Left participation | Right participation | Domain rule | What changes if relaxed |
|---|-----------|-------------|--------------------|---------------------|-------------|-------------------------|
| 1 | A biological target is measured by assays. | TODO | TODO | TODO | TODO | TODO |
| 2 | An assay produces activity observations. | TODO | TODO | TODO | TODO | TODO |
| 3 | A molecule has activity observations. | TODO | TODO | TODO | TODO | TODO |
| 4 | A dataset has versions. | TODO | TODO | TODO | TODO | TODO |
| 5 | A dataset version is used by experiments. | TODO | TODO | TODO | TODO | TODO |
| 6 | An experiment produces model versions. | TODO | TODO | TODO | TODO | TODO |
| 7 | A model version makes predictions about molecules. | TODO | TODO | TODO | TODO | TODO |
| 8 | A prediction is validated. | TODO | TODO | TODO | TODO | TODO |
| 9 | A user account holds roles. | TODO | TODO | TODO | TODO | TODO |
| 10 | A user account causes audit-log entries. | TODO | TODO | TODO | TODO | TODO |

## Part B — The four combinations

Cardinality and participation are independent. Give one MoleculeTrace example of
each combination below, and one sentence saying what it forbids.

| Combination | Example | What it forbids |
|-------------|---------|-----------------|
| 1:N, total on the many side | TODO | TODO |
| 1:N, partial on the many side | TODO | TODO |
| 1:1, total on one side and partial on the other | TODO | TODO |
| M:N, partial on both sides | TODO | TODO |

Then answer: is `M:N` with **total participation on both sides** loadable? Say
what would have to happen at insert time, and what it means for week 11.

## Part C — Cardinality that is only true today

Three statements that look like rules but may be sampling accidents. For each,
say whether it is a genuine domain rule or an accident of the current data, and
what evidence would settle it.

1. "Every molecule in our registry has exactly one supplier code."
2. "Every experiment in our registry produced exactly one model version."
3. "Every validated prediction was validated exactly once."

| # | Rule or accident? | Evidence that would settle it | Safer cardinality |
|---|-------------------|-------------------------------|-------------------|
| 1 | TODO | TODO | TODO |
| 2 | TODO | TODO | TODO |
| 3 | TODO | TODO | TODO |

## Part D — Reflection (three sentences maximum)

Which participation cell did you change after writing the "what it forbids"
sentence, and why did writing the sentence change your mind?
