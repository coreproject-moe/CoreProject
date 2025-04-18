import time

from quart_redis import get_redis

from coreproject_tracker.constants import HASH_EXPIRE_TIME, PEER_TTL


async def hset(
    hash_key: str, field: str, value: str, expire_time: int = PEER_TTL
) -> None:
    r = get_redis()

    expiration = int(time.time() + expire_time)
    await r.hset(hash_key, field, value)

    await r.hexpireat(hash_key, expiration, field)
    await r.expire(hash_key, HASH_EXPIRE_TIME)


async def hget(hash_key: str) -> None | dict[str, str | int]:
    r = get_redis()

    # Retrieve all fields and their values from the hash
    data = await r.hgetall(hash_key)
    if not data:
        return None  # Return None if the hash doesn't exist or is empty

    # Update the ttl again
    await r.expire(hash_key, HASH_EXPIRE_TIME)
    valid_fields = {}

    # Iterate over each field-value pair in the hash
    for field, value in data.items():
        valid_fields[field] = value

    return valid_fields


async def hdel(hash_key, field_name) -> None:
    r = get_redis()

    await r.hdel(hash_key, field_name)


async def get_all_hash_keys():
    r = get_redis()

    cursor = "0"
    hash_keys = []

    while cursor != 0:
        cursor, keys = await r.scan(cursor, match="*", count=10000)  # Match all keys
        for key in keys:
            if await r.type(key) == b"hash":
                hash_keys.append(key)

    return hash_keys
