from typing import Optional

from redis import Redis

from coreproject_tracker.constants import REDIS_HOST, REDIS_PORT


class RedisConnectionManager:
    _instance: Optional["RedisConnectionManager"] = None
    _redis_client: Redis | None = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RedisConnectionManager, cls).__new__(cls)
        return cls._instance

    @classmethod
    def initialize(cls):
        """Initialize the Redis connection if it doesn't exist"""
        from coreproject_tracker.functions import compare_versions

        if cls._redis_client is None:
            client = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
            redis_version = client.info().get("redis_version")
            if compare_versions("7.4.2", redis_version) == -1:
                raise RuntimeError("Redis needs to be at least 7.4.2")

            cls._redis_client = client

    @classmethod
    def get_client(cls) -> Redis:
        """Get the Redis client instance"""

        if cls._redis_client is None:
            raise RuntimeError("Redis client not initialized. Call initialize() first")
        return cls._redis_client

    @classmethod
    async def cleanup(cls):
        """Cleanup the Redis connection"""
        if cls._redis_client is not None:
            await cls._redis_client.close()
            cls._redis_client = None
