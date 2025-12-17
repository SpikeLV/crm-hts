from datetime import datetime
from typing import TYPE_CHECKING    
from core.models.base import Base
from sqlalchemy import String, Date, Integer, Numeric, ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .invoice import Invoice

class Payment(Base):
    __tablename__ = "payments"

    amount: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    invoice_id: Mapped[int] = mapped_column(Integer, ForeignKey("invoices.id"), nullable=False)

    # Relationship: Many payments to one invoice
    invoice: Mapped["Invoice"] = relationship("Invoice", back_populates="payments")