import enum
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Enum,
    ForeignKey, Integer, Numeric, SmallInteger, String, Text, UniqueConstraint
)
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import func
from app.db.connection import Base
from .enums import *

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
    created_at     = Column(DateTime(timezone=True), server_default=func.now())
    updated_at     = Column(DateTime(timezone=True), nullable=True)  # maintained by trigger

    owner     = relationship("Users",                back_populates="plans")
    exercises = relationship("WorkoutPlanExercise", back_populates="plan",
                             cascade="all, delete-orphan",
                             order_by="WorkoutPlanExercise.day_order, WorkoutPlanExercise.position")
    sessions  = relationship("WorkoutSession",      back_populates="plan")