"""update Invoice table, remove payment columns

Revision ID: da6610e0e2ab
Revises: 1c5f0fca9374
Create Date: 2025-12-17 08:28:34.761917

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "da6610e0e2ab"
down_revision: Union[str, Sequence[str], None] = "1c5f0fca9374"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_column("invoices", "invoice_payed_date")
    op.drop_column("invoices", "invoice_payed_amount")


def downgrade() -> None:
    op.add_column(
        "invoices",
        sa.Column(
            "invoice_payed_amount",
            mysql.DECIMAL(precision=10, scale=2),
            nullable=False,
        ),
    )
    op.add_column(
        "invoices", sa.Column("invoice_payed_date", sa.DATE(), nullable=False)
    )