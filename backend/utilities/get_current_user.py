from fastapi import Request

from models.user import UserModel


async def get_current_user(request: Request) -> UserModel:
    pass
