from django.core.mail import send_mail
from asgiref.sync import sync_to_async


@sync_to_async
def send_mail_function(
    email_subject: str, email_reset_message: str, from_sender: str, to_receiver: str
) -> None:
    send_mail(
        email_subject,  # subject
        email_reset_message,  # message
        from_sender,  # from email
        [to_receiver],  # to email
    )
