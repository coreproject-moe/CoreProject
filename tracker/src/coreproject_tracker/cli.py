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


@click.command()
@click.option("--host", default="127.0.0.1", help="Host to bind")
@click.option("--port", default=5000, help="Port to bind")
def main(host: str, port: int):
    """Start application with multiple workers and UDP server"""
    # Validate host IP first
    try:
        validate_host(host)
    except ValueError as e:
        logging.error(str(e))
        sys.exit(1)

    # UDP Server Process
    udp_process = Process(target=udp_server_wrapper, args=((host, port),), daemon=True)
    udp_process.start()

    # Configure Hypercorn
    config = Config()
    config.bind = [f"{host}:{port}"]
    config.workers = multiprocessing.cpu_count()

    if HAS_UVLOOP:
        # uvloop requires patching before creating the event loop
        from hypercorn.utils import _set_loop_policy

        _set_loop_policy(uvloop.EventLoopPolicy())

    # Run Hypercorn with proper cleanup
    try:
        anyio.run(
            serve,
            app,
            config,
            backend="asyncio",
            backend_options={"use_uvloop": HAS_UVLOOP},
        )
    except KeyboardInterrupt:
        logging.info("Received exit signal, shutting down...")
    finally:
        if udp_process.is_alive():
            udp_process.terminate()
            udp_process.join()


if __name__ == "__main__":
    # Windows multiprocessing safeguard
    if sys.platform == "win32":
        multiprocessing.freeze_support()

    # Click command execution
    main()
