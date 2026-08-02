# project/

The MoleculeTrace application. Everything here is built incrementally by the
curriculum; folders start empty by design.

| Folder | Built in | Contents |
|--------|----------|----------|
| `database/` | weeks 01–11, 17–22 | `init/` bootstrap SQL, `migrations/`, `seeds/`, `queries/` |
| `backend/` | weeks 12–13 | FastAPI application and Pydantic models |
| `frontend/` | week 22 | Streamlit dashboard |
| `ml/` | weeks 14–16 | Feature building, training, evaluation, model artefacts |
| `data/` | weeks 05, 14–15 | `raw/`, `processed/`, `synthetic/` |
| `tests/` | week 05 onward | pytest suites for the project code |

Domain chain modelled here:

```
molecules → targets → assays → activities → dataset versions
          → experiments → model versions → predictions → validation
```

> Educational project. Molecular results are teaching artefacts, not scientific
> or medical claims.
