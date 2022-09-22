import djclick as click
import functools
import asyncio
import textwrap
from django.contrib.humanize.templatetags.humanize import intcomma, naturaltime
from django.conf import settings
from django.core.management.color import color_style
from datetime import timedelta, datetime

from aiohttp_client_cache.session import CachedSession
from aiohttp_client_cache.backends.redis import RedisBackend
from aiohttp_retry import RetryClient, ExponentialRetry
from pyrate_limiter import Limiter, RequestRate, Duration, RedisBucket


style = color_style()
CACHE_NAME = settings.BUCKET_NAME
RETRY_STATUSES = settings.REQUEST_STATUS_CODES_TO_RETRY
limiter = Limiter(
    RequestRate(1, Duration.SECOND),
    RequestRate(60, Duration.MINUTE),
    bucket_class=RedisBucket,
    bucket_kwargs={
        "bucket_name": CACHE_NAME,
    },
)


# https://github.com/pallets/click/issues/2033#issue-960810534
def make_sync(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))

    return wrapper


@click.command()
@make_sync
async def command() -> None:
    session = RetryClient(
        client_session=CachedSession(
            cache=RedisBackend(
                CACHE_NAME,
                allowed_methods=["GET"],  # Cache requests with these HTTP methods
            )
        ),
        retry_options=ExponentialRetry(
            attempts=10,
            max_timeout=100.00,
            statuses=set(RETRY_STATUSES),
        ),
    )

    ending_number: int = await get_ending_number(session)
    character_number = 0

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

    await session.close()


@limiter.ratelimit("ending", delay=True)
async def get_ending_number(session: CachedSession | RetryClient) -> int:
    res = await session.get("https://api.jikan.moe/v4/characters")
    data = await res.json()
    return int(data["pagination"]["items"]["total"])


@limiter.ratelimit("jikan", delay=True)
async def get_character_data_from_jikan(
    character_number: int,
    session: CachedSession | RetryClient,
) -> dict[str, str] | None:
    """
    :param character_number: The id of character
    :param session: Requests instance to get data
    """
    res = await session.get(f"https://api.jikan.moe/v4/characters/{character_number}")
    data = await res.json()
    returnable_data = None

    if res.status == 200 and str(data.get("status", None)) not in [
        "404",
        "408",
        "429",
    ]:
        ############################################################################################################
        success_list.append(style.SUCCESS("Jikan"))

        returnable_data = data["data"]
        self.character_name = returnable_data["name"]
        self.character_name_kanji = returnable_data.get("name_kanji", None)
        self.character_about = returnable_data.get("about", None)

        # Try to get webp image first
        # If that fails get jpg image
        try:
            self.image_url = returnable_data["images"]["webp"]["image_url"]
        except KeyError:
            self.image_url = returnable_data["images"]["jpg"]["image_url"]
        finally:
            image = self.session.get(self.image_url)
            self.character_image = BytesIO(image.content)

    elif data.get("status", None) == 408:
        self.warning_list.append(self.style.WARNING("Jikan"))

        # Write the number to a file so that we can deal with it later
        file = open(self.MAL_RATE_LIMIT_FILE_NAME, "a", encoding="utf-8")
        file.write(f"{str(character_number)}\n")
        file.close()

    else:
        self.error_list.append(self.style.ERROR("Jikan"))

    return returnable_data
