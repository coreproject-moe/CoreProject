import os
from pathlib import Path
import sys

import aiohttp
from aiohttp import web
import django
from django.conf import settings
from django.template import Context, Template
from user.avatar import app as avatar_app

# Goes to the directory where pipfile is present
BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIRS = str(
    BASE_DIR.joinpath("templates"),
)

routes = web.RouteTableDef()


async def on_startup(app):
    sys.path.append(
        str(
            Path(
                BASE_DIR.parent.joinpath("django_core"),
            )
        )
    )
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
    settings.DEBUG = False
    django.setup()


@routes.get("/")
async def home(
    request: web.BaseRequest,
) -> web.Response:
    # Load template
    template_file = open(TEMPLATE_DIRS + "/index.html")
    template = Template(template_file.read())
    context = Context(
        {
            "server_name": "server",  # Change this in future
            "aiohttp_version": aiohttp.__version__,
            "django_version": django.__version__,
        }
    )

    response = web.Response(
        text=template.render(context),
        headers={"Content-Type": "text/html"},
    )
    return response


async def aiohttp_app() -> web.Application:
    app = web.Application()
    app.on_startup.append(on_startup)
    app.add_routes(routes)
    app.add_subapp("/user", avatar_app)
    return app


if __name__ == "__main__":
    web.run_app(aiohttp_app())
