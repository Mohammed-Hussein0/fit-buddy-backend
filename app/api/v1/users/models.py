import enum
from sqlalchemy import (
    BigInteger, SmallInteger, Integer, String,
    Date, DateTime, Numeric, ForeignKey, func
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID, ENUM


class Base(DeclarativeBase):
    pass


class GenderEnum(enum.Enum):
    male = "male"
    female = "female"


class ThemeEnum(enum.Enum):
    light = "light"
    dark = "dark"


class WeightUnitEnum(enum.Enum):
    kg = "kg"
    lbs = "lbs"


class HeightUnitEnum(enum.Enum):
    cm = "cm"
    feet = "feet"


class SubscriptionPlanEnum(enum.Enum):
    free = "free"
    premium = "premium"

# ------------------------------------------------------------------------------------------------------------------------------------

class UserProfile(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    username: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    birth_date: Mapped[Date] = mapped_column(
        Date,
        nullable=False
    )

    gender: Mapped[GenderEnum] = mapped_column(
        ENUM(GenderEnum, name="gender_enum"),
        nullable=False
    )

    height: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )

    weight: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )

    goal_weight: Mapped[int] = mapped_column(
        SmallInteger,
        nullable=False
    )

    preferred_theme: Mapped[ThemeEnum] = mapped_column(
        ENUM(ThemeEnum, name="theme_enum"),
        nullable=False
    )

    preferred_weight_unit: Mapped[WeightUnitEnum] = mapped_column(
        ENUM(WeightUnitEnum, name="weight_unit_enum"),
        nullable=False
    )

    preferred_height_unit: Mapped[HeightUnitEnum] = mapped_column(
        ENUM(HeightUnitEnum, name="height_unit_enum"),
        nullable=False
    )

    subscription_plan: Mapped[SubscriptionPlanEnum] = mapped_column(
        ENUM(SubscriptionPlanEnum, name="subscription_plan_enum"),
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    modified_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )

    bmi: Mapped[float] = mapped_column(
        Numeric,
        nullable=False
    )

    bmr: Mapped[float] = mapped_column(
        Numeric,
        nullable=False
    )

    age: Mapped[int] = mapped_column(
        Integer,
        nullable=False
    )

    auth_id: Mapped[str] = mapped_column(
        UUID(as_uuid=True), 
        unique=True, 
        index=True
    )