from collections.abc import Callable
import functools
from typing import Any, Literal

# These decorators catch :
#   AttributeError : In case `selectolax` fails to find the dom node
#   IndexError : In case `selectolax` finds empty dom node


def return_on_error(
    return_type: Literal["[]"] | Literal[""],
) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any | None]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any | None:
            try:
                return func(*args, **kwargs)

            except (AttributeError, IndexError):
                return return_type

        return wrapper

    return decorator
