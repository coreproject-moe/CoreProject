from typing import Any, Optional

from attrs import Attribute


def validate_peer_length(inst: Any, attr: Attribute, value: Optional[str]) -> None:
    if value and len(value) != 20:
        raise ValueError(f"`{attr}` of `{inst}` is {value} which not 20 bytes")
