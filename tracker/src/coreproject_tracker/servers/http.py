from http import HTTPStatus
from importlib.metadata import version

import bencodepy
from quart import Blueprint, json, jsonify, request
from quart_redis import get_redis

from coreproject_tracker.constants import ANNOUNCE_INTERVAL
from coreproject_tracker.datastructures import HttpDatastructure
from coreproject_tracker.enums import EVENT_NAMES, IP
from coreproject_tracker.functions import (
    check_ip_type,
    convert_event_name_to_event_enum,
    get_n_random_items,
    hdel,
    hex_str_to_bin_str,
    hget,
    hset,
)

http_blueprint = Blueprint("http", __name__)


@http_blueprint.route("/")
async def http_endpoint():
    if len(request.args) == 0:
        return "🐟🐈 ⸜(｡˃ ᵕ ˂ )⸝♡"

    try:
        _data = {
            "info_hash_raw": request.args.get("info_hash"),
            "port": request.args.get("port"),
            "left": request.args.get("left"),
            "numwant": request.args.get("numwant"),
            "peer_ip": request.remote_addr,
            "peer_id": request.args.get("peer_id"),
        }
        if request.args.get("event"):
            _data |= {
                "event_name": await convert_event_name_to_event_enum(
                    request.args.get("event")
                ),
            }
        data = HttpDatastructure(**_data)
    except Exception as e:
        print(e)
        return str(e), HTTPStatus.BAD_REQUEST

    if data.event_name == EVENT_NAMES.STOP:
        await hdel(data.info_hash, f"{data.peer_ip}:{data.port}")
        return ""

    await hset(
        data.info_hash,
        f"{data.peer_ip}:{data.port}",
        json.dumps(
            {
                "peer_id": data.peer_id,
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

    redis_data = await hget(data.info_hash) or {}
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
            match peer_ip_type:
                case IP.IPV4:
                    _peers.append(
                        {
                            "peer id": await hex_str_to_bin_str(peer_data["peer_id"]),
                            "ip": peer_data["peer_ip"],
                            "port": peer_data["port"],
                        }
                    )
                case IP.IPV6:
                    _peers6.append(
                        {
                            "peer id": await hex_str_to_bin_str(peer_data["peer_id"]),
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


@http_blueprint.route("/api")
async def api_endpoint():
    r = get_redis()

    redis_information = await r.info()
    redis_server_version = redis_information["redis_version"]
    redis_client_version = version("redis")
    database_size = await r.dbsize()

    quart_version = version("quart")

    data = {
        "quart_version": quart_version,
        "redis_version": {
            "client": redis_client_version,
            "server": redis_server_version,
        },
        "total": {
            "torrents": database_size,
        },
    }
    return jsonify(data), HTTPStatus.OK
