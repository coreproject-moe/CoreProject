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

anime = {
    id: 1,
    "mal_id": 23273,
    "anilist_id": None,
    "kitsu_id": None,
    "name": "Your Lie in April",
    "japanese_name": "四月は君の嘘",
    "source": None,
    "aired_from": None,
    "aired_to": None,
    "banner": "/images/YourLieInApril-bg.avif",
    "cover": "/images/Hyouka-bg.avif",
    "banner_background_color": "#2A1710",
    "cover_background_color": "#D8E4D8",
    "synopsis": "Kousei Arima is a child prodigy known as the \"Human Metronome\" for playing the piano with precision and perfection. Guided by a strict mother and rigorous training, Kousei dominates every competition he enters, earning the admiration of his musical peers and praise from audiences. When his mother suddenly passes away, the subsequent trauma makes him unable to hear the sound of a piano, and he never takes the stage thereafter.\r\n\r\nNowadays, Kousei lives a quiet and unassuming life as a junior high school student alongside his friends Tsubaki Sawabe and Ryouta Watari. While struggling to get over his mother's death, he continues to cling to music. His monochrome life turns upside down the day he encounters the eccentric violinist Kaori Miyazono, who thrusts him back into the spotlight as her accompanist. Through a little lie, these two young musicians grow closer together as Kaori tries to fill Kousei's world with color.",
    "background": "Winner in the anime division of the 2016 Sugoi Japan® Awards.",
    "rating": "",
    "updated": "2023-03-11T02:37:40.790Z",
    "name_synonyms": [],
    "genres": "/api/v1/anime/1/genres",
    "themes": "/api/v1/anime/1/themes",
    "characters": "/api/v1/anime/1/character",
    "studios": "/api/v1/anime/1/studios",
    "producers": "/api/v1/anime/1/producers",
    "staffs": "/api/v1/anime/1/staffs",
    "recommendations": [],
    "episodes": "/api/v1/anime/1/episodes",
    "openings": [],
    "endings": [],
    "episodes_count": 9,
    "average_episode_length": 1611,
}

anime_episode = {
    "banner": "https://theglorioblog.files.wordpress.com/2014/11/april4b.png",
    "name": "The Revival of the Long-established Classic Literature Club. The Descendants of the Classic Literature Club",
    "japanese_name": "老舗古典部復活 カッコいいですよね 栄光の古典文学クラブの昔 古典文学部の活動",
    "duration": "20:54",  # add logic for this time later | See this -> https://stackoverflow.com/a/1384465
    "formats": ["sub", "dub"],
    "resolutions": ["sd", "hd", "fhd"],
}

my_list = [
    {
        "id": 1,
        "name": "One piece",
        "image": "https://i.pinimg.com/originals/04/65/2b/04652b44ea7c1275d1022d98d59ecc97.jpg",
        "status": "watching",
        "current_ep": 612,
        "total_ep": 1086,
    },
    {
        "id": 2,
        "name": "Jujutsu Kaisen",
        "image": "https://m.media-amazon.com/images/M/MV5BMTMwMDM4N2EtOTJiYy00OTQ0LThlZDYtYWUwOWFlY2IxZGVjXkEyXkFqcGdeQXVyNjAwNDUxODI@._V1_FMjpg_UX1000_.jpg",
        "status": "watching",
        "current_ep": 13,
        "total_ep": 25,
    }
]
