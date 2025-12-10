from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, DateTime, MetaData
from datetime import datetime
from core.config import settings

class Base(DeclarativeBase):
    __abstract__ = True
    metadata = MetaData(
        naming_convention=settings.db.naming_convention
    )
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now, onupdate=datetime.now, nullable=True)
    deleted_at: Mapped[datetime] = mapped_column(DateTime, default=None, nullable=True)