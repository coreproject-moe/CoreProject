from apps.staffs.models import StaffModel, StaffAlternateNameModel
from rest_framework import serializers


class StaffAlternateNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffAlternateNameModel
        fields = "__all__"


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaffModel
        fields = "__all__"
