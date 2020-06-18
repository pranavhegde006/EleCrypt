from rsa_keys import get_keys, d , e, N
pl = input("Enter the plain text you want to encrypt: ")

def rsa_encrypt():
    e = 5
    N = 14
    cip_li = []
    for i in range(len(pl)):        
        cip_li.append(ord(pl[i])-ord("A")+1)
        cip_li[i] = pow(cip_li[i], e, N)
        cip_li[i] += ord("A")
        cip_li[i] -= 1
        cip_li[i] = chr(cip_li[i])
    print(cip_li)

    
rsa_encrypt()