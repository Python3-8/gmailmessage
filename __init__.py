from smtplib import SMTP_SSL
from email.message import EmailMessage
__name__ = 'gmailmessage'
__author__ = 'Pranav Balaji Pooruli'
__email__ = 'pranav.pooruli@gmail.com'
__version__ = '0.0.1'


class Client:
    def __init__(self, email_address, password_or_apppassword):
        self.email_address = email_address
        self.password_or_apppassword = password_or_apppassword


class Message:
    def __init__(self, client, subject, body):
        self.message = EmailMessage()
        self.message['Subject'] = subject
        self.message['From'] = client.email_address
        self.password = client.password_or_apppassword
        self.message.set_content(body)

    def send(self, to):
        self.message['To'] = to
        with SMTP_SSL('smtp.gmail.com', 465) as outgoing:
            outgoing.login(self.message['From'], self.password)
            outgoing.send_message(self.message)
