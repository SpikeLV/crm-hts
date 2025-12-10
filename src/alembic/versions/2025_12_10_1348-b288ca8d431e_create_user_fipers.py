"""create user fipers

Revision ID: b288ca8d431e
Revises: f1bca90c0bed
Create Date: 2025-12-10 13:48:13.604401

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from core.column_types import EncryptedString


# revision identifiers, used by Alembic.
revision: str = "b288ca8d431e"
down_revision: Union[str, Sequence[str], None] = "f1bca90c0bed"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "fipers",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "first_name",
            EncryptedString(length=255),
            nullable=False,
        ),
        sa.Column(
            "last_name",
            EncryptedString(length=255),
            nullable=False,
        ),
        sa.Column(
            "ssn", EncryptedString(length=255), nullable=True
        ),
        sa.Column("middle_name", sa.String(length=255), nullable=True),
        sa.Column("gender", sa.String(length=255), nullable=True),
        sa.Column("birth_date", sa.Date(), nullable=True),
        sa.Column("height", sa.Integer(), nullable=True),
        sa.Column("weight", sa.Integer(), nullable=True),
        sa.Column("phone", sa.String(length=255), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("address", sa.String(length=255), nullable=True),
        sa.Column("city", sa.String(length=255), nullable=True),
        sa.Column("state", sa.String(length=255), nullable=True),
        sa.Column("zip", sa.String(length=255), nullable=True),
        sa.Column("country", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_fipers")),
    )


def downgrade() -> None:
    op.drop_table("fipers")
