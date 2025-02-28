
from quart import Blueprint, Websocket, websocket
from quart_redis import get_redis

ws_blueprint = Blueprint("websocket", __name__)


# SEE: https://chatgpt.com/share/67b9ea68-4f94-8011-bd93-7dd69c2310e0


async def redis_subscriber(ws: Websocket, channel_name: str) -> None:
    """Subscribe to a Redis channel and forward messages to WebSocket clients."""
    redis_client = get_redis()
    pubsub = redis_client.pubsub()
    await pubsub.subscribe(channel_name)
    try:
        async for message in pubsub.listen():
            if message["type"] == "message":
                await ws.send(message["data"].decode("utf-8"))
    except Exception as e:
        print(f"Redis subscriber error: {e}")
    finally:
        await pubsub.unsubscribe(channel_name)


@ws_blueprint.websocket("/")
async def ws():
    """WebSocket endpoint that listens for incoming messages and publishes them."""
    initial_message = await websocket.receive()
    data = parse_websocket(initial_message)
