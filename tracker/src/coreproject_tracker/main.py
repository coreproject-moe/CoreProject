import functools
from typing import NoReturn

import anyio
from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart

from coreproject_tracker.env import REDIS_DATABASE, REDIS_HOST, REDIS_PORT
from coreproject_tracker.servers.http import http_blueprint
from coreproject_tracker.servers.udp import run_udp_server
from coreproject_tracker.servers.websocket import ws_blueprint
from quart_redis import RedisHandler

app = Quart(__name__)
app.register_blueprint(http_blueprint)
app.register_blueprint(ws_blueprint)

# Config
app.config["REDIS_URI"] = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}"

# Handler
RedisHandler(app)


async def run_web_server(host: str, port: int) -> NoReturn:
    config = Config()
    config.bind = [f"{host}:{port}"]
    await serve(app, config)


async def main():
    host = "127.0.0.1"
    port = 5000

    async with anyio.create_task_group() as tg:
        tg.start_soon(functools.partial(run_web_server, host, port))
        tg.start_soon(functools.partial(run_udp_server, host, port))
