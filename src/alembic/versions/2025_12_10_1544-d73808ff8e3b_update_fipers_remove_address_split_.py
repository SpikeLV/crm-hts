"""update fipers remove address split fields

Revision ID: d73808ff8e3b
Revises: 676aeea272dc
Create Date: 2025-12-10 15:44:16.652057

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "d73808ff8e3b"
down_revision: Union[str, Sequence[str], None] = "676aeea272dc"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("fipers", "zip")
    op.drop_column("fipers", "middle_name")
    op.drop_column("fipers", "city")
    op.drop_column("fipers", "country")
    op.drop_column("fipers", "state")


def downgrade() -> None:
    op.add_column(
        "fipers", sa.Column("state", mysql.VARCHAR(length=255), nullable=True)
    )
    op.add_column(
        "fipers",
        sa.Column("country", mysql.VARCHAR(length=255), nullable=True),
    )
    op.add_column(
        "fipers", sa.Column("city", mysql.VARCHAR(length=255), nullable=True)
    )
    op.add_column(
        "fipers",
        sa.Column("middle_name", mysql.VARCHAR(length=255), nullable=True),
    )
    op.add_column(
        "fipers", sa.Column("zip", mysql.VARCHAR(length=255), nullable=True)
    )
