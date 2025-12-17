"""add index to invoice and jupers

Revision ID: 1c5f0fca9374
Revises: e6a9027b8f08
Create Date: 2025-12-10 16:30:35.790218

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1c5f0fca9374"
down_revision: Union[str, Sequence[str], None] = "e6a9027b8f08"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "invoices",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("invoice_number", sa.String(length=255), nullable=False),
        sa.Column("invoice_date", sa.Date(), nullable=False),
        sa.Column(
            "invoice_amount", sa.Numeric(precision=10, scale=2), nullable=False
        ),
        sa.Column("invoice_payment_date", sa.Date(), nullable=False),
        sa.Column(
            "invoice_payed_amount",
            sa.Numeric(precision=10, scale=2),
            nullable=False,
        ),
        sa.Column("invoice_payed_date", sa.Date(), nullable=False),
        sa.Column(
            "invoice_description", sa.String(length=255), nullable=False
        ),
        sa.Column("project_id", sa.Integer(), nullable=False),
        sa.Column("jupers_id", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(
            ["jupers_id"],
            ["jupers.id"],
            name=op.f("fk_invoices_jupers_id_jupers"),
        ),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_invoices")),
    )


def downgrade() -> None:
    op.drop_table("invoices")
