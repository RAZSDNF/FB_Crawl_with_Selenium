from fbchat import Client
import time
from fbchat.models import *
client = Client('xxxxx', 'xxxxxxx')
while(True):
    time.sleep(5)
    print("Sending Message")
    sent=client.send(Message(text="Found Something"), thread_id="user_id_of_receiver", thread_type=ThreadType.USER)
    if sent:
        print("Message sent successfully!")
