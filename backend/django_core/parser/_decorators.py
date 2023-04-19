from typing import Any, Literal
from collections.abc import Callable
import functools

# These decorators catch :
#   AttributeError : In case `selectolax` fails to find the dom node
#   IndexError : In case `selectolax` finds empty dom node


def return_specified_type_on_catched_error(
    return_type: Literal["str"] | Literal["list"],
) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Any | None]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any | None:
            try:
                return func(*args, **kwargs)

            except (AttributeError, IndexError):
                if return_type == "str":
                    return ""
                elif return_type == "list":
                    return []
                else:
                    return None

        return wrapper

    return decorator
