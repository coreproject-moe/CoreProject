from django.contrib import admin

from ..models import EpisodeTimestampModel

# Register your models here.


@admin.register(EpisodeTimestampModel)
class EpisodeTimestampAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user", "episode"]
    list_filter = ["user", "episode"]
    search_fields = ["user__username"]

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )
        if "#" in search_term:
            queryset = (
                self.model.objects.get_username_with_discriminator(prefix="user")
                .filter(username_with_discriminator__in=search_term.strip().split(","))
                .distinct()
            )

        return queryset, may_have_duplicates
