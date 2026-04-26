from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from typing import Optional

from pydantic import BaseModel

from app.models.enums import (
    GenderEnum,
    HeightUnitEnum,
    SubscriptionPlanEnum,
    ThemeEnum,
    WeightUnitEnum,
)
from .common import HeightType, UsernameType, WeightType


class UserProfileCreate(BaseModel):
    username:              UsernameType
    birth_date:            date
    gender:                GenderEnum
    height:                HeightType
    weight:                WeightType
    goal_weight:           WeightType
    preferred_theme:       ThemeEnum
    preferred_weight_unit: WeightUnitEnum
    preferred_height_unit: HeightUnitEnum
    subscription_plan:     SubscriptionPlanEnum

    model_config = {"from_attributes": True}


class UserProfileUpdate(BaseModel):
    # All fields optional for partial PATCH. extra="forbid" rejects unknown fields.
    username:              Optional[UsernameType]         = None
    birth_date:            Optional[date]                 = None
    gender:                Optional[GenderEnum]           = None
    height:                Optional[HeightType]           = None
    weight:                Optional[WeightType]           = None
    goal_weight:           Optional[WeightType]           = None
    preferred_theme:       Optional[ThemeEnum]            = None
    preferred_weight_unit: Optional[WeightUnitEnum]       = None
    preferred_height_unit: Optional[HeightUnitEnum]       = None
    subscription_plan:     Optional[SubscriptionPlanEnum] = None

    model_config = {"from_attributes": True, "extra": "forbid"}


class UserProfileResponse(BaseModel):
    # bmi, bmr, age are computed server-side (DB trigger / computed column) — read-only
    id:                    int
    username:              str
    birth_date:            date
    gender:                GenderEnum
    height:                Decimal
    weight:                Decimal
    goal_weight:           Decimal
    preferred_theme:       ThemeEnum
    preferred_weight_unit: WeightUnitEnum
    preferred_height_unit: HeightUnitEnum
    subscription_plan:     SubscriptionPlanEnum
    bmi:                   Decimal
    bmr:                   Decimal
    age:                   int
    created_at:            datetime
    modified_at:           datetime

    model_config = {"from_attributes": True}