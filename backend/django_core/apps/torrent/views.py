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
from django.http import HttpRequest, HttpResponse
from .helper import get_params
import urllib.parse
from django.views.decorators.http import require_http_methods


@require_http_methods(["GET"])
def announce_view(request: HttpRequest) -> HttpResponse:
    params = get_params(request)  # What a shitty way to do things
    data = {
        "info_hash": urllib.parse.unquote_to_bytes(params["info_hash"]).hex(),
        "port": params["port"],
        "peer_id": params["peer_id"],
        "left": params["left"],
    }

    # Validate request data
    serializer = AnnounceRequestSerializer(data=data)
    if not serializer.is_valid():
        return HttpResponse(serializer.errors, status=HTTPStatus.BAD_REQUEST)

    peer_ip = request.META.get("REMOTE_ADDR")
    info_hash = serializer.validated_data["info_hash"]
    peer_port = serializer.validated_data["port"]
    peer_id = serializer.validated_data["peer_id"]
    left = serializer.validated_data["left"]

    if left == 0:
        is_seeding = True
    else:
        is_seeding = False

    # Fetch the torrent
    torrent = get_object_or_404(Torrent, info_hash=info_hash)

    # Update or create the peer
    Peer.objects.update_or_create(
        ip=peer_ip,
        port=peer_port,
        torrent=torrent,
        is_seeding=is_seeding,
        peer_id=peer_id,
        defaults={"updated_at": now()},
    )

    # Remove stale peers
    timeout = now() - timedelta(minutes=settings.TORRENT_TIMEOUT)
    torrent.peers.filter(updated_at__lt=timeout).delete()

    seeds = torrent.peers.filter(is_seeding=True)
    leeches = torrent.peers.filter(is_seeding=False)

    if numwant := params.get("numwant", None):
        peer_instances = torrent.peers.all()[: int(numwant)]
    else:
        peer_instances = torrent.peers.all()

    peer_serializer = PeerSerializer(peer_instances, many=True)

    if isinstance(peer_serializer.data, list):
        data_dict = [dict(item) for item in peer_serializer.data]
    else:
        data_dict = dict(peer_serializer.data)

    normal_output = {
        "peers": data_dict,
        "min interval": settings.TORRENT_TIMEOUT,
        "complete": len(seeds),
        "incomplete": len(leeches),
    }
    output_data = bencodepy.bencode(normal_output)
    return HttpResponse(output_data, content_type="text/plain")


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
                {
                    "error": f"Failed to parse .torrent file: {str(e)}",
                },
                status=HTTPStatus.BAD_REQUEST,
            )

        # Extract 'info' dictionary from the bencoded torrent data
        torrent_info = torrent_data[b"info"]

        # Extract info_hash and name from the torrent data
        info_hash = hashlib.sha1(bencodepy.bencode(torrent_info)).hexdigest()
        name = torrent_info.get(b"name", b"Unknown").decode()

        # Check if torrent already exists, if not create it
        torrent, created = Torrent.objects.get_or_create(
            info_hash=info_hash,
            defaults={"name": name},
        )

        # Create magnet URI
        magnet_uri = f"magnet:?xt=urn:btih:{info_hash}&dn={name}"

        return Response({"id": torrent.id, "created": created, "magneturi": magnet_uri})
