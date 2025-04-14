from typing import Optional

__all__ = ["convert_binary_string_to_bytes"]


def convert_binary_string_to_bytes(value: str) -> bytes:
    return value.encode("latin1")
