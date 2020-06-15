from smtpgmail import Client, Message
googleuser = Client('pranav.pooruli@gmail.com', 'N/A')
message = Message(googleuser, 'Subject', 'Body')
message.send('pranav.pooruli@gmail.com')
