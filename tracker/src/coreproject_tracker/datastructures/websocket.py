from attrs import define, field, validators

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

    left: int = field()

    offers: list[dict[str, str | dict[str, str]]] = field()
    offer_id = field()
    ip: str = field()
    uploaded: int = field()
    event: str = field()
    addr: str = field()

    # Optional
    answer = field(default=None)
    to_peer_id: bytes = field(
        default=None,
        converter=convert_binary_string_to_bytes,
        validator=[validate_peer_length],
    )

    # Derived
    info_hash: str = field(init=False)
    numwant: int = field(init=False)

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
