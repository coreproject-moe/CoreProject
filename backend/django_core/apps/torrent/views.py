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
from .helper import get_params
import urllib.parse


class AnnounceView(APIView):
    def get(self, request: HttpRequest):
        params = get_params(request)  # what a shitty way to do things
        data = {
            "info_hash": urllib.parse.unquote_to_bytes(params["info_hash"]).hex(),
            "port": params["port"],
        }

        # Validate request data
        serializer = AnnounceRequestSerializer(data=data)
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
        timeout = now() - timedelta(minutes=settings.TORRENT_TIMEOUT)
        torrent.peers.filter(updated_at__lt=timeout).delete()

        # Serialize peers
        instances = torrent.peers.all()
        serializer = PeerSerializer(instances, many=True)

        output_data = bencodepy.bencode({"peers": serializer.data})
        return Response(output_data)


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

        # Parse the .torrent file using bencode.py
        try:
            torrent_data = bencodepy.decode(torrent_file.read())
        except Exception as e:
            return Response(
                {"error": f"Failed to parse .torrent file: {str(e)}"},
                status=HTTPStatus.BAD_REQUEST,
            )

        # Extract 'info' dictionary from the bencoded torrent data
        torrent_info = torrent_data[b"info"]

        # Extract info_hash and name from the torrent data
        info_hash = hashlib.sha1(bencodepy.encode(torrent_info)).hexdigest()
        name = torrent_info.get(b"name", b"Unknown").decode()

        # Check if torrent already exists, if not create it
        torrent, created = Torrent.objects.get_or_create(
            info_hash=info_hash,
            defaults={"name": name},
        )

        # Create magnet URI
        magnet_uri = f"magnet:?xt=urn:btih:{info_hash}&dn={name}"

        return Response({"id": torrent.id, "created": created, "magneturi": magnet_uri})
