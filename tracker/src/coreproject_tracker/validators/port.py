from typing import Any, NoReturn

__all__ = ["validate_port"]


def validate_port(ins: Any, attr: str, value: int | str | None) -> NoReturn:
    if value:
        if isinstance(value, str):
            value = int(value)

        if value <= 0 and value >= 65535:
            raise ValueError(
                f"`{attr}` of `{ins}` is {value} which is not in range(0, 65535)"
            )
