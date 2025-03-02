from enum import Enum, auto

__all__ = ["EVENT_NAMES"]


class EVENT_NAMES(Enum):
    UPDATE = auto()
    COMPLETE = auto()
    START = auto()
    STOP = auto()
    PAUSE = auto()
