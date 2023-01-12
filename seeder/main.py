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

import httpx


async def get_ending_number(
    session: aiohttp.ClientSession,
) -> int:
    """
    :param session: `aiohttp.Client` instance to get data
    """
    res = await session.get("https://api.jikan.moe/v4/characters")
    data = await res.json()
    return int(data["pagination"]["items"]["total"])


async def get_character_data_from_jikan(
    character_number: int,
) -> dict[str, str | None | BytesIO] | None:
    """
    :param character_number: The id of character
    :param session: `aiohttp.Client` instance to get data
    """
    res = await httpx.get(f"https://api.jikan.moe/v4/characters/{character_number}")
    data = await res.json()

    returnable_data = {}

    if res.status == 200 and str(data.get("status", None)) not in [
        "404",
        "408",
        "429",
        "500",
    ]:
        SUCCESS_LIST.append("JIKAN")

        data = data["data"]

        # Try to get webp image first
        # If that fails get jpg image
        try:
            image_url = data["images"]["webp"]["image_url"]
        except KeyError:
            image_url = data["images"]["jpg"]["image_url"]
        finally:
            image = await httpx.get(image_url)

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
) -> None:
    global EXECUTION_TIME

    while starting_number <= ending_number:
        start_time = datetime.now()

        # Actual work is being done here
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

        # Profile Execution of this function
        end_time = datetime.now()
        EXECUTION_TIME += (end_time - start_time).total_seconds()

        message = (
            f"[{round(EXECUTION_TIME, 2)}]"
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
        }

        # Log the data to a `.lock` file
        json.dump(
            log_dictionary,
            open(CHARACTER_LOCK_FILE_NAME, "w", encoding="utf-8"),
            indent=2,
        )

        click.secho(message)
