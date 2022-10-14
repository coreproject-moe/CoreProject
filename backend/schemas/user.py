from tortoise.contrib.pydantic.creator import pydantic_model_creator

from models.user import UserModel

UserSchema = pydantic_model_creator(UserModel, name="User")
UserInSchema = pydantic_model_creator(
    UserModel,
    name="UserIn",
    include=(
        "username",
        "password",
        "email",
        "first_name",
        "last_name",
        "username_discriminator",
        "avatar",
        "avatar_provider",
    ),
    exclude_readonly=True,
)
