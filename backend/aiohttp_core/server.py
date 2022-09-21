from typing import AsyncGenerator

from aiohttp import web

from .database import SessionLocal, engine
from .views.user.avatar import routes as avatar_routes

routes = web.RouteTableDef()


async def db_context(
    app: web.Application,
) -> AsyncGenerator[None, None]:
    app["db"] = SessionLocal(bind=engine)
    yield
    await engine.dispose()


@routes.get("/")
async def home(
    request: web.BaseRequest,
) -> web.Response:
    pass


async def aiohttp_app() -> web.Application:
    app = web.Application()
    app.cleanup_ctx.append(db_context)
    app.add_routes(routes)
    app.add_routes(avatar_routes)
    return app


if __name__ == "__main__":
    web.run_app(aiohttp_app())
