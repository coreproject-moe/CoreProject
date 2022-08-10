from typing import NoReturn

from django.core.exceptions import ValidationError

RESERVED_USERNAME = [
    "admin",
]


INVALID_USERNAMES = set(RESERVED_USERNAME)

# This will only get invoked when using modelform
def username_validator(username: str) -> NoReturn:
    if username in INVALID_USERNAMES:
        raise ValidationError(f"Username {username} not allowed")
