from typing import Any, NoReturn

from coreproject_tracker.constants import CONNECTION_ID
from coreproject_tracker.functions import from_uint64

__all__ = ["validate_connection_id"]


def validate_connection_id(ins: Any, attr: str, value: bytes) -> NoReturn:
    connection_id_unpacked = from_uint64(value)
    if connection_id_unpacked != CONNECTION_ID:
        raise ValueError(f"`{attr}` of `{ins}` is {value} which not {CONNECTION_ID}")
