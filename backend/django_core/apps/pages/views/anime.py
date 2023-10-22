from django.shortcuts import render
from ..data.anime import icons


def anime_home_view(request):
    if request.htmx:
        return render(request, "anime/_partial.html")

    return render(request, "anime/home.html", context={"icons": icons})
