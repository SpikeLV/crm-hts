"""add foreign key  payment to invoice

Revision ID: 72b23d041199
Revises: a712ba9aec89
Create Date: 2025-12-17 09:07:06.454972

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "72b23d041199"
down_revision: Union[str, Sequence[str], None] = "a712ba9aec89"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column(
        "invoices",
        "invoice_amount",
        existing_type=mysql.DECIMAL(precision=10, scale=2),
        nullable=True,
    )
    op.alter_column(
        "invoices",
        "invoice_payment_date",
        existing_type=sa.DATE(),
        nullable=True,
    )
    op.alter_column(
        "invoices",
        "invoice_description",
        existing_type=mysql.VARCHAR(length=255),
        nullable=True,
    )


def downgrade() -> None:
    op.alter_column(
        "invoices",
        "invoice_description",
        existing_type=mysql.VARCHAR(length=255),
        nullable=False,
    )
    op.alter_column(
        "invoices",
        "invoice_payment_date",
        existing_type=sa.DATE(),
        nullable=False,
    )
    op.alter_column(
        "invoices",
        "invoice_amount",
        existing_type=mysql.DECIMAL(precision=10, scale=2),
        nullable=False,
    )
