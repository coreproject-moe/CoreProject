from django.shortcuts import render


def anime_home_view(request):
    if request.htmx:
        return render(request, "anime/_partial.html")

    icons = [
        {
            "html": "icons/home.html",
            "class": "w-[1.25vw]",
            "label": "home",
            "href": "/anime/",
        },
        {
            "html": "icons/compass.html",
            "class": "w-[1.25vw]",
            "label": "explore",
            "href": "/anime/explore/",
        },
        {
            "html": "icons/list.html",
            "class": "w-[1.75vw]",
            "label": "list",
            "href": "/anime/list/",
        },
        {
            "html": "icons/calender.html",
            "class": "w-[1.25vw]",
            "href": "/anime/shedule",
            "label": "schedule/",
        },
        {
            "html": "icons/chat.html",
            "class": "w-[1.25vw]",
            "href": "/anime/forum",
            "label": "forum/",
        },
    ]
    return render(request, "anime/home.html", context={"icons": icons})
