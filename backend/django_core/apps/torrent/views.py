from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from django.utils.timezone import now
from django.conf import settings
from .models import Torrent, Peer
from .serializers import AnnounceRequestSerializer, PeerSerializer, TorrentSerializer
from django.shortcuts import get_object_or_404
import bencodepy
import hashlib
from datetime import timedelta
from http import HTTPStatus
from django.http import HttpRequest
from urllib.parse import unquote_to_bytes


class AnnounceView(APIView):
    def get(self, request: HttpRequest):
        data = {
            "info_hash": unquote_to_bytes(request.query_params.get("info_hash")).hex(),
            "port": request.query_params["port"],
        }
        print(data)
        # Validate request data
        serializer = AnnounceRequestSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        info_hash = serializer.validated_data["info_hash"]
        peer_port = serializer.validated_data["port"]
        peer_ip = request.META.get("REMOTE_ADDR")
        print(serializer.validated_data)
        torrent = get_object_or_404(Torrent, info_hash=info_hash)

        # Update or create peer
        Peer.objects.update_or_create(
            ip=peer_ip,
            port=peer_port,
            torrent=torrent,
            defaults={"updated_at": now()},
        )

        # Remove stale peers
        timeout = now() - timedelta(minutes=settings.TORRENT_TIMEOUT)
        torrent.peers.filter(updated_at__lt=timeout).delete()

        # Serialize peers
        instances = torrent.peers.all()
        serializer = PeerSerializer(instances, many=True)

        return Response({"peers": serializer.data})


class TorrentView(APIView):
    parser_classes = [MultiPartParser, FormParser]  # Handle file upload

    def get(self, request):
        torrents = Torrent.objects.all()
        serializer = TorrentSerializer(torrents, many=True)
        return Response(serializer.data)

    def post(self, request):
        # Ensure file is present
        torrent_file = request.FILES.get("torrent_file")
        if not torrent_file:
            return Response(
                {"error": "No .torrent file provided."}, status=HTTPStatus.BAD_REQUEST
            )

        # Parse the .torrent file
        try:
            torrent_data = bencodepy.decode(torrent_file.read())
        except Exception as e:
            return Response(
                {"error": f"Failed to parse .torrent file: {str(e)}"},
                status=HTTPStatus.BAD_REQUEST,
            )

        torrent_info = torrent_data[b"info"]
        # Extract info_hash and name from the torrent data
        info_hash = hashlib.sha1(bencodepy.encode(torrent_info)).hexdigest()
        name = torrent_info.get(b"name", b"Unknown").decode()

        # Check if torrent already exists
        torrent, created = Torrent.objects.get_or_create(
            info_hash=info_hash,
            defaults={"name": name},
        )

        magnet_uri = f"magnet:?xt=urn:btih:{info_hash}&dn={name}"
        return Response({"id": torrent.id, "created": created, "magneturi": magnet_uri})
