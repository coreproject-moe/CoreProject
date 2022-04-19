from rest_framework import serializers

from .episode import EpisodeSerializer
from ..models import (
    AnimeInfoModel,
    AnimeProducerModel,
    AnimeStudioModel,
    AnimeThemeModel,
    AnimeGenreModel,
    AnimeSynonymModel,
)


class AnimeGenericSerializer(serializers.Serializer):
    mal_id = serializers.IntegerField(required=False)
    name = serializers.CharField(required=True)
    type = serializers.CharField(required=False)


class AnimeInfoSerializer(serializers.ModelSerializer):
    anime_episodes = EpisodeSerializer(many=True, required=False)
    # Everything is generic
    anime_genres = AnimeGenericSerializer(many=True, required=False)
    anime_themes = AnimeGenericSerializer(many=True, required=False)
    anime_studios = AnimeGenericSerializer(many=True, required=False)
    anime_producers = AnimeGenericSerializer(many=True, required=False)
    anime_name_synonyms = AnimeGenericSerializer(many=True, required=False)

    class Meta:
        model = AnimeInfoModel
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # https://stackoverflow.com/questions/38316321/change-a-field-in-a-django-rest-framework-modelserializer-based-on-the-request-t
        if self.context["request"].method in ["GET"]:
            self.fields["anime_episodes"] = serializers.SerializerMethodField()
            self.fields["anime_name_synonyms"] = serializers.StringRelatedField(
                many=True
            )

    def get_anime_episodes(self, instance):
        return instance.anime_episodes.all().count()

    def create(self, validated_data):
        """https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers"""
        validated_data.pop("anime_episodes", None)  # ignore
        genres = validated_data.pop("anime_genres", None)
        themes = validated_data.pop("anime_themes", None)
        studios = validated_data.pop("anime_studios", None)
        producers = validated_data.pop("anime_producers", None)
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

        if themes:
            items = []
            for item in themes:
                anime_theme_model, _ = AnimeThemeModel.objects.get_or_create(
                    mal_id=item["mal_id"],
                    defaults={
                        "name": item["name"],
                        "type": item["type"],
                    },
                )
                items.append(anime_theme_model)

            anime.anime_themes.set(items) if items else None

        if studios:
            items = []
            for item in studios:
                anime_studio_model, _ = AnimeStudioModel.objects.get_or_create(
                    mal_id=item["mal_id"],
                    defaults={
                        "name": item["name"],
                        "type": item["type"],
                    },
                )
                items.append(anime_studio_model)

            anime.anime_studios.set(items) if items else None

        if producers:
            items = []
            for item in producers:
                anime_producer_model, _ = AnimeProducerModel.objects.get_or_create(
                    mal_id=item["mal_id"],
                    defaults={
                        "name": item["name"],
                        "type": item["type"],
                    },
                )
                items.append(anime_producer_model)

            anime.anime_producers.set(items) if items else None

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
        themes = validated_data.pop("anime_themes", None)
        studios = validated_data.pop("anime_studios", None)
        producers = validated_data.pop("anime_producers", None)
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
        if themes:
            for item in themes:
                anime_theme_model, created = AnimeThemeModel.objects.get_or_create(
                    mal_id=item["mal_id"],
                    defaults={
                        "name": item["name"],
                        "type": item["type"],
                    },
                )
                if created:
                    instance.anime_themes.add(anime_theme_model)

        if studios:
            for item in studios:
                anime_studio_model, created = AnimeStudioModel.objects.get_or_create(
                    mal_id=item["mal_id"],
                    defaults={
                        "name": item["name"],
                        "type": item["type"],
                    },
                )
                if created:
                    instance.anime_studios.add(anime_studio_model)

        if producers:
            for item in producers:
                (
                    anime_producer_model,
                    created,
                ) = AnimeProducerModel.objects.get_or_create(
                    mal_id=item["mal_id"],
                    defaults={
                        "name": item["name"],
                        "type": item["type"],
                    },
                )
                if created:
                    instance.anime_producers.add(anime_producer_model)
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
