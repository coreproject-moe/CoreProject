from typing import Any, Callable, Optional, Literal
import functools


def return_specified_type_on_catched_error(
    return_type: Literal["str"] | Literal["list"],
) -> Callable[..., Any]:
    def decorator(func: Callable[..., Any]) -> Callable[..., Optional[Any]]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Optional[Any]:
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
