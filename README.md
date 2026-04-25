# Fit-Buddy Backend

A privacy-first, AI-driven fitness assistant and workout tracking backend built with FastAPI. Delivers personalized workout and nutrition insights while keeping user data secure.

## Tech Stack

| Layer            | Technology                            |
| ---------------- | ------------------------------------- |
| API Framework    | FastAPI                               |
| Primary Database | PostgreSQL (SQLAlchemy ORM + Alembic) |
| Caching          | Redis                                 |
| Authentication   | JWT (middleware-based)                |
| Containerization | Docker                                |
| Language         | Python 3.11+                          |

## Features

- JWT-based authentication via custom middleware
- User management with role/enum support
- Weight tracking with versioned schema migrations
- Modular v1 API structure ready for versioning
- Request logging middleware
- Alembic migrations for reliable schema management

## Project Structure

```
fit-buddy-backend/
├── app/
│   ├── api/
│   │   ├── routers/           # API Endpoints, empty of logic
│   │   ├── schemas/           # Contract definitions between client and endpoints
│   │   └── services/          # Business logic lives here
│   ├── db/                    # Database related logic
│   └── models/                # Database models written in SQLAlchemy
├── infra/                     # All related infrastructure configs live here
│   └── migrations/            # The folder where alembic lives in
│       └── versions/          # Continous version of alembic migrations
└── tests/                     # Here we run the tests

```

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL
- Redis

### Setup

```bash
git clone https://github.com/Mohammed-Hussein0/fit-buddy-backend.git
cd fit-buddy-backend

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Fill in your values in .env
'''

### Routine

'''bash
#Activate virtual environment
source venv/bin/activate        # Windows: venv\Scripts\activate

# Start the server
uvicorn main:app --reload       # Without --reload to stop automatic reloads of the server

# Run database migrations
alembic revision --autogenerate -m {description} # To revise the migration
alembic -c infra/alembic.ini upgrade head        # To force the migration
```

API available at: `http://localhost:8000`  
Interactive docs at: `http://localhost:8000/docs`

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
DATABASE_URL=database-url
SECRET_KEY=secret-key
```

## API Overview

| Resource | Base Path         |
| -------- | ----------------- |
| Users    | `/api/users`   |
| Weights  | `/api/weights` |
| Workouts | `/api/workouts` |

Full interactive documentation available at `/docs` when running locally.

## Running Tests

```bash
pytest tests/
```
