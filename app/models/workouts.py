import enum
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Enum,
    ForeignKey, Integer, Numeric, SmallInteger, String, Text, UniqueConstraint)
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy.sql import func
from app.db.connection import Base
from sqlalchemy import Date
import datetime

# ── Workout Sets ──────────────────────────────────────────

class WorkoutSet(Base):
    __tablename__ = "workout_sets"

    id          = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id     = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    exercise_id = Column(Integer,    ForeignKey("exercises.id", ondelete="RESTRICT"), nullable=False)
    logged_date = Column(Date, nullable=False, default=datetime.date.today)
    set_number  = Column(SmallInteger, nullable=False)
    weight_kg   = Column(Numeric(6, 2), nullable=True)
    reps        = Column(SmallInteger,  nullable=True)
    rpe         = Column(Numeric(3, 1), nullable=True)
    is_warmup   = Column(Boolean, nullable=False, default=False)
    is_dropset  = Column(Boolean, nullable=False, default=False)
    is_failure  = Column(Boolean, nullable=False, default=False)
    notes       = Column(Text, nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    modified_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    user     = relationship("User",     back_populates="workout_sets")
    exercise = relationship("Exercise", back_populates="workout_sets")

# ── Workout Notes ─────────────────────────────────────────

class WorkoutNote(Base):
    __tablename__ = "workout_notes"

    id          = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id     = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    logged_date = Column(Date, nullable=False, default=datetime.date.today)
    notes       = Column(Text, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    modified_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())

    __table_args__ = (
        UniqueConstraint("user_id", "logged_date", name="uq_workout_notes_user_date"),
    )

    user = relationship("User", back_populates="workout_notes")