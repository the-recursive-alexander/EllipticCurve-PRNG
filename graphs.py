import matplotlib.pyplot as plt
import numpy as np

A = -2
B = 1
slope = 2/3

y, x = np.ogrid[-5:5:100j, -5:5:100j]
xl = np.arange(-5, 5, 0.05)
yl = slope * xl
plt.contour(x.ravel(), y.ravel(), pow(y, 2) - pow(x, 3) - x * A - B, [0])
plt.grid()
plt.plot(xl, yl)
plt.show()