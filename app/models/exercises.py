import enum
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Enum,
    ForeignKey, Integer, Numeric, SmallInteger, String, Text, UniqueConstraint
)
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.sql import func
from app.db.connection import Base
from .enums import *

class Exercise(Base):
    __tablename__ = "exercises"

    id                = Column(Integer, primary_key=True, autoincrement=True)
    name              = Column(String(120), nullable=False, unique=True)
    primary_muscle    = Column(Enum(MuscleGroup, values_callable=lambda e: [i.value for i in e]), nullable=False)
    secondary_muscles = Column(String(255), nullable=True)
    equipment         = Column(Enum(Equipment, values_callable=lambda e: [i.value for i in e]), nullable=False, default=Equipment.bodyweight)
    difficulty        = Column(Enum(DifficultyLevel, values_callable=lambda e: [i.value for i in e]), nullable=False, default=DifficultyLevel.intermediate)
    is_bilateral      = Column(Boolean, nullable=False, default=True)
    description       = Column(Text, nullable=True)
    instructions      = Column(Text, nullable=True)
    is_active         = Column(Boolean, nullable=False, default=True)
    created_at        = Column(DateTime(timezone=True), server_default=func.now())

    plan_exercises = relationship("WorkoutPlanExercise", back_populates="exercise")
    workout_sets   = relationship("WorkoutSet",          back_populates="exercise")
