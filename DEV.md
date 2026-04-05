# Database Modeling & Migrating

## Modeling

- Each feature has a "models.py" file in it's folder, where it contains the orm's models and their behvaviors

## Migrating

- Run the command "alembic revision --autogenerate -m {description}" in the terminal in the venv of the app
- ALWAYS revise the migration file now existing in /infra/migrations/versions, adjust as needed
- run the command "alembic upgrade head" to modify the database to match the orm, without destroying it

## Helpful Commands

- alembic stamp head : Tells Alembic “this DB state is our baseline, don’t change anything yet”
- alembic downgrade -1 : Reverts last migration
- alembic current : Shows which migration is applied
- alembic history : List all migrations

# To start the server, run "uvicorn main:app", you can add "--reload" in development to automatically see changes