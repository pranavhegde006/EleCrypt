import datetime
import invert
import numpy as np

key = [[0]*3 for i in range(3)]
msg = [[0] for i in range(3)]
ciph = [[0] for i in range(3)]
rn = datetime.date.today()
time = datetime.datetime.now()
h = time.hour%12
m = time.minute
s = time.second
#print(rn.year,rn.month,rn.day)
d = {0: "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six",\
     7 : "seven", 8 : "eight", 9 :"nine", 10 :"ten", 11 : "eleven", 12 : "twelve"}
ls = [h,m,s]    #time list
ls = [d[x%12][:3:] for x in ls]
print(ls,time)

def HillCipher(message, key):
    message=message.replace('.',"")
    #print("message:",message)
    for i in range(3):
        msg[i][0] = (int(message[i])+97)% 97
    print("msg:",msg)
    print(key)
    for i in range(3):
        for j in range(1):
            ciph[i][j] = 0
            for k in range(3):
                #print(key[i][k],message[k][j])
                ciph[i][j] += (key[i][k]*msg[k][j])
            ciph[i][j] = ciph[i][j]% 26
    print(ciph)
    CipherText = []
    for i in range(3):
        CipherText.append(chr(ciph[i][0] + 65 + 32))

    # Finally print the ciphertext
    print("Ciphertext: ", "".join(CipherText))

for i in range(3):
    for j in range(3):
        key[i][j] = ord(ls[i][j])%97
print("key:",key)

if (invert.isInvertible(key, 3)):
    print("Invertible key matrix")
    HillCipher("60.8",key)  #encrypt 60.78 six zero seven zero
    #print("Inverse:",np.dot(key,np.linalg.inv(np.array(key))))
else:
    print("Not invertible")
