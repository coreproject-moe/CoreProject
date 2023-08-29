from apps.characters.models import CharacterModel
from rest_framework import serializers


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharacterModel
        fields = [
            "mal_id",
            "kitsu_id",
            "anilist_id",
            "name",
            "name_kanji",
            "character_image",
            "about",
        ]
