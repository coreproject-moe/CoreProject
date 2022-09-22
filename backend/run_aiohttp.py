from aiohttp_core.server import aiohttp_app
from aiohttp import web

if __name__ == "__main__":
    web.run_app(aiohttp_app())
