
import sys
import subprocess
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory, PNOperationType
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import os

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-ce7f4874-0d5e-11ec-9c1c-9adb7f1f2877"
pnconfig.publish_key = "pub-c-d8499027-383c-40de-8ae5-934f6ed366b8"
pnconfig.uuid = "myUniqueUUID"
pubnub = PubNub(pnconfig)

def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        pass  # Message successfully published to specified channel.
    else:
        print(status.is_error())
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];

class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data

    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            pass  # This event happens when radio / connectivity is lost

        elif status.category == PNStatusCategory.PNConnectedCategory:
            pass
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            #pubnub.publish().channel('pubnub_onboarding_channel').message('Hello world!').pn_async(my_publish_callback)
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.

    def message(self, pubnub, message):
        # Handle new message stored in message.message
        #print(message.message)
        pass



# Keep 'while True' and 'time.sleep()' if this script needs to loop
pubnub.add_listener(MySubscribeCallback())
fname = "/tmp/zoom.txt";

if not os.path.isfile(fname):
    f = open(fname,"w+")
    f.write("")
    f.close() 

f = open(fname,"r")
content =f.read()
f.close()

p1 = subprocess.Popen(["ps", "x"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["grep", "-E", "\-key [0-9]{9,10}"], stdin=p1.stdout, stdout=subprocess.PIPE)
p1.stdout.close()

output = p2.communicate()[0]
if output:
    code = output.split()[-1].decode()
    
    if output.decode("utf-8") != content:
        print("zoom_on:", str(code))
        f = open(fname,"w+")
        f.write(output.decode("utf-8"))
        f.close() 
        pubnub.publish().channel("pubnub_onboarding_channel").message("zoom_on").pn_async(my_publish_callback)
    
else:
    if output != content:
        print("zoom_off")
        f = open(fname,"w+")
        f.write(output.decode("utf-8"))
        f.close() 
        pubnub.publish().channel("pubnub_onboarding_channel").message("zoom_off").pn_async(my_publish_callback)


    