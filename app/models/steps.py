from typing import Optional
import datetime
from sqlalchemy import BigInteger, ForeignKey, Numeric, Integer, DateTime, text, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.connection import Base



class Steps(Base):
    __tablename__ = "steps"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)

    user_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    duration_secs: Mapped[int] = mapped_column(Integer, nullable=False)
    distance_m: Mapped[float] = mapped_column(Numeric(10, 2), nullable=False)
    steps: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), nullable=False, server_default=text("CURRENT_TIMESTAMP"))

    user: Mapped["Users"] = relationship("Users", back_populates="steps_logs")