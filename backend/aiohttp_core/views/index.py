import aiohttp
from aiohttp import web
import aiohttp_jinja2
import gunicorn
import jinja2
import sqlalchemy

import django

routes = web.RouteTableDef()


@routes.get("/")
@aiohttp_jinja2.template("index.html")
async def home(
    request: web.BaseRequest,
) -> web.Response:
    return {
        "aiohttp_version": aiohttp.__version__,
        "django_version": django.__version__,
        "sqlalchemy_version": sqlalchemy.__version__,
        "gunicorn_version": gunicorn.__version__,
        "jinja2_version": jinja2.__version__,
    }
