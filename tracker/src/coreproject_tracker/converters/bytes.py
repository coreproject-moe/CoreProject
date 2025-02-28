__all__ = ["convert_binary_string_to_bytes"]


def convert_binary_string_to_bytes(value: str | None) -> bytes:
    if value:
        return value.encode("latin1")
