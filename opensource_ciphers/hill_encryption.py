import numpy as np 
import datetime
import random
time = datetime.datetime.now()



def enc(key):
    pl = 37.2547896123
    pl = str(pl)
    plli = []
    for i in range(len(pl)):
        plli.append(pl[i])
    plli.remove(".")
    if len(plli) %2 != 0:
        plli.append(str(0))
    plli = [plli[i:i + 2] for i in range(0, len(plli), 2)]
    i = 0; j = 0
    for i in range(len(plli)):
        for j in range(2):
            plli[i][j] = int(plli[i][j])
    i = 0; j = 0
    cip = []
    for i in range(len(plli)):
        cip.append(hill(key, plli[i])) 
    
    fin = []
    for i in range(len(cip)):
        fin.append(cip[i].tolist())

    print("The cipher text is: ", fin)


def hill(key, plain):
    temp = np.dot(key, plain)
    return temp


def getKey():
    key = [[time.hour, time.minute], [time.second, random.randint(10,100)]]
    print("The key is: ", key)
    check(key)

def check(x):
    if np.linalg.det(x) != 0:
        enc(x)
    else:
        getKey()
        

getKey()
