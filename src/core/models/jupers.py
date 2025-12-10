from datetime import date
from typing import List, TYPE_CHECKING
from core.models.base import Base
from core.column_types import EncryptedString
from sqlalchemy import Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship

if TYPE_CHECKING:
    from .invoice import Invoice


class Jupers(Base):
    __tablename__ = "jupers"
        
    name: Mapped[str] = mapped_column(EncryptedString(255), nullable=False)
    reg_nr: Mapped[str] = mapped_column(EncryptedString(255), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=True)
    phone: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    notes: Mapped[str] = mapped_column(String(255), nullable=True)

    # Relationship: One Jupers to many Invoices
    invoices: Mapped[List["Invoice"]] = relationship("Invoice", back_populates="jupers")
