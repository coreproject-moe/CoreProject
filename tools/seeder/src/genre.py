from ._session import Session
from ._conf import ANIME_GENRE_ENDPOINT, TOKEN
from ._welcome import get_welcome_message
from ._report import get_report_message

from termcolor import colored
from datetime import datetime

EXECUTION_TIME = 0


def command() -> None:
    global EXECUTION_TIME

    session = Session()
    res = session.get("https://api.jikan.moe/v4/genres/anime")
    data_list = res.json()["data"]
    for data in data_list:
        data.pop("url")
        data.pop("count")

    print(
        get_welcome_message(
            base_field_number=1,
            ending_number=len(data_list),
            execution_time=0,
            starting_number=1,
            field_name="genre",
        )
    )

    for index, item in enumerate(data_list):
        start_time = datetime.now()
        print(
            get_report_message(
                base_field_number=index + 1,
                starting_number=index + 1,
                execution_time=EXECUTION_TIME,
                field_name="genre_info",
                success_list=[colored("Jikan", color="green")],
                error_list=[],
                warning_list=[],
            )
        )

        res = session.post(
            ANIME_GENRE_ENDPOINT,
            json=([item]),
            headers={
                "Authorization": f"Bearer {TOKEN}",
            },
        )
        end_time = datetime.now()
        EXECUTION_TIME += (end_time - start_time).total_seconds()
