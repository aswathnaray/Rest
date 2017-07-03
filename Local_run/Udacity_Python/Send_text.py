from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC88721a7d8bae5a7370df4e7e04980c9f"
# Your Auth Token from twilio.com/console
auth_token  = "3a77a307bbf4f4cf655d14e8565fdd72"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+32489466924",
    from_="+32460208467",
    body="Hello Bhave, this is an automated message from a python code!")

print(message.sid)