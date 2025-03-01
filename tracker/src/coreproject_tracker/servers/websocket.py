import json

from quart import Blueprint, Websocket, websocket

from coreproject_tracker.constants import WEBSOCKET_INTERVAL
from coreproject_tracker.datastructures import WebsocketDatastructure
from coreproject_tracker.functions import (
    hdel,
    hex_str_to_bin_str,
    bin_str_to_hex_str,
    hget,
    hset,
)
from collections import defaultdict

from coreproject_tracker.managers import WebsocketConnectionManager

ws_blueprint = Blueprint("websocket", __name__)
connections = {}
connection_manager = WebsocketConnectionManager()


@ws_blueprint.websocket("/")
async def ws():
    """WebSocket endpoint that listens for incoming messages and publishes them."""
    try:
        initial_message = await websocket.receive_json()
        client_ip, client_port = websocket.scope.get("client")

        _data = {
            # Constants
            "ip": client_ip,
            # Required attributes
            "info_hash_raw": initial_message["info_hash"],
            "action": initial_message["action"],
            "peer_id": initial_message["peer_id"],
            "numwant": initial_message.get("numwant"),  # Ensure default value
            "uploaded": initial_message["uploaded"],
            "offers": initial_message["offers"],  # Default to empty list
            "left": initial_message["left"],
            "event": initial_message.get("event"),
        }

        data = WebsocketDatastructure(**_data)
        connections[data.peer_id.hex()] = websocket

        while True:
            if initial_message.get("answer"):
                _data |= {
                    "to_peer_id": initial_message["to_peer_id"],
                }
                data = WebsocketDatastructure(**_data)

            response = {
                "action": data.action,
            }

            await hset(
                data.info_hash,
                f"{client_ip}:{client_port}",
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

            redis_data = await hget(data.info_hash) or {}  # Ensure non-None value

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
                    "info_hash": await hex_str_to_bin_str(data.info_hash),
                    "interval": WEBSOCKET_INTERVAL,
                }
                await websocket.send(json.dumps(response))

            if not initial_message.get("answer"):
                await websocket.send(json.dumps(response))

            if offers := data.offers:
                for key, value in redis_data.items():
                    peer = json.loads(value)

                    peer_instance = connections[peer["peer_id"]]
                    if not peer_instance:
                        continue

                    print(peer_instance)
                    for offer in offers:
                        await peer_instance.send(
                            json.dumps(
                                {
                                    "action": "announce",
                                    "offer": offer["offer"],
                                    "offer_id": offer["offer_id"],
                                    "peer_id": await hex_str_to_bin_str(
                                        data.peer_id.hex()
                                    ),
                                    "info_hash": await hex_str_to_bin_str(
                                        data.info_hash
                                    ),
                                }
                            )
                        )

            if data.answer:
                to_peer = await connection_manager.get_connection(
                    await bin_str_to_hex_str(data.to_peer_id)
                )

                if to_peer:
                    await to_peer.send(
                        json.dumps(
                            {
                                "action": "announce",
                                "answer": data.answer,
                                "offer_id": data.offer_id,
                                "peer_id": await hex_str_to_bin_str(data.peer_id),
                                "info_hash": await hex_str_to_bin_str(data.info_hash),
                            }
                        )
                    )

            await websocket.receive_json()
    except Exception:
        pass
    finally:
        del connections[data.peer_id.hex()]
