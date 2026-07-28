import os
import smtplib

from email.message import EmailMessage
from dotenv import load_dotenv


def SendMail(receiver, subject, body, filename):

    load_dotenv()

    sender = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    msg = EmailMessage()

    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject

    msg.set_content(body)

    with open(filename, "rb") as f:

        file_data = f.read()
        file_name = os.path.basename(filename)

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name
    )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    smtp.login(sender, app_password)

    smtp.send_message(msg)

    smtp.quit()

    print("Mail Sent Successfully")