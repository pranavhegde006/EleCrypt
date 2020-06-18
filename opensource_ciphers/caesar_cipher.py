print("\t\t  \t\t\tWelcome to one of the oldest ciphers in the world!!!")
print("\t\t\tWe do not recommend to encrypt your sensitive information using Caesar cipher")
print("Go ahead and Enjoy ;)")
case = int(input("If your plain text is all small letters, Enter \"0\" \nIf your plain text is all capital letters, Enter \"1\" "))
pl = input("Enter the plain text you want to encrypt: ")
plain = pl
key = int(input("Enter the shift key for Caesar encryption: "))
plli = []
cip = ""

for i in pl:
    plli.append(i)
def error():
    print("The cipher is case sensitive. Please enter all small or all capital letters only")

for j in range(len(plli)):
    plli[j] = int(ord(plli[j]))
    plli[j] = plli[j] + key
    if case == 0:
        plli[j] = (plli[j] % ord("a")) + ord("a")
    elif case == 1:
        plli[j] = (plli[j] % ord("A")) + ord("A")
    else:
        error()
    plli[j] = chr(plli[j])

cip = "".join(plli)
print("Your plain text was: ", plain)
print("Your cipher text is: ", cip)
