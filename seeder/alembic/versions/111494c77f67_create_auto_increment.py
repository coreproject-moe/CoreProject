"""Create Auto Increment

Revision ID: 111494c77f67
Revises:
Create Date: 2024-07-29 17:01:38.916222

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "111494c77f67"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "character",
        sa.Column(
            "id", sa.BigInteger().with_variant(sa.Integer(), "sqlite"), nullable=False
        ),
        sa.Column("mal_id", sa.BigInteger(), nullable=True),
        sa.Column("name", sa.String(), nullable=True),
        sa.Column("name_kanji", sa.String(), nullable=True),
        sa.Column("character_image", sa.String(), nullable=True),
        sa.Column("about", sa.String(), nullable=True),
        sa.Column("lol", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("mal_id", "name", "name_kanji", name="_name_uc"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("character")
    # ### end Alembic commands ###