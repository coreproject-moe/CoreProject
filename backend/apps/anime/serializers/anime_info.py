from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from ..models import AnimeGenreModel, AnimeInfoModel, AnimeSynonymModel


class AnimeInfoGenericSerializer(serializers.Serializer):
    mal_id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=True)
    type = serializers.CharField(required=False)


class AnimeInfoSerializer(serializers.ModelSerializer):
    # Everything is generic
    anime_genres = AnimeInfoGenericSerializer(many=True, required=False)
    anime_name_synonyms = AnimeInfoGenericSerializer(many=True, required=False)

    anime_studios = serializers.HyperlinkedIdentityField(
        view_name="animestudiomodel-list", lookup_url_kwarg="anime_id"
    )

    class Meta:
        model = AnimeInfoModel
        exclude = (
            "anime_themes",
            "anime_producers",
            "anime_recommendation",
            "anime_episodes",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # https://stackoverflow.com/questions/38316321/change-a-field-in-a-django-rest-framework-modelserializer-based-on-the-request-t
        request = self.context.get("request")

        if request and request.method in ["GET"]:
            self.fields["anime_name_synonyms"] = serializers.StringRelatedField(
                many=True
            )

    def get_anime_episodes(self, instance):
        return instance.anime_episodes.all().count()

    def create(self, validated_data):
        """https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers"""
        validated_data.pop("anime_episodes", None)  # ignore
        genres = validated_data.pop("anime_genres", None)
        synonyms = validated_data.pop("anime_name_synonyms", None)

        anime = AnimeInfoModel.objects.create(**validated_data)

        if genres:
            items = []
            for item in genres:
                anime_genre_model, _ = AnimeGenreModel.objects.get_or_create(
                    mal_id=item["mal_id"],
                    defaults={
                        "name": item["name"],
                        "type": item["type"],
                    },
                )
                items.append(anime_genre_model)

            anime.anime_genres.set(items) if items else None

        if synonyms:
            items = []
            for item in synonyms:
                anime_synonym_model, _ = AnimeSynonymModel.objects.get_or_create(
                    name=item["name"]
                )
                items.append(anime_synonym_model)

            anime.anime_name_synonyms.set(items) if items else None

        return anime

    def update(self, instance: AnimeInfoModel, validated_data):
        validated_data.pop("anime_episodes", None)  # ignore

        genres = validated_data.pop("anime_genres", None)
        synonyms = validated_data.pop("anime_name_synonyms", None)

        if genres:
            for item in genres:
                anime_genre_model, created = AnimeGenreModel.objects.get_or_create(
                    mal_id=item["mal_id"],
                    defaults={
                        "name": item["name"],
                        "type": item["type"],
                    },
                )
                if created:
                    instance.anime_genres.add(anime_genre_model)

        if synonyms:
            for item in synonyms:
                anime_synonym_model, created = AnimeSynonymModel.objects.get_or_create(
                    name=item.name
                )

                if created:
                    instance.anime_name_synonyms.add(anime_synonym_model)

        # https://stackoverflow.com/questions/53779723/django-rest-framework-update-with-kwargs-from-validated-data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
