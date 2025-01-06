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
from .response import BencodeResponse


@require_http_methods(["GET", "POST"])
def announce_view(request: HttpRequest):
    # Get parameters for WebRTC or HTTP-based peer
    params = get_params(request)
    data = {
        "info_hash": urllib.parse.unquote_to_bytes(params["info_hash"]).hex(),
        "port": params.get("port"),
        "peer_id": params["peer_id"],
        "left": params["left"],
        "peer_ip": request.META.get("REMOTE_ADDR"),
    }

    if request.method == "POST":
        # Handle WebRTC signaling data
        data["sdp"] = params.get("sdp")
        data["candidate"] = params.get("candidate")

    # Validate request data
    serializer = AnnounceRequestSerializer(data=data)
    if not serializer.is_valid():
        return HttpResponse(serializer.error_messages, status=HTTPStatus.BAD_REQUEST)

    info_hash = serializer.validated_data["info_hash"]
    peer_id = serializer.validated_data["peer_id"]
    peer_ip = serializer.validated_data["peer_ip"]
    peer_port = serializer.validated_data["port"]
    left = serializer.validated_data["left"]

    is_seeding = left == 0

    # Fetch the torrent
    torrent = get_object_or_404(Torrent, info_hash=info_hash)

    # Update or create the peer
    peer_data = {
        "ip": peer_ip,
        "port": peer_port,
        "peer_id": peer_id,
        "is_seeding": is_seeding,
        "updated_at": now(),
    }
    if "sdp" in data:
        peer_data["sdp"] = data["sdp"]
    if "candidate" in data:
        peer_data["candidate"] = data["candidate"]

    Peer.objects.update_or_create(
        ip=peer_ip,
        torrent=torrent,
        defaults=peer_data,
    )

    # Remove stale peers
    timeout = now() - timedelta(seconds=settings.TORRENT_TIMEOUT)
    torrent.peers.filter(updated_at__lt=timeout).delete()

    seeds = torrent.peers.filter(is_seeding=True)
    leeches = torrent.peers.filter(is_seeding=False)

    # Select peers to return
    numwant = int(params.get("numwant", 50))
    selected_peers = torrent.peers.all()[:numwant]

    # Serialize selected peers
    peer_serializer = PeerSerializer(selected_peers, many=True)
    response_peers = []
    for peer in peer_serializer.data:
        peer_info = {
            "peer_id": peer["peer_id"],
            "ip": peer["ip"],
            "port": peer["port"],
        }
        if "sdp" in peer:
            peer_info["sdp"] = peer["sdp"]
        if "candidate" in peer:
            peer_info["candidate"] = peer["candidate"]
        response_peers.append(peer_info)

    response_data = {
        "interval": 60,
        "complete": seeds.count(),
        "incomplete": leeches.count(),
        "peers": response_peers,
    }

    if request.method == "GET":
        return BencodeResponse(response_data)
    elif request.method == "POST":
        return BencodeResponse({"status": "success", "message": "Peer updated or added."})


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
