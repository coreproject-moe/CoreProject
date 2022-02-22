from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .forms import LoginForm, RegisterForm


# Create your views here


def login_page(request: HttpRequest) -> HttpResponse:
    """
    This is a simple login page built with django forms.
    """
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username: str = form.cleaned_data["username"]
            password: str = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)

            try:
                login(request, user)
            except AttributeError:
                messages.warning(request, "No such user exists")

            next_url = request.GET.get("next", None)

            if user:
                # Redirect to root if theres no next query
                return redirect(next_url if next_url else "/")

    return render(request, "authentication/login.html", {"form": form})


def logout_page(request: HttpRequest) -> HttpResponse:
    """
    Simple Logout page
    """
    logout(request)

    next_url = request.GET.get("next", None)
    return redirect(next_url if next_url else "/")


def register_page(request: HttpRequest) -> HttpResponse:
    """
    A simple user register page built with django ModelForm.

    Works Like this.
                                        Redirect to root if it doesn't exist
                                                        🠕
        Create the user ➞ Authenticate the user ➞ Check if next url exists
                                                        🠗
                                                Redirect there if it exists

    """
    form = RegisterForm(data=request.POST or None, files=request.FILES or None)

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

    return render(request, "authentication/register.html", {"form": form})
