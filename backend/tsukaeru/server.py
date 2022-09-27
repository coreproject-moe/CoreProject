from typing import AsyncGenerator

import jinja2

from aiohttp import web
import aiohttp_jinja2

from .database import SessionLocal, engine
from .settings import TEMPLATE_DIRS
from .views.index import routes as index_routes
from .views.user.avatar import routes as avatar_routes

routes = web.RouteTableDef()


@web.middleware
async def confuse_people(request, handler):
    response = await handler(request)
    php = "PHP/8.2.1"
    response.headers["server"] = php
    response.headers["x-powered-by"] = php
    return response


async def db_context(
    app: web.Application,
) -> AsyncGenerator[None, None]:
    app["db"] = SessionLocal(bind=engine)
    yield
    await engine.dispose()


async def aiohttp_app() -> web.Application:
    app = web.Application(middlewares=[confuse_people])
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIRS))
    app.cleanup_ctx.append(db_context)
    app.add_routes(index_routes)
    app.add_routes(avatar_routes)
    return app


if __name__ == "__main__":
    web.run_app(aiohttp_app())
