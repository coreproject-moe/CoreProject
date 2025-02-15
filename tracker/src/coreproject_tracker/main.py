import trio
from coreproject_tracker.server.http import http_blueprint
from coreproject_tracker.server.websocket import ws_blueprint
from coreproject_tracker.server.udp import run_udp_server
from quart_trio import QuartTrio
from hypercorn.trio import serve
from hypercorn.config import Config
import multiprocessing

app = QuartTrio(__name__)
app.register_blueprint(http_blueprint)
app.register_blueprint(ws_blueprint)


async def run_web_server():
    config = Config()
    config.bind = ["[::1]:5000"]
    config.workers = multiprocessing.cpu_count()
    await serve(app, config)


async def main():
    async with trio.open_nursery() as nursery:
        nursery.start_soon(run_web_server)
        nursery.start_soon(run_udp_server)
