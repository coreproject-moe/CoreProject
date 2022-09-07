from argparse import ArgumentParser
from datetime import datetime, timedelta
import os
import textwrap
from threading import Thread
from typing import Any

from django.conf import settings
from django.contrib.humanize.templatetags.humanize import intcomma, naturaltime
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from django.db import IntegrityError
from requests.adapters import HTTPAdapter
from requests_cache import RedisCache  # type: ignore
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry

# pylint: disable=import-error
from apps.anime.models import CharacterModel
from core.utilities.CachedLimiterSession import CachedLimiterSession

retry_strategy = Retry(
    total=settings.MAX_RETRY,
    status_forcelist=settings.REQUEST_STATUS_CODES_TO_RETRY,
)
adapter = HTTPAdapter(max_retries=retry_strategy)


class Command(BaseCommand):
    """Populates the character database"""

    help = "Populates the character database"

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    def handle(self, *args: Any, **options: Any) -> None:
        """Starting point for our application"""
        self.character_number = options["character-number-start"]
        self.character_number_end = options["character_number_end"]
        self.stdout.write(
            textwrap.dedent(
                f"""

                Starting Number : {
                    self.style.SUCCESS(
                        str(
                            intcomma(
                                self.character_number
                            )
                        )
                    )
                }
                Total `characters` to get : {
                    self.style.SUCCESS(
                        str(
                            intcomma(
                                self.character_number_end
                            )
                        )
                    )
                }
                Time to finish : {
                    self.style.SUCCESS(
                        str(
                            naturaltime(
                                datetime.now()
                                +
                                timedelta(
                                    minutes=
                                        round(
                                            (
                                                self.character_number_end
                                                -
                                                self.character_number
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
        )


class MyAnimeList(Thread):
    def __init__(
        self,
        args: Any,
        kwargs: Any,
    ) -> None:
        super().__init__(args, kwargs)

    def run(self) -> None:
        return super().run()
