from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import StreamingResponse, FileResponse
from fastapi import Request
from database import get_db
from models.user import User

router = APIRouter()


@router.get("/avatar/{user_id:str}")
async def get_avatar(
    request: Request, db: AsyncSession = Depends(get_db), user_id: str | None = None
):
    user_model: AsyncSession = await db.get(
        User,
        {"id": int(user_id)},
    )

    if user_model.avatar:
        response = web.FileResponse(
            path=str(DJANGO_MEDIA_DIR) + "\\" + str(user_model.avatar),
            chunk_size=512,
        )

    else:
        response = web.StreamResponse()

        url = str(
            URL(
                user_model.avatar_provider.format(
                    EMAIL=hashlib.md5(
                        user_model.email.strip().lower().encode()
                    ).hexdigest()
                )
            ),
        )

        async with client_session.get(url, allow_redirects=True) as r:
            response.content_type = r.headers["content-type"]
            await response.prepare(request)

            async for line in r.content:
                await response.write(line)

    # Lets confuse peoples
    return response
