from django.contrib import admin
from django.db.models.query import QuerySet
from django.http import HttpRequest

from ..models.episode_comment import EpisodeCommentModel

# Register your models here.


@admin.register(EpisodeCommentModel)
class EpisodeCommentAdmin(admin.ModelAdmin[EpisodeCommentModel]):
    autocomplete_fields = ["user"]
    list_filters = ["user"]
    search_fields = ["user__username", "text"]

    def get_search_results(
        self,
        request: HttpRequest,
        queryset: QuerySet[EpisodeCommentModel],
        search_term: str,
    ) -> tuple[QuerySet[EpisodeCommentModel], bool]:
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )
        if "#" in search_term:
            queryset = (
                self.model.objects.get_username_with_discriminator(prefix="user")
                .filter(
                    username_with_discriminator__in=[
                        # Remove trailing whitespace
                        # We might have something like
                        # user = ['baseplate-admin ', ' baseplate-foot']
                        # make it
                        # user = ['baseplate-admin','baseplate-foot']
                        item.strip()
                        for item in search_term.split(",")
                    ]
                )
                .distinct()
            )

        return queryset, may_have_duplicates
