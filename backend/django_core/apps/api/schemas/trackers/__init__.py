from typing import Literal

from ninja import Schema


class TrackerSchema(Schema):
    status: Literal[
        "watching",
        "completed",
        "on_hold",
        "dropped",
        "plan_to_watch",
    ]
    is_rewatching: bool
    score: int
    num_watched_episodes: int
    priority: int
    num_times_rewatched: int
    rewatch_value: int
    tags: str
    comments: str


class TrackerDeleteSchema(Schema):
    anime_id: int
