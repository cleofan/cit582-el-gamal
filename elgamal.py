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
    a = m * pow(pk,r)
    c2 = pow(a, 1, mod = p)
    return [c1,c2]

def decrypt(sk,c):
    m = 0
    return m

