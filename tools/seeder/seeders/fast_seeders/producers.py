# from itertools import count
import httpx
import utils
import asyncio
import dotenv
import os

dotenv.load_dotenv()
AUTHBEARER = os.getenv("AUTHBEARER")
BASE_URL = "https://backend.coreproject.moe/api/v1"


async def post_producer_or_studio(api: str, data: dict):
    try:
        headers = {
            "authorization": f"Bearer {AUTHBEARER}",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(api, json=data, headers=headers)
            response.raise_for_status()
            print("OK:", response.status_code)
            return True
    except Exception:
        print("Failed:", response.status_code)
        return False


async def batch_poster(api: str, datas: list):
    await asyncio.gather(
        *[asyncio.create_task(post_producer_or_studio(api, data)) for data in datas]
    )


async def batch_producer_studio_poster():
    async with httpx.AsyncClient() as client:
        for page in range(1, 999):
            print("Page:", page)
            url = f"https://api.jikan.moe/v4/producers?page={page}"
            response = await client.get(url)
            producers: list[dict] = response.json()["data"]
            if not producers:
                break
            producers_data = []
            for producer in producers:
                titles = producer.get("titles", [])
                title = titles[0]["title"] if titles else ""
                japanese_title = titles[1]["title"] if len(titles) > 1 else ""
                data = {
                    "mal_id": producer["mal_id"],
                    "name": title,
                    "default_title": title,
                    "japanese_title": japanese_title,
                    "established": utils.date_converter(producer["established"]),
                    "about": producer["about"],
                }
                data = utils.dictionary_filter(data)
                producers_data.append(data)
            await batch_poster(f"{BASE_URL}/producers", producers_data)
    # print(f"Pass: {pass_count}")
    # print(f"Fail: {fail_count}")


if __name__ == "__main__":
    asyncio.run(batch_producer_studio_poster())
