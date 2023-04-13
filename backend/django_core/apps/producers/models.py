from django.db import models

# Create your models here.


class ProducerModel(models.Model):
    mal_id = models.IntegerField(unique=True, blank=True, null=True)
    kitsu_id = models.IntegerField(unique=True, blank=True, null=True)
    name = models.CharField(
        max_length=128,
        default="",
        null=False,
        blank=False,
    )
    # Titles
    default_title = models.CharField(
        max_length=128,
        default="",
        null=True,
        blank=True,
    )
    japanese_title = models.CharField(
        max_length=128,
        default="",
        null=True,
        blank=True,
    )
    established = models.DateTimeField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)

    # Timestamp field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.pk}. {self.name} | Mal_id : {self.mal_id}"

    class Meta:
        verbose_name = "Producer"
        verbose_name_plural = "Producers"
