from pathlib import Path
from typing import (
    Optional,
    List,
    AsyncGenerator,
)
from functools import partial

import aiohttp_jinja2
import aiopg.sa
from aiohttp import web
import aioredis
import jinja2

from web.routes import init_routes
from web.utils.common import init_config


path = Path(__file__).parent


def init_jinja2(app: web.Application) -> None:
    '''
    Initialize jinja2 template for application.
    '''
    aiohttp_jinja2.setup(
        app,
        loader=jinja2.FileSystemLoader(str(path / 'templates'))
    )


async def database(app: web.Application) -> AsyncGenerator[None, None]:
    '''
    A function that, when the server is started, connects to postgresql,
    and after stopping it breaks the connection (after yield)
    '''
    config = app['config']['postgres']

    engine = await aiopg.sa.create_engine(**config)
    app['db'] = engine

    yield

    app['db'].close()
    await app['db'].wait_closed()


async def redis(app: web.Application) -> None:
    '''
    A function that, when the server is started, connects to redis,
    and after stopping it breaks the connection (after yield)
    '''
    config = app['config']['redis']

    create_redis = partial(
        aioredis.create_redis,
        f'redis://{config["host"]}:{config["port"]}'
    )

    sub = await create_redis()
    pub = await create_redis()

    app['redis_sub'] = sub
    app['redis_pub'] = pub
    app['create_redis'] = create_redis

    yield

    app['redis_sub'].close()
    app['redis_pub'].close()

    await app['redis_sub'].wait_closed()
    await app['redis_pub'].wait_closed()


def init_app(config: Optional[List[str]] = None) -> web.Application:
    app = web.Application()

    init_jinja2(app)
    init_config(app, config=config)
    init_routes(app)

    app.cleanup_ctx.extend([
        redis,
        database,
    ])

    return app
