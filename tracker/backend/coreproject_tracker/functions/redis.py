import time

from quart_redis import get_redis

from coreproject_tracker.constants import HASH_EXPIRE_TIME


async def hset(hash_key: str, field: str, value: str, expire_time: int) -> None:
    r = get_redis()

    expiration = int(time.time() + expire_time)
    await r.hset(hash_key, field, value)  # type: ignore[no-untyped-call]

    await r.hexpireat(hash_key, expiration, field)
    await r.expire(hash_key, HASH_EXPIRE_TIME)


async def hget(hash_key: str) -> None | dict[str, str | int]:
    r = get_redis()

    # Retrieve all fields and their values from the hash
    data = await r.hgetall(hash_key)  # type: ignore[no-untyped-call]
    if not data:
        return None

    # Update the ttl again
    await r.expire(hash_key, HASH_EXPIRE_TIME)
    valid_fields = {}

    # Iterate over each field-value pair in the hash
    for field, value in data.items():
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
