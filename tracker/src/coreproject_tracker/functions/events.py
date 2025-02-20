from coreproject_tracker.enums import EVENT_NAMES


def convert_event_id_to_event_enum(event_id: int) -> EVENT_NAMES:
    match event_id:
        case 0:
            return EVENT_NAMES.UPDATE
        case 1:
            return EVENT_NAMES.COMPLETE
        case 2:
            return EVENT_NAMES.START
        case 3:
            return EVENT_NAMES.STOP
        case 4:
            return EVENT_NAMES.PAUSE
        case _:
            raise ValueError("`event_id` is not supported")


def convert_event_name_to_event_enum(event_name: str) -> EVENT_NAMES:
    match event_name.lower():
        case "update":
            return EVENT_NAMES.UPDATE
        case "completed":
            return EVENT_NAMES.COMPLETE
        case "started":
            return EVENT_NAMES.START
        case "stopped":
            return EVENT_NAMES.STOP
        case "paused":
            return EVENT_NAMES.PAUSE
        case _:
            raise ValueError("`event_name` not supported")
