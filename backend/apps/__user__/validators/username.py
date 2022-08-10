from pathlib import Path
from typing import NoReturn

from django.core.exceptions import ValidationError

BASE_DIR = Path(__file__).resolve()

RESERVED_USERNAME = [
    "admin",
]


INVALID_USERNAMES = set(RESERVED_USERNAME)


def username_validator(username: str) -> NoReturn:
    print(username)
    if username in INVALID_USERNAMES:
        raise ValidationError(f"Username {username} not allowed")
