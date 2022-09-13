import os
from pathlib import Path
import sys

import django

# Goes to the directory where pipfile is present
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    str(
        Path(
            BASE_DIR.joinpath("django_core"),
        )
    )
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


from aiohttp import web
from user.avatar import app as avatar_app


async def aiohttp_app() -> web.Application:
    app = web.Application()
    app.add_subapp("/user", avatar_app)
    return app


if __name__ == "__main__":
    web.run_app(aiohttp_app())
