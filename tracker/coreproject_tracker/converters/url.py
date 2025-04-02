import urllib.parse

__all__ = ["convert_to_url_bytes"]


def convert_to_url_bytes(value: str) -> bytes:
    return urllib.parse.unquote_to_bytes(value)
