import json

from quart import Blueprint, websocket, Websocket, copy_current_websocket_context

from coreproject_tracker.constants import WEBSOCKET_INTERVAL
from coreproject_tracker.datastructures import WebsocketDatastructure
from coreproject_tracker.functions import hex_str_to_bin_str, hget, hset, hdel
from coreproject_tracker.managers import WebsocketConnectionManager

ws_blueprint = Blueprint("websocket", __name__)

connection_manager = WebsocketConnectionManager()
weboscket_dict = {}


@ws_blueprint.websocket("/")
async def ws():
    """WebSocket endpoint that listens for incoming messages and publishes them."""
    while True:
        initial_message = await websocket.receive_json()

        client_ip, client_port = websocket.scope.get("client")

        _data = {
            # Constants
            "ip": client_ip,
            "addr": f"{client_ip}:{client_port}",
            # Required attributes
            "info_hash_raw": initial_message["info_hash"],
            "action": initial_message["action"],
            "peer_id": initial_message["peer_id"],
            "numwant": initial_message.get("numwant"),  # Ensure default value
            "uploaded": initial_message["uploaded"],
            "offers": initial_message.get("offers", []),  # Default to empty list
            "left": initial_message["left"],
            "event": initial_message.get("event"),
            # Optional
            "answer": initial_message.get("answer"),
            "offer_id": initial_message.get("offer_id"),
            "to_peer_id": initial_message.get("to_peer_id"),
        }

        data = WebsocketDatastructure(**_data)
        weboscket_dict[data.peer_id.hex()] = websocket

        response = {"action": data.action}

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

        if not data.answer:
            await websocket.send(json.dumps(response))

        if offers := data.offers:
            for key, value in redis_data.items():
                peer = json.loads(value)

                try:
                    peer_instance: Websocket = weboscket_dict[peer["peer_id"]]
                except KeyError:
                    await hdel(data.info_hash, key)
                    continue

                for offer in offers:
                    await peer_instance.send(
                        json.dumps(
                            {
                                "action": "announce",
                                "offer": offer["offer"],
                                "offer_id": offer["offer_id"],
                                "peer_id": await hex_str_to_bin_str(data.peer_id.hex()),
                                "info_hash": await hex_str_to_bin_str(data.info_hash),
                            }
                        )
                    )

        if data.answer:
            to_peer = await connection_manager.get_connection(data.to_peer_id.hex())

            if to_peer:
                await to_peer.send(
                    json.dumps(
                        {
                            "action": "announce",
                            "answer": data.answer,
                            "offer_id": data.offer_id,
                            "peer_id": await hex_str_to_bin_str(data.peer_id.hex()),
                            "info_hash": await hex_str_to_bin_str(data.info_hash),
                        }
                    )
                )
