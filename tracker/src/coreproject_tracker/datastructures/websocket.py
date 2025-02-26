from attrs import define, field

from coreproject_tracker.validators import validate_info_hash
from coreproject_tracker.functions import bin_to_hex


@define
class WebsocketDatastructure:
    info_hash_raw: str = field()
    action: str = field(default=None)
    peer_id: str = field()

    # Derived
    info_hash = field(init=False)

    def __attrs_post_init__(self):
        self.info_hash = bin_to_hex(self.info_hash_raw)
