"""empty message

Revision ID: 85ea359b45b3
Revises: ba1097757c73
Create Date: 2021-10-19 10:03:41.068244

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "85ea359b45b3"
down_revision = "ba1097757c73"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "users",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(length=128), nullable=False),
        sa.Column("email", sa.String(length=128), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("users")
    # ### end Alembic commands ###
