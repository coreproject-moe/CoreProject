from django.conf import settings
from django.contrib import admin
from django.db.models import CharField, Value
from django.db.models.functions import Cast, Concat, LPad

from ..models import EpisodeCommentModel

# Register your models here.


@admin.register(EpisodeCommentModel)
class EpisodeCommentAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user"]
    list_filters = ["user"]
    search_fields = ["user__username", "text"]

    def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request,
            queryset,
            search_term,
        )
        if "#" in search_term:
            queryset = (
                self.model.objects.annotate(
                    username_discriminator_as_string=Cast(
                        "user__username_discriminator", output_field=CharField()
                    ),
                    username_with_discriminator=Concat(
                        "user__username",
                        Value("#"),
                        LPad(
                            "username_discriminator_as_string",
                            int(settings.USERNAME_DISCRIMINATOR_LENGTH),
                            Value("0"),
                        ),
                        output_field=CharField(),
                    ),
                )
                .filter(username_with_discriminator__in=search_term.split(","))
                .distinct()
            )

        return queryset, may_have_duplicates
