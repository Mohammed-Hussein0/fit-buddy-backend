from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, DeclarativeBase
import os
from dotenv import load_dotenv
from fastapi import Depends

class Base(DeclarativeBase):
    pass

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

engine = create_engine(DB_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()