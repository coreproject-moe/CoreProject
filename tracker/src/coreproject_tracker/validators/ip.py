from typing import Any, NoReturn

from coreproject_tracker.functions import convert_str_to_ip_object


def validate_ip(ins: Any, attr: str, value: str | None) -> NoReturn:
    if not convert_str_to_ip_object(value):
        raise ValueError(f"`{value}` is not a valid ip.")


def validate_nullable_ip(ins: Any, attr: str, value: str | None) -> NoReturn:
    if value:
        validate_ip(ins, attr, value)
