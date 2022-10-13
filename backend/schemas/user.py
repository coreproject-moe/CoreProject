from tortoise.contrib.pydantic import pydantic_model_creator

from models.user import User

User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(
    User,
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
