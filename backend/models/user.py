from tortoise.models import Model
from tortoise import fields

import settings
from tortoise.validators import MaxValueValidator, MinValueValidator


class User(Model):
    id = fields.UUIDField(pk=True, unique=True)
    password = fields.CharField(max_length=256)
    last_login = fields.DatetimeField()
    username = fields.CharField(max_length=512)
    first_name = fields.CharField(max_length=512)
    last_name = fields.CharField(max_length=512)
    email = fields.CharField(max_length=512)  # Maybe modify this

    is_active = fields.BooleanField(default=True)
    is_staff = fields.BooleanField(default=False)
    is_superuser = fields.BooleanField()

    username_discriminator = fields.IntField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(int("9" * settings.USERNAME_DISCRIMINATOR_LENGTH)),
        ]
    )

    avatar = fields.CharField(max_length=512)
    avatar_provider = fields.CharField(
        max_length=512, default="https://seccdn.libravatar.org/avatar/{EMAIL}?s=512"
    )

    date_joined = fields.DatetimeField(auto_now_add=True)

    class PydanticMeta:
        # computed = ["full_name"]
        exclude = ["password_hash"]
