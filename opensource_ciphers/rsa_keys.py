from math import gcd
from random import shuffle, choice
d = 0; e = 0; N = 0;

def prime(n):
    c = 0
    for k in range(2, n-1):
        if n%k == 0:
            c += 1
    if c == 0:
        return True
    else: 
        return False

def get_keys():
    p = int(input("Enter a prime number: "))
    if not prime(p):
        p = int(input("Please enter a correct prime number!! "))
    q = int(input("Enter another prime number: "))
    if not prime(q):
        q = int(input("Please enter a correct prime number!! "))
    global N
    N = p * q
    phi = (p-1) * (q-1)
    poss_e = []
    for i in range(1, phi+1):
        if gcd(phi, i) == 1:
            poss_e.append(i)
    shuffle(poss_e)
    global e
    e = choice(poss_e)

    poss_d = []
    for j in range(1, phi**2):
        if (e*j) % phi == 1: 
            poss_d.append(j)
    shuffle(poss_d)
    global d
    d = choice(poss_d)

    print("Your Public key is (", e, ", ", N, ")")
    print("Your Private key is (", d, ", ", N, ")")

get_keys()

