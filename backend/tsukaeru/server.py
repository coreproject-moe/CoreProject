from collections.abc import AsyncGenerator

import jinja2

from aiohttp import web
from aiohttp_client_cache.backends.redis import RedisBackend
from aiohttp_client_cache.session import CachedSession
import aiohttp_jinja2

from .database import SessionLocal, engine
from .settings import TEMPLATE_DIRS
from .views.index import routes as index_routes
from .views.user.avatar import routes as avatar_routes

routes = web.RouteTableDef()


async def session_context(app: web.Application) -> None:
    session = CachedSession(
        cache=RedisBackend(
            "aiohttp_cache",
            expire_after=120,
        )
    )
    app["client_session"] = session
    yield
    await session.close()


async def db_context(
    app: web.Application,
) -> AsyncGenerator[None, None]:
    app["db"] = SessionLocal(bind=engine)
    yield
    await engine.dispose()


async def aiohttp_app() -> web.Application:
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIRS))
    app.cleanup_ctx.append(db_context)
    app.cleanup_ctx.append(session_context)
    app.add_routes(index_routes)
    app.add_routes(avatar_routes)
    return app


if __name__ == "__main__":
    web.run_app(aiohttp_app())
