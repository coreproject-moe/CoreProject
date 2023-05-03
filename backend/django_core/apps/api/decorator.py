import sys
from functools import wraps


def recursionlimit(limit):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            old_limit = sys.getrecursionlimit()
            sys.setrecursionlimit(limit)
            try:
                result = func(*args, **kwargs)
            finally:
                sys.setrecursionlimit(old_limit)
            return result

        return wrapper

    return decorator
