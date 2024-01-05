from typing import TYPE_CHECKING

from defender import config, utils
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.cache import never_cache
from django_htmx.http import HttpResponseClientRedirect, HttpResponseClientRefresh, retarget

if TYPE_CHECKING:
    from ..request import HtmxHttpRequest

from ..forms.user import FirstRegisterForm, ResetPasswordForm, SecondRegisterForm

animes = [
    {"name": "Demon Slayer", "cover": static("/public/images/mock/DemonSlayer-cover.avif")},
    {"name": "Hyouka", "cover": static("/public/images/mock/Hyouka-bg.avif")},
    {
        "name": "You Lie in April",
        "cover": static("/public/images/mock/YourLieInApril-bg.avif"),
    },
    {
        "name": "Attack on Titan",
        "cover": static("/public/images/mock/AttackOnTitan-bg.avif"),
    },
    {"name": "Jujutsu Kaisen", "cover": static("/public/images/mock/JujutsuKaisen.avif")},
    {"name": "Death Note", "cover": static("/public/images/mock/DeathNote-bg.avif")},
]


@never_cache
def login_view(request: "HtmxHttpRequest") -> HttpResponse:
    return render(
        request,
        "user/login/index.html",
        context={
            "animes": animes,
        },
    )


@never_cache
def logout_view(request: "HtmxHttpRequest") -> HttpResponse:
    logout(request)
    redirect_location = request.GET.get("next") or reverse_lazy("login_view")
    url_is_safe = url_has_allowed_host_and_scheme(
        url=redirect_location,
        allowed_hosts=settings.ALLOWED_HOSTS,
        require_https=request.is_secure(),
    )
    if redirect_location and url_is_safe:
        return redirect(redirect_location)

    return HttpResponseClientRefresh()


async def register_view(request: "HtmxHttpRequest") -> HttpResponse:
    if request.htmx:
        _internal_state_ = request.session["_internal_state_"]

        if _internal_state_ == 1:
            form = FirstRegisterForm(request.POST or None)

            if form.is_valid():
                request.session["_internal_state_"] = _internal_state_ + 1
                request.session["_form_"] = dict(form.data)
                return await register_view(request)

            elif form.errors:
                if form.errors.get("email"):
                    form.fields["email"].widget.attrs["class"] += " focus:border-error"

                elif form.errors.get("confirm_password"):
                    form.fields["confirm_password"].widget.attrs[
                        "class"
                    ] += " focus:border-error"
                    form.fields["confirm_password"].widget.attrs["_"] = "init focus() me"

            return render(
                request,
                "user/register/_1.html",
                context={
                    "form": form,
                },
            )

        elif _internal_state_ == 2:
            form = SecondRegisterForm(request.POST or None)

            if form.is_valid():
                request.session["_internal_state_"] = 3
                request.session["_form_"] = request.session["_form_"] | form.data
                return await register_view(request)

            elif form.errors:
                if form.fields["username"].error_messages:
                    form.fields["username"].widget.attrs["class"] += " focus:border-error"

            return render(request, "user/register/_2.html", context={"form": form})

        elif _internal_state_ == 3:
            form_data = request.session["_form_"]
            username = form_data.get("username", [None])[0]
            email = form_data.get("email", [None])[0]

            # TODO: Finish register logics

            return render(
                request,
                "user/register/_3.html",
                context={
                    "username": username,
                    "email": email,
                },
            )
    else:
        # Fresh state
        request.session["_internal_state_"] = 1
        request.session["_form_"] = {}

    return render(
        request,
        "user/register/index.html",
        context={
            "animes": animes,
        },
    )


async def reset_password_view(request: "HtmxHttpRequest") -> HttpResponse:
    form = ResetPasswordForm(request.POST or None)

    if request.htmx:
        if form.is_valid():
            pass

        elif form.errors:
            if form.fields["email"].error_messages:
                form.fields["email"].widget.attrs["class"] += " focus:border-error"

        return render(
            request,
            "user/reset_password/_partial.html",
            context={
                "form": form,
            },
        )

    return render(
        request,
        "user/reset_password/index.html",
        context={
            "animes": animes,
            "form": form,
        },
    )
