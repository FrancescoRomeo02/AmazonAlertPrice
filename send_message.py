from email import message
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

sid = os.environ.get('TWILIO_SID')
token = os.environ.get('TWILIO_TOKEN')

client = Client(sid, token)
message = client.messages.create(
    to='whatsapp:+393423380249', from_='whatsapp:+14155238886', body=sms)
