import hashlib
from http import HTTPStatus
import textwrap

from django_htmx.http import HttpResponseLocation
import httpx

from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.management.utils import get_random_secret_key
from django.core.validators import URLValidator
from django.http import FileResponse, HttpRequest, HttpResponse, StreamingHttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm, UsernameWithDiscriminatorForm
from .models import CustomUser, Token


async def avatar_view(
    request: HttpRequest,
    user_id: int,
) -> StreamingHttpResponse | HttpResponse:
    CLIENT = httpx.AsyncClient()

    try:
        user = await CustomUser.objects.aget(pk=user_id)
    except CustomUser.DoesNotExist:
        return render(
            request,
            "user/user_does_not_exist.htm",
            context={
                "database_name": "postgres",
                "database_user": "animecore",
                "database_password": str(get_random_secret_key()),
                "user_id": user_id,
            },
        )

    if user.avatar:
        avatar_file = open(user.avatar.path, "rb")
        response = FileResponse(avatar_file)

    else:
        try:
            avatar_url = user.avatar_provider.format(
                EMAIL=hashlib.md5(user.email.strip().lower().encode()).hexdigest()
            )
            # Just a check Here
            URLValidator()(avatar_url)

            _request_ = CLIENT.build_request("GET", avatar_url)
            avatar_response = await CLIENT.send(_request_)
            response = StreamingHttpResponse(
                avatar_response.iter_bytes(),
                content_type=avatar_response.headers["content-type"],
            )
        except Exception as e:
            response = HttpResponse(
                textwrap.dedent(
                    f"""
                        Please Check your <b>email</b> string.
                        <br/>
                        It is |> <b>{avatar_url}</b>
                        which might not a valid string
                        <br />
                        <b>Error</b> : {e}
                    """
                )
            )

    await CLIENT.aclose()
    return response


def signup_view(request: HttpRequest) -> HttpResponse:
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            user = CustomUser.objects.create(**form.cleaned_data)
            login(request, user)
            token_model = Token.objects.create(user=user)
            response = HttpResponseLocation(reverse_lazy("login_view"))
            response.set_cookie(
                key="token",
                value=token_model.token,
                httponly=False,
                samesite="lax",
            )
            return response

    return render(
        request,
        "user/signup.html",
        context={
            "form": form,
        },
    )


def login_view(request: HttpRequest) -> HttpResponse:
    form = LoginForm(data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        if user := authenticate(
            request,
            username=form.cleaned_data.get("username"),
            password=form.cleaned_data.get("password"),
        ):
            login(request, user)
            token_model = Token.objects.create(user=request.user)
            response = HttpResponseLocation(reverse_lazy("login_view"))
            response.set_cookie(
                key="token",
                value=token_model.token,
                httponly=False,
                samesite="lax",
            )
            return response

    return render(
        request,
        "user/login.html",
        context={
            "form": form,
        },
    )


def logout_view(request: HttpRequest) -> HttpResponse:
    Token.objects.get(user=request.user).delete()
    logout(request)
    response = HttpResponseLocation(reverse_lazy("login_view"))
    response.delete_cookie("token")
    return response


def username_and_discriminator_validity_checker_view(
    request: HttpRequest,
) -> HttpRequest:
    form = UsernameWithDiscriminatorForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        if CustomUser.objects.filter(username=form.cleaned_data.get("username")).distinct(
            "discriminator"
        ).count() > int("9" * settings.DISCRIMINATOR_LENGTH):
            return HttpResponse("Your username is too popular. Please pick another one")

        if (
            CustomUser.objects.get_username_with_discriminator()
            .filter(
                username_with_discriminator=f"""{
                form
                .cleaned_data
                .get('username')
            }#{
                str(
                    form
                    .cleaned_data
                    .get('discriminator')
                ).zfill(
                    settings
                    .DISCRIMINATOR_LENGTH
                )
            }"""
            )
            .exists()
        ):
            # Return status code 300 if username with discriminator exists
            return HttpResponse(HTTPStatus.FOUND)
        else:
            # Return status code 200 if username with discriminator is available
            return HttpResponse(HTTPStatus.OK)

    else:
        return form.errors
