from django.db import models
from mixins.models.created_at import CreatedAtMixin
from mixins.models.updated_at import UpdatedAtMixin

# Create your models here.


class Torrent(CreatedAtMixin):
    name = models.CharField(max_length=255)
    info_hash = models.CharField(unique=True)


class Peer(UpdatedAtMixin):
    ip = models.GenericIPAddressField()
    port = models.PositiveIntegerField()
    torrent = models.ForeignKey(Torrent, on_delete=models.CASCADE, related_name="peers")
    is_seeding = models.BooleanField(default=False)

    class Meta:
        unique_together = (
            "torrent",
            "ip",
            "port",
        )

    def __str__(self):
        return f"{self.ip}:{self.port} - {'Seeding' if self.is_seeding else 'Leeching'}"
