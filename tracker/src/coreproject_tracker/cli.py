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
    import uvloop

    HAS_UVLOOP = True
except ImportError:
    HAS_UVLOOP = False

from coreproject_tracker.app import make_app
from coreproject_tracker.servers import run_udp_server

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
)


def udp_server_wrapper(host_port: Tuple[str, int]) -> None:
    """Wrapper for UDP server process"""
    host, port = host_port
    anyio.run(run_udp_server, host, port)


def run_hypercorn_worker(config: Config) -> None:
    """Hypercorn worker process entry point"""
    if HAS_UVLOOP:
        uvloop.install()
    # Ensure no event loop is active before starting
    import asyncio

    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.close()
    except RuntimeError:
        pass
    anyio.run(serve, make_app(), config)


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
        p = Process(target=run_hypercorn_worker, args=(config,), daemon=True)
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
    worker_count = multiprocessing.cpu_count() if workers == -1 else max(1, workers)
    try:
        anyio.run(_main_async_wrapper, host, port, worker_count)
    except KeyboardInterrupt:
        logging.info("Application shutdown complete")


if __name__ == "__main__":
    if sys.platform == "win32":
        multiprocessing.freeze_support()
    else:
        multiprocessing.set_start_method("spawn", force=True)
    main()
