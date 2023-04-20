from parser.sitemap import SitemapParser
import httpx


res = httpx.get("https://myanimelist.net/anime.php")


print(SitemapParser(res.content).genres())
