from builder.sitemap import SitemapBuilder


x = SitemapBuilder("https://myanimelist.net/sitemap/index.xml").build(filter="anime")
with open("test.txt", "w") as f:
    f.write(str(x))
