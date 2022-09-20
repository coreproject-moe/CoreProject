import hashlib

import aiohttp
from aiohttp import web
from django.contrib.auth import get_user_model
from yarl import URL

routes = web.RouteTableDef()


@routes.get("/avatar/{user_id}")
async def avatar(
    request: web.BaseRequest,
) -> web.StreamResponse | web.FileResponse:

    user_id = request.match_info.get("user_id")
    user_model = await get_user_model().objects.aget(
        pk=user_id,
    )
    # Explicitly declare type
    response: web.StreamResponse | web.FileResponse

    if user_model.avatar:
        response = web.FileResponse(
            path=user_model.avatar.path,
            chunk_size=512,
        )

    else:
        response = web.StreamResponse()

        url = str(
            URL(
                f"""https://seccdn.libravatar.org/avatar/{
                    hashlib
                    .md5(
                        user_model.
                        email.
                        strip().
                        lower().
                        encode()
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


app = web.Application()
app.add_routes(routes)
