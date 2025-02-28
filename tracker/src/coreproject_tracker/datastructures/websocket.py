from attrs import define, field

from coreproject_tracker.functions import bin_str_to_hex_str


@define
class WebsocketDatastructure:
    info_hash_raw: str = field()
    action: str = field(default=None)
    peer_id: str = field()

    # Derived
    info_hash = field(init=False)

    def __attrs_post_init__(self):
        self.info_hash = bin_str_to_hex_str(self.info_hash_raw)
