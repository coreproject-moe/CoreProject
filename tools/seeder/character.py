from datetime import datetime, timedelta
from io import BytesIO
import json
import os
import textwrap

from humanize import intcomma, naturaltime
from termcolor import colored


from requests.sessions import Session
from _session import session

CHARACTER_LOCK_FILE_NAME = "Character.lock"

EXECUTION_TIME: int = 0

JIKAN: dict[int, list[int]] = {}
KITSU: dict[str, list[dict[int, str]]] = {}
ANILIST: dict[str, list[dict[int, str]]] = {}

SUCCESSFUL_KITSU_IDS = []
SUCCESSFUL_ANILIST_IDS = []

SUCCESS_LIST = []
WARNING_LIST = []
ERROR_LIST = []

BACKEND_API_URL = "http://127.0.0.1:8000/api/v1/characters"


def command() -> None:
    global JIKAN, KITSU, ANILIST
    global EXECUTION_TIME
    global SUCCESSFUL_KITSU_IDS, SUCCESSFUL_ANILIST_IDS

    starting_number = 1
    character_number = 1
    ending_number: int = get_ending_number(session)

    # Load JSON file and get data from it
    if os.path.exists(CHARACTER_LOCK_FILE_NAME):
        print("Lock file found. Do you want to use it?")

        # While loop to ask for data
        while True:
            answer = input("\r").lower()

            if "y" in answer:
                data = json.load(open(CHARACTER_LOCK_FILE_NAME, encoding="utf-8"))
                starting_number = int(data.get("STARTING_NUMBER", starting_number))
                character_number = int(data.get("CHARACTER_NUMBER", character_number))

                JIKAN = data.get("JIKAN", JIKAN)
                KITSU = data.get("KITSU", KITSU)
                ANILIST = data.get("ANILIST", ANILIST)
                EXECUTION_TIME = data.get("EXECUTION_TIME", EXECUTION_TIME)
                SUCCESSFUL_KITSU_IDS = data.get(
                    "SUCCESSFUL_KITSU_IDS", SUCCESSFUL_KITSU_IDS
                )
                SUCCESSFUL_ANILIST_IDS = data.get(
                    "SUCCESSFUL_ANILIST_IDS", SUCCESSFUL_ANILIST_IDS
                )
                break

            elif "n" in answer:
                break

    welcome_message = textwrap.dedent(
        f"""
            Starting Number : {
                colored(
                    text=str(
                        intcomma(
                            character_number
                        )
                    ),
                    color='green'
                )
            }
            Total `characters` to get : {
                colored(
                    text=str(
                        intcomma(
                            ending_number
                        )
                    ),
                    color='green'
                )
            }
            Time to finish : {
                colored(
                    text=str(
                        naturaltime(
                            datetime.now()
                            +
                            timedelta(
                                seconds=
                                    round(
                                        (
                                            ending_number
                                            -
                                            character_number
                                        )
                                        *
                                        (
                                            EXECUTION_TIME
                                            /
                                            starting_number
                                        )
                                )
                            )
                        )
                    ),
                    color='green'
                )
            }
        """
    )
    print(welcome_message)

    # Magic starts here
    populate_database(
        session=session,
        starting_number=starting_number,
        character_number=character_number,
        ending_number=ending_number,
    )

    session.close()

    # Remove lock file
    os.remove(CHARACTER_LOCK_FILE_NAME)


def get_ending_number(
    session: Session,
) -> int:
    """
    :param session: `requests.Session` instance to get data
    """
    res = session.get("https://api.jikan.moe/v4/characters")
    data = res.json()
    return int(data["pagination"]["items"]["total"])


def get_character_data_from_jikan(
    character_number: int,
    session: Session,
) -> dict[str, str | None | BytesIO] | None:
    """
    :param character_number: The id of character
    :param session: `requests.Session` instance to get data
    """
    res = session.get(f"https://api.jikan.moe/v4/characters/{character_number}")
    data = res.json()

    returnable_data = {}

    if res.status_code == 200 and str(data.get("status", None)) not in [
        "403",
        "404",
        "408",
        "429",
        "500",
    ]:
        SUCCESS_LIST.append(colored("Jikan", "green"))

        data = data["data"]

        # Try to get webp image first
        # If that fails get jpg image
        try:
            image_url = data["images"]["webp"]["image_url"]
        except KeyError:
            image_url = data["images"]["jpg"]["image_url"]
        finally:
            image = session.get(image_url)

        returnable_data = {
            "character_name": data["name"],
            "character_name_kanji": data.get("name_kanji", None),
            "character_about": data.get("about", None),
            "image_url": image_url,
            "character_image": BytesIO(
                image.content,
            ),
        }
    elif data.get("status", None) == 403:
        dictionary = JIKAN.setdefault(403, [])
        dictionary.append(character_number)

        ERROR_LIST.append(colored("Jikan", "red"))

    elif data.get("status", None) == 408:
        dictionary = JIKAN.setdefault(408, [])
        dictionary.append(character_number)

        WARNING_LIST.append(colored("Jikan", "yellow"))

    elif data.get("status", None) == 500:
        dictionary = JIKAN.setdefault(500, [])
        dictionary.append(character_number)

        ERROR_LIST.append(colored("Jikan", "yellow"))

    else:
        ERROR_LIST.append(colored("Jikan", "red"))

    # We need none as output if theres no data
    return returnable_data


def get_character_data_from_kitsu(
    character_number: int,
    character_name: str,
    session: Session,
) -> dict[str, str | None] | None:
    """
    :param character_name: The name of the character
    :param session: `requests.Session` instance to get data
    """
    res = session.get(
        f"https://kitsu.io/api/edge/characters?filter[name]:{character_name}",
    )
    res_data = res.json()

    returnable_data = {}

    if res.status_code == 200:
        for data in res_data["data"]:
            # If the Kitsu ID exists in database
            # Skip to next iteration
            if data["id"] in SUCCESSFUL_KITSU_IDS:
                continue

            returnable_data = {
                "kitsu_id": data["id"],
                "character_name_kanji": data["attributes"]["names"].get("ja_jp"),
            }

        if returnable_data.get("kitsu_id"):
            SUCCESS_LIST.append(colored("Kitsu", "green"))

        else:
            WARNING_LIST.append(colored("Kitsu", "yellow"))
            dictionary = KITSU.setdefault("error", [])
            dictionary.append(
                {character_number: character_name},
            )

    else:
        ERROR_LIST.append(colored("Kitsu", "red"))

    return returnable_data


def get_character_data_from_anilist(
    character_number: int,
    character_name: str,
    session: Session,
) -> dict[str, str | None] | None:
    """
    :param character_name: The name of the character
    :param session: `requests.Session instance to get data
    """
    query = {
        "query": """
            query (
                $page:Int = 1
                $id:Int
                $search:String
                $isBirthday:Boolean
                $sort:[CharacterSort]=[FAVOURITES_DESC]
            ) {
                Page (
                    page:$page,
                    perPage:20
                ) {
                    pageInfo {
                        total
                        perPage
                        currentPage
                        lastPage
                        hasNextPage
                    }
                    characters (
                        id:$id
                        search:$search
                        isBirthday:$isBirthday
                        sort:$sort
                    ) {
                        id
                        name
                        {userPreferred}
                        image
                        {large}
                    }
                }
            }
        """,
        "variables": {
            "page": 1,
            "type": "CHARACTERS",
            "search": character_name,
            "sort": "SEARCH_MATCH",
        },
    }
    res = session.post(url="https://graphql.anilist.co/", json=query)
    res_data = res.json()

    returnable_data = {}

    if res_data and res.status_code == 200:
        for data in res_data["data"]["Page"]["characters"]:
            # If the Anilist ID exists in database
            # Skip to next iteration
            if data["id"] in SUCCESSFUL_ANILIST_IDS:
                continue

            returnable_data = {
                "anilist_id": data["id"],
            }

        if returnable_data.get("anilist_id"):
            SUCCESS_LIST.append(colored("Anilist", "green"))

        else:
            WARNING_LIST.append(colored("Anilist", "yellow"))
            dictionary = ANILIST.setdefault("error", [])
            dictionary.append(
                {character_number: character_name},
            )

    else:
        ERROR_LIST.append(colored("Anilist", "yellow"))

    return returnable_data


def populate_database(
    session: Session,
    character_number: int,
    starting_number: int,
    ending_number: int,
) -> None:
    global EXECUTION_TIME

    while starting_number <= ending_number:
        start_time = datetime.now()

        # Actual work is being done here
        jikan_data = get_character_data_from_jikan(
            character_number=character_number,
            session=session,
        )

        if jikan_data:
            kitsu_data = get_character_data_from_kitsu(
                character_number=character_number,
                character_name=jikan_data["character_name"],
                session=session,
            )
            anilist_data = get_character_data_from_anilist(
                character_number=character_number,
                character_name=jikan_data["character_name"],
                session=session,
            )

            formdata = {}
            file_data = {}

            if kitsu_id := kitsu_data.get("kitsu_id", None):
                formdata["kitsu_id"] = str(kitsu_id)

            if anilist_id := anilist_data.get("anilist_id", None):
                formdata["anilist_id"] = str(anilist_id)

            formdata["mal_id"] = str(starting_number)
            formdata["name"] = str(jikan_data["character_name"])

            if name_kanji := (
                jikan_data.get("character_name_kanji", None)
                or kitsu_data.get("character_name_kanji", None)
            ):
                formdata["name_kanji"] = name_kanji

            file_data["character_image"] = (
                f"{character_number}.{jikan_data['image_url'].split('.')[-1]}",
                BytesIO(jikan_data["character_image"].read()),
            )
            if about := jikan_data.get("character_about", None):
                formdata["about"] = about

            res = session.post(BACKEND_API_URL, data=formdata, files=file_data)
            if res.status_code == 200:
                if successful_kitsu_id := kitsu_data.get("kitsu_id", None):
                    SUCCESSFUL_KITSU_IDS.append(successful_kitsu_id)
                if successful_anilist_id := anilist_data.get("anilist_id", None):
                    SUCCESSFUL_ANILIST_IDS.append(successful_anilist_id)

            else:
                print(res.text)
                raise Exception

            # Add 1 to `starting_number` on every successful request
            starting_number += 1

        # Profile Execution of this function
        end_time = datetime.now()
        EXECUTION_TIME += (end_time - start_time).total_seconds()

        message = (
            f"[{round(EXECUTION_TIME, 2):2f}]"
            " "
            f"Requested `character_info` for {character_number}"
            " | "
            f"""`starting_number` {
                    starting_number - 1
                    if jikan_data else starting_number
            }"""
            " | "
            f"""[{', '.join(
                sorted(
                    (
                        SUCCESS_LIST +
                        ERROR_LIST +
                        WARNING_LIST
                    ),
                    key=lambda string: string[10],
                    )
                )
            }]"""
        )
        # Reset the list
        SUCCESS_LIST.clear()
        ERROR_LIST.clear()
        WARNING_LIST.clear()

        character_number += 1
        log_dictionary = {
            "CHARACTER_NUMBER": character_number,
            "STARTING_NUMBER": starting_number,
            "JIKAN": JIKAN,
            "KITSU": KITSU,
            "ANILIST": ANILIST,
            "EXECUTION_TIME": EXECUTION_TIME,
            "SUCCESSFUL_KITSU_IDS": SUCCESSFUL_KITSU_IDS,
            "SUCCESSFUL_ANILIST_IDS": SUCCESSFUL_ANILIST_IDS,
        }

        # Log the data to a `.lock` file
        json.dump(
            log_dictionary,
            open(CHARACTER_LOCK_FILE_NAME, "w", encoding="utf-8"),
            indent=2,
        )

        print(message)


if __name__ == "__main__":
    command()
