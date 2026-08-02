# init/

SQL in this folder runs **only when the database volume is empty**, in filename
order. Re-running it requires `make reset`, which deletes the volume.

Keep it minimal: extensions, schemas and roles. Table creation belongs in
`../migrations/`.
