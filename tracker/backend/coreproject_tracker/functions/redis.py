import json
import time

from quart import json as quart_json

from coreproject_tracker.constants import HASH_EXPIRE_TIME
from coreproject_tracker.singletons import get_redis
from coreproject_tracker.enums import REDIS_NAMESPACE_ENUM


def _ns_key(namespace: REDIS_NAMESPACE_ENUM, key: str) -> str:
    return f"{namespace.value}:{key}"


async def hset(
    hash_key: str,
    field: str,
    value: str,
    expire_time: int,
    namespace: REDIS_NAMESPACE_ENUM,
) -> None:
    r = get_redis()
    namespaced_key = _ns_key(namespace, hash_key)

    expiration = int(time.time() + expire_time)
    await r.hset(namespaced_key, field, value)  # type: ignore[no-untyped-call]
    await r.hexpireat(namespaced_key, expiration, field)
    await r.expire(namespaced_key, HASH_EXPIRE_TIME)


async def hget(
    hash_key: str,
    namespace: REDIS_NAMESPACE_ENUM,
) -> None | dict[str, str]:
    r = get_redis()
    namespaced_key = _ns_key(namespace, hash_key)

    data = await r.hgetall(namespaced_key)  # type: ignore[no-untyped-call]
    if not data:
        return None

    await r.expire(namespaced_key, HASH_EXPIRE_TIME)

    valid_fields = {}
    for field, value in data.items():
        try:
            decoded = quart_json.loads(value)
        except json.JSONDecodeError:
            continue

        if isinstance(decoded, dict):
            valid_fields[field] = value

    return valid_fields


async def hdel(
    hash_key: str,
    field_name: str,
    namespace: REDIS_NAMESPACE_ENUM,
) -> None:
    r = get_redis()
    namespaced_key = _ns_key(namespace, hash_key)

    await r.hdel(namespaced_key, field_name)  # type: ignore[no-untyped-call]


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
