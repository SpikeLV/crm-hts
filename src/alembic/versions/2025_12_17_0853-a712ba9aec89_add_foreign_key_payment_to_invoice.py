"""add foreign key  payment to invoice

Revision ID: a712ba9aec89
Revises: 18f63feb5905
Create Date: 2025-12-17 08:53:25.561830

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a712ba9aec89"
down_revision: Union[str, Sequence[str], None] = "18f63feb5905"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        op.f("fk_payments_invoice_id_invoices"),
        "payments",
        "invoices",
        ["invoice_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_payments_invoice_id_invoices"), "payments", type_="foreignkey"
    )
