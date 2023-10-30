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

latest_animes = [
    {
        "id": 1,
        "name": "Jujutsu Kaisen",
        "type": "TV",
        "episodes": 24,
        "status": "Completed",
        "release_date": "Autumn 2014",  # update this logic later
        "studio": "mappa",
        "genres": ["sci-fi", "action", "echhi"],
        "synopsis": """Idly indulging in baseless paranormal activities with the Occult Club, high schooler Yuuji Itadori spends his days at either the clubroom or the hospital, where he visits his bedridden grandfather. However, this leisurely lifestyle soon takes a turn for the strange when he unknowingly encounters a cursed item. Triggering a chain of supernatural occurrences, Yuuji finds himself suddenly thrust into the world of Curses—dreadful beings formed from human malice and negativity—after swallowing the said item, revealed to be a finger belonging to the demon Sukuna Ryoumen, the "King of Curses.""",
        "image": "https://staticg.sportskeeda.com/editor/2023/04/95453-16812287437122-1920.jpg?w=840",
    },
    {
        "id": 2,
        "name": "One Piece",
        "type": "TV",
        "episodes": 12,
        "status": "Completed",
        "release_date": "Spring 2014",  # update this logic later
        "studio": "tokito",
        "genres": ["hentai", "action", "romance", "smooth"],
        "synopsis": """Since the premiere of the anime adaptation of Eiichiro Oda's One Piece manga in 1999, Toei Animation has produced 15 feature films based on the franchise traditionally released during the Japanese school spring break since 2000.[1] Four of the films were originally shown as double features alongside other Toei film productions and thus have a running time below feature length (between 30 and 56 minutes). The first three films were shown at the Toei Anime Fair (東映アニメフェア, Toei Anime Fea) and the eleventh was released as part of Jump Heroes Film. The films generally use original storylines, but some adapt story arcs from the manga directly. With the release of films ten, twelve, thirteen, and fourteen, tie-in story arcs of the TV series were aired concurrently. """,
        "image": "https://bg-so-1.zippyimage.com/2021/05/29/bcb474d59354a3d20036490aa807fc77.png",
    },
    {
        "id": 3,
        "name": "Demon Slayer",
        "type": "TV",
        "episodes": 12,
        "status": "Completed",
        "release_date": "Winter 2014",  # update this logic later
        "studio": "sheldon",
        "genres": ["hentai", "action", "romance", "smooth"],
        "synopsis": """Since the premiere of the anime adaptation of Eiichiro Oda's One Piece manga in 1999, Toei Animation has produced 15 feature films based on the franchise traditionally released during the Japanese school spring break since 2000.[1] Four of the films were originally shown as double features alongside other Toei film productions and thus have a running time below feature length (between 30 and 56 minutes). The first three films were shown at the Toei Anime Fair (東映アニメフェア, Toei Anime Fea) and the eleventh was released as part of Jump Heroes Film. The films generally use original storylines, but some adapt story arcs from the manga directly. With the release of films ten, twelve, thirteen, and fourteen, tie-in story arcs of the TV series were aired concurrently. """,
        "image": "https://static1.cbrimages.com/wordpress/wp-content/uploads/2021/03/demon-slayer-banner.jpg",
    },
]
