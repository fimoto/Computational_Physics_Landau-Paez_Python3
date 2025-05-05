""" From "COMPUTATIONAL PHYSICS: PROBLEM SOLVING with PYTHON"
    3rd Ed. by RH Landau, MJ Paez, and CC Bordeianu, 2015 """
# Updated for Python 3.10.17

from numpy import pi, sin, cos, mgrid
import matplotlib
#import mayavi
from mayavi import mlab

dphi , dtheta = pi /250.0 , pi /250.0
[phi , theta ] = mgrid [0: pi+dphi *1.5: dphi ,0:2* pi+dtheta *1.5: dtheta ]
m0 = 4; m1 = 3; m2 = 2; m3 = 3; m4 = 6; m5 = 2; m6 = 6; m7 = 4;
r = sin (m0*phi) **m1 + cos(m2*phi) **m3 + sin (m4*theta ) **m5 + cos(m6*theta ) **m7
x = r*sin (phi)*cos( theta ) ; y = r*cos(phi) # Function
z = r*sin (phi)*sin ( theta ) # Projections
# View data
s = mlab.mesh(x , y , z)
mlab.show()
