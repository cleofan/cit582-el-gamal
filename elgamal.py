import random


from params import p
from params import g

def keygen():
    sk = 0
    pk = 0
    sk = random.randint(1, (p-1)/2)
    pk = pow(g, sk, mod = p)
    return pk,sk

def encrypt(pk,m):
    c1 = 0
    c2 = 0
    r = random.randint(1, (p-1)/2)
    c1 = pow(g,r, mod = p)
    c2 = pow(pow(pk,r,mod = p) * pow(m, 1, mod = p), 1, mod = p)
    return [c1,c2]

def decrypt(sk,c):
    m = 0
    x = pow(c[0], p-1-sk, mod = p)
    c2 = pow(c[1], 1, mod = p)
    m = pow(x * c2, 1, mod = p)
    return m

