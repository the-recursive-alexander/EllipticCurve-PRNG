from ecpy.curves import Curve, Point
from tqdm import tqdm

"""
points:

Point(0x2a38c67e5a4335b98b612168e3a5ca7cd83e0cac75990d4e2ce1e3cb609096a8, 0xd82e4cff94ecf334547cdd2de8d98976a7f5d8ce9c433b8265e34459ba429484, cv)
Point(0x73c0af56e81d6900e408ab06598008e5d038d1f00a1f6182b6616605862fcde6, 0xb99d6dd0efa748785c67da2381325cf6919e30e7376d1003bf31f9ec21435300, cv)
Point(0xc07de9de3132d2ea578ad40bd1bf9ef80aa349c2f07a11595d05da08d39e7c48, 0x34f9dce2ab5d8e6e6e8face59d6173989151dc57979e2b834119b699de3fc46f, cv)
Point(0x78868d1adada46e7d962887b5c04cc24295f0d9e901fc0454d657ac573446b49, 0x42e8e946abbb563a4e67805b3fc541a034385bdf58123f47731195286063d73c, cv)
Point(0x846bc549bf3a1094126313fa0f48e255e007a78d6f9d8292aa725e998313fa8f, 0x4248efbc0f8b6049ae8d2af2854f83194f8c7fd67b6b551ed9c87637d64c110, cv)
Point(0x3c2907dfb65672f81e7a0c9de8e469bfce1d1dd44599c18697456e221a9e5a78, 0xc27b82ee414d00e2af84834e4f0dc9f90a28c72273f07b24c43825b98c3ac203, cv)
Point(0xb63754f6af87855c24032a1f3e1ed4f272974f24dae1b5441a5e479ef17c1535, 0x6d621e62732f0b16b4f996691f764814f6e5535b0f469eff7bb5098e58fd63c6, cv)
Point(0x8507f36e74f9727672016fd7d78a63b57113c979cc6f0debbe14f4b6a6276603, 0x73b0b2d48bb0f86478e833df77f0c83436586e4dcdcb2b1a211e1f507496b7d7, cv)
Point(0xc3d79ee93e925531179c9b7ac43ffc139b8b4469a44f3a2f950aa3027a1011fd, 0xbd24a5e68910d66056f99ebc5b76c1c27955e67400235906ac6344c27c931c88, cv)
Point(0x2bc646d34bf8a00731411c7f41f7d400be3e8cf0f159825c0ad7431eb832bdf, 0x740c051c505b5e452fb77c5643412a229a26d3d044e877621bb094dbd09c90d8, cv)

k = 0xfb26a4e75eec75544c0f44e937dcf5ee6355c7176600b9688c667e5c283b43c5
k = 0xab7a7a5e00e7a4a2c0c61f3dbc968153fd14338dfab58373cfd90187afc34758
k = 0xcd6283bedfac3856076252febcde244648d392a43cb9302edaf2c3648bce92dc
k = 0x3830dfba34047a7db39dcae2748be940a8d727592ce8dfb8b37afecd12309acd
k = 0x37adf3b7373cfedab47258dfeac4637d6d8f66a6e56c7b86f7d6e66a776c78f7
k = 0x77a778d777e77cf88b8f8d7d7dd6d5c44a3ad3f3c3dfcb43483726654a4345c7
k = 0x098a7657d6c7b865e4f4a32457c67b6f7d6e7c76a78f8e7dd654a5f7b8161aae
k = 0xb2f2edc51da6f7c8b7203847571fed1c38598acb5895736fdecdaf3618790893
k = 0xbdfec4611738568927164facedb2859018587adefc26457edfc13748afe0bcfd
k = 0x1237567df84903abf8388c7368fbe710adc7832229fbea74dcedf00493822283

"""



domain = {'name': "P-163", 'size': 163, 'a': 3}

cv = Curve.get_curve('secp256k1')
P  = Point(0x2a38c67e5a4335b98b612168e3a5ca7cd83e0cac75990d4e2ce1e3cb609096a8, 0xd82e4cff94ecf334547cdd2de8d98976a7f5d8ce9c433b8265e34459ba429484, cv)
"""
Point(0x65d5b8bf9ab1801c9f168d4815994ad35f1dcb6ae6c7a1a303966b677b813b00,
           0xe6b865e529b8ecbf71cf966e900477d49ced5846d7662dd2dd11ccd55c0aff7f,
           cv)
"""

Q = Point(0x73c0af56e81d6900e408ab06598008e5d038d1f00a1f6182b6616605862fcde6, 0xb99d6dd0efa748785c67da2381325cf6919e30e7376d1003bf31f9ec21435300, cv)
"""
Point(0x1cb2dc4d59b6714c9d96e3a5603b012f2d6df7e71ed10b77e5ebb11cf779b80d,
          0x20684258422ea9b73941ae0c224a578487de64cc17c94de29e62dffef2311381,
          cv)
"""

f = open("./output/output2.data", 'w')
n = int(input("Print how many?: "))
for i in tqdm(range(n)):
    P = P + Q
    f.write(bin(P.x)[2:])
f.close()
