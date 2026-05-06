# Product Snapshot

This repository is the bootstrap for a small Flask message board backed by PostgreSQL. As of `main` today, the app itself is not implemented yet; the merged state only prepares the project for that work.

## What Exists

- Python dependencies are pinned in `requirements.txt`:
  `Flask`, `psycopg2-binary`, and `gunicorn`.
- Environment configuration is established through `.env.example` with a required `DATABASE_URL`.
- A repository `.gitignore` covers Python artifacts and local workspace secrets/state files.
- `README.md` documents the basic setup flow for creating a virtualenv, installing dependencies, and exporting `DATABASE_URL`.

## Intended Product Direction

The planned product is a Flask web app that stores persistent message data in PostgreSQL and is intended to run under Gunicorn. Persistent state is expected to live in PostgreSQL, configured entirely through environment variables.

## Current Conventions

- Keep configuration environment-driven; do not hardcode database credentials.
- Treat PostgreSQL as the only persistent datastore.
- Keep repository docs accurate to the merged `main` branch state, even when later issues are still pending.
