# scripts/

Small helper scripts invoked by the `Makefile` or by a curriculum week. Each
script must:

- be runnable from the repository root;
- take configuration from `.env` (never hard-coded credentials);
- print what it is about to do before doing it;
- be idempotent, or refuse to run twice.

Any script that generates data writes it to `project/data/synthetic/` with
`_synthetic` in the filename.

Scripts are added by the weeks that need them; the folder starts empty.
