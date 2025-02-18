from attrs import define, field
from coreproject_tracker.constants import (
    CONNECTION_ID,
    DEFAULT_ANNOUNCE_PEERS,
    MAX_ANNOUNCE_PEERS,
    ANNOUNCE_INTERVAL,
)

import struct


def max_20_length(instance: "UdpValidator", attribute: str, value: bytes):
    if (length := len(value)) != 20:
        raise ValueError(f"{attribute} of {instance} is larger than 20. It is {length}")


@define
class UdpValidator:
    connection_id: bytes = field()
    action: int = field()
    transaction_id: int = field()

    # Inherited from constants
    interval: int = field(default=ANNOUNCE_INTERVAL)

    # Only available on ANNOUNCE
    info_hash: bytes = field(default=None, validator=[max_20_length])  # 20 bytes
    peer_id: bytes = field(default=None, validator=[max_20_length])  # 20 bytes
    downloaded: int = field(default=None)
    left: int = field(default=None)
    uploaded: int = field(default=None)
    event_id: int = field(default=None)  # 0/1/2/3
    key: int = field(default=None)
    numwant: int = field(default=DEFAULT_ANNOUNCE_PEERS)

    # Set from function call
    peers: bytes = field(default=None)  # TODO: make a log_2 based validator here
    incomplete: int = field(default=0)
    complete: int = field(default=0)

    # Might not need these
    ip: str = field(default=None)
    port: int = field(default=None)
    addr: str = field(default=None)

    @connection_id.validator
    def _check_connection_id(self, attribute: str, value: bytes):
        connection_id_unpacked = struct.unpack(">Q", value)[0]
        if value != CONNECTION_ID:
            raise ValueError(
                f"`{connection_id_unpacked}` of `{attribute}` is not same as `{CONNECTION_ID}`"
            )

    def __attrs_post_init__(self):
        self.numwant = min(self.numwant, MAX_ANNOUNCE_PEERS)
