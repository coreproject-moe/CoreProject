from rest_framework import serializers
from .models import Peer


class PeerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Peer
        fields = ["ip", "port", "peer_id", "torrent", "is_seeding", "updated_at"]

    def validate_peer_id(self, value):
        """
        Validate that peer_id is exactly 20 characters (standard for BitTorrent).
        """
        if len(value) != 20:
            raise serializers.ValidationError("Peer ID must be exactly 20 characters.")
        return value

    def validate_port(self, value):
        """
        Validate that port is within the valid range (1-65535).
        """
        if not (1 <= value <= 65535):
            raise serializers.ValidationError("Port must be between 1 and 65535.")
        return value


class AnnounceRequestSerializer(serializers.Serializer):
    info_hash = serializers.CharField()
    port = serializers.IntegerField(min_value=0, max_value=65535)
    peer_id = serializers.CharField()
    left = serializers.IntegerField()
    peer_ip = serializers.IPAddressField()


class TorrentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    info_hash = serializers.CharField(max_length=40)
