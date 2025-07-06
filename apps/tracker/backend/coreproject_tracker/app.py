from quart import Quart
from quart_cors import cors

try:
    from flask_orjson import OrjsonProvider  # type: ignore[import]

    HAS_FLASK_ORJSON = True
except ImportError:
    HAS_FLASK_ORJSON = False

from coreproject_tracker.envs import REDIS_URI
from coreproject_tracker.servers import http_blueprint, ws_blueprint


def make_app() -> Quart:
    app = Quart(__name__)
    app = cors(app, allow_origin="*")

    if HAS_FLASK_ORJSON:
        app.json = OrjsonProvider(app)  # type: ignore

    from coreproject_tracker.singletons.redis import RedisHandler

    redis_manager = RedisHandler(REDIS_URI)

    @app.before_serving
    async def before_serving():
        await redis_manager.init_redis()

    @app.after_serving
    async def after_serving():
        await redis_manager.close_redis()

    app.register_blueprint(http_blueprint)
    app.register_blueprint(ws_blueprint)

    return app
