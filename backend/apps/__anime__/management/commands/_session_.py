from requests.adapters import HTTPAdapter
from requests_cache import RedisCache
from requests_ratelimiter import RedisBucket
from urllib3.util import Retry

from core.requests import CachedLimiterSession

retry_strategy = Retry(
    total=3,
    status_forcelist=[408, 429, 500, 502, 503, 504],
)


SESSION = CachedLimiterSession(
    bucket_class=RedisBucket,
    # Undocumented
    bucket_kwargs={"bucket_name": "_populate_"},
    backend=RedisCache(),
    # https://docs.api.jikan.moe/#section/Information/Rate-Limiting
    per_minute=60,
    per_second=1,
    # https://requests-cache.readthedocs.io/en/stable/user_guide/expiration.html
    expire_after=360,
)

adapter = HTTPAdapter(max_retries=retry_strategy)
SESSION.mount("https://", adapter)
SESSION.mount("http://", adapter)
