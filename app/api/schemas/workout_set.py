from __future__ import annotations

import datetime
import decimal
from typing import Optional

from pydantic import BaseModel, Field


class WorkoutSetBase(BaseModel):
    exercise_id: int = Field(...,
        description="Must exist in the exercises table (public, not user-scoped)")
    set_number: int = Field(..., ge=1, le=99)
    weight_kg: Optional[decimal.Decimal] = Field(None, ge=0, le=1000, decimal_places=2,
        description="Load lifted. Null for bodyweight-only sets.")
    reps: Optional[int] = Field(None, ge=0, le=999,
        description="Reps completed. Null for time-based sets.")
    rpe: Optional[decimal.Decimal] = Field(None, ge=1, le=10, decimal_places=1,
        description="Rate of Perceived Exertion (1.0 – 10.0)")
    is_warmup: bool = False
    is_dropset: bool = False
    is_failure: bool = Field(False, description="True if the set was taken to failure")
    notes: Optional[str] = None


class WorkoutSetCreate(WorkoutSetBase):
    # session_id comes from the URL path, not the body
    # logged_at defaults to now() server-side
    pass


class WorkoutSetUpdate(BaseModel):
    exercise_id: Optional[int] = None
    set_number: Optional[int] = Field(None, ge=1, le=99)
    weight_kg: Optional[decimal.Decimal] = Field(None, ge=0, le=1000, decimal_places=2)
    reps: Optional[int] = Field(None, ge=0, le=999)
    rpe: Optional[decimal.Decimal] = Field(None, ge=1, le=10, decimal_places=1)
    is_warmup: Optional[bool] = None
    is_dropset: Optional[bool] = None
    is_failure: Optional[bool] = None
    notes: Optional[str] = None


class WorkoutSetResponse(WorkoutSetBase):
    id: int
    session_id: int
    logged_at: datetime.datetime

    model_config = {"from_attributes": True}
