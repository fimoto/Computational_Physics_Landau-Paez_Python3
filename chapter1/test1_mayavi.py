""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

import numpy
import matplotlib
import mayavi
from mayavi import mlab

X, Y = numpy.mgrid[-2:2: 0.1, -2:2: 0.1]; Z = X**4 + Y**4

mayavi.mlab.surf(Z)
mayavi.mlab.axes()
mayavi.mlab.outline()
mayavi.mlab.show()
