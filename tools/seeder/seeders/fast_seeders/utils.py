from contextlib import suppress
from datetime import datetime


def date_converter(date: str) -> str:
    with suppress(Exception):
        dt = datetime.fromisoformat(date[:-6])
        return dt.strftime("%Y-%m-%dT%H:%M:%SZ")
    return None


def dictionary_filter(dictionary: dict):
    return {key: value for key, value in dictionary.items() if value}
