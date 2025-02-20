from typing import NoReturn

from attrs import define, field, validators

from coreproject_tracker.constants import DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS
from coreproject_tracker.converters import (
    convert_ip,
    convert_to_url_bytes,
)
from coreproject_tracker.enums import EVENT_NAMES
from coreproject_tracker.functions import (
    convert_event_name_to_event_enum,
)
from coreproject_tracker.validators import (
    validate_info_hash,
    validate_ip,
    validate_port,
)


@define
class HttpDatastructure:
    info_hash_raw: bytes = field(
        converter=convert_to_url_bytes,
        validator=[validators.instance_of(bytes), validate_info_hash],
    )
    port: int = field(converter=int, validator=[validate_port])
    left: str = field(converter=int, validator=validators.instance_of(int))
    numwant: str = field(converter=int, validator=validators.instance_of(int))
    peer_id: str = field(validator=validators.instance_of(str))
    peer_ip: str = field(converter=convert_ip, validator=[validate_ip])
    event: int = field(default=None)

    # Derived
    info_hash: bytes = field(init=False)
    event_name: EVENT_NAMES = field(init=False)

    def __attrs_post_init__(self) -> NoReturn:
        self.numwant = min(self.numwant or DEFAULT_ANNOUNCE_PEERS, MAX_ANNOUNCE_PEERS)

        # Derived Data
        self.info_hash = self.info_hash_raw.hex()
        if self.event:
            self.event_name = convert_event_name_to_event_enum(self.event)
