from __future__ import annotations

# =============================================================================
# Read-only schemas for public catalogue browsing
#
# These are used by routes that let any authenticated user browse the shared
# exercise library and official workout plans (owner_id IS NULL).
# No Create/Update schemas here — this data is managed by admins, not users.
# =============================================================================

import datetime
import decimal
from typing import Optional

from pydantic import BaseModel, Field

from app.models.enums import (
    DifficultyLevel,
    Equipment,
    MuscleGroup,
    PlanGoal,
)


# =============================================================================
# EXERCISE
# Read-only. Users pick exercises from this shared library when logging sets
# or building their own workout plans.
# =============================================================================

class ExerciseResponse(BaseModel):
    id: int
    name: str
    primary_muscle: MuscleGroup
    secondary_muscles: Optional[str] = Field(None,
        description="Comma-separated secondary muscle groups (raw string from DB)")
    equipment: Equipment
    difficulty: DifficultyLevel
    is_bilateral: bool = Field(...,
        description="True if the movement works both sides simultaneously (e.g. barbell curl vs. single-arm)")
    description: Optional[str] = None
    instructions: Optional[str] = None
    created_at: datetime.datetime

    model_config = {"from_attributes": True}


class ExerciseListResponse(BaseModel):
    total: int
    items: list[ExerciseResponse]


# =============================================================================
# OFFICIAL WORKOUT PLAN  (owner_id IS NULL)
# Read-only. Returned when a user browses the built-in plan catalogue.
# Shares the same DB table as user plans but exposed through a separate schema
# to make the "official / read-only" intent explicit in the API contract.
# =============================================================================

class OfficialPlanExerciseResponse(BaseModel):
    """A single exercise slot inside an official plan (flattened for readability)."""
    id: int
    exercise_id: int
    exercise_name: str          # joined from exercises.name for convenience
    primary_muscle: MuscleGroup # joined from exercises.primary_muscle
    day_order: int
    day_label: Optional[str] = None
    position: int
    prescribed_sets: Optional[int] = None
    prescribed_reps: Optional[str] = None
    prescribed_rpe: Optional[decimal.Decimal] = None
    rest_seconds: Optional[int] = None
    notes: Optional[str] = None

    model_config = {"from_attributes": True}


class OfficialPlanResponse(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    goal: Optional[PlanGoal] = None
    duration_weeks: Optional[int] = None
    days_per_week: Optional[int] = None
    created_at: datetime.datetime
    exercises: list[OfficialPlanExerciseResponse] = []

    model_config = {"from_attributes": True}


class OfficialPlanListResponse(BaseModel):
    total: int
    items: list[OfficialPlanResponse]
