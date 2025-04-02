import logging
import multiprocessing
import sys

import anyio
import click
from hypercorn.asyncio import serve
from hypercorn.config import Config

from coreproject_tracker.enums import IP
from coreproject_tracker.functions import check_ip_type

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
    match await check_ip_type(host):
        case IP.IPV6:
            if sys.platform == "win32":
                raise ValueError(
                    "IPv6 not supported on Windows under AnyIO. "
                    + "See:https://github.com/agronholm/anyio/discussions/872"
                )

    config = Config()
    config.bind = [f"{host}:{port}"]

    if HAS_UVLOOP:
        uvloop.install()

    async with anyio.create_task_group() as tg:
        tg.start_soon(run_udp_server, host, port)
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
