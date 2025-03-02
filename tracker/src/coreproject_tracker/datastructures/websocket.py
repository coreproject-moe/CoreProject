from attrs import define, field, validators

from coreproject_tracker.constants import DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS
from coreproject_tracker.converters import convert_binary_string_to_bytes
from coreproject_tracker.enums import EVENT_NAMES
from coreproject_tracker.validators import (
    validate_20_length,
    validate_ip,
    validate_peer_length,
    validate_port,
)


@define
class WebsocketDatastructure:
    info_hash_raw: bytes = field(
        converter=convert_binary_string_to_bytes,
        validator=[validate_20_length],
    )
    action: str = field(validator=[validators.instance_of(str)])
    peer_id: bytes = field(
        converter=convert_binary_string_to_bytes,
        validator=[validate_peer_length],
    )
    ip: str = field(validator=[validate_ip])
    port: int = field(validator=[validate_port])
    addr: str = field(validator=[validators.instance_of(str)])

    # Hardcoded
    left: float = field(default=float("inf"))
    numwant: int = field(default=DEFAULT_ANNOUNCE_PEERS)
    offers: list[dict[str, str | dict[str, str]]] = field(default=[])

    # Optional
    event: EVENT_NAMES = field(default=None)
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
                self.numwant,
                len(offers) if offers else DEFAULT_ANNOUNCE_PEERS,
                MAX_ANNOUNCE_PEERS,
            )
