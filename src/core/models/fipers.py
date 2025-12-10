from datetime import date
from core.models.base import Base
from core.column_types import EncryptedString
from sqlalchemy import Date, String, Integer
from sqlalchemy.orm import Mapped, mapped_column


class Fipers(Base):
    __tablename__ = "fipers"
    
    first_name: Mapped[str] = mapped_column(EncryptedString(255), nullable=False)
    last_name: Mapped[str] = mapped_column(EncryptedString(255), nullable=False)
    ssn: Mapped[str] = mapped_column(EncryptedString(255), nullable=True)
    
    # Non-encrypted fields (less sensitive or required for indexing)
    gender: Mapped[str] = mapped_column(String(255), nullable=True)
    birth_date: Mapped[date] = mapped_column(Date, nullable=True)
    
    phone: Mapped[str] = mapped_column(String(255), nullable=True)
    email: Mapped[str] = mapped_column(String(255), nullable=True)

    address: Mapped[str] = mapped_column(String(255), nullable=True)