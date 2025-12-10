"""create user jupers

Revision ID: dfb1f97c7559
Revises: b288ca8d431e
Create Date: 2025-12-10 14:00:18.741050

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from core.column_types import EncryptedString

# revision identifiers, used by Alembic.
revision: str = "dfb1f97c7559"
down_revision: Union[str, Sequence[str], None] = "b288ca8d431e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "jupers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "name",
            EncryptedString(length=255),
            nullable=False,
        ),
        sa.Column(
            "reg_nr",
            EncryptedString(length=255),
            nullable=False,
        ),
        sa.Column("type", sa.String(length=255), nullable=False),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("city", sa.String(length=255), nullable=True),
        sa.Column("state", sa.String(length=255), nullable=True),
        sa.Column("zip", sa.String(length=255), nullable=True),
        sa.Column("country", sa.String(length=255), nullable=True),
        sa.Column("phone", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("website", sa.String(length=255), nullable=True),
        sa.Column("notes", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_jupers")),
    )


def downgrade() -> None:
    op.drop_table("jupers")
