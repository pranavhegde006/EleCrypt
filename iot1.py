from time import ctime
import time
import random
from encrypt1 import encrypt
from firebase import firebase
firebase = firebase.FirebaseApplication("https://iot-proj-1-bbf47.firebaseio.com/sensor1")
while(True):
    data = dict()
    data[ctime()] = encrypt(round(random.uniform(20,70),3))
    print(f"Sending {data}")
    firebase.post('/sensor_1',data)
    time.sleep(1)
