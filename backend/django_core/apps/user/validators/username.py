from django.core.exceptions import ValidationError

INVALID_USERNAMES = {
    "admin",
}


# This will only get invoked when using modelform
def username_validator(username: str) -> None:
    if username in INVALID_USERNAMES:
        raise ValidationError(f"Username {username} not allowed")
