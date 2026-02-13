from pydantic import BaseModel, Field
from typing import Optional
from datetime import date, datetime
from uuid import UUID
import enum


class GenderEnum(str, enum.Enum):
    male = "male"
    female = "female"


class ThemeEnum(str, enum.Enum):
    light = "light"
    dark = "dark"


class WeightUnitEnum(str, enum.Enum):
    kg = "kg"
    lbs = "lbs"


class HeightUnitEnum(str, enum.Enum):
    cm = "cm"
    feet = "feet"


class SubscriptionPlanEnum(str, enum.Enum):
    free = "free"
    paid = "paid"


class UserProfileUpdate(BaseModel):
    username: Optional[str] = None
    birth_date: Optional[date] = None
    gender: Optional[GenderEnum] = None
    height: Optional[int] = None
    weight: Optional[int] = None
    goal_weight: Optional[int] = None
    preferred_theme: Optional[ThemeEnum] = None
    preferred_weight_unit: Optional[WeightUnitEnum] = None
    preferred_height_unit: Optional[HeightUnitEnum] = None
    subscription_plan: Optional[SubscriptionPlanEnum] = None

    class Config:
        from_attributes = True
        extra = "forbid"

#-------------------------------------------------------------------------------------------------------

class UserProfileResponse(BaseModel):
    id: int
    username: str
    birth_date: date
    gender: GenderEnum
    height: int
    weight: int
    goal_weight: int
    preferred_theme: ThemeEnum
    preferred_weight_unit: WeightUnitEnum
    preferred_height_unit: HeightUnitEnum
    subscription_plan: SubscriptionPlanEnum
    bmi: float
    bmr: float
    age: int
    created_at: datetime
    modified_at: datetime

    class Config:
        from_attributes = True

###############################################################################

class UserProfileCreate(BaseModel):
    username: str = Field(None, max_length=20)
    birth_date: date
    gender: GenderEnum
    height: int
    weight: int
    goal_weight: int
    preferred_theme: ThemeEnum
    preferred_weight_unit: WeightUnitEnum
    preferred_height_unit: HeightUnitEnum
    subscription_plan: SubscriptionPlanEnum

    class Config:
        from_attributes = True