"""emailyer.py template"""

import smtplib
from email.message import EmailMessage


def send_email(subject: str, body: str, to: str, attachment: str = None):

    port_to_use = 587

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = "you@example.com"
    msg["To"] = to
    msg.set_content(body)

    if attachment:
        with open(attachment, "rb") as f:
            file_data = f.read()
            msg.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=attachment,
            )

    with smtplib.SMTP("smtp.example.com", port_to_use) as smtp:
        smtp.starttls()
        smtp.login("you@example.com", "yourpassword")
        smtp.send_message(msg)
