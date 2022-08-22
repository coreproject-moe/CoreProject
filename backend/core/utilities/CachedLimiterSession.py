from typing import TYPE_CHECKING
from requests import Session
from requests.structures import CaseInsensitiveDict
from requests.utils import default_headers
from requests_cache import CacheMixin
from requests_ratelimiter import LimiterMixin

if TYPE_CHECKING:
    from typing import Any


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    """
    Session class with caching and rate-limiting behavior.
        Accepts arguments for both LimiterSession and CachedSession.
    """

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.headers = self.default_headers()

    def default_headers(self) -> CaseInsensitiveDict[str | bytes]:
        """Remove user agent | Why does requests do this?"""
        previous_dict = default_headers()
        del previous_dict["User-Agent"]
        return CaseInsensitiveDict(previous_dict)
