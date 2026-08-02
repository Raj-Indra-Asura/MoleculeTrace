# project/frontend/

Streamlit dashboard, built in week 22. Entry point: `app.py`, launched with
`make dashboard`.

The dashboard reads through the FastAPI service (`API_BASE_URL`) or through
read-only queries, and presents dataset versions, experiment history and model
metrics.

Every chart that shows molecular results carries an "educational, synthetic
data" note.
