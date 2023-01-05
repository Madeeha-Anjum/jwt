"""create address id to user

Revision ID: 87c9e0625262
Revises: 65a38d1776a7
Create Date: 2023-01-05 17:34:01.168536

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "87c9e0625262"
down_revision = "65a38d1776a7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column("users", sa.Column("address_id", sa.Integer(), nullable=True))
    op.create_foreign_key(
        "address_users_fk",
        source_table="users",
        referent_table="address",
        local_cols=["address_id"],
        remote_cols=["id"],
        ondelete="CASCADE",
    )


def downgrade() -> None:
    op.drop_constraint("address_users_fk", table_name="users")
    op.drop_column("users", "address_id")
