from ecpy.curves import Curve, Point
from tqdm import tqdm

domain = {'name': "P-163", 'size': 163, 'a': 3}

cv = Curve.get_curve('secp256k1')
P  = Point(0x65d5b8bf9ab1801c9f168d4815994ad35f1dcb6ae6c7a1a303966b677b813b00,
           0xe6b865e529b8ecbf71cf966e900477d49ced5846d7662dd2dd11ccd55c0aff7f,
           cv)
k  = 0xfb26a4e75eec75544c0f44e937dcf5ee6355c7176600b9688c667e5c283b43c5

def kPModule(k, P):
    return k*P

def newK(P, n):
    return (P.x + n) % P.curve.field

f = open("./output/output1.data", 'w')
n = int(input("Print how many?: "))
for i in tqdm(range(n)):
    P = kPModule(k, P)
    f.write(bin(P.x)[2:])
    k = newK(P, i)
f.close()
