from enum import Enum, auto


class EVENT_NAMES(Enum):
    UPDATE = auto()
    COMPLETE = auto()
    START = auto()
    STOP = auto()
    PAUSE = auto()
