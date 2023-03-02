from dataclasses import dataclass
from typing import List, Dict


@dataclass
class Image:
    image_url: str
    small_image_url: str
    large_image_url: str


@dataclass
class Trailer:
    youtube_id: str
    url: str
    embed_url: str
    images: Dict[str, str]


@dataclass
class Title:
    type: str
    title: str


@dataclass
class Aired:
    from_date: str
    to_date: str
    prop: Dict[str, Dict[str, int]]
    string: str


@dataclass
class MyAnimeList:
    mal_id: int
    url: str
    images: Dict[str, Image]
    trailer: Trailer
    approved: bool
    titles: List[Title]
    title: str
    title_english: str
    title_japanese: str
    title_synonyms: List[str]
    type: str
    source: str
    episodes: int
    status: str
    airing: bool
    aired: Aired
    duration: str
    rating: str
    score: float
    scored_by: int
    rank: int
    popularity: int
    members: int
    favorites: int
    synopsis: str
    background: str


# Main models
@dataclass
class AniList:
    id: int
    link: str


@dataclass
class Kitsu:
    id: int
    link: str


@dataclass
class AnimeInfo:
    myanimelist: MyAnimeList
    kitsu: Kitsu
    anilist: AniList
