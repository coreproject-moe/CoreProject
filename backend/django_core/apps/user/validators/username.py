from django.core.exceptions import ValidationError

RESERVED_USERNAME = [
    "admin",
]


INVALID_USERNAMES = set(RESERVED_USERNAME)


# This will only get invoked when using modelform
def username_validator(username: str) -> None:
    if username in INVALID_USERNAMES:
        raise ValidationError(f"Username {username} not allowed")

    # It can raise issues with usernames like `baseplate-admin#0001#0001`
    if "#" in username:
        raise ValidationError(f"Usernames should not contain `#`")
