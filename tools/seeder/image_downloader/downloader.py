from bing_image_downloader import downloader


def image_downloader(term: str, output_dir: str = "images"):
    return downloader.download(
        term,
        limit=1,
        output_dir=output_dir,
        adult_filter_off=True,
        force_replace=False,
        timeout=60,
        verbose=True,
    )


# usage
image_downloader("boku no pico 2")
# will be saved in images/{term}/Image_1.jpg
