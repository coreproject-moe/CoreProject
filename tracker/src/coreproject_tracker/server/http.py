import bencodepy
from quart import Blueprint, request
from coreproject_tracker.functions import (
    hset,
    hget,
    hdel,
    get_n_random_items,
    check_ip_type,
    hex_to_bin,
)
from coreproject_tracker.constants import ANNOUNCE_INTERVAL
from coreproject_tracker.validators import HttpValidator
from http import HTTPStatus
import json
from coreproject_tracker.enums import EVENT_NAMES, IP

http_blueprint = Blueprint("http", __name__)


@http_blueprint.route("/")
async def http_endpoint():
    if len(request.args) == 0:
        return "🐟🐈 ⸜(｡˃ ᵕ ˂ )⸝♡"

    try:
        data = HttpValidator(**request.args, peer_ip=request.remote_addr)
    except Exception as e:
        return str(e), HTTPStatus.BAD_REQUEST

    if data.event == EVENT_NAMES.STOP:
        await hdel(data.info_hash, f"{data.peer_ip}:{data.port}")
        return ""

    await hset(
        data.info_hash,
        f"{data.peer_ip}:{data.port}",
        json.dumps(
            {
                "peer_id": data.peer_id,
                "info_hash": data.info_hash,
                "peer_ip": data.peer_ip,
                "port": data.port,
                "left": data.left,
            }
        ),
    )

    peers = []
    peers6 = []
    seeders = 0
    leechers = 0

    redis_data = await hget(data.info_hash)
    peers_list = await get_n_random_items(redis_data.values(), data.numwant)

    for peer in peers_list:
        # Local variables to make undo possible
        _peers = []
        _peers6 = []
        _seeders = 0
        _leechers = 0

        try:
            peer_data = json.loads(peer)

            if peer_data["left"] == 0:
                _seeders += 1
            else:
                _leechers += 1

            peer_ip = peer_data["peer_ip"]
            peer_ip_type = await check_ip_type(peer_ip)
            if peer_ip_type == IP.IPV4:
                _peers.append(
                    {
                        "peer id": await hex_to_bin(peer_data["peer_id"]),
                        "ip": peer_data["peer_ip"],
                        "port": peer_data["port"],
                    }
                )
            elif peer_ip_type == IP.IPV6:
                _peers6.append(
                    {
                        "peer id": await hex_to_bin(peer_data["peer_id"]),
                        "ip": peer_data["peer_ip"],
                        "port": peer_data["port"],
                    }
                )

        except (ValueError, KeyError):
            continue

        # This is here to make undo possible
        peers.extend(_peers)
        peers6.extend(_peers6)
        seeders += _seeders
        leechers += _leechers

    output = {
        "peers": peers,
        "peers6": peers6,
        "min interval": ANNOUNCE_INTERVAL,
        "complete": seeders,
        "incomplete": leechers,
    }
    return bencodepy.bencode(output)
