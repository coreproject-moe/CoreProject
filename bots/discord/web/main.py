from collections.abc import AsyncGenerator

import jinja2

from aiohttp import web
import aiohttp_jinja2

from database import SessionLocal, engine, DjangoSessionLocal
from settings import TEMPLATE_DIRS

routes = web.RouteTableDef()


async def db_context(
    app: web.Application,
) -> AsyncGenerator[None, SessionLocal]:
    app["db"] = SessionLocal(bind=engine)
    yield
    await engine.dispose()


async def django_db_context(
    app: web.Application,
) -> AsyncGenerator[None, SessionLocal]:
    app["django_db"] = DjangoSessionLocal(bind=engine)
    yield
    await engine.dispose()


async def aiohttp_app() -> web.Application:
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(TEMPLATE_DIRS))
    app.cleanup_ctx.append(db_context)
    app.cleanup_ctx.append(django_db_context)

    return app


if __name__ == "__main__":
    web.run_app(aiohttp_app())
