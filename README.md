# Fit-Buddy Backend

A privacy-first, AI-driven fitness assistant backend built with FastAPI. Delivers personalized workout and nutrition insights while keeping user data secure.

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
│   ├── api/
│   │   ├── api.py               # Root API router
│   │   └── v1/
│   │       ├── api.py           # v1 router
│   │       ├── users/           # User routes, models, schemas, enums
│   │       └── weights/         # Weight tracking routes, models, schemas
│   ├── config/
│   │   ├── db.py                # Database connection setup
│   │   └── settings.py          # Environment settings
│   ├── middlewares/
│   │   ├── auth.py              # JWT authentication middleware
│   │   └── logging.py           # Request logging middleware
│   └── utils/
│       └── helpers.py
├── infra/
│   ├── alembic.ini
│   └── migrations/              # Alembic migration versions
├── tests/
├── main.py
├── requirements.txt
└── .env.example
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

# Run database migrations
alembic -c infra/alembic.ini upgrade head

# Start the server
uvicorn main:app --reload
```

API available at: `http://localhost:8000`  
Interactive docs at: `http://localhost:8000/docs`

## Environment Variables

Create a `.env` file based on `.env.example`:

```env
DATABASE_URL=database-url
REDIS_URL=redis-url
SECRET_KEY=secret-key
```

## API Overview

| Resource | Base Path         |
| -------- | ----------------- |
| Users    | `/api/v1/users`   |
| Weights  | `/api/v1/weights` |

Full interactive documentation available at `/docs` when running locally.

## Running Tests

```bash
pytest tests/
```
