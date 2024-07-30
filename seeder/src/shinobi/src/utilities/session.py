import os
from typing import Any

from redis import ConnectionPool
from requests import Session
from requests.adapters import HTTPAdapter
from requests.structures import CaseInsensitiveDict
from requests.utils import DEFAULT_ACCEPT_ENCODING
from requests_cache import RedisCache
from requests_ratelimiter import LimiterMixin, RedisBucket
from urllib3.util import Retry


class CachedLimiterSession(LimiterMixin, Session):
    """
    Session class with caching and rate-limiting behavior.
        Accepts arguments for both LimiterSession and CachedSession.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.headers = self.default_headers()

    def default_headers(self) -> CaseInsensitiveDict[str | bytes]:
        """
        :rtype: requests.structures.CaseInsensitiveDict
        """
        return CaseInsensitiveDict(
            {
                "User-Agent": "CoreProject",
                "Accept-Encoding": DEFAULT_ACCEPT_ENCODING,
                "Accept": "*/*",
                "Connection": "keep-alive",
            }
        )


CACHE_NAME = "seeder"
RETRY_STATUSES = [403]

retry_strategy = Retry(
    total=15,
    backoff_factor=2,
    status_forcelist=RETRY_STATUSES,
)
adapter = HTTPAdapter(max_retries=retry_strategy)
redis_pool = ConnectionPool.from_url(os.environ.get("REDIS_URL", "redis://localhost:6379"))

session = CachedLimiterSession(
    bucket_class=RedisBucket,
    backend=RedisCache(),
    # Undocumented ( pyrate-limiter )
    bucket_kwargs={
        "redis_pool": redis_pool,
        "bucket_name": CACHE_NAME,
        "expire_time": 30,
    },
    # https://docs.api.jikan.moe/#section/Information/Rate-Limiting
    per_minute=100,
    # per_second=1,
    per_host=True,
    # https://requests-cache.readthedocs.io/en/stable/user_guide/expiration.html
    expire_after=360,
)
session.mount("http://", adapter)
session.mount("https://", adapter)
