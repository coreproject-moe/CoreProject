import hashlib
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
from yarl import URL

import aiohttp
from aiohttp import web
import aiohttp_jinja2

from ...models.user import User
from ...settings import DJANGO_MEDIA_DIR

routes = web.RouteTableDef()


@routes.get("/user/avatar/{user_id}")
async def avatar(
    request: Any,
) -> web.StreamResponse | web.FileResponse | web.Response:
    response: web.StreamResponse | web.FileResponse | web.Response

    db_session = request.app["db"]
    client_session: aiohttp.ClientSession = request.app["client_session"]
    user_id = request.match_info.get("user_id")

    user_model: AsyncSession = await db_session.get(
        User,
        {"id": int(user_id)},
    )
    if not user_model:
        response = aiohttp_jinja2.render_template(
            "not_found.html",
            request,
            context={
                "user_id": user_id,
            },
        )

    elif user_model.avatar:
        response = web.FileResponse(
            path=str(DJANGO_MEDIA_DIR) + "\\" + str(user_model.avatar),
            chunk_size=512,
        )

    else:
        response = web.StreamResponse()

        url = str(
            URL(
                user_model.avatar_provider.format(
                    EMAIL=hashlib.md5(user_model.email.strip().lower().encode()).hexdigest()
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
