import functools
import logging
import sys
from typing import NoReturn

import anyio
from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart import Quart
from quart_cors import cors
from quart_redis import RedisHandler

from coreproject_tracker.enums import IP
from coreproject_tracker.env import REDIS_DATABASE, REDIS_HOST, REDIS_PORT
from coreproject_tracker.functions import check_ip_type
from coreproject_tracker.servers import http_blueprint, run_udp_server, ws_blueprint

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
)
app = Quart(__name__)
# app = cors(app, allow_origin="*")

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

    match await check_ip_type(host):
        case False:
            raise ValueError(f"{host} is not a valid `host`")
        case IP.IPV6:
            if sys.platform == "win32":
                raise ValueError(
                    f"`ip` is {host}, which is `IPV6`",
                    "`IPV6` is not supported on windows under `anyio`.",
                    "Check: https://github.com/agronholm/anyio/discussions/872",
                )

    async with anyio.create_task_group() as tg:
        tg.start_soon(functools.partial(run_web_server, host, port))
        tg.start_soon(functools.partial(run_udp_server, host, port))
