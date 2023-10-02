from django.shortcuts import render


def anime_home_view(request):
    icons = [
        {
            "html": "icons/compass.html",
            "klass": "hello",
            "label": "",
            "href": "",
        },
        {
            "html": "icons/compass.html",
            "klass": "world",
            "label": "",
            "href": "",
        },
    ]
    return render(request, "anime/home.html", context={"icons": icons})
