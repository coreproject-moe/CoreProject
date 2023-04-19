from parser.producer import ProducerParser
import httpx

res = httpx.get("https://myanimelist.net/anime/producer/1")

x = ProducerParser(res.text)

print(x.build_dictionary())
{
    "mal_id": "1",
    "name": "Pierrot",
    "japanese_title": "ぴえろ",
    "established": datetime.datetime(1979, 5, 19, 0, 0),
    "about": "Pierrot ぴえろ (Pierrot Co., Ltd.) is a Japanese animation studio established in May 1979 by former employees of both Tatsunoko Production and Mushi Production. Its headquarters are located in Mitaka, Tokyo. Pierrot is renowned for several worldwide popular anime series, such as Naruto, Bleach, Yu Yu Hakusho, Black Clover, Boruto: Naruto Next Generations, Tokyo Ghoul, and Great Teacher Onizuka.",
}
