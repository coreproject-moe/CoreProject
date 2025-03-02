from typing import Any, NoReturn

__all__ = ["validate_20_length"]


def validate_20_length(ins: Any, attr: str, value: str | bytes | None) -> NoReturn:
    if length := value:
        if len(length) != 20:
            raise ValueError(f"`{attr}` of `{ins}` is {value} which not 20 bytes")
