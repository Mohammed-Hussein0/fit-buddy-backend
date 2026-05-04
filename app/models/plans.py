import enum
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Enum,
    ForeignKey, Integer, Numeric, SmallInteger, String, Text, UniqueConstraint
)
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy.sql import func
from app.db.connection import Base
from datetime import datetime
from .enums import *

# ── Workout Plans ─────────────────────────────────────────

class WorkoutPlan(Base):
    __tablename__ = "workout_plans"

    id             = Column(Integer, primary_key=True, autoincrement=True)
    owner_id       = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    name           = Column(String(120), nullable=False)
    description    = Column(Text,        nullable=True)
    goal           = Column(Enum(PlanGoal, values_callable=lambda e: [i.value for i in e]), nullable=True)
    duration_weeks = Column(SmallInteger,   nullable=True)
    days_per_week  = Column(SmallInteger,   nullable=True)
    is_active      = Column(Boolean, nullable=False, default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    modified_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)  # maintained by trigger

    owner     = relationship("Users",                back_populates="plans")
    exercises = relationship("WorkoutPlanExercise", back_populates="plan",
                             cascade="all, delete-orphan",
                             order_by="WorkoutPlanExercise.day_order, WorkoutPlanExercise.position")

# ── Workout PLan Exercises ──────────────────────────────────

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