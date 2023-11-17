import smtplib
from dotenv import load_dotenv
import os

class NotificationManager:
    '''Sends notification email.'''
    def __init__(self):
        load_dotenv()
        # smtp variables
        self.FROM = os.environ.get("GMAIL_ADDR")
        self.KEY = os.environ.get("GMAIL_KEY")
        self.SERVER = 'smtp.gmail.com'
        self.PORT = 587

    def send_message(self, to_addrs: str, message: str):
        # message = message.encode("utf-8")
        with smtplib.SMTP(self.SERVER, port=self.PORT) as connection:
            connection.starttls()
            connection.login(user=self.FROM, password=self.KEY)
            connection.sendmail(
                from_addr=self.FROM, 
                to_addrs=to_addrs, 
                msg=f"Subject: Cheap Flight Alert\n\n{message}"
            )