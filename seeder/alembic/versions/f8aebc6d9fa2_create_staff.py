"""Create Staff

Revision ID: f8aebc6d9fa2
Revises: 111494c77f67
Create Date: 2024-07-30 13:02:57.039121

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "f8aebc6d9fa2"
down_revision: Union[str, None] = "111494c77f67"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "staff",
        sa.Column(
            "id", sa.BigInteger().with_variant(sa.Integer(), "sqlite"), nullable=False
        ),
        sa.Column("mal_id", sa.BigInteger(), nullable=False),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("given_name", sa.String(), nullable=True),
        sa.Column("family_name", sa.String(), nullable=True),
        sa.Column("alternate_name", sa.PickleType(), nullable=True),
        sa.Column("birthday", sa.Date(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("mal_id", "name", "given_name", "family_name", name="_name_uc"),
    )
    op.drop_column("character", "lol")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("character", sa.Column("lol", sa.VARCHAR(), nullable=True))
    op.drop_table("staff")
    # ### end Alembic commands ###
