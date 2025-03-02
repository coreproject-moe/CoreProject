import asyncio
import json
from typing import cast

from quart import Blueprint, Websocket, copy_current_websocket_context, websocket

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
from coreproject_tracker.managers import WebsocketConnectionManager

ws_blueprint = Blueprint("websocket", __name__)
connection_manager = WebsocketConnectionManager()


@ws_blueprint.websocket("/")
async def ws():
    """WebSocket endpoint that listens for incoming messages and publishes them."""

    @copy_current_websocket_context
    async def parse_websocket() -> WebsocketDatastructure:
        initial_message = await websocket.receive_json()
        client_ip, client_port = websocket.scope.get("client")

        _data = {
            # Constants
            "ip": client_ip,
            "port": client_port,
            "addr": f"{client_ip}:{client_port}",
            # Required attributes
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
    try:
        ws_obj = cast(Websocket, websocket._get_current_object())
        await connection_manager.add_connection(data.peer_id.hex(), ws_obj)

        while True:
            if data.event == EVENT_NAMES.STOP:
                await connection_manager.remove_connection(data.peer_id.hex())
                await websocket.close()

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

            redis_data = await hget(data.info_hash) or {}  # Ensure non-None value

            for peer in redis_data.values():
                peer = json.loads(peer)
                if peer["left"] == 0:
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
                                "peer_id": await bytes_to_bin_str(data.peer_id),
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
                            "peer_id": await bytes_to_bin_str(data.peer_id),
                            "info_hash": await hex_str_to_bin_str(data.info_hash),
                        }
                    )

            data = await parse_websocket()

    except asyncio.CancelledError:
        print("Connection closed")

    finally:
        await connection_manager.remove_connection(data.peer_id.hex())
