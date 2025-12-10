from datetime import date
from core.models.base import Base
from core.column_types import EncryptedString
from sqlalchemy import Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Jupers(Base):
    __tablename__ = "jupers"
        
    name: Mapped[str] = mapped_column(EncryptedString(255), nullable=False)
    reg_nr: Mapped[str] = mapped_column(EncryptedString(255), nullable=False)
    type: Mapped[str] = mapped_column(String(255), nullable=False)
    address: Mapped[str] = mapped_column(String(255), nullable=True)
    city: Mapped[str] = mapped_column(String(255), nullable=True)
    state: Mapped[str] = mapped_column(String(255), nullable=True)
    zip: Mapped[str] = mapped_column(String(255), nullable=True)
    country: Mapped[str] = mapped_column(String(255), nullable=True)
    phone: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)
    website: Mapped[str] = mapped_column(String(255), nullable=True)
    notes: Mapped[str] = mapped_column(String(255), nullable=True)
