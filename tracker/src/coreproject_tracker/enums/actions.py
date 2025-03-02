import enum

__all__ = ["ACTIONS"]


class ACTIONS(enum.IntEnum):
    CONNECT = 0
    ANNOUNCE = 1
    SCRAPE = 2
    ERROR = 3
