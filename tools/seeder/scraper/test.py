from pprint import pprint
from scrapers import AnimeScraper


anime_scraper = AnimeScraper(query="death note")
anime_info = anime_scraper.get_anime_info()
pprint(anime_info)
