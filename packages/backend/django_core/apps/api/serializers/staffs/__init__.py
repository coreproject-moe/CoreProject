from apps.api.bases.serializer import GetOrCreateSlugRelatedField
from apps.staffs.models import StaffAlternateNameModel, StaffModel
from rest_framework import serializers


class StaffSerializer(serializers.ModelSerializer):
    alternate_names = GetOrCreateSlugRelatedField(
        many=True,
        slug_field="name",
        required=False,
        queryset=StaffAlternateNameModel.objects.all(),
    )

    class Meta:
        model = StaffModel
        fields = [
            "mal_id",
            "kitsu_id",
            "anilist_id",
            "name",
            "given_name",
            "family_name",
            "alternate_names",
            "staff_image",
            "about",
        ]
