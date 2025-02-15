from werkzeug.datastructures import MultiDict
from coreproject_tracker.constants import DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS
from coreproject_tracker.functions import (
    convert_str_to_ip_object,
    bin_to_hex,
    convert_ipv4_coded_ipv6_to_ipv4,
    convert_event_name_to_event_enum,
)


async def parse_data(args: MultiDict[str, str]) -> dict[str, str | int] | str:
    params = {}

    info_hash_raw = args.get("info_hash").encode()
    info_hash = info_hash_raw.hex()
    if (info_hash_length := len(info_hash_raw)) > 20:
        raise ValueError(
            f"`info_hash` length is {info_hash_length} which is greater than 20"
        )
    params["info_hash"] = info_hash

    port = args.get("port")
    if not port.isdigit():
        raise ValueError("`port` is not an integer")
    port = int(port)
    if port <= 0 and port >= 65535:
        raise ValueError(f"`port` is {port} which is not in range(0, 65535)")
    params["port"] = port

    left = args["left"]
    if not left.isdigit():
        raise ValueError("`left` is not an integer")
    left = int(left)
    params["left"] = left

    numwant = args["numwant"]
    if not numwant.isdigit():
        raise ValueError("`numwant` is not an integer")
    numwant = int(numwant)
    params["numwant"] = min(numwant or DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS)

    peer_ip = request.getClientAddress().host
    if not convert_str_to_ip_object(peer_ip):
        raise ValueError("`peer_ip` is not a valid ip")

    if ipv4_address := convert_ipv4_coded_ipv6_to_ipv4(peer_ip):
        params["peer_ip"] = ipv4_address
    else:
        params["peer_ip"] = peer_ip

    peer_id = args["peer_id"]
    if not isinstance(peer_id, str):
        raise ValueError("`peer_id` must be a str")
    params["peer_id"] = bin_to_hex(peer_id)

    try:
        event = args["event"]
        if not isinstance(event, str):
            raise ValueError("`event` is not a string")
        params["event"] = convert_event_name_to_event_enum(event)

    # Webtorrent doesn't provide event
    except KeyError:
        params["event"] = None

    return params
