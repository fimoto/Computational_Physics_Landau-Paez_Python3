""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

# List 1.8 Simple3Dplot.py

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

print("Please be patient , I have packages to import & points to plot")
delta = 0.1
x = np.arange(-3. , 3. , delta )
y = np.arange(-3. , 3. , delta )
X, Y = np.meshgrid(x, y)
Z = np.sin(X) *np.cos(Y)

fig = plt.figure()
ax = Axes3D(fig)
fig.add_axes(ax) # added here
ax.plot_surface(X,Y,Z)
ax.plot_wireframe(X,Y,Z, color = 'r')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
