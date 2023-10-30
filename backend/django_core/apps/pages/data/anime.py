from django.urls import reverse_lazy

icons = [
    {
        "html": "icons/home.html",
        "class": "w-[1.25vw]",
        "label": "home",
        "href": reverse_lazy("anime_home_view"),
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
        "label": "schedule",
    },
    {
        "html": "icons/chat.html",
        "class": "w-[1.25vw]",
        "href": "/anime/forum",
        "label": "forum",
    },
]
