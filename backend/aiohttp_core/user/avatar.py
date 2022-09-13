import hashlib
import mimetypes

import aiofiles
import aiohttp
from aiohttp import web
from django.contrib.auth import get_user_model

routes = web.RouteTableDef()


@routes.get("/avatar/{user_id}")
async def avatar(
    request: web.BaseRequest,
) -> web.StreamResponse:

    response = web.StreamResponse()
    user_id = request.match_info.get("user_id")
    user_model = await get_user_model().objects.aget(pk=user_id)

    if user_model.avatar:
        async with aiofiles.open(user_model.avatar.path, "rb") as avatar_file:
            response.content_type = mimetypes.MimeTypes().guess_type(
                url=str(avatar_file),
            )[0]
            await response.prepare(request)

            async for line in avatar_file:
                await response.write(line)

            await avatar_file.close()

    else:
        url = f"""https://seccdn.libravatar.org/avatar/{
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
        async with aiohttp.ClientSession(raise_for_status=True) as session:
            async with session.get(url) as r:
                response.content_type = r.headers["content-type"]
                await response.prepare(request)

                async for line in r.content:
                    await response.write(line)

    return response


avatar = web.Application()
avatar.add_routes(routes)
