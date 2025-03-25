import asyncio
from typing import TYPE_CHECKING

from quart import Blueprint, copy_current_websocket_context, json, websocket
from quart_redis import get_redis

from coreproject_tracker.constants import WEBSOCKET_INTERVAL
from coreproject_tracker.datastructures import WebsocketDatastructure
from coreproject_tracker.enums import ACTIONS, EVENT_NAMES
from coreproject_tracker.functions import (
    bytes_to_bin_str,
    convert_event_name_to_event_enum,
    hdel,
    hex_str_to_bin_str,
    hget,
    hset,
)

if TYPE_CHECKING:
    from redis.client import PubSub

ws_blueprint = Blueprint("websocket", __name__)


@ws_blueprint.websocket("/")
async def ws():
    """
    WebSocket endpoint that uses Redis Pub/Sub for message dissemination.
    """

    @copy_current_websocket_context
    async def parse_websocket() -> WebsocketDatastructure:
        initial_message = await websocket.receive_json()
        client_ip, client_port = websocket.scope.get("client")

        _data = {
            "ip": client_ip,
            "port": client_port,
            "addr": f"{client_ip}:{client_port}",
            "info_hash_raw": initial_message["info_hash"],
            "action": initial_message["action"],
            "peer_id": initial_message["peer_id"],
            "numwant": initial_message.get("numwant"),
            "uploaded": initial_message.get("uploaded"),
            "offers": initial_message.get("offers"),
            "left": initial_message.get("left"),
        }

        if initial_message.get("answer"):
            _data |= {
                "answer": initial_message["answer"],
                "to_peer_id": initial_message["to_peer_id"],
                "offer_id": initial_message["offer_id"],
            }

        if event := initial_message.get("event"):
            _data |= {
                "event": await convert_event_name_to_event_enum(event),
            }

        return WebsocketDatastructure(**_data)

    data = await parse_websocket()
    task = None
    redis = get_redis()
    pubsub: PubSub | None = None

    try:
        pubsub = redis.pubsub()
        # Not using `peer:data.peer_id.hex()` causes phantom errors
        await pubsub.subscribe(f"peer:{data.peer_id.hex()}")

        async def listen_pubsub():
            try:
                while True:
                    message = await pubsub.get_message(
                        ignore_subscribe_messages=True, timeout=1.0
                    )
                    if message and message["type"] == "message":
                        await websocket.send_json(json.loads(message["data"]))
            except asyncio.CancelledError:
                pass
            finally:
                await pubsub.unsubscribe(f"peer:{data.peer_id.hex()}")
                await pubsub.close()

        task = asyncio.create_task(listen_pubsub())

        while True:
            if data.event == EVENT_NAMES.STOP:
                await websocket.close()
                break

            response = {"action": data.action}

            await hset(
                data.info_hash,
                data.addr,
                json.dumps(
                    {
                        "peer_id": data.peer_id.hex(),
                        "peer_ip": data.ip,
                        "port": data.port,
                        "left": data.left,
                    }
                ),
            )

            seeders = 0
            leechers = 0
            redis_data = await hget(data.info_hash) or {}
            for peer in redis_data.values():
                peer_info = json.loads(peer)
                if peer_info["left"] == 0:
                    seeders += 1
                else:
                    leechers += 1

            response |= {"completed": seeders, "incompleted": leechers}

            if data.action == ACTIONS.ANNOUNCE:
                response |= {
                    "info_hash": await hex_str_to_bin_str(data.info_hash),
                    "interval": WEBSOCKET_INTERVAL,
                }
                await websocket.send_json(response)

            if not data.answer:
                await websocket.send_json(response)

            # Handle offers by publishing to respective peers
            if offers := data.offers:
                for value in redis_data.values():
                    peer_info = json.loads(value)
                    for offer in offers:
                        message = json.dumps(
                            {
                                "action": "announce",
                                "offer": offer["offer"],
                                "offer_id": offer["offer_id"],
                                "peer_id": await bytes_to_bin_str(data.peer_id),
                                "info_hash": await hex_str_to_bin_str(data.info_hash),
                            }
                        )
                        await redis.publish(f"peer:{peer_info['peer_id']}", message)

            # Handle answers by publishing to the target peer
            if data.answer:
                message = json.dumps(
                    {
                        "action": "announce",
                        "answer": data.answer,
                        "offer_id": data.offer_id,
                        "peer_id": await bytes_to_bin_str(data.peer_id),
                        "info_hash": await hex_str_to_bin_str(data.info_hash),
                    }
                )
                await redis.publish(f"peer:{data.to_peer_id.hex()}", message)

            # Wait for next message from client
            data = await parse_websocket()

    except asyncio.CancelledError:
        print("Connection closed")

    finally:
        # Cleanup
        if task:
            task.cancel()
            try:
                await task
            except asyncio.CancelledError:
                pass
        if pubsub:
            await pubsub.unsubscribe(f"peer:{data.peer_id.hex()}")
            await pubsub.close()
        await hdel(data.info_hash, data.addr)
