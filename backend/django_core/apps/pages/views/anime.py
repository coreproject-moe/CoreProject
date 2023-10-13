from django.shortcuts import render


def anime_home_view(request):
    icons = [
        {
            "html": "icons/home.html",
            "class": "w-[1.25vw] text-white",
            "label": "home",
            "href": "/anime/",
        },
        {
            "html": "icons/compass.html",
            "class": "w-[1.25vw] text-white",
            "label": "explore",
            "href": "/anime/explore/",
        },
        {
            "html": "icons/list.html",
            "class": "w-[1.75vw] text-white",
            "label": "list",
            "href": "/anime/list/",
        },
        {
            "html": "icons/calender.html",
            "class": "w-[1.25vw] text-white",
            "href": "/anime/shedule",
            "label": "schedule/",
        },
        {
            "html": "icons/chat.html",
            "class": "w-[1.25vw] text-white",
            "href": "/anime/forum",
            "label": "forum/",
        },
    ]
    return render(request, "anime/home.html", context={"icons": icons})
