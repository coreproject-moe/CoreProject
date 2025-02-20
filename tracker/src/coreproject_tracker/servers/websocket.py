from quart import Blueprint, websocket

ws_blueprint = Blueprint("websocket", __name__)


@ws_blueprint.websocket("/ws")
async def ws():
    while True:
        data = await websocket.receive()
        await websocket.send(f"Echo: {data}")
