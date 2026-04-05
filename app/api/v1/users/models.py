from typing import Optional
import datetime
import decimal
from app.api.v1.users.enums import *
import uuid

from sqlalchemy import BigInteger, Boolean, CheckConstraint, Column, Computed, Date, DateTime, Double, Enum, ForeignKeyConstraint, Identity, Index, Numeric, PrimaryKeyConstraint, SmallInteger, String, Table, Text, UniqueConstraint, Uuid, text
from sqlalchemy.dialects.postgresql import JSONB, OID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

from app.config.db import Base


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        CheckConstraint('age >= 6 AND age <= 150', name='age_valid'),
        CheckConstraint('goal_weight > 40::numeric AND goal_weight <= 200::numeric', name='goal_weight_valid'),
        CheckConstraint('height > 100::numeric AND height <= 300::numeric', name='height_valid'),
        CheckConstraint('weight > 30::numeric AND weight <= 800::numeric', name='weight_valid'),
    )

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    username: Mapped[str] = mapped_column(String(20), nullable=False)

    birth_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)

    gender: Mapped[GenderEnum] = mapped_column(Enum(GenderEnum, name = 'gender_enum'), nullable=False)

    height: Mapped[decimal.Decimal] = mapped_column(Numeric(4, 1), nullable=False)

    weight: Mapped[decimal.Decimal] = mapped_column(Numeric(4, 1), nullable=False)

    goal_weight: Mapped[decimal.Decimal] = mapped_column(Numeric(4, 1), nullable=False)

    preferred_theme: Mapped[ThemeEnum] = mapped_column(Enum(ThemeEnum, name = 'theme_enum'), nullable=False)

    preferred_weight_unit: Mapped[WeightUnitEnum] = mapped_column(Enum(WeightUnitEnum, name='weight_unit_enum'), nullable=False)

    preferred_height_unit: Mapped[HeightUnitEnum] = mapped_column(Enum(HeightUnitEnum, name='height_unit_enum'), nullable=False)

    subscription_plan: Mapped[SubscriptionPlanEnum] = mapped_column(Enum(SubscriptionPlanEnum, name='subscription_plan_enum'), nullable=False)

    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    modified_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text('CURRENT_TIMESTAMP'))

    bmi: Mapped[decimal.Decimal] = mapped_column(Numeric, nullable=False)

    bmr: Mapped[decimal.Decimal] = mapped_column(Numeric, nullable=False)

    age: Mapped[int] = mapped_column(SmallInteger, nullable=False)
    
    auth_id: Mapped[uuid.UUID] = mapped_column(Uuid, unique=True, nullable=False)

    weight_logs: Mapped[list["Weights"]] = relationship(
        back_populates="user"
    )    