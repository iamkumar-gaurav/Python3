# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc410797d4fe005c5e5623c2c1d4d609c'
auth_token = '35b526b23196ca8c3782cbd2c4d64c42'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!welcome to the hell',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+917250000246'
                          )

print(message.sid)
