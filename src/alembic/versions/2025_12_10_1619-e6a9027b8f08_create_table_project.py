"""create table Project

Revision ID: e6a9027b8f08
Revises: fbae5a753ad5
Create Date: 2025-12-10 16:19:41.456086

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "e6a9027b8f08"
down_revision: Union[str, Sequence[str], None] = "fbae5a753ad5"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "projects",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("project_code", sa.String(length=255), nullable=False),
        sa.Column("project_status", sa.String(length=255), nullable=True),
        sa.Column(
            "project_budget", sa.Numeric(precision=10, scale=2), nullable=True
        ),
        sa.Column("project_description", sa.String(length=255), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("deleted_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_projects")),
    )


def downgrade() -> None:
    op.drop_table("projects")
