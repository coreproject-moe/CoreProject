from defender import config, utils
from django.contrib.auth import authenticate, login
from django.http import HttpRequest
from django.shortcuts import render
from django.templatetags.static import static
from django_htmx.http import retarget

from ..forms.user import LoginForm


def login_view(request: HttpRequest):
    form = LoginForm(request.POST or None)

    animes = [
        {"name": "Demon Slayer", "cover": static("/images/mock/DemonSlayer-cover.avif")},
        {"name": "Hyouka", "cover": static("/images/mock/Hyouka-bg.avif")},
        {
            "name": "You Lie in April",
            "cover": static("/images/mock/YourLieInApril-bg.avif"),
        },
        {"name": "Attack on Titan", "cover": static("/images/mock/AttackOnTitan-bg.avif")},
        {"name": "Jujutsu Kaisen", "cover": static("/images/mock/JujutsuKaisen.avif")},
        {"name": "Death Note", "cover": static("/images/mock/DeathNote-bg.avif")},
    ]

    login_unsuccessful = False

    if form.is_valid():
        username = form.cleaned_data["username"]
        user = authenticate(
            username=username,
            password=form.cleaned_data["password"],
        )

        if utils.is_already_locked(request, username=username):
            message = (
                f"You have attempted to login {config.FAILURE_LIMIT} times, with no success."
                f"Your account is locked for {utils.get_lockout_cooloff_time(username=username)} seconds"
            )

        if user is not None:
            login(request, user)
            message = f"Welcome Back {username}"

        else:
            login_unsuccessful = True
            utils.add_login_attempt_to_db(
                request,
                login_valid=False,
                username=username,
            )
            
            login_attempts = int(config.FAILURE_LIMIT) - int(
                utils.get_user_attempts(request, username=username)
            )

            if login_attempts == 0:
                message = f"Your account is locked for {utils.get_lockout_cooloff_time(username=username)} seconds"
            else:
                message = (
                    "User not found!\n"
                    f"You have {login_attempts} attempts left for {username}"
                )

        utils.check_request(
            request,
            login_unsuccessful=login_unsuccessful,
            username=username,
        )
        response = render(
            request,
            "components/toast.html",
            {"message": message},
        )
        return retarget(response, "#toast")

    return render(
        request,
        "user/login.html",
        context={
            "form": form,
            "animes": animes,
        },
    )
