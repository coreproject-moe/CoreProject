from requests import Session
from requests.structures import CaseInsensitiveDict
from requests.utils import default_headers
from requests_cache import CacheMixin
from requests_ratelimiter import LimiterMixin


class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    """
    Session class with caching and rate-limiting behavior.
        Accepts arguments for both LimiterSession and CachedSession.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.headers = self.default_headers()

    def default_headers(self) -> CaseInsensitiveDict[str]:
        """Remove user agent | Why does requests do this?"""
        previous_dict = default_headers()
        del previous_dict["User-Agent"]
        return previous_dict
