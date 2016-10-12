import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm


fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = y = np.arange(-3, 3, 0.1)
X, Y = np.meshgrid(x, y)

sigma = 2
#Z = np.exp(-(X**2 + Y**2)/(2*sigma**2)) / (2*np.pi*sigma**2)
#Z = (-(X**2 + Y**2))
ZZ = X + Y
Z = np.exp(-(X))

#ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm)
ax.plot_surface(X, Y, ZZ, rstride=1, cstride=1, cmap=cm.coolwarm)
ax.plot_wireframe(X, Y, Z, rstride=2, cstride=2)
ax.scatter(X, Y, Z, s=1)

plt.show()

# print("I'm studying about git by using SourceTree")
# print("I'm studying about git by using SourceTree2")

# a = 1
# b = 1
# for i in range(100):

# 	print("addition" + str(a))

# 	a += i

# 	print("multiplication" + str(b))

# 	if i==0:
# 		continue
	
# 	else:
# 		b *= i


