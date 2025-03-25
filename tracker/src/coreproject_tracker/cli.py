import logging
import multiprocessing
import sys
from multiprocessing import Process
from typing import Tuple

import anyio
import click
from hypercorn.asyncio import serve
from hypercorn.config import Config

try:
    import uvloop  # type: ignore

    HAS_UVLOOP = True
except ImportError:
    HAS_UVLOOP = False

from coreproject_tracker.enums import IP
from coreproject_tracker.functions import check_ip_type
from coreproject_tracker.main import app
from coreproject_tracker.servers import run_udp_server

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
)


def validate_host(host: str) -> None:
    """Validate host IP type synchronously"""
    ip_type = anyio.run(check_ip_type, host)
    if not ip_type:
        raise ValueError(f"Invalid host: {host}")
    if ip_type == IP.IPV6 and sys.platform == "win32":
        raise ValueError(
            "IPv6 is not supported on Windows under anyio. "
            "See: https://github.com/agronholm/anyio/discussions/872"
        )


def udp_server_wrapper(host_port: Tuple[str, int]) -> None:
    """Wrapper for UDP server process"""
    host, port = host_port
    anyio.run(run_udp_server, host, port)


def run_hypercorn_worker(config: Config, use_uvloop: bool) -> None:
    """Hypercorn worker process entry point"""
    if HAS_UVLOOP:
        uvloop.install()

    anyio.run(serve, app, config)


async def _main_async_wrapper(host: str, port: int, workers: int) -> None:
    """Async context for process management"""
    config = Config()
    config.bind = [f"{host}:{port}"]
    config.reuse_port = True

    # Start UDP server process
    udp_process = Process(target=udp_server_wrapper, args=((host, port),), daemon=True)
    udp_process.start()

    # Start Hypercorn workers
    hypercorn_workers = []
    for _ in range(workers):
        p = Process(target=run_hypercorn_worker, args=(config, HAS_UVLOOP), daemon=True)
        p.start()
        hypercorn_workers.append(p)

    try:
        while True:
            await anyio.sleep(3600)
    except KeyboardInterrupt:
        logging.info("Shutdown signal received")
    finally:
        # Cleanup processes
        for p in hypercorn_workers + [udp_process]:
            if p.is_alive():
                p.terminate()
                p.join()


@click.command()
@click.option("--host", default="127.0.0.1", help="Host to bind")
@click.option("--port", default=5000, help="Port to bind")
@click.option(
    "--workers", default=-1, help="Number of worker processes (-1 = CPU count)"
)
def main(host: str, port: int, workers: int):
    """Entry point for CoreProject Tracker"""
    try:
        validate_host(host)
    except ValueError as e:
        logging.error(str(e))
        sys.exit(1)

    worker_count = multiprocessing.cpu_count() if workers == -1 else max(1, workers)

    try:
        anyio.run(_main_async_wrapper, host, port, worker_count)
    except KeyboardInterrupt:
        logging.info("Application shutdown complete")


if __name__ == "__main__":
    if sys.platform == "win32":
        multiprocessing.freeze_support()

    main()
