import logging
import multiprocessing
import sys

import anyio
import click
from hypercorn.asyncio import serve
from hypercorn.config import Config

try:
    import uvloop  # type: ignore[import]

    HAS_UVLOOP = True
except ImportError:
    HAS_UVLOOP = False

from coreproject_tracker.app import make_app
from coreproject_tracker.servers import run_udp_server

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
)


async def _main_async_wrapper(host: str, port: int) -> None:
    """Async context for server management"""
    config = Config()
    config.bind = [f"{host}:{port}"]

    if HAS_UVLOOP:
        uvloop.install()

    async with anyio.create_task_group() as tg:
        # Start UDP server as async task
        tg.start_soon(run_udp_server, host, port)

        # Start Hypercorn server
        tg.start_soon(serve, make_app(), config)

        # Keep running until cancelled
        await anyio.sleep_forever()


@click.command()
@click.option("--host", default="127.0.0.1", help="Host to bind")
@click.option("--port", default=5000, help="Port to bind")
def main(host: str, port: int):
    """Entry point for CoreProject Tracker"""

    try:
        anyio.run(_main_async_wrapper, host, port)
    except KeyboardInterrupt:
        logging.info("Application shutdown complete")


if __name__ == "__main__":
    if sys.platform == "win32":
        multiprocessing.freeze_support()
    main()
