import logging
import platform
from http import HTTPStatus
from importlib.metadata import version
from typing import cast

import bencodepy  # type: ignore
from quart import Blueprint, json, jsonify, request
from quart_redis import get_redis  # type: ignore

from coreproject_tracker.constants import ANNOUNCE_INTERVAL
from coreproject_tracker.datastructures import (
    HttpDatastructure,
    MutableBox,
    RedisDatastructure,
)
from coreproject_tracker.enums import EVENT_NAMES, IP
from coreproject_tracker.functions import (
    check_ip_type,
    convert_event_name_to_event_enum,
    decode_dictionary,
    get_all_hash_keys,
    get_n_random_items,
    hdel,
    hget,
)
from coreproject_tracker.transaction import rollback_on_exception

http_blueprint = Blueprint("http", __name__)


@http_blueprint.route("/announce")
async def http_endpoint():
    ip = request.headers.get("X-Real-IP", request.remote_addr)

    if len(request.args) == 0:
        return f"🐟🐈 ⸜(｡˃ ᵕ ˂ )⸝♡ {ip}"

    try:
        _data = {
            "info_hash_raw": request.args.get("info_hash"),
            "port": request.args.get("port"),
            "left": request.args.get("left"),
            "numwant": request.args.get("numwant"),
            "peer_ip": ip,
            "peer_id": request.args.get("peer_id"),
        }
        if request.args.get("event"):
            event_enum = await convert_event_name_to_event_enum(
                request.args.get("event")
            )
            _data |= {"event_name": event_enum}
        data = HttpDatastructure(**_data)  # type: ignore[call-arg]

    except Exception as e:
        print(e)
        return str(e), HTTPStatus.BAD_REQUEST

    if data.event_name == EVENT_NAMES.STOP:
        await hdel(data.info_hash, f"{data.peer_ip}:{data.port}")
        return ""

    redis_stroage = RedisDatastructure(
        info_hash=data.info_hash,
        type="http",
        peer_id=data.peer_id,
        peer_ip=data.peer_ip,
        port=data.port,
        left=data.left,
    )

    await redis_stroage.save()

    peers = peers6 = MutableBox[list[dict[str, str]]]([])
    seeders = leechers = MutableBox[int](0)

    redis_data = await hget(data.info_hash) or {}

    for peer in await get_n_random_items(redis_data.values(), data.numwant):
        try:
            peer = cast(str, peer)
            with rollback_on_exception(peers, peers6, seeders, leechers):
                peer_data = RedisDatastructure(**json.loads(peer))

                if peer_data.left == 0:
                    seeders.value += 1
                else:
                    leechers.value += 1

                appendable_data = {
                    "peer id": peer_data.peer_id,
                    "ip": peer_data.peer_ip,
                    "port": peer_data.port,
                }

                match await check_ip_type(peer_data.peer_ip):
                    case IP.IPV4:
                        peers.value.append(appendable_data)
                    case IP.IPV6:
                        peers6.value.append(appendable_data)

        except TypeError:
            # Error in the peer data, delete the peer
            logging.error(f"Error in peer data, deleting the peer: {data.peer_id}")
            await hdel(data.info_hash, f"{data.peer_ip}:{data.port}")

    output = {
        "peers": peers.value,
        "peers6": peers6.value,
        "min interval": ANNOUNCE_INTERVAL,
        "complete": seeders.value,
        "incomplete": leechers.value,
    }
    logging.info(
        f"Sent HTTP response for {data.info_hash}. Event: {data.event_name}. Peers: {len(peers.value)}. Peers6: {len(peers6.value)}."
    )
    return bencodepy.bencode(output)


@http_blueprint.route("/api")
async def api_endpoint():
    r = get_redis()

    redis_information = await r.info()
    redis_server_version = redis_information["redis_version"]
    redis_client_version = version("redis")

    quart_version = version("quart")

    python_version = platform.python_version()

    hash_keys = await get_all_hash_keys()
    pipe = await r.pipeline()
    for hash_key in hash_keys:
        await pipe.hgetall(hash_key)  # type: ignore[no-untyped-call]
    hash_data = await pipe.execute()

    result = dict(zip(hash_keys, hash_data))
    result = await decode_dictionary(result)

    data = {
        "quart_version": quart_version,
        "redis_version": {
            "client": redis_client_version,
            "server": redis_server_version,
        },
        "python_version": python_version,
        "redis_data": result,
    }
    return jsonify(data), HTTPStatus.OK
