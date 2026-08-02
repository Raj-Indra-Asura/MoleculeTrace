# project/ml/

Deliberately simple molecular machine learning, built in weeks 14–16.

| Folder | Purpose |
|--------|---------|
| `features/` | RDKit descriptor computation from SMILES |
| `models/` | Trained scikit-learn artefacts (git-ignored) |
| `notebooks/` | Exploration only; nothing here is a dependency of the project |

Scope rule: descriptor-based scikit-learn models only. No docking, no
protein-structure prediction, no graph neural networks, no molecular generation.

All metrics are educational. They are not evidence of biological activity.
