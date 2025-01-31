import json
from http import HTTPStatus

import bencodepy
from twisted.internet import threads
from twisted.logger import Logger
from twisted.web import resource, server
from twisted.web.server import Request

from coreproject_tracker.constants import (
    ANNOUNCE_INTERVAL,
    DEFAULT_ANNOUNCE_PEERS,
    MAX_ANNOUNCE_PEERS,
)
from coreproject_tracker.enums import EVENT_NAMES, IP
from coreproject_tracker.functions import (
    bin_to_hex,
    check_ip_type,
    convert_event_name_to_event_enum,
    convert_ipv4_coded_ipv6_to_ipv4,
    convert_str_to_ip_object,
    get_n_random_items,
    hdel,
    hex_to_bin,
    hget,
    hset,
)

log = Logger(namespace="coreproject_tracker")


class HTTPServer(resource.Resource):
    isLeaf = True

    def render_GET(self, request: Request):
        deferred = threads.deferToThread(self.__render_GET, request)
        deferred.addCallback(self.on_task_done, request)
        deferred.addErrback(self.on_task_error, request)
        return server.NOT_DONE_YET

    def on_task_done(self, result, request):
        request.write(result)
        request.finish()

    def on_task_error(self, failure, request):
        print(failure)
        request.setResponseCode(HTTPStatus.BAD_REQUEST)
        request.write(bencodepy.bencode({"failure reason": failure.getErrorMessage()}))
        request.finish()

    def __render_GET(self, request: Request) -> bytes:
        if request.args == {}:
            request.setHeader("Content-Type", "text/html; charset=utf-8")
            return "🐟🐈 ⸜(｡˃ ᵕ ˂ )⸝♡".encode("utf-8")

        data = self.parse_data(request)

        if data["event"] == EVENT_NAMES.STOP:
            hdel(data["info_hash"], f"{data['peer_ip']}:{data['port']}")
            return b""

        hset(
            data["info_hash"],
            f"{data['peer_ip']}:{data['port']}",
            json.dumps(
                {
                    "peer_id": data["peer_id"],
                    "info_hash": data["info_hash"],
                    "peer_ip": data["peer_ip"],
                    "port": data["port"],
                    "left": data["left"],
                }
            ),
        )

        peers = []
        peers6 = []
        seeders = 0
        leechers = 0

        redis_data = hget(data["info_hash"])

        peers_list = get_n_random_items(redis_data.values(), data["numwant"])

        for peer in peers_list:
            peer_data = json.loads(peer)

            if peer_data["left"] == 0:
                seeders += 1
            else:
                leechers += 1

            peer_ip = peer_data["peer_ip"]
            peer_ip_type = check_ip_type(peer_ip)
            if peer_ip_type == IP.IPV4:
                peers.append(
                    {
                        "peer id": hex_to_bin(peer_data["peer_id"]),
                        "ip": peer_data["peer_ip"],
                        "port": peer_data["port"],
                    }
                )
            elif peer_ip_type == IP.IPV6:
                peers6.append(
                    {
                        "peer id": hex_to_bin(peer_data["peer_id"]),
                        "ip": peer_data["peer_ip"],
                        "port": peer_data["port"],
                    }
                )

        output = {
            "peers": peers,
            "peers6": peers6,
            "min interval": ANNOUNCE_INTERVAL,
            "complete": seeders,
            "incomplete": leechers,
        }
        return bencodepy.bencode(output)

    def parse_data(self, request: Request) -> dict[str, str | int] | str:
        params = {}

        info_hash_raw = request.args[b"info_hash"][0]
        info_hash = info_hash_raw.hex()
        if (info_hash_length := len(info_hash_raw)) > 20:
            raise ValueError(
                f"`info_hash` length is {info_hash_length} which is greater than 20"
            )
        params["info_hash"] = info_hash

        port = request.args[b"port"][0].decode()
        if not port.isdigit():
            raise ValueError("`port` is not an integer")
        port = int(port)
        if port <= 0 and port >= 65535:
            raise ValueError(f"`port` is {port} which is not in range(0, 65535)")
        params["port"] = port

        left = request.args[b"left"][0].decode()
        if not left.isdigit():
            raise ValueError("`left` is not an integer")
        left = int(left)
        params["left"] = left

        numwant = request.args[b"numwant"][0].decode()
        if not numwant.isdigit():
            raise ValueError(b"`numwant` is not an integer")
        numwant = int(numwant)
        params["numwant"] = min(numwant or DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS)

        peer_ip = request.getClientAddress().host
        if not convert_str_to_ip_object(peer_ip):
            raise ValueError("`peer_ip` is not a valid ip")

        if ipv4_address := convert_ipv4_coded_ipv6_to_ipv4(peer_ip):
            params["peer_ip"] = ipv4_address
        else:
            params["peer_ip"] = peer_ip

        peer_id = request.args[b"peer_id"][0].decode()
        if not isinstance(peer_id, str):
            raise ValueError("`peer_id` must be a str")
        params["peer_id"] = bin_to_hex(peer_id)

        try:
            event = request.args[b"event"][0].decode()
            if not isinstance(event, str):
                raise ValueError("`event` is not a string")
            params["event"] = convert_event_name_to_event_enum(event)

        # Webtorrent doesn't provide event
        except KeyError:
            params["event"] = None
        return params
