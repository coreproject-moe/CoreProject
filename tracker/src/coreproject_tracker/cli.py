import anyio
import click

try:
    import uvloop  # type: ignore

    HAS_UVLOOP = True
except ImportError:
    HAS_UVLOOP = False
from coreproject_tracker.main import main as main_function


@click.command()
def main():
    """Simple command that prints Hello, World!"""
    backend_options = {}
    if HAS_UVLOOP:
        backend_options |= {"loop_factory": uvloop.new_event_loop}

    anyio.run(main_function, backend_options=backend_options)
