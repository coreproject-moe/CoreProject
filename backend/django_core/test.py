from builder.anime import AnimeBuilder


x = AnimeBuilder().build_urls()
with open("test.txt", "w") as f:
    f.write(str(x))
