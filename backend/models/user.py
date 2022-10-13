import sqlalchemy as sa

from database import BASE


from sqlalchemy.dialects.postgresql import INET


class User(BASE):
    __tablename__ = "user"  # Match with django

    id = sa.Column(sa.BigInteger(), primary_key=True)
    password = sa.Column(sa.String())
    last_login = sa.Column(sa.DateTime())
    is_superuser = sa.Column(sa.Boolean())
    username = sa.Column(sa.String(150))
    first_name = sa.Column(sa.String(150))
    last_name = sa.Column(sa.String(150))
    email = sa.Column(sa.String(254))
    is_staff = sa.Column(sa.Boolean())
    is_active = sa.Column(sa.Boolean())
    username_discriminator = sa.Column(sa.Integer())
    avatar = sa.Column(sa.String(150))
    avatar_provider = sa.Column(sa.String())
    ip = sa.Column(sa.String(12))
    date_joined = sa.Column(sa.DateTime())
