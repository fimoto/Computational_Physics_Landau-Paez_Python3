""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

import numpy as np
import mayavi
from mayavi import mlab

x, y , z = np.ogrid[ -10:10:20j, -10:10:20j, -10:10:20j ]
scalar = np.sin(x*y*z) /(x*y*z)
mlab.contour3d ( scalar )
mlab.show()
