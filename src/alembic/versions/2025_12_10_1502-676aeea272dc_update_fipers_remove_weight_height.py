"""update fipers :: remove weight height

Revision ID: 676aeea272dc
Revises: dfb1f97c7559
Create Date: 2025-12-10 15:02:49.179362

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "676aeea272dc"
down_revision: Union[str, Sequence[str], None] = "dfb1f97c7559"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("fipers", "height")
    op.drop_column("fipers", "weight")


def downgrade() -> None:
    op.add_column(
        "fipers",
        sa.Column(
            "weight", mysql.INTEGER(), autoincrement=False, nullable=True
        ),
    )
    op.add_column(
        "fipers",
        sa.Column(
            "height", mysql.INTEGER(), autoincrement=False, nullable=True
        ),
    )
