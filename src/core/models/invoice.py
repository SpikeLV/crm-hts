from datetime import datetime
from typing import TYPE_CHECKING, List
from core.models.base import Base
from sqlalchemy import String, Date, Integer, Numeric, ForeignKey, func, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .jupers import Jupers
    from .payment import Payment
    from .project import Project


class Invoice(Base):
    __tablename__ = "invoices"

    invoice_number: Mapped[str] = mapped_column(String(255), nullable=False)
    invoice_date: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    invoice_amount: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=True)
    invoice_payment_date: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    invoice_description: Mapped[str] = mapped_column(String(255), nullable=True)
    project_id: Mapped[int] = mapped_column(Integer, ForeignKey("projects.id"), nullable=False)
    jupers_id: Mapped[int] = mapped_column(Integer, ForeignKey("jupers.id"), nullable=False)

    # Relationship: Many invoices to one Jupers
    jupers: Mapped["Jupers"] = relationship("Jupers", back_populates="invoices")

    # Relationship: One invoice to many payments
    payments: Mapped[List["Payment"]] = relationship("Payment", back_populates="invoice")

    # Relationship: One invoice to one project
    project: Mapped["Project"] = relationship("Project", back_populates="invoices")