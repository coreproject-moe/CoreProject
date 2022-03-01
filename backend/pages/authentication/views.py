from django.views import View
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from rest_framework_simplejwt.tokens import RefreshToken
from .forms import LoginForm, RegisterForm

# Create your views here


class LoginPageView(View):
    """
    This is a simple login page built with django forms.
    """

    form_class = LoginForm
    template_name = "authentication/login/index.html"

    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }

    def get(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)

        if form.is_valid():
            username: str = form.cleaned_data["username"]
            password: str = form.cleaned_data["password"]

            # Get the user
            user = authenticate(username=username, password=password)

            try:
                login(request, user)
            except AttributeError:
                messages.warning(request, "No such user exists")

            if user:
                return render(
                    request,
                    "authentication/login/success.html",
                    {"token": self.get_tokens_for_user(request.user)},
                )

        return render(request, self.template_name, {"form": form})


class RegisterPageView(View):
    """
    A simple user register page built with django ModelForm.

    Works Like this.
                                        Redirect to root if it doesn't exist
                                                        🠕
        Create the user ➞ Authenticate the user ➞ Check if next url exists
                                                        🠗
                                                Redirect there if it exists

    """

    form_class = RegisterForm
    template_name = "authentication/register.html"

    def get(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class()
        return render(request, self.template_name, {"form": form})

    def post(self, request: HttpRequest) -> HttpResponse:
        form = RegisterForm(data=request.POST, files=request.FILES)

        if request.method == "POST":
            if form.is_valid():
                # Create the user.
                form.save()

                # Get Username and password
                username: str = form.cleaned_data["username"]
                password: str = form.cleaned_data["password"]

                # Authenticate the user.
                authenticate(username=username, password=password)

                # Get next url from request query
                next_url = request.GET.get("next", None)

                # Final redirect.
                return redirect(next_url if next_url else "/")

        return render(request, self.template_name, {"form": form})


def logout_page(request: HttpRequest) -> HttpResponse:
    """
    Simple Logout page
    """
    logout(request)

    next_url = request.GET.get("next", None)
    return redirect(next_url if next_url else "/")
