import hashlib
from collections.abc import AsyncGenerator

import aiohttp
from fastapi import APIRouter, Depends
from fastapi.responses import FileResponse, StreamingResponse
from yarl import URL

from dependencies.session import get_session
from models.user import UserModel

router = APIRouter()

MEDIA_TYPE = ""


@router.get("/avatar/{user_id:str}")
async def get_avatar(
    user_id: str | None = None,
    client_session: aiohttp.ClientSession = Depends(get_session),
) -> FileResponse | StreamingResponse:
    response: FileResponse | StreamingResponse
    user_model: UserModel = await UserModel.get(id=user_id)

    if user_model.avatar:
        response = FileResponse(user_model.avatar)

    else:
        url = str(
            URL(
                user_model.avatar_provider.format(
                    EMAIL=hashlib.md5(user_model.email.strip().lower().encode()).hexdigest()
                )
            ),
        )
        # url = "https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.B1.png" # noqa

        # Thank you random guy at stackoverflow
        # https://stackoverflow.com/questions/71395796/return-file-streaming-response-from-online-video-url-in-fastapi
        async def __async_response_iterator__() -> AsyncGenerator[bytes, None]:
            async with client_session.get(url, allow_redirects=True) as res:
                global MEDIA_TYPE
                MEDIA_TYPE = res.headers["content-type"]

                async for chunk in res.content.iter_any():
                    yield chunk

        response = StreamingResponse(
            content=__async_response_iterator__(),
            media_type=MEDIA_TYPE,
        )

    return response
