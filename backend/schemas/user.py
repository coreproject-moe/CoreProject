from tortoise.contrib.pydantic import pydantic_model_creator
from models.user import User

User_Pydantic = pydantic_model_creator(User, name="User")
UserIn_Pydantic = pydantic_model_creator(User, name="UserIn", exclude_readonly=True)
