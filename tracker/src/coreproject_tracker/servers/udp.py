import json
import struct

from twisted.internet import threads
from twisted.internet.protocol import DatagramProtocol
from twisted.logger import Logger

from coreproject_tracker.constants import (
    ANNOUNCE_INTERVAL,
    CONNECTION_ID,
    DEFAULT_ANNOUNCE_PEERS,
    MAX_ANNOUNCE_PEERS,
)
from coreproject_tracker.enums import ACTIONS, EVENT_NAMES
from coreproject_tracker.functions import (
    addrs_to_compact,
    convert_event_id_to_event_enum,
    from_uint16,
    from_uint32,
    from_uint64,
    get_n_random_items,
    hdel,
    hget,
    hset,
    to_uint32,
)

log = Logger(namespace="coreproject_tracker")


class UDPServer(DatagramProtocol):
    def datagramReceived(self, data, addr):
        deferred = threads.deferToThread(self.__datagramReceived, data, addr)
        deferred.addCallback(self.on_task_done, addr)
        deferred.addErrback(self.on_task_error, addr)
        # res = self._datagramReceived(data, addr)
        # self.on_task_done(res, addr)

    def on_task_done(self, result, addr):
        self.transport.write(result, addr)

    def on_task_error(self, failure, addr):
        print(failure)
        self.transport.write(failure.getErrorMessage(), addr)

    def __datagramReceived(self, data, addr):
        """
        Called when a datagram (UDP packet) is received.

        - `data`: The received message.
        - `addr`: The address of the sender (tuple of IP and port).
        """
        if (packet_length := len(data)) < 16:
            log.error(
                f"received packet length is {packet_length} is shorter than 16 bytes"
            )

        param = self.parse_udp_packet(data, addr)
        if param["action"] == ACTIONS.ANNOUNCE:
            hset(
                param["info_hash"],
                f"{param['ip']}:{param['port']}",
                json.dumps(
                    {
                        "peer_id": param["peer_id"],
                        "info_hash": param["info_hash"],
                        "peer_ip": param["ip"],
                        "port": param["port"],
                        "left": param["left"],
                    }
                ),
            )

            peers = []
            seeders = 0
            leechers = 0

            redis_data = hget(param["info_hash"])
            peers_list = get_n_random_items(redis_data.values(), param["numwant"])

            for peer in peers_list:
                peer_data = json.loads(peer)

                if peer_data["left"] == 0:
                    seeders += 1
                else:
                    leechers += 1

                peers.append(f"{peer_data['peer_ip']}:{peer_data['port']}")

            param["peers"] = addrs_to_compact(peers)

            param["complete"] = seeders
            param["incomplete"] = leechers
            param["interval"] = ANNOUNCE_INTERVAL

        if param.get("event") == EVENT_NAMES.STOP:
            hdel(param["info_hash"], f"{param['ip']}:{param['port']}")

        res = self.make_udp_packet(param)
        return res

    def parse_udp_packet(self, msg, addr):
        connection_id = msg[:8]
        connection_id_unpacked = struct.unpack(">Q", msg[:8])[0]
        if connection_id_unpacked != CONNECTION_ID:
            raise ValueError(
                f"'{connection_id_unpacked}' is not same as {CONNECTION_ID}"
            )

        action = from_uint32(msg[8:12])
        transaction_id = from_uint32(msg[12:16])

        # Construct the result (similar to the JavaScript object)
        params = {
            "connection_id": connection_id,
            "action": action,
            "transaction_id": transaction_id,
        }

        if params["action"] == ACTIONS.ANNOUNCE:
            params["info_hash"] = msg[16:36].hex()  # 20 bytes
            params["peer_id"] = msg[36:56].hex()  # 20 bytes
            params["downloaded"] = from_uint64(
                msg[56:64]
            )  # Convert 64-bit unsigned integer
            params["left"] = from_uint64(msg[64:72])  # Convert 64-bit unsigned integer
            params["uploaded"] = from_uint64(
                msg[72:80]
            )  # Convert 64-bit unsigned integer

            # Read 4-byte unsigned int (big-endian)
            event_id = struct.unpack(">I", msg[80:84])[0]
            params["event"] = convert_event_id_to_event_enum(event_id)

            ip = from_uint32(msg[84:88]) or addr[0]

            params["ip"] = ip

            params["key"] = from_uint32(msg[88:92])

            params["numwant"] = min(
                from_uint32(msg[92:96]) or DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS
            )
            params["port"] = from_uint16(msg[96:98]) or addr[1]
            params["addr"] = f"{params['ip']}:{params['port']}"

        return params

    def make_udp_packet(self, params: dict[str, int | bytes | dict]) -> bytes:
        """
        Create UDP packets for BitTorrent tracker protocol.

        Args:
            params: Dictionary containing packet parameters including 'action' and other
                action-specific parameters.

        Returns:
            bytes: The constructed UDP packet

        Raises:
            ValueError: If the action is not implemented
        """
        action = params["action"]
        if action == ACTIONS.CONNECT:
            packet = b"".join(
                [
                    to_uint32(ACTIONS.CONNECT),
                    to_uint32(params["transaction_id"]),
                    params["connection_id"],
                ]
            )

        elif action == ACTIONS.ANNOUNCE:
            packet = b"".join(
                [
                    to_uint32(ACTIONS.ANNOUNCE),
                    to_uint32(params["transaction_id"]),
                    to_uint32(params["interval"]),
                    to_uint32(params["incomplete"]),
                    to_uint32(params["complete"]),
                    params["peers"],
                ]
            )

        elif action == ACTIONS.SCRAPE:
            scrape_response = [
                to_uint32(ACTIONS.SCRAPE),
                to_uint32(params["transaction_id"]),
            ]

            for info_hash, file in params["files"].items():
                scrape_response.extend(
                    [
                        to_uint32(file["complete"]),
                        to_uint32(
                            file["downloaded"]
                        ),  # Note: this only provides a lower-bound
                        to_uint32(file["incomplete"]),
                    ]
                )

            packet = b"".join(scrape_response)

        elif action == ACTIONS.ERROR:
            packet = b"".join(
                [
                    to_uint32(ACTIONS.ERROR),
                    to_uint32(params.get("transaction_id", 0)),
                    str(params.get("failure_reason", "")).encode(),
                ]
            )

        else:
            raise ValueError(f"Action not implemented: {action}")

        return packet
