from typing import Any, NoReturn

from coreproject_tracker.functions import convert_str_to_ip_object


def validate_ip(ins: Any, attr: str, value: str | None) -> NoReturn:
    if value and not convert_str_to_ip_object(value):
        raise ValueError(f"`{value}` is not a valid ip.")
