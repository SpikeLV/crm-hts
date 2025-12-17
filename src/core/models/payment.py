from datetime import date
from typing import TYPE_CHECKING
from core.models.base import Base
from sqlalchemy import String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .invoice import Invoice

class Payment(Base):
    __tablename__ = "payments"

    amount: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    date: Mapped[date] = mapped_column(Date, nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=False)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"), nullable=False)

    # Relationship: Many payments to one invoice
    invoice: Mapped["Invoice"] = relationship("Invoice", back_populates="payments")