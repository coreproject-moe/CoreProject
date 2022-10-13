from tortoise.models import Model
from tortoise import fields

from sqlalchemy.dialects.postgresql import INET


class User(Model):
    id = fields.UUIDField(pk=True, unique=True)
    password = fields.CharField(max_length=256)
    last_login = fields.DatetimeField()
    is_superuser = fields.BooleanField()
    username = fields.CharField(max_length=512)
    first_name = fields.CharField(max_length=512)
    last_name = fields.CharField(max_length=512)
    email = fields.CharField(max_length=512)  # Maybe modify this
    is_staff = fields.BooleanField(default=False)
    is_active = fields.BooleanField(default=True)
    username_discriminator = fields.IntField()
    avatar = fields.CharField(max_length=512)
    avatar_provider = fields.CharField(max_length=512)
    ip = fields.CharField(max_length=512)
    date_joined = fields.DatetimeField(auto_now_add=True)
