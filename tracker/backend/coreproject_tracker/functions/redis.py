import json
import time
from typing import Iterable

from quart import json as quart_json

from coreproject_tracker.constants import HASH_EXPIRE_TIME
from coreproject_tracker.singletons import get_redis


async def hset(hash_key: str, field: str, value: str, expire_time: int) -> None:
    r = get_redis()

    expiration = int(time.time() + expire_time)
    await r.hset(hash_key, field, value)  #  type: ignore[no-untyped-call]

    await r.hexpireat(hash_key, expiration, field)
    await r.expire(hash_key, HASH_EXPIRE_TIME)


async def hget(
    hash_key: str, peer_type: str | Iterable[str] | None = None
) -> None | dict[str, str]:
    r = get_redis()

    # Retrieve all fields and their values from the hash
    data = await r.hgetall(hash_key)  # type: ignore[no-untyped-call]
    if not data:
        return None

    # Update the TTL
    await r.expire(hash_key, HASH_EXPIRE_TIME)

    valid_fields = {}

    # Normalize peer_type into a set for fast lookup (if not None)
    if peer_type is not None:
        if isinstance(peer_type, str):
            peer_type = {peer_type}
        else:
            peer_type = set(peer_type)

    for field, value in data.items():
        try:
            decoded = quart_json.loads(value)
        except json.JSONDecodeError:
            continue

        if not isinstance(decoded, dict):
            continue

        if peer_type is None or decoded.get("type") in peer_type:
            valid_fields[field] = value

    return valid_fields


async def hdel(hash_key, field_name) -> None:
    r = get_redis()

    await r.hdel(hash_key, field_name)  # type: ignore[no-untyped-call]


async def get_all_hash_keys():
    r = get_redis()

    cursor = 0
    hash_keys = []

    while True:
        cursor, keys = await r.scan(cursor, match="*", count=100_000)
        for key in keys:
            if await r.type(key) == b"hash":
                hash_keys.append(key)
        if cursor == 0:
            break

    return hash_keys
