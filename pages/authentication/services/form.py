from django.http.request import HttpRequest
from .auth import get_user_for_auth
from .database import check_if_username_exist, check_if_email_exist
from django.contrib import messages


async def check_register_form_validity(
    request: HttpRequest,
    username: str,
    email: str,
    password: str,
    confirm_password: str,
) -> bool:
    user = await get_user_for_auth(username, password)
    if user:
        messages.warning(request, "User exists")

    username_exists = await check_if_username_exist(username)
    if username_exists:
        messages.warning(request, "Username Exists")

    email_exists = await check_if_email_exist(email)
    if email_exists:
        messages.warning(request, "Email Exists")

    if confirm_password != password:
        messages.warning(request, "Passwords doesn't match")

    if (
        not user
        and not username_exists
        and not email_exists
        and not confirm_password != password
    ):
        return True
    else:
        return False
