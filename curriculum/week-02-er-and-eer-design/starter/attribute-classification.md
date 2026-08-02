# Starter — Attribute classification

Copy this table into `docs/data-model.md` section 3 and fill it in. At least
twenty attributes across the model, including at least two composite, at least
two multivalued and at least two derived.

Labels: `simple`, `composite`, `multivalued`, `derived`, `key`.

| Entity or relationship | Attribute | Kind | Why this label | Treatment in the improved model |
|------------------------|-----------|------|----------------|----------------------------------|
| TODO: Molecule | TODO: canonical_smiles | TODO | TODO | TODO |

The *treatment* column is where the marks are:

- **composite** → say whether the parts are separately queried, and therefore
  whether the attribute splits in week 03 or stays whole.
- **multivalued** → name the entity set or relationship set it becomes. A
  multivalued attribute may not survive into the improved model.
- **derived** → name the data it is computed from, and who recomputes it (a
  query in week 07, a view in week 10, or nobody — in which case delete it).
- **key** → say whether it is a natural key of the domain, and whether it is
  unique globally or only within an owner (a partial key).

## Prompts, so that you do not only list the easy ones

Consider at least these, and decide for yourself which apply:

- a user's name, contact details and account status;
- a molecule's canonical structure, registration date, and how many activity
  observations it has;
- the names a molecule is known by across suppliers and papers;
- a descriptor type's name, unit and computation software version;
- an assay's protocol details: method, readout, temperature, units;
- an activity observation's value, unit, quality flag and measurement date;
- a dataset's title, purpose and how many versions it has;
- a dataset version's number, creation timestamp, row count and checksum;
- an experiment's algorithm, hyperparameters and random seed;
- a model version's metrics, artefact location and whether it is the current
  one;
- a prediction's value, confidence and generation timestamp;
- an audit-log entry's actor, action, target and timestamp.

## Checks before you commit

- [ ] At least twenty rows.
- [ ] At least two composite, two multivalued and two derived attributes.
- [ ] Every multivalued attribute has a named destination entity or relationship
      set.
- [ ] Every derived attribute names its source data and its recomputer.
- [ ] No attribute appears under two different entities with the same meaning.
