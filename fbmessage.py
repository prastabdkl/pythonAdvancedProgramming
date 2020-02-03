""" Hi Friends, Wish you a very happy new year.
I was thinking how to send the happy new year wishes to my all friend in facebook through a python code. Then I wrote the below code. Please note fb can apply a security check if you sending it randomly. 

I am not and no where responsible for any FB action for your activity around this.

step 1: Download your fb friendlist in a json format from face book.
step 2: keep the file in our local drive/ desktop

step 3: Change the path, email, password, message inside the code
step 4: Run it! have fun :)
```python
# pip install fbchat if you dont have it
from fbchat import Client
from fbchat.models import *
import json
# first give your email id and password
EMAIL = "xxxxxxxx"
PASSWORD = "xxxxxxx"
# path to your json file
file = r'path\friends.json'
# Open and load the json file and load the data into a dictionary
with open(file) as json_file:
    data = json.load(json_file)
    fl = {}
    for key, val in data.items():
        for each in val:
            for ke, va in each.items():
                if ke == 'name':       # Load only name field
                    fl.update({va:'t'}) # t is just taken to construct the dictionary
class Sendmsg:
    def __init__(self):
       pass
    def onmessage(self, email, password):
        self.email = email
        self.password = password
        # client object
        client = Client(self.email,self.password)
        for friendkey, friendval in fl.items():
            # search for user from your friend list
            user = client.searchForUsers(friendkey)
            # select the first option as facebook give your friend name in the first position
            friend = user[0]
            # Here you have the message
            msg = "Happy New Year 2020.\n" \
                  "Hope this year will be very special for you and your family.\n"\
                  "Cheers!"
            # Double check huh! I dont believe facebook :)
            if friend.is_friend == True:
                client.send(Message(text=msg), thread_id=friend.uid, thread_type=ThreadType.USER)
                # Confirm the name which is done
                print(friend.name)
        print("Done!")
if __name__ == "__main__":
    msg = Sendmsg()
    msg.onmessage(EMAIL, PASSWORD) """