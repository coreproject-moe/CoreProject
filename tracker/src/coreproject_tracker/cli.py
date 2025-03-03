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
    if HAS_UVLOOP:
        anyio.run(
            main_function, backend_options={"loop_factory": uvloop.new_event_loop}
        )

    else:
        anyio.run(main_function)
