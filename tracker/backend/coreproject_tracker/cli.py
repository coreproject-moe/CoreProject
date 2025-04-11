import asyncio
import logging
import sys
from concurrent.futures import ProcessPoolExecutor

import anyio
import click
from hypercorn import Config
from hypercorn.asyncio import serve  # type: ignore

from coreproject_tracker.app import make_app
from coreproject_tracker.enums import IP
from coreproject_tracker.envs import WORKERS_COUNT
from coreproject_tracker.functions import check_ip_type
from coreproject_tracker.servers import run_udp_server as _run_udp_server

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
)


def run_udp_server(host: str, port: int) -> None:
    anyio.run(_run_udp_server, host, port, backend="asyncio")


def run_http_websocket_server(host: str, port: int) -> None:
    config = Config()
    config.bind = [f"{host}:{port}"]
    anyio.run(serve, make_app(), config, backend="asyncio")


async def _main_async_wrapper(host: str, port: int) -> None:
    """Async context for server management"""
    ip_type = await check_ip_type(host)
    if ip_type == IP.IPV6:
        if sys.platform == "win32":
            raise ValueError(
                "IPv6 not supported on Windows under AnyIO. "
                + "See:https://github.com/agronholm/anyio/discussions/872"
            )

    loop = asyncio.get_event_loop()

    with ProcessPoolExecutor() as executor:
        # Run one instance of UDP server in the main process
        loop.run_in_executor(executor, run_udp_server, host, port)

        for _ in range(WORKERS_COUNT):
            loop.run_in_executor(executor, run_http_websocket_server, host, port)


@click.command()
@click.option("--host", default="127.0.0.1", help="Host to bind")
@click.option("--port", default=5000, help="Port to bind")
def main(host: str, port: int):
    """Entry point for CoreProject Tracker"""

    try:
        asyncio.run(_main_async_wrapper(host, port))
    except KeyboardInterrupt:
        logging.info("Application shutdown complete")


if __name__ == "__main__":
    main()
