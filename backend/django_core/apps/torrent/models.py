from django.db import models
from mixins.models.created_at import CreatedAtMixin

# Create your models here.


class Torrent(CreatedAtMixin):
    name = models.CharField(max_length=255)
    info_hash = models.CharField(max_length=40, unique=True)


class Peer(models.Model):
    ip = models.GenericIPAddressField()
    port = models.PositiveIntegerField()
    torrent = models.ForeignKey(Torrent, on_delete=models.CASCADE, related_name="peers")
    last_seen = models.DateTimeField(auto_now=True)
