import logging

from quart import Quart
from quart_redis import RedisHandler

from coreproject_tracker.envs import REDIS_DATABASE, REDIS_HOST, REDIS_PORT
from coreproject_tracker.servers import http_blueprint, ws_blueprint

logging.basicConfig(
    level=logging.INFO, format="[%(asctime)s] [%(process)d] [%(levelname)s] %(message)s"
)
app = Quart(__name__)

app.register_blueprint(http_blueprint)
app.register_blueprint(ws_blueprint)

# Config
app.config["REDIS_URI"] = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}"

# Handler
RedisHandler(app)
