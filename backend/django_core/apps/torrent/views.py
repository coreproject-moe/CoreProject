from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.utils.timezone import now
from datetime import timedelta

from .models import Torrent, Peer
from .serializers import AnnounceRequestSerializer, PeerSerializer, TorrentSerializer


class AnnounceView(APIView):
    def get(self, request):
        # Validate request data
        serializer = AnnounceRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        info_hash = serializer.validated_data["info_hash"]
        peer_port = serializer.validated_data["port"]
        peer_ip = request.META.get("REMOTE_ADDR")

        try:
            torrent = Torrent.objects.get(info_hash=info_hash)
        except Torrent.DoesNotExist:
            raise NotFound({"error": "Torrent not found"})

        # Update or create peer
        Peer.objects.update_or_create(
            ip=peer_ip,
            port=peer_port,
            torrent=torrent,
            defaults={"last_seen": now()},
        )

        # Remove stale peers
        timeout = now() - timedelta(minutes=30)
        torrent.peers.filter(last_seen__lt=timeout).delete()

        # Serialize peers
        peers = torrent.peers.all()
        peers_data = PeerSerializer(peers, many=True).data

        return Response({"peers": peers_data})


class TorrentView(APIView):
    def get(self, request):
        torrents = Torrent.objects.all()
        serializer = TorrentSerializer(torrents, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TorrentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        torrent, created = Torrent.objects.get_or_create(
            info_hash=serializer.validated_data["info_hash"],
            defaults={"name": serializer.validated_data["name"]},
        )

        return Response({"id": torrent.id, "created": created})
