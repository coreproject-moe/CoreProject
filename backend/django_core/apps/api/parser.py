from ninja.parser import Parser
from ninja.types import DictStrAny

from django.http import HttpRequest

try:
    import orjson

    HAS_ORJSON = True
except ImportError:
    HAS_ORJSON = False


class CustomParser(Parser):
    def __init__(self) -> None:
        # Override method only if `orjson`` exists
        if HAS_ORJSON:
            self.parse_body = self._parse_body

    def _parse_body(self, request: HttpRequest) -> DictStrAny:
        return orjson.loads(request.body)
