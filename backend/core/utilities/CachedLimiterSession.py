from typing import Any

from requests import Session
from requests.structures import CaseInsensitiveDict
from requests.utils import DEFAULT_ACCEPT_ENCODING
from requests_cache import CacheMixin
from requests_ratelimiter import LimiterMixin


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
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
                "Accept-Encoding": DEFAULT_ACCEPT_ENCODING,
                "Accept": "*/*",
                "Connection": "keep-alive",
            }
        )
