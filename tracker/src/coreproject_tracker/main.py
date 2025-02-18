import anyio
from coreproject_tracker.server.http import http_blueprint
from coreproject_tracker.server.websocket import ws_blueprint
from coreproject_tracker.server.udp import run_udp_server
from coreproject_tracker.env import REDIS_HOST, REDIS_PORT, REDIS_DATABASE
from quart import Quart
from hypercorn.asyncio import serve
from hypercorn.config import Config
from quart_redis import RedisHandler

app = Quart(__name__)
app.register_blueprint(http_blueprint)
app.register_blueprint(ws_blueprint)

# Config
app.config["REDIS_URI"] = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}"

# Handler
RedisHandler(app)


async def run_web_server():
    config = Config()
    config.bind = ["[::1]:5000"]
    await serve(app, config)


async def main():
    async with anyio.create_task_group() as nursery:
        nursery.start_soon(run_web_server)
        nursery.start_soon(run_udp_server)
