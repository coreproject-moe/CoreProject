import struct
from typing import NoReturn

from attrs import define, field, validators

from coreproject_tracker.constants import (
    ANNOUNCE_INTERVAL,
    CONNECTION_ID,
    DEFAULT_ANNOUNCE_PEERS,
    MAX_ANNOUNCE_PEERS,
)
from coreproject_tracker.enums import EVENT_NAMES
from coreproject_tracker.functions import convert_event_id_to_event_enum
from coreproject_tracker.validators import validate_ip, validate_port


@define
class UdpDatastructure:
    # CONSTANT
    interval: int = field(
        init=False, default=ANNOUNCE_INTERVAL, validator=validators.instance_of(int)
    )

    connection_id: bytes = field(validator=validators.instance_of(bytes))
    action: int = field(validator=validators.instance_of(int))
    transaction_id: int = field(validator=validators.instance_of(int))

    # Only available on ANNOUNCE
    info_hash: bytes = field(default=None)  # 20 bytes
    peer_id: bytes = field(default=None)  # 20 bytes
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
    ip: str = field(default=None, validator=[validate_ip])
    port: int = field(default=None, validator=[validate_port])

    # Derived
    event_name: EVENT_NAMES = field(init=False)

    @connection_id.validator
    def _check_connection_id(self, attribute: str, value: bytes) -> NoReturn:
        connection_id_unpacked = struct.unpack(">Q", value)[0]
        if connection_id_unpacked != CONNECTION_ID:
            raise ValueError(
                f"`{connection_id_unpacked}` of `{attribute}` is not same as `{CONNECTION_ID}`"
            )

    def __attrs_post_init__(self):
        self.numwant = min(self.numwant, MAX_ANNOUNCE_PEERS)
        if self.event_id:
            self.event_name = convert_event_id_to_event_enum(self.event_id)
