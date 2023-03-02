from AnilistPython import Anilist
import httpx
from models import AnimeInfo, AniList, Kitsu, MyAnimeList, Image, Trailer, Title, Aired
from typing import List


class AnimeScraper:
    KITSU_BASE_URL = "https://kitsu.io/api/edge"

    def __init__(self, query):
        self.query = query

    def get_anime_info(self):
        self.mal = self._get_mal_info()
        self.anilist = self._get_anilist_info(self.mal.title)
        self.kitsu = self._get_kitsu_info(self.mal.title)
        return AnimeInfo(myanimelist=self.mal, kitsu=self.kitsu, anilist=self.anilist)

    def _get_mal_info(self) -> MyAnimeList:
        data = httpx.get(f"https://api.jikan.moe/v4/anime?q={self.query}").json()[
            "data"
        ][0]
        images_data = data["images"]["webp"]

        images: Image = Image(
            image_url=images_data["image_url"],
            small_image_url=images_data["small_image_url"],
            large_image_url=images_data["large_image_url"],
        )

        trailer_data = data["trailer"]
        trailer: Trailer = Trailer(
            youtube_id=trailer_data["youtube_id"],
            url=trailer_data["url"],
            embed_url=trailer_data["embed_url"],
            images=trailer_data["images"],
        )

        titles_data = data["titles"]
        titles: List[Title] = [
            Title(type=title_data["type"], title=title_data["title"])
            for title_data in titles_data
        ]

        title_synonyms: List[str] = data["title_synonyms"]
        aired_data = data["aired"]
        aired: Aired = Aired(
            from_date=aired_data["from"],
            to_date=aired_data["to"],
            prop=aired_data["prop"],
            string=aired_data["string"],
        )

        mal_id: int = data["mal_id"]
        url: str = data["url"]
        approved: bool = data["approved"]
        title: str = data["title"]
        title_english: str = data["title_english"]
        title_japanese: str = data["title_japanese"]
        type: str = data["type"]
        source: str = data["source"]
        episodes: int = data["episodes"]
        status: str = data["status"]
        airing: bool = data["airing"]
        aired: Aired = aired
        duration: str = data["duration"]
        rating: str = data["rating"]
        score: float = data["score"]
        scored_by: int = data["scored_by"]
        rank: int = data["rank"]
        popularity: int = data["popularity"]
        members: int = data["members"]
        favorites: int = data["favorites"]
        synopsis: str = data["synopsis"]
        background: str = data["background"]

        return MyAnimeList(
            mal_id=mal_id,
            url=url,
            images=images,
            trailer=trailer,
            approved=approved,
            titles=titles,
            title=title,
            title_english=title_english,
            title_japanese=title_japanese,
            title_synonyms=title_synonyms,
            type=type,
            source=source,
            episodes=episodes,
            status=status,
            airing=airing,
            aired=aired,
            duration=duration,
            rating=rating,
            score=score,
            scored_by=scored_by,
            rank=rank,
            popularity=popularity,
            members=members,
            favorites=favorites,
            synopsis=synopsis,
            background=background,
        )

    def _get_anilist_info(self, query: str) -> AniList:
        anilist_id = Anilist().get_anime_id(query)
        link = f"https://anilist.co/anime/{anilist_id}"
        return AniList(anilist_id, link)

    def _get_kitsu_info(self, query: str) -> Kitsu:
        params = {"page[limit]": "1", "filter[text]": query}
        data = httpx.get(f"{self.KITSU_BASE_URL}/anime", params=params).json()["data"][
            0
        ]
        kitsu_id = data["id"]
        link = f'https://kitsu.io/anime/{data["attributes"]["slug"]}'
        return Kitsu(kitsu_id, link)
