from typing import Any, NoReturn

__all__ = ["validate_info_hash"]


def validate_info_hash(ins: Any, attr: str, value: str | bytes | None) -> NoReturn:
    if info_hash := value:
        if len(info_hash) != 20:
            raise ValueError(f"`{attr}` of `{ins}` is {value} which not 20 bytes")
