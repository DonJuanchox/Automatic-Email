import os
import imaplib
import smtplib
from email.message import EmailMessage

class Email_Access:
    """
    This class encapsulates email functionality using IMAP for reading emails
    and SMTP for sending emails.
    """

    def __init__(self, imap_server, smtp_server, email_user, email_pass):
        self.imap_server = imap_server
        self.smtp_server = smtp_server
        self.email_user = email_user
        self.email_pass = email_pass

    def send_email(self, to_address, subject, body, attachment_paths=None, html_body=False, cc_address=None):
        """
        Send an email using SMTP (Gmail settings).
        """
        msg = EmailMessage()
        msg["From"] = self.email_user
        msg["To"] = to_address
        if cc_address:
            msg["Cc"] = cc_address
        msg["Subject"] = subject

        if html_body:
            msg.add_alternative(body, subtype="html")
        else:
            msg.set_content(body)

        # Attach files if provided
        if attachment_paths:
            for attachment in attachment_paths:
                with open(attachment, "rb") as f:
                    msg.add_attachment(f.read(), filename=os.path.basename(attachment))

        # Connect to SMTP server (Gmail requires STARTTLS)
        with smtplib.SMTP(self.smtp_server, 587) as server:
            server.starttls()  # Secure the connection
            server.login(self.email_user, self.email_pass)
            server.send_message(msg)
