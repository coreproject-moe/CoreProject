import aiohttp
from aiohttp import web

routes = web.RouteTableDef()


@routes.get("/user/{user_id}")
async def hello(
    request: web.BaseRequest,
) -> web.StreamResponse:
    response = web.StreamResponse()
    user_id = request.match_info.get("user_id")

    url = "https://eoimages.gsfc.nasa.gov/images/imagerecords/73000/73751/world.topo.bathy.200407.3x21600x21600.B1.png"
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        async with session.get(url) as r:
            response.content_type = r.headers["content-type"]
            await response.prepare(request)

            async for line in r.content:
                await response.write(line)

    print(response.headers)
    return response


app = web.Application()
app.add_routes(routes)
web.run_app(app)
