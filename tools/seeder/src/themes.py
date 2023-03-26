from selectolax.parser import HTMLParser
import re
import json
from ._session import session
from ._conf import ANIME_THEME_ENDPOINT, TOKEN
from ._welcome import get_welcome_message
from ._report import get_report_message

from termcolor import colored
from datetime import datetime

EXECUTION_TIME = 0


def command() -> None:
    global EXECUTION_TIME

    resp = session.get("https://myanimelist.net/anime.php")

    pattern = re.compile(r"^(.*) \(([\d,]+)\)$")
    themes_header = [
        header
        for header in HTMLParser(resp.text).css("div.normal_header")
        if header.text() == "Themes"
    ][0]
    themes_raw = themes_header.css_first("div + div").css(
        "div.genre-list.al a.genre-name-link"
    )
    themes = []
    for theme in themes_raw:
        if match := pattern.search(theme.text()):
            name = match[1]
            theme_id = theme.attributes["href"].split("/")[-2]
            themes.append({"mal_id": theme_id, "name": name})
        else:
            print(f"Failed to parse line: {theme.text()}")

    print(
        get_welcome_message(
            base_field_number=1,
            ending_number=len(themes),
            execution_time=0,
            starting_number=1,
            field_name="themes",
        )
    )

    for index, item in enumerate(themes):
        start_time = datetime.now()
        res = session.post(
            ANIME_THEME_ENDPOINT,
            djosn=([item]),
            headers={
                "Authorization": f"Bearer {TOKEN}",
            },
        )
        if res.ok:
            print(
                get_report_message(
                    base_field_number=index + 1,
                    starting_number=index + 1,
                    execution_time=EXECUTION_TIME,
                    field_name="theme_info",
                    success_list=[colored("MyAnimeList", color="green")],
                    error_list=[],
                    warning_list=[],
                )
            )
        else:
            raise Exception(f"Cannot POST to backend | Reason : {res.json()}")

        end_time = datetime.now()
        EXECUTION_TIME += (end_time - start_time).total_seconds()
