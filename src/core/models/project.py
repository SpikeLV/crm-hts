from core.models.base import Base
from sqlalchemy import String, Numeric
from sqlalchemy.orm import Mapped, mapped_column


class Project(Base):
    __tablename__ = "projects"

    project_code: Mapped[str] = mapped_column(String(255), nullable=False)
    project_status: Mapped[str] = mapped_column(String(255), nullable=True)
    project_budget: Mapped[float] = mapped_column(Numeric(precision=10, scale=2), nullable=True)
    project_description: Mapped[str] = mapped_column(String(255), nullable=True)

