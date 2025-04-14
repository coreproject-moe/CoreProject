from typing import Any, Optional

from attrs import Attribute

__all__ = ["validate_port"]


def validate_port(inst: Any, attr: Attribute[int], value: Optional[int]) -> None:
    if value:
        if value <= 0 and value >= 65535:
            raise ValueError(
                f"`{attr}` of `{inst}` is {value} which is not in range(0, 65535)"
            )
