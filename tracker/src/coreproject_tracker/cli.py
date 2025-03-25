import logging
import multiprocessing
import sys
from multiprocessing import Process

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
from coreproject_tracker.main import app  # Import your Quart app instance
from coreproject_tracker.servers import run_udp_server

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
)


def validate_host(host: str) -> None:
    """Synchronous wrapper for IP validation"""
    ip = anyio.run(check_ip_type, host)
    if ip == IP.IPV6:
        if sys.platform == "win32":
            raise ValueError(
                f"`ip` is `{host}`,"
                + "`IPV6` is not supported on windows under `anyio`,"
                + "see: https://github.com/agronholm/anyio/discussions/872"
            )


def udp_server_wrapper(host_port: tuple[str, int]) -> None:
    """Wrapper function for UDP server to run in a process"""
    host, port = host_port
    anyio.run(run_udp_server, host, port)


def run_hypercorn_worker(config: Config, use_uvloop: bool = False) -> None:
    """Worker process entry point for Hypercorn server"""
    if HAS_UVLOOP:
        uvloop.install()

    anyio.run(serve, app, config)


@click.command()
@click.option("--host", default="127.0.0.1", help="Host to bind")
@click.option("--port", default=5000, help="Port to bind")
@click.option(
    "--workers", default=-1, help="Number of worker processes (-1 = CPU count)"
)
def main(host: str, port: int, workers: int):
    """Start application with multiple workers"""
    # Calculate worker count
    worker_count = multiprocessing.cpu_count() if workers == -1 else workers

    # Configure Hypercorn (single worker per process)
    config = Config()
    config.bind = [f"{host}:{port}"]
    config.reuse_port = True  # Critical for multiple workers sharing port

    # Start UDP server in separate process (your existing implementation)
    udp_process = Process(
        target=udp_server_wrapper,  # Your UDP server entry function
        args=((host, port),),
        daemon=True,
    )
    udp_process.start()

    # Start Hypercorn worker processes
    hypercorn_workers = []
    for _ in range(worker_count):
        p = Process(target=run_hypercorn_worker, args=(config, HAS_UVLOOP), daemon=True)
        p.start()
        hypercorn_workers.append(p)

    # Handle shutdown gracefully
    try:
        while True:
            anyio.sleep(3600)  # Main process stays alive
    except KeyboardInterrupt:
        logging.info("Shutting down workers...")
    finally:
        for p in hypercorn_workers + [udp_process]:
            if p.is_alive():
                p.terminate()
                p.join()


if __name__ == "__main__":
    # Windows multiprocessing safeguard
    if sys.platform == "win32":
        multiprocessing.freeze_support()

    # Click command execution
    main()
