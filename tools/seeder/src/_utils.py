import contextlib
from datetime import datetime


def date_converter(date: str) -> str:
    with contextlib.suppress(Exception):
        dt = datetime.fromisoformat(date[:-6])
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    return None
