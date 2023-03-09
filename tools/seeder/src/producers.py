from ._session import Session
from ._conf import PRODUCER_ENDPOINT, TOKEN
from ._welcome import get_welcome_message
from ._report import get_report_message
from ._utils import date_converter
import time
from termcolor import colored
from datetime import datetime

EXECUTION_TIME = 0


def command() -> None:
    global EXECUTION_TIME

    session = Session()

    res = session.get("https://api.jikan.moe/v4/producers")
    data = res.json()

    print(
        get_welcome_message(
            base_field_number=1,
            ending_number=int(data["pagination"]["items"]["total"])
            * int(data["pagination"]["items"]["per_page"]),
            execution_time=0,
            starting_number=1,
            field_name="producers",
        )
    )

    data_list = []
    _EXECUTION_TIME_ = 0

    for page in range(0, data["pagination"]["last_visible_page"]):
        start = datetime.now()
        time.sleep(1)
        _res_ = session.get(f"https://api.jikan.moe/v4/producers?page={page}")
        print(
            get_report_message(
                base_field_number=page + 1,
                starting_number=page + 1,
                execution_time=_EXECUTION_TIME_,
                field_name="bulk_producer_info",
                success_list=[colored("Jikan", color="green")],
                error_list=[],
                warning_list=[],
            )
        )

        if data := _res_.json().get("data"):
            for item in data:
                data_list.append(item)

        else:
            raise Exception(f"Why did this fail | Reason : {_res_.json()}")

        end = datetime.now()
        _EXECUTION_TIME_ += (end - start).total_seconds()

    for index, item in enumerate(data_list):
        start_time = datetime.now()
        print(
            get_report_message(
                base_field_number=index + 1,
                starting_number=index + 1,
                execution_time=EXECUTION_TIME,
                field_name="producer_info",
                success_list=[colored("Jikan", color="green")],
                error_list=[],
                warning_list=[],
            )
        )

        titles = item.get("titles", [])
        title = titles[0]["title"] if titles else ""
        japanese_title = titles[1]["title"] if len(titles) > 1 else ""
        data = {
            "mal_id": item["mal_id"],
            "name": title,
            "default_title": title,
            "japanese_title": japanese_title,
            "established": date_converter(item["established"]),
            "about": item["about"],
        }

        res = session.post(
            PRODUCER_ENDPOINT,
            json=data,
            headers={
                "Authorization": f"Bearer {TOKEN}",
            },
        )
        end_time = datetime.now()
        EXECUTION_TIME += (end_time - start_time).total_seconds()
