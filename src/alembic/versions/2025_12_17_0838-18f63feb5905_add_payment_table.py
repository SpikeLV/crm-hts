"""add payment table

Revision ID: 18f63feb5905
Revises: da6610e0e2ab
Create Date: 2025-12-17 08:38:50.639078

"""

from typing import Sequence, Union

from alembic import op
from pydantic.deprecated.tools import T
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "18f63feb5905"
down_revision: Union[str, Sequence[str], None] = "da6610e0e2ab"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "payments",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("amount", sa.Numeric(precision=10, scale=2), nullable=False),
        sa.Column("date", sa.Date(), nullable=False),
        sa.Column("description", sa.String(length=255), nullable=True),
        sa.Column("invoice_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_payments")),
    )


def downgrade() -> None:
    op.drop_table("payments")
