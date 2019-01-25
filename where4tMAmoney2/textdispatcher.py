import os
import whitelist
import config

# Constants
text_from = whitelist.FROM
TWILIO_SID = config.TWILIO_SID
TWILIO_AUTH_TOKEN = config.TWILIO_AUTH_TOKEN

# Text recipients specified in textTo list
def text(bod, textTo):
	for recipient in textTo:
	    from twilio.rest import Client
	    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
	    message = client.messages.create(body=bod, from_=text_from, to=recipient)
	    print('Sent SMS to {}'.format(recipient))
