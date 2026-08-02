# Week 02 — Solution notes (instructor only)

**Students: read this only after submitting your own `docs/data-model.md`.**

This file holds the reference description of the MoleculeTrace conceptual model.
It is deliberately written as *prose and tables*, not as a finished diagram file,
so that it cannot be pasted into a student deliverable — and it is deliberately
kept out of `curriculum/week-02-er-and-eer-design/`, where the week's rule is
that no polished ER or EER diagram may appear.

A student answer that differs from this reference is not automatically wrong.
Section 6 lists the alternatives that earn full marks.

---

## 1. Reference model — entity sets

| Entity set | Kind | Identity | Notable attributes |
|------------|------|----------|--------------------|
| `UserAccount` | Strong | `username` (natural, unique) | `full_name` (**composite**: given, family), `email` (absent for service accounts), `status`, `created_at` |
| `Role` | Strong | `role_name` | `description`, `permission_summary` |
| `Molecule` | Strong | `canonical_smiles` (natural key) | `inchi_key`, `registered_at`, *`activity_count`* (**derived**) |
| `MoleculeSynonym` | Weak-ish (see §3) | (`molecule`, `synonym_text`) | `source`, `synonym_type` |
| `DescriptorType` | Strong | `descriptor_name` | `unit`, `software_version`, `description` |
| `MoleculeDescriptor` | Associative | (`molecule`, `descriptor_type`, `software_version`) | `value`, `computed_at` |
| `BiologicalTarget` | Strong | `target_code` | `target_name`, `organism`, `target_class` |
| `Assay` | Strong | `assay_code` | `protocol` (**composite**: method, readout, temperature), `standard_unit`, `description` |
| `ActivityObservation` | Strong, compound candidate key | (`assay`, `molecule`, `measured_at`) | `value`, `unit`, `quality_flag` |
| `Dataset` | Strong | `dataset_name` | `purpose`, `created_by`, *`version_count`* (**derived**) |
| `DatasetVersion` | **Weak** | (`dataset`, `version_number`) | `created_at`, `row_count`, `checksum`, `notes` |
| `Experiment` | Strong | `experiment_code` | `algorithm`, `hyperparameters`, `random_seed`, `started_at` |
| `ModelVersion` | Strong (weak is defensible) | `model_version_code`, or (`experiment`, `version_number`) | `metrics`, `artefact_uri`, `trained_at`, *`is_current`* (**derived or governed**) |
| `Prediction` | Strong | (`model_version`, `molecule`, `generated_at`) | `predicted_value`, `confidence` |
| `PredictionValidation` | Strong, 1:1 dependent | `prediction` | `observed_value`, `validated_on`, `validated_by`, `outcome` |
| `AuditLog` | Strong, append-only | `log_id` + `occurred_at` | `action`, `entity_name`, `entity_identifier`, `detail` |

**Not entity sets in the reference model:** nothing from the sixteen. All
sixteen survive as entity sets, but three of them (`MoleculeDescriptor`,
`ActivityObservation`, and the `holds` assignment between `UserAccount` and
`Role`) exist *because* a relationship carries descriptive attributes. A student
who models `holds` as a plain M:N relationship rather than an associative entity
is correct if they do not need `granted_at` / `granted_by`; they must say so.

## 2. Reference model — relationships, cardinality and participation

Participation is written as (left, right).

| # | Relationship | Left | Right | Card. | Participation | Domain rule |
|---|--------------|------|-------|-------|---------------|-------------|
| R-01 | is known as | `Molecule` | `MoleculeSynonym` | 1:N | (partial, total) | A synonym names exactly one structure; a molecule may have none. |
| R-02 | has value for | `Molecule` | `MoleculeDescriptor` | 1:N | (partial, total) | A descriptor value is about one molecule; descriptors are computed later. |
| R-03 | is instance of | `DescriptorType` | `MoleculeDescriptor` | 1:N | (partial, total) | A value has no meaning without its type and unit. |
| R-04 | is measured by | `BiologicalTarget` | `Assay` | 1:N | (partial, total) | An assay measures activity against exactly one target. |
| R-05 | produces | `Assay` | `ActivityObservation` | 1:N | (partial, total) | The protocol determines what the number means. |
| R-06 | is observed for | `Molecule` | `ActivityObservation` | 1:N | (partial, total) | An observation measures exactly one compound. |
| R-07 | belongs to (identifying) | `Dataset` | `DatasetVersion` | 1:N | (partial, **total**) | A version number means nothing outside its dataset. |
| R-08 | contains | `DatasetVersion` | `ActivityObservation` | M:N | (total, partial) | A snapshot lists many observations; an observation may sit in many snapshots or none. |
| R-09 | trains on | `DatasetVersion` | `Experiment` | 1:N | (partial, total) | Reproducibility requires exactly one frozen input snapshot per experiment. |
| R-10 | produces | `Experiment` | `ModelVersion` | 1:N | (partial, total) | A trained model comes from exactly one experiment run. |
| R-11 | predicts | `ModelVersion` | `Prediction` | 1:N | (partial, total) | A prediction is attributable to one model version. |
| R-12 | is predicted for | `Molecule` | `Prediction` | 1:N | (partial, total) | A prediction concerns one compound. |
| R-13 | is checked by | `Prediction` | `PredictionValidation` | 1:1 | (partial, total) | Most predictions are never validated; a validation checks exactly one prediction. |
| R-14 | holds | `UserAccount` | `Role` | M:N | (total, partial) | People wear several hats; a role may be defined before anyone holds it. |
| R-15 | acted | `UserAccount` | `AuditLog` | 1:N | (partial, total) | Every logged action has exactly one actor. |
| R-16 | curates | `UserAccount` | `Dataset` | 1:N | (partial, total) | A dataset has one accountable owner. |

Notes for grading:

- **R-08** is the row students most often get wrong. Modelling membership as
  molecules rather than observations is acceptable *if* they say what it costs:
  the model then cannot record which measurement of a molecule the snapshot
  froze, which weakens week 15's reproducibility claim. Award full marks for
  either, zero for neither being justified.
- **R-13** must be 1:1 with partial participation on the `Prediction` side. Total
  on both sides is the classic error: it makes a prediction unloadable until its
  validation exists.
- **R-09** as M:N is wrong and must be marked down: an experiment that trains on
  two dataset versions is not reproducible, and the requirement traceability in
  week 15 assumes one.

## 3. `DatasetVersion` as a weak entity — the argument to expect

- **Owner:** `Dataset`.
- **Identifying relationship:** *belongs to* (R-07), many-to-one towards the
  owner, with total participation on the `DatasetVersion` side.
- **Partial key (discriminator):** `version_number`, unique only within a
  dataset. Version 3 of "hERG screening" and version 3 of "aqueous solubility"
  are unrelated.
- **Full identifier:** (`dataset_name`, `version_number`).
- **Existence dependency:** deleting the dataset destroys the meaning of every
  version; the cascade is the correct default and becomes a referential action in
  week 09.
- **Alternative:** a globally unique `dataset_version_id`. It still works, but
  it silently permits a version whose parent is unknown, and it hides the rule
  that version numbers are consecutive per dataset — a rule week 15 relies on
  when it says "version N+1 supersedes version N".

`MoleculeSynonym` is the acceptable near-miss: it passes existence dependency and
identity-within-owner, so calling it weak with partial key `synonym_text` is
correct; calling it strong with a compound candidate key is also correct. What is
*not* acceptable is asserting one without applying the three tests.

`ActivityObservation` is not weak: it is a measurement event with its own
identity and other entities (dataset versions) refer to it directly.

`ModelVersion` is the deliberate grey case. Weak (owner `Experiment`, partial key
`version_number`) and strong (own code, unique registry-wide) are both
defensible; the deciding question is whether a model version is ever cited
outside the context of its experiment. In MoleculeTrace it is — predictions cite
it — so the reference makes it strong.

## 4. User–role specialisation — the argument to expect

The reference answer is **both**, and the reasoning matters more than the choice:

- **Generalisation** of `UserAccount` into `HumanAccount` and `ServiceAccount`,
  **disjoint** (no account is both) and **total** (every account is one or the
  other). Justified by *structural* difference: a human account has an email and
  a password credential; a service account has a rotating key, no email, and no
  interactive session.
- **`Role` kept as an entity set** with an M:N *holds* relationship carrying
  `granted_at` and `granted_by`. Justified because permissions change far more
  often than account structure, one person legitimately holds several roles, and
  "who granted this and when" is an auditable fact that has nowhere else to live.
- An administrator who is also a curator is two `holds` rows, not two subclasses.
  That is the sentence to look for.

Accept **M:N only** (no specialisation) with the argument that human and service
accounts differ in data but not in behaviour, if the student says what they lose:
a nullable email and no place for the service key's rotation policy.

Reject: a single `role` attribute on `UserAccount` (cannot hold two roles);
subclasses named after roles (`Curator`, `DataScientist`) with identical
attributes and relationships, since specialisation without extra structure is
just a type attribute wearing a costume.

## 5. Repairs for the five broken fragments (exercise 1)

| Fragment | Defects | Expected repair |
|----------|---------|-----------------|
| **F1** | Multivalued attribute flattened into `synonym_1..3`; a second multivalued attribute hidden in a comma-separated `supplier_codes`; `activity_count` is a stored derived value | Extract `MoleculeSynonym` as its own entity set related 1:N to `Molecule` (supplier codes are synonyms with `synonym_type = 'supplier code'`); delete `activity_count`, or label it derived and name the query that computes it. The fourth synonym then needs no schema change at all — which is the whole point. |
| **F2** | `DatasetVersion` modelled as strong although it is existence-dependent; `dataset_title` duplicated from the owner; `version_count` derived and stored; the relationship is drawn optional on the weak side | Make it weak: identifying relationship `Dataset ||--\|{ DatasetVersion`, partial key `version_number`, full identifier (`dataset`, `version_number`); delete `dataset_title` and `version_count`. It fails the partial-key and identity tests; it accidentally passes existence dependency, which is why the mistake survives review. |
| **F3** | `ActivityObservation.target_name` is reachable through `Assay`; the third relationship is a redundant shortcut that can contradict the two-step path | Delete both the attribute and the shortcut edge. The shortcut is only defensible if an observation could be attributed to a target *other* than its assay's target — for example a counter-screen recorded against a second target — and then it is a different fact and needs a different name. |
| **F4** | The descriptor value sits on `Molecule`, so a molecule can hold exactly one value for all descriptor types; the M:N relationship carries the fact it cannot hold | Promote the pairing to the associative entity `MoleculeDescriptor` with `value` and `computed_at`. Keeping two values computed by different software versions does not change the structure — it extends the identifier to (`molecule`, `descriptor_type`, `software_version`), which is a key change, not a shape change. |
| **F5** | `PREDICTION }\|--\|{ PREDICTION_VALIDATION` is M:N with total participation on both sides — wrong cardinality *and* wrong participation; `has_been_validated` is derived; `is_current` is derived-or-governed; `MODEL_VERSION \|\|--\|{ PREDICTION` forces a model to have a prediction before it can be registered | 1:1 with participation (partial, total): a prediction may have no validation, a validation must have exactly one prediction. Delete `has_been_validated` (derivable from the existence of the validation). `is_current` is not derivable at all — it is a governance decision, so it belongs on a relationship or a status entity that records who made it and when. Change the model-version relationship to `\|\|--o{`. |

Wrap-up answers: F1 and F4 fail for the same underlying reason — a fact was
attached to the wrong thing, once as a repeated attribute and once as an
attribute of one participant instead of the pairing. Normalisation (week 04)
would catch F1 and F3's copied attribute, but would leave F5's cardinality and
participation errors completely untouched: normal forms say nothing about how
many.

## 6. Acceptable alternatives

- Dataset membership by molecule instead of by activity observation, if the cost
  is stated (see R-08).
- `MoleculeSynonym` as strong with a compound key.
- `ModelVersion` as weak, owned by `Experiment`.
- `holds` as a plain M:N relationship without `granted_at`/`granted_by`, if the
  student explicitly gives up grant auditing and says which requirement suffers.
- `AuditLog` with a partial actor (system-generated entries with no user), if the
  participation table says so and the narrative explains it.
- Splitting or not splitting `Assay.protocol` — either is fine this week, because
  it is a week-03 decision; what is graded is that it was *identified* as
  composite.

## 7. Where students lose marks

1. **Participation stated on one side only.** Most common failure by a wide
   margin; the checkpoint catches it, so it usually means the checkpoint was not
   run.
2. **Cardinality justified by the sample data** ("1:1 because our CSV has one
   row each"). Ask for the domain rule; if there is none, the answer is 1:N.
3. **A diagram with no narratives.** The plain-language sentences are where
   misunderstandings surface. If the sentences are missing, do not assume the
   model is understood.
4. **Derived attributes left unlabelled**, especially `is_current` and the
   `*_count` attributes.
5. **The improved EER model identical to the initial one.** If the before/after
   table has six rows but the two Mermaid blocks are byte-identical, the student
   has documented improvements they did not make.
6. **Weak entity asserted, not argued.** "DatasetVersion is weak because it
   depends on Dataset" earns one mark out of two; the three tests, the partial
   key and the full identifier earn both.

## 8. Timing

Observed against the five-hour budget: concept notes 55–70 min; initial ER model
50–70 min (harvesting nouns is faster than students expect, classification
slower); improved EER model 40–55 min; the two tables 25–35 min; weak-entity and
specialisation arguments 20–30 min; exercises 55–70 min. The five broken
fragments take the longest of the exercises and are worth protecting if the week
overruns — cut exercise 4 Part D first.
