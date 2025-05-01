from redis import asyncio as redis
import asyncio





async def main():
    print(await get_all_hash_keys())


asyncio.run(main())
