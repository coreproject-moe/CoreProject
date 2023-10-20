from django.http import HttpRequest
from django.shortcuts import render

from ..forms.user import LoginForm


def login_view(request: HttpRequest):
    form = LoginForm(request.POST or None)

    animes = [
        {"name": "Demon Slayer", "cover": "/images/mock/DemonSlayer-cover.avif"},
        {"name": "Hyouka", "cover": "/images/mock/Hyouka-bg.avif"},
        {"name": "You Lie in April", "cover": "/images/mock/YourLieInApril-bg.avif"},
        {"name": "Attack on Titan", "cover": "/images/mock/AttackOnTitan-bg.avif"},
        {"name": "Jujutsu Kaisen", "cover": "/images/mock/JujutsuKaisen.avif"},
        {"name": "Death Note", "cover": "/images/mock/DeathNote-bg.avif"},
    ]

    context = {
        "form": form,
        "animes": animes,
    }

    return render(request, "user/login.html", context)
