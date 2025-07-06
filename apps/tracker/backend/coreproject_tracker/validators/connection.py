from typing import Any, Optional

from attrs import Attribute

from coreproject_tracker.constants import CONNECTION_ID
from coreproject_tracker.functions import from_uint64

__all__ = ["validate_connection_id"]


def validate_connection_id(inst: Any, attr: Attribute, value: Optional[bytes]) -> None:
    if value:
        connection_id_unpacked = from_uint64(value)
        if connection_id_unpacked != CONNECTION_ID:
            raise ValueError(
                f"`{attr}` of `{inst}` is {value} which not {CONNECTION_ID}"
            )
