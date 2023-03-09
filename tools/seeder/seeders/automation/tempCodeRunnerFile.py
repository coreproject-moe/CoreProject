import json
import requests

url = "https://backend.coreproject.moe/api/v1/anime"
headers = {"accept": "application/json", "Authorization": "Bearer uBRFvhuEDUiuviXU"}
files = {
    "banner": open("image.webp", "rb"),
    "cover": open("image.webp", "rb"),
}
data = {
    "aired_from": "1998-04-03T00:00:00Z",
    "anilist_id": 1,
    "producers": [2, 3],
    "mal_id": 1,
    "kitsu_id": 1,
    "name_japanese": "fadsfasd",
    "themes": [1, 2],
    "name": "fdafsdfa",
    "name_synonyms": "baka,dasf",
    "genres": [1, 2],
    "aired_to": "1998-04-03T00:00:00Z",
    "synopsis": "dfadfadsfa",
    "source": "3dsffasfas",
    "studios": [1, 2],
    "rating": 11,
}
data = json.dumps(data)
print(data)
response = requests.post(url, headers=headers, files=files, data=data)
print(response.json())
