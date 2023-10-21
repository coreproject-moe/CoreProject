from django.http import HttpRequest
from django.shortcuts import render
from django.templatetags.static import static

from ..forms.user import LoginForm


def login_view(request: HttpRequest):
    form = LoginForm(request.POST or None)

    animes = [
        {"name": "Demon Slayer", "cover": static("/images/mock/DemonSlayer-cover.avif")},
        {"name": "Hyouka", "cover": static("/images/mock/Hyouka-bg.avif")},
        {"name": "You Lie in April", "cover": static("/images/mock/YourLieInApril-bg.avif")},
        {"name": "Attack on Titan", "cover": static("/images/mock/AttackOnTitan-bg.avif")},
        {"name": "Jujutsu Kaisen", "cover": static("/images/mock/JujutsuKaisen.avif")},
        {"name": "Death Note", "cover": static("/images/mock/DeathNote-bg.avif")},
    ]

    context = {
        "form": form,
        "animes": animes,
    }

    return render(request, "user/login.html", context)
