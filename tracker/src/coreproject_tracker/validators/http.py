from attrs import define, field
from coreproject_tracker.constants import DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS
from coreproject_tracker.functions import (
    convert_event_name_to_event_enum,
    convert_ipv4_coded_ipv6_to_ipv4,
)
from coreproject_tracker.enums import EVENT_NAMES
import urllib.parse


def convert_to_url_bytes(value: str) -> bytes:
    return urllib.parse.unquote_to_bytes(value)


def convert_ip(value: str) -> str:
    if ipv4_address := convert_ipv4_coded_ipv6_to_ipv4(value):
        return ipv4_address
    else:
        return value


def convert_event(value: str):
    if value:
        convert_event_name_to_event_enum(value)


@define
class HttpValidator:
    info_hash_raw: bytes = field(converter=convert_to_url_bytes)
    port: int = field(converter=int)
    left: str = field(converter=int)
    numwant: str = field(converter=int)
    peer_id: str = field()
    peer_ip: str = field(converter=convert_ip)
    event: EVENT_NAMES = field(default=None, converter=convert_event)

    # Derived
    info_hash: bytes = field(init=False)

    @info_hash_raw.validator
    def _check_info_hash(self, attribute: str, value: bytes):
        if len(value) > 20:
            raise ValueError(
                f"`info_hash` of `{attribute}` length is {len(value)} which is greater than 20"
            )

    @port.validator
    def _check_port(self, attribute: str, value: int):
        if value <= 0 and value >= 65535:
            raise ValueError(
                f"`port` of {attribute} is {value} which is not in range(0, 65535)"
            )

    def __attrs_post_init__(self):
        self.numwant = min(self.numwant or DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS)
        self.info_hash = self.info_hash_raw.hex()
