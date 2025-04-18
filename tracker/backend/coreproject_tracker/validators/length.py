from typing import Any, Optional

from attrs import Attribute

__all__ = ["validate_20_length"]


def validate_20_length(inst: Any, attr: Attribute, value: Optional[bytes]) -> None:
    if length := value:
        if len(length) != 20:
            raise ValueError(f"`{attr}` of `{inst}` is {value} which not 20 bytes")
