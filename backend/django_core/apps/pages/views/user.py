from django.http import HttpRequest, HttpResponseForbidden
from django.shortcuts import render
from django.templatetags.static import static
from django.contrib.auth import authenticate, login
from ..forms.user import LoginForm
from defender import utils
from defender import config


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

    context = {
        "form": form,
        "animes": animes,
    }
    login_unsuccessful = False

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
            return HttpResponseForbidden(detail)
        if user is not None:
            login(request, user)
        else:
            login_unsuccessful = True
            utils.add_login_attempt_to_db(request, login_valid=False, username=username)
            return HttpResponseForbidden(f'Attempts = {utils.get_user_attempts(username)}')
        utils.check_request(
            request,
            login_unsuccessful=login_unsuccessful,
            username=username,
        )
        if login_unsuccessful:
            return HttpResponseForbidden("Login not allowed")

    return render(request, "user/login.html", context)
