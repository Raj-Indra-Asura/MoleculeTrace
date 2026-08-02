# Expected shape — `docs/03_architecture.md`

## The diagram

One fenced ```` ```mermaid ```` block. It must name all three tiers, show the
ML/ETL component, and label every arrow with a protocol. Presentation must not
have an arrow to the data tier.

```
flowchart TD
    subgraph PRESENTATION[...]
    subgraph APPLICATION[...]
    subgraph DATA[...]
    <client> -->|HTTP/JSON| <service>
    <service> -->|SQL over TCP 5432| <database>
    <etl>     -->|SQL over TCP 5432| <database>
```

## The responsibility table

```markdown
| Responsibility | Owning tier | Justification |
|----------------|-------------|---------------|
| Uniqueness of a molecule's canonical SMILES | Data | Must hold for every writer, including the ETL job |
```

At least 8 rows; owning tier is one of `Data`, `Application`, `ML`,
`Presentation`.

## The file-system versus DBMS comparison

Six rows, one per dimension: redundancy and inconsistency, difficulty accessing
data, data isolation, integrity, atomicity, concurrent access and security. Each
row carries a MoleculeTrace example.

## The data-flow narrative

Prose, numbered steps, naming for each step: the component, the protocol and the
rule enforced there. Two flows are required — one ingest flow and one prediction
flow.

## Levels of abstraction

Three headed subsections — physical, logical, view — plus one worked example of
physical data independence and one of logical data independence.
