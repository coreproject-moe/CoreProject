import httpx
from selectolax.parser import HTMLParser
from typing import Literal
import re


class SitemapBuilder:
    def __init__(self, url: str) -> None:
        self.url = url

    @staticmethod
    def get_parser(xml: str) -> HTMLParser:
        return HTMLParser(xml)

    @staticmethod
    def get_content_given_url(url: str) -> str:
        return httpx.get(url).content

    @staticmethod
    def contains_integer(string):
        pattern = re.compile(r"\d+")
        return bool(re.search(pattern, string))

    def get_links_from_sitemap(self, url: str) -> list[str]:
        sitemap_content = self.get_content_given_url(url)
        sitemap_parser = self.get_parser(sitemap_content)

        loc_nodes = sitemap_parser.select("loc").matches
        links = [node.text() for node in loc_nodes]
        return links

    def build(
        self,
        filter: Literal["character"]
        | Literal["anime"]
        | Literal["manga"]
        | Literal["people"]
        | Literal["news"]
        | Literal["featured"]
        | Literal["mangastore"],
        return_only_ids=True,
    ):
        index_sitemap_links = self.get_links_from_sitemap(self.url)
        index_sitemap_links = [url for url in index_sitemap_links if f"{filter}-" in url]

        sitemap_link_buffer = []
        for sitemap in index_sitemap_links:
            individual_sitemap_link = self.get_links_from_sitemap(sitemap)
            if return_only_ids:
                for item in individual_sitemap_link:
                    if self.contains_integer(item):
                        sitemap_link_buffer.append(item)
            else:
                sitemap_link_buffer.extend(individual_sitemap_link)

        return sitemap_link_buffer
