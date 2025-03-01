from attrs import define, field

from coreproject_tracker.constants import DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS
from coreproject_tracker.converters import convert_binary_string_to_bytes
from coreproject_tracker.functions import (
    convert_ipv4_coded_ipv6_to_ipv4,
)
from coreproject_tracker.validators import validate_info_hash, validate_peer_length


@define
class WebsocketDatastructure:
    info_hash_raw: bytes = field(
        converter=convert_binary_string_to_bytes,
        validator=[validate_info_hash],
    )
    action: str = field()
    peer_id: bytes = field(
        converter=convert_binary_string_to_bytes,
        validator=[validate_peer_length],
    )

    ip: str = field()

    # Hardcoded
    left: float = field(default=float("inf"))
    numwant: int = field(default=DEFAULT_ANNOUNCE_PEERS)
    offers: list[dict[str, str | dict[str, str]]] = field(default=[])

    # Optional
    event: str = field(default=None)
    uploaded: int = field(default=None)
    answer = field(default=None)
    to_peer_id: bytes = field(
        default=None,
        converter=convert_binary_string_to_bytes,
        validator=[validate_peer_length],
    )
    offer_id: bytes = field(default=None)
    # Derived
    info_hash: str = field(init=False)

    def __attrs_post_init__(self):
        # Derived Data
        self.info_hash = self.info_hash_raw.hex()

        if offers := self.offers:
            self.numwant = min(
                len(offers) if offers else DEFAULT_ANNOUNCE_PEERS,
                MAX_ANNOUNCE_PEERS,
            )

        if ipv4_address := convert_ipv4_coded_ipv6_to_ipv4(self.ip):
            self.ip = ipv4_address
        else:
            self.ip = self.ip
