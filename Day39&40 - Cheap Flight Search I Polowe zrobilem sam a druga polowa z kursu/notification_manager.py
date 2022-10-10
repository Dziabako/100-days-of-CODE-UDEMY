# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
import smtplib

# To jest do twilio
account_sid = "AC4d1a0b54cc08ca9c1bc68f0295a9906a"
auth_token = "875812ca149039517660b28358ae5235"

# Gmail
my_email = "dawidtest315@gmail.com"
password = "ahbzwewvvugqmmig"


class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_message(self, message):
        text_message = self.client.messages.create(
            body=message,
            from_='+48732106918',
            to='+48666532414'
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
                to_addrs="dawidtest@yahoo.com",
                msg=f"Subject:Flight Alert!\n{message}"
            )
