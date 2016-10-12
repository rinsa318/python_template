import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-2, 2, 0.1)
X, Y = np.meshgrid(x, y)

sigma = 2
# Z_exp = np.exp(-(X**2 + Y**2)/(2*sigma**2)) / (2*np.pi*sigma**2)
#Z = (-(X**2 + Y**2))
# ZZ = X + Y
# Z = np.exp(-(X))
# Z = np.sin(np.sqrt(X**2 + Y**2)) / np.sqrt(X**2 + Y**2)
Z = np.exp(-(X**2 + Y**2)/2)*(X**2 + Y**2) / 2*np.radians(180)
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
#ax.plot_surface(X, Y, ZZ, rstride=1, cstride=1, cmap=cm.coolwarm)
# ax.plot_wireframe(X, Y, Z_exp, rstride=2, cstride=2)
#ax.scatter(X, Y, Z_exp, s=1)
#ax.scatter(X, Y, ZZ, s=1)
#ax.scatter(X, Y, Z, s=1)

plt.show()



