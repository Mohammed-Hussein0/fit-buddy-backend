from decimal import Decimal
from datetime import date, datetime
from typing import Annotated, Optional

from pydantic import BaseModel, ConfigDict, Field
from app.models.enums import *

HeightType    = Annotated[Decimal, Field(gt=0, max_digits=4, decimal_places=1)]
WeightType    = Annotated[Decimal, Field(gt=0, max_digits=5, decimal_places=2)]
UsernameType  = Annotated[str,     Field(min_length=3, max_length=20)]

class UserProfileCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    username:               UsernameType
    birth_date:             date
    gender:                 GenderEnum
    height:                 HeightType
    weight:                 WeightType
    goal_weight:            WeightType
    preferred_theme:        ThemeEnum
    preferred_weight_unit:  WeightUnitEnum
    preferred_height_unit:  HeightUnitEnum
    subscription_plan:      SubscriptionPlanEnum


class UserProfileUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True, extra="forbid")

    username:               Optional[UsernameType]          = None
    birth_date:             Optional[date]                  = None
    gender:                 Optional[GenderEnum]            = None
    height:                 Optional[HeightType]            = None
    weight:                 Optional[WeightType]            = None
    goal_weight:            Optional[WeightType]            = None
    preferred_theme:        Optional[ThemeEnum]             = None
    preferred_weight_unit:  Optional[WeightUnitEnum]        = None
    preferred_height_unit:  Optional[HeightUnitEnum]        = None
    subscription_plan:      Optional[SubscriptionPlanEnum]  = None


class UserProfileResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id:                     int
    username:               str
    birth_date:             date
    gender:                 GenderEnum
    height:                 Decimal
    weight:                 Decimal
    goal_weight:            Decimal
    preferred_theme:        ThemeEnum
    preferred_weight_unit:  WeightUnitEnum
    preferred_height_unit:  HeightUnitEnum
    subscription_plan:      SubscriptionPlanEnum
    bmi:                    Decimal
    bmr:                    Decimal
    age:                    int
    created_at:             datetime
    modified_at:            datetime