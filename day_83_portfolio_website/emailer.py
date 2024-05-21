import smtplib
from dotenv import load_dotenv
import os

class Emailer:
    def __init__(self):
        load_dotenv()
        self.SENDER = os.getenv("SENDER")
        self.SENDER_PW = os.getenv("SENDER_PW")
    
    def send_email(self, recipient, message):
        try:
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=self.SENDER, password=self.SENDER_PW)
                connection.sendmail(
                    from_addr=self.SENDER, 
                    to_addrs=recipient, 
                    msg=message
                )
            return True  # Email sent successfully
        except Exception as e:
            print(f"Error sending email: {e}")
            return False  # Failed to send email
