from quart import Blueprint, request
from coreproject_tracker.validators import HttpValidator
from http import HTTPStatus

http_blueprint = Blueprint("http", __name__)


@http_blueprint.route("/")
async def hello():
    if len(request.args) == 0:
        return "🐟🐈 ⸜(｡˃ ᵕ ˂ )⸝♡".encode("utf-8")

    try:
        data = HttpValidator(**request.args, peer_ip=request.remote_addr)
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

    print(data)

    return "yi"
