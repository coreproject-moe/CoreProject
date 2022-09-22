from aiohttp import web

from aiohttp_core.server import aiohttp_app

if __name__ == "__main__":
    web.run_app(aiohttp_app())
