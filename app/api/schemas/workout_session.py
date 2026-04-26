from __future__ import annotations

import datetime
from typing import Optional

from pydantic import BaseModel, Field

from .workout_set import WorkoutSetResponse


class WorkoutSessionBase(BaseModel):
    training_date: datetime.date = Field(..., description="The calendar date of the workout")
    plan_id: Optional[int] = Field(None,
        description="Optional plan this session follows. May be user's own or a public plan.")
    plan_day: Optional[int] = Field(None, ge=1, le=7,
        description="Which day of the plan is being followed today")
    notes: Optional[str] = None


class WorkoutSessionCreate(WorkoutSessionBase):
    # started_at defaults to now() server-side
    pass


class WorkoutSessionUpdate(BaseModel):
    training_date: Optional[datetime.date] = None
    plan_id: Optional[int] = None
    plan_day: Optional[int] = Field(None, ge=1, le=7)
    notes: Optional[str] = None
    # ended_at is NOT here — use the dedicated /end endpoint


class WorkoutSessionResponse(WorkoutSessionBase):
    id: int
    user_id: int
    started_at: datetime.datetime
    ended_at: Optional[datetime.datetime] = None
    sets: list[WorkoutSetResponse] = []

    model_config = {"from_attributes": True}


class WorkoutSessionListResponse(BaseModel):
    total: int
    items: list[WorkoutSessionResponse]
