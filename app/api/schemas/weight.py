from __future__ import annotations

import datetime
import decimal
from typing import Optional

from pydantic import BaseModel, Field


class WeightLogBase(BaseModel):
    weight_kg: decimal.Decimal = Field(..., gt=30, le=800, decimal_places=2,
                                       description="Body weight in kilograms")
    body_fat_pct: Optional[decimal.Decimal] = Field(None, ge=0, le=100, decimal_places=1)
    muscle_mass_kg: Optional[decimal.Decimal] = Field(None, gt=0, le=500, decimal_places=2)
    water_pct: Optional[decimal.Decimal] = Field(None, ge=0, le=100, decimal_places=1)
    visceral_fat: Optional[int] = Field(None, ge=1, le=59,
                                        description="Visceral fat level (1–59 scale)")
    notes: Optional[str] = Field(None, max_length=1000)
    logged_at: Optional[datetime.datetime] = Field(
        None,
        description="When the measurement was taken. Defaults to now() if omitted."
    )


class WeightLogCreate(WeightLogBase):
    pass


class WeightLogUpdate(BaseModel):
    weight_kg: Optional[decimal.Decimal] = Field(None, gt=30, le=800, decimal_places=2)
    body_fat_pct: Optional[decimal.Decimal] = Field(None, ge=0, le=100, decimal_places=1)
    muscle_mass_kg: Optional[decimal.Decimal] = Field(None, gt=0, le=500, decimal_places=2)
    water_pct: Optional[decimal.Decimal] = Field(None, ge=0, le=100, decimal_places=1)
    visceral_fat: Optional[int] = Field(None, ge=1, le=59)
    notes: Optional[str] = Field(None, max_length=1000)
    logged_at: Optional[datetime.datetime] = None


class WeightLogResponse(WeightLogBase):
    id: int
    user_id: int
    logged_at: datetime.datetime
    created_at: datetime.datetime

    model_config = {"from_attributes": True}


class WeightLogListResponse(BaseModel):
    total: int
    items: list[WeightLogResponse]
