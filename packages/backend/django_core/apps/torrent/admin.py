from django.contrib import admin

from .models import Torrent, Peer

# Register your models here.


@admin.register(Torrent)
class TorrentAdmin(admin.ModelAdmin[Torrent]):
    pass


@admin.register(Peer)
class PeerAdmin(admin.ModelAdmin[Peer]):
    pass
