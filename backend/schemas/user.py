from tortoise.contrib.pydantic.creator import pydantic_model_creator

from models.user import UserModel

User_Pydantic = pydantic_model_creator(UserModel, name="User")
UserIn_Pydantic = pydantic_model_creator(
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
