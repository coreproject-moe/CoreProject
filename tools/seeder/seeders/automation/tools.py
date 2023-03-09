from typing import Dict
from tqdm import tqdm
import requests
from datetime import datetime


def downloader(download_url: str, filename: str):
    with requests.get(download_url, stream=True) as response:
        total_size = int(response.headers.get("content-length", 0))
        block_size = 1024
        progress_bar = tqdm(total=total_size, unit="iB", unit_scale=True)
        with open(filename, "wb") as f:
            for chunk in response.iter_content(block_size):
                progress_bar.update(len(chunk))
                f.write(chunk)
        progress_bar.close()


def date_converter(date: str) -> str:
    dt = datetime.fromisoformat(date[:-6])
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def select_highest_resolutions(data: Dict[str, str]) -> str:
    preferred_resolutions = ["1080P", "720P", "480P", "360P"]
    for resolution in preferred_resolutions:
        for item in data:
            if resolution in item["name"].upper():
                print("Selected item:", item["name"])
                return item["link"]
