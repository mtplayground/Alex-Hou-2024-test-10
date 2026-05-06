# Alex-Hou-2024-test-10

Flask/PostgreSQL message board bootstrap.

## Setup

1. Create a virtual environment and install dependencies:
   `python3 -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt`
2. Configure the database connection:
   `cp .env.example .env`
3. Export `DATABASE_URL` before running the app:
   `export DATABASE_URL=postgresql://user:password@host:5432/database`

`app.py` and the container/runtime entrypoints are added in later issues. This issue only prepares the repository dependencies and environment configuration.
