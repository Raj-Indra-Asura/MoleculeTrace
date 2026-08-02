# Week 02 — ER and EER Design

**Phase:** 0. Foundations · **Required effort:** 5 hours ·
**Depends on:** weeks 00–01

**Topic scope:** Entity sets and attributes; composite, multivalued and derived
attributes; relationship sets; 1:1, 1:N and M:N cardinalities; total and partial
participation; weak entities; specialisation and generalisation (EER); and the
detection of redundant attributes — applied to the sixteen MoleculeTrace
concepts named in section 5.1.

Week 01 agreed *what* is being built. Week 02 decides *what things exist, how
they relate, and how many of each* — the conceptual model that week 03 turns
into DDL and week 04 normalises.

## 1. Learning objectives

By the end of this week you can:

1. Identify entity sets in a written problem statement and defend each one
   against the alternative of making it an attribute of something else.
2. Classify an attribute as simple, composite, multivalued, derived or key, and
   restructure composite and multivalued attributes into the parts an ER diagram
   can hold.
3. Draw relationship sets with descriptive attributes and state the cardinality
   of each as 1:1, 1:N or M:N, with a reason drawn from the domain rather than
   from convenience.
4. Decide total versus partial participation for **both** sides of every
   relationship and say what each choice forbids.
5. Recognise a weak entity by its existence dependency, identifying relationship
   and partial key, and explain why `DatasetVersion` is one.
6. Apply specialisation and generalisation to the user/role part of the model
   and argue for one of: subclasses, a role relationship, or both.
7. Find redundant attributes and redundant relationships in an ER diagram and
   remove them without losing information.
8. Explain every relationship in the model in plain language that a bench
   scientist would accept.

## 2. Connection to MoleculeTrace

This week produces the conceptual backbone of the whole chain:

```
molecules → targets → assays → activities → dataset versions
         → experiments → model versions → predictions → validation
```

Week 03 converts your entity sets into tables and your cardinalities into keys
and foreign keys; week 04 checks the result against the normal forms; week 09
turns your participation constraints into `NOT NULL` and referential actions;
week 15 depends on `DatasetVersion` being modelled as a weak, immutable version
of a `Dataset`; week 16 depends on `Experiment`, `ModelVersion` and `Prediction`
being separate entity sets.

**Visible improvement this week:** the repository gains `docs/data-model.md` — an
initial ER model, an improved EER model, a cardinality table, a
participation-constraint table, a plain-language explanation of every
relationship and a design-decision log that later weeks cite instead of
re-arguing.

## 3. Prerequisites

- Week 01 checkpoint passed: `docs/01_problem_statement.md`,
  `docs/02_requirements.md` and `docs/03_architecture.md` are complete and their
  `FR-`/`NFR-` identifiers are stable.
- Mermaid renders for you (the week-01 architecture diagram proved this).

### Retrieval practice (15 minutes, required)

Answer from memory before opening any notes:

1. What is the difference between a schema and an instance, and which of the two
   does an ER diagram describe?
2. Name three of the six failures of file-based processing, and for each say
   which part of a conceptual model prevents it.
3. Which requirement IDs from `docs/02_requirements.md` mention a *rule about
   how many* of one thing may relate to another? Those are cardinality
   constraints in disguise.

Check your answers against
[`../week-01-requirements-and-architecture/LEARNING_NOTES.md`](../week-01-requirements-and-architecture/LEARNING_NOTES.md).

## 4. Five-hour study plan

| Block | Time | Activity | Output |
|-------|------|----------|--------|
| 1 | 0:00–0:15 | Retrieval practice (section 3) | Three written answers in `LEARNING_NOTES.md` |
| 2 | 0:15–1:15 | Conceptual notes (section 5) | Sections 2–4 of `LEARNING_NOTES.md` |
| 3 | 1:15–2:15 | Guided work (section 6) | Initial ER model in `docs/data-model.md` §2 |
| 4 | 2:15–3:45 | Independent work (section 7) | EER model, cardinality and participation tables, narratives, decision log |
| 5 | 3:45–4:30 | Exercises 1–4 (section 8) | Completed exercise files, five ER fragments repaired |
| 6 | 4:30–4:45 | Validation (section 9) | `make test-week` passes |
| 7 | 4:45–5:00 | Reflection and commit (sections 11–15) | Commit pushed, evidence saved |

## 5. Conceptual notes

Read once, then write section 3 of `LEARNING_NOTES.md` in your own words.

### 5.1 The sixteen concepts you must model

Every deliverable this week covers exactly these, no more and no fewer. The
one-line meanings are given; the structure is your job.

| Concept | Meaning in MoleculeTrace |
|---------|--------------------------|
| `UserAccount` | A person or program that can act in the system |
| `Role` | A named bundle of permissions (curator, data scientist, administrator, pipeline) |
| `Molecule` | One distinct chemical structure, identified by its canonical SMILES |
| `MoleculeSynonym` | An alternative name or supplier code for a molecule |
| `DescriptorType` | A kind of computed molecular property (molecular weight, logP, TPSA…) |
| `MoleculeDescriptor` | The value of one descriptor type for one molecule |
| `BiologicalTarget` | A protein or biological entity that compounds are tested against |
| `Assay` | A defined experimental protocol measuring activity against a target |
| `ActivityObservation` | One measured result: this molecule, this assay, this value, this unit |
| `Dataset` | A named, curated collection intended for modelling |
| `DatasetVersion` | An immutable snapshot of a dataset, numbered within that dataset |
| `Experiment` | One modelling attempt: a dataset version, an algorithm, a configuration |
| `ModelVersion` | A trained model produced by an experiment, with its metrics |
| `Prediction` | One model version's predicted value for one molecule |
| `PredictionValidation` | A later measured check of whether a prediction held up |
| `AuditLog` | An append-only record of who changed what, and when |

Nothing here says which of these is an entity set, which is a relationship set
with attributes, and which is a weak entity. Deciding that *is* the week.

### 5.2 Entity sets and attributes

An **entity** is a thing that exists independently and that the system needs to
remember facts about. An **entity set** is the collection of all entities of the
same kind, described by the same attributes: `Molecule` is an entity set,
"aspirin" is an entity in it.

The recurring question is *entity or attribute?* Three tests:

1. **Does it have attributes of its own?** A biological target has a name, an
   organism and an identifier — it is an entity, not a string on `Assay`.
2. **Can it exist before or after the thing that mentions it?** A `Role` exists
   whether or not anyone currently holds it.
3. **Do you need more than one of them per owner?** A molecule has many
   synonyms; a repeated attribute is an entity set waiting to be extracted.

Attribute vocabulary, all of which you must use correctly this week:

| Kind | Definition | MoleculeTrace example |
|------|------------|-----------------------|
| Simple (atomic) | Cannot usefully be divided | `Molecule.canonical_smiles` |
| **Composite** | Made of named parts that are separately meaningful | `Assay.protocol` = (method, readout, temperature); `UserAccount.full_name` = (given name, family name) |
| **Multivalued** | Several values of the same kind for one entity | the set of synonyms of a molecule; the set of roles held by a user |
| **Derived** | Computable from other stored data, so storing it invites contradiction | `Dataset.version_count`, `Molecule.activity_count`, `ModelVersion.is_current` |
| Key | Uniquely identifies an entity in its set | `Molecule.canonical_smiles`; `BiologicalTarget.target_code` |

Two rules of thumb that survive into week 03:

- A **composite** attribute is drawn as an attribute with sub-attributes; at
  logical design time it either becomes several columns or stays as one, and you
  must record which and why.
- A **multivalued** attribute cannot survive into a relational table. It becomes
  a separate entity set (`MoleculeSynonym`) or a relationship set (`UserAccount`
  holds `Role`). Deciding *which* is exercise 4's job.
- A **derived** attribute is a note in the model, not a stored fact, unless you
  can name what keeps it true. Week 10 shows the legitimate way to keep one.

### 5.3 Relationship sets

A **relationship** associates two (occasionally more) entities; a **relationship
set** is all relationships of the same kind. Relationships can carry
**descriptive attributes** of their own — the attribute belongs to the *pairing*,
not to either participant.

The single most useful question in this week: *does this fact describe the
molecule, the descriptor type, or the pairing of the two?* The numeric value of
logP for aspirin describes the pairing. That is why `MoleculeDescriptor` exists.

A relationship set with several descriptive attributes, or one that itself
participates in other relationships, is usually promoted to an **associative
entity set** — an entity that exists to record a pairing.
`ActivityObservation` is the clearest case: it pairs a molecule with an assay
and carries value, unit, quality flag and observation date, and other things
refer to it.

Every relationship you draw must be readable as a sentence in both directions:

> *One assay produces many activity observations; each activity observation was
> produced by exactly one assay.*

If you cannot say that sentence out loud without hedging, the relationship is
wrong or the cardinality is wrong. Section 7 requires this sentence, in plain
language, for **every** relationship in your model.

### 5.4 Cardinality: 1:1, 1:N and M:N

**Mapping cardinality** answers "how many of B may one A be related to, and vice
versa".

| Cardinality | Reading | MoleculeTrace candidate |
|-------------|---------|-------------------------|
| **1:1** | Each A relates to at most one B, and each B to at most one A | A prediction and its validation |
| **1:N** | One A relates to many B; each B to at most one A | A dataset and its versions; an assay and its observations |
| **M:N** | Many A relate to many B, and vice versa | Users and roles; dataset versions and molecules |

Practical guidance:

- Cardinality comes from a **domain rule**, not from convenience. Write the rule
  down: "an activity observation is produced by exactly one assay because the
  protocol determines the meaning of the number".
- Every **M:N** relationship becomes a table of its own in week 03. If it also
  carries attributes, model it now as an associative entity so week 03 has
  nothing to invent.
- A **1:1** relationship almost always hides a question: why are these two
  entity sets, not one? The answer is usually "because one side is optional, or
  written later, or owned by a different actor". `PredictionValidation` is
  separate from `Prediction` because most predictions are never validated and a
  validation arrives weeks later.
- Beware of cardinality that is true only of *today's* data. "One molecule has
  one supplier code" is a sampling accident, not a rule.

### 5.5 Participation: total and partial

Participation says whether *every* entity of a set must take part in a
relationship:

- **Total participation** (existence dependency, drawn as a double line): every
  entity of the set must participate. Every `ActivityObservation` must reference
  a `Molecule`.
- **Partial participation**: some entities may stand alone. A `Molecule` need
  not have any activity observation — a newly registered compound has none yet.

Two habits worth forming now:

1. State participation **for both sides** of every relationship. Half the design
   errors in this week come from only considering the interesting side.
2. Say what the constraint *forbids*, in one sentence: "total participation of
   `DatasetVersion` in *belongs to* forbids a version that names no dataset".
   That sentence becomes a `NOT NULL` in week 03 and a test in week 09.

Cardinality and participation are independent: 1:N tells you *how many*,
participation tells you *whether zero is allowed*. Together they give the
familiar minimum/maximum pair, written `(min, max)` in some notations.

### 5.6 Weak entity sets

A **weak entity set** has no key of its own. It is identified only in
combination with an **owner** (identifying) entity set, through an **identifying
relationship**, using a **partial key** (discriminator) that is unique only
within one owner.

Three properties must all hold:

1. **Existence dependency** — deleting the owner destroys the meaning of the
   weak entity.
2. **Identifying relationship** — the weak entity participates *totally* in it,
   and the relationship is many-to-one towards the owner.
3. **Partial key** — an attribute unique within the owner, not globally.

`DatasetVersion` is the worked example (section 6 step 6 and exercise 3):
version 3 of the "hERG screening" dataset and version 3 of the "solubility"
dataset are different things; `version_number` means nothing without the
dataset. The full argument is yours to write.

Not everything that looks dependent is weak. `ActivityObservation` depends on an
assay, but it has its own identity as a measurement event and other things point
at it; a candidate key of (assay, molecule, measured_at) makes it a strong
entity with a compound key. Knowing the difference is the point.

### 5.7 Specialisation and generalisation (the EER part)

**Specialisation** is top-down: an entity set has subgroups with extra
attributes or extra relationships. **Generalisation** is bottom-up: several
similar entity sets share attributes, which you lift into a superclass.
Subclasses inherit the superclass's attributes and relationships.

Two constraints must be stated for every specialisation:

- **Disjoint or overlapping** — may one entity belong to two subclasses at once?
- **Total or partial** — must every superclass entity belong to some subclass?

The user/role part of MoleculeTrace is deliberately ambiguous, and section 7
requires you to take a position. Two defensible designs:

1. **Specialisation** — `UserAccount` generalises `Curator`, `DataScientist`,
   `Administrator` and `PipelineAccount`, each with its own attributes and
   relationships. Good when subclasses genuinely differ in *structure* (a
   pipeline account has no email but has a service key).
2. **`Role` as an entity set with an M:N relationship** — a user *holds* roles,
   the assignment carries a granted-at date and a granting user. Good when
   permissions change often and one person wears several hats.

A common answer is *both*: generalise the structural difference (human versus
program) as a disjoint, total specialisation, and keep permissions as an M:N
`holds` relationship. Whatever you choose, record why, and record what the
rejected alternative would have cost.

### 5.8 Redundant attributes and redundant relationships

Redundancy in a conceptual model is not a performance question — it is a
**correctness** question, because two copies of a fact can disagree.

Four smells and their repairs:

| Smell | Example | Repair |
|-------|---------|--------|
| Attribute copied along a relationship | `ActivityObservation.target_name`, already reachable through `Assay` | Delete it; navigate the relationship |
| Derived value stored as a fact | `Dataset.version_count`, `Molecule.descriptor_count` | Mark as derived; compute it (week 07), or maintain it deliberately (week 10) |
| Redundant relationship (a cycle where one edge is implied) | `ActivityObservation → BiologicalTarget` *and* `ActivityObservation → Assay → BiologicalTarget` | Remove the implied edge — unless the two paths can legitimately differ, which must then be justified |
| Same fact in two entity sets | `Molecule.smiles` copied into `Prediction` | Keep one home for the fact |

The test for a redundant relationship: *can the two paths ever disagree?* If not,
the shortcut is redundant. If they can, it is not redundancy — it is a second,
different fact, and you must name it.

Weeks 04 and 09 will punish anything you leave in. It is cheaper to remove it
now, on paper.

### 5.9 Notation used in this repository

Diagrams are committed as **Mermaid source** (`.mmd`), so pull requests can
review them. Mermaid's `erDiagram` supports the cardinalities you need:

| Mermaid | Meaning |
|---------|---------|
| `\|\|--o{` | one to zero-or-many (1:N, partial on the many side) |
| `\|\|--\|{` | one to one-or-many (1:N, total on the many side) |
| `\|\|--o\|` | one to zero-or-one (1:1, optional) |
| `}o--o{` | many to many, optional both sides |

Mermaid cannot draw composite, multivalued or derived attributes, subclass
triangles or partial keys. So the diagram is only half the deliverable: the
tables and the narratives in `docs/data-model.md` carry the rest, and every
attribute you mark as composite, multivalued or derived must appear in the
attribute-classification table with that label.

## 6. Guided work (required)

Produce sections 1–3 of `docs/data-model.md` — the **initial ER model**, warts
included. Copy the skeletons from `starter/` and replace every `TODO:` marker.
The expected result is stated for each step.

1. **Harvest the nouns.** Re-read `docs/01_problem_statement.md` and list every
   noun that the system must remember. Map each to one of the sixteen concepts
   in section 5.1; anything left over is either out of scope or a missing
   requirement — say which.
   *Expected:* all sixteen concepts accounted for, each classified as candidate
   entity set, candidate relationship set or candidate attribute.
2. **Apply the entity-or-attribute tests.** For each of the sixteen, apply the
   three tests in section 5.2 and record the verdict in one line.
   *Expected:* every verdict cites at least one of the three tests.
3. **Classify the attributes.** Using `starter/attribute-classification.md`, list
   at least twenty attributes across the model and label each simple, composite,
   multivalued, derived or key.
   *Expected:* at least two composite, at least two multivalued and at least two
   derived attributes, each with the reason for the label.
4. **Draw the initial ER diagram.** Fill in `starter/er-initial.mmd` with the
   entity sets and relationships you have so far. It is *meant* to be imperfect:
   leave the multivalued attributes and any redundancy visible so that section 7
   can improve on something real.
   *Expected:* the file renders in <https://mermaid.live/> and contains every
   entity set you declared in step 2.
5. **Write the first relationship narratives.** For each relationship in the
   initial diagram, write the two-direction sentence from section 5.3.
   *Expected:* no sentence contains "maybe", "usually" or "some".
6. **Mark the weak-entity candidates.** Apply the three tests of section 5.6 to
   `DatasetVersion`, `MoleculeSynonym`, `MoleculeDescriptor` and `ModelVersion`,
   and record which pass all three.
   *Expected:* a verdict per candidate, with the failing test named where it
   fails.
7. **Commit the initial model on its own**, before improving it. The history is
   part of the lesson.
   *Expected:* `git log --oneline -1` shows a `docs(week-02)` commit and
   `docs/data-model.md` §2 contains the initial diagram.

## 7. Independent work (required)

No step list. Complete `docs/data-model.md`. Expect to revise it once.

**A. Improved EER model (§4 of the document)**

- A second Mermaid diagram, derived from the initial one, in which: every
  multivalued attribute has become an entity set or a relationship set; every
  redundant attribute and redundant relationship identified in section 5.8 is
  gone; associative entities carry their descriptive attributes; and the
  user/role decision from section 5.7 is applied.
- A prose block naming every **specialisation or generalisation** you introduced,
  each with its disjoint/overlapping and total/partial constraints.
- A **before/after list**: at least six concrete differences between the initial
  ER model and the improved EER model, each with the defect it removes.

**B. Cardinality table (§5)**

One row per relationship, with columns: relationship name, left entity, right
entity, cardinality (`1:1`, `1:N`, `M:N`), the domain rule that forces it, and
the plain-language sentence in both directions. Every relationship in the
improved diagram must appear. At least one 1:1, at least six 1:N and at least
two M:N.

**C. Participation-constraint table (§6)**

One row per relationship, with columns: relationship name, participation of the
left entity (`total`/`partial`), participation of the right entity, and *what
each total participation forbids*, in one sentence. Both sides must be stated
for every relationship — a blank cell fails validation.

**D. `DatasetVersion` as a weak entity (§7)**

A written argument, at least 200 words, that names: the owner entity set, the
identifying relationship, the partial key, the full identifier that results, the
existence dependency, and what happens to versions when a dataset is deleted.
Also state one alternative design (a globally unique version identifier) and say
what it would cost — week 15 depends on this argument.

**E. User–role specialisation discussion (§8)**

A written argument choosing between specialisation, an M:N `holds` relationship,
or both. Name the subclasses if you specialise, state disjointness and totality,
and explain how an administrator who is also a curator is represented. Connect it
to at least one requirement ID from `docs/02_requirements.md`.

**F. Relationship narratives (§9)**

Every relationship in the improved model explained in plain language a bench
scientist would accept: what it means, why it exists, and one sentence per
direction. No SQL, no foreign keys, no "many-to-many" jargon in the explanation
itself.

**G. Design-decision log (§10)**

At least eight decisions, `DD-01` upward, each with: the decision, the
alternatives considered, the reason for the choice, the consequence for a later
week, and the requirement ID it serves where applicable. At least one decision
must record something you changed your mind about between §2 and §4.

## 8. Exercises

Files live in `exercises/`. Skeletons with `TODO:` markers live in `starter/`.

| # | File | Type | Required? |
|---|------|------|-----------|
| 1 | `exercises/01-broken-er-fragments.md` | Repair five deliberately incorrect ER fragments | Required |
| 2 | `exercises/02-cardinality-and-participation.md` | Constraint drill | Required |
| 3 | `exercises/03-weak-entities.md` | Weak-entity analysis | Required |
| 4 | `exercises/04-attributes-and-redundancy.md` | Attribute classification and redundancy hunt | Required |
| 5 | `exercises/05-specialisation-alternatives.md` | EER design argument | **Optional (stretch)** |

Optional exercises are never assumed by a later week.

## 9. Validation

```bash
make test-week WEEK=week-02-er-and-eer-design
```

The tests read `docs/data-model.md` and check the structure later weeks depend
on: both diagrams present as Mermaid source, all sixteen domain concepts
mentioned, the cardinality table populated with valid values and no missing
cells, the participation table stating both sides, the weak-entity and
specialisation sections long enough to be arguments rather than assertions, at
least eight `DD-` decisions, and no `TODO:` marker left behind. They do not grade
your model — a human does that with the rubric and
`instructor/validation/week-02.md`.

Then:

```bash
make lint
```

Manual checks, with exact expected results, are listed in `CHECKPOINT.md`.
Compare your document against `expected-outputs/` for *shape* — column names,
identifier formats, the kind of sentence expected — not for content. There is
deliberately **no finished ER or EER diagram anywhere in this folder**: the
reference model lives in `instructor/solution-notes/week-02.md` and is to be
read only after you submit.

## 10. Common mistakes

- **Attribute that should be an entity set** → the same attribute name repeats
  with a number (`synonym_1`, `synonym_2`) or holds a comma-separated list →
  extract an entity set with a relationship to the owner.
- **Entity set that should be an attribute** → the "entity" has exactly one
  attribute, which is its own name, and nothing else ever refers to it → make it
  an attribute, unless a later week needs it to carry metadata.
- **M:N relationship with hidden attributes** → you cannot say where the measured
  value lives → promote the relationship to an associative entity set.
- **Cardinality copied from the sample data** → "1:1 because our CSV has one row
  each" → restate as a domain rule, or widen to 1:N.
- **Participation stated on one side only** → the table has blanks → decide both
  sides; "partial" is an answer, "blank" is not.
- **Weak entity with a surrogate key already attached** → the "weak" entity has a
  globally unique id and no partial key → either it is not weak, or the surrogate
  is a week-03 implementation decision that does not belong in the conceptual
  model.
- **Specialisation with no extra structure** → subclasses have identical
  attributes and relationships → use a role or a type attribute instead.
- **Redundant relationship kept "for convenience"** → two paths between the same
  entity sets that can never disagree → delete the shortcut; note it as a
  possible week-17 index instead.
- **Derived value stored as a plain attribute** → a count or a flag that some
  other data already determines → label it derived and say who recomputes it.
- **A diagram with no sentences** → the model is only pictures → every
  relationship needs its two-direction sentence before the week can pass.

## 11. Reflection questions

Answer in `REFLECTION.md`:

1. Which of the sixteen concepts was hardest to classify as entity, relationship
   or attribute, and what finally decided it?
2. Which cardinality did you first get wrong, and what domain fact corrected it?
3. Week 01 asked you to assign responsibilities to tiers. Which participation
   constraint from this week will become a database constraint rather than an
   application check, and why?

## 12. Completion checklist

- [ ] Retrieval practice answered before consulting notes.
- [ ] Conceptual notes summarised in `LEARNING_NOTES.md`.
- [ ] `docs/data-model.md` complete, no `TODO:` markers left.
- [ ] Initial ER diagram (§2) and improved EER diagram (§4) both present as
      Mermaid source, with a before/after list of at least six differences.
- [ ] Cardinality table (§5) covers every relationship, ≥1 one-to-one, ≥6
      one-to-many, ≥2 many-to-many.
- [ ] Participation table (§6) states both sides for every relationship.
- [ ] `DatasetVersion` weak-entity argument (§7) names owner, identifying
      relationship and partial key.
- [ ] User–role specialisation discussion (§8) states disjointness and totality.
- [ ] Every relationship explained in plain language (§9).
- [ ] Design-decision log (§10) has ≥8 `DD-` entries.
- [ ] Required exercises 1–4 done, all five broken fragments repaired.
- [ ] `make test-week WEEK=week-02-er-and-eer-design` passes.
- [ ] Shapes match `expected-outputs/`.
- [ ] `REFLECTION.md` completed.
- [ ] Portfolio evidence saved (section 14).
- [ ] Work committed and the progress table in the root `README.md` updated.

## 13. Syllabus mapping

| Syllabus topic | Covered by |
|----------------|-----------|
| ER model: entity sets and attributes | sections 5.2, 6 (steps 1–3), exercise 4 |
| Composite, multivalued and derived attributes | section 5.2, `starter/attribute-classification.md`, exercise 4 |
| Relationship sets and descriptive attributes | sections 5.3, 7A, 7F |
| Mapping cardinalities 1:1, 1:N, M:N | sections 5.4, 7B, exercise 2 |
| Total and partial participation | sections 5.5, 7C, exercise 2 |
| Weak entity sets, identifying relationships, partial keys | sections 5.6, 7D, exercise 3 |
| Specialisation, generalisation and inheritance (EER) | sections 5.7, 7E, exercise 5 |
| Reduction of redundancy in conceptual design | sections 5.8, 7A, exercise 1 |

See [`SYLLABUS_MAPPING.md`](../../SYLLABUS_MAPPING.md).

## 14. Portfolio evidence

Save to `docs/portfolio/week-02/`:

- `er-model-summary.md` — the improved EER diagram source, the cardinality table
  and the three design decisions you are most confident defending.
- An export of the improved EER diagram.
- A one-paragraph write-up, suitable for a README or an interview, explaining
  why `DatasetVersion` is a weak entity and what reproducibility problem that
  choice prevents.

## 15. Suggested Git commit

```bash
git add -A
git commit -m "docs(week-02): model the molecular domain as ER and EER designs"
```

## 16. Rubric (out of 10)

| Criterion | Weight | 0 | 1 | 2 |
|-----------|--------|---|---|---|
| Correctness of required exercises | 3 | Not attempted | Partly correct | Fully correct and validated |
| Depth of conceptual understanding (notes + reflection) | 2 | Absent | Restates the text | Explains in own words with a project example |
| Quality of the project improvement | 2 | None | A diagram with no constraints or justification | Complete EER model with cardinality, participation and a reasoned decision log |
| Validation and evidence | 2 | None | Partial | All checks pass, evidence saved |
| Git hygiene and documentation | 1 | Absent | Inconsistent | Clear commits, progress table updated |

Scoring: multiply each criterion's score (0–2) by its weight, divide by 2,
round to the nearest whole number. **Pass mark: 7/10.** The detailed rubric
lives in [`instructor/rubrics/`](../../instructor/rubrics/).
