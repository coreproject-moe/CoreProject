import contextlib
import json

from quart import Blueprint, websocket

from coreproject_tracker.constants import WEBSOCKET_INTERVAL
from coreproject_tracker.datastructures import WebsocketDatastructure
from coreproject_tracker.functions import hdel, hget, hset
from coreproject_tracker.managers import WebsocketConnectionManager

ws_blueprint = Blueprint("websocket", __name__)


connection_manager = WebsocketConnectionManager()


@ws_blueprint.websocket("/")
async def ws():
    """WebSocket endpoint that listens for incoming messages and publishes them."""
    initial_message = await websocket.receive_json()

    client_ip, client_port = websocket.scope.get("client")

    _data = {
        "info_hash_raw": initial_message["info_hash"],
        "action": initial_message["action"],
        "peer_id": initial_message["peer_id"],
        # "numwant": initial_message["numwant"],
        "uploaded": initial_message["uploaded"],
        "event": initial_message["event"],
        "offers": initial_message["offers"],
        "left": initial_message["left"],
        "answer": initial_message.get("answer"),
        "offer_id": initial_message.get("offer_id"),
        "ip": client_ip,
        "addr": f"{client_ip}:{client_port}",
    }
    data = WebsocketDatastructure(**_data)

    response = {
        "action": data.action,
    }

    await hset(
        data.info_hash,
        data.addr,
        json.dumps(
            {
                "peer_id": data.peer_id.hex(),
                "info_hash": data.info_hash,
                "peer_ip": data.ip,
                "port": client_port,
                "left": data.left,
            }
        ),
    )
    seeders = 0
    leechers = 0

    redis_data = await hget(data.info_hash)

    for peer in redis_data.values():
        peer = json.loads(peer)
        if peer["left"] == 0:
            seeders += 1
        else:
            leechers += 1
    response |= {
        "completed": seeders,
        "incompleted": leechers,
    }

    if data.action == "announce":
        response |= {
            "info_hash": data.info_hash,
            "interval": WEBSOCKET_INTERVAL,
        }
        await websocket.send_json(response)

    if not data.answer:
        await websocket.send_json(response)

    connection_manager.add_connection(data.peer_id.hex(), websocket)

    if (offers := data.offers) and isinstance(offers, list):
        for key, peer in redis_data.items():
            try:
                peer = json.loads(peer)

                for offer in offers:
                    # Peer doesn't exist in connection manager raises AttributeError
                    with contextlib.suppress(AttributeError):
                        peer_instance = connection_manager.get_connection(data.peer_id)
                        await peer_instance.send_json(
                            {
                                "action": "announce",
                                "offer": offer["offer"],
                                "offer_id": offer["offer_id"],
                                "peer_id": data.peer_id.hex(),
                                "info_hash": data.info_hash,
                            }
                        )

            # Cleanup stale peers
            except Exception:
                await hdel(data.info_hash, key)

    if data.answer:
        to_peer = connection_manager.get_connection(data.to_peer_id)

        if to_peer:
            await to_peer.send_json(
                {
                    "action": "announce",
                    "answer": data.answer,
                    "offer_id": data.offer_id,
                    "peer_id": data.peer_id.hex(),
                    "info_hash": data.info_hash,
                }
            )
