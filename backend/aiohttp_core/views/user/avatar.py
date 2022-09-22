import hashlib
from typing import Any

import aiohttp
from aiohttp import web
from yarl import URL
from sqlalchemy.ext.asyncio import AsyncSession

from ...models.user import User
from ...settings import DJANGO_MEDIA_DIR


routes = web.RouteTableDef()


@routes.get("/user/avatar/{user_id}")
async def avatar(
    request: Any,
) -> web.StreamResponse | web.FileResponse:
    session = request.app["db"]
    user_id = request.match_info.get("user_id")
    user_model: AsyncSession = await session.get(
        User,
        {"id": int(user_id)},
    )
    response: web.StreamResponse | web.FileResponse

    if user_model.avatar:
        response = web.FileResponse(
            path=str(DJANGO_MEDIA_DIR) + "\\" + str(user_model.avatar),
            chunk_size=512,
        )
    else:
        response = web.StreamResponse()
        avatar_provider = user_model.avatar_provider

        if avatar_provider.name == "GRAVATAR":
            hashing_algorithm = hashlib.md5

        elif avatar_provider.name == "LIBRAVATAR":
            hashing_algorithm = hashlib.sha256

        url = str(
            URL(
                f"""{avatar_provider.value}/{
                    (
                       hashing_algorithm(
                            user_model
                            .email
                            .strip()
                            .lower()
                            .encode()
                        )
                    )
                    .hexdigest()
                }
                """
            ).with_query(
                request.rel_url.query,
            ),
        )
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get(url, allow_redirects=True) as r:
                response.content_type = r.headers["content-type"]
                await response.prepare(request)

                async for line in r.content:
                    await response.write(line)
    return response
