cip_li = ['D']
def rsa_decrypt(cip_li):
    d = 11
    N = 14
    pl_li = []
    for i in range(len(cip_li)):
        pl_li.append(cip_li[i])
        pl_li[i] = ord(pl_li[i]) - ord("A") + 1
        pl_li[i] = pow(pl_li[i], d, N)
        pl_li[i] = pl_li[i] -1 + ord("A")
        pl_li[i] = chr(pl_li[i])
    print(pl_li)

rsa_decrypt(cip_li)