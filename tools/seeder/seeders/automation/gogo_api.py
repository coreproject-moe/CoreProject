# non async version

# from itertools import count
from functools import cache
import time
import httpx
from selectolax.parser import HTMLParser
from contextlib import suppress
from playwright.sync_api import sync_playwright

# from functools import cache

BASE_URL = "https://www2.gogoanimes.fi"


def get_js_render(url: str) -> None:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        time.sleep(5)
        # page.wait_for_selector(".dowload a", timeout=10)
        content = page.content()
        context.close()
        browser.close()
        return content


def html_parser(html: str) -> HTMLParser:
    return HTMLParser(html)


@cache
def get_download_links(anime_id: str, episode_no: int) -> str:
    response = httpx.get(f"{BASE_URL}/{anime_id}-episode-{episode_no}")
    parser = html_parser(response.content)
    download_page_url = parser.css_first(".dowloads a").attributes["href"]
    html_content = get_js_render(download_page_url)
    parser = html_parser(html_content)
    data = []
    for a in parser.css(".dowload a"):
        name = a.text().strip().replace("\n", "")
        name = " ".join(list(name.split()))
        data.append({"name": name, "link": a.attributes["href"]})
    return data


@cache
def search(query: str) -> list[dict]:  # sourcery skip: avoid-builtin-shadow
    response = httpx.get(f"{BASE_URL}/search.html?keyword={query}")
    parser = html_parser(response.content)

    anime_list = []
    total_page = 1
    with suppress(Exception):
        total_page = int(
            parser.css_first(".pagination-list li:last-child a").attributes["data-page"]
        )
    for element in parser.css("div.last_episodes ul.items li"):
        name = element.css_first("p a").attributes["title"]
        img = element.css_first("div a img").attributes["src"]
        id = element.css_first("div a").attributes["href"].split("/")[-1]
        anime = {
            "total_page": total_page,
            "name": name,
            "img_url": img,
            "id": id,
        }
        anime_list.append(anime)
    return anime_list


@cache
def get_anime(anime_id: str) -> dict:
    url = f"{BASE_URL}/category/{anime_id}"
    response = httpx.get(url)
    parser = html_parser(response.content)
    img_url = parser.css_first(".anime_info_body_bg img").attributes["src"]
    about = parser.css_first(".anime_info_body_bg p:nth-of-type(3)").text()
    name = parser.css_first("div.anime_info_body_bg h1").text()
    last_ep = int(parser.css_first("#episode_page li:last-child a").attributes["ep_end"])
    episodes = list(range(1, last_ep + 1))
    return {"name": name, "img": img_url, "about": about, "episodes": episodes}


@cache
def new_season(page_no: int) -> list[dict]:  # sourcery skip: avoid-builtin-shadow
    anime_list = []
    response = httpx.get(f"{BASE_URL}/new-season.html?page={page_no}")
    parser = html_parser(response.content)

    for element in parser.css("div.main_body div.last_episodes ul.items li"):
        name = element.css_first("p a").text()
        img = element.css_first("div a img").attributes["src"]
        id = element.css_first("div a").attributes["href"].split("/")[-1]
        anime = {"name": name, "img": img, "id": id}
        anime_list.append(anime)
    return anime_list


@cache
def get_streaming_link(anime_id: str, episode_no: int) -> str:
    response = httpx.get(f"{BASE_URL}/{anime_id}-episode-{episode_no}")
    parser = html_parser(response.content)
    return f'https:{parser.css_first(".play-video > iframe").attributes["src"]}'


@cache
def home(page: int):
    response = httpx.get(
        f"https://ajax.gogo-load.com/ajax/page-recent-release.html?page={page}"
    )
    parser = html_parser(response.content)
    anime = []
    for li in parser.css("ul.items li"):
        img = li.css_first("div.img img").attributes["src"]
        episode_id = li.css_first("div.img a").attributes["href"][1:]
        name = li.css_first("div.img a").attributes["title"]
        episode_text = li.css_first("p.episode").text()
        anime.append(
            {
                "name": name,
                "episode_id": episode_id,
                "episode_text": episode_text,
                "img": img,
            }
        )
    return anime


@cache
def get_anime_list(page: int) -> list:
    response = httpx.get(f"{BASE_URL}/anime-list.html?page={page}")
    parser = html_parser(response.content)
    anime_list_a = parser.css_first(".anime_list_body").css("a")
    return [
        {"title": a.text(), "link": f'{BASE_URL}{a.attributes["href"]}'}
        for a in anime_list_a
        if "(Dub)" not in a.text()
    ]


# for page in count(80):
#     animes = get_anime_list(page)
#     if not animes:
#         break
#     for i in animes:
#         print(i)
