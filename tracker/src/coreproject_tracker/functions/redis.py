import time

from coreproject_tracker.constants import (
    HASH_EXPIRE_TIME,
    PEER_TTL,
)
from coreproject_tracker.singletons import RedisConnectionManager


def hset(hash_key, field, value):
    r = RedisConnectionManager.get_client()

    expiration = int(time.time() + PEER_TTL)
    r.hset(hash_key, field, value)

    r.hexpireat(hash_key, expiration, field)
    r.expire(hash_key, HASH_EXPIRE_TIME)


def hget(hash_key):
    r = RedisConnectionManager.get_client()

    # Retrieve all fields and their values from the hash
    data = r.hgetall(hash_key)
    if not data:
        return None  # Return None if the hash doesn't exist or is empty

    # Update the ttl again
    r.expire(hash_key, HASH_EXPIRE_TIME)
    valid_fields = {}

    # Iterate over each field-value pair in the hash
    for field, value in data.items():
        valid_fields[field] = value

    return valid_fields


def hdel(hash_key, field_name):
    r = RedisConnectionManager.get_client()

    r.hdel(hash_key, field_name)
