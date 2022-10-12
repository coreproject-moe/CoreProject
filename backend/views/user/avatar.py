from fastapi import APIRouter
from fastapi.responses import StreamingResponse,FileResponse
from fastapi import  Request

router = APIRouter()

@router.get('/avatar')
async def get_avatar(request:Request):
    pass