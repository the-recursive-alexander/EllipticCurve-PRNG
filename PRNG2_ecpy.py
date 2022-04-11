from ecpy.curves import Curve, Point
from tqdm import tqdm

domain = {'name': "P-163", 'size': 163, 'a': 3}

cv = Curve.get_curve('secp256k1')
P  = Point(0x65d5b8bf9ab1801c9f168d4815994ad35f1dcb6ae6c7a1a303966b677b813b00,
           0xe6b865e529b8ecbf71cf966e900477d49ced5846d7662dd2dd11ccd55c0aff7f,
           cv)
Q = Point(0x1cb2dc4d59b6714c9d96e3a5603b012f2d6df7e71ed10b77e5ebb11cf779b80d,
          0x20684258422ea9b73941ae0c224a578487de64cc17c94de29e62dffef2311381,
          cv)


f = open("./output/output2.data", 'w')
n = int(input("Print how many?: "))
for i in tqdm(range(n)):
    P = P + Q
    f.write(bin(P.x)[2:])
f.close()
