from twilio.rest import Client
from datetime import datetime, timedelta
import time
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("Account_SID")    
auth_token = os.getenv("Auth_Token")
client = Client(account_sid, auth_token)

From = os.getenv("From_Twilio")

def send_message(resipient, msg):
    try:
        message = client.messages.create(
            from_=From,
            to=f'whatsapp:{resipient}',
            body=msg,
        )
        print(f"Message sent to {resipient}: {msg}")
        print(message.sid)
    except Exception as e:
        print(f"Error sending message: {e}")
        return None 
    

# main
name=input("Enter Recipient Name: ")
number=input("Enter Recipient Number with country code: ")
msg=input("Enter your message: ")
date_str=input("Enter date and time in format 'DD-MM-YYYY HH:MM': ")
date_time_obj = datetime.strptime(date_str, '%d-%m-%Y %H:%M')
current_time = datetime.now()
time_diff = (date_time_obj - current_time).total_seconds()
if time_diff > 0:
    print(f"Message will be sent to {name} at {date_time_obj}")
    time.sleep(time_diff)   

send_message(number, msg)

# message = client.messages.create(
#   from_='whatsapp:+14155238886',
#   content_sid='HXb5b62575e6e4ff6129ad7c8efe1f983e',
#   content_variables='{"1":"12/1","2":"3pm"}',
#   to='whatsapp:+918957756630'
# )
