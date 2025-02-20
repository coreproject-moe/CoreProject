from typing import NoReturn

from attrs import define, field

from coreproject_tracker.constants import DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS
from coreproject_tracker.converters import (
    convert_ip,
    convert_to_url_bytes,
)
from coreproject_tracker.enums import EVENT_NAMES
from coreproject_tracker.functions import (
    convert_event_name_to_event_enum,
)


@define
class HttpValidator:
    info_hash_raw: bytes = field(converter=convert_to_url_bytes)
    port: int = field(converter=int)
    left: str = field(converter=int)
    numwant: str = field(converter=int)
    peer_id: str = field()
    peer_ip: str = field(converter=convert_ip)
    event: int = field(default=None)

    # Derived
    info_hash: bytes = field(init=False)
    event_name: EVENT_NAMES = field(init=False)

    @info_hash_raw.validator
    def _check_info_hash(self, attribute: str, value: bytes) -> NoReturn:
        if len(value) > 20:
            raise ValueError(
                f"`info_hash` of `{attribute}` length is {len(value)} which is greater than 20"
            )

    @port.validator
    def _check_port(self, attribute: str, value: int) -> NoReturn:
        if value <= 0 and value >= 65535:
            raise ValueError(
                f"`port` of {attribute} is {value} which is not in range(0, 65535)"
            )

    def __attrs_post_init__(self) -> NoReturn:
        self.numwant = min(self.numwant or DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS)

        # Derived Data
        self.info_hash = self.info_hash_raw.hex()
        if self.event:
            self.event_name = convert_event_name_to_event_enum(self.event)
