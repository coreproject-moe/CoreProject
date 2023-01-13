# STATUS : BORKED
# SOURCE : https://github.com/baseplate-admin/CoreProject/blob/03bbffbb911a82a9d87814b50a4c8279b539e9b7/backend/django_core/apps/staffs/management/commands/populate_staffs.py


import asyncio
import json
import os
import textwrap
from datetime import datetime, timedelta
from io import BytesIO
from typing import Any, cast

import aiohttp
from aiohttp_client_cache.backends.redis import RedisBackend
from aiohttp_client_cache.session import CachedSession
from aiohttp_retry import ExponentialRetry, RetryClient
from humanize import intcomma, naturaltime
from pyrate_limiter import Duration, Limiter, RedisBucket, RequestRate
from termcolor import colored

STAFF_LOCK_FILE_NAME = "Staff.lock"

CACHE_NAME = "staffs"
RETRY_STATUSES = [408, 429, 500, 502, 503, 504]

JIKAN: dict[str, list[dict[int, str]]] = {}
KITSU: dict[str, list[int]] = {}
ANILIST: dict[str, list[dict[int, str]]] = {}

EXECUTION_TIME: int = 0

SUCCESS_LIST = []
WARNING_LIST = []
ERROR_LIST = []

limiter = Limiter(
    RequestRate(1, Duration.SECOND),
    RequestRate(60, Duration.MINUTE),
    bucket_class=RedisBucket,
    bucket_kwargs={
        "bucket_name": CACHE_NAME,
    },
)


async def command() -> None:
    retry_client = RetryClient(  # aiohttp-retry
        client_session=CachedSession(  # aiohttp-client-cache
            cache=RedisBackend(
                CACHE_NAME,
                expire_after=3600,
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
                staff_number = int(data.get("staff_number", staff_number))

                # Load Lists
                global JIKAN, KITSU, ANILIST
                JIKAN = data.get("JIKAN", JIKAN)
                KITSU = data.get("KITSU", KITSU)
                ANILIST = data.get("ANILIST", ANILIST)
                data.get("EXECUTION_TIME", EXECUTION_TIME)

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
            staff_mal_exists = await StaffModel.objects.filter(
                mal_id=data["mal_id"]
            ).aexists()
            if staff_mal_exists:
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
            anilist_id_exists = await StaffModel.objects.filter(
                anilist_id=data["id"]
            ).aexists()
            if anilist_id_exists:
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

    while staff_number < ending_number:
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

            try:
                data_dictionary = {
                    "name": kitsu_data["staff_name"],
                    "mal_id": jikan_data.get("mal_id", None),
                    "anilist_id": anilist_data.get("anilist_id", None),
                    "given_name": jikan_data.get("given_name", None),
                    "family_name": jikan_data.get("family_name", None),
                    "about": jikan_data.get("about", None),
                }
                (instance, _) = await StaffModel.objects.aupdate_or_create(
                    kitsu_id=staff_number,
                    defaults={k: v for k, v in data_dictionary.items() if v is not None},
                )

                if jikan_data:
                    # Try to get webp image first
                    # If that fails get jpg image
                    try:
                        image_url = jikan_data["images"]["webp"]["image_url"]
                    except KeyError:
                        image_url = jikan_data["images"]["jpg"]["image_url"]
                    finally:
                        image = await session.get(image_url)

                        @sync_to_async
                        def save_image_to_database(
                            staff_database: StaffModel,
                            staff_number: int,
                            image_content: bytes,
                            image_url: str,
                        ) -> None:
                            staff_database.staff_image.save(
                                f"{staff_number}.{image_url.split('.')[-1]}",
                                ContentFile(
                                    BytesIO(image_content).read(),
                                ),
                            )

                        await save_image_to_database(
                            staff_database=instance,
                            staff_number=staff_number,
                            image_content=await image.read(),
                            image_url=image_url,
                        )

                for name in jikan_data.get("alternate_names", []):
                    (
                        _instance_,
                        _,
                    ) = await StaffAlternateNameModel.objects.aget_or_create(name=name)

                    @sync_to_async
                    def add_to_database(
                        staff_model: StaffModel,
                        staff_alternate_name_model: StaffAlternateNameModel,
                    ) -> None:
                        staff_model.alternate_names.add(staff_alternate_name_model)

                    await add_to_database(
                        staff_model=instance, staff_alternate_name_model=_instance_
                    )
            except IntegrityError as e:
                click.echo(e)
                click.echo(f"Entry exists : {staff_number}")

            # Add 1 to `starting_number` on every successful request
            starting_number += 1

        success_error_warnings = sorted(
            set(SUCCESS_LIST + ERROR_LIST + WARNING_LIST),
            key=lambda string: string[10],  #  colors are usually 10 digits
        )

        click.echo(
            f"Requested `staff_info` for {staff_number}"
            " | "
            f"""`starting_number` {
                starting_number - 1
                if jikan_data
                else starting_number
            }"""
            " | "
            f"[{', '.join(success_error_warnings)}]"
        )

        # Reset the list
        SUCCESS_LIST.clear()
        ERROR_LIST.clear()
        WARNING_LIST.clear()

        staff_number += 1

        # Log the data to a `.lock` file
        json.dump(
            {
                "staff_number": staff_number,
                "STARTING_NUMBER": starting_number,
                "JIKAN": JIKAN,
                "KITSU": KITSU,
                "ANILIST": ANILIST,
            },
            open(STAFF_LOCK_FILE_NAME, "w", encoding="utf-8"),
            indent=2,
        )


if __name__ == "__main__":
    asyncio.run(command)
