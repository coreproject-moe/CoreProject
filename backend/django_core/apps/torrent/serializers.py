from rest_framework import serializers


class PeerSerializer(serializers.Serializer):
    ip = serializers.IPAddressField()
    port = serializers.IntegerField()


class AnnounceRequestSerializer(serializers.Serializer):
    info_hash = serializers.CharField(max_length=20)
    port = serializers.IntegerField(min_value=0, max_value=65535)
    peer_id = serializers.CharField()
    left = serializers.IntegerField()
    peer_ip = serializers.IPAddressField()


class TorrentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    info_hash = serializers.CharField(max_length=40)
