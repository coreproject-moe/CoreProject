import asyncio
from datetime import datetime, timedelta
import functools
from io import BytesIO
import json
import os
from pathlib import Path
from pprint import pprint
import textwrap
from typing import Any, Callable, TypeVar, cast

from asgiref.sync import sync_to_async
from core import settings as base_settings
from pyrate_limiter import Duration, Limiter, RedisBucket, RequestRate

from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma, naturaltime
from django.core.files.base import ContentFile
from django.core.management.color import color_style, no_style as django_no_style
from django.db import IntegrityError, connection
import djclick as click

import aiohttp
from aiohttp_client_cache.backends.redis import RedisBackend
from aiohttp_client_cache.session import CachedSession
from aiohttp_retry import ExponentialRetry, RetryClient

from ...models import StaffAlternateNameModel, StaffModel

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


STAFF_LOCK_FILE_NAME = Path(settings.BASE_DIR, "Staff.lock")

CACHE_NAME: base_settings = settings.BUCKET_NAME
RETRY_STATUSES: base_settings = settings.REQUEST_STATUS_CODES_TO_RETRY

JIKAN: dict[str, list[dict[int, str]]] = {}
KITSU: dict[str, list[int]] = {}
ANILIST: dict[str, list[dict[int, str]]] = {}


SUCCESS_LIST = []
WARNING_LIST = []
ERROR_LIST = []

style = color_style()
no_style = django_no_style()
limiter = Limiter(
    RequestRate(1, Duration.SECOND),
    RequestRate(60, Duration.MINUTE),
    bucket_class=RedisBucket,
    bucket_kwargs={
        "bucket_name": CACHE_NAME,
    },
)

# https://stackoverflow.com/questions/43013083/typing-decorator-with-parameters-in-mypy-with-typevar-yields-expected-uninhabite
FuncT = TypeVar("FuncT", bound=Callable[..., Any])


# https://github.com/pallets/click/issues/2033#issue-960810534
def make_sync(func: FuncT) -> FuncT:
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        return asyncio.run(func(*args, **kwargs))

    return cast(FuncT, wrapper)


@click.command()
@make_sync
async def command() -> None:
    retry_client = RetryClient(
        client_session=CachedSession(
            cache=RedisBackend(
                CACHE_NAME,
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
        click.echo("Lock file found. Do you want to use it?")

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

                break

            elif "n" in answer:
                break

    # Everything is new
    if starting_number == 1:
        await StaffModel.objects.all().adelete()
        await StaffAlternateNameModel.objects.all().adelete()

        # Reset SQL Sequence
        @sync_to_async
        def reset_sql_sequence() -> None:
            sequence_sql = connection.ops.sequence_reset_sql(
                no_style,
                [
                    StaffModel,
                    StaffAlternateNameModel,
                ],
            )
            with connection.cursor() as cursor:
                for sql in sequence_sql:
                    cursor.execute(sql)

        await reset_sql_sequence()

    welcome_message = textwrap.dedent(
        f"""
            Starting Number : {
                style.SUCCESS(
                    str(
                        intcomma(
                            staff_number
                        )
                    )
                )
            }
            Total `staff` to get :  {
                style.SUCCESS(
                    str(
                        intcomma(
                            ending_number
                        )
                    )
                )
            }
            Time to finish : {
                style.SUCCESS(
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
                                        settings.MAX_REQUESTS_PER_MINUTE
                                )
                            )
                        )
                    )
                )
            }
        """
    )
    click.echo(welcome_message)

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
            SUCCESS_LIST.append(style.SUCCESS("Kitsu"))

        except IndexError:
            WARNING_LIST.append(style.WARNING("Kitsu"))
            dictionary = KITSU.setdefault("error", [])
            dictionary.append(staff_number)

    else:
        ERROR_LIST.append(style.ERROR("Kitsu"))

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
            SUCCESS_LIST.append(style.SUCCESS("Jikan"))

        else:
            WARNING_LIST.append(style.WARNING("Jikan"))
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
            SUCCESS_LIST.append(style.SUCCESS("Anilist"))

        else:
            dictionary = ANILIST.setdefault("error", [])
            dictionary.append(
                {staff_number: staff_name},
            )
            WARNING_LIST.append(style.WARNING("Anilist"))

    else:
        ERROR_LIST.append(style.ERROR("Anilist"))

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
