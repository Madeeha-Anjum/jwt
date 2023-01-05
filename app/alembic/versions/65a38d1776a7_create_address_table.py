"""Create address table

Revision ID: 65a38d1776a7
Revises: a6a3369851f3
Create Date: 2023-01-02 18:44:24.550439

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "65a38d1776a7"
down_revision = "a6a3369851f3"
branch_labels = None

depends_on = None


def upgrade() -> None:
    op.create_table(
        "address",
        sa.Column("id", sa.Integer(), nullable=False, primary_key=True),
        sa.Column("address1", sa.String(), nullable=False),
        sa.Column("address2", sa.String(), nullable=False),
        sa.Column("city", sa.String(), nullable=False),
        sa.Column("state", sa.String(), nullable=False),
        sa.Column("country", sa.String(), nullable=False),
        sa.Column("postalcode", sa.String(), nullable=False),
    )


def downgrade() -> None:
    pass
