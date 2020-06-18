import math
import datetime

def crypt():
    val = float(input("Enter your plain text: "))
    key = datetime.datetime.now()
    key = key.second
    print("Your key is: ", key)
    cip = math.tan(math.radians(val))
    cip = pow(cip, key)
    print("The cipher text is: ", cip)

def decrypt():
    cry = float(input("Enter the cipher text for decryption: "))
    keyd = int(input("Enter your key for decryption: "))
    mes = pow(cry, 1/keyd)
    mes = math.atan(mes)
    print(math.degrees(mes))

crypt()
decrypt()