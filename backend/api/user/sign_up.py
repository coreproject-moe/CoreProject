from fastapi import APIRouter
from fastapi.responses import Response

from schemas.user import UserInSchema

router = APIRouter(prefix="/user")


@router.post("sign_up")
async def sign_up(data: UserInSchema) -> Response:
    print(data)
    return {}
