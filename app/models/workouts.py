import enum
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Enum,
    ForeignKey, Integer, Numeric, SmallInteger, String, Text, UniqueConstraint
)
from sqlalchemy.orm import DeclarativeBase, relationship
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

    user     = relationship("User",     back_populates="workout_sets")
    exercise = relationship("Exercise", back_populates="workout_sets")

# ── Workout Plan Exercise ───────────────────────────────────

class WorkoutPlanExercise(Base):
    __tablename__ = "workout_plan_exercises"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    plan_id = Column(UUID(as_uuid=True), ForeignKey("workout_plans.id", ondelete="CASCADE"), nullable=False)
    exercise_id = Column(UUID(as_uuid=True), ForeignKey("exercises.id", ondelete="CASCADE"), nullable=False)
    day_order = Column(Integer, nullable=True)
    day_label = Column(String, nullable=True)
    position = Column(Integer, nullable=True)
    prescribed_sets = Column(Integer, nullable=True)
    prescribed_reps = Column(String, nullable=True)   # varchar — could be "3x8" or "8-12"
    prescribed_rpe = Column(Numeric, nullable=True)
    rest_seconds = Column(Integer, nullable=True)
    notes = Column(String, nullable=True)

    # Relationships
    plan = relationship("WorkoutPlan", back_populates="exercises")
    exercise = relationship("Exercise", back_populates="plan_exercises")

# ── Workout Notes ─────────────────────────────────────────

class WorkoutNote(Base):
    __tablename__ = "workout_notes"

    id          = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id     = Column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    logged_date = Column(Date, nullable=False, default=datetime.date.today)
    notes       = Column(Text, nullable=False)

    __table_args__ = (
        UniqueConstraint("user_id", "logged_date", name="uq_workout_notes_user_date"),
    )

    user = relationship("User", back_populates="workout_notes")