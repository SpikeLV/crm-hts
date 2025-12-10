"""update jupers type field

Revision ID: fbae5a753ad5
Revises: ad7c9ebda058
Create Date: 2025-12-10 16:07:15.536499

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "fbae5a753ad5"
down_revision: Union[str, Sequence[str], None] = "ad7c9ebda058"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("jupers", "type")


def downgrade() -> None:
    op.add_column(
        "jupers", sa.Column("type", mysql.VARCHAR(length=255), nullable=False)
    )
