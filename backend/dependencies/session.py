from collections.abc import AsyncGenerator

import aiohttp
from aiohttp_client_cache.backends.redis import RedisBackend
from aiohttp_client_cache.session import CachedSession

import settings.settings as settings

client_session: aiohttp.ClientSession = CachedSession(  # aiohttp-client-cache
    cache=RedisBackend(
        expire_after=settings.CACHE_MIDDLEWARE_SECONDS,
    )
)


async def get_session() -> AsyncGenerator[aiohttp.ClientSession, None]:
    try:
        yield client_session

    finally:
        await client_session.close()
