from django.db import models

# Create your models here.


class CharacterLogModel(models.Model):
    log_dictionary = models.JSONField()
    logs = models.TextField()
