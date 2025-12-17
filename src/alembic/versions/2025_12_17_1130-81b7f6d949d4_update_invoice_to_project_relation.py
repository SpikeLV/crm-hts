"""update invoice to project relation

Revision ID: 81b7f6d949d4
Revises: c0267c16716e
Create Date: 2025-12-17 11:30:54.008694

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "81b7f6d949d4"
down_revision: Union[str, Sequence[str], None] = "c0267c16716e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_foreign_key(
        op.f("fk_invoices_project_id_projects"),
        "invoices",
        "projects",
        ["project_id"],
        ["id"],
    )


def downgrade() -> None:
    op.drop_constraint(
        op.f("fk_invoices_project_id_projects"), "invoices", type_="foreignkey"
    )
