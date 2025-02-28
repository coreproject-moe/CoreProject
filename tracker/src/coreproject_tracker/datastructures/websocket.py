from attrs import define, field

from coreproject_tracker.constants import DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS
from coreproject_tracker.functions import (
    bin_str_to_hex_str,
    convert_ipv4_coded_ipv6_to_ipv4,
)
from coreproject_tracker.validators import validate_peer_length


@define
class WebsocketDatastructure:
    info_hash_raw: str = field()
    action: str = field()
    peer_id: str = field(validator=validate_peer_length)

    answer = field()

    to_peer_id = field(validator=validate_peer_length)
    left: int = field()

    offers = field()
    ip: str = field()

    # Derived
    info_hash = field(init=False)
    numwant: int = field(init=False)

    def __attrs_post_init__(self):
        self.info_hash = bin_str_to_hex_str(self.info_hash_raw)
        if offers := self.offers:
            self.numwant = min(
                len(offers) if offers else DEFAULT_ANNOUNCE_PEERS,
                MAX_ANNOUNCE_PEERS,
            )

        if ipv4_address := convert_ipv4_coded_ipv6_to_ipv4(self.ip):
            self.ip = ipv4_address
        else:
            self.ip = self.ip
