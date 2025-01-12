import contextlib
import json

from autobahn.exception import Disconnected
from autobahn.twisted.websocket import WebSocketServerProtocol
from twisted.internet import reactor, threads

from coreproject_tracker.constants import (
    DEFAULT_ANNOUNCE_PEERS,
    MAX_ANNOUNCE_PEERS,
    WEBSOCKET_INTERVAL,
)
from coreproject_tracker.functions import (
    bin_to_hex,
    convert_ipv4_coded_ipv6_to_ipv4,
    hdel,
    hex_to_bin,
    hget,
    hset,
)
from coreproject_tracker.singletons import WebsocketConnectionManager


class WebSocketServer(WebSocketServerProtocol):
    __connection_manager = WebsocketConnectionManager()

    def onMessage(self, payload, isBinary):
        """
        Called when a message is received from the client.
        """
        threads.deferToThread(self.__onMessage, payload, isBinary)

    def __sendMessage(self, message, isBinary):
        reactor.callFromThread(self.sendMessage, message, isBinary)

    def __onMessage(self, payload, isBinary):
        payload = payload.decode("utf8") if not isBinary else payload
        params = json.loads(payload)
        try:
            data = self.parse_websocket(params)
        except ValueError as e:
            self.sendMessage(
                json.dumps(
                    {
                        "failure reason": e,
                    }
                ),
                isBinary,
            )

        response = {}
        response["action"] = data["action"]
        hset(
            data["info_hash"],
            data["addr"],
            json.dumps(
                {
                    "peer_id": data["peer_id"],
                    "info_hash": data["info_hash"],
                    "peer_ip": data["ip"],
                    "port": data["port"],
                    "left": data["left"],
                }
            ),
        )

        seeders = 0
        leechers = 0

        redis_data = hget(data["info_hash"])

        for peer in redis_data.values():
            peer = json.loads(peer)
            if peer["left"] == 0:
                seeders += 1
            else:
                leechers += 1

        response["completed"] = seeders
        response["incompleted"] = leechers

        if response["action"] == "announce":
            response["info_hash"] = hex_to_bin(params["info_hash"])
            response["interval"] = WEBSOCKET_INTERVAL
            self.__sendMessage(json.dumps(response).encode(), isBinary)

        if not params.get("answer"):
            self.__sendMessage(json.dumps(response).encode(), isBinary)

        self.__connection_manager.add_connection(data["peer_id"], self)

        if (offers := params.get("offers")) and isinstance(offers, list):
            for key, peer in redis_data.items():
                try:
                    peer = json.loads(peer)

                    for offer in offers:
                        # Peer doesn't exist in connection manager raises AttributeError
                        with contextlib.suppress(AttributeError):
                            peer_instance = self.__connection_manager.get_connection(
                                peer["peer_id"]
                            )
                            peer_instance.sendMessage(
                                json.dumps(
                                    {
                                        "action": "announce",
                                        "offer": offer["offer"],
                                        "offer_id": offer["offer_id"],
                                        "peer_id": hex_to_bin(params["peer_id"]),
                                        "info_hash": hex_to_bin(params["info_hash"]),
                                    }
                                ).encode(),
                                isBinary,
                            )

                # Cleanup stale peers
                except Disconnected:
                    hdel(data["info_hash"], key)

        if params.get("answer"):
            to_peer = self.__connection_manager.get_connection(
                bin_to_hex(data["to_peer_id"])
            )

            if to_peer:
                to_peer.sendMessage(
                    json.dumps(
                        {
                            "action": "announce",
                            "answer": params["answer"],
                            "offer_id": params["offer_id"],
                            "peer_id": hex_to_bin(params["peer_id"]),
                            "info_hash": hex_to_bin(params["info_hash"]),
                        }
                    ).encode(),
                    isBinary,
                )

    def __sendMessage(self, message, isBinary):
        reactor.callFromThread(self.sendMessage, message, isBinary)

    def parse_websocket(self, params={}):
        params["type"] = "ws"

        if params["action"] == "announce":
            info_hash_raw = params["info_hash"]
            if not isinstance(info_hash_raw, str):
                raise ValueError("`info_hash` is not a str")
            if (info_hash_length := len(info_hash_raw)) != 20:
                raise ValueError(
                    f"`info_hash` is not a 20 bytes, it is {info_hash_length}"
                )
            info_hash = bin_to_hex(info_hash_raw)
            params["info_hash"] = info_hash

            peer_id = params["peer_id"]
            if not isinstance(peer_id, str):
                raise ValueError("`peer_id` is not a str")
            if (peer_id_length := len(peer_id)) != 20:
                raise ValueError(f"`peer_id` is not a 20 bytes, it is {peer_id_length}")
            params["peer_id"] = bin_to_hex(peer_id)

            if params.get("answer"):
                to_peer_id = params["to_peer_id"]
                if not isinstance(to_peer_id, str):
                    raise ValueError("`to_peer_id` is not a str")
                if (to_peer_id_length := len(peer_id)) != 20:
                    raise ValueError(
                        f"`to_peer_id` is not a 20 bytes, it is {to_peer_id_length}"
                    )
                to_peer_id = bin_to_hex(to_peer_id)

            try:
                params["left"] = (
                    float(params["left"])
                    if params["left"] is not None
                    else float("inf")
                )

            except (ValueError, TypeError, KeyError):
                params["left"] = float("inf")

            offers = params.get("offers")
            params["numwant"] = min(
                len(offers) if offers else DEFAULT_ANNOUNCE_PEERS,
                MAX_ANNOUNCE_PEERS,
            )

        client_ip = self.transport.getPeer().host
        client_port = self.transport.getPeer().port

        if ipv4_address := convert_ipv4_coded_ipv6_to_ipv4(client_ip):
            params["ip"] = ipv4_address
        else:
            params["ip"] = client_ip

        params["port"] = client_port
        params["addr"] = f"{client_ip}:{client_port}"
        return params
