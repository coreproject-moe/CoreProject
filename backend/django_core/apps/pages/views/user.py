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

    if form.is_valid():
        username = form.cleaned_data["username"]
        user = authenticate(
            username=username,
            password=form.cleaned_data["password"],
        )

        if utils.is_already_locked(request, username=username):
            detail = (
                f"You have attempted to login {config.FAILURE_LIMIT} times, with no success."
                f"Your account is locked for {utils.get_lockout_cooloff_time(username=username)} seconds"
            )
            response = render(request, "components/toast.html", {"message": detail})
            return retarget(response, "#toast")

        if user is not None:
            login(request, user)
            utils.check_request(
                request,
                login_unsuccessful=False,
                username=username,
            )
            response = render(
                request,
                "components/toast.html",
                {"message": (f"Welcome Back {username}")},
            )
            return retarget(response, "#toast")

        else:
            utils.add_login_attempt_to_db(
                request,
                login_valid=False,
                username=username,
            )
            response = render(
                request,
                "components/toast.html",
                {"message": "User not found!"},
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
