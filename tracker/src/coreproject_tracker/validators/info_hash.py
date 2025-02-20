from typing import Any, NoReturn


def validate_info_hash(ins: Any, attr: str, value: bytes | None) -> NoReturn:
    if value:
        info_hash = value.hex()
        if len(info_hash != 20):
            raise ValueError(f"`{attr}` of `{ins}` is {value} which not 20 bytes")
