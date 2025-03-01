import asyncio
import json

from quart import Blueprint, websocket

from coreproject_tracker.constants import WEBSOCKET_INTERVAL
from coreproject_tracker.datastructures import WebsocketDatastructure
from coreproject_tracker.functions import (
    hdel,
    hex_str_to_bin_str,
    hget,
    hset,
)
from coreproject_tracker.managers import WebsocketConnectionManager

ws_blueprint = Blueprint("websocket", __name__)
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
            "numwant": initial_message.get("numwant"),
            "uploaded": initial_message["uploaded"],
            "offers": initial_message["offers"],
            "left": initial_message.get("left"),
            "event": initial_message.get("event"),
        }

        data = WebsocketDatastructure(**_data)

        ws_obj = websocket._get_current_object()
        await connection_manager.add_connection(data.peer_id.hex(), ws_obj)

        while True:
            if initial_message.get("answer"):
                _data |= {
                    "answer": initial_message["answer"],
                    "to_peer_id": initial_message["to_peer_id"],
                    "offer_id": initial_message["offer_id"],
                }
                data = WebsocketDatastructure(**_data)

            response = {"action": data.action}

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

            response |= {"completed": seeders, "incompleted": leechers}

            if data.action == "announce":
                response |= {
                    "info_hash": await hex_str_to_bin_str(data.info_hash),
                    "interval": WEBSOCKET_INTERVAL,
                }
                await websocket.send_json(response)

            if not initial_message.get("answer"):
                await websocket.send_json(response)

            if offers := data.offers:
                for key, value in redis_data.items():
                    peer = json.loads(value)

                    for offer in offers:
                        peer_instance = await connection_manager.get_connection(
                            peer["peer_id"]
                        )
                        if not peer_instance:
                            await hdel(data.info_hash, key)
                            continue

                        await peer_instance.send_json(
                            {
                                "action": "announce",
                                "offer": offer["offer"],
                                "offer_id": offer["offer_id"],
                                "peer_id": await hex_str_to_bin_str(data.peer_id.hex()),
                                "info_hash": await hex_str_to_bin_str(data.info_hash),
                            }
                        )

            if data.answer:
                to_peer = await connection_manager.get_connection(data.to_peer_id.hex())

                if to_peer:
                    await to_peer.send_json(
                        {
                            "action": "announce",
                            "answer": data.answer,
                            "offer_id": data.offer_id,
                            "peer_id": await hex_str_to_bin_str(data.peer_id.hex()),
                            "info_hash": await hex_str_to_bin_str(data.info_hash),
                        }
                    )

            initial_message = await websocket.receive_json()
            _data = {
                "ip": client_ip,
                # Required attributes
                "info_hash_raw": initial_message["info_hash"],
                "action": initial_message["action"],
                "peer_id": initial_message["peer_id"],
                "numwant": initial_message.get("numwant"),
                "offers": initial_message.get("offers"),  # Default to empty list
                "left": initial_message.get("left"),
                "event": initial_message.get("event"),
            }

            data = WebsocketDatastructure(**_data)

    except asyncio.CancelledError:
        print("Connection closed")

    finally:
        await connection_manager.remove_connection(data.peer_id.hex())
