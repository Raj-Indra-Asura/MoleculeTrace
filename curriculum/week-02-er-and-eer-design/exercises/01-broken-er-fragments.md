# Exercise 1 — Five broken ER fragments (Required)

Each fragment below is a real design mistake, written the way people actually
write them. For each one: name the defect, say what goes wrong in the data if it
ships, and write the repaired fragment as Mermaid `erDiagram` source.

Answer in the three cells under each fragment. Replace every `TODO`.

Defect vocabulary to draw on: *multivalued attribute*, *composite attribute not
decomposed*, *derived attribute stored*, *redundant attribute*, *redundant
relationship*, *wrong cardinality*, *wrong participation*, *missing associative
entity*, *weak entity modelled as strong*, *specialisation with no extra
structure*.

---

## F1 — The molecule that knows its own names

```mermaid
erDiagram
    MOLECULE {
        string canonical_smiles
        string synonym_1
        string synonym_2
        string synonym_3
        string supplier_codes "comma-separated"
        int    activity_count
    }
```

| Field | Your answer |
|-------|-------------|
| Defect(s) | TODO |
| What goes wrong in the data | TODO |
| Repaired fragment | TODO: Mermaid source |

Also answer: a fourth synonym arrives. What has to change in the broken version,
and what has to change in your repaired version?

---

## F2 — The dataset version that stands alone

```mermaid
erDiagram
    DATASET {
        int    dataset_id
        string title
        int    version_count
    }
    DATASET_VERSION {
        int    dataset_version_id
        string dataset_title
        int    version_number
        date   created_at
    }
    DATASET ||--o{ DATASET_VERSION : "has"
```

| Field | Your answer |
|-------|-------------|
| Defect(s) | TODO |
| What goes wrong in the data | TODO |
| Repaired fragment | TODO: Mermaid source |

Also answer: which of the three weak-entity tests does the broken version fail,
and which one does it accidentally pass?

---

## F3 — The observation that knows its target twice

```mermaid
erDiagram
    BIOLOGICAL_TARGET {
        string target_code
        string target_name
    }
    ASSAY {
        string assay_code
        string method
        string readout
        string temperature
    }
    ACTIVITY_OBSERVATION {
        int    observation_id
        float  value
        string unit
        string target_name
    }
    BIOLOGICAL_TARGET ||--o{ ASSAY : "is measured by"
    ASSAY ||--o{ ACTIVITY_OBSERVATION : "produces"
    BIOLOGICAL_TARGET ||--o{ ACTIVITY_OBSERVATION : "is measured in"
```

| Field | Your answer |
|-------|-------------|
| Defect(s) | TODO |
| What goes wrong in the data | TODO |
| Repaired fragment | TODO: Mermaid source |

Also answer: name the one circumstance in which the third relationship would
*not* be redundant, and say what would have to be true of the domain for that
circumstance to arise.

---

## F4 — The descriptor value with nowhere to live

```mermaid
erDiagram
    MOLECULE {
        string canonical_smiles
        float  descriptor_value
    }
    DESCRIPTOR_TYPE {
        string descriptor_name
        string unit
    }
    MOLECULE }o--o{ DESCRIPTOR_TYPE : "has"
```

| Field | Your answer |
|-------|-------------|
| Defect(s) | TODO |
| What goes wrong in the data | TODO |
| Repaired fragment | TODO: Mermaid source |

Also answer: two descriptor values for the same molecule and the same descriptor
type, computed by different software versions, must both be kept. Does that
change your repair? Say what it changes and what it does not.

---

## F5 — The validation that outnumbers the prediction

```mermaid
erDiagram
    MODEL_VERSION {
        int    model_version_id
        string algorithm
        bool   is_current
    }
    PREDICTION {
        int    prediction_id
        float  predicted_value
        bool   has_been_validated
    }
    PREDICTION_VALIDATION {
        int    validation_id
        float  observed_value
        date   validated_on
    }
    MODEL_VERSION ||--|{ PREDICTION : "produces"
    PREDICTION }|--|{ PREDICTION_VALIDATION : "is validated by"
```

| Field | Your answer |
|-------|-------------|
| Defect(s) | TODO |
| What goes wrong in the data | TODO |
| Repaired fragment | TODO: Mermaid source |

Also answer two questions:

1. `PREDICTION.has_been_validated` and `MODEL_VERSION.is_current` are both
   suspect, for different reasons. Name each reason.
2. `MODEL_VERSION ||--|{ PREDICTION` says a model version has at least one
   prediction. What does that forbid, and is it what you want the moment a model
   is registered?

---

## Wrap-up

1. Which of the five defects also exists somewhere in *your* initial ER model in
   `docs/data-model.md` section 2? Name it, and record the repair in the
   before/after table in section 4.2.
2. Two of the five fragments fail for the same underlying reason. Which two, and
   what is the reason?
3. Which defect would be caught by week 04's normalisation, and which would
   survive normalisation untouched? Explain why normalisation is not a substitute
   for conceptual design.
