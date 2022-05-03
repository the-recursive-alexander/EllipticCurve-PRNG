import sys
sys.path.insert(0, './lib')

from point import *
from ec import *
from modarith import *

import matplotlib.pyplot as plt
import numpy as np

BACKGROUND = False
A = 3
B = 2
P = 79
slope = 2/3


if(BACKGROUND):
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    im = plt.imread("../Capture.PNG")
    fig, ax = plt.subplots()
    im = ax.imshow(im, extent=[-5, 5, -5, 5])
    ax.grid(False)
y, x = np.ogrid[-5:5:100j, -5:5:100j]
xl = np.arange(-5, 5, 0.05)
yl = slope * xl
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) + x * 2 - 0, [0], colors = "blue")

plt.plot(xl, yl, color="red")

yl2 = np.arange(-5, 5, 0.05)
xl2 = np.empty(len(yl2))
for i in range(len(yl2)):
    xl2[i] = 1.65

plt.plot(xl2, yl2, color="green")

xpoints = np.array([-1.22, 0, 1.65, 1.65])
ypoints = np.array([-0.82, 0, 1.11, -1.11])
plt.scatter(xpoints, ypoints, color = "red")
plt.show()



curEC = EC(A, B)
Field.m = P
points = curEC.points()[1:]

x = []
y = []
for point in points:
    x.append(point.x.val)
    y.append(point.y.val)

X = np.array(x)
Y = np.array(y)

plt.scatter(X, Y)
plt.show()