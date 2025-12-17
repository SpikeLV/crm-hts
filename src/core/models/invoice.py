from datetime import date
from typing import TYPE_CHECKING, List
from core.models.base import Base
from sqlalchemy import String, Date, Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .jupers import Jupers
    from .payment import Payment


class Invoice(Base):
    __tablename__ = "invoices"

    invoice_number: Mapped[str] = mapped_column(String(255), nullable=False)
    invoice_date: Mapped[date] = mapped_column(Date, nullable=False)
    invoice_amount: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=False)
    invoice_payment_date: Mapped[date] = mapped_column(Date, nullable=False)
    invoice_description: Mapped[str] = mapped_column(String(255), nullable=False)
    project_id: Mapped[int] = mapped_column(Integer, nullable=False)
    jupers_id: Mapped[int] = mapped_column(Integer, ForeignKey("jupers.id"), nullable=False)

    # Relationship: Many invoices to one Jupers
    jupers: Mapped["Jupers"] = relationship("Jupers", back_populates="invoices")

    # Relationship: One invoice to many payments
    payments: Mapped[List["Payment"]] = relationship("Payment", back_populates="invoice")