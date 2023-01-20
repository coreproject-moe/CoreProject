# STATUS : BORKED
# SOURCE : https://github.com/baseplate-admin/CoreProject/blob/03bbffbb911a82a9d87814b50a4c8279b539e9b7/backend/django_core/apps/staffs/management/commands/populate_staffs.py

import asyncio
from datetime import datetime, timedelta
from io import BytesIO
import json
import os
import textwrap
from typing import Any, cast
from aiohttp import FormData

from humanize import intcomma, naturaltime
from pyrate_limiter import Duration, Limiter, RedisBucket, RequestRate
from termcolor import colored

import aiohttp
from aiohttp_client_cache.backends.redis import RedisBackend
from aiohttp_client_cache.session import CachedSession
from aiohttp_retry import ExponentialRetry, RetryClient

STAFF_LOCK_FILE_NAME = "Staff.lock"

CACHE_NAME = "staffs"
RETRY_STATUSES = [408, 429, 500, 502, 503, 504]

JIKAN: dict[str, list[dict[int, str]]] = {}
KITSU: dict[str, list[int]] = {}
ANILIST: dict[str, list[dict[int, str]]] = {}

EXECUTION_TIME: int = 0

SUCCESSFUL_JIKAN_IDS = []
SUCCESSFUL_ANILIST_IDS = []

SUCCESS_LIST = []
WARNING_LIST = []
ERROR_LIST = []

BACKEND_API_URL = "http://127.0.0.1:8000/api/v1/staffs"

limiter = Limiter(
    RequestRate(1, Duration.SECOND),
    RequestRate(60, Duration.MINUTE),
    bucket_class=RedisBucket,
    bucket_kwargs={
        "bucket_name": CACHE_NAME,
    },
)


async def command() -> None:
    global JIKAN, KITSU, ANILIST, DATABASE_ID, EXECUTION_TIME, SUCCESSFUL_NAMES, SUCCESSFUL_JIKAN_IDS, SUCCESSFUL_ANILIST_IDS

    retry_client = RetryClient(  # aiohttp-retry
        client_session=CachedSession(  # aiohttp-client-cache
            cache=RedisBackend(
                CACHE_NAME,
                expire_after=10,
            )
        ),
        retry_options=ExponentialRetry(
            attempts=10,
            max_timeout=100.00,
            statuses=set(RETRY_STATUSES),
        ),
    )

    session = cast(aiohttp.ClientSession, retry_client)

    starting_number = 1
    staff_number = 1
    ending_number: int = await get_ending_number(session)

    # Load JSON file and get data from it
    if os.path.exists(STAFF_LOCK_FILE_NAME):
        print("Lock file found. Do you want to use it?")

        # While loop to ask for data
        while True:
            answer = input("\r").lower()

            if "y" in answer:
                data = json.load(open(STAFF_LOCK_FILE_NAME, encoding="utf-8"))
                starting_number = int(data.get("STARTING_NUMBER", starting_number))
                staff_number = int(data.get("STAFF_NUMBER", staff_number))

                # Load Lists
                JIKAN = data.get("JIKAN", JIKAN)
                KITSU = data.get("KITSU", KITSU)
                ANILIST = data.get("ANILIST", ANILIST)
                EXECUTION_TIME = data.get("EXECUTION_TIME", EXECUTION_TIME)
                SUCCESSFUL_JIKAN_IDS = data.get(
                    "SUCCESSFUL_JIKAN_IDS", SUCCESSFUL_JIKAN_IDS
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
                    str(
                        intcomma(
                            staff_number
                        )
                    ),
                    color='green'

                )
            }
            Total `staff` to get :  {
                colored(
                    str(
                        intcomma(
                            ending_number
                        )
                    ),
                    color='green'
                )
            }
            Time to finish : {
                colored(
                    str(
                        naturaltime(
                            datetime.now()
                            +
                            timedelta(
                                minutes=
                                    round(
                                        (
                                            ending_number
                                            -
                                            staff_number
                                        )
                                        /
                                        60
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
    await populate_database(
        session=session,
        starting_number=starting_number,
        staff_number=staff_number,
        ending_number=ending_number,
    )

    await session.close()

    # Remove lock file
    os.remove(STAFF_LOCK_FILE_NAME)


@limiter.ratelimit("ending", delay=True)
async def get_ending_number(
    session: aiohttp.ClientSession,
) -> int:
    """
    :param session: `aiohttp.Client` instance to get data
    """
    res = await session.get("https://kitsu.io/api/edge/people/")
    data = await res.json()
    return int(data["meta"]["count"])


@limiter.ratelimit("kitsu", delay=True)
async def get_staff_data_from_kitsu(
    staff_number: int,
    session: aiohttp.ClientSession,
) -> dict[str, str | None] | None:
    """
    :param staff_number: The id of the staff
    :param session: `aiohttp.Client` instance to get data
    """
    res = await session.get(f"https://kitsu.io/api/edge/people/{staff_number}")
    res_data = await res.json()

    returnable_data = {}

    if res.status == 200:
        try:
            data = res_data["data"]
            returnable_data = {
                "staff_name": data["attributes"]["name"],
            }
            SUCCESS_LIST.append(colored("Kitsu", color="green"))

        except IndexError:
            WARNING_LIST.append(colored("Kitsu", color="yellow"))
            dictionary = KITSU.setdefault("error", [])
            dictionary.append(staff_number)

    else:
        ERROR_LIST.append(colored("Kitsu", color="red"))

    return returnable_data


@limiter.ratelimit("jikan", delay=True)
async def get_staff_data_from_jikan(
    staff_name: int,
    staff_number: int,
    session: aiohttp.ClientSession,
) -> dict[str, str | None | BytesIO] | None:
    """
    :param staff_number: The id of staff
    :param staff_name: The name of staff
    :param session: `aiohttp.Client` instance to get data
    """
    returnable_data: dict[Any, Any] = {}
    if not staff_name:
        return returnable_data

    # In jikan staff = people
    res = await session.get(f"https://api.jikan.moe/v4/people/?q={staff_name}")
    res_data = await res.json()

    returnable_data = {}

    if res.status == 200:
        for data in res_data["data"]:
            # If the MyAnimeList ID exists in database
            # Skip to next iteration
            if data["mal_id"] in SUCCESSFUL_JIKAN_IDS:
                continue

            returnable_data = data

        if returnable_data:
            SUCCESS_LIST.append(colored("Jikan", color="green"))

        else:
            WARNING_LIST.append(colored("Jikan", color="yellow"))
            dictionary = JIKAN.setdefault("error", [])
            dictionary.append(
                {staff_number: staff_name},
            )

    # We need none as output if theres no data
    return returnable_data


@limiter.ratelimit("kitsu", delay=True)
async def get_staff_data_from_anilist(
    staff_name: str,
    staff_number: int,
    session: aiohttp.ClientSession,
) -> dict[str, str | None] | None:
    """
    :param staff_number: The id of the staff
    :param staff_name: The name of the staff
    :param session: `aiohttp.Client instance to get data
    """
    returnable_data = {}
    if not staff_name:
        return returnable_data

    query = {
        "query": """
            query (
                $page:Int = 1
                $id:Int
                $search:String
                $isBirthday:Boolean
                $sort:[StaffSort]=[FAVOURITES_DESC]
            ) {
                Page(
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
                    staff (
                        id:$id
                        search:$search
                        isBirthday:$isBirthday
                        sort:$sort
                    ) {
                        id name{userPreferred}
                        image{large}
                    }
                }
            }
        """,
        "variables": {
            "page": 1,
            "type": "STAFF",
            "search": staff_name,
            "sort": "SEARCH_MATCH",
        },
    }
    res = await session.post(url="https://graphql.anilist.co/", json=query)
    res_data = await res.json()

    if res_data and res.status == 200:
        for data in res_data["data"]["Page"]["staff"]:
            # If the Anilist ID exists in database
            # Skip to next iteration
            if data["id"] in SUCCESSFUL_ANILIST_IDS:
                continue

            returnable_data = {
                "anilist_id": data["id"],
            }

        if returnable_data.get("anilist_id"):
            SUCCESS_LIST.append(colored("Anilist", color="green"))

        else:
            dictionary = ANILIST.setdefault("error", [])
            dictionary.append(
                {staff_number: staff_name},
            )
            WARNING_LIST.append(colored("Anilist", color="yellow"))

    else:
        ERROR_LIST.append(colored("Anilist", color="red"))

    return returnable_data


async def populate_database(
    session: aiohttp.ClientSession,
    staff_number: int,
    starting_number: int,
    ending_number: int,
) -> None:
    global EXECUTION_TIME

    while staff_number < ending_number:
        start_time = datetime.now()

        kitsu_data = await get_staff_data_from_kitsu(
            staff_number=staff_number,
            session=session,
        )

        if kitsu_data:
            jikan_data = await get_staff_data_from_jikan(
                staff_number=staff_number,
                staff_name=kitsu_data["staff_name"],
                session=session,
            )
            anilist_data = await get_staff_data_from_anilist(
                staff_number=staff_number,
                staff_name=kitsu_data["staff_name"],
                session=session,
            )

            formdata = FormData()
            formdata.add_field("name", kitsu_data["staff_name"])
            formdata.add_field("kitsu_id", str(staff_number))

            if mal_id := jikan_data.get("mal_id", None):
                formdata.add_field("mal_id", str(mal_id))

            if anilist_id := anilist_data.get("anilist_id", None):
                formdata.add_field("anilist_id", str(anilist_id))

            if given_name := jikan_data.get("given_name", None):
                formdata.add_field("given_name", given_name)

            if family_name := jikan_data.get("family_name", None):
                formdata.add_field("family_name", family_name)

            if about := jikan_data.get("about", None):
                formdata.add_field("about", about)

            # M2M Alternate name field
            if alternate_names := jikan_data.get("alternate_names", None):
                formdata.add_field("alternate_names", ",".join(alternate_names))

            if jikan_data:
                # Try to get webp image first
                # If that fails get jpg image
                try:
                    image_url = jikan_data["images"]["webp"]["image_url"]
                except KeyError:
                    image_url = jikan_data["images"]["jpg"]["image_url"]
                finally:
                    image = await session.get(image_url)
                    formdata.add_field(
                        "staff_image",
                        BytesIO(await image.read()).read(),
                        filename=f"{staff_number}.{image_url.split('.')[-1]}",
                    )

            res = await session.post(BACKEND_API_URL, data=formdata)
            if res.status == 200:
                SUCCESSFUL_JIKAN_IDS.append(jikan_data.get("mal_id"))
                SUCCESSFUL_ANILIST_IDS.append(anilist_data.get("anilist_id"))
            else:
                print(await res.text())
                raise Exception

            # Add 1 to `starting_number` on every successful request
            starting_number += 1

        end_time = datetime.now()
        EXECUTION_TIME += (end_time - start_time).total_seconds()

        print(
            f"[{EXECUTION_TIME:.2f}]"
            " "
            f"Requested `staff_info` for {staff_number}"
            " | "
            f"""`starting_number` {
                starting_number - 1
                if jikan_data
                else starting_number
            }"""
            " | "
            f"""[{', '.join(
                sorted(
                        set(
                            SUCCESS_LIST
                            + ERROR_LIST 
                            + WARNING_LIST
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

        staff_number += 1
        log_dictionary = {
            "STAFF_NUMBER": staff_number,
            "STARTING_NUMBER": starting_number,
            "JIKAN": JIKAN,
            "KITSU": KITSU,
            "ANILIST": ANILIST,
            "EXECUTION_TIME": EXECUTION_TIME,
            "SUCCESSFUL_JIKAN_IDS": SUCCESSFUL_JIKAN_IDS,
            "SUCCESSFUL_ANILIST_IDS": SUCCESSFUL_ANILIST_IDS,
        }

        # Log the data to a `.lock` file
        json.dump(
            log_dictionary,
            open(STAFF_LOCK_FILE_NAME, "w", encoding="utf-8"),
            indent=2,
        )


if __name__ == "__main__":
    asyncio.run(command())
