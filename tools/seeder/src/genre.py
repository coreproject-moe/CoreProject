from ._session import Session
from ._conf import ANIME_GENRE_ENDPOINT, TOKEN
from ._welcome import get_welcome_message


def command() -> None:
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

    session.post(
        ANIME_GENRE_ENDPOINT,
        data=data_list,
        headers={
            "Authorization": f"Bearer {TOKEN}",
        },
    )
