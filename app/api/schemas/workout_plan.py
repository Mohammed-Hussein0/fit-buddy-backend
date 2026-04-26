from __future__ import annotations

import datetime
import decimal
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from app.models.enums import PlanGoal


# =============================================================================
# WORKOUT PLAN EXERCISE
# Defined first because WorkoutPlanResponse nests a list of these.
# =============================================================================

class WorkoutPlanExerciseBase(BaseModel):
    exercise_id: int
    day_order: int = Field(..., ge=1, le=7,
                           description="Which training day this exercise belongs to (1–7)")
    day_label: Optional[str] = Field(None, max_length=80,
                                     description="Human label, e.g. 'Push Day' or 'Monday'")
    position: int = Field(..., ge=1,
                          description="Order of this exercise within the day")
    prescribed_sets: Optional[int] = Field(None, ge=1, le=20)
    prescribed_reps: Optional[str] = Field(None, max_length=20,
                                           description="Free-form, e.g. '8-12' or '5x5'")
    prescribed_rpe: Optional[decimal.Decimal] = Field(None, ge=1, le=10, decimal_places=1)
    rest_seconds: Optional[int] = Field(None, ge=0, le=600)
    notes: Optional[str] = None


class WorkoutPlanExerciseCreate(WorkoutPlanExerciseBase):
    # plan_id comes from the URL path, not the body
    pass


class WorkoutPlanExerciseUpdate(BaseModel):
    exercise_id: Optional[int] = None
    day_order: Optional[int] = Field(None, ge=1, le=7)
    day_label: Optional[str] = Field(None, max_length=80)
    position: Optional[int] = Field(None, ge=1)
    prescribed_sets: Optional[int] = Field(None, ge=1, le=20)
    prescribed_reps: Optional[str] = Field(None, max_length=20)
    prescribed_rpe: Optional[decimal.Decimal] = Field(None, ge=1, le=10, decimal_places=1)
    rest_seconds: Optional[int] = Field(None, ge=0, le=600)
    notes: Optional[str] = None


class WorkoutPlanExerciseResponse(WorkoutPlanExerciseBase):
    id: int
    plan_id: int

    model_config = {"from_attributes": True}


# =============================================================================
# WORKOUT PLAN
# =============================================================================

class WorkoutPlanBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=120)
    description: Optional[str] = None
    goal: Optional[PlanGoal] = None
    duration_weeks: Optional[int] = Field(None, ge=1, le=52)
    days_per_week: Optional[int] = Field(None, ge=1, le=7)
    is_active: bool = True


class WorkoutPlanCreate(WorkoutPlanBase):
    # owner_id is injected server-side from the authenticated user
    pass


class WorkoutPlanUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=120)
    description: Optional[str] = None
    goal: Optional[PlanGoal] = None
    duration_weeks: Optional[int] = Field(None, ge=1, le=52)
    days_per_week: Optional[int] = Field(None, ge=1, le=7)
    is_active: Optional[bool] = None


class WorkoutPlanResponse(WorkoutPlanBase):
    id: int
    owner_id: Optional[int]           # None → official public plan
    is_public: bool = Field(False, description="True when owner_id is NULL (official plan)")
    created_at: datetime.datetime
    updated_at: Optional[datetime.datetime]
    exercises: list[WorkoutPlanExerciseResponse] = []

    @field_validator("is_public", mode="before")
    @classmethod
    def derive_is_public(cls, v, info):
        # Computed from owner_id; the ORM doesn't store this column
        return info.data.get("owner_id") is None

    model_config = {"from_attributes": True}


class WorkoutPlanListResponse(BaseModel):
    total: int
    items: list[WorkoutPlanResponse]
