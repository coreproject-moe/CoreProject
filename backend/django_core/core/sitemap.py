from django.contrib.sitemaps import Sitemap
from apps.anime.models import AnimeModel


class AnimeSitemap(Sitemap):
    priority = 0.5

    def items(self):
        return AnimeModel.objects.all().order_by("-id")

    def location(self, obj: AnimeModel) -> str:
        return f"/anime/{obj.pk}"

    def lastmod(self, obj: AnimeModel):
        return obj.updated
