# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import smtplib

# To jest do twilio
account_sid = "ACCOUNT SID"
auth_token = "AUTH TOKEN"

# Gmail
my_email = "mail@gmail.com"
password = "password"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        text_message = self.client.messages.create(
            body=message,
            from_='number',
            to='number'
        )
        # Sprawdzanie czy zostalo wyslane pomyslnie
        print(text_message.sid)

    @staticmethod
    def send_emails(message):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="mail@yahoo.com",
                msg=f"Subject:Flight Alert!\n{message}"
            )
