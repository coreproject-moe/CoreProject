from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import ReportedCommentModel
from ..user.models import CustomUser

@receiver(post_save, sender=ReportedCommentModel)
def send_mail_on_report(sender, instance, created, **kwargs):
    # Send mail to admins
    if created:
        # admin_users = CustomUser.objects.filter(is_superuser=True)
        # for user in admin_users:
        #     send_mail(user.email)
        pass