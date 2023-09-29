from django.core.mail.backends.smtp import EmailBackend
from django.core.mail.message import EmailMessage
from apps.landing.models import EmailLog 
class DatabaseEmailBackend(EmailBackend):
    def send_messages(self, email_messages):
        """
        Save sent emails to the database before sending.
        """
        if not email_messages:
            return

        sent_messages = []
        for email_message in email_messages:
            # Save the email to the database
            email_log = EmailLog(
                subject=email_message.subject,
                message=email_message.body,
                from_email=email_message.from_email,
                recipient_list=','.join(email_message.recipients()),
            )
            email_log.save()

            # Append the email to the list of sent messages
            sent_messages.append(email_message)

        # Send the emails
        super().send_messages(sent_messages)
