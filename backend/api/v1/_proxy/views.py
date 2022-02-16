import httpx
from platform import python_version

from django.http import HttpResponse

# Master Header.
# Mimics Firefox.
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/jxl,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}


async def proxy_view(request, secret_id: str) -> HttpResponse:
    client = httpx.AsyncClient(http2=True, follow_redirects=True)

    url = f"https://docs.google.com/uc?export=download&id={secret_id}"
    res = await client.get(url)
    await client.aclose()
    
    return HttpResponse(
        await res.aread(),
        content_type="video/mp4",
        headers={
            "server": f"Python/{python_version()}",
        },
    )
