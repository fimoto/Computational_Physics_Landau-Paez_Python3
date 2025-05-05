""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

import numpy
import mayavi
from mayavi import mlab

x, y , z = numpy.mgrid[-2:3, -2:3, -2:3]
r = numpy.sqrt(x ** 2 + y ** 2 + z ** 4)
u = y * numpy.sin(r) / (r + 0.001)
v = -x * numpy.sin(r) / (r + 0.001)
w = 4*numpy.zeros_like(z)
mayavi.mlab.quiver3d(x, y , z , u, v , w, line_width=3, scale_factor =1.5)
mayavi.mlab.show()
