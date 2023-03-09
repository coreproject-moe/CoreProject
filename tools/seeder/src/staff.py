from datetime import datetime
from io import BytesIO
import time
from termcolor import colored

from ._welcome import get_welcome_message
from ._report import get_report_message
from ._session import session


from ._conf import STAFF_ENDPOINT, TOKEN


# Token from from backend
def post_list_to_backend(data_list):
    EXECUTION_TIME = 0
    for index, item in enumerate(data_list):
        start_time = datetime.now()

        file_data = {}
        try:
            image_url = item["images"]["webp"]["image_url"]
        except KeyError:
            image_url = item["images"]["jpg"]["image_url"]
        finally:
            image = session.get(image_url)
            file_data["staff_image"] = (
                f"{index}.{image_url.split('.')[-1]}",
                BytesIO(image.content).read(),
            )

        formdata = {}

        if mal_id := item.get("mal_id"):
            formdata["mal_id"] = mal_id

        if name := item.get("name", None):
            formdata["name"] = name

        if given_name := item.get("given_name", None):
            formdata["given_name"] = given_name

        if family_name := item.get("family_name", None):
            formdata["family_name"] = family_name

        if about := item.get("about", None):
            formdata["about"] = about

        if alternate_names := item.get("alternate_names", None):
            formdata["alternate_names"] = ",".join(alternate_names)

        res = session.post(
            STAFF_ENDPOINT,
            data=formdata,
            files=file_data,
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
                    field_name="staff_info",
                    success_list=[colored("Jikan", color="green")],
                    error_list=[],
                    warning_list=[],
                )
            )
        else:
            raise Exception(f"Cannot POST to backend | Reason : {res.json()}")

        end_time = datetime.now()
        EXECUTION_TIME += (end_time - start_time).total_seconds()


def command() -> None:
    res = session.get("https://api.jikan.moe/v4/people")
    data = res.json()
    total = int(data["pagination"]["last_visible_page"]) * len(data["data"])

    print(
        get_welcome_message(
            base_field_number=1,
            ending_number=total,
            execution_time=0,
            starting_number=1,
            field_name="staff",
        )
    )
    _EXECUTION_TIME_ = 0
    for page in range(0, int(data["pagination"]["last_visible_page"])):
        start = datetime.now()
        _res_ = session.get(f"https://api.jikan.moe/v4/people?page={page}")

        print(
            get_report_message(
                base_field_number=page + 1,
                starting_number=page + 1,
                execution_time=_EXECUTION_TIME_,
                field_name="bulk_staff_info",
                success_list=[colored("Jikan", color="green")],
                error_list=[],
                warning_list=[],
            )
        )

        if data := _res_.json().get("data"):
            post_list_to_backend(data)
        else:
            raise Exception(f"Why did this fail | Reason : {_res_.json()}")

        end = datetime.now()
        _EXECUTION_TIME_ += (end - start).total_seconds()
