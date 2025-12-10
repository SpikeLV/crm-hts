"""update jupers remove address split fields

Revision ID: ad7c9ebda058
Revises: d73808ff8e3b
Create Date: 2025-12-10 16:00:14.959438

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "ad7c9ebda058"
down_revision: Union[str, Sequence[str], None] = "d73808ff8e3b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("jupers", "website")
    op.drop_column("jupers", "state")
    op.drop_column("jupers", "zip")
    op.drop_column("jupers", "city")
    op.drop_column("jupers", "country")


def downgrade() -> None:
    op.add_column(
        "jupers",
        sa.Column("country", mysql.VARCHAR(length=255), nullable=True),
    )
    op.add_column(
        "jupers", sa.Column("city", mysql.VARCHAR(length=255), nullable=True)
    )
    op.add_column(
        "jupers", sa.Column("zip", mysql.VARCHAR(length=255), nullable=True)
    )
    op.add_column(
        "jupers", sa.Column("state", mysql.VARCHAR(length=255), nullable=True)
    )
    op.add_column(
        "jupers",
        sa.Column("website", mysql.VARCHAR(length=255), nullable=True),
    )
