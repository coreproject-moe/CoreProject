from pprint import pprint
from scrapers import AnimeScraper


anime_scraper = AnimeScraper(mal_id=1)
anime_info = anime_scraper.get_anime_info()
pprint(anime_info)
