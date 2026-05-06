# Product Snapshot

This repository is a small server-rendered Flask message board backed by PostgreSQL. As of `main` today, the project includes the application entrypoint, database connection/bootstrap logic, deployment packaging, a homepage that renders stored messages, and a form flow for posting new messages.

## What Exists

- Python dependencies are pinned in `requirements.txt`:
  `Flask`, `psycopg2-binary`, and `gunicorn`.
- Environment configuration is established through `.env.example` with a required `DATABASE_URL`.
- A repository `.gitignore` covers Python artifacts and local workspace secrets/state files.
- Container packaging is defined with a `python:3.11-slim` `Dockerfile` that installs dependencies, copies the repository, exposes port `8080`, and is configured to start Gunicorn with `app:app`.
- A `.dockerignore` keeps local secrets and workspace-only files out of the image build context.
- A minimal Flask application entrypoint exists in `app.py`.
- PostgreSQL access is centralized in `db.py`, which reads `DATABASE_URL` from the environment.
- App startup bootstraps the `messages` table automatically with `CREATE TABLE IF NOT EXISTS`.
- `GET /` renders an inline HTML page with `name` and `text` inputs plus the current message list.
- `POST /messages` accepts form-encoded `name` and `text`, inserts valid submissions into PostgreSQL, and redirects back to `/`.
- Messages are read from PostgreSQL and displayed newest first by `created_at DESC`.
- Blank `name` or `text` submissions are rejected with HTTP `400`.
- `README.md` documents the basic setup flow for creating a virtualenv, installing dependencies, and exporting `DATABASE_URL`.

## Intended Product Direction

The product is taking shape as a Flask web app that stores persistent message data in PostgreSQL and runs behind Gunicorn on port `8080`. Persistent state lives in PostgreSQL, configured entirely through environment variables.

## Current Conventions

- Keep configuration environment-driven; do not hardcode database credentials.
- Treat PostgreSQL as the only persistent datastore.
- Initialize required database schema during app startup.
- Keep the current UI server-rendered with `render_template_string`.
- Use a classic POST/redirect flow after successful writes.
- Use the container image as the intended production packaging format.
- Keep repository docs accurate to the merged `main` branch state, even when later issues are still pending.
