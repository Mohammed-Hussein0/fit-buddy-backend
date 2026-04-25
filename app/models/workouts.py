import enum
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Enum,
    ForeignKey, Integer, Numeric, SmallInteger, String, Text, UniqueConstraint
)
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import func
from app.db.connection import Base

# ── Workout Exercises ─────────────────────────────────────

class WorkoutPlanExercise(Base):
    __tablename__ = "workout_plan_exercises"

    id              = Column(Integer, primary_key=True, autoincrement=True)
    plan_id         = Column(Integer, ForeignKey("workout_plans.id", ondelete="CASCADE"),  nullable=False)
    exercise_id     = Column(Integer, ForeignKey("exercises.id",     ondelete="RESTRICT"), nullable=False)
    day_order       = Column(SmallInteger, nullable=False)
    day_label       = Column(String(80),   nullable=True)
    position        = Column(SmallInteger, nullable=False)
    prescribed_sets = Column(SmallInteger, nullable=True)
    prescribed_reps = Column(String(20),   nullable=True)
    prescribed_rpe  = Column(Numeric(3, 1), nullable=True)
    rest_seconds    = Column(SmallInteger,  nullable=True)
    notes           = Column(Text, nullable=True)

    __table_args__ = (
        UniqueConstraint("plan_id", "day_order", "position", name="uq_plan_day_position"),
    )

    plan     = relationship("WorkoutPlan", back_populates="exercises")
    exercise = relationship("Exercise",    back_populates="plan_exercises")


# ── Workout Sessions ──────────────────────────────────────

class WorkoutSession(Base):
    __tablename__ = "workout_sessions"

    id            = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id       = Column(Integer, ForeignKey("users.id",         ondelete="CASCADE"),   nullable=False)
    plan_id       = Column(Integer, ForeignKey("workout_plans.id", ondelete="SET NULL"),  nullable=True)
    plan_day      = Column(SmallInteger, nullable=True)
    training_date = Column(Date, nullable=False)
    started_at    = Column(DateTime(timezone=True), nullable=False, default=func.now())
    ended_at      = Column(DateTime(timezone=True), nullable=True)
    notes         = Column(Text, nullable=True)

    user = relationship("Users", back_populates="sessions")
    plan = relationship("WorkoutPlan", back_populates="sessions")
    sets = relationship("WorkoutSet",  back_populates="session", cascade="all, delete-orphan")


# ── Workout Sets ──────────────────────────────────────────

class WorkoutSet(Base):
    __tablename__ = "workout_sets"

    id          = Column(BigInteger, primary_key=True, autoincrement=True)
    session_id  = Column(BigInteger, ForeignKey("workout_sessions.id", ondelete="CASCADE"),  nullable=False)
    exercise_id = Column(Integer,    ForeignKey("exercises.id",        ondelete="RESTRICT"), nullable=False)
    set_number  = Column(SmallInteger, nullable=False)
    weight_kg   = Column(Numeric(6, 2), nullable=True)
    reps        = Column(SmallInteger,  nullable=True)
    rpe         = Column(Numeric(3, 1), nullable=True)
    is_warmup   = Column(Boolean, nullable=False, default=False)
    is_dropset  = Column(Boolean, nullable=False, default=False)
    is_failure  = Column(Boolean, nullable=False, default=False)
    notes       = Column(Text, nullable=True)
    logged_at   = Column(DateTime(timezone=True), nullable=False, default=func.now())

    session  = relationship("WorkoutSession", back_populates="sets")
    exercise = relationship("Exercise",        back_populates="workout_sets")
