from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import timedelta
from django.conf import settings
from .models import Torrent, Peer
from .serializers import AnnounceRequestSerializer, PeerSerializer, TorrentSerializer
from django.shortcuts import get_object_or_404


class AnnounceView(APIView):
    def get(self, request):
        # Validate request data
        serializer = AnnounceRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        info_hash = serializer.validated_data["info_hash"]
        peer_port = serializer.validated_data["port"]
        peer_ip = request.META.get("REMOTE_ADDR")

        torrent = get_object_or_404(Torrent, info_hash=info_hash)

        # Update or create peer
        Peer.objects.update_or_create(
            ip=peer_ip,
            port=peer_port,
            torrent=torrent,
            defaults={"updated_at": now()},
        )

        # Remove stale peers
        # TODO: Might be better to offload to celery
        timeout = now() - timedelta(minutes=settings.TORRENT_TIMEOUT)
        torrent.peers.filter(updated_at__lt=timeout).delete()

        # Serialize peers
        instances = torrent.peers.all()
        serializer = PeerSerializer(instances, many=True)

        return Response({"peers": serializer.data})


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
