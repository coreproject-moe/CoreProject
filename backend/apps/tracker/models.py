from django.contrib.auth import get_user_model
from django.db import models

# Create your models here.


class MalModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    access_token = models.CharField(max_length=1024, null=True, blank=True)
    expires_in = models.DurationField(null=True, blank=True)
    refresh_token = models.CharField(max_length=1024, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)


class KitsuModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    access_token = models.CharField(max_length=64, null=True, blank=True)
    expires_in = models.DurationField(null=True, blank=True)
    refresh_token = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)


class AnilistModel(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    access_token = models.CharField(max_length=64, null=True, blank=True)
    expires_in = models.DurationField(null=True, blank=True)
    refresh_token = models.CharField(max_length=64, null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
