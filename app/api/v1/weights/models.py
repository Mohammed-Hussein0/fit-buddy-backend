from datetime import datetime
from sqlalchemy import (
    ForeignKey, DateTime, Numeric,
    UniqueConstraint, CheckConstraint,
    text
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.config.db import Base

class Weights(Base):
    __tablename__ = "weight_logs"

    __table_args__ = (
        UniqueConstraint("user_id", "timestamp", name="uq_user_timestamp"),
        CheckConstraint('weight > 30::numeric AND weight <= 800::numeric', name='weight_valid'),
    )

    id: Mapped[int] = mapped_column(primary_key=True, index=True)

    user_id: Mapped[int] = mapped_column(
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    weight: Mapped[float] = mapped_column(Numeric(5, 2), nullable=False)

    timestamp: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text('CURRENT_TIMESTAMP'),
        nullable=False,
        index=True
    )

    user = relationship("Users", back_populates="weight_logs")