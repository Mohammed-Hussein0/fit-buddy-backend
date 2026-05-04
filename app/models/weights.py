import enum
from sqlalchemy import (
    BigInteger, Boolean, Column, Date, DateTime, Enum,
    ForeignKey, Integer, Numeric, SmallInteger, String, Text, UniqueConstraint,
)
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from sqlalchemy.sql import func
from app.db.connection import Base
import datetime

class WeightLog(Base):
    __tablename__ = "weight_logs"

    id             = Column(BigInteger, primary_key=True, autoincrement=True)
    user_id        = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    weight_kg      = Column(Numeric(5, 2), nullable=False)
    body_fat_pct   = Column(Numeric(4, 1), nullable=True)
    muscle_mass_kg = Column(Numeric(5, 2), nullable=True)
    water_pct      = Column(Numeric(4, 1), nullable=True)
    visceral_fat   = Column(SmallInteger,  nullable=True)
    notes          = Column(Text,          nullable=True)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=func.now())
    modified_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    user = relationship("Users", back_populates="weight_logs")
