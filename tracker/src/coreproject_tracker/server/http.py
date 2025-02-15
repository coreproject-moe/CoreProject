from quart import Blueprint
from quart import request
from coreproject_tracker.parser.http import parse_data

http_blueprint = Blueprint("http", __name__)


@http_blueprint.route("/")
async def hello():
    if len(request.args) == 0:
        return "🐟🐈 ⸜(｡˃ ᵕ ˂ )⸝♡".encode("utf-8")
    try:
        data = await parse_data(request.args)
        print(data)
    except Exception as e:
        print(e)

    return "yi"
