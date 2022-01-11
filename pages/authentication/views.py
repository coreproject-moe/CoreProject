from django.http.response import HttpResponse
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.conf import settings

from .forms import ForgetPasswordForm, LoginForm, RegisterForm
from .services import (
    auth_login,
    auth_logout,
    check_if_username_exist,
    check_register_form_validity,
    create_new_reset_database,
    create_new_user,
    get_user_for_auth,
    get_user_by_id,
    send_mail_function,
)

# Create your views here.


async def login_page(request) -> HttpResponse:
    """
    A Simple Login Form to authenticate users.
    """
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username: str = form.cleaned_data["username"]
            password: str = form.cleaned_data["password"]
            user = await get_user_for_auth(username, password)

            next_url = request.GET.get("next", None)
            # If theres next url redirect there
            if next_url:
                return redirect(next_url)

            if user:
                await auth_login(request, user)
                return redirect(reverse("home_page"))

            elif not user:
                messages.warning(
                    request, "No such user | Check your username and password please"
                )

    return render(request, "authentication/login.html", {"form": form})


async def logout(request) -> HttpResponse:
    await auth_logout(request)

    next_url = request.GET.get("next", None)
    # If theres next url redirect there
    if next_url:
        return redirect(next_url)

    return redirect(reverse("home_page"))


async def register_page(request) -> HttpResponse:
    """
    A Simple User Register Form
    """
    form = RegisterForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            first_name: str = form.cleaned_data["first_name"]
            last_name: str = form.cleaned_data["last_name"]
            username: str = form.cleaned_data["username"]
            email: str = form.cleaned_data["email"]
            password: str = form.cleaned_data["password_1"]
            confirm_password: str = form.cleaned_data["password_2"]

            response_is_valid = await check_register_form_validity(
                request=request,
                username=username,
                email=email,
                password=password,
                confirm_password=confirm_password,
            )

            if response_is_valid:
                await create_new_user(username, email, password, first_name, last_name)

                # Auth the user
                user = await get_user_for_auth(username, password)
                await auth_login(request, user)

                # Redirect to home
                next_url = request.GET.get("next", None)
                # If theres next url redirect there
                if next_url:
                    return redirect(next_url)

                return redirect(reverse("home_page"))

    return render(request, "authentication/register.html", {"form": form})


async def forget_password_form(request) -> HttpResponse:

    form = ForgetPasswordForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]

            is_user_actually_there = await check_if_username_exist(username)
            if not is_user_actually_there:
                messages.warning(request, "Did you enter the correct username")

            elif is_user_actually_there:
                user = await get_user_by_id(username)

                reset_database = create_new_reset_database(user=user)
                password_reset_url = reset_database.url

                subject = "Reset Password!"

                reset_message = f"""Hello, 
                This is an automated message. 
                You are getting this message because someone requested a password accounts_reset on your account.
                Click  https://127.0.0.1/accounts/reset/{password_reset_url}/ to accounts_reset your password."""

                sender_email = settings.EMAIL_HOST_USER
                receiver_email = user.email
                await send_mail_function(
                    email_subject=subject,
                    email_reset_message=reset_message,
                    from_sender=sender_email,
                    to_receiver=receiver_email,
                )

                return render(request, "authentication/forget.html")

    return render(request, "accounts/forget/index.html", {"form": form})
