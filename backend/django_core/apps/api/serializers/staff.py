from apps.staffs.models import StaffAlternateNameModel, StaffModel
from rest_framework import serializers


class StaffSerializer(serializers.ModelSerializer):
    alternate_names = serializers.SlugRelatedField(
        many=True,
        read_only=False,
        queryset=StaffAlternateNameModel.objects.all(),
        slug_field="name",
    )

    class Meta:
        model = StaffModel
        fields = "__all__"

    def create(self, validated_data):
        alternate_names_data = validated_data.pop("alternate_names")
        instance: StaffModel = super().create(validated_data)
        instance.alternate_names.set(alternate_names_data)
        return instance

    def update(self, instance, validated_data):
        alternate_names_data = validated_data.pop("alternate_names", None)
        instance: StaffModel = super().update(instance, validated_data)
        if alternate_names_data is not None:
            instance.alternate_names.set(alternate_names_data)
        return instance
