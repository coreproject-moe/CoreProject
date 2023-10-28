from defender import config, utils
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.cache import never_cache
from django_htmx.http import HttpResponseClientRedirect, HttpResponseClientRefresh, retarget

from ..forms.user import FirstRegisterForm, LoginForm, ResetPasswordForm, SecondRegisterForm

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


@never_cache
def login_view(request: HttpRequest) -> HttpResponse | HttpResponseClientRefresh:
    form = LoginForm(request.POST or None)

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

            redirect_location = request.GET.get("next")
            url_is_safe = url_has_allowed_host_and_scheme(
                url=redirect_location,
                allowed_hosts=settings.ALLOWED_HOSTS,
                require_https=request.is_secure(),
            )
            if redirect_location and url_is_safe:
                return HttpResponseClientRedirect(redirect_location)
            else:
                return HttpResponseClientRefresh()

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
    elif form.errors:
        response = render(
            request,
            "components/toast.html",
            {"message": form.non_field_errors().as_text()},
        )
    else:
        return render(
            request,
            "user/login.html",
            context={
                "form": form,
                "animes": animes,
            },
        )
    return retarget(response, "#toast")


@never_cache
def logout_view(request: HttpRequest) -> HttpResponse:
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


def register_view(request: HttpRequest) -> HttpResponse:
    if request.htmx:
        _internal_state_ = request.session["_internal_state_"]

        if _internal_state_ == 1:
            form = FirstRegisterForm(request.POST or None)

            if form.is_valid():
                request.session["_internal_state_"] = _internal_state_ + 1
                request.session["_form_"] = dict(form.data)
                return register_view(request)

            elif form.errors:
                response = render(
                    request,
                    "components/toast.html",
                    {"message": form.non_field_errors().as_text()},
                )
                return retarget(response, "#toast")
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
                return register_view(request)

            elif form.errors:
                if form.fields["username"].error_messages:
                    form.fields["username"].widget.attrs["class"] += " focus:border-error"

            return render(request, "user/register/_2.html", context={"form": form})
        elif _internal_state_ == 3:
            form_data = request.session["_form_"]
            username = form_data.get("username", [None])[0]
            email = form_data.get("email", [None])[0]

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


def reset_password_view(request):
    form = ResetPasswordForm(request.POST or None)

    if request.htmx:
        return render(request, "user/reset_password/_partial.html", context={"form": form})

    if form.is_valid():
        print("Valid")

    elif form.errors:
        if form.fields["email"].error_messages:
            form.fields["email"].widget.attrs["class"] += " focus:border-error"

    return render(
        request, "user/reset_password/index.html", context={"animes": animes, "form": form}
    )
