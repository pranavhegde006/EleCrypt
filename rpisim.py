from functions import encrypt
from random import uniform
from time import sleep,ctime
from firebaseapp import firebaseapp
firebaseapp=firebaseapp

while(True):
    data = dict()
    data[ctime()] = encrypt(str(uniform(20,70)).format('.2f'))
    firebaseapp.post('/sensor1',data)
    sleep(1)
