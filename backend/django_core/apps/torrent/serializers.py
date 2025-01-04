from rest_framework import serializers


class PeerSerializer(serializers.Serializer):
    ip = serializers.IPAddressField()
    port = serializers.IntegerField()


class AnnounceRequestSerializer(serializers.Serializer):
    info_hash = serializers.CharField()
    port = serializers.IntegerField()


class TorrentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    info_hash = serializers.CharField(max_length=40)
