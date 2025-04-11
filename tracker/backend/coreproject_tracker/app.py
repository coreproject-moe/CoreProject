from quart import Quart
from quart_cors import cors
from quart_redis import RedisHandler

try:
    from flask_orjson import OrjsonProvider  # type: ignore[import]

    HAS_FLASK_ORJSON = True
except ImportError:
    HAS_FLASK_ORJSON = False

from coreproject_tracker.envs import REDIS_DATABASE, REDIS_HOST, REDIS_PORT
from coreproject_tracker.servers import http_blueprint, ws_blueprint


def make_app() -> Quart:
    app = Quart(__name__)
    app = cors(app, allow_origin="*")

    if HAS_FLASK_ORJSON:
        app.json = OrjsonProvider(app)  # type: ignore

    # Config
    app.config["REDIS_URI"] = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}"

    # Handler
    RedisHandler(app)

    app.register_blueprint(http_blueprint)
    app.register_blueprint(ws_blueprint)

    return app
