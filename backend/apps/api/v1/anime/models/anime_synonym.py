from django.db import models

# Create your models here.


class AnimeSynonymModel(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta:
        verbose_name = "Anime Synonym"
