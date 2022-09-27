import asyncio
from collections.abc import Callable
from datetime import datetime, timedelta
import functools
from io import BytesIO
import json
import os
from pathlib import Path
import textwrap
from typing import Any, TypeVar, cast

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

from ...models import CharacterLogModel, CharacterModel

try:
    import uvloop

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass


CHARACTER_LOCK_FILE_NAME = Path(settings.BASE_DIR, "Character.lock")

CACHE_NAME: base_settings = settings.BUCKET_NAME
RETRY_STATUSES: base_settings = settings.REQUEST_STATUS_CODES_TO_RETRY

DATABASE_ID: int | None = None
JIKAN: dict[int, list[int]] = {}
KITSU: dict[str, list[dict[int, str]]] = {}
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
@click.argument("no_input", required=False, default=False)
@click.argument("headless", required=False, default=False)
@click.argument("reset", required=False, default=False)
@make_sync
async def command(no_input: bool, headless: bool, reset: bool) -> None:
    global JIKAN, KITSU, ANILIST, DATABASE_ID

    retry_client = RetryClient(  # aiohttp-retry
        client_session=CachedSession(  # aiohttp-client-cache
            cache=RedisBackend(
                CACHE_NAME,
                expire_after=settings.CACHE_MIDDLEWARE_SECONDS,
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
    character_number = 1
    ending_number: int = await get_ending_number(session)

    if headless:
        database: CharacterLogModel = await CharacterLogModel.objects.alast()
        database_starting_number = database.log_dictionary.get("STARTING_NUMBER")

        # get the last item from database and get data from it
        if not database_starting_number == ending_number and not reset:
            data = database.log_dictionary
            starting_number = int(data.get("STARTING_NUMBER", starting_number))
            character_number = int(data.get("CHARACTER_NUMBER", character_number))

            JIKAN = data.get("JIKAN", JIKAN)
            KITSU = data.get("KITSU", KITSU)
            ANILIST = data.get("ANILIST", ANILIST)

        else:
            database = await CharacterLogModel.objects.acreate(
                log_dictionary={},
                logs="",
            )

        DATABASE_ID = database.pk

    else:
        # Load JSON file and get data from it
        if os.path.exists(CHARACTER_LOCK_FILE_NAME) and no_input:
            click.echo("Lock file found. Do you want to use it?")

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

                    break

                elif "n" in answer:
                    break

    # Everything is new
    if starting_number == 1:
        # Reset SQL Sequence
        @sync_to_async
        def reset_sql_sequence() -> None:
            CharacterModel.objects.all().delete()
            sequence_sql = connection.ops.sequence_reset_sql(
                no_style,
                [
                    CharacterModel,
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
                            character_number
                        )
                    )
                )
            }
            Total `characters` to get : {
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
                                            character_number
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
        character_number=character_number,
        ending_number=ending_number,
        headless=headless,
    )

    await session.close()

    # Remove lock file
    os.remove(CHARACTER_LOCK_FILE_NAME)


@limiter.ratelimit("ending", delay=True)
async def get_ending_number(
    session: aiohttp.ClientSession,
) -> int:
    """
    :param session: `aiohttp.Client` instance to get data
    """
    res = await session.get("https://api.jikan.moe/v4/characters")
    data = await res.json()
    return int(data["pagination"]["items"]["total"])


@limiter.ratelimit("jikan", delay=True)
async def get_character_data_from_jikan(
    character_number: int,
    session: aiohttp.ClientSession,
) -> dict[str, str | None | BytesIO] | None:
    """
    :param character_number: The id of character
    :param session: `aiohttp.Client` instance to get data
    """
    res = await session.get(f"https://api.jikan.moe/v4/characters/{character_number}")
    data = await res.json()

    returnable_data = {}

    if res.status == 200 and str(data.get("status", None)) not in [
        "404",
        "408",
        "429",
        "500",
    ]:
        SUCCESS_LIST.append(style.SUCCESS("Jikan"))

        data = data["data"]

        # Try to get webp image first
        # If that fails get jpg image
        try:
            image_url = data["images"]["webp"]["image_url"]
        except KeyError:
            image_url = data["images"]["jpg"]["image_url"]
        finally:
            image = await session.get(image_url)

        returnable_data = {
            "character_name": data["name"],
            "character_name_kanji": data.get("name_kanji", None),
            "character_about": data.get("about", None),
            "image_url": image_url,
            "character_image": BytesIO(
                await image.read(),
            ),
        }

    elif data.get("status", None) == 408:
        dictionary = JIKAN.setdefault(408, [])
        dictionary.append(character_number)

        WARNING_LIST.append(style.WARNING("Jikan"))

    elif data.get("status", None) == 500:
        dictionary = JIKAN.setdefault(500, [])
        dictionary.append(character_number)

        ERROR_LIST.append(style.WARNING("Jikan"))

    else:
        ERROR_LIST.append(style.ERROR("Jikan"))

    # We need none as output if theres no data
    return returnable_data


@limiter.ratelimit("kitsu", delay=True)
async def get_character_data_from_kitsu(
    character_number: int,
    character_name: str,
    session: aiohttp.ClientSession,
) -> dict[str, str | None] | None:
    """
    :param character_name: The name of the character
    :param session: `aiohttp.Client` instance to get data
    """
    res = await session.get(
        f"https://kitsu.io/api/edge/characters?filter[name]:{character_name}",
    )
    res_data = await res.json()

    returnable_data = {}

    if res.status == 200:
        for data in res_data["data"]:
            # If the Kitsu ID exists in database
            # Skip to next iteration
            character_kitsu_entry_exists: bool = await CharacterModel.objects.filter(
                kitsu_id=data["id"],
            ).aexists()
            if character_kitsu_entry_exists:
                continue

            returnable_data = {
                "kitsu_id": data["id"],
                "character_name_kanji": data["attributes"]["names"].get("ja_jp"),
            }

        if returnable_data.get("kitsu_id"):
            SUCCESS_LIST.append(style.SUCCESS("Kitsu"))

        else:
            WARNING_LIST.append(style.WARNING("Kitsu"))
            dictionary = KITSU.setdefault("error", [])
            dictionary.append(
                {character_number: character_name},
            )

    else:
        ERROR_LIST.append(style.ERROR("Kitsu"))

    return returnable_data


@limiter.ratelimit("kitsu", delay=True)
async def get_character_data_from_anilist(
    character_number: int,
    character_name: str,
    session: aiohttp.ClientSession,
) -> dict[str, str | None] | None:
    """
    :param character_name: The name of the character
    :param session: `aiohttp.Client instance to get data
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
    res = await session.post(url="https://graphql.anilist.co/", json=query)
    res_data = await res.json()

    returnable_data = {}

    if res_data and res.status == 200:
        for data in res_data["data"]["Page"]["characters"]:
            # If the Anilist ID exists in database
            # Skip to next iteration
            character_anilist_entry_exists: bool = await CharacterModel.objects.filter(
                anilist_id=data["id"],
            ).aexists()
            if character_anilist_entry_exists:
                continue

            returnable_data = {
                "anilist_id": data["id"],
            }

        if returnable_data.get("anilist_id"):
            SUCCESS_LIST.append(style.SUCCESS("Anilist"))

        else:
            WARNING_LIST.append(style.WARNING("Anilist"))
            dictionary = ANILIST.setdefault("error", [])
            dictionary.append(
                {character_number: character_name},
            )

    else:
        ERROR_LIST.append(style.WARNING("Anilist"))

    return returnable_data


async def populate_database(
    session: aiohttp.ClientSession,
    character_number: int,
    starting_number: int,
    ending_number: int,
    headless: bool,
) -> None:
    while starting_number <= ending_number:
        jikan_data = await get_character_data_from_jikan(
            character_number=character_number,
            session=session,
        )

        if jikan_data:
            try:
                kitsu_data = await get_character_data_from_kitsu(
                    character_number=character_number,
                    character_name=jikan_data["character_name"],
                    session=session,
                )
                anilist_data = await get_character_data_from_anilist(
                    character_number=character_number,
                    character_name=jikan_data["character_name"],
                    session=session,
                )
                data_dictionary = {
                    "kitsu_id": kitsu_data.get("kitsu_id", None),
                    "anilist_id": anilist_data.get("anilist_id", None),
                    "name": jikan_data["character_name"],
                    "name_kanji": jikan_data.get("character_name_kanji", None)
                    or kitsu_data.get("character_name_kanji", None),
                    "character_image": ContentFile(
                        jikan_data["character_image"].read(),
                        f"{character_number}.{jikan_data['image_url'].split('.')[-1]}",
                    ),
                    "about": jikan_data["character_about"],
                }
                await CharacterModel.objects.aupdate_or_create(
                    mal_id=character_number,
                    defaults={k: v for k, v in data_dictionary.items() if v is not None},
                )

            except IntegrityError as e:
                click.echo(e)
                click.echo(f"Entry exists : {character_number}")

            # Add 1 to `starting_number` on every successful request
            starting_number += 1

        message = (
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
        }

        if headless:

            @sync_to_async
            def save_to_db():
                database = CharacterLogModel.objects.get(pk=DATABASE_ID)
                database.log_dictionary = log_dictionary
                database.logs += "\n" + message
                database.save()

            await save_to_db()

        # Log the data to a `.lock` file
        else:
            json.dump(
                log_dictionary,
                open(CHARACTER_LOCK_FILE_NAME, "w", encoding="utf-8"),
                indent=2,
            )

        click.secho(message)
