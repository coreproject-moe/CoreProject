from django.db import models
from mixins.models.created_at import CreatedAtMixin
from mixins.models.updated_at import UpdatedAtMixin

# Create your models here.


class Torrent(CreatedAtMixin):
    name = models.TextField()
    info_hash = models.CharField(unique=True)


class Peer(UpdatedAtMixin):
    ip = models.GenericIPAddressField()
    port = models.PositiveIntegerField()
    torrent = models.ForeignKey(Torrent, on_delete=models.CASCADE, related_name="peers")
    is_seeding = models.BooleanField()
    peer_id = models.TextField()
    sdp = models.TextField(null=True, blank=True)
    candidate = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = (
            "torrent",
            "ip",
            "port",
            "peer_id",
        )

    def __str__(self):
        return f"{self.ip}:{self.port} - {self.peer_id} - {'Seeding' if self.is_seeding else 'Leeching'}"
