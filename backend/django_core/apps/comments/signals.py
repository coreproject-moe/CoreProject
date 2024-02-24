from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ReportedCommentModel

@receiver(post_save, sender=ReportedCommentModel)
def send_mail_on_report(sender, instance, created, **kwargs):
    print(instance)