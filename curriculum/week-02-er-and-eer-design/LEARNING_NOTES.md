# Week 02 — Learning Notes

Section 1 is given. Write sections 2–6 yourself, as you go, not afterwards.

## 1. The vocabulary, in one page

| Term | Definition | MoleculeTrace example |
|------|------------|-----------------------|
| Entity | A thing the system must remember facts about | The molecule with canonical SMILES `CC(=O)Oc1ccccc1C(=O)O` |
| Entity set | All entities of the same kind, same attributes | `Molecule` |
| Attribute | A property of an entity or of a relationship | `Molecule.canonical_smiles` |
| Simple attribute | Cannot usefully be divided | `Assay.assay_code` |
| Composite attribute | Has named, separately meaningful parts | `UserAccount.full_name` = (given, family) |
| Multivalued attribute | Several values of one kind per entity | The synonyms of a molecule |
| Derived attribute | Computable from other stored data | `Dataset.version_count` |
| Key attribute | Uniquely identifies an entity in its set | `BiologicalTarget.target_code` |
| Relationship | An association between entities | *this assay produced this observation* |
| Relationship set | All relationships of the same kind | *produces* |
| Descriptive attribute | An attribute of the pairing, not of either side | The measured value of a descriptor for a molecule |
| Associative entity | A relationship promoted to an entity because it carries facts | `ActivityObservation`, `MoleculeDescriptor` |
| Mapping cardinality | How many of each side may be related | `Dataset` 1:N `DatasetVersion` |
| Total participation | Every entity of the set must participate | Every `ActivityObservation` references a `Molecule` |
| Partial participation | Some entities may stand alone | A `Molecule` may have no predictions |
| Weak entity set | Has no key of its own | `DatasetVersion` |
| Owner (identifying) entity set | Supplies the missing identity | `Dataset` |
| Identifying relationship | Links weak entity to owner; weak side is total | *belongs to* |
| Partial key (discriminator) | Unique only within one owner | `version_number` |
| Specialisation | Top-down split into subclasses with extra structure | `UserAccount` → human / program accounts |
| Generalisation | Bottom-up merge of similar entity sets into a superclass | Curator and data scientist → `UserAccount` |
| Disjoint / overlapping | May one entity be in two subclasses at once? | Decide and record |
| Total / partial specialisation | Must every superclass entity be in a subclass? | Decide and record |
| Redundant attribute | The same fact stored twice, reachable another way | A target's name copied onto an observation |
| Redundant relationship | An edge implied by a path that can never disagree | Observation → target, when observation → assay → target exists |

### The three weak-entity tests

Existence dependency · identifying relationship with total participation on the
weak side · partial key unique only within the owner. All three must hold. Learn
them as a list; you will apply them to four candidates this week.

## 2. My retrieval-practice answers (README section 3)

1. Schema versus instance, and which one an ER diagram describes:
2. Three failures of file-based processing and the modelling feature that
   prevents each:
3. Requirement IDs from `docs/02_requirements.md` that are really cardinality
   constraints:

## 3. Core ideas in my words

1. When a noun becomes an entity set rather than an attribute:
2. Why a descriptive attribute belongs to the relationship and not to either
   participant:
3. How I tell 1:N from M:N without looking at sample data:
4. What total participation forbids, in one sentence:
5. Why `DatasetVersion` cannot be identified without `Dataset`:
6. When specialisation beats a role relationship, and when it does not:

## 4. My attribute classification, in miniature

Two examples of each kind from my own model, with the reason for the label.

| Kind | Example 1 | Example 2 | Why |
|------|-----------|-----------|-----|
| Composite | | | |
| Multivalued | | | |
| Derived | | | |

## 5. Worked example from this week

<Paste one relationship whose cardinality or participation you changed. Show the
first version, the corrected version, and the domain fact that forced the
change.>

Before:

After:

The domain fact that decided it:

## 6. Connections to earlier weeks

- Which requirement from `docs/02_requirements.md` did the model force me to
  add, change or delete?
- Which responsibility from `docs/03_architecture.md` is now clearly a database
  concern because the model makes it a constraint?
- What do I expect week 03 to take directly from `docs/data-model.md`?

## Open questions

-
