from typing import Any, NoReturn


def validate_peer_length(ins: Any, attr: str, value: str) -> NoReturn:
    if len(value) > 20:
        raise ValueError(f"`{attr}` of `{ins}` is {value} which not 20 bytes")
