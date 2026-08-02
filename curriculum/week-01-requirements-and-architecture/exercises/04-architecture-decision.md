# Exercise 4 — Architecture decision (Required)

## Part A — The tier argument

Complete both columns honestly; the two-tier column must contain real
advantages, or the exercise is worthless.

| Criterion | Two-tier (client → database) | Three-tier (client → application → database) |
|-----------|------------------------------|----------------------------------------------|
| Where credentials live | | |
| Where business rules live | | |
| Effect of 50 concurrent dashboard users | | |
| Cost of replacing the dashboard | | |
| Cost of adding an ML batch job | | |
| Ease of debugging a failure | | |
| Effort to build in this course | | |

**Decision:** MoleculeTrace uses ______ -tier.

**Three reasons, each citing a requirement ID from `docs/02_requirements.md`:**

1.
2.
3.

**The strongest argument against the decision, and your answer to it:**

## Part B — Responsibility assignment

For each responsibility, name the owning tier and defend it in one sentence.
Two of these are deliberately arguable.

| Responsibility | Owner (data / application / ML / presentation) | Justification |
|----------------|-----------------------------------------------|---------------|
| A molecule's canonical SMILES is unique | | |
| An activity cannot reference a missing assay | | |
| An activity value must be within a plausible range | | |
| A published dataset version is immutable | | |
| Descriptor calculation from SMILES | | |
| Choosing which model version is current | | |
| Rejecting a malformed HTTP request body | | |
| Deciding a user may not see raw supplier data | | |

## Part C — Where a rule is enforced

Pick the rule "a published dataset version is immutable" and describe, in three
sentences, what happens to a client that tries to modify one at each tier it
passes through. Name the component that finally refuses.
