# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
from datetime import datetime
# Get these credentials from http://twilio.com/user/account
account_sid = "ACf73be3433473f2230edb17e2f6698287"
auth_token = "13bb02b173787324fa1505d3c499f93b"
client = TwilioRestClient(account_sid, auth_token)

# Make the call
called = client.calls.create(to="+917048733848",  # Any phone number
                           from_="+14702261683", # Must be a valid Twilio number
                           url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

sid = called.sid
value = client.calls.list(call=sid)
for i in value:
	print i.status
