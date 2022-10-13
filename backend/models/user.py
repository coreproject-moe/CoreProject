from tortoise import fields
from tortoise.models import Model
from tortoise.validators import MaxValueValidator, MinValueValidator

import settings


class User(Model):
    id = fields.UUIDField(pk=True, unique=True)
    email = fields.CharField(max_length=512)  # Maybe modify this
    username = fields.CharField(max_length=512)
    password = fields.CharField(max_length=256)

    first_name = fields.CharField(max_length=512)
    last_name = fields.CharField(max_length=512)

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

    last_login = fields.DatetimeField()
    date_joined = fields.DatetimeField(auto_now_add=True)

    def username_with_discriminator(self):
        return f"{self.username}#{str(self.username_discriminator).zfill(settings.USERNAME_DISCRIMINATOR_LENGTH)}"

    class PydanticMeta:
        computed = ["username_with_discriminator"]
        exclude = ["password_hash"]
